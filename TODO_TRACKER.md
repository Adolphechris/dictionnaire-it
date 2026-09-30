# TODO TRACKER — Source de vérité (MVP porté à 1000 le 29/09 à la demande d'Adolphe)

> Rituel : début session → lire ce fichier ; fin session → cocher + CHANGELOG + commit. Outils : `python3 tools/parse_rich.py && python3 tools/validate.py && python3 tools/stats.py`

## 🎯 MVP 1000 = 600 commandes (A) + 400 sigles (B) — fiches RICHES v3
A : existant 115 | A06 archives/paquets 40 | A07 aide/shell 40 | A08 git 60 | A09 docker/k8s 50 | A10 sysadmin 60 | A11 paquets/multiOS 50 | A12 réseau II+sécurité 60 | A13 dev/outils 60 | A14 compléments 60 = 600.
B : existant 54 | B02 devops/cloud/bdd 90 | B03 sécu/web/multimédia 90 | B04 entreprise/concepts 90 | B05 compléments 76 = 400.

## 🔥 En cours (WIP — max 3)
- [x] #033 FaceA_13_dev_outils : **60/60 ✅ FAIT** (gcc, g++, clang... just)
- [x] #029 FaceA_12_reseau2_secu : **60/60 ✅ FAIT** (tcpdump... auditctl)
- [x] #028 FaceA_11_paquets_multiOS : **50/50 ✅ FAIT** (apt-get... n)
- [x] #027 FaceA_10_sysadmin : **60/60 ✅ FAIT** (chmod, chown, useradd... apparmor_status)
- [x] #026 FaceA_09_docker_k8s : **50/50 ✅ FAIT** (docker run... crictl)
- [x] #024 FaceA_08_git : **60/60 ✅ FAIT** (git... git-filter-repo)
- [x] #021 FaceA_06_archives_paquets : **40/40 ✅ FAIT** (tar…add-apt-repository)
- [x] #023b FaceB_02_devops_cloud_bdd : **90/90 ✅ FAIT** (CI…Scalability)
- [x] #022 FaceA_07_aide_shell : **40/40 ✅ FAIT** (man... yes)

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
- 2026-09-30 #022 FaceA_07_aide_shell : 40/40 fiches v3 — AI
- 2026-09-30 #060 README vitrine professionnel + vérif pipeline réel — AI
- 2026-09-30 #024 FaceA_08_git : 60/60 fiches v3 — AI
- 2026-09-30 #026 FaceA_09_docker_k8s : 50/50 fiches v3 — AI
- 2026-09-30 #027 FaceA_10_sysadmin : 60/60 fiches v3 — AI
- 2026-09-30 #028 FaceA_11_paquets_multiOS : 50/50 fiches v3 — AI
- 2026-09-30 #029 FaceA_12_reseau2_secu : 60/60 fiches v3 — AI
- 2026-09-30 #033 FaceA_13_dev_outils : 60/60 fiches v3 — AI
- 2026-09-30 #034 FaceA_14_complements : 60/60 fiches v3 — AI (Face A 600/600 fiches complète !)
- 2026-09-30 #035 FaceB_03_secu_web_multimedia : 90/90 fiches v3 — AI

## 📋 Backlog MVP 1000 (P1 = contenu, dans l'ordre)
- [ ] #036 FaceB_04_entreprise_concepts (90) ⏳ **Prochain lot**
- [ ] #037 FaceB_05_complements (76)
- [ ] #025 enrichir les 106 legacy vers v3 (progressif, non bloquant)

## 📋 Backlog hors-MVP (P2/P3)
- [ ] #030 Firebase import (rules déjà posées) — P2
- [ ] #031 Flutter init + SQLite FTS5 — P2
- [ ] #032 builds Web+Android — P2
- [ ] #033b builds Desktop — P2
- [ ] #040 pipeline import masse — P3
- [ ] #041 Meilisearch synonymes — P3
- [ ] #042 recherche sémantique IA — P3

## 📊 Compteurs (auto — maj 30/09)
- Entités: 765 / 1000 MVP (76.5%) — A 546/600 | B 219/400 | riches v3: 659 | legacy: 106
- Lots terminés: #021 FaceA_06 ✅ 40/40 | #023b FaceB_02 ✅ 90/90 | #022 FaceA_07 ✅ 40/40 | #024 FaceA_08_git ⏳ 18/60
- Apps: Web preview OK (offline + fiches riches dépliables) | Android 0% | Desktop 0%
- Docs: README vitrine refait (badges, anatomy, architecture, outils, contribution, roadmap) — 220 lignes
- Dette: validate ✅ 0 erreur | parse_rich ✅ 183 fiches conformes | 3 fusions riche→legacy en attente (SQL, VM, ORM)

## 🧰 Outils anti-perte-de-fil
1. Ce fichier = Kanban texte, source de vérité (branché à git)
2. `CHANGELOG.md` : 1 entrée par session
3. `DECISIONS.md` : toute décision tech notée avec pourquoi
4. `tools/parse_rich.py` : la machine valide les 10 rubriques, pas ta mémoire
5. Rituel : début session → lire TODO ; fin session → cocher + changelog + commit
