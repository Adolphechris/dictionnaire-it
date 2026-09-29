#!/usr/bin/env python3
"""stats.py — Compteurs pour TODO_TRACKER."""
import json
from pathlib import Path
from collections import Counter
p = Path(__file__).resolve().parent.parent / "data" / "dictionnaire.json"
if not p.exists():
    print("Lance d'abord: python3 tools/md_to_json.py"); raise SystemExit(1)
d = json.loads(p.read_text(encoding="utf-8"))
entries = d["entries"]
print(f"Total: {len(entries)} / 500 MVP ({len(entries)/500*100:.1f}%)")
print("Par OS:", dict(Counter(o for e in entries for o in e["os"])))
print("Par thème:", dict(Counter(c for e in entries for c in e["categories"])))
