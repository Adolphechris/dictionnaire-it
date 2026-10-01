# Décisions — Traçabilité (1 entrée = 1 décision, jamais de code sans noter pourquoi)

## 2026-09-29 — Flutter + Firebase + SQLite FTS5 (1 codebase, 6 OS)
Pourquoi : solo-dev, offline-first obligatoire, free tier Firebase suffisant pour MVP. Alternative écartée : React-Native+Electron (2 codebases).
## 2026-09-29 — Format Fiche Riche v3 (fini les tableaux pour le nouveau contenu)
Pourquoi : Adolphe exige "la totale" (contextes, urgences, cas réguliers, origines, subtilités/confusions). 7 colonnes incapables de porter ça. Legacy gardé + parsé, enrichissement progressif.
## 2026-09-29 — MVP porté de 500 à 1000 (600 A + 400 B)
Pourquoi : demande Adolphe. 1000 = seuil crédible "riche". Découpé en 14 lots pour ne pas perdre le fil.

## 2026-10-01 — Réparation du parseur : fin de l'avalement des rubriques (bug bloquant)
Symptôme : la lecture des puces `((?:\s*[-*].*\n?)+)` avalait les rubriques suivantes. Dégâts mesurés : **5 249 faux « cas réguliers »** et **3 439 fausses « subtilités »** sur 905 fiches riches ; les rubriques `Syntaxe`, `Précautions`, `Équivalents`, `Urgences/dangers` des fiches Face B étaient forcées à vide (**~940 rubriques rédigées jamais publiées**) ; le contrôle annoncé « 905 fiches conformes » était donc faussement vert.
Correctif : fin de liste à la première ligne vide ou à la rubrique suivante, puces `- ` uniquement, libellés insensibles aux accents/casse, lecture des rubriques multiples sur une même ligne, conservation de tous les champs Face B, alias automatiques des titres composés, normalisation des cibles `voir aussi` (retrait des `(OS)`).
Garde-fous : `tools/test_parse.py` (15 tests + fixtures) garantit notamment que **toute rubrique déclarée dans les .md se retrouve dans le JSON** (invariant `importées ≥ déclarées`). Effet mesurable : JSON de 4,3 Mo → 2,5 Mo (le junk disparaît), 2 titres composés récupérés (`yum`/`dnf`, `test`/`[`) → 1002 entrées.

## 2026-10-01 — Longueur du rôle : cible 80, maximum dur 200 caractères
871 rôles sur 1000 dépassaient 80 caractères (max 245) sans qu'aucun contrôle ne le signale. Réécrire 871 rôles dégraderait la précision technique pour un gain cosmétique : nouvelle règle **cible ≤ 80, max 200** (avertissement `W-ROLE` au-delà), troncature « voir plus » côté UI.

## 2026-10-01 — Catégorie Face B : rubrique prioritaire, sinon crochet du titre
Les 282 fiches Face B récentes n'ont pas de rubrique `**Catégorie :**` (l'information est dans le crochet : `[Cloud/Réseau]`). Le parseur déduit la catégorie du crochet via `CAT_CANON` (36 catégories canoniques) au lieu d'afficher le slug du fichier. La rubrique reste prioritaire quand elle est écrite.

## 2026-10-01 — Sortie JSON stable + index léger
`updated_at` = date de modification la plus récente des sources : régénérer le JSON sans changer le contenu ne produit plus aucun diff (avant : ~15 800 lignes de diff chaque jour à cause d'un `updated_at` quotidien). Ajout de `data/index.json` (~380 Ko) pour lister les 1002 entrées sans charger les 2,5 Mo de fiches.

## 2026-10-01 — Licences : MIT (code) + CC BY-SA 4.0 (contenu)
Un dépôt public sans licence est « tous droits réservés » par défaut, ce qui décourage la contribution. Code des outils/app = **MIT** (`LICENSE`) ; contenu rédactionnel (fiches, JSON, textes d'app) = **CC BY-SA 4.0** (`LICENSE-CONTENT.md`). Décision réversible à la demande d'Adolphe.

## 2026-10-01 — `md_to_json.py` déprécié
L'ancien pipeline (schéma v2, sans validation) est remplacé par `tools/parse_rich.py`. Le script refuse de s'exécuter sans `--force` et n'est conservé que pour l'historique.

## 2026-10-01 — Rituel de vérification : `tools/check.sh`
Un seul point d'entrée avant chaque commit : tests du parseur, validation, `parse_rich.py --check` (sans écriture), `--compare` (dérive du JSON committé), statistiques, audit qualité. Objectif : rendre impossible la publication d'un corpus incohérent.
