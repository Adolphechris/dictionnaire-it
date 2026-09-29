#!/usr/bin/env python3
"""parse_rich.py — Fiches riches v3 (## ...) + tableaux legacy → JSON unifié."""
import re, json, glob
from pathlib import Path
from datetime import date
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "dictionnaire.json"
def norm_os(s):
    s = (s or "").lower()
    out = []
    if "powershell" in s: out.append("windows-powershell")
    if "cmd" in s and "powershell" not in s: out.append("windows-cmd")
    if "linux" in s: out.append("linux")
    if "macos" in s: out.append("macos")
    if "windows" in s and not out: out.append("windows")
    if "git" in s and not out: out.append("git")
    if "docker" in s and not out: out.append("docker")
    return out or ["cross"]
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
def get_field(body, *names):
    for n in names:
        m = re.search(r"\*\*" + re.escape(n) + r"\s*:\*\*\s*(.+)", body)
        if m:
            val = m.group(1).strip()
            # coupe les champs accolés sur la même ligne : `... | **Autre :** ...`
            val = re.split(r"\s*\|\s*\*\*", val)[0].strip()
            return val
    return ""
def get_list(body, *names):
    for n in names:
        m = re.search(r"\*\*" + re.escape(n) + r"\s*:.*\n((?:\s*[-*].*\n?)+)", body)
        if m: return [l.strip()[1:].strip() for l in m.group(1).strip().splitlines()]
    return []
def parse_cas(items):
    out = []
    for it in items:
        m = re.match(r"`([^`]+)`\s*[\-—–]\s*(.+)", it)
        if m: out.append({"cmd": m.group(1).strip(), "explication": m.group(2).strip(), "contexte": ""})
        else: out.append({"cmd": it.strip("` "), "explication": "", "contexte": ""})
    return out

def parse_fiches(path):
    text = path.read_text(encoding="utf-8")
    mface = re.search(r"face([A-F])_", path.name)
    face = mface.group(1) if mface else "A"
    theme = re.search(r"face[A-F]_\d+_(.+)\.md", path.name)
    theme = theme.group(1) if theme else path.stem
    fiches = []
    blocks = re.split(r"(?m)^##\s+", text)
    for b in blocks[1:]:
        hm = re.match(r"`([^`]+)`\s*[—–-]\s*(.+?)(?:\[([^\]]+)\])?\s*\n", b)
        if not hm: continue
        nom, titre, osraw = hm.group(1).strip(), hm.group(2).strip(), (hm.group(3) or "").strip()
        body = b[hm.end():]
        niveau = (get_field(body, "Niveau") or "debutant").lower()
        popm = re.search(r"\d+", get_field(body, "Popularité") or "")
        pop = int(popm.group()) if popm else 50
        aliases = [a.strip() for a in get_field(body, "Aliases").split(",") if a.strip() and a.strip() != "—"]
        contextes = [c.strip() for c in get_field(body, "Contexte", "Contextes").split(",") if c.strip() and c.strip() != "—"]
        role = get_field(body, "Rôle", "Définition")
        signification = get_field(body, "Signification")
        categorie = get_field(body, "Catégorie") or theme
        syntaxe = get_field(body, "Syntaxe").strip("`")
        cas = parse_cas(get_list(body, "Cas réguliers"))
        origine = get_field(body, "Origine")
        subtil = get_list(body, "Subtilités/confusions", "Subtilités")
        dangers = get_field(body, "Urgences/dangers", "Urgences")
        precautions = get_field(body, "Précautions")
        equiv = get_field(body, "Équivalents")
        voir = [v.strip() for v in get_field(body, "Voir aussi").split(",") if v.strip() and v.strip() != "—"]
        exemple1 = get_field(body, "Exemple")
        base = {"nom": nom, "aliases": aliases, "niveau": niveau, "popularite": pop,
            "contextes": contextes, "origine": origine, "subtilites": subtil,
            "voir_aussi": voir, "source": path.name}
        if face == "B":
            base.update({"face": face, "type": "sigle",
                "aliases": ([signification] + aliases) if signification else aliases,
                "os": ["cross"], "os_raw": "cross", "categories": [categorie],
                "tags": [], "role_fr": role or titre, "syntaxe": "",
                "cas_reguliers": cas or ([{"cmd": exemple1.strip("`"), "explication": "", "contexte": ""}] if exemple1 else []),
                "exemples": ([{"cmd": exemple1.strip("`"), "explication": ""}] if exemple1 else []),
                "urgences_dangers": "", "precautions": "", "equivalents": []})
        else:
            base.update({"face": face, "type": "commande",
                "os": norm_os(osraw), "os_raw": osraw or "cross", "categories": [theme],
                "tags": [], "role_fr": role or titre, "syntaxe": syntaxe,
                "cas_reguliers": cas,
                "exemples": [{"cmd": c["cmd"], "explication": c["explication"]} for c in cas],
                "urgences_dangers": dangers, "precautions": precautions,
                "equivalents": [] if equiv.strip() in ("—", "-", "") else [{"note": equiv}]})
        fiches.append(base)
    return fiches

