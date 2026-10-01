#!/usr/bin/env python3
"""audit.py - Audit qualite du corpus (lecture seule, aucun fichier ecrit).

Usage: python3 tools/audit.py [--summary]
"""
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parse_rich as pr

PLACEHOLDERS = ("todo", "lorem ipsum", "a completer", "placeholder", "xxx")


def densite(e):
    n = len(e.get("role_fr", "")) + len(" ".join(e.get("contextes", [])))
    n += sum(len(c["cmd"]) + len(c["explication"]) for c in e.get("cas_reguliers", []))
    n += len(" ".join(e.get("subtilites", []))) + len(e.get("syntaxe", ""))
    n += len(e.get("precautions", "")) + len(e.get("urgences_dangers", "")) + len(e.get("origine", ""))
    return n


def mediane(valeurs):
    v = sorted(valeurs)
    return v[len(v) // 2] if v else 0


def main():
    resume = "--summary" in sys.argv
    entries, errors, warnings, unresolved = pr.build()
    riches = [e for e in entries if not e.get("legacy")]
    legacy = [e for e in entries if e.get("legacy")]
    A = [e for e in riches if e["face"] == "A"]
    B = [e for e in riches if e["face"] == "B"]
    dens = [densite(e) for e in riches]
    print("AUDIT QUALITE")
    print("  total %d | riches %d (A %d / B %d) | legacy %d" % (len(entries), len(riches), len(A), len(B), len(legacy)))
    print("  densite utile: moy %d car, mediane %d, min %d, <400 car: %d fiche(s)" % (
        sum(dens) // max(1, len(dens)), mediane(dens), min(dens) if dens else 0, sum(1 for d in dens if d < 400)))
    vide_role = sum(1 for e in riches if len(e.get("role_fr", "")) < 20)
    vide_ctx = sum(1 for e in riches if not e.get("contextes"))
    vide_cas = sum(1 for e in riches if len(e.get("cas_reguliers", [])) < 2)
    vide_sub = sum(1 for e in riches if not e.get("subtilites"))
    un_sub = sum(1 for e in riches if len(e.get("subtilites", [])) == 1)
    vide_ori = sum(1 for e in riches if not e.get("origine"))
    vide_voir = sum(1 for e in riches if not e.get("voir_aussi"))
    print("  rubriques faibles: role %d | contextes %d | cas<2 %d | subtilites 0 %d / 1 %d | origine %d | voir_aussi %d" % (
        vide_role, vide_ctx, vide_cas, vide_sub, un_sub, vide_ori, vide_voir))
    if not resume:
        print("  Face B: syntaxe %d | precautions %d | equivalents %d | urgences %d | signification %d (sur %d)" % (
            sum(1 for e in B if e["syntaxe"]), sum(1 for e in B if e["precautions"]),
            sum(1 for e in B if e["equivalents"]), sum(1 for e in B if e["urgences_dangers"]),
            sum(1 for e in B if e["signification"]), len(B)))
        casdist = Counter(len(e.get("cas_reguliers", [])) for e in riches)
        print("  distribution cas :", dict(sorted(casdist.items())))
        print("  distribution subtilites :", dict(sorted(Counter(len(e.get("subtilites", [])) for e in riches).items())))
        print("  categories :", dict(sorted(Counter(c for e in entries for c in e.get("categories", [])).items(), key=lambda x: -x[1])))
        print("  OS :", dict(Counter(o for e in entries for o in e.get("os", []))))
        roles = [len(e["role_fr"]) for e in riches]
        print("  longueur role: moy %d, max %d, >200 car %d" % (sum(roles)//max(1,len(roles)), max(roles) if roles else 0, sum(1 for r in roles if r > 200)))
        sus = [e["nom"] for e in riches if any(p in (e["role_fr"] + " ".join(e["subtilites"])).lower() for p in PLACEHOLDERS)]
        print("  placeholders suspects :", sus[:10] if sus else "aucun")
        cross = [(a["nom"], b["nom"], a["source"], b["source"]) for a in A for b in B if a["nom"].lower() == b["nom"].lower()]
        print("  doublons inter-faces (A<->B) :", len(cross), cross[:12])
        lg = Counter(e["source"] for e in legacy)
        print("  legacy par fichier :", dict(sorted(lg.items())))
    refs = sum(len(e.get("voir_aussi", [])) for e in entries)
    print("  liens voir_aussi: %d refs, %d mortes (%.1f%%), %d cibles distinctes" % (
        refs, sum(unresolved.values()), 100.0 * sum(unresolved.values()) / max(1, refs), len(unresolved)))
    top = sorted(unresolved.items(), key=lambda x: -x[1])[:20] if not resume else []
    if top:
        print("  top cibles manquantes :", ", ".join("%s x%d" % (k, v) for k, v in top))
    print("  erreurs %d | avertissements %d (dont liens %d)" % (len(errors), len(warnings), sum(unresolved.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
