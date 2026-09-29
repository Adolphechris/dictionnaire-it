#!/usr/bin/env python3
"""md_to_json.py — Convertit les face*.md en data/dictionnaire.json (schéma DATA_MODEL v2)."""
import re, json, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "dictionnaire.json"

def split_row(line):
    parts, cur, in_bt = [], "", False
    for ch in line.strip():
        if ch == "`": in_bt = not in_bt; cur += ch
        elif ch == "|" and not in_bt: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur)
    if parts and parts[0].strip() == "": parts = parts[1:]
    if parts and parts[-1].strip() == "": parts = parts[:-1]
    return [c.strip() for c in parts]

def norm_os(s):
    s = s.lower()
    out = []
    if "powershell" in s: out.append("windows-powershell")
    if "cmd" in s and "powershell" not in s: out.append("windows-cmd")
    if "linux" in s: out.append("linux")
    if "macos" in s: out.append("macos")
    if "windows" in s and not out: out.append("windows")
    return out or ["cross"]

entries = []
compteurs = {"A": 0}
for f in sorted(glob.glob(str(ROOT / "face*.md"))):
    p = Path(f)
    m = re.search(r"face([A-F])_(\d+)_(.+)", p.stem)
    face = m.group(1) if m else "A"
    theme = m.group(3) if m else p.stem
    lignes = p.read_text(encoding="utf-8").splitlines()
    for i, l in enumerate(lignes):
        if l.strip().startswith("| commande"):
            for j in range(i+2, len(lignes)):
                dl = lignes[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) < 7: continue
                cmd, osv, role, syntaxe, exemples, precautions, equiv = cols[:7]
                compteurs["A"] = compteurs.get("A", 0) + 1
                eid = f"A-{compteurs['A']:05d}"
                entries.append({
                    "id": eid, "face": "A", "type": "commande", "nom": cmd,
                    "aliases": [], "os": norm_os(osv),
                    "os_raw": osv, "categories": [theme],
                    "tags": [], "niveau": "debutant",
                    "role_fr": role, "syntaxe": syntaxe.strip("`"),
                    "exemples": [{"cmd": e.strip().strip("`"), "explication": ""} for e in exemples.split("·")],
                    "precautions": "" if precautions.strip() in ("—","-","") else precautions,
                    "equivalents": [] if equiv.strip() in ("—","-","") else [{"note": equiv}],
                    "source": p.name
                })
            break

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps({"version": 1, "total": len(entries), "entries": entries}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✅ {len(entries)} entrées → {OUT}")
