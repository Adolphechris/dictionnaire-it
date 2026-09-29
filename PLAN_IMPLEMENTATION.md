# Plan d'Implémentation — 10 Phases (12 semaines MVP → Produit)

## Phase 0 — Sauvegarde & Hygiène [J1-J2] — PRIORITÉ
- [ ] `git init`, `.gitignore` (firebase-debug.log, .dart_tool...), premier commit
- [ ] Supprimer `test_write.md`, déplacer `firebase-debug.log` → `.logs/`
- [ ] Corriger erreurs bloquantes : `tail -f.log`, `hostname -I` macOS, `free` macOS
- [ ] Créer `SUMMARY.md` + ce dossier docs/

## Phase 1 — Normalisation Data [S1]
- [ ] Figer `DATA_MODEL.md` (fait) + `CONVENTIONS.md`
- [ ] Écrire `tools/validate.py` (vérifie tableaux, doublons, OS valides)
- [ ] Écrire `tools/md_to_json.py` (génère `data/dictionnaire.json`)
- [ ] Générer `stats.py` (compte par OS/catégorie, détecte trous)

## Phase 2 — Contenu MVP 500 [S2-S4]
- [ ] FaceA_05_reseau.md (ping, curl, ssh, ip, dns...)
- [ ] FaceA_06_archives_paquets.md (tar, zip, apt, brew, winget...)
- [ ] FaceA_07_aide_git_docker.md (man, git, docker base)
- [ ] FaceB_01_abreviations.md (200 sigles top)
- [ ] FaceC_01_concepts.md (100 concepts)
- [ ] Objectif : 85 → 500 entités validées

## Phase 3 — Recherche locale V1 [S5]
- [ ] `web_preview/index.html` : 1 fichier, recherche instantanée offline sur dictionnaire.json, filtres OS
- [ ] `cherche.py` CLI pour terminal
- [ ] Test avec 500 entrées <50ms

## Phase 4 — Firebase Cloud [S6]
- [ ] `firebase.json`, `firestore.rules`, `firestore.indexes.json`
- [ ] `tools/import_firestore.py` (push json → Firestore)
- [ ] Hosting PWA preview

## Phase 5 — Flutter MVP [S7-S9]
- [ ] `flutter create app_dico` + SQLite FTS5 + sync Firestore
- [ ] Écrans : Home/Recherche/Filtres/Détail/Favoris/Historique/Offline
- [ ] Build Web + Android APK

## Phase 6 — Desktop [S10]
- [ ] Build Windows/macOS/Linux depuis même code
- [ ] Raccourci global `Ctrl+Alt+D` + recherche clipboard

## Phase 7 — Scale 5000+ [S11-S16]
- [ ] Pipeline import masse (man pages, MS Docs) + modération
- [ ] Meilisearch + synonymes FR/EN
- [ ] Auth + favoris cloud + contributions users

## Phase 8 — IA sémantique [S17+]
- [ ] Embeddings + recherche langage naturel + "équivalent de..."
- [ ] Mode quiz/apprentissage

## Phase 9 — Stores & Public [S18+]
- [ ] Play Store, App Store, MS Store, Snap
- [ ] Landing + SEO

Règle d'or : on ne passe à la phase N+1 que si `validate.py` est vert + TODO_TRACKER.md à jour.
