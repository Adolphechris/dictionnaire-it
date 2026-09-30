<h1 align="center">Dictionnaire IT</h1>

<p align="center">
  <strong>Le référentiel vivant des commandes et du vocabulaire informatiques —<br>3 OS, recherche dans tous les sens, 100 % offline.</strong>
</p>

<p align="center">
  <img alt="entrées" src="https://img.shields.io/badge/entr%C3%A9es-338%20%2F%201000%20MVP-2f81f7?style=flat-square">
  <img alt="fiches riches" src="https://img.shields.io/badge/fiches%20riches%20v3-187-3fb950?style=flat-square">
  <img alt="validation" src="https://img.shields.io/badge/validation-0%20erreur-3fb950?style=flat-square">
  <img alt="langue" src="https://img.shields.io/badge/contenu-fran%C3%A7ais-8957b5?style=flat-square">
  <img alt="stack" src="https://img.shields.io/badge/stack-Flutter%20%C2%B7%20Firebase%20%C2%B7%20SQLite%20FTS5-blue?style=flat-square">
  <img alt="phase" src="https://img.shields.io/badge/phase-2%20sur%2010%20(contenu%20MVP)-yellow?style=flat-square">
</p>

<p align="center">
  <a href="#le-problème">Problème</a> ·
  <a href="#anatomie-dune-fiche">Format de fiche</a> ·
  <a href="#état-du-projet">Avancement</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#démarrage-rapide">Démarrage</a> ·
  <a href="#contribuer">Contribuer</a> ·
  <a href="#feuille-de-route">Roadmap</a>
</p>

---


## Le problème

Les pros de l'informatique perdent un temps considérable à chercher **la bonne commande**, **le bon flag**, **le bon sigle** — et surtout **l'équivalent d'un OS à l'autre**. Les man pages sont denses, les docs officielles éparpillées, les tutos approximatifs, et rien n'explique les pièges qui coûtent une nuit blanche.

## La réponse

Un **dictionnaire structuré, validé par machine**, où chaque entrée est une fiche complète : à quoi ça sert, dans quels contextes, les cas réellement fréquents, l'origine de l'outil, les confusions classiques, les dangers, les précautions et les équivalents multi-OS.

- **Deux faces** — Face A : les commandes (`tar`, `grep`, `git rebase`). Face B : les sigles (`CI/CD`, `ORM`, `SRE`).
- **Multi-OS dès la donnée** — chaque fiche déclare ses OS (`linux`, `macos`, `windows-cmd`, `windows-powershell`) et ses équivalents (`cp` ↔ `Copy-Item`).
- **Cherche dans tous les sens** — par nom, alias, rôle/intention, OS, catégorie, niveau, équivalence.
- **Offline-first** — la donnée vit dans des Markdown versionnés, compilés en JSON/SQLite ; l'app doit fonctionner sans réseau.
- **Qualité garantie par l'outil** — pas de mise en page "à l'œil" : `tools/parse_rich.py` refuse toute fiche incomplète, `tools/validate.py` refuse tout doublon ou tableau cassé.

---

## Anatomie d'une fiche (format « Fiche riche v3 »)

Une fiche = 10 rubriques obligatoires, contrôlées par le parser. Extrait réel de `faceA_06_archives_paquets.md` :

```markdown
## `tar` — Archiver et compresser des dossiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** sauvegarde serveur, distribution logicielle, backup avant migration
**Rôle :** Créer, lister et extraire des archives (souvent compressées en .tar.gz).
**Syntaxe :** `tar [options] <archive> <fichiers>`
**Cas réguliers :**
- `tar -tzf backup.tar.gz` — Lister le contenu SANS extraire (vérification avant restauration)
**Origine :** Tape ARchive, Unix V7 (1979), bandes magnétiques ; standard POSIX.
**Subtilités/confusions :**
- Sans -z/-j/-J, tar ne compresse PAS, il concatène seulement.
**Urgences/dangers :** ⚠️ `tar -xzf arc -C /` écrase le système — toujours lister avec -t avant.
**Précautions :** Vérifier la taille et le contenu avec `tar -tzf` avant extraction.
**Équivalents :** Compress-Archive (PowerShell), 7z (Windows)
**Voir aussi :** gzip, gunzip, zip, unzip, rsync
```

Chaque fiche est compilée en entité JSON typée (`DATA_MODEL.md`) : `id` stable `A-00001`, `os[]`, `niveau`, `popularite`, `cas_reguliers[]`, `subtilites[]`, `equivalents[]`… Le même JSON alimente la recherche SQLite FTS5, Firestore et l'aperçu web.

---

## État du projet

