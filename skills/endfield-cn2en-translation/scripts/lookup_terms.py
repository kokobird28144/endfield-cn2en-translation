#!/usr/bin/env python3
"""Search user-supplied local dictionaries without fetching game data."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


FILENAMES = {
    "game": "game-terms.csv",
    "aliases": "community-aliases.json",
    "official": "official-names.json",
}
CSV_COLUMNS = {"category", "zh", "en", "aliases_zh", "item_id", "name_id",
               "version", "status", "notes"}
Record = dict[str, Any]


class DataError(ValueError):
    """The selected local dictionary is missing or malformed."""


def text_fields(record: Record, required: tuple[str, ...],
                optional: tuple[str, ...] = ()) -> None:
    for key in required:
        value = record.get(key)
        if not isinstance(value, str) or not value.strip():
            raise DataError(f"{key} must be a non-empty string")
    for key in optional:
        if key in record and not isinstance(record[key], str):
            raise DataError(f"{key} must be a string; keep IDs as strings")


def load_game(path: Path) -> list[Record]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        columns = reader.fieldnames or []
        if len(set(columns)) != len(columns):
            raise DataError("duplicate CSV headers")
        missing = sorted(CSV_COLUMNS - set(columns))
        if missing:
            raise DataError("missing CSV columns: " + ", ".join(missing))
        records: list[Record] = []
        for number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise DataError(f"CSV record {number} has the wrong column count")
            text_fields(row, ("zh", "en", "version", "status"),
                        ("item_id", "name_id", "aliases_zh"))
            records.append(row)
        return records


def load_json(path: Path, scope: str) -> list[Record]:
    with path.open(encoding="utf-8-sig") as stream:
        data = json.load(stream)
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise DataError("JSON root must be an object containing a records array")
    records = data["records"]
    for number, record in enumerate(records, 1):
        if not isinstance(record, dict):
            raise DataError(f"record {number} must be an object")
        if scope == "official":
            text_fields(record, ("zh", "en", "version", "status"),
                        ("item_id", "name_id"))
            continue
        aliases = record.get("aliases")
        if (not isinstance(aliases, list) or not aliases
                or any(not isinstance(x, str) or not x.strip() for x in aliases)):
            raise DataError(f"record {number}: aliases must be non-empty strings")
        text_fields(record, ("meaning_status", "rule"), ("user_meaning",))
        if record["meaning_status"] not in ("user-confirmed", "user-suggested"):
            raise DataError(f"record {number}: unsupported meaning_status")
        targets = record.get("targets")
        if not isinstance(targets, list) or not targets:
            raise DataError(f"record {number}: targets must be a non-empty array")
        for target in targets:
            if not isinstance(target, dict):
                raise DataError(f"record {number}: each target must be an object")
            text_fields(target, ("zh", "en"),
                        ("item_id", "name_id", "version", "status"))
    return records


def search_fields(record: Record, scope: str) -> list[str]:
    if scope == "aliases":
        fields = [*record["aliases"], record.get("user_meaning", "")]
        for target in record["targets"]:
            fields.extend(target.get(key, "") for key in ("zh", "en", "item_id", "name_id"))
        return fields
    fields = [record.get(key, "") for key in ("zh", "en", "item_id", "name_id")]
    if scope == "game":
        fields.extend(record["aliases_zh"].split(";"))
    return fields


def lookup(data_dir: Path, query: str, scope: str, exact: bool,
           fallback_dir: Path | None = None) -> list[Record]:
    scopes = list(FILENAMES) if scope == "all" else [scope]
    matches: list[Record] = []
    loaded = 0
    for selected in scopes:
        path = data_dir / FILENAMES[selected]
        if not path.exists() and fallback_dir is not None:
            path = fallback_dir / FILENAMES[selected]
        if not path.exists():
            message = f"Missing local data: {path}. Supply a dictionary using --data-dir."
            if scope != "all":
                raise DataError(message)
            print(message, file=sys.stderr)
            continue
        try:
            rows = load_game(path) if selected == "game" else load_json(path, selected)
        except (OSError, UnicodeError, csv.Error, ValueError) as error:
            raise DataError(f"Cannot read {path}: {error}") from error
        loaded += 1
        for record in rows:
            fields = (value.casefold() for value in search_fields(record, selected) if value)
            if not any(query == value if exact else query in value for value in fields):
                continue
            if selected == "aliases":
                source = ("user-confirmed-alias" if record["meaning_status"] == "user-confirmed"
                          else "user-suggested-alias")
            else:
                source = "game" if selected == "game" else "verified-name"
            matches.append({**record, "record_source": source})
    if not loaded:
        raise DataError("No selected local dictionaries are available. See references/data-format.md.")
    return matches


def print_records(records: list[Record]) -> None:
    if not records:
        print("No matching term in the supplied data.")
    for record in records:
        if record["record_source"] in ("user-confirmed-alias", "user-suggested-alias"):
            targets = " / ".join(f"{target['zh']} → {target['en']}" for target in record["targets"])
            print(f"{'、'.join(record['aliases'])} | {targets}")
            print(f"  {record['meaning_status']}: {record['rule']}")
            continue
        print(f"{record['zh']} | {record['en']} | {record.get('item_id', '')} | {record['version']}")
        print(f"  Evidence status: {record['status']}")
        if record.get("aliases_zh"):
            print(f"  Conditional aliases: {record['aliases_zh']}")
        if record.get("notes"):
            print(f"  Note: {record['notes']}")


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Chinese/English name, alias, item ID or text ID")
    parser.add_argument("--exact", action="store_true", help="Match complete fields")
    parser.add_argument("--json", action="store_true", help="Print a JSON array to stdout")
    parser.add_argument("--scope", choices=[*FILENAMES, "all"], default="game")
    parser.add_argument("--data-dir", type=Path,
                        help="Use only this directory instead of bundled dictionaries")
    args = parser.parse_args(argv)
    query = args.query.strip().casefold()
    if not query:
        parser.error("query must not be empty")
    try:
        skill_dir = Path(__file__).resolve().parents[1]
        data_dir = args.data_dir.expanduser() if args.data_dir is not None else skill_dir / "data"
        fallback_dir = None if args.data_dir is not None else skill_dir / "references"
        records = lookup(data_dir, query, args.scope, args.exact, fallback_dir)
    except DataError as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print_records(records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