def parse_legacy(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for i, l in enumerate(lines):
        if l.strip().startswith("| commande"):
            for j in range(i+2, len(lines)):
                dl = lines[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) < 7: continue
                cmd, osv, role, syntaxe, exemples, precautions, equiv = cols[:7]
                out.append({"face": "A", "type": "commande", "nom": cmd, "aliases": [],
                    "os": norm_os(osv), "os_raw": osv, "categories": ["legacy"],
                    "tags": [], "niveau": "debutant", "popularite": 50, "role_fr": role,
                    "syntaxe": syntaxe.strip("`"), "contextes": [], "cas_reguliers": [],
                    "exemples": [{"cmd": e.strip().strip("`"), "explication": ""} for e in exemples.split("·")],
                    "origine": "", "subtilites": [], "urgences_dangers": "",
                    "precautions": "" if precautions.strip() in ("—", "-", "") else precautions,
                    "equivalents": [] if equiv.strip() in ("—", "-", "") else [{"note": equiv}],
                    "voir_aussi": [], "source": path.name})
            break
        if l.strip().startswith("| sigle"):
            for j in range(i+2, len(lines)):
                dl = lines[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) < 6: continue
                sigle, signification, categorie, description, exemple, voir = cols[:6]
                out.append({"face": "B", "type": "sigle", "nom": sigle, "aliases": [signification],
                    "os": ["cross"], "os_raw": "cross", "categories": [categorie],
                    "tags": [], "niveau": "debutant", "popularite": 50, "role_fr": description,
                    "syntaxe": "", "contextes": [], "cas_reguliers": [],
                    "exemples": [{"cmd": exemple.strip().strip("`"), "explication": ""}],
                    "origine": "", "subtilites": [], "urgences_dangers": "",
                    "precautions": "", "equivalents": [],
                    "voir_aussi": [] if voir.strip() in ("—", "-", "") else [v.strip() for v in voir.split(",")],
                    "source": path.name})
            break
    return out
entries, seen = [], set()
for f in sorted(glob.glob(str(ROOT / "face*.md"))):
    p = Path(f)
    riches = parse_fiches(p)
    legacy = parse_legacy(p) if not riches else []
    for e in riches + legacy:
        key = (e["face"], e["nom"].lower())
        if key in seen:
            print(f"DOUBLON ignore: {e['face']}:{e['nom']} dans {p.name}"); continue
        seen.add(key)
        entries.append(e)
cpt = {}
for e in entries:
    cpt[e["face"]] = cpt.get(e["face"], 0) + 1
    e["id"] = f"{e['face']}-{cpt[e['face']]:05d}"
    e["version"] = 1
    e["updated_at"] = str(date.today())
OUT.write_text(json.dumps({"version": 3, "total": len(entries), "entries": entries}, ensure_ascii=False, indent=2), encoding="utf-8")
nA = sum(1 for e in entries if e["face"] == "A")
nB = sum(1 for e in entries if e["face"] == "B")
nr = sum(1 for e in entries if e.get("origine"))
print(f"OK {len(entries)} entrees (A:{nA} B:{nB}, riches:{nr}) vers {OUT}")

# --- Validation des fiches riches v3 (la totale : chaque rubrique obligatoire) ---
errs = []
for e in entries:
    if not e.get("origine"):
        continue  # legacy, non concerné
    tag = f"{e['source']}:{e['nom']}"
    if not e.get("role_fr"): errs.append(f"{tag} — Rôle/Définition manquant")
    if not e.get("contextes"): errs.append(f"{tag} — Contexte manquant")
    if len(e.get("cas_reguliers", [])) < 2: errs.append(f"{tag} — Cas réguliers < 2")
    if not e.get("origine"): errs.append(f"{tag} — Origine manquante")
    if not e.get("voir_aussi"): errs.append(f"{tag} — Voir aussi manquant")
    if e["face"] == "A":
        if not e.get("syntaxe"): errs.append(f"{tag} — Syntaxe manquante")
        if not e.get("subtilites"): errs.append(f"{tag} — Subtilités manquantes (≥1)")
        if not e.get("urgences_dangers"): errs.append(f"{tag} — Urgences/dangers manquant (mettre — si sans danger)")
    if e["face"] == "B":
        if len(e.get("subtilites", [])) < 2: errs.append(f"{tag} — Subtilités < 2 (sigles : confusions fréquentes)")
if errs:
    print(f"\n❌ {len(errs)} fiche(s) riche(s) incomplète(s):")
    for x in errs: print("  -", x)
    raise SystemExit(1)
print(f"✅ Validation riche OK ({nr} fiches v3 conformes)")

