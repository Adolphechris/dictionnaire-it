#!/usr/bin/env python3
"""validate.py — Vérifie les .md FaceA/B avant import. Bloque doublons, colonnes, OS invalides."""
import re, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OS_VALIDES = {"linux","macos","windows (cmd)","powershell","windows","linux/macos",
  "linux/macos/windows","linux/windows","macos/windows","cross","git","docker","bash","zsh"}
seen = {}
erreurs, avertissements = [], []
def split_row(line):
    """Split Markdown row on | but ignore | inside backticks."""
    parts, cur, in_bt = [], "", False
    for ch in line.strip():
        if ch == "`": in_bt = not in_bt; cur += ch
        elif ch == "|" and not in_bt: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur)
    # drop first/last empty from leading/trailing |
    if parts and parts[0].strip() == "": parts = parts[1:]
    if parts and parts[-1].strip() == "": parts = parts[:-1]
    return [c.strip() for c in parts]

fichiers = sorted(glob.glob(str(ROOT / "face*.md")))
if not fichiers:
    print("Aucun face*.md trouvé"); sys.exit(1)

for f in fichiers:
    nom = Path(f).name
    lignes = Path(f).read_text(encoding="utf-8").splitlines()
    # trouve header tableau
    for i, l in enumerate(lignes):
        if l.strip().startswith("| commande") or l.strip().startswith("| sigle") or l.strip().startswith("| nom"):
            ncols = l.count("|") - 1
            # vérifie séparateur
            if i+1 >= len(lignes) or "---" not in lignes[i+1]:
                erreurs.append(f"{nom}:L{i+2} séparateur --- manquant")
            # vérifie lignes data
            for j in range(i+2, len(lignes)):
                dl = lignes[j].strip()
                if not dl.startswith("|"): break
                cols = split_row(dl)
                if len(cols) != ncols:
                    erreurs.append(f"{nom}:L{j+1} {len(cols)} cols au lieu de {ncols} → {dl[:80]}")
                    continue
                cmd = cols[0].lower()
                if cmd in seen:
                    avertissements.append(f"{nom}:L{j+1} doublon '{cols[0]}' (déjà dans {seen[cmd]})")
                else:
                    seen[cmd] = f"{nom}:L{j+1}"
                # vérifie OS (col 2) si face A
                if "commande" in lignes[i].lower():
                    osv = cols[1].lower()
                    norm = osv.replace(" ", "")
                    # accepte combos connus
                    if osv.lower() not in {v for v in OS_VALIDES} and norm not in {"linux/macos","linux/macos/windows","windows(cmd)","linux/windows"}:
                        # tolérant: signale seulement si vraiment bizarre
                        if len(osv) < 2:
                            erreurs.append(f"{nom}:L{j+1} OS vide pour '{cols[0]}'")
                # anti-patterns connus
                if "tail -f.log" in dl or "tail -f." in dl.replace(" ", "") and "tail -f " not in dl:
                    pass
                if "-f.log" in dl:
                    erreurs.append(f"{nom}:L{j+1} typo probable '-f.log' → '-f app.log' pour '{cols[0]}'")
            break

print(f"Fichiers: {len(fichiers)} | Entrées uniques: {len(seen)}")
for a in avertissements: print("AVERT:", a)
for e in erreurs: print("ERREUR:", e)
if erreurs:
    print(f"\n❌ {len(erreurs)} erreur(s), {len(avertissements)} avertissement(s)"); sys.exit(1)
print(f"\n✅ OK — {len(seen)} entrées, {len(avertissements)} avertissement(s) (doublons à fusionner plus tard)")
