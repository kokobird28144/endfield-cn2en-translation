#!/usr/bin/env python3
"""Check the release file allowlist, local links and obvious private artifacts."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    manifest = json.loads((ROOT / "release-manifest.json").read_text(encoding="utf-8"))
    listed = manifest["files"]
    errors: list[str] = []
    if len(listed) != len(set(listed)):
        errors.append("duplicate paths in manifest")
    for name in listed:
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or path.as_posix() != name:
            errors.append(f"invalid manifest path: {name}")
    paths = [p for p in ROOT.rglob("*") if ".git" not in p.relative_to(ROOT).parts]
    for path in paths:
        if path.is_symlink():
            errors.append(f"symlink is not allowed: {path.relative_to(ROOT)}")
    actual = {p.relative_to(ROOT).as_posix() for p in paths if p.is_file()}
    expected = set(listed)
    for name in sorted(actual - expected):
        errors.append(f"unlisted file: {name}")
    for name in sorted(expected - actual):
        errors.append(f"missing file: {name}")

    patterns = {
        "machine path": re.compile(r"(?<![A-Za-z])(?:[A-Za-z]:[\\/](?!/)|/(?:Users|home)/)"),
        "loopback address": re.compile(r"127[.]0[.]0[.]1|localhost:[0-9]+"),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "common secret prefix": re.compile(r"(?:ghp_|github_pat_|sk-proj-|AKIA)[A-Za-z0-9_]{12,}"),
        "signed URL": re.compile(r"[?&](?:token|access_token|auth|signature|sig)=[^\s)]+", re.I),
    }
    checked_links = 0
    for name in sorted(actual & expected):
        path = ROOT / name
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"not UTF-8 text: {name}")
            continue
        if any(ord(char) < 32 and char not in "\t\n\r" for char in text):
            errors.append(f"unexpected control character: {name}")
        for label, pattern in patterns.items():
            if pattern.search(text):
                errors.append(f"{label} detected: {name}")
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=name, feature_version=(3, 10))
            except SyntaxError as error:
                errors.append(f"Python 3.10 syntax: {name}: {error}")
        if path.suffix == ".json":
            try:
                json.loads(text)
            except ValueError as error:
                errors.append(f"invalid JSON: {name}: {error}")
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(ROOT):
                errors.append(f"link outside release: {name}: {target}")
            elif not dest.exists():
                errors.append(f"missing local link: {name}: {target}")
            checked_links += 1

    entry = ROOT / "skills" / "endfield-cn2en-translation" / "SKILL.md"
    text = entry.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append("SKILL frontmatter is missing")
    else:
        fields = dict(re.findall(r"^([a-z_]+): ([^\n]+)$", parts[1], re.M))
        if fields.get("name") != entry.parent.name or fields.get("license") != "MIT":
            errors.append("SKILL name/license mismatch")
        if not fields.get("description", "").strip():
            errors.append("SKILL description is empty")
    if manifest.get("license") != "MIT":
        errors.append("manifest license mismatch")
    refs = entry.parent / "references"
    bundled = manifest.get("bundled_data", {})
    try:
        with (refs / "game-terms.csv").open(encoding="utf-8-sig", newline="") as stream:
            game = list(csv.DictReader(stream))
        aliases = json.loads((refs / "community-aliases.json").read_text(encoding="utf-8"))["records"]
        official = json.loads((refs / "official-names.json").read_text(encoding="utf-8"))["records"]
        interface = json.loads((refs / "interface-terms-1.6.4.json").read_text(encoding="utf-8"))
        sizes = {"game_records": len(game), "alias_records": len(aliases),
                 "official_records": len(official), "interface_records": len(interface)}
        for key, value in sizes.items():
            if bundled.get(key) != value:
                errors.append(f"bundled count mismatch: {key}: {value}")
        versions = {version: sum(row["version"] == version for row in game)
                    for version in {row["version"] for row in game}}
        if versions != bundled.get("game_versions"):
            errors.append("game version count mismatch")
        for filename, expected_hash in bundled.get("preserved_file_sha256", {}).items():
            if hashlib.sha256((refs / filename).read_bytes()).hexdigest() != expected_hash:
                errors.append(f"preserved reference hash mismatch: {filename}")
        for row in game:
            if not all(row.get(key) for key in ("zh", "en", "version", "status")):
                errors.append("game record missing name, version or status")
            if row["name_id"] and not re.fullmatch(r"-?[0-9]+", row["name_id"]):
                errors.append("game name_id is not an integer string")
        for row in aliases:
            if "context_pages" in row:
                errors.append("alias still contains source-page bindings")
            if row.get("meaning_status") not in ("user-confirmed", "user-suggested"):
                errors.append("alias confirmation status missing")
        for filename, count_key in (("production-terms.md", "production_terms"),
                                    ("community-slang.md", "slang_terms")):
            lines = (refs / filename).read_text(encoding="utf-8").splitlines()
            rows = [line for line in lines if line.startswith("|")
                    and line.split("|")[1].strip() not in ("---", "中文", "玩家用语")]
            if len(rows) != bundled.get(count_key):
                errors.append(f"terminology count mismatch: {filename}: {len(rows)}")
        excluded = ("document-translation.md", "translation-review-issues.md")
        for name in actual:
            if Path(name).name in excluded:
                errors.append(f"project-specific registry included: {name}")
        for path in refs.iterdir():
            if path.is_file() and re.search(r"src/page-[A-Za-z0-9]+", path.read_text(encoding="utf-8-sig")):
                errors.append(f"source-page binding included: {path.name}")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"cannot validate bundled data: {error}")
    if errors:
        print("Release check FAILED:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Release check passed: {len(actual)} files, {checked_links} local links, "
          "Python 3.10 syntax, UTF-8, manifest and artifact checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
