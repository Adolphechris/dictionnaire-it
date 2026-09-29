# TODO TRACKER — Source de vérité (mettre à jour à chaque session)

> Comment l'utiliser : cocher `[x]`, ajouter date + initiales. Ne jamais supprimer une ligne, barrer si abandonné. `npm run stats` ou `python tools/stats.py` met à jour les compteurs.

## 🔥 En cours (WIP — max 3)
- [x] 2026-09-29 — #001 git init + nettoyage (Phase 0) — AI
- [x] 2026-09-29 — #002 corriger erreurs factuelles (tail, hostname, free, mv, head) — AI
- [x] 2026-09-29 — #003 valider plan avec Adolphe → OK Phase 0 lancée — AI+Adolphe
- [x] 2026-09-29 — #010 créer `tools/validate.py` (split_row anti-pipe, clés Face:nom) — AI
- [x] 2026-09-29 — #011 créer `data/dictionnaire.json` (154 entrées) — AI
- [x] 2026-09-29 — #012 créer `web_preview/index.html` démo recherche — AI
- [x] 2026-09-29 — #020 FaceA_05_reseau (15 cmds) — AI
- [ ] #021 FaceA_06_archives_paquets (25 cmds) — prochain
- [ ] #022 FaceA_07_git_docker_base (30 cmds)
- [ ] #023 FaceB_01 vague 1/4 faite (54/200 : matériel, réseau, web, prog, sécu, concept) — reste 146

## 📋 Backlog trié par priorité
### P0 — Bloquant
- [ ] #010 créer `tools/validate.py`
- [ ] #011 créer `data/dictionnaire.json` (85 entrées actuelles)
- [ ] #012 créer `web_preview/index.html` démo recherche

### P1 — Contenu (vers 500)
- [ ] #020 FaceA_05_reseau (30 cmds)
- [ ] #021 FaceA_06_archives_paquets (25 cmds)
- [ ] #022 FaceA_07_git_docker_base (30 cmds)
- [ ] #023 FaceB_01_abreviations_top200
- [ ] #024 FaceC_01_concepts_100
- [ ] #025 dédupliquer cp/cp-r, kill/kill-9, ps/ps-aux

### P2 — Cloud & Apps
- [ ] #030 firebase.json + rules + import
- [ ] #031 Flutter init + SQLite FTS5
- [ ] #032 builds Web+Android
- [ ] #033 builds Desktop

### P3 — Scale & IA
- [ ] #040 pipeline import masse
- [ ] #041 Meilisearch synonymes
- [ ] #042 recherche sémantique IA

## ✅ Fait
- [x] 2026-09-29 — 4 fichiers FaceA créés (85 entrées) — Adolphe
- [x] 2026-09-29 — Vision v2 + Architecture + DataModel + Plan — AI

## 📊 Compteurs (auto — maj 29/09 10h40)
- Entités: 154 / 500 MVP (30.8%) / 5000 P2 (3.1%)
- Faces: A 100 cmds (5 fichiers) | B 54 sigles (vague 1/4) | C 0% | D 0% | E 0% | F 0%
- Apps: Web preview OK (offline, filtres OS) | Android 0% | iOS 0% | Desktop 0%
- Dette: 0 erreur validate ✅ | 0 doublon intra-face ✅ | reste à fusionner cp/cp-r, kill/-9 (volontaire, #025)

## 🧰 Outils anti-perte-de-fil
1. Ce fichier = tableau Kanban texte (branché à git)
2. `CHANGELOG.md` : 1 ligne par session (quoi/pourquoi)
3. `DECISIONS.md` : toute décision tech notée (ex: Flutter choisi car...)
4. `tools/` : validate, stats, import (la machine vérifie, pas ta mémoire)
5. Rituel : début session → lire TODO, fin session → cocher + changelog