| Indicateur | Valeur |
|---|---|
| **Entités totales** | **338 / 1000** (33,8 % du MVP) |
| Face A — commandes | 197 / 600 |
| Face B — sigles | 141 / 400 |
| Fiches riches v3 | 187 |
| Entrées legacy (tableaux) | 151 — conservées, enrichies progressivement |
| Fichiers source | 10 (8 × Face A, 2 × Face B) |
| Validation | ✅ 0 erreur, 0 avertissement |
| Aperçu web offline | ✅ `web_preview/index.html` |
| App Flutter | ⏳ Phase 5 (non démarrée) |

> Chiffres produits par `python3 tools/stats.py` — à régénérer à chaque lot de contenu.

**Progression par lot** : #021 FaceA_06 archives/paquets ✅ 40/40 · #022 FaceA_07 aide/shell ✅ 40/40 · #023b FaceB_02 DevOps/Cloud/BDD ✅ 90/90 · #024 FaceA_08 git ⏳ 18/60.

Le suivi détaillé, lot par lot, vit dans [`TODO_TRACKER.md`](TODO_TRACKER.md) — c'est la source de vérité du chantier.


---

## Architecture

```
   Markdown versionnés (source de vérité)
   faceA_*.md · faceB_*.md
                │
                ├── tools/parse_rich.py  → data/dictionnaire.json (entités typées)
                ├── tools/validate.py    → contrôle rubriques, doublons, vocabulaire OS
                └── tools/stats.py       → compteurs MVP, trous de couverture
                │
      ┌─────────┴──────────────┐
      │                        │
  web_preview/            Firebase (Firestore + Hosting)
  aperçu HTML offline          │
      │                        ▼
      └──────► Flutter (1 codebase) → Android · iOS · Web PWA · Windows · macOS · Linux
                  └─ SQLite FTS5 embarqué : recherche instantanée sans réseau
```

**Choix techniques actés** (voir [`DECISIONS.md`](DECISIONS.md)) :

| Décision | Pourquoi |
|---|---|
| **Flutter** plutôt que React-Native + Electron | Une seule codebase Dart, 6 cibles natives, maintenance solo tenable |
| **Firebase** (Firestore, Auth, Hosting) | Free tier suffisant pour le MVP, sync et PWA sans backend à maintenir |
| **SQLite FTS5 embarqué** | Recherche full-text instantanée **offline**, exigence produit non négociable |
| **Fiche riche v3** en Markdown | Les 7 colonnes du format tableau ne portaient pas contextes, dangers et subtilités |
| **Validateurs en Python, sans dépendance** | Reliables dans n'importe quel CI, exécutables en 2 secondes |

---

## Démarrage rapide

Prérequis : **Python 3.8+** uniquement pour la chaîne de données (aucune dépendance externe).

```bash
git clone https://github.com/Adolphechris/dictionnaire-it.git
cd dictionnaire-it

# 1. Compiler les Markdown en JSON (fusionne legacy + fiches v3)
python3 tools/parse_rich.py

# 2. Valider la conformité (rubriques manquantes, doublons, OS hors vocabulaire)
python3 tools/validate.py

# 3. Afficher la couverture du MVP
python3 tools/stats.py

# 4. Ouvrir l'aperçu web offline (recherche instantanée sur tout le dictionnaire)
python3 -m http.server 8000        # depuis la racine du dépôt
# puis ouvrir http://localhost:8000/web_preview/
```

> L'aperçu charge `data/dictionnaire.json` en `fetch()` : il doit donc être servi par un serveur HTTP local (un simple `http.server` suffit). Une fois chargé, il fonctionne **sans aucune connexion**.

### Les outils

| Outil | Rôle | Sortie |
|---|---|---|
| `tools/parse_rich.py` | Parse fiches v3 **+** tableaux legacy, fusionne les doublons riche→legacy | `data/dictionnaire.json` |
| `tools/validate.py` | Rubriques obligatoires, colonnes de tableaux, vocabulaire OS/catégories, doublons | rapport, code retour non nul si erreur |
| `tools/stats.py` | Couverture MVP, répartition OS / catégorie / niveau, fiches riches vs legacy | tableau de bord texte |
| `tools/md_to_json.py` | Extracteur historique du format tableau | `data/` |

Tout ajout de contenu **doit** passer par ce trio avant commit : c'est ce qui permet de tenir la cohérence à plusieurs centaines, puis à des milliers d'entrées.

---

## Structure du dépôt

