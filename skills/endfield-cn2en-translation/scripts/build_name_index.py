#!/usr/bin/env python3
"""Build references/name-index.json from the AKEData public data domain.

Names only: each record joins one game text id to its CN and EN strings, and
lists the entities that use it. No dialogue, descriptions or other prose.

    python scripts/build_name_index.py --version 1.6.4@11262943-8 \
        --out references/name-index.json --provenance references/data-provenance-name-index.json

The script needs network access to https://data.akedata.wiki. The shipped
name-index.json is produced by this command; see references/sources.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.request
from datetime import date

BASE = "https://data.akedata.wiki"
USER_AGENT = "endfield-name-index-builder/1.0"

# category -> table that carries a `name` / `nameId` text id
TABLES = [
    ("物品与物料", "ItemTable"),
    ("设施与物流部件", "FactoryBuildingTable"),
    ("角色", "CharacterTable"),
    ("敌人", "EnemyTemplateDisplayInfoTable"),
    ("副本", "DungeonSeriesTable"),
    ("活动", "ActivityTable"),
    ("物品分类", "ItemTypeTable"),
]
TEXT_TABLES = ("I18nTextTable_CN", "I18nTextTable_EN")


def fetch(url: str, path: str) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=600) as response, open(path + ".part", "wb") as handle:
        while True:
            chunk = response.read(1 << 20)
            if not chunk:
                break
            handle.write(chunk)
    os.replace(path + ".part", path)


def cached(name: str, table_dir: str, cache: str) -> str:
    path = os.path.join(cache, name + ".json")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        fetch(f"{BASE}/{table_dir}/{name}.json", path)
    return path


def load(path: str) -> dict:
    with open(path, encoding="utf-8-sig") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit(f"expected a JSON object in {path}")
    return data


def text_of(table: dict, key: object) -> str:
    value = table.get(str(key))
    if isinstance(value, dict):
        return value.get("text") or ""
    return value if isinstance(value, str) else ""


def name_id_of(row: dict) -> object:
    for field in ("name", "nameId", "displayName"):
        value = row.get(field)
        if isinstance(value, dict) and value.get("id") is not None:
            return value["id"]
        if isinstance(value, (str, int)) and value:
            return value
    return None


def resolve_version(version: str, cache: str) -> tuple[str, str]:
    path = os.path.join(cache, "manifest.json")
    if not os.path.exists(path):
        fetch(f"{BASE}/manifest.json", path)
    manifest = load(path)
    if version in ("latest", ""):
        version = manifest["latest"]
    for row in manifest["versions"]:
        if row["id"] == version:
            return version, row["tableCfgPath"]
    raise SystemExit(f"version not in manifest: {version}")


def sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", default="latest")
    parser.add_argument("--cache", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache"))
    parser.add_argument("--out", required=True)
    parser.add_argument("--provenance", help="also write a provenance JSON to this path")
    args = parser.parse_args()

    os.makedirs(args.cache, exist_ok=True)
    version, table_dir = resolve_version(args.version, args.cache)
    print(f"version: {version}  tableCfgPath: {table_dir}")

    files = {}
    cn = load(cached("I18nTextTable_CN", table_dir, args.cache))
    en = load(cached("I18nTextTable_EN", table_dir, args.cache))
    files["I18nTextTable_CN.json"] = os.path.join(args.cache, "I18nTextTable_CN.json")
    files["I18nTextTable_EN.json"] = os.path.join(args.cache, "I18nTextTable_EN.json")

    records: dict[str, dict] = {}
    skipped_no_text = 0
    for category, table_name in TABLES:
        path = cached(table_name, table_dir, args.cache)
        files[table_name + ".json"] = path
        table = load(path)
        paired = 0
        for entity_id, row in table.items():
            if not isinstance(row, dict):
                continue
            nid = name_id_of(row)
            if nid is None:
                continue
            zh, english = text_of(cn, nid), text_of(en, nid)
            if not zh or not english:
                skipped_no_text += 1
                continue
            paired += 1
            key = str(nid)
            record = records.get(key)
            if record is None:
                record = records[key] = {
                    "name_id": key,
                    "zh": zh,
                    "en": english,
                    "status": "game-data-paired",
                    "entities": [],
                }
            elif record["zh"] != zh or record["en"] != english:
                raise SystemExit(f"text id {key} maps to conflicting strings")
            record["entities"].append({"id": entity_id, "table": table_name, "category": category})
        print(f"  {category:8} {table_name:32} rows={len(table):5} paired={paired:5}")

    ordered = sorted(records.values(), key=lambda item: (item["zh"], item["name_id"]))
    for record in ordered:
        record["entities"].sort(key=lambda item: (item["table"], item["id"]))

    entity_count = sum(len(record["entities"]) for record in ordered)
    index = {
        "schema_version": 1,
        "dataset": "name-index",
        "version": version,
        "generated_at": date.today().isoformat(),
        "source": {
            "manifest": f"{BASE}/manifest.json",
            "table_cfg_path": table_dir,
            "project": "https://github.com/NagiYume/AKEDatabase",
            "method": "table[name].id -> I18nTextTable_CN/EN[str(id)]",
            "tables": [name for _, name in TABLES],
        },
        "counts": {
            "records": len(ordered),
            "entities": entity_count,
            "zh": len({record["zh"] for record in ordered}),
            "en": len({record["en"] for record in ordered}),
        },
        "records": ordered,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(index, handle, ensure_ascii=False, indent=1, sort_keys=False)
        handle.write("\n")
    print(f"wrote {args.out}: {json.dumps(index['counts'], ensure_ascii=False)}")

    if args.provenance:
        provenance = {
            "dataset": "name-index",
            "version": version,
            "generated_at": index["generated_at"],
            "builder": "scripts/build_name_index.py",
            "project": "https://github.com/NagiYume/AKEDatabase",
            "manifest_url": f"{BASE}/manifest.json",
            "table_cfg_path": table_dir,
            "method": "For each table row, resolve the name text id and pair I18nTextTable_CN with "
                      "I18nTextTable_EN; keep names only, never descriptions or dialogue. "
                      "64-bit ids stay strings.",
            "tables": [name for _, name in TABLES],
            "counts": index["counts"],
            "skipped_entities_without_text": skipped_no_text,
            "files": [
                {
                    "name": os.path.basename(path),
                    "url": f"{BASE}/{table_dir}/{os.path.basename(path)}",
                    "bytes": os.path.getsize(path),
                    "sha256": sha256(path),
                }
                for path in sorted(files.values(), key=os.path.basename)
            ],
        }
        with open(args.provenance, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(provenance, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"wrote {args.provenance}")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
