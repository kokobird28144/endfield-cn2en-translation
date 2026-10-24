"""Exercise bundled dictionaries, custom data and standalone installation."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "endfield-cn2en-translation"
SCRIPT = SKILL / "scripts" / "lookup_terms.py"
EXAMPLES = ROOT / "examples" / "data"


class LookupTests(unittest.TestCase):
    def run_cli(self, *args: str, script: Path = SCRIPT,
                cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, "-B", str(script), *args],
                              cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", timeout=15,
                              env={**os.environ, "PYTHONIOENCODING": "utf-8"})

    def example(self, query: str, *args: str) -> subprocess.CompletedProcess[str]:
        return self.run_cli(query, "--data-dir", str(EXAMPLES), "--json", *args)

    def parse_success(self, result: subprocess.CompletedProcess[str]) -> list[dict]:
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_chinese_exact_and_int64_string(self) -> None:
        rows = self.parse_success(self.example("演示矿", "--exact"))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["name_id"], "9223372036854775807")

    def test_casefold_english(self) -> None:
        rows = self.parse_success(self.example("demo ore", "--exact"))
        self.assertEqual(rows[0]["zh"], "演示矿")

    def test_ids_and_aliases(self) -> None:
        for query in ("demo_ore", "9223372036854775807", "样矿"):
            with self.subTest(query=query):
                self.assertEqual(len(self.parse_success(self.example(query, "--exact"))), 1)

    def test_exact_does_not_match_partial(self) -> None:
        self.assertEqual(self.parse_success(self.example("Demo", "--exact")), [])

    def test_alias_keeps_tentative_status(self) -> None:
        rows = self.parse_success(self.example("小样", "--scope", "aliases"))
        self.assertEqual(rows[0]["meaning_status"], "user-suggested")
        self.assertEqual(rows[0]["record_source"], "user-suggested-alias")

    def test_official_does_not_upgrade_evidence(self) -> None:
        rows = self.parse_success(self.example("Demo Hub", "--scope", "official"))
        self.assertEqual(rows[0]["status"], "fictional-example")

    def test_all_scopes(self) -> None:
        rows = self.parse_success(self.example("Demo", "--scope", "all"))
        self.assertEqual({r["record_source"] for r in rows},
                         {"game", "verified-name", "user-suggested-alias"})

    def test_no_match_is_empty_array(self) -> None:
        self.assertEqual(self.parse_success(self.example("unmatched-test-term")), [])

    def test_empty_query_is_error(self) -> None:
        result = self.example("   ")
        self.assertEqual(result.returncode, 2)
        self.assertIn("query must not be empty", result.stderr)

    def test_default_uses_bundled_game_dictionary(self) -> None:
        result = self.run_cli("壤晶", "--json", "--exact")
        rows = self.parse_success(result)
        self.assertTrue(rows)
        self.assertTrue(all(row["en"] == "Xircon" for row in rows))
        self.assertEqual(result.stderr, "")

    def test_default_alias_keeps_both_candidates(self) -> None:
        rows = self.parse_success(self.run_cli("小药", "--scope", "aliases", "--json"))
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]["targets"]), 2)
        self.assertEqual(rows[0]["meaning_status"], "user-confirmed")

    def test_default_tentative_alias_stays_tentative(self) -> None:
        rows = self.parse_success(self.run_cli("土豆苔", "--scope", "aliases", "--json"))
        self.assertEqual(rows[0]["meaning_status"], "user-suggested")

    def test_default_official_dictionary(self) -> None:
        rows = self.parse_success(self.run_cli("帝江号", "--scope", "official", "--json"))
        self.assertTrue(rows)
        self.assertNotEqual(rows[0]["status"], "fictional-example")

    def test_default_all_has_no_missing_files(self) -> None:
        result = self.run_cli("Xircon", "--scope", "all", "--json")
        self.assertTrue(self.parse_success(result))
        self.assertEqual(result.stderr, "")

    def test_explicit_empty_directory_does_not_use_bundled_data(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli("壤晶", "--data-dir", temp, "--json")
            self.assertEqual(result.returncode, 2)
            self.assertIn("Missing local data", result.stderr)

    def test_missing_all_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli("Demo", "--scope", "all", "--data-dir", temp, "--json")
            self.assertEqual(result.returncode, 2)
            self.assertIn("No selected local dictionaries", result.stderr)

    def test_aliases_work_without_csv_or_official(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            shutil.copy2(EXAMPLES / "community-aliases.json", temp)
            result = self.run_cli("小样", "--scope", "aliases", "--data-dir", temp, "--json")
            self.assertEqual(len(self.parse_success(result)), 1)
            self.assertEqual(result.stderr, "")
            result = self.run_cli("小样", "--scope", "all", "--data-dir", temp, "--json")
            self.assertEqual(len(self.parse_success(result)), 1)
            self.assertIn("Missing local data", result.stderr)

    def test_standalone_bundled_data_without_original_project(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "endfield-cn2en-translation"
            shutil.copytree(SKILL, installed)
            for query, scope in (("壤晶", "game"), ("小药", "aliases"), ("帝江号", "official")):
                with self.subTest(scope=scope):
                    result = self.run_cli(query, "--scope", scope, "--json",
                                          script=installed / "scripts" / "lookup_terms.py",
                                          cwd=Path(temp))
                    self.assertTrue(self.parse_success(result))
                    self.assertEqual(result.stderr, "")

    def test_selected_scope_ignores_unrelated_corrupt_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            shutil.copy2(EXAMPLES / "official-names.json", temp)
            (Path(temp) / "game-terms.csv").write_text("broken", encoding="utf-8")
            result = self.run_cli("Demo Hub", "--scope", "official", "--data-dir", temp, "--json")
            self.assertEqual(len(self.parse_success(result)), 1)

    def test_corrupt_selected_json_is_error(self) -> None:
        for content in ("{", '{"records":[42]}',
                        '{"records":[{"zh":"Demo","en":"Demo","version":"1","status":false}]}'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                (Path(temp) / "official-names.json").write_text(content, encoding="utf-8")
                result = self.run_cli("Demo", "--scope", "official", "--data-dir", temp, "--json")
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_numeric_json_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            data = json.loads((EXAMPLES / "official-names.json").read_text(encoding="utf-8"))
            data["records"][0]["name_id"] = 9223372036854775807
            (Path(temp) / "official-names.json").write_text(json.dumps(data), encoding="utf-8")
            result = self.run_cli("Demo", "--scope", "official", "--data-dir", temp)
            self.assertEqual(result.returncode, 2)
            self.assertIn("keep IDs as strings", result.stderr)

    def test_malformed_csv_is_error(self) -> None:
        for content in ("zh,en\nDemo,Demo\n", (EXAMPLES / "game-terms.csv").read_text(encoding="utf-8") + "extra\n"):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                (Path(temp) / "game-terms.csv").write_text(content, encoding="utf-8")
                result = self.run_cli("Demo", "--data-dir", temp)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)

    def test_bom_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            text = (EXAMPLES / "game-terms.csv").read_text(encoding="utf-8")
            (Path(temp) / "game-terms.csv").write_text(text, encoding="utf-8-sig")
            result = self.run_cli("演示矿", "--data-dir", temp, "--json")
            self.assertEqual(len(self.parse_success(result)), 1)

    def test_standalone_install_from_different_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "endfield-cn2en-translation"
            shutil.copytree(SKILL, installed)
            shutil.copy2(EXAMPLES / "community-aliases.json", installed / "data")
            result = self.run_cli("小样", "--scope", "aliases", "--json",
                                  script=installed / "scripts" / "lookup_terms.py",
                                  cwd=Path(temp))
            self.assertEqual(len(self.parse_success(result)), 1)


if __name__ == "__main__":
    unittest.main()
