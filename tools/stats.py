#!/usr/bin/env python3
"""stats.py — Compteurs pour TODO_TRACKER (MVP = 1000 : 600 A + 400 B)."""
import json
from pathlib import Path
from collections import Counter
p = Path(__file__).resolve().parent.parent / "data" / "dictionnaire.json"
if not p.exists():
    print("Lance d'abord: python3 tools/parse_rich.py"); raise SystemExit(1)
d = json.loads(p.read_text(encoding="utf-8"))
entries = d["entries"]
nA = sum(1 for e in entries if e["face"] == "A")
nB = sum(1 for e in entries if e["face"] == "B")
riches = sum(1 for e in entries if e.get("origine"))
print(f"TOTAL: {len(entries)} / 1000 MVP ({len(entries)/10:.1f}%)")
print(f"  A commandes: {nA}/600 ({nA/6:.1f}%) | B sigles: {nB}/400 ({nB/4:.1f}%)")
print(f"  Fiches riches v3: {riches} | legacy: {len(entries)-riches}")
print("  Par OS:", dict(Counter(o for e in entries for o in e["os"])))
print("  Par catégorie:", dict(Counter(c for e in entries for c in e["categories"])))

