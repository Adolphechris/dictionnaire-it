#!/usr/bin/env python3
"""validate.py - Controle du corpus avant import (tableaux legacy + fiches riches v3).

Usage: python3 tools/validate.py [--strict] [--links N]
  --strict   les avertissements deviennent bloquants
  --links N  nombre de liens voir_aussi morts tolere (defaut 0)
"""
import sys, glob
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parse_rich as pr

ROOT = Path(__file__).resolve().parent.parent


def split_row(line):
    """Decoupe une ligne Markdown sur | en ignorant les | entre accents graves."""
    parts, cur, in_bt = [], "", False
    for ch in line.strip():
        if ch == "`":
            in_bt = not in_bt
            cur += ch
        elif ch == "|" and not in_bt:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [c.strip() for c in parts]


def check_tables():
    """Controles sur les tableaux legacy (fichiers sans fiche riche)."""
    erreurs, averts, vus, fichiers = [], [], {}, 0
    for f in sorted(glob.glob(str(ROOT / "face*.md"))):
        nom = Path(f).name
        face = nom[4] if nom.startswith("face") else "?"
        lignes = Path(f).read_text(encoding="utf-8").splitlines()
        if any(l.startswith("## ") for l in lignes):
            continue
        fichiers += 1
        for i, l in enumerate(lignes):
            entete = l.strip()
            if not entete.startswith(("| commande", "| sigle", "| nom")):
                continue
            ncols = entete.count("|") - 1
            if i + 1 >= len(lignes) or "---" not in lignes[i + 1]:
                erreurs.append("%s:L%d separateur --- manquant" % (nom, i + 2))
            for j in range(i + 2, len(lignes)):
                dl = lignes[j].strip()
                if not dl.startswith("|"):
                    break
                cols = split_row(dl)
                if len(cols) != ncols:
                    erreurs.append("%s:L%d %d colonnes au lieu de %d" % (nom, j + 1, len(cols), ncols))
                    continue
                cle = (face, cols[0].lower())
                if cle in vus:
                    averts.append("%s:L%d doublon '%s' (deja %s)" % (nom, j + 1, cols[0], vus[cle]))
                else:
                    vus[cle] = "%s:L%d" % (nom, j + 1)
                if "commande" in entete.lower() and len(cols[1].strip()) < 2:
                    erreurs.append("%s:L%d OS vide pour '%s'" % (nom, j + 1, cols[0]))
                if "-f.log" in dl:
                    erreurs.append("%s:L%d typo probable '-f.log' -> '-f app.log' pour '%s'" % (nom, j + 1, cols[0]))
            break
    return erreurs, averts, len(vus), fichiers


def main():
    strict = "--strict" in sys.argv
    tol = 0
    if "--links" in sys.argv:
        tol = int(sys.argv[sys.argv.index("--links") + 1])
    entries, errors, warnings, unresolved = pr.build()
    t_err, t_av, nb_lignes, nb_fichiers = check_tables()
    liens = sum(unresolved.values())
    riches = sum(1 for e in entries if not e.get("legacy"))
    legacy = len(entries) - riches
    fam = {}
    for w in warnings:
        fam[w.split()[0]] = fam.get(w.split()[0], 0) + 1
    print("VALIDATION")
    print("  fiches riches analysees     : %d" % riches)
    print("  entrees legacy (tableaux)   : %d (%d fichiers legacy)" % (legacy, nb_fichiers))
    print("  lignes legacy uniques       : %d" % nb_lignes)
    print("  erreurs bloquantes          : %d" % (len(errors) + len(t_err)))
    print("  avertissements              : %d" % (len(warnings) + len(t_av)))
    if fam:
        print("  familles d'avertissement    : %s" % fam)
    print("  liens voir_aussi morts      : %d / %d" % (liens, liens + sum(1 for e in entries for _ in e.get("voir_aussi", [])) - liens))
    for e in (errors + t_err)[:40]:
        print("  ERREUR :", e)
    if len(errors) + len(t_err) > 40:
        print("  ... +%d erreurs" % (len(errors) + len(t_err) - 40))
    for a in (warnings + t_av)[:15]:
        print("  AVERT  :", a)
    if len(warnings) + len(t_av) > 15:
        print("  ... +%d avertissements" % (len(warnings) + len(t_av) - 15))
    top = sorted(unresolved.items(), key=lambda x: -x[1])[:12]
    if top:
        print("  cibles manquantes (top)     : %s" % ", ".join("%s x%d" % (k, v) for k, v in top))
    if errors or t_err:
        print("X %d erreur(s)" % (len(errors) + len(t_err)))
        return 1
    if strict and (warnings or t_av or liens > tol):
        print("X mode strict: %d avertissement(s), %d lien(s) mort(s) (> %d)" % (len(warnings) + len(t_av), liens, tol))
        return 1
    print("OK corpus conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
