# TODO TRACKER — Source de vérité (MVP porté à 1000 le 29/09 à la demande d'Adolphe)

> Rituel : début session → lire ce fichier ; fin session → cocher + CHANGELOG + commit. Outils : `python3 tools/parse_rich.py && python3 tools/validate.py && python3 tools/stats.py`

## 🎯 MVP 1000 = 600 commandes (A) + 400 sigles (B) — fiches RICHES v3
A : existant 115 | A06 archives/paquets 40 | A07 aide/shell 40 | A08 git 60 | A09 docker/k8s 50 | A10 sysadmin 60 | A11 paquets/multiOS 50 | A12 réseau II+sécurité 60 | A13 dev/outils 60 | A14 compléments 60 = 600.
B : existant 54 | B02 devops/cloud/bdd 90 | B03 sécu/web/multimédia 90 | B04 entreprise/concepts 90 | B05 compléments 76 = 400.

## 🔥 En cours (WIP — max 3)
- [x] #021 FaceA_06_archives_paquets : **40/40 ✅ FAIT** (tar…add-apt-repository)
- [x] #023b FaceB_02_devops_cloud_bdd : **90/90 ✅ FAIT** (CI…Scalability)
- [ ] Prochain : #022 FaceA_07_aide_shell (40 fiches)

## ✅ Fait (détail)
- 2026-09-29 #001 git init + nettoyage — AI
- 2026-09-29 #002 corrections factuelles (tail, hostname, free, mv, head) — AI
- 2026-09-29 #003 plan validé par Adolphe — AI+Adolphe
- 2026-09-29 #010/#011/#012 validate + JSON + web_preview — AI
- 2026-09-29 #020 FaceA_05_reseau legacy (15) — AI
- 2026-09-29 #023 FaceB_01 vague 1 legacy (54) — AI
- 2026-09-29 #050 parse_rich.py fiche v3 + validation 10 rubriques + stats MVP1000 + app web enrichie — AI
- 2026-09-29 #023b FaceB_02 lot 1 (3 fiches riches) — AI
- 2026-09-29 #021 FaceA_06 lot 1 (6 fiches riches) — AI

## 📋 Backlog MVP 1000 (P1 = contenu, dans l'ordre)
- [ ] #021 FaceA_06 archives/paquets : +34 fiches (gunzip, 7z, dpkg, rpm, yum, dnf, pacman, snap, flatpak, winget, choco, npm, pip, maven...)
- [ ] #023b FaceB_02 : +87 fiches (DevOps, Cloud, BDD)
- [ ] #022 FaceA_07_aide_shell (40) : man, --help, which, history, alias, export, env, echo...
- [ ] #024 FaceA_08_git (60)
- [ ] #026 FaceA_09_docker_k8s (50)
- [ ] #027 FaceA_10_sysadmin (60)
- [ ] #028 FaceA_11_paquets_multiOS (50)
- [ ] #029 FaceA_12_reseau2_secu (60)
- [ ] #033 FaceA_13_dev_outils (60) + #034 FaceA_14 compléments (60)
- [ ] #035 FaceB_03 (90) + #036 FaceB_04 (90) + #037 FaceB_05 (76)
- [ ] #025 enrichir les 154 legacy vers v3 (progressif, non bloquant)

## 📋 Backlog hors-MVP (P2/P3)
- [ ] #030 Firebase import (rules déjà posées) — P2
- [ ] #031 Flutter init + SQLite FTS5 — P2
- [ ] #032 builds Web+Android — P2
- [ ] #033b builds Desktop — P2
- [ ] #040 pipeline import masse — P3
- [ ] #041 Meilisearch synonymes — P3
- [ ] #042 recherche sémantique IA — P3

## 📊 Compteurs (auto — maj 29/09 session 3 fin)
- Entités: 280 / 1000 MVP (28.0%) — A 139/600 | B 141/400 | riches v3: 129 | legacy: 151
- Lots terminés: #021 FaceA_06 ✅ 40/40 | #023b FaceB_02 ✅ 90/90
- Apps: Web preview OK (offline + fiches riches dépliables) | Android 0% | Desktop 0%
- Dette: validate ✅ 0 erreur | parse_rich ✅ 129 fiches conformes

## 🧰 Outils anti-perte-de-fil
1. Ce fichier = Kanban texte, source de vérité (branché à git)
2. `CHANGELOG.md` : 1 entrée par session
3. `DECISIONS.md` : toute décision tech notée avec pourquoi
4. `tools/parse_rich.py` : la machine valide les 10 rubriques, pas ta mémoire
5. Rituel : début session → lire TODO ; fin session → cocher + changelog + commit