```
.
├── faceA_01 → 08_*.md          # Face A : commandes (navigation, fichiers, contenu,
│                               #   processus, réseau, archives/paquets, aide/shell, git)
├── faceB_01 → 02_*.md          # Face B : sigles (généralistes, DevOps/Cloud/BDD)
├── data/
│   └── dictionnaire.json       # Entités compilées (généré — ne pas éditer à la main)
├── tools/                      # parse_rich · validate · stats · md_to_json
├── web_preview/index.html      # Aperçu web offline (un seul fichier, zéro build)
├── firebase.json · firestore.rules · firestore.indexes.json
├── README.md                   # ce fichier — vitrine du projet
├── 00_VISION.md                # cap produit (6 faces, 30 000+ entités à terme)
├── PLAN_IMPLEMENTATION.md      # les 10 phases du chantier
├── DATA_MODEL.md               # schéma d'entité universel
├── CONVENTIONS.md              # grammaire d'écriture des fiches
├── DECISIONS.md                # décisions techniques + pourquoi
├── TODO_TRACKER.md             # Kanban texte — SOURCE DE VÉRITÉ
└── CHANGELOG.md                # une entrée par session de travail
```

## Contribuer

1. **Lire `CONVENTIONS.md`** : le format des fiches n'est pas décoratif, il est parsé.
2. **Créer/éditer** un `face<X>_<NN>_<theme>.md` (noms en minuscules, underscores, pas d'espaces).
3. **Tout nouveau contenu s'écrit en Fiche riche v3** — le format tableau legacy est figé, il ne fait qu'être enrichi.
4. **Vérifier** : `python3 tools/parse_rich.py && python3 tools/validate.py && python3 tools/stats.py` — tout doit être vert.
5. **Mettre à jour** `TODO_TRACKER.md` (lot coché, compteurs) et `CHANGELOG.md` (une entrée par session).
6. **Committer** sur un message clair : `Lot #024 FaceA_08_git 12/60`.

> Règle d'or : aucune commande n'est ajoutée "à mémoire". Les exemples de chaque fiche doivent être réellement exécutés et vérifiés, et les dangers signalés par ⚠️.

### Ce qui fait refus machine

- Rubrique manquante ou champ vide sans `—` (tiret long) pour le signaler.
- OS en dehors du vocabulaire fermé (`Linux`, `macOS`, `Windows (CMD)`, `PowerShell`, combinaisons).
- Catégorie Face B hors liste, `|` non échappé dans une cellule, backticks déséquilibrés.
- Doublon de commande — le validateur signale aussi les fusions riche→legacy en attente.

## Gouvernance

Le projet est pensé pour survivre à des mois de travail en solo sans perdre le fil :

| Document | Rôle |
|---|---|
| `TODO_TRACKER.md` | Kanban texte : qu'est-ce qui est fait, en cours, prochain. Lu en début de session, écrit en fin de session. |
| `CHANGELOG.md` | Récit daté des sessions, avec les compteurs réels. |
| `DECISIONS.md` | Chaque arbitrage technique est justifié par écrit — et donc réversible en connaissance de cause. |
| `CONVENTIONS.md` | La grammaire du contenu, pour que 1 000 fiches se ressemblent. |
| `00_VISION.md` | Le produit visé à terme : 6 faces, 7 axes de recherche, 6 plateformes. |

## Feuille de route

- [x] **Phase 0** — Hygiène : git, gouvernance, corrections factuelles
- [x] **Phase 1** — Data : modèle d'entité, validateurs, générateur de JSON, statistiques
- [ ] **Phase 2** — Contenu MVP **← nous sommes ici (338 / 1000)**
- [ ] **Phase 3** — Recherche locale V1 (aperçu web, CLI `cherche.py`)
- [ ] **Phase 4** — Firebase : import Firestore, rules, hosting PWA
- [ ] **Phase 5** — App Flutter : SQLite FTS5, écrans Recherche / Détail / Favoris / Offline
- [ ] **Phase 6** — Desktop : Windows, macOS, Linux + raccourci global
- [ ] **Phase 7** — Passer à 5 000+ : import assisté, Meilisearch, contributions
- [ ] **Phase 8** — Recherche sémantique (langage naturel, « donne-moi l'équivalent Windows de… »)
- [ ] **Phase 9** — Stores et public

**Prochains lots de contenu** : `#024` git (60) → `#026` Docker/Kubernetes (50) → `#027` sysadmin (60) → `#028` paquets multi-OS (50) → `#029` réseau II & sécurité (60) → `#035-037` Face B (256).

## Licence et auteur

Projet porté par **Adolphe** — contenu rédigé en français, avec l'assistance d'agents IA pour la production et la validation machine (traçée dans `CHANGELOG.md`).

**Licence : à trancher.** Aucun fichier `LICENSE` n'existe à ce jour, le dépôt est donc *tous droits réservés* par défaut. Une licence ouverte (MIT pour le code des outils, CC BY-SA pour le contenu rédactionnel) est envisagée pour la phase de publication — la décision sera notée dans `DECISIONS.md` au moment du choix.


