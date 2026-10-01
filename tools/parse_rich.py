#!/usr/bin/env python3
"""parse_rich.py - Fiches riches v3 (## ...) + tableaux legacy -> JSON unifie.

Usage:
  python3 tools/parse_rich.py            ecrit data/dictionnaire.json + data/index.json
  python3 tools/parse_rich.py --check    analyse sans ecrire (code retour 1 si erreur)
  python3 tools/parse_rich.py --strict   les avertissements deviennent bloquants
  python3 tools/parse_rich.py --quiet    resume seulement
"""
from __future__ import annotations
import argparse, glob, json, re, sys, unicodedata
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "dictionnaire.json"
INDEX = ROOT / "data" / "index.json"

# Tokens autorises dans le crochet de titre (CONVENTIONS.md)
OS_TOKENS = {"linux", "macos", "windows", "cmd", "powershell", "cross", "dev", "git", "docker",
             "alpine", "debian", "ubuntu", "rhel", "fedora", "centos", "arch", "suse",
             "opensuse", "bsd", "freebsd", "unix", "android", "ios"}
OS_DISTROS = {"alpine": "linux", "debian": "linux", "ubuntu": "linux", "rhel": "linux",
              "fedora": "linux", "centos": "linux", "arch": "linux", "suse": "linux",
              "opensuse": "linux", "unix": "linux", "bsd": "linux", "freebsd": "linux"}

# Categorie canonique <- premier/chaque token du crochet Face B
CAT_CANON = {
    "materiel": "Matériel", "hardware": "Matériel", "stockage": "Stockage", "storage": "Stockage",
    "systeme": "Système", "system": "Système", "linux": "Système", "reseau": "Réseau",
    "network": "Réseau", "web": "Web", "programmation": "Programmation", "securite": "Sécurité",
    "security": "Sécurité", "devops": "DevOps", "concept": "Concept", "bureautique": "Bureautique",
    "cloud": "Cloud", "data": "Data", "bdd": "Bases de données", "bases de donnees": "Bases de données",
    "developpement": "Développement", "virtualisation": "Virtualisation", "architecture": "Architecture",
    "entreprise": "Entreprise", "management": "Management", "itsm": "ITSM", "supervision": "Supervision",
    "infrastructure": "Infrastructure", "infrastructure it": "Infrastructure", "telecoms": "Télécoms",
    "multimedia": "Multimédia", "ui/ux": "UI/UX", "ui": "UI/UX", "ux": "UI/UX", "finance": "Finance",
    "gouvernance": "Gouvernance", "qualite": "Qualité", "sre": "SRE", "git": "DevOps",
    "api": "Développement", "serverless": "Cloud", "mobile": "Mobile", "seo": "Web",
    "marketing": "Web", "automation": "Automatisation", "ia": "IA", "dsi": "Management",
    "produit": "Management", "tech": "Management", "agile": "Management", "dispositifs": "ITSM",
}

