# Conventions — Pour rester cohérent à 30 000 entrées

## Nommage fichiers
`face<LETTRE>_<NN>_<theme>.md` ex: `faceA_05_reseau.md`, `faceB_01_abreviations.md`
Jamais d'espaces, minuscules, underscores.

## Format LEGACY — Tableaux (154 existantes, ne plus en créer)
Face A 7 colonnes : `| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |`
Face B 6 colonnes : `| sigle | signification | catégorie | description | exemple | voir_aussi |`
Séparateur exemples : `·`. Précautions vides : `—`. Ne jamais mettre de `|` brut dans une cellule.

## Format RICHE v3 — Fiches (obligatoire pour tout nouveau contenu)
Une fiche = un bloc `##`. Modèle Face A :
```markdown
## `tar` — Archiver et compresser des fichiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contexte :** sauvegarde serveur, distribution logicielle, backup avant migration
**Rôle :** Créer et extraire des archives (souvent compressées).
**Syntaxe :** `tar [options] <archive> <fichiers>`
**Cas réguliers :**
- `tar -czf backup.tar.gz dossier/` — Sauvegarde compressée du dossier (backup quotidien)
- `tar -tzf backup.tar.gz` — Lister le contenu SANS extraire (vérification avant restauration)
- `tar -xzf backup.tar.gz -C /tmp/resto` — Extraire dans un dossier cible
**Origine :** Tape ARchive, Unix V7 (1979), bandes magnétiques ; standard POSIX.
**Subtilités/confusions :**
- Sans -z/-j/-J, tar ne compresse pas, il concatène.
- tar vs zip : tar préserve permissions Unix, zip non.
- `-f` doit être immédiatement suivi du nom d'archive.
**Urgences/dangers :** ⚠️ `tar -xzf arc -C /` écrase le système — toujours lister avec -t avant.
**Équivalents :** Compress-Archive (PowerShell), 7z (Windows)
**Voir aussi :** gzip, zip, rsync
```
Modèle Face B :
```markdown
## `CI` — Continuous Integration [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 85
**Signification :** Continuous Integration (Intégration Continue)
**Définition :** Pratique qui fusionne et teste le code automatiquement à chaque commit.
**Contextes :** équipe dev, pipeline GitHub Actions/GitLab CI, qualité logicielle
**Cas réguliers :**
- `Pipeline CI : lint + tests à chaque push` — Bloquer la fusion si les tests échouent
- `Badge CI vert sur README` — Preuve que la branche principale est saine
**Origine :** Grady Booch (1991), popularisé par Extreme Programming (Beck, 1999), explosé avec Jenkins (2011) puis GitHub Actions (2019).
**Subtilités/confusions :**
- CI vs CD : CI = tester/intégrer, CD = livrer/déployer. CI sans CD = tests sans mise en prod auto.
- CI vs Git simple : committer souvent sans pipeline n'est PAS de la CI.
- Faux vert : pipeline qui ne teste rien donne une fausse confiance.
**Exemple :** `.github/workflows/ci.yml qui lance pytest à chaque pull request`
**Voir aussi :** CD, DevOps, TDD
```
Règles : OS entre crochets avec vocabulaire existant. Champs en gras exacts (parser sensible). `—` si vide avec justification. Exemples testés réellement.

### Règles machine (contrôlées à chaque exécution)

