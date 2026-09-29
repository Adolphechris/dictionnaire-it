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


## Tableau Face A (7 colonnes fixes)
`| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |`
Séparateur exemples : `·` (Alt+183). Pas de `,` ambiguë.
OS vocab fermé : `Linux` `macOS` `Windows (CMD)` `PowerShell` `Linux/macOS` `Linux/macOS/Windows` — tout autre → erreur validate.py.

## Tableau Face B (6 colonnes fixes)
`| sigle | signification | catégorie | description | exemple | voir_aussi |`
Catégories fermées : `Matériel` `Stockage` `Système` `Réseau` `Web` `Programmation` `Sécurité` `DevOps` `Concept` `Bureautique`.
`voir_aussi` : sigles séparés par `,` ou `—` si aucun. Ne jamais mettre de `|` dans une cellule (ni backticks déséquilibrés).

## Style rédactionnel
- rôle : verbe infinitif FR, ≤80 car. Ex: "Copier un fichier" pas "ça copie".
- syntaxe : backticks + `<obligatoire>` `[optionnel]`.
- exemples : 2-4 max, testés réellement.
- précautions : `⚠️` si destructif, `—` si RAS (tiret long, pas `-`).
- équivalents : `—` si aucun, sinon `cmd (OS)`.

## IDs
Donnés à l'import, pas à la main. Ne pas renommer une commande sans laisser alias.

## Workflow contribution
1. Éditer .md → 2. `python tools/validate.py` → 3. commit `faceA: ajoute curl, wget (#020)` → 4. update TODO_TRACKER + CHANGELOG