def deaccent(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower().strip()


def canon_categories(bracket: str) -> tuple[list[str], list[str]]:
    """Crochet de titre -> (categories canoniques, tags bruts)."""
    if not bracket:
        return [], []
    parts = [p.strip() for p in re.split(r"[/,]", bracket) if p.strip()]
    cats, tags = [], []
    for p in parts:
        tags.append(p)
        c = CAT_CANON.get(deaccent(p)) or CAT_CANON.get(deaccent(p).replace(" ", ""))
        if c and c not in cats:
            cats.append(c)
    return cats, tags

def norm_os(s: str) -> list[str]:
    """Crochet/traduction d'un OS vers la liste fermee d'OS."""
    raw = (s or "").lower()
    out = []
    if "powershell" in raw: out.append("windows-powershell")
    if "cmd" in raw and "powershell" not in raw: out.append("windows-cmd")
    if "linux" in raw or any(d in raw for d in OS_DISTROS if d != "unix"): out.append("linux")
    if "macos" in raw: out.append("macos")
    if "windows" in raw and not out: out.append("windows")
    if "git" in raw and not out: out.append("git")
    if "docker" in raw and not out: out.append("docker")
    if "ios" in raw and not out: out.append("ios")
    if "android" in raw and not out: out.append("android")
    return out or ["cross"]

A_LABELS = {
    "navigation": "Navigation", "fichiers": "Fichiers", "contenu_fichiers": "Fichiers",
    "processus_systeme": "Système", "systeme_avance": "Système", "sysadmin": "Système",
    "reseau": "Réseau", "reseau2_secu": "Réseau", "archives_paquets": "Paquets",
    "paquets_multiOS": "Paquets", "aide_shell": "Shell", "git": "Git",
    "docker_k8s": "Docker/K8s", "dev_outils": "Développement", "complements": "Compléments",
}


def label_A(theme: str) -> str:
    return A_LABELS.get(theme, theme.replace("_", " ").capitalize())


def split_row(line: str) -> list[str]:
    parts, cur, in_bt = [], "", False
    for ch in line.strip():
        if ch == "`":
            in_bt = not in_bt; cur += ch
        elif ch == "|" and not in_bt:
            parts.append(cur); cur = ""
        else:
            cur += ch
    parts.append(cur)
    if parts and parts[0].strip() == "": parts = parts[1:]
    if parts and parts[-1].strip() == "": parts = parts[:-1]
    return [c.strip() for c in parts]

FIELD_RE = "(?m)^[*][*]([^*]+?)[ ]*:[*][*][ ]*(.*)$"
FIELD_CUT = "[ ]*[|][ ]*[*][*]"
PAREN_FIN = "[ ]*[(][^)]*[)][ ]*$"


def _decle(label):
    """Cle de comparaison de rubrique : sans accents, sans espaces, en minuscules."""
    return deaccent(label).replace(" ", "")


def champs(body):
    """Dictionnaire des rubriques d'une fiche.

    Une meme ligne peut porter plusieurs rubriques :
    '**Niveau :** x | **Popularite :** y | **Aliases :** z'.
    La premiere occurrence d'un libelle gagne (comportement historique).
    """
    out = {}
    for m in re.finditer(FIELD_RE, body):
        parts = re.split(FIELD_CUT, m.group(2))
        out.setdefault(_decle(m.group(1)), parts[0].strip())
        for extra in parts[1:]:
            lab, sep, val = extra.partition(":")
            if sep:
                out.setdefault(_decle(lab.replace("*", "")), val.lstrip("* ").strip())
    return out


def get_field(body, *names):
    """Valeur d'une rubrique **Nom :** (insensible aux accents et a la casse)."""
    c = champs(body)
    for n in names:
        if _decle(n) in c:
            return c[_decle(n)]
    return ""


def get_list(body, *names):
    """Puces d'une rubrique. S'arrete a la ligne vide ou a la rubrique suivante
    (corrige le bug historique qui avalait '**Origine :**' comme une puce)."""
    cibles = {_decle(n) for n in names}
    for m in re.finditer(FIELD_RE, body):
        if _decle(m.group(1)) not in cibles:
            continue
        inline = m.group(2).strip()
        if inline:
            return [x.strip() for x in inline.split(" \u00b7 ") if x.strip()]
        items = []
        for line in body[m.end():].splitlines():
            s = line.strip()
            if not s:
                if items:
                    break
                continue
            if s.startswith("-") or (s.startswith("*") and not s.startswith("**")):
                items.append(s.lstrip("-* ").strip())
            elif items and line[:1].isspace():
                items[-1] = items[-1] + " " + s
            else:
                break
        if items:
            return items
    return []


def parse_cas(items: list[str]) -> list[dict]:
    out = []
    for it in items:
        it = it.strip()
        m = re.match(r"`([^`]+)`\s*[\-\u2014\u2013]\s*(.+)", it)
        if m:
            out.append({"cmd": m.group(1).strip(), "explication": m.group(2).strip(), "contexte": ""})
            continue
        m2 = re.match(r"(.+?)\s*[\-\u2014\u2013]\s*(.+)", it.strip("` "))
        if m2 and m2.group(2).strip():
            out.append({"cmd": m2.group(1).strip("` "), "explication": m2.group(2).strip(), "contexte": ""})
        else:
            out.append({"cmd": it.strip("` "), "explication": "", "contexte": ""})
    return out

def split_names(raw: str) -> tuple[str, list[str]]:
    """`yum` / `dnf` -> ("yum", ["dnf"]) : un titre compose donne un nom + des alias."""
    toks = re.findall(r"`([^`]+)`", raw) or [t.strip() for t in re.split(r"\s*/\s*", raw)]
    toks = [t.strip() for t in toks if t.strip()]
    return (toks[0] if toks else raw.strip()), toks[1:]

def parse_fiches(path: Path, warnings: list[str]) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    mface = re.search(r"face([A-F])_", path.name)
    face = mface.group(1) if mface else "A"
    theme = re.search(r"face[A-F]_\d+_(.+)\.md", path.name)
    theme = theme.group(1) if theme else path.stem
    fiches = []
    for b in re.split(r"(?m)^##\s+", text)[1:]:
        hm = re.match(r"^(.+?)\n", b)
        if not hm: continue
        head = hm.group(1).strip()
        m = re.match(r"((?:`[^`]+`\s*(?:/\s*)?)+?)\s*[\u2014\u2013-]\s*(.+?)\s*(?:\[([^\]]+)\])?\s*$", head)
        if not m:
            m = re.match(r"`([^`]+)`\s*[\u2014\u2013-]\s*(.+?)\s*(?:\[([^\]]+)\])?\s*$", head)
        if not m:
            warnings.append("W-TITLE %s titre non conforme -> %s" % (path.name, head[:70]))
            continue
        nom, titre, osraw = m.group(1).strip(), m.group(2).strip(), (m.group(3) or "").strip()
        nom, extra_aliases = split_names(nom)
        body = b[hm.end():]
        niveau = (get_field(body, "Niveau") or "debutant").split("|")[0].strip().lower()
        popm = re.search(r"\d+", get_field(body, "Popularité"))
        pop = int(popm.group()) if popm else 50
        aliases = [a.strip() for a in get_field(body, "Aliases").split(",") if a.strip() and a.strip() != "\u2014"]
        aliases = [a for a in aliases + extra_aliases if a and a != nom]
        contextes = [c.strip() for c in get_field(body, "Contexte", "Contextes").split(",") if c.strip() and c.strip() != "\u2014"]
        role = get_field(body, "Rôle", "Définition")
        signification = get_field(body, "Signification")
        syntaxe = get_field(body, "Syntaxe").strip("`")
        cas = parse_cas(get_list(body, "Cas réguliers", "Cas courants"))
        origine = get_field(body, "Origine")
        subtil = [s for s in get_list(body, "Subtilités/confusions", "Subtilités", "Confusions") if s]
        dangers = get_field(body, "Urgences/dangers", "Urgences", "Dangers")
        precautions = get_field(body, "Précautions")
        equiv = get_field(body, "Équivalents", "Equivalents")
        voir = [v.strip() for v in re.split(",", get_field(body, "Voir aussi")) if v.strip() and v.strip() != "—"]
        voir = [re.sub(PAREN_FIN, "", v).strip() for v in voir]
        voir = [v for v in voir if v]
        exemple1 = get_field(body, "Exemple")
        cat_field = get_field(body, "Catégorie", "Categorie")
        cats, tags = canon_categories(osraw)
        if face == "B":
            if cat_field and cat_field.strip() not in ("\u2014", "-"):
                cats = [cat_field.strip()] + [c for c in cats if c != cat_field.strip()]
            if not cats:
                cats = ["Concept"]
                warnings.append("W-CAT %s:%s categorie deduite 'Concept' (crochet absent)" % (path.name, nom))
            if not signification:
                signification = re.sub(r"\s*\[[^\]]*\]\s*$", "", titre).strip()
                warnings.append("W-SIG %s:%s Signification absente -> reprise du titre : '%s'" % (path.name, nom, signification))
            e = {"face": face, "type": "sigle", "nom": nom, "titre": titre, "aliases": ([signification] + aliases) if signification else aliases,
                 "signification": signification, "os": ["cross"], "os_raw": "cross", "os_tokens": [],
                 "categories": cats, "tags": tags, "niveau": niveau, "popularite": pop, "role_fr": role or titre,
                 "syntaxe": syntaxe, "contextes": contextes, "cas_reguliers": cas,
                 "exemples": ([{"cmd": exemple1.strip("`"), "explication": ""}] if exemple1 else []),
                 "origine": origine, "subtilites": subtil, "urgences_dangers": dangers,
                 "precautions": precautions, "equivalents": [] if equiv.strip() in ("\u2014", "-", "") else [{"note": equiv}],
                 "voir_aussi": voir, "source": path.name, "legacy": False}
        else:
            cats, tags = [label_A(theme)], []
            e = {"face": face, "type": "commande", "nom": nom, "titre": titre, "aliases": aliases,
                 "signification": "", "os": norm_os(osraw), "os_raw": osraw or "cross",
                 "os_tokens": [t.strip() for t in re.split(r"/", osraw) if t.strip()],
                 "categories": cats, "tags": tags, "niveau": niveau, "popularite": pop, "role_fr": role or titre,
                 "syntaxe": syntaxe, "contextes": contextes, "cas_reguliers": cas,
                 "exemples": [{"cmd": c["cmd"], "explication": c["explication"]} for c in cas],
                 "origine": origine, "subtilites": subtil, "urgences_dangers": dangers,
                 "precautions": precautions, "equivalents": [] if equiv.strip() in ("\u2014", "-", "") else [{"note": equiv}],
                 "voir_aussi": voir, "source": path.name, "legacy": False}
        for t in e["os_tokens"]:
            mots = [w for w in deaccent(t).split() if w]
            if not any(w in OS_TOKENS for w in mots):
                warnings.append("W-OS %s:%s jeton OS hors vocabulaire : '%s'" % (path.name, nom, t))
        fiches.append(e)
    return fiches

def parse_legacy(path: Path) -> list[dict]:
    theme = re.search(r"face[A-F]_[0-9]+_(.+)[.]md", path.name)
    theme = theme.group(1) if theme else path.stem
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for i, l in enumerate(lines):
        if l.strip().startswith("| commande"):
            for j in range(i + 2, len(lines)):
                dl = lines[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) < 7: continue
                cmd, osv, role, syntaxe, exemples, precautions, equiv = cols[:7]
                out.append({"face": "A", "type": "commande", "nom": cmd, "titre": role, "aliases": [], "signification": "",
                    "os": norm_os(osv), "os_raw": osv, "os_tokens": [t.strip() for t in re.split(r"/", osv) if t.strip()],
                    "categories": [label_A(theme)], "tags": [], "niveau": "debutant", "popularite": 50, "role_fr": role,
                    "syntaxe": syntaxe.strip("`"), "contextes": [], "cas_reguliers": [],
                    "exemples": [{"cmd": x.strip().strip("`"), "explication": ""} for x in exemples.split("·") if x.strip()],
                    "origine": "", "subtilites": [], "urgences_dangers": "",
                    "precautions": "" if precautions.strip() in ("\u2014", "-", "") else precautions,
                    "equivalents": [], "voir_aussi": [] if equiv.strip() in ("\u2014", "-", "") else [x.strip() for x in equiv.split(",")],
                    "source": path.name, "legacy": True})
            break
        if l.strip().startswith("| sigle"):
            for j in range(i + 2, len(lines)):
                dl = lines[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) < 6: continue
                sigle, signification, categorie, description, exemple, voir = cols[:6]
                out.append({"face": "B", "type": "sigle", "nom": sigle, "titre": description, "aliases": [signification],
                    "signification": signification, "os": ["cross"], "os_raw": "cross", "os_tokens": [],
                    "categories": [categorie], "tags": [], "niveau": "debutant", "popularite": 50, "role_fr": description,
                    "syntaxe": "", "contextes": [], "cas_reguliers": [],
                    "exemples": [{"cmd": exemple.strip().strip("`"), "explication": ""}],
                    "origine": "", "subtilites": [], "urgences_dangers": "", "precautions": "", "equivalents": [],
                    "voir_aussi": [] if voir.strip() in ("\u2014", "-", "") else [v.strip() for v in voir.split(",")],
                    "source": path.name, "legacy": True})
            break
    for e in out:
        e["voir_aussi"] = [v for v in (re.sub(PAREN_FIN, "", x).strip() for x in e["voir_aussi"]) if v]
    return out

def build(check_only: bool = False):
    entries, seen = [], {}
    errors, warnings = [], []
    for f in sorted(glob.glob(str(ROOT / "face*.md"))):
        p = Path(f)
        riches = parse_fiches(p, warnings)
        rows = riches if riches else parse_legacy(p)
        for e in rows:
            key = (e["face"], e["nom"].lower())
            if key in seen:
                i = seen[key]
                if e.get("origine") and not entries[i].get("origine"):
                    entries[i] = e
                else:
                    warnings.append("W-DUP doublon %s:%s (garde dans %s, ignore dans %s)" % (e["face"], e["nom"], entries[i]["source"], p.name))
                continue
            seen[key] = len(entries)
            entries.append(e)
    cpt = {}
    stamp = date.today()
    for e in entries:
        cpt[e["face"]] = cpt.get(e["face"], 0) + 1
        e["id"] = "%s-%05d" % (e["face"], cpt[e["face"]])
        e["version"] = 1
        e["updated_at"] = str(stamp)
    names = {(e["face"], e["nom"].lower()) for e in entries}
    for e in entries:
        gardes = []
        for a in e.get("aliases", []):
            if a.lower() != e["nom"].lower() and (e["face"], a.lower()) in names:
                warnings.append("W-ALIAS %s:%s alias '%s' ecarte (entree dediee existe)" % (e["source"], e["nom"], a))
                continue
            gardes.append(a)
        e["aliases"] = gardes
    sources = sorted(glob.glob(str(ROOT / "face*.md")))
    if sources:
        latest = max(datetime.fromtimestamp(Path(s).stat().st_mtime).date() for s in sources)
        stamp = latest
        for e in entries:
            e["updated_at"] = str(latest)
    known = {e["nom"].lower() for e in entries} | {a.lower() for e in entries for a in e.get("aliases", [])}
    unresolved = {}
    for e in entries:
        tag = "%s:%s" % (e["source"], e["nom"])
        for v in e.get("voir_aussi", []):
            if v.lower() not in known:
                unresolved[v] = unresolved.get(v, 0) + 1
                warnings.append("W-LINK %s -> '%s' (cible inexistante)" % (tag, v))
        if e.get("legacy"):
            warnings.append("W-LEGACY %s fiche heurtee en tableau legacy (a migrer en v3)" % tag)
            continue
        if not e.get("origine"): errors.append("E-ORI %s origine manquante" % tag)
        if not e.get("role_fr"): errors.append("E-ROLE %s role/definition manquant" % tag)
        elif len(e["role_fr"]) > 200: warnings.append("W-ROLE %s role long (%d car, cible <= 200)" % (tag, len(e["role_fr"])))
        if not e.get("contextes"): errors.append("E-CTX %s contextes manquants" % tag)
        if len(e.get("cas_reguliers", [])) < 2: errors.append("E-CAS %s cas reguliers < 2" % tag)
        if not e.get("voir_aussi"): errors.append("E-VOIR %s voir aussi manquant" % tag)
        if len(e.get("subtilites", [])) < 1: errors.append("E-SUB %s subtilites manquantes (min 1)" % tag)
        elif len(e["subtilites"]) < 2: warnings.append("W-SUB %s une seule subtilite (cible >= 2)" % tag)
        if not (1 <= int(e.get("popularite", 0)) <= 100): errors.append("E-POP %s popularite hors 1-100" % tag)
        if e["face"] == "A":
            if not e.get("syntaxe"): errors.append("E-SYN %s syntaxe manquante" % tag)
            if not e.get("urgences_dangers"): errors.append("E-DAN %s urgences/dangers manquant (tiret long si sans danger)" % tag)
            if not e.get("os_tokens"): errors.append("E-OS %s crochet OS absent du titre" % tag)
        if e["face"] == "B":
            if not e.get("signification"): errors.append("E-SIG %s signification manquante" % tag)
            if not e.get("categories"): errors.append("E-CAT %s categorie manquante" % tag)
    return entries, errors, warnings, unresolved


def payloads(entries):
    payload = {"version": 3, "total": len(entries), "updated_at": str(date.today()), "entries": entries}
    if entries:
        payload["updated_at"] = entries[0]["updated_at"]
    index = {"version": 1, "total": len(entries), "updated_at": payload["updated_at"],
             "entries": [{"id": e["id"], "face": e["face"], "nom": e["nom"], "aliases": e.get("aliases", []),
                          "os": e.get("os", []), "os_raw": e.get("os_raw", ""), "categories": e.get("categories", []),
                          "tags": e.get("tags", []), "niveau": e.get("niveau", "debutant"),
                          "popularite": e.get("popularite", 50), "role_fr": e.get("role_fr", ""),
                          "source": e.get("source", ""), "riche": bool(e.get("origine"))} for e in entries]}
    return payload, index


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="analyse sans ecrire")
    ap.add_argument("--strict", action="store_true", help="les avertissements sont bloquants")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--compare", action="store_true", help="compare le JSON committe, sans ecrire")
    a = ap.parse_args()
    entries, errors, warnings, unresolved = build()
    nA = sum(1 for e in entries if e["face"] == "A")
    nB = sum(1 for e in entries if e["face"] == "B")
    riche = sum(1 for e in entries if e.get("origine"))
    fam = {}
    for w in warnings:
        fam[w.split()[0]] = fam.get(w.split()[0], 0) + 1
    print("ENTREES %d (A:%d B:%d) | riches v3: %d | legacy: %d" % (len(entries), nA, nB, riche, len(entries) - riche))
    print("ERREURS %d | AVERTISSEMENTS %d" % (len(errors), len(warnings)))
    for k in sorted(fam):
        print("   %-10s %d" % (k, fam[k]))
    if errors:
        for x in errors[:80]: print("  -", x)
        if len(errors) > 80: print("  ... +%d" % (len(errors) - 80))
    if warnings and not a.quiet:
        for x in warnings[:25]: print("  ~", x)
        if len(warnings) > 25: print("  ... +%d avertissements" % (len(warnings) - 25))
    if a.check:
        return 1 if errors or (a.strict and warnings) else 0
    payload, index = payloads(entries)
    if a.compare:
        drift = []
        for path, doc in ((OUT, payload), (INDEX, index)):
            old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
            if old is not None and old.get("updated_at") != doc.get("updated_at"):
                doc = dict(doc, updated_at=old.get("updated_at"))
            if old != doc:
                drift.append(path.name)
        print("COMPARE %s" % ("identique" if not drift else "DERIVE -> " + ", ".join(drift)))
        return 1 if drift else 0
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    INDEX.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("ECRIT %s (%d KB) + %s" % (OUT.name, OUT.stat().st_size // 1024, INDEX.name))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
