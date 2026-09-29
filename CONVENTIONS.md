# Conventions — Pour rester cohérent à 30 000 entrées

## Nommage fichiers
`face<LETTRE>_<NN>_<theme>.md` ex: `faceA_05_reseau.md`, `faceB_01_abreviations.md`
Jamais d'espaces, minuscules, underscores.

## Tableau Face A (7 colonnes fixes)
`| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |`
Séparateur exemples : `·` (Alt+183). Pas de `,` ambiguë.
OS vocab fermé : `Linux` `macOS` `Windows (CMD)` `PowerShell` `Linux/macOS` `Linux/macOS/Windows` — tout autre → erreur validate.py.

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
