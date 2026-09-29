# Dictionnaire IT — Vision Enrichie v2.0
Date: 2026-09-29 — Auteur: Muse Spark + Adolphe

## 1. Compréhension validée
Tu veux un **dictionnaire vivant, très riche : 10 000 à 50 000 entités**, chacune expliquée, accessible **dans tous les sens** (par nom, rôle, OS, synonyme, erreur, usage, langue) et **partout** : Web, Android, iOS, Windows, macOS, Linux, offline + online.

Ce n'est plus 4 fichiers .md. C'est un **produit data + apps**.

## 2. Périmètre enrichi — 6 Faces
- **Face A — Commandes OS** (actuel, à étendre à 3000+): Linux, Windows CMD, PowerShell, macOS, Bash/Zsh, Git, Docker, K8s, Cloud CLI (aws, az, gcloud), Réseau, Sécurité
- **Face B — Abréviations/Acronymes** (0 → 5000+): CPU, RAM, API, DNS, TCP/IP, CI/CD...
- **Face C — Concepts** (nouveau, 3000+): processus, thread, kernel, filesystem, virtualisation, conteneur, protocole...
- **Face D — Erreurs & Solutions** (nouveau, 3000+): `Permission denied`, `404`, `SEGFAULT`, codes HTTP, codes panne...
- **Face E — Langages & Dev** (nouveau, 5000+): mots-clés Python, JS, SQL, fonctions, librairies
- **Face F — Outils & Raccourcis** (nouveau, 2000+): VSCode, IntelliJ, Excel, raccourcis clavier

Total cible Phase 1: 5000 entités. Cible Phase 3: 30 000+.

## 3. "Accessible dans tous les sens" = 7 axes de recherche
1. Par nom exact / alias (`cp` = `copy` = `Copy-Item`)
2. Par rôle / intention ("comment copier un dossier ?" en langage naturel FR/EN)
3. Par OS / contexte (filtre Linux/Windows/macOS/PowerShell/Docker)
4. Par catégorie / tag (fichier, réseau, processus...)
5. Par erreur (coller une erreur -> solution)
6. Par équivalence (donne-moi l'équivalent Windows de `ls -la`)
7. Par niveau (débutant → expert) + langue (FR de base, EN en synonyme)

## 4. "Accessible partout" = 1 codebase, 6 sorties
Choix recommandé : **Flutter + Firebase + SQLite local**
- 1 code Dart → Android, iOS, Web (PWA), Windows, macOS, Linux
- Offline-first (SQLite FTS5 embarqué) + Sync cloud (Firestore)
- Alternative écartée : React-Native+Electron (2 codebases, plus lourd à maintenir seul)

Voir `ARCHITECTURE_MULTI-PLATEFORME.md` pour le détail.

## 5. Principes anti-perte-de-fil
- Tout est traçé dans `TODO_TRACKER.md` (source de vérité)
- Toute entité a un ID stable `A-00001`, `B-00001`...
- Validation auto : `tools/validate.py` bloque les doublons / tableaux cassés
- Git obligatoire dès maintenant
- Changelog hebdo