- **Libellés de rubriques** : reconnus *sans tenir compte des accents ni de la casse* (`**Role :**` = `**Rôle :**`). Les libellés officiels restent accentués.
- **Listes à puces** : uniquement `- ` (jamais `*`). Une liste s'arrête à la première ligne vide **ou** à la rubrique suivante — ne jamais compter sur une rubrique en gras pour la clôturer (bug d'avalement corrigé le 01/10/2026, ~940 rubriques avaient disparu à l'import).
- **Rubriques multiples** : plusieurs rubriques peuvent partager une ligne (`**Niveau :** x | **Popularité :** y | **Aliases :** z`) — c'est le format standard de l'en-tête.
- **Titres composés** : `` `yum` / `dnf` — … `` crée l'entrée `yum` avec l'alias `dnf`. Un nom contenant une barre oblique reste insécable s'il est entre accents graves (`` `blue/green` ``).
- **Catégorie Face B** : la rubrique `**Catégorie :**` gagne si présente, sinon la catégorie est déduite du crochet du titre (`[Cloud/Réseau]` → `Cloud`, `Réseau`). Mapping canonique dans `tools/parse_rich.py` (`CAT_CANON`).
- **Signification Face B** : la rubrique `**Signification :**` gagne si présente, sinon le titre fait office de signification — le titre d'une fiche Face B doit donc être le développement du sigle.
- **OS** : jetons autorisés dans le crochet — `Linux`, `macOS`, `Windows`, `PowerShell`, `CMD`, `Cross`, distributions (`Debian`, `Ubuntu`, `RHEL`, `Fedora`, `CentOS`, `Alpine`, `Arch`, `SUSE`, `BSD`) et `Dev`, `Git`, `Docker`, `Android`, `iOS`. Tout autre jeton → avertissement `W-OS`.
- **`voir aussi`** : chaque cible doit être le nom exact ou un alias d'une entrée existante (sinon `W-LINK`). Pas d'indication d'OS entre parenthèses : `Set-Location`, jamais `Set-Location (PowerShell)`.
- **Popularité** : entier de 1 à 100.
- **Interdits** : `TODO`, `placeholder`, `xxx`, champ vide sans `—`, doublon de nom dans une même face.


## Tableau Face A (7 colonnes fixes)
`| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |`
Séparateur exemples : `·` (Alt+183). Pas de `,` ambiguë.
OS vocab fermé : `Linux` `macOS` `Windows (CMD)` `PowerShell` `Linux/macOS` `Linux/macOS/Windows` — tout autre → erreur validate.py.

## Tableau Face B (6 colonnes fixes)
`| sigle | signification | catégorie | description | exemple | voir_aussi |`
Catégories fermées : `Matériel` `Stockage` `Système` `Réseau` `Web` `Programmation` `Sécurité` `DevOps` `Concept` `Bureautique`.
`voir_aussi` : sigles séparés par `,` ou `—` si aucun. Ne jamais mettre de `|` dans une cellule (ni backticks déséquilibrés).

## Style rédactionnel
- rôle : phrase nominale ou verbe à l'infinitif en français, **cible ≤ 80 caractères, maximum dur 200** (au-delà → erreur `validate.py`). Ex : « Copier un fichier », jamais « ça copie ». Les rôles historiques plus longs sont tolérés jusqu'à relecture, tout nouveau contenu tient la cible.
- syntaxe : backticks + `<obligatoire>` `[optionnel]`.
- exemples : 2-4 max, testés réellement.
- précautions : `⚠️` si destructif, `—` si RAS (tiret long, pas `-`).
- équivalents : `—` si aucun, sinon `cmd (OS)`.

## IDs
Donnés à l'import, pas à la main. Ne pas renommer une commande sans laisser alias.

## Workflow contribution
1. Éditer le `.md` (nouveau contenu en **Fiche riche v3** uniquement).
2. `./tools/check.sh` — tests du parseur, validation, `parse_rich.py --check`, contrôle de dérive du JSON, statistiques, audit. Tout doit être vert.
3. Commit au format `faceB_05: ajoute Bluetooth, NFC (#039)`.
4. Mettre à jour `TODO_TRACKER.md` et `CHANGELOG.md` avec les compteurs réels.

## Sorties générées (ne jamais éditer à la main)
- `data/dictionnaire.json` — entités complètes (`version: 3`, ~2,5 Mo).
- `data/index.json` — index léger (`id`, `nom`, `aliases`, `os`, `categories`, `niveau`, `popularite`, `role_fr`, `source`) pour l'affichage instantané des listes.
- `updated_at` = date de modification la plus récente des sources : régénérer sans changer le contenu **ne produit aucun diff**.
- `tools/md_to_json.py` est **déprécié** (ancien schéma v2, conservé pour l'historique).
- Le format legacy (tableaux) est **figé** : 95 entrées restantes à migrer en v3, le parseur les gère encore mais aucun nouveau tableau n'est créé.
