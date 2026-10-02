# Face A — Commandes : GIT ET CONTRÔLE DE VERSION (fiches riches v3)

> Lot MVP #024 — cible 60 fiches. Avancement : 18/60 (bloc 1 socle Git : git, init, clone, status, add, commit, diff, push, pull, log, branch, switch, checkout, fetch — bloc 2 fusions & retours : merge, rebase, stash, reset). Format : `## \`commande\` — titre [OS]` + 10 rubriques obligatoires validées par `tools/parse_rich.py`.

## `git` — Contrôle de version distribué [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** —
**Contextes :** tout projet de code, travail en équipe, historique de versions, retour arrière
**Rôle :** Enregistrer l'histoire complète d'un projet (fichiers, auteurs, dates) et permettre de revenir à n'importe quel état antérieur.
**Syntaxe :** `git <sous-commande> [options] [args]`
**Cas réguliers :**
- `git status` — Où j'en suis (la commande réflexe, le plus courant)
- `git log --oneline --graph` — Voir l'histoire en une ligne par commit
- `git config --global user.email "toi@mail.fr"` — S'identifier une bonne fois
- `git help <cmd>` — Le manuel intégré de n'importe quelle sous-commande
**Origine :** Linus Torvalds (2005), pour développer le noyau Linux après le retrait de BitKeeper — distribué par conception : chaque clone contient tout l'historique.
**Subtilités/confusions :**
- Git ne stocke pas des différences mais des INSTANTANÉS (snapshots) complets du projet à chaque commit.
- « Distribué » : `git log`, `git diff`, `git blame` fonctionnent SANS réseau — le `push` n'est jamais obligatoire.
- Comprendre trois mots débloque tout le reste : index (zone de préparation), HEAD (position courante), objet SHA.
**Urgences/dangers :** ⚠️ `git push --force` sur une branche partagée écrase le travail des autres — ne jamais le faire sans `--force-with-lease`.
**Précautions :** Travailler sur des branches, commiter souvent ; `git reflog` reste le filet de secours des erreurs courantes.
**Équivalents :** SVN, Mercurial, Perforce (contrôle de version)
**Voir aussi :** git init, git clone, git commit, git push, git rebase

## `git init` — Créer un dépôt Git [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 80 | **Aliases :** —
**Contextes :** démarrer un projet, versionner un dossier existant, créer un dépôt local de test
**Rôle :** Transformer un dossier en dépôt Git en créant le répertoire caché `.git` qui contiendra tout l'historique.
**Syntaxe :** `git init [dossier]`
**Cas réguliers :**
- `git init` — Versionner le dossier courant (le plus courant)
- `git init -b main` — Branche principale nommée main d'office (git 2.28+)
- `git init --bare repo.git` — Dépôt SANS dossier de travail, pour servir de serveur partagé
- Rédiger `.gitignore` avant le premier commit — Exclure node_modules et .env dès le départ
**Origine :** Git 1.0 (2005) — `init` crée le système d'objets ; `--bare` vient de l'usage serveur où aucun fichier de travail n'a de sens.
**Subtilités/confusions :**
- `git init` dans un SOUS-dossier d'un dépôt existant crée un dépôt imbriqué (piège fréquent) : vérifier avec `git rev-parse --show-toplevel`.
- `.git` contient TOUT : le supprimer efface l'historique tout en laissant les fichiers de travail.
- Un dépôt `--bare` ne s'édite pas : on y `push` depuis un dépôt de travail.
**Urgences/dangers :** ⚠️ `git init` dans son dossier personnel (home) est très pénible à annuler : le `.git` parasite tous les sous-dossiers.
**Précautions :** Écrire `.gitignore` AVANT le premier commit ; ne jamais versionner de secret (`.env`, clés privées).
**Équivalents :** svnadmin create, hg init
**Voir aussi :** git clone, git status, git add, .gitignore

## `git clone` — Copier un dépôt complet [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** récupérer un projet, participer à un dépôt distant, créer une copie de travail rapide
**Rôle :** Télécharger un dépôt et TOUT son historique, puis créer un dépôt de travail prêt à l'emploi.
**Syntaxe :** `git clone <url> [dossier]`
**Cas réguliers :**
- `git clone https://github.com/org/projet.git` — Le réflexe (le plus courant)
- `git clone --depth 1 <url>` — Une seule version : rapide pour un build CI
- `git clone -b dev <url>` — Cloner directement sur une branche donnée
- `git clone /chemin/local/depot` — Copie locale (test, sauvegarde d'un dépôt)
**Origine :** Git 1.0 (2005) — l'équivalent d'un checkout complet : contrairement à SVN, `clone` rapporte l'intégralité des commits, pas seulement la dernière version.
**Subtilités/confusions :**
- Un clone contient le distant `origin` : `git log origin/main` marche immédiatement, mais cet historique ne s'actualise qu'avec `git fetch`.
- `--depth 1` (shallow) casse `git blame`, les logs profonds et souvent les tags : réservé à la CI.
- SSH (`git@github.com:...`) demande une clé ; HTTPS demande un JETON depuis que le mot de passe est refusé.
**Urgences/dangers :** ⚠️ Cloner un dépôt inconnu puis exécuter ses scripts = exécuter du code arbitraire : relire avant tout `npm install` ou `make`.
**Précautions :** Vérifier l'URL du dépôt (typosquatting) ; `git remote -v` pour contrôler ce qu'on a réellement cloné.
**Équivalents :** svn checkout, hg clone
**Voir aussi :** git init, git remote, git fetch, git pull

## `git status` — État de la zone de travail [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** git st (alias courant)
**Contextes :** avant chaque commit, comprendre ce qui a changé, reprendre un travail interrompu
**Rôle :** Afficher les fichiers modifiés, préparés (index) ou non suivis, et la position de la branche par rapport au distant.
**Syntaxe :** `git status [options]`
**Cas réguliers :**
- `git status` — Le bilan complet (le plus courant, à faire en premier systématiquement)
- `git status -s` — Format court, une ligne par fichier (idéal en script)
- `git status -sb` — Court + position de la branche vs `origin/main`
- `git status --ignored` — Voir ce que `.gitignore` exclut (debug d'exclusion)
**Origine :** Git 1.0 (2005) — `status` compare les trois états internes : dossier de travail, index, dernier commit (HEAD).
**Subtilités/confusions :**
- Trois listes, trois sens : *untracked* (jamais ajoutés) ≠ *modified* (pas dans l'index) ≠ *staged* (prêts à commiter).
- « Your branch is ahead of 'origin/main' by 3 commits » veut dire : à pousser — ce n'est PAS une erreur.
- Un fichier « modified » sans `git diff` visible = fins de ligne CRLF/LF ou droits (`chmod +x`) qui ont bougé.
**Urgences/dangers :** — (lecture seule : `git status` ne modifie jamais le dépôt)
**Précautions :** Toujours `git status` avant un `git add .` : c'est ce qui évite de commiter un `.env` ou un binaire de 200 Mo.
**Équivalents :** svn status, hg status
**Voir aussi :** git add, git diff, git commit, .gitignore

## `git add` — Préparer les modifications pour le commit [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** git stage (synonyme officiel)
**Contextes :** sélectionner ce qui entre dans le prochain commit, ajouter de nouveaux fichiers, construire un commit propre
**Rôle :** Copier l'état des fichiers dans l'INDEX (la zone de préparation) : tout ce qui est ajouté sera inclus dans le prochain commit.
**Syntaxe :** `git add [options] <fichiers>`
**Cas réguliers :**
- `git add src/main.py` — Ajouter un fichier précis (le plus courant, la bonne habitude)
- `git add -p` — Ajouter PAR MORCEAUX, écran par écran (commit propre garanti)
- `git add .` — Tout le dossier courant (à n'utiliser qu'après un `git status`)
- `git add -u` — Seulement les fichiers DÉJÀ suivis (jamais les nouveaux)
**Origine :** Git 1.0 (2005) — l'index est l'idée la plus déroutante de Git : c'est une MAQUETTE du prochain commit, pas un simple « file tracking ».
**Subtilités/confusions :**
- `git add` n'envoie RIEN sur le réseau : il prépare uniquement. Le réseau, c'est `push`.
- Après un `git add` puis une nouvelle modification du même fichier : il faut re-`add` (sinon le commit garde la version ajoutée).
- `git add -A` (tout, partout) vs `git add .` (dossier courant) : le premier peut traverser tout l'arbre.
**Urgences/dangers :** ⚠️ `git add .` sur un dépôt sans `.gitignore` publié `.env`, `id_rsa`, `node_modules` — un secret commité doit être considéré COMPROMIS (rotation obligatoire).
**Précautions :** `git add -p` par défaut sur du code partagé ; vérifier `git diff --cached` avant de commiter.
**Équivalents :** svn add (sans notion d'index), hg add
**Voir aussi :** git status, git commit, git diff, .gitignore

## `git commit` — Enregistrer un instantané [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** valider une étape de travail, documenter une décision, sceller un changement réversible
**Rôle :** Créer un commit : instantané de l'index + message + auteur + empreinte SHA immuable.
**Syntaxe :** `git commit [options] [-m "message"]`
**Cas réguliers :**
- `git commit -m "corrige le timeout de connexion"` — Le réflexe (le plus courant)
- `git commit` — Ouvre l'éditeur pour un message long (corps explicatif)
- `git commit -a -m "hotfix"` — Commet les fichiers DÉJÀ suivis modifiés, sans `add`
- `git commit --amend --no-edit` — Corriger le dernier commit (message ou oubli local)
**Origine :** Git 1.0 (2005) — un commit est un nœud immuable pointant vers son parent : c'est ce qui rend l'histoire infalsifiable et l'écrasement possible uniquement en réécrivant la suite.
**Subtilités/confusions :**
- `commit -a` OMET les nouveaux fichiers non suivis : le piège du « mon fichier n'est pas dans le commit ».
- Un commit local n'est PAS partagé : tant qu'il n'est pas poussé, `--amend` est sans danger ; après `push`, réécrire l'histoire dérange l'équipe.
- Message impératif (« corrige X » et non « corrigé ») : convention héritée de Torvalds, lisible dans `git log`.
**Urgences/dangers :** ⚠️ Committer un SECRET (token, clé privée) = exposition durable même après suppression : il faut purger l'historique (`filter-repo`) ET révoquer le secret.
**Précautions :** Un commit = une idée ; relire `git diff --cached` ; message qui explique le POURQUOI, pas le QUOI.
**Équivalents :** svn commit (qui pousse directement), hg commit
**Voir aussi :** git add, git log, git reset, git revert

## `git diff` — Voir les différences [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** —
**Contextes :** relecture avant commit, comparaison de branches, compréhension d'un changement inconnu
**Rôle :** Afficher les écarts ligne à ligne entre deux états du projet (dossier de travail, index, commit, branche).
**Syntaxe :** `git diff [cible] [fichiers]`
**Cas réguliers :**
- `git diff` — Ce qui a changé depuis le dernier `add` (le plus courant)
- `git diff --cached` — Ce qui EST PRÉPARÉ pour le commit (à lire avant chaque commit)
- `git diff main..ma-branche` — L'écart complet avec la branche principale
- `git diff HEAD~3 src/` — Ce qui a bougé sur 3 commits dans un dossier
**Origine :** Git 1.0 (2005) — `diff` est le wrapper Git du format unifié (1979, Unix) ; Git le recalcule à la demande, il ne le stocke pas.
**Subtilités/confusions :**
- `git diff A B` (avec ESPACE) compare deux objets ; `git diff A..B` compare aussi mais `A...B` (3 points) compare depuis leur ancêtre commun : distinction capitale dans les pull requests.
- `git diff` seul ne montre PAS les fichiers non suivis : il faut `git diff --stat` + `git status` pour tout voir.
- Sortie colorée et paginée par `less` : `q` pour sortir, `/mot` pour chercher, `--no-pager` pour enchaîner dans un script.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Activer `diff.color.ui=auto` ; pour les binaires, `git diff --stat` ne montre qu'un nombre de lignes : utiliser un outil dédié.
**Équivalents :** diff -u (Unix), svn diff, WinMerge (GUI)
**Voir aussi :** git status, git add, git log, git show

## `git push` — Publier ses commits vers un dépôt distant [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** partager du travail, alimenter une pull request, sauvegarder une branche sur le serveur
**Rôle :** Envoyer ses commits locaux vers une branche distante pour les partager avec l'équipe.
**Syntaxe :** `git push [remote] [branche]`
**Cas réguliers :**
- `git push` — Pousser la branche suivie (le plus courant)
- `git push -u origin feature-x` — Premier push : crée la branche et lie le suivi
- `git push --force-with-lease` — Réécrire prudemment après un rebase personnel
- `git push --delete origin branche-morte` — Supprimer une branche fusionnée côté serveur
**Origine :** Git 1.0 (2005) — le `push` est ce qui distingue Git de SVN : chacun publie depuis son propre dépôt, modèle dont est née la pull request.
**Subtilités/confusions :**
- Un commit non poussé n'existe PAS pour l'équipe : il ne vit que sur ta machine (panne = perte).
- `push` refuse un historique divergent : c'est une protection, pas un bug — il faut d'abord `pull --rebase`.
- `--force` écrase sans regarder ; `--force-with-lease` refuse si quelqu'un a poussé entre-temps.
**Urgences/dangers :** ⚠️ `git push --force` sur `main` peut détruire le travail des collègues et casser les environnements — réservé aux branches personnelles.
**Précautions :** Relire `git log origin/main..HEAD --oneline` avant de pousser ; protéger les branches clés côté serveur.
**Équivalents :** svn commit (pousse directement), hg push
**Voir aussi :** git pull, git fetch, git remote, git rebase

## `git pull` — Récupérer et intégrer les changements distants [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** démarrer la journée, synchroniser avant de travailler, mettre à jour un serveur
**Rôle :** Combinaison de `git fetch` (télécharger) puis `git merge` (intégrer) depuis la branche suivie.
**Syntaxe :** `git pull [remote] [branche]`
**Cas réguliers :**
- `git pull` — Se mettre à jour sur la branche courante (le plus courant)
- `git pull --rebase` — Rejouer tes commits PAR-DESSUS le distant (historique linéaire)
- `git pull --ff-only` — Refuser si ce n'est pas une avance simple : le plus sûr en équipe
- `git pull origin main` — Amener `main` dans la branche courante avant une PR
**Origine :** Git 1.0 (2005) — `pull` = fetch + merge par défaut ; depuis Git 2.27, Git avertit et recommande de choisir explicitement merge ou rebase.
**Subtilités/confusions :**
- `pull` peut créer un COMMIT DE FUSION parasite sans demander : `--ff-only` ou `--rebase` l'évitent.
- `git fetch` seul est TOUJOURS sans danger : il ne touche pas ton travail, il actualise seulement `origin/...`.
- `git config --global pull.rebase true` (ou `false`) fixe l'habitude d'équipe et supprime l'avertissement.
**Urgences/dangers :** ⚠️ `git pull` avec un travail non committé peut refuser ou créer un conflit pénible : `git stash` ou commit d'abord.
**Précautions :** `git fetch` puis `git log HEAD..origin/main` pour voir ce qui arrive avant d'intégrer.
**Équivalents :** svn update, hg pull
**Voir aussi :** git fetch, git merge, git rebase, git stash

## `git log` — Explorer l'histoire du projet [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** git lg (alias courant)
**Contextes :** comprendre qui a changé quoi, retrouver l'origine d'un bug, préparer des notes de version
**Rôle :** Lister les commits avec auteur, date et message, filtrables par fichier, auteur, période ou contenu.
**Syntaxe :** `git log [options] [chemins]`
**Cas réguliers :**
- `git log --oneline --graph --decorate -20` — La vue compacte de l'arbre (le plus courant)
- `git log -p src/api.py` — Les diffs successifs d'un fichier
- `git log --author=adolphe --since="2 weeks ago"` — Filtrer par auteur et période
- `git log -S "token_cache" --oneline` — Quel commit a INTRODUIT ou supprimé ce texte
**Origine :** Git 1.0 (2005) — l'histoire est un graphe orienté acyclique : Git le reconstruit à la demande, d'où la visualisation multi-branches.
**Subtilités/confusions :**
- `git log` ne montre que la branche COURANTE : pour tout voir, ajouter `--all`.
- `-S "texte"` (apparition du texte) ≠ `-G "regex"` (ligne de diff correspondante) : l'un retrouve le bug, l'autre passe à côté.
- `HEAD~1` = un commit avant ; `HEAD^` = le parent — les deux diffèrent sur un commit de fusion.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Sortir du pager avec `q` ; dans un script, ajouter `--no-pager` et `--pretty=format:`.
**Équivalents :** svn log, hg log, gitk (graphique)
**Voir aussi :** git diff, git blame, git show, git reflog

## `git branch` — Lister, créer et supprimer des branches [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** isoler une fonctionnalité, préparer un correctif d'urgence, ranger les branches mortes
**Rôle :** Gérer les branches : les lister, en créer une pointant sur un commit, en supprimer une fusionnée.
**Syntaxe :** `git branch [options] [nom] [commit]`
**Cas réguliers :**
- `git branch` — Lister les branches locales (le plus courant)
- `git branch feature-x` — Créer SANS y aller (puis `git switch feature-x`)
- `git branch -d feature-x` — Supprimer seulement si DÉJÀ fusionnée (sécurisé)
- `git branch -v` — Voir le dernier commit de chaque branche avant de nettoyer
**Origine :** Git 1.0 (2005) — une branche n'est qu'un CURSEUR de 41 octets vers un commit : créer et changer de branche coûte quasi nul, contrairement à SVN où la branche est une copie.
**Subtilités/confusions :**
- `-d` refuse si la branche n'est pas fusionnée ; `-D` force et peut perdre des commits.
- Supprimer une branche LOCALE ne touche pas la DISTANTE : il faut `git push --delete origin nom`.
- `git branch -a` révèle les branches distantes mourantes : `git remote prune origin` les nettoie.
**Urgences/dangers :** ⚠️ `git branch -D` sur une branche non fusionnée perd son travail : relire `git log nom-branche` avant.
**Précautions :** Nommer les branches par intention (`fix-timeout`, pas `test2`) ; nettoyer régulièrement.
**Équivalents :** svn branch (copie coûteuse), hg branch
**Voir aussi :** git switch, git checkout, git merge, git worktree

## `git switch` — Changer de branche [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** —
**Contextes :** passer d'une fonctionnalité à l'autre, revenir sur main, créer une branche en un pas
**Rôle :** Changer la branche courante du dossier de travail — spécialisation lisible de l'ancienne commande `git checkout`.
**Syntaxe :** `git switch [options] [branche]`
**Cas réguliers :**
- `git switch main` — Revenir sur la branche principale (le plus courant)
- `git switch -c feature-x` — Créer ET basculer (remplace `checkout -b`)
- `git switch -` — Retourner à la branche précédente (comme `cd -`)
- `git switch --detach HEAD~5` — Explorer un état passé sans modifier de branche
**Origine :** Git 2.23 (2019) — `checkout` faisait TROP de choses (branchage + restauration de fichiers) ; la communauté a demandé deux commandes distinctes : `switch` et `restore`.
**Subtilités/confusions :**
- `git checkout` reste valide partout, mais sur Git récent `switch`/`restore` lèvent l'ambiguïté à la lecture.
- Git refuse le switch si tes modifications non committées seraient ÉCRASÉES : committer ou `stash` d'abord.
- `--detach` = HEAD pointe sur un commit sans branche : tout commit fait là est orphelin (récupérable via `reflog`).
**Urgences/dangers :** ⚠️ En HEAD détaché, un `git switch main` fait disparaître les commits créés entre deux (visuellement) — créer une branche avant de travailler.
**Précautions :** `git status` avant de changer de branche ; vérifier `git branch --show-current` après.
**Équivalents :** svn switch, hg update
**Voir aussi :** git checkout, git branch, git restore, git stash

## `git checkout` — Basculer un état (branche ou fichiers) [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** revenir sur une version antérieure, restaurer un fichier abîmé, explorer un tag
**Rôle :** Multi-usage historique : changer de branche, restaurer un fichier depuis un commit, ou détacher HEAD sur un commit donné.
**Syntaxe :** `git checkout <branche|commit|-- fichier>`
**Cas réguliers :**
- `git checkout main` — Changer de branche (le plus courant)
- `git checkout -- src/app.py` — JETER les modifications locales de ce fichier
- `git checkout v1.2.0` — Explorer le code tel que livré en v1.2.0
- `git checkout -b hotfix` — Créer et basculer sur une nouvelle branche
**Origine :** Git 1.0 (2005) — le couteau suisse originel ; sa surcharge de sens est la raison de la scission en `switch` + `restore` (Git 2.23).
**Subtilités/confusions :**
- `git checkout X` et `git checkout -- X` n'ont RIEN à voir : le premier navigue, le second DETRUIT tes changements. Toujours vérifier le `--`.
- En Git ancien, `git checkout B` avec un travail en cours peut emporter les modifications non commitées sur l'autre branche : déstabilisant.
- Un checkout de commit met en HEAD détaché : les nouveaux commits ne sont sur aucune branche.
**Urgences/dangers :** ⚠️ `git checkout -- .` efface TOUTES les modifications non commitées du dépôt, sans corbeille ni confirmation.
**Précautions :** Préférer `git switch` et `git restore` (plus sûrs à relire) ; sur un fichier précieux, faire une copie avant.
**Équivalents :** svn switch, svn revert, hg update
**Voir aussi :** git switch, git restore, git branch, git stash

## `git fetch` — Télécharger le distant sans rien toucher [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** regarder ce qui a changé avant de décider, alimenter un tableau de bord CI, préparer un rebase
**Rôle :** Récupérer les commits et références du dépôt distant dans `origin/...` SANS modifier ton travail.
**Syntaxe :** `git fetch [remote] [options]`
**Cas réguliers :**
- `git fetch origin` — Mettre à jour les références distantes (le plus courant)
- `git fetch --all --prune` — Tous les distants + nettoyage des branches supprimées
- `git log HEAD..origin/main --oneline` — Ce que les autres ont ajouté
- `git diff origin/main -- src/` — Comparer son travail au distant, sans fusionner
**Origine :** Git 1.0 (2005) — la séparation fetch/merge est le cœur du modèle distribué : on peut examiner le travail d'autrui AVANT de l'accepter.
**Subtilités/confusions :**
- Après `fetch`, tes fichiers ne bougent PAS : `origin/main` est une copie, pas ton dossier de travail.
- `git fetch` ne supprime pas par défaut les branches effacées côté serveur : `--prune` le fait.
- `git pull` = `fetch` + intégration : préférer fetch puis décider (`merge` ou `rebase`).
**Urgences/dangers :** — (aucun effet sur le dossier de travail, jamais destructif)
**Précautions :** `fetch` avant toute décision de réécriture d'historique pour éviter d'écraser du travail récent.
**Équivalents :** svn status -u (sans télécharger l'historique), hg fetch
**Voir aussi :** git pull, git push, git remote, git rebase

## `git merge` — Fusionner deux branches [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** intégrer une fonctionnalité dans main, remonter un correctif, réconcilier deux historiques
**Rôle :** Créer un commit de fusion qui réunit deux branches, en réconciliant leurs modifications.
**Syntaxe :** `git merge [options] <branche>`
**Cas réguliers :**
- `git merge feature-x` — Intégrer la fonctionnalité dans la branche courante (le plus courant)
- `git merge --no-ff feature-x` — Forcer un commit de fusion même en avance simple (traçabilité PR)
- `git merge --abort` — Abandonner une fusion en conflit et revenir en arrière
- `git merge --squash feature-x` — Emporter le travail EN UN SEUL commit (historique propre)
**Origine :** Git 1.0 (2005) — la fusion à trois voies (ancêtre commun + deux branches) vient du diff3 (1990) ; Git ne fusionne que depuis l'ancêtre commun trouvé automatiquement.
**Subtilités/confusions :**
- Fast-forward : sans divergence, Git déplace juste le curseur — AUCUN commit de fusion n'est créé (d'où `--no-ff` en équipe).
- Un conflit se résout ÉDITER puis `git add` puis `git commit` : beaucoup croient qu'il faut `git merge --continue`.
- `merge` garde l'histoire telle quelle ; `rebase` la RÉÉCRIT : merge pour l'intégration partagée, rebase pour son travail privé.
**Urgences/dangers :** ⚠️ Résoudre un conflit en prenant « le leur » ou « le nôtre » à l'aveugle perd du code : lire chaque bloc `<<<<<<<`.
**Précautions :** `git mergetool` ou l'éditeur pour les conflits ; `git diff --check` repère les marqueurs oubliés avant de commiter.
**Équivalents :** svn merge, hg merge
**Voir aussi :** git rebase, git pull, git branch, git log

## `git rebase` — Rejouer ses commits ailleurs [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** synchroniser une branche de travail, nettoyer des commits avant une PR, appliquer un correctif sur plusieurs versions
**Rôle :** Recréer ses commits UN PAR-DESSUS une autre base : l'historique devient linéaire et lisible.
**Syntaxe :** `git rebase [options] <nouvelle-base>`
**Cas réguliers :**
- `git rebase main` — Rejouer ses commits par-dessus main (le plus courant)
- `git rebase -i HEAD~5` — Réordonner, grouper (`squash`), modifier 5 commits
- `git rebase --continue` — Reprendre après avoir résolu un conflit
- `git rebase --abort` — Annuler et retrouver l'état d'avant, intact
**Origine :** Git 1.0 (2005) — le rebase recrée des commits NEUFS (nouveaux SHA) : c'est pourquoi il n'est sûr que sur du travail non poussé.
**Subtilités/confusions :**
- `rebase` réécrit l'identité des commits : après un rebase local, pousser exige `--force-with-lease`.
- Ne JAMAIS rebaser une branche que d'autres utilisent : leurs bases ne correspondent plus.
- `rebase -i` demande un éditeur : configurer `git config --global core.editor "nano"` évite de rester bloqué dans Vim.
**Urgences/dangers :** ⚠️ Rebase sur branche partagée = le piège n°1 de Git en équipe : les collègues doivent re-`pull` et peuvent perdre du travail.
**Précautions :** Toujours vérifier `git status` propre avant ; `git reflog` garde la version d'avant en cas de doute.
**Équivalents :** hg rebase (extension), svn : aucune équivalence propre
**Voir aussi :** git merge, git cherry-pick, git reflog, git push

## `git stash` — Mettre son travail de côté temporairement [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** —
**Contextes :** devoir changer de branche d'urgence, tester un état propre, récupérer un stash oublié
**Rôle :** Ranger les modifications non commitées dans une pile pour retrouver un dossier de travail PROPRE, puis les rejouer plus tard.
**Syntaxe :** `git stash [push [-m "message"] | pop | apply | list | drop]`
**Cas réguliers :**
- `git stash` — Tout ranger pour changer de branche (le plus courant)
- `git stash pop` — Récupérer et RETIRER le dernier stash (reprise de travail)
- `git stash list` — Voir ce qui est rangé (`stash@{0}`, `stash@{1}`…)
- `git stash -u` — Inclure aussi les fichiers NON SUIVIS (souvent oubliés)
**Origine :** Git 1.0 (2005) — le stash est stocké comme des commits dans une référence spéciale : il survit aux changements de branche mais PAS à un `git clean -f` mal placé ni au nettoyage du GC après 90 jours.
**Subtilités/confusions :**
- `pop` applique ET supprime ; `apply` applique en LE GARDANT : en cas de doute, `apply` d'abord.
- Le stash est une PILE globale au dépôt, pas liée à la branche : on peut le rejouer sur une autre branche (conflits possibles).
- `git stash` ignore les fichiers non suivis SANS `-u` et les fichiers ignorés SANS `-a` : d'où des « disparitions » mal comprises.
**Urgences/dangers :** ⚠️ Un `git stash` mal nommé finit oublié des mois : `git stash list` régulièrement, les stash de plus de 90 jours sont éligibles au nettoyage.
**Précautions :** Mettre un message (`git stash push -m "avant refactor API"`) ; préférer un commit WIP poussé sur une branche pour du travail longue durée.
**Équivalents :** hg shelve, svn : pas d'équivalent (copie manuelle)
**Voir aussi :** git status, git worktree, git diff, git clean

## `git reset` — Déplacer HEAD (annuler plus ou moins profondément) [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 76 | **Aliases :** —
**Contextes :** annuler un commit pas encore poussé, dé-préparer des fichiers, revenir à un état de référence en local
**Rôle :** Replacer HEAD (et la branche courante) sur un autre commit, avec trois niveaux de profondeur sur l'index et le dossier de travail.
**Syntaxe :** `git reset [--soft|--mixed|--hard] <commit>`
**Cas réguliers :**
- `git reset --soft HEAD~1` — Décommetter le dernier commit EN GARDANT tout prêt à re-commit (le plus utile)
- `git reset HEAD src/x.py` — Dé-préparer un fichier ajouté par erreur
- `git reset --hard origin/main` — Recaler sa branche locale sur le distant (jettes tes commits locaux)
- `git reset --mixed HEAD~3` — Revenir 3 commits en arrière en gardant les modifications
**Origine :** Git 1.0 (2005) — les trois modes correspondent aux trois zones de Git : HEAD (histoire), index (préparation), dossier de travail (fichiers) ; `--hard` touche les trois.
**Subtilités/confusions :**
- `--soft` garde tout, `--mixed` (défaut) garde les fichiers mais vide l'index, `--hard` détruit les modifications locales.
- `reset` LOCAL ne dit rien au dépôt distant : pour « annuler » publiquement, c'est `git revert` qu'il faut.
- `reset HEAD~1` puis `commit` produit un historique différent de `revert` : le premier réécrit, le second ajoute.
**Urgences/dangers :** ⚠️ `git reset --hard` est la commande qui fait le plus pleurer : elle écrase le travail non commité SANS confirmation. Vérifier `git status` avant.
**Précautions :** `git reflog` conserve les positions précédentes (90 jours par défaut) : c'est le recours après un reset raté.
**Équivalents :** svn revert (fichiers seulement), hg revert / hg strip
**Voir aussi :** git revert, git checkout, git restore, git reflog

## `git revert` — Annuler un commit publiquement [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** annuler un commit déjà poussé sur le serveur, corriger une erreur sur branche partagée, garder l'historique intact
**Rôle :** Créer un NOUVEAU commit qui inverse exactement les modifications introduites par un commit précédent.
**Syntaxe :** `git revert [options] <commit>`
**Cas réguliers :**
- `git revert HEAD` — Annuler le tout dernier commit en créant un commit inverse (le plus courant)
- `git revert 4b2a1c` — Annuler un commit spécifique identifié par son SHA
- `git revert -n HEAD` — Préparer l'inversion dans l'index SANS commiter immédiatement (permet d'inverser plusieurs commits)
- `git revert --abort` — Interrompre l'inversion en cas de conflit complexe
**Origine :** Git 1.0 (2005) — conçu spécifiquement pour le travail collaboratif : au lieu d'effacer le passé (comme reset), revert ajoute une page d'histoire pour corriger.
**Subtilités/confusions :**
- `revert` ne supprime PAS le commit original : il crée un commit complémentaire (histoire 100% conservée).
- Inverser un commit de fusion (`merge commit`) exige l'option `-m 1` pour indiquer quelle branche parent garder comme référence.
- Si le fichier a été modifié depuis, `revert` peut générer des conflits de fusion qu'il faut résoudre manuellement.
**Urgences/dangers :** ⚠️ `git revert -m 1` sur une fusion invalide temporairement la branche fusionnée : pour réintroduire cette branche plus tard, il faudra revert le revert.
**Précautions :** Préférer `git revert` à `git reset` dès que les commits ont été poussés sur une branche partagée.
**Équivalents :** svn revert (différent : svn annule en local), hg backout
**Voir aussi :** git reset, git commit, git log, git checkout

## `git cherry-pick` — Appliquer un commit spécifique [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** rapatrier un correctif d'une branche à une autre, appliquer une fonctionnalité isolée sans fusionner toute la branche
**Rôle :** Sélectionner un commit existant sur une autre branche et appliquer ses modifications exactes sur la branche courante.
**Syntaxe :** `git cherry-pick [options] <commit>`
**Cas réguliers :**
- `git cherry-pick 7f9a2b` — Appliquer un commit donné sur la branche actuelle (le plus courant)
- `git cherry-pick -x <commit>` — Ajouter la mention d'origine « (cherry picked from commit...) » dans le message
- `git cherry-pick A..B` — Appliquer une série séquentielle de commits
- `git cherry-pick --continue` — Reprendre après avoir résolu un conflit
**Origine :** Git 1.0 (2005) — métaphore de la cueillette de cerises (« pick only what you need ») dans les arbres d'historique.
**Subtilités/confusions :**
- `cherry-pick` génère un NOUVEAU commit avec un nouveau SHA, même si le contenu est identique.
- En cas de conflit, Git s'arrête en mode cherry-pick : `git cherry-pick --abort` permet d'annuler proprement.
- Utiliser abusivement `cherry-pick` au lieu d'une vraie fusion produit des commits en double et complique les merges futurs.
**Urgences/dangers :** ⚠️ Cherry-picker un commit de merge exige `-m` et peut semer la confusion dans l'arbre généalogique du projet.
**Précautions :** Toujours privilégier `git merge` ou `git rebase` si l'on souhaite intégrer l'intégralité d'une branche.
**Équivalents :** hg graft, svn merge -c
**Voir aussi :** git merge, git rebase, git log, git revert

## `git bisect` — Recherche dichotomique de bugs [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 72 | **Aliases :** —
**Contextes :** identifier quel commit a introduit une régression, isoler un bug furtif parmi des centaines de commits
**Rôle :** Effectuer une recherche binaire (dichotomie) dans l'historique des commits pour trouver la révision exacte ayant causé une panne.
**Syntaxe :** `git bisect <start|bad|good|reset|run>`
**Cas réguliers :**
- `git bisect start` — Démarrer la session de débogage dichotomique
- `git bisect bad` — Déclarer le commit actuel comme défectueux (bug présent)
- `git bisect good v1.0` — Déclarer un commit ancien connu comme fonctionnel
- `git bisect run pytest` — Automatiser entièrement la recherche en exécutant un script d'invariance à chaque étape
**Origine :** Git 1.0 (2005) — l'une des fonctionnalités les plus puissantes de Git, tirant parti de la structure en graphe acyclique dirigé (DAG).
**Subtilités/confusions :**
- `bisect` découpe l'intervalle de commits par moitié : 1000 commits nécessitent seulement 10 étapes de test ($2^{10} = 1024$).
- `git bisect skip` permet de sauter un commit intermédiaire qui ne compile pas ou ne peut pas être testé.
- Ne pas oublier `git bisect reset` à la fin pour revenir sur la branche de travail initiale.
**Urgences/dangers :** — (aucun danger pour le dépôt : bisect ne fait que déplacer HEAD temporairement)
**Précautions :** S'assurer que le test de vérification est 100% déterministe avant de lancer `git bisect run`.
**Équivalents :** hg bisect, svn (pas d'outil natif équivalent)
**Voir aussi :** git log, git checkout, git status, git blame

## `git blame` — Identifier l'auteur ligne par ligne [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** git annotate (synonyme)
**Contextes :** comprendre pourquoi une ligne de code a été écrite, contacter l'auteur original, enquêter sur un bug
**Rôle :** Afficher pour chaque ligne d'un fichier l'auteur, la date et le SHA du dernier commit qui l'a modifiée.
**Syntaxe :** `git blame [options] <fichier>`
**Cas réguliers :**
- `git blame src/index.js` — Inspecter tout le fichier (le plus courant)
- `git blame -L 40,60 src/index.js` — Limiter l'inspection aux lignes 40 à 60
- `git blame -w src/index.js` — Ignorer les changements de pure mise en forme (espaces, indentation)
- `git blame -C src/index.js` — Détecter si les lignes proviennent d'un autre fichier (copier-coller/refactoring)
**Origine :** Git 1.0 (2005) — tiré de la commande Unix traditionnelle `blame` / `annotate` pour attribuer la responsabilité du code.
**Subtilités/confusions :**
- `blame` (blâmer) porte un nom négatif, mais son but premier est l'explication et la traçabilité contextuelle.
- Un reformatage global du code (ex: Prettier, Black) peut masquer les vrais auteurs : utiliser `.git-blame-ignore-revs` pour l'ignorer.
- `git blame` inspecte le fichier tel qu'il est sur HEAD par défaut, mais accepte aussi n'importe quel SHA ou branche.
**Urgences/dangers :** — (commande de lecture seule sans risque)
**Précautions :** Utiliser `-w` et `-C` pour éviter les faux positifs causés par les refactorisations cosmétiques.
**Équivalents :** svn blame / svn annotate, hg blame
**Voir aussi :** git log, git show, git log -p, git config

## `git reflog` — Historique des mouvements de HEAD [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** secourir un commit perdu après un reset hard ou une branche supprimée, retrouver un état antérieur précis
**Rôle :** Enregistrer la liste chronologique de TOUS les déplacements de HEAD en local, offrant une traçabilité totale même pour les commits orphelins.
**Syntaxe :** `git reflog [show | expire | delete]`
**Cas réguliers :**
- `git reflog` — Afficher l'historique récent de HEAD (le réflexe d'urgence)
- `git reset --hard HEAD@{2}` — Revenir à l'état où se trouvait HEAD il y a deux actions
- `git reflog show main` — Inspecter uniquement les mouvements de la référence `main`
- `git checkout HEAD@{1}` — Examiner un état temporaire perdu sans modifier les branches
**Origine :** Git 1.4 (2006) — acronyme de « Reference Log ». C'est le journal de bord local qui rend Git quasi incassable.
**Subtilités/confusions :**
- Le `reflog` est 100% LOCAL : il ne s'envoie jamais au serveur lors d'un `push` et varie d'une machine à l'autre.
- Les entrées de reflog expirent par défaut au bout de 90 jours (ou 30 jours pour les objets inaccessibles), puis sont supprimées par `git gc`.
- Même si une branche est supprimée via `git branch -D`, ses commits restent accessibles via le reflog tant que le garbage collector n'a pas tourné.
**Urgences/dangers :** — (outil de secours passif, aucun danger en consultation)
**Précautions :** Consulter `git reflog` dès qu'une fausse manipulation survient avant d'exécuter d'autres commandes de nettoyage.
**Équivalents :** hg journal, svn (pas d'équivalent local)
**Voir aussi :** git reset, git checkout, git gc, git log

## `git tag` — Poser des jalons de version [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** marquer une version livrée (v1.0.0, v2.1.4-rc1), déclencher un pipeline de déploiement CI/CD, archiver une étape clé
**Rôle :** Associer un nom d'étiquette fixe et immuable à un commit précis dans l'historique.
**Syntaxe :** `git tag [options] <nom-du-tag> [commit]`
**Cas réguliers :**
- `git tag -a v1.0.0 -m "Release version 1.0.0"` — Créer un tag annoté avec message (le plus recommandé)
- `git tag` — Lister tous les tags du dépôt
- `git push origin v1.0.0` — Pousser un tag spécifique vers le serveur distant
- `git push origin --tags` — Pousser TOUS les tags locaux vers le serveur distant
**Origine :** Git 1.0 (2005) — s'inspire des tags SVN/CVS, mais sous forme d'objets ou de références fixes qui ne bougent jamais avec les commits futurs.
**Subtilités/confusions :**
- Deux types de tags : léger (*lightweight*, simple pointeur) vs annoté (*annotated*, vrai objet Git avec auteur, date et signature GPG). Toujours préférer le tag annoté (`-a`).
- Contrairement aux branches, un tag ne se déplace PAS automatiquement lorsqu'on ajoute de nouveaux commits.
- `git push` ne pousse PAS les tags par défaut : il faut spécifier le tag ou `--tags`.
**Urgences/dangers :** ⚠️ Déplacer ou supprimer un tag déjà publié (`git tag -d` + `push --delete`) perturbe la reproductibilité des builds et des dépendances.
**Précautions :** Adopter la convention Semantic Versioning (SemVer: `vMAJOR.MINOR.PATCH`) pour nommer les tags.
**Équivalents :** svn copy (création de tag), hg tag
**Voir aussi :** git describe, git push, git checkout, git release

## `git remote` — Gérer les dépôts distants [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** —
**Contextes :** connecter un dépôt local à GitHub/GitLab, consulter les URL distantes, ajouter un dépôt d'équipe (upstream)
**Rôle :** Administrer la liste des dépôts distants enregistrés et leurs URL d'accès (fetch/push).
**Syntaxe :** `git remote <add | remove | rename | set-url | show | -v>`
**Cas réguliers :**
- `git remote -v` — Afficher la liste des remotes avec leurs URL (le plus courant)
- `git remote add origin https://github.com/user/repo.git` — Lier le dépôt local à origin
- `git remote set-url origin git@github.com:user/repo.git` — Passer de HTTPS à SSH
- `git remote prune origin` — Nettoyer les branches distantes locales qui ont été supprimées sur le serveur
**Origine :** Git 1.0 (2005) — brique essentielle du modèle distribué permettant de synchroniser plusieurs serveurs ou pairs.
**Subtilités/confusions :**
- `origin` n'est pas un mot clé magique : c'est simplement le nom par défaut donné au dépôt distant principal lors du clone.
- `git remote -v` montre deux URL par remote : une pour le `fetch` (lecture) et une pour le `push` (écriture), qui peuvent différer.
- Supprimer un remote (`git remote remove`) supprime la liaison locale, PAS le dépôt distant lui-même.
**Urgences/dangers :** ⚠️ Se tromper d'URL dans `origin` peut pousser du code privé vers un dépôt public non désiré.
**Précautions :** Toujours vérifier `git remote -v` après la création ou la modification de liens distants.
**Équivalents :** hg paths, svn (concept de dépôt central unique)
**Voir aussi :** git fetch, git push, git pull, git clone

## `git config` — Personnaliser Git [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** installer Git, paramétrer son identité, définir son éditeur par défaut, configurer des alias pratiques
**Rôle :** Consulter et modifier les variables de configuration de Git aux niveaux système, global ou projet.
**Syntaxe :** `git config [<niveau>] <clef> [<valeur>]`
**Cas réguliers :**
- `git config --global user.name "Adolphe"` — Définir son nom pour tous les commits (incontournable)
- `git config --global user.email "contact@domaine.fr"` — Définir son adresse courriel
- `git config --list --show-origin` — Lister toute la configuration avec la provenance de chaque fichier
- `git config --global alias.st status` — Créer un alias court (`git st` au lieu de `git status`)
**Origine :** Git 1.0 (2005) — système d'options au format INI lisible situé dans `~/.gitconfig` ou `.git/config`.
**Subtilités/confusions :**
- Trois niveaux prioritaires : `--local` (.git/config) surcharge `--global` (~/.gitconfig) qui surcharge `--system` (/etc/gitconfig).
- Les modifications de nom ou d'adresse courriel ne s'appliquent qu'aux COMMITS FUTURS : elles ne réécrivent pas l'historique passé.
- `core.autocrlf` est crucial pour éviter les conflits de fins de ligne entre Windows (CRLF) et Linux/macOS (LF).
**Urgences/dangers :** ⚠️ Configurer une mauvaise adresse courriel empêche la liaison automatique des commits avec le compte GitHub/GitLab.
**Précautions :** Utiliser `--global` pour les préférences personnelles et `--local` pour les configurations spécifiques au projet professionnel.
**Équivalents :** hg config, svn (fichiers de conf ~/.subversion)
**Voir aussi :** git commit, git init, git alias

## `git restore` — Restaurer les fichiers [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 84 | **Aliases :** —
**Contextes :** annuler des modifications locales non commitées, vider l'index, remplacer `git checkout -- <fichier>`
**Rôle :** Restaurer les fichiers du dossier de travail ou de la zone de préparation (index) depuis une version de référence.
**Syntaxe :** `git restore [options] <fichiers>`
**Cas réguliers :**
- `git restore src/app.js` — Annuler les modifications non commitées du fichier (le plus courant)
- `git restore --staged src/app.js` — Retirer un fichier de l'index (équivalent de `git reset HEAD <file>`)
- `git restore --source=HEAD~2 src/app.js` — Restaurer le fichier tel qu'il était il y a deux commits
- `git restore .` — Annuler TOUTES les modifications non préparées du dossier courant
**Origine :** Git 2.23 (2019) — introduite pour séparer la responsabilité de restauration du fichier de la commande surchargée `git checkout`.
**Subtilités/confusions :**
- `git restore` annule les modifications dans le dossier de travail SANS possibilité de retour (sauf si enregistrées dans l'index).
- Sans `--staged`, la commande touche au fichier physique dans le dossier de travail ; avec `--staged`, elle ne touche qu'à l'index.
- `restore` ne supprime pas les nouveaux fichiers non suivis (*untracked*) : pour cela, utiliser `git clean`.
**Urgences/dangers :** ⚠️ `git restore .` détruit irrémédiablement le travail non commité et non préparé.
**Précautions :** Vérifier `git diff` avant d'exécuter `git restore` pour s'assurer que les modifications annulées ne sont plus utiles.
**Équivalents :** svn revert, hg revert
**Voir aussi :** git checkout, git reset, git status, git diff

## `git rm` — Supprimer des fichiers sous contrôle Git [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 78 | **Aliases :** —
**Contextes :** retirer un fichier du projet, arrêter le suivi d'un fichier commité par erreur, nettoyer l'arborescence
**Rôle :** Supprimer un fichier du dossier de travail ET enregistrer sa suppression dans l'index Git pour le prochain commit.
**Syntaxe :** `git rm [options] <fichiers>`
**Cas réguliers :**
- `git rm config/old.json` — Supprimer le fichier physiquement et préparer le commit (le plus courant)
- `git rm --cached .env` — Retirer du suivi Git EN GARDANT le fichier physique sur le disque
- `git rm -r temp/` — Supprimer récursivement tout un dossier
- `git rm -f app.log` — Forcer la suppression d'un fichier modifié et déjà préparé dans l'index
**Origine :** Git 1.0 (2005) — évite de devoir faire `rm file` puis `git add file` manuellement.
**Subtilités/confusions :**
- `git rm --cached` est la solution clé pour arrêter de versionner un fichier commité par erreur (ex: `.env`) sans le détruire localement.
- Supprimer un fichier avec le `rm` du système laisse le fichier marqué comme « deleted » dans `git status` : il faut faire `git add` ou `git rm` pour valider.
- `--cached` ne supprime pas le fichier de l'historique PASSE : il s'arrête simplement de le suivre dans les commits futurs.
**Urgences/dangers :** ⚠️ `git rm -f` détruit les modifications non commitées du fichier sans confirmation.
**Précautions :** Ajouter le fichier à `.gitignore` juste après avoir exécuté `git rm --cached` pour éviter de le réintégrer par accident.
**Équivalents :** svn delete, hg remove
**Voir aussi :** git mv, git add, git commit, .gitignore

## `git mv` — Déplacer ou renommer un fichier [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 76 | **Aliases :** —
**Contextes :** refactoriser l'arborescence, renommer un composant, déplacer des classes dans de nouveaux dossiers
**Rôle :** Déplacer ou renommer un fichier ou dossier tout en mettant à jour l'index Git pour préserver la traçabilité.
**Syntaxe :** `git mv [options] <source> <destination>`
**Cas réguliers :**
- `git mv src/old.js src/new.js` — Renommer un fichier en préparant le commit (le plus courant)
- `git mv utils/ src/utils/` — Déplacer tout un dossier vers un nouvel emplacement
- `git mv -f file.txt File.txt` — Forcer le renommage pour les systèmes de fichiers insensibles à la casse (Windows/macOS)
- `git mv docs/ manual/` — Renommer le répertoire de documentation
**Origine :** Git 1.0 (2005) — raccourci pratique pour `mv source dest` suivi de `git add dest` et `git rm source`.
**Subtilités/confusions :**
- Git ne stocke pas le renommage de façon explicite : il le DÉTECTE dynamiquement lors du `git log` ou `git diff` grâce à la similitude de contenu (heuristique).
- Sur Windows/macOS, renommer `fichier.txt` en `Fichier.txt` avec le système peut être ignoré par Git : `git mv -f` est indispensable.
- Si le fichier subit de trop grosses modifications en même temps que son déplacement, Git peut perdre l'historique du renommage (`git log --follow`).
**Urgences/dangers :** — (aucun danger particulier, l'index enregistre l'opération)
**Précautions :** Préférer séparer le commit de renommage (`git mv`) du commit de modification de contenu pour préserver un `git blame` propre.
**Équivalents :** svn move / svn rename, hg move / hg rename
**Voir aussi :** git rm, git add, git log, git status

## `git clean` — Nettoyer les fichiers non suivis [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** —
**Contextes :** purger les artéfacts de compilation, supprimer les fichiers temporaires créés par des tests, réinitialiser le dossier de travail
**Rôle :** Supprimer définitivement du dossier de travail tous les fichiers et répertoires qui ne sont pas suivis par Git.
**Syntaxe :** `git clean [options]`
**Cas réguliers :**
- `git clean -n` — Mode simulation (*dry-run*) : afficher ce qui SERAIT supprimé sans rien toucher (indispensable !)
- `git clean -fd` — Supprimer les fichiers (`-f`) ET les dossiers non suivis (`-d`)
- `git clean -fx` — Supprimer aussi les fichiers ignorés par `.gitignore` (builds, node_modules)
- `git clean -i` — Nettoyage interactif avec menu de sélection
**Origine :** Git 1.0 (2005) — conçu pour remettre à neuf un arbre de source sans avoir à supprimer et recloner le dépôt.
**Subtilités/confusions :**
- `git clean` exige le drapeau de force `-f` ou `-n` par sécurité : Git refuse de nettoyer à l'aveugle par défaut.
- Attention : les fichiers supprimés par `git clean` NE PASSENT PAS par la corbeille du système et ne sont PAS enregistrés dans Git !
- L'option `-x` supprime aussi les fichiers dans `.gitignore` (ex: `.env` locaux, clés de test) : utiliser avec extrême précaution.
**Urgences/dangers :** ⚠️ `git clean -fdx` supprime de manière IRREVOCABLE tous les fichiers non suivis et ignorés (dont vos configurations locales `.env` et dépendances).
**Précautions :** Toujours exécuter `git clean -n` (simulation) avant de lancer `git clean -fd`.
**Équivalents :** hg purge, svn (pas d'outil natif direct)
**Voir aussi :** git reset, git restore, git status, .gitignore

## `git worktree` — Multiples arbres de travail simultanés [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** travailler sur deux branches en même temps sans stasher, corriger un hotfix d'urgence sans abandonner sa branche de dev
**Rôle :** Permettre la présence de plusieurs répertoires de travail indépendants rattachés au même dépôt `.git`.
**Syntaxe :** `git worktree <add | list | remove | prune>`
**Cas réguliers :**
- `git worktree add ../hotfix-login hotfix/login` — Créer un dossier de travail séparé pour la branche `hotfix/login`
- `git worktree list` — Lister tous les arbres de travail actifs et leurs branches rattachées
- `git worktree remove ../hotfix-login` — Supprimer un arbre de travail une fois le travail fini
- `git worktree prune` — Nettoyer les métadonnées des arbres dont le dossier physique a été supprimé
**Origine :** Git 2.5 (2015) — résout élégamment le problème historique des développeurs qui clonaient le dépôt 5 fois sur leur disque pour travailler sur plusieurs branches.
**Subtilités/confusions :**
- Deux worktrees du même dépôt ne peuvent PAS être positionnés sur la MÊME branche simultanément (Git bloque l'opération par sécurité).
- Chaque worktree possède son propre index et son propre dossier de travail, mais partage les objets Git, les remotes et le reflog.
- Supprimer manuellement le dossier d'un worktree sans `git worktree remove` laisse des traces mortes nettoyables via `git worktree prune`.
**Urgences/dangers :** — (outil très sûr, chaque dossier reste totalement isolé)
**Précautions :** Placer les dossiers de worktree en dehors du dossier principal du projet pour éviter de les ajouter par accident au `.gitignore`.
**Équivalents :** hg share, svn (pas d'équivalent natif)
**Voir aussi :** git checkout, git stash, git branch, git status

## `git submodule` — Gérer des dépôts imbriqués [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** inclure une bibliothèque externe en tant que dépôt indépendant, partager des composants communs entre plusieurs projets
**Rôle :** Conserver un autre dépôt Git comme un sous-répertoire d'un dépôt parent, bloqué sur un commit précis.
**Syntaxe :** `git submodule <add | update | init | status | deinit>`
**Cas réguliers :**
- `git submodule add https://github.com/lib/core.git libs/core` — Attacher un sous-module dans le dossier `libs/core`
- `git submodule update --init --recursive` — Initialiser et récupérer le contenu des sous-modules après un clone
- `git submodule update --remote` — Mettre à jour les sous-modules vers la version la plus récente de leur branche distante
- `git clone --recurse-submodules <url>` — Cloner un projet principal ET tous ses sous-modules en une commande
**Origine :** Git 1.5.3 (2007) — créé pour gérer les grosses dépendances structurées du noyau et des sous-systèmes Linux.
**Subtilités/confusions :**
- Le projet parent ne stocke pas les fichiers du sous-module, mais seulement son URL et le SHA du commit exact auquel il est verrouillé.
- Après un `git clone`, le dossier du sous-module est VIDE par défaut tant qu'on n'a pas exécuté `git submodule update --init`.
- Travailler à l'intérieur d'un sous-module place souvent Git en état de tête détachée (*detached HEAD*) : il faut basculer sur une branche pour y commiter.
**Urgences/dangers :** ⚠️ Oublier de commiter et pousser les modifications faites dans un sous-module casse le projet parent pour tous les autres développeurs.
**Précautions :** Toujours vérifier `git status` dans le sous-module ET dans le projet parent avant de pusher.
**Équivalents :** svn externals, hg subrepo
**Voir aussi :** git clone, git status, git fetch, git subtree

## `git show` — Inspecter un objet Git en détail [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** consulter le diff d'un commit précis, inspecter le contenu d'un tag, vérifier un commit récent
**Rôle :** Afficher sous forme textuelle le contenu détaillé et le diff d'un ou plusieurs objets Git (commit, tag, arbre, blob).
**Syntaxe :** `git show [options] [<objet>]`
**Cas réguliers :**
- `git show` — Afficher les détails du tout dernier commit sur HEAD (le plus courant)
- `git show 8a3f12` — Inspecter un commit spécifique via son SHA
- `git show v1.0.0` — Afficher les détails et le message d'un tag annoté
- `git show main:src/index.js` — Afficher le contenu du fichier `src/index.js` tel qu'il est sur la branche `main` sans basculer de branche
**Origine :** Git 1.0 (2005) — l'inspecteur polyvalent de la base de données orientée objets de Git.
**Subtilités/confusions :**
- `git show <commit>` combine le message de commit, l'auteur, la date ET le diff complet des fichiers modifiés.
- `git show commit:fichier` permet de lire une ancienne version d'un fichier sans modifier son dossier de travail actuel.
- Fonctionne aussi bien sur les commits que sur les tags, les arbres et les objets binaires (*blobs*).
**Urgences/dangers :** — (commande de consultation sans aucun effet de bord)
**Précautions :** Associer avec `--stat` (`git show --stat`) pour voir la liste des fichiers touchés sans afficher le diff complet.
**Équivalents :** svn log -v -c, hg log -v -r
**Voir aussi :** git log, git diff, git blame, git cat-file

## `git describe` — Nommer un commit par rapport aux tags [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 76 | **Aliases :** —
**Contextes :** générer un numéro de version dynamique dans un build CI/CD, identifier une révision précise entre deux livraisons
**Rôle :** Trouver le tag le plus proche accessible depuis un commit et construire un nom de version lisible de la forme `v1.2.0-4-g2a1b3c`.
**Syntaxe :** `git describe [options] [<commit>]`
**Cas réguliers :**
- `git describe` — Nommer le commit actuel par rapport au tag annoté le plus récent (le plus courant)
- `git describe --tags` — Prendre aussi en compte les tags simples non annotés
- `git describe --always` — Retourner le SHA court si aucun tag n'est trouvé dans l'historique
- `git describe --dirty` — Ajouter le suffixe `-dirty` si le dossier de travail contient des modifications non commitées
**Origine :** Git 1.5.0 (2007) — inventé pour donner un nom compréhensible par un humain aux builds intermédiaires entre deux releases.
**Subtilités/confusions :**
- Le résultat `v1.2.0-4-g2a1b3c` se lit : 4 commits après le tag `v1.2.0`, sur le commit dont l'empreinte commence par `2a1b3c` (`g` signifie Git).
- Par défaut, `git describe` ne prend en compte QUE les tags annotés (`git tag -a`) : ajouter `--tags` pour inclure les tags légers.
- Si le commit exact est lui-même tagué, `git describe` retourne simplement le nom du tag sans suffixe.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser des tags annotés pour les versions officielles afin d'assurer un fonctionnement optimal de `git describe`.
**Équivalents :** hg identify, svn info (numéro de révision séquentiel)
**Voir aussi :** git tag, git log, git status

## `git shortlog` — Résumé de l'historique par auteur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 74 | **Aliases :** —
**Contextes :** préparer le fichier `AUTHORS` ou les notes de version, mesurer le volume de contributions, analyser l'activité du dépôt
**Rôle :** Regrouper et synthétiser les messages de commits par auteur dans un format condensé et lisible.
**Syntaxe :** `git shortlog [options] [<revision-range>]`
**Cas réguliers :**
- `git shortlog` — Liste alphabétique des auteurs et de leurs commits sur la branche courante
- `git shortlog -sn` — Afficher uniquement le nombre total de commits par auteur, trié par ordre décroissant (classement des contributeurs)
- `git shortlog v1.0..v2.0` — Résumer les contributions effectuées entre deux versions taguées
- `git shortlog --email` — Afficher aussi l'adresse courriel des contributeurs
**Origine :** Git 1.0 (2005) — créé par Linus Torvalds pour rédiger rapidement les courriels de synthèse de release du noyau Linux.
**Subtilités/confusions :**
- Si un contributeur utilise plusieurs adresses ou noms différents, `shortlog` crée plusieurs entrées : corriger avec un fichier `.mailmap`.
- Le nombre de commits ne reflète pas toujours la valeur ou le volume de code produit (un commit de 10k lignes vaut 1 commit comme une typo).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Configurer un fichier `.mailmap` à la racine pour fusionner les identités multiples des contributeurs.
**Équivalents :** hg log --template, svn log (traité par script)
**Voir aussi :** git log, git blame, git config

## `git grep` — Rechercher dans les fichiers suivis [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** chercher une fonction ou une variable dans tout le projet, rechercher un terme dans une branche distante sans switcher
**Rôle :** Rechercher ultra-rapidement des expressions ou motifs de texte dans les fichiers suivis du projet ou dans les commits passés.
**Syntaxe :** `git grep [options] <motif> [<revision>]`
**Cas réguliers :**
- `git grep "connect_db"` — Chercher la chaîne dans tous les fichiers suivis (infiniment plus rapide que `grep -r`)
- `git grep -n "FIXME"` — Afficher les numéros de ligne des occurrences
- `git grep -i "API_KEY"` — Recherche insensible à la casse
- `git grep "UPDATE_V2" HEAD~5` — Rechercher dans les fichiers tels qu'ils étaient il y a 5 commits
**Origine :** Git 1.0 (2005) — exploite le cache de l'index Git et le multi-threading pour surpasser de loin la vitesse d'un `grep` classique.
**Subtilités/confusions :**
- `git grep` ignore automatiquement tous les fichiers non suivis et ceux listés dans `.gitignore` (pas besoin de filtrer `node_modules`).
- Ne recherche QUE dans les fichiers suivis : les nouveaux fichiers pas encore ajoutés avec `git add` ne sont pas scannés.
- Prend en charge les expressions régulières avec `-E` (POSIX) ou `-P` (Perl-compatible regex).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pour chercher dans des fichiers non suivis, utiliser l'outil système `grep` ou `ripgrep` (`rg`).
**Équivalents :** ripgrep, grep -r, hg grep, svn (pas natif)
**Voir aussi :** git log -S, git blame, git ls-files

## `git ls-files` — Lister les fichiers de l'index [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** —
**Contextes :** écrire des scripts de validation, vérifier ce qui est réellement suivi par Git, déboguer les règles `.gitignore`
**Rôle :** Afficher la liste complète des fichiers enregistrés dans l'index Git et le dossier de travail avec leur état.
**Syntaxe :** `git ls-files [options]`
**Cas réguliers :**
- `git ls-files` — Afficher tous les fichiers actuellement suivis par le dépôt (le plus courant)
- `git ls-files -m` — Afficher uniquement les fichiers suivis qui ont été modifiés
- `git ls-files -o --exclude-standard` — Lister les fichiers non suivis (*untracked*) en appliquant `.gitignore`
- `git ls-files -i --exclude-standard` — Lister les fichiers suivis qui correspondent pourtant à une règle `.gitignore` (anomalie)
**Origine :** Git 1.0 (2005) — l'une des commandes de plomberie (*plumbing*) originelles exposée pour les scripts et l'outillage externe.
**Subtilités/confusions :**
- Outil fondamental pour comprendre la différence entre un fichier présent sur le disque et un fichier réellement pris en compte par Git.
- Très utilisé dans les wrappers de scripts ou CI/CD pour alimenter des linters ou des formateurs de code (`git ls-files '*.py' | xargs flake8`).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `--exclude-standard` pour s'assurer que les exclusions globales et locales `.gitignore` sont bien respectées.
**Équivalents :** hg manifest, svn list
**Voir aussi :** git status, git check-ignore, .gitignore

## `git am` — Appliquer des patchs issus d'un courriel [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 68 | **Aliases :** —
**Contextes :** intégrer des contributions envoyées par courrier électronique, appliquer des séries de patchs formatés avec `git format-patch`
**Rôle :** Appliquer une série de fichiers patchs issus d'une boîte aux lettres (format mbox) en conservant les auteurs, dates et messages d'origine.
**Syntaxe :** `git am [options] [<mbox>|<mail>]`
**Cas réguliers :**
- `git am 0001-fix-bug.patch` — Appliquer un fichier de patch individuel
- `git am ~/mail/patches.mbox` — Appliquer tout un paquet de patchs contenus dans un fichier mbox
- `git am --resolved` — Reprendre l'application après avoir résolu un conflit
- `git am --abort` — Abandonner la séquence de patchs et revenir à l'état initial
**Origine :** Git 1.0 (2005) — acronyme de « Apply Mailbox ». Mode de contribution historique principal du noyau Linux et de Git lui-même.
**Subtilités/confusions :**
- Contrairement à `git apply`, `git am` crée automatiquement les COMMITS correspondants avec toutes leurs métadonnées d'origine.
- En cas de conflit, la séquence s'arrête : il faut résoudre le conflit, faire `git add` puis `git am --resolved` (ne pas commiter manuellement !).
**Urgences/dangers :** ⚠️ `git am` applique des commits signés par d'autres : toujours réviser le contenu du patch avant application.
**Précautions :** Vérifier que les patchs s'appliquent sur la bonne version de départ pour limiter les conflits de fusion.
**Équivalents :** hg import, svn patch
**Voir aussi :** git am, git apply, git send-email

## `git apply` — Appliquer un patch sans commiter [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 74 | **Aliases :** —
**Contextes :** tester des modifications fournies sous forme de diff, appliquer un patch léger sans créer de commit d'office
**Rôle :** Appliquer les changements d'un fichier diff/patch directement sur le dossier de travail ou l'index sans toucher à l'historique.
**Syntaxe :** `git apply [options] [<patch>]`
**Cas réguliers :**
- `git apply feature.patch` — Appliquer les changements du patch dans le dossier de travail (le plus courant)
- `git apply --check feature.patch` — Tester si le patch s'applique sans erreur (simulation sans modification)
- `git apply --stat feature.patch` — Afficher un résumé des statistiques du patch (fichiers touchés, lignes +/-)
- `git apply -R feature.patch` — Appliquer le patch À L'ENVERS pour annuler ses modifications
**Origine :** Git 1.0 (2005) — conçu comme un substitut moderne, robuste et atomique à la commande Unix `patch`.
**Subtilités/confusions :**
- `git apply` est une opération Tout-ou-Rien (atomique) : si une seule partie du patch échoue, rien n'est appliqué (contrairement au `patch` Unix).
- N'enregistre aucun commit et ne conserve pas le nom de l'auteur : c'est une modification brute de vos fichiers.
**Urgences/dangers :** — (les modifications restent non commitées, annulables avec `git restore`)
**Précautions :** Exécuter `git apply --check` avant pour vérifier l'absence de conflits sur les lignes cibles.
**Équivalents :** patch (commande Unix), svn patch, hg import --no-commit
**Voir aussi :** git am, git diff, git restore

## `git archive` — Archiver un arbre de sources [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** —
**Contextes :** créer un tarball/zip de livraison de code sans le dossier `.git`, exporter une version précise pour le déploiement
**Rôle :** Générer une archive compressée (zip, tar, tar.gz) contenant l'arborescence des fichiers d'une version donnée sans les métadonnées Git.
**Syntaxe :** `git archive [options] <tree-ish> [<chemin>...]`
**Cas réguliers :**
- `git archive --format=zip HEAD > export.zip` — Exporter le commit actuel sous forme d'archive zip propre
- `git archive --format=tar.gz --prefix=app-1.0/ v1.0.0 > app-1.0.tar.gz` — Archiver la version v1.0.0 avec un préfixe de dossier
- `git archive -o release.zip main src/` — Archiver uniquement le dossier `src/` de la branche main
**Origine :** Git 1.0 (2005) — créé pour distribuer facilement des paquets de code source légers sans trimbaler l'historique `.git`.
**Subtilités/confusions :**
- L'archive générée ne contient PAS le dossier `.git` : elle est idéale pour l'envoi en production ou la distribution aux clients.
- Respecte le fichier d'attributs `.gitattributes` : les fichiers marqués `export-ignore` (ex: tests, CI) sont exclus de l'archive.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Configurer `.gitattributes` avec `export-ignore` pour exclure les configurations de dev et clés de test de vos archives de release.
**Équivalents :** hg archive, svn export
**Voir aussi :** git bundle, .gitattributes, tar, zip

## `git bundle` — Archiver un dépôt complet en un fichier [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** —
**Contextes :** transférer un dépôt Git sur une machine isolée sans réseau (air-gapped), sauvegarder des branches sur clé USB
**Rôle :** Empaqueter des objets et des références Git dans un unique fichier binaire équivalent à un dépôt distant.
**Syntaxe :** `git bundle <create | verify | list-heads | unbundle>`
**Cas réguliers :**
- `git bundle create backup.bundle main` — Créer un fichier de sauvegarde contenant tout l'historique de `main`
- `git bundle verify backup.bundle` — Vérifier qu'un fichier bundle est valide et compatible avec le dépôt courant
- `git clone backup.bundle repo-local` — Cloner un dépôt complet directement à partir du fichier `.bundle`
- `git pull backup.bundle main` — Récupérer les nouveaux commits depuis un fichier bundle transféré par clé USB
**Origine :** Git 1.5.1 (2007) — conçu pour le transport offline de dépôts Git distribués.
**Subtilités/confusions :**
- Un bundle est un VRAI dépôt Git sous forme d'un seul fichier : on peut exécuter `git clone`, `git fetch` ou `git pull` dessus directement.
- Permet des sauvegardes incrémentales : `git bundle create diff.bundle main~10..main` empaquète uniquement les 10 derniers commits.
**Urgences/dangers :** — (le fichier bundle doit être conservé en lieu sûr s'il contient du code propriétaire)
**Précautions :** Vérifier le bundle avec `git bundle verify` avant de détruire le dépôt d'origine lors d'une migration physique.
**Équivalents :** hg bundle
**Voir aussi :** git archive, git clone, git fetch

## `git fsck` — Vérifier l'intégrité de la base Git [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 72 | **Aliases :** —
**Contextes :** vérifier la santé du dépôt après une coupure de courant, rechercher des objets corrompus ou orphelins
**Rôle :** Inspecter l'intégrité physique du système d'objets Git et identifier les objets corrompus, pendants ou inaccessibles.
**Syntaxe :** `git fsck [options]`
**Cas réguliers :**
- `git fsck` — Vérifier la cohérence globale de la base de données Git (le plus courant)
- `git fsck --full` — Inspection complète approfondie de tous les blocs d'objets
- `git fsck --unreachable` — Afficher la liste des commits et objets qui ne sont rattachés à aucune branche ni tag
- `git fsck --lost-found` — Récupérer tous les objets inaccessibles dans le dossier `.git/lost-found/`
**Origine :** Git 1.0 (2005) — fait référence à l'outil Unix classique de vérification de système de fichiers `fsck` (*File System Consistency Check*).
**Subtilités/confusions :**
- `dangling commit` ou `dangling blob` ne signifie pas que le dépôt est corrompu : ce sont simplement des éléments temporaires abandonnés.
- Si `git fsck` signale des erreurs d'empreinte SHA-1, des fichiers dans `.git/objects/` sont physiquement endommagés sur le disque.
**Urgences/dangers :** ⚠️ En cas de corruption avérée de disque, réparer avec `git fsck` peut nécessiter le remplacement manuel d'objets depuis un clone sain.
**Précautions :** Exécuter `git fsck` périodiquement sur les serveurs centraux de stockage de code.
**Équivalents :** hg verify, svnadmin verify
**Voir aussi :** git gc, git reflog, git maintenance

## `git gc` — Optimiser la base d'objets [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** —
**Contextes :** nettoyer un dépôt devenu lourd, compacter les petits fichiers d'objets isolés, purger les commits expirés
**Rôle :** Nettoyer le système d'objets local en supprimant les objets inaccessibles expirés et en empilant les fichiers d'objets dans des archives compressées (*packfiles*).
**Syntaxe :** `git gc [options]`
**Cas réguliers :**
- `git gc` — Lancer un nettoyage et une compression standard (le plus courant)
- `git gc --prune=now` — Forcer la suppression immédiate de tous les objets inaccessibles sans attendre le délai de rétention
- `git gc --aggressive` — Optimiser de manière très agressive (plus lent mais compression maximale)
- `git gc --auto` — Vérifier si le nettoyage est nécessaire et l'exécuter uniquement si le seuil est dépassé
**Origine :** Git 1.0 (2005) — acronyme de « Garbage Collector ». Essentiel pour maintenir les performances de lecture/écriture sur les gros dépôts.
**Subtilités/confusions :**
- Par défaut, `git gc` conserve les objets inaccessibles (*dangling*) pendant 14 jours et les entrées de reflog pendant 90 jours avant purge.
- `git gc --aggressive` recalcule les deltas d'objets : peut prendre des dizaines de minutes sur les très gros projets.
- Git exécute automatiquement `git gc --auto` lors de certaines opérations lourdes (`git merge`, `git rebase`).
**Urgences/dangers :** ⚠️ `git gc --prune=now` supprime définitivement les commits inaccessibles : tout reset involontaire devient irrécupérable après cette commande !
**Précautions :** Éviter `--prune=now` sauf si vous êtes absolument certain de ne plus avoir besoin des commits orphelins du reflog.
**Équivalents :** hg clean unrefs, svnadmin pack
**Voir aussi :** git reflog, git fsck, git maintenance, git prune

## `git maintenance` — Tâches d'optimisation en arrière-plan [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** —
**Contextes :** maintenir la rapidité des gros dépôts d'entreprise, automatiser l'optimisation sans bloquer le développeur
**Rôle :** Configurer et exécuter des tâches d'arrière-plan périodiques (fetch, prefetch, commit-graph, loose-objects) pour garder le dépôt performant.
**Syntaxe :** `git maintenance <start | stop | run | register | unregister>`
**Cas réguliers :**
- `git maintenance start` — Enregistrer le dépôt dans le service de planification du système (cron/systemd/launchd/Windows Task Scheduler)
- `git maintenance run` — Exécuter immédiatement toutes les tâches de maintenance programmées
- `git maintenance register` — Ajouter le dépôt courant à la liste des dépôts entretenus automatiquement
- `git maintenance stop` — Désactiver l'entretien automatique pour ce dépôt
**Origine :** Git 2.30 (2021) — développé par Microsoft/GitHub pour gérer les dépôts géants de millions de commits (ex: Monorepos).
**Subtilités/confusions :**
- Préfère l'arrière-plan discret aux blocages soudains provoqués par `git gc --auto` en plein travail.
- Met à jour le `commit-graph` qui accélère l'affichage des logs et le calcul de révisions jusqu'à 10 fois.
- S'intègre directement au planificateur de tâches natif de l'OS du système hôte.
**Urgences/dangers :** — (processus d'arrière-plan très à faible priorité qui ne perturbe pas le travail)
**Précautions :** Utile principalement sur les monorepos ou les projets ayant un volume de commits très élevé.
**Équivalents :** hg bg maintenance
**Voir aussi :** git gc, git fsck, git config

## `git lfs` — Gestion des gros fichiers binaires [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** stocker des vidéos, des modèles d'IA, des paquets 3D ou des binaires lourds sans faire exploser la taille du `.git`
**Rôle :** Remplacer les fichiers volumineux par de simples pointeurs texte dans Git, tout en stockant le contenu réel sur un serveur LFS distant dédié.
**Syntaxe :** `git lfs <install | track | ls-files | pull | push | env>`
**Cas réguliers :**
- `git lfs install` — Initialiser l'extension Git LFS sur votre système hôte (une fois par machine)
- `git lfs track "*.psd"` — Déclarer tous les fichiers `.psd` sous la gestion Git LFS (met à jour `.gitattributes`)
- `git lfs ls-files` — Afficher la liste des fichiers actuellement gérés par LFS dans le dépôt
- `git lfs pull` — Télécharger le contenu réel des gros fichiers pour les pointeurs du commit actuel
**Origine :** GitHub (2015) — extension open-source devenue le standard de facto pour la gestion des assets lourds dans Git.
**Subtilités/confusions :**
- `git lfs track` met à jour le fichier `.gitattributes` : il FOUDROIE de le commiter, sinon les collègues téléchargeront les binaires dans Git classique.
- Sans le client LFS installé, cloner un dépôt LFS ne télécharge que des minuscules fichiers textes contenant un identifiant hash SHA-256.
- Les serveurs LFS disposent souvent de quotas de stockage et de bande passante séparés de Git (sur GitHub/GitLab).
**Urgences/dangers :** ⚠️ Commiter un binaire de 500 Mo AVANT d'avoir configuré `git lfs track` intègre définitivement ce binaire dans l'historique Git classique.
**Précautions :** Configurer `git lfs track` AVANT d'ajouter les gros fichiers dans le projet et commiter `.gitattributes`.
**Équivalents :** hg bigfiles, svn (gestion binaire native mais centralisée)
**Voir aussi :** .gitattributes, git checkout, git clone

## `git hooks` — Scripting automatique d'événements [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** forcer le linter avant un commit, vérifier le format du message de commit, bloquer le push de secrets ou de tests en échec
**Rôle :** Exécuter des scripts personnalisés (Bash, Python, Node.js) automatiquement au déclenchement de certaines étapes Git.
**Syntaxe :** Placer des scripts exécutables dans `.git/hooks/<nom-du-hook>` ou configurer `core.hooksPath`.
**Cas réguliers :**
- `.git/hooks/pre-commit` — S'exécute avant de finaliser un commit (idéal pour formater le code ou lancer des linters)
- `.git/hooks/commit-msg` — Vérifie que le message de commit respecte les normes (ex: Conventional Commits)
- `.git/hooks/pre-push` — S'exécute avant le push (idéal pour exécuter la suite de tests rapides)
- `git config core.hooksPath .githooks` — Rediriger le dossier des hooks vers un répertoire versionné dans le dépôt
**Origine :** Git 1.0 (2005) — mécanisme d'extension natif inspiré des déclencheurs de bases de données et des hooks Unix.
**Subtilités/confusions :**
- Les fichiers du dossier `.git/hooks/` par défaut ne sont PAS versionnés ni partagés lors d'un `git clone`.
- Pour partager des hooks avec l'équipe, utiliser un outil comme `Husky`, `pre-commit` (Python) ou configurer `core.hooksPath`.
- On peut sauter l'exécution des hooks locaux avec l'option `--no-verify` lors d'un `git commit` ou `git push`.
**Urgences/dangers :** ⚠️ Un hook mal écrit qui plante bloque toutes les opérations Git de l'utilisateur concerné.
**Précautions :** Tester soigneusement les scripts de hooks et prévoir une option de contournement rapide en cas de crise (`--no-verify`).
**Équivalents :** hg hooks, svn hooks (côté serveur)
**Voir aussi :** git commit, git push, git config

## `git notes` — Attacher des remarques aux commits [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 65 | **Aliases :** —
**Contextes :** ajouter des commentaires de revue de code, lier des identifiants de tickets de déploiement sans réécrire l'historique
**Rôle :** Associer des informations textuelles supplémentaires à un commit existant sans modifier son contenu ni son empreinte SHA.
**Syntaxe :** `git notes <add | show | edit | append | list | prune>`
**Cas réguliers :**
- `git notes add -m "Validé par l'équipe QA" HEAD` — Attacher une note au dernier commit
- `git notes show` — Afficher les notes rattachées au commit actuel
- `git push origin "refs/notes/*"` — Pousser les notes vers le serveur distant
- `git notes edit 4b2a1c` — Modifier la note rattachée à un commit spécifique
**Origine :** Git 1.6.6 (2010) — conçu pour permettre le métadouveau collaboratif (revues, statut CI) sans déstabiliser les SHA de commits.
**Subtilités/confusions :**
- Les notes ne modifient PAS l'empreinte SHA-1 du commit auquel elles sont rattachées (stockées dans des références séparées `refs/notes/`).
- `git log` affiche automatiquement les notes rattachées sous le message de commit si elles sont présentes.
- `git push` ne pousse PAS les notes par défaut : il faut spécifier la référence `refs/notes/*`.
**Urgences/dangers :** — (les notes sont totalement indépendantes de l'arbre de code)
**Précautions :** Synchroniser explicitement les références de notes entre les machines de l'équipe pour qu'elles soient visibles de tous.
**Équivalents :** hg extra metadata
**Voir aussi :** git log, git commit, git tag

## `git whatchanged` — Historique des fichiers modifiés [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 65 | **Aliases :** —
**Contextes :** inspecter rapidement quels fichiers ont changé à chaque commit dans un format condensé historique
**Rôle :** Afficher l'historique des commits accompagné de la liste des fichiers ajoutés, modifiés ou supprimés à chaque étape.
**Syntaxe :** `git whatchanged [options]`
**Cas réguliers :**
- `git whatchanged` — Afficher les commits récents et les fichiers touchés (le plus courant)
- `git whatchanged -p` — Afficher les commits avec les diffs complets associés
- `git whatchanged --since="2 weeks ago"` — Inspecter les fichiers modifiés au cours des deux dernières semaines
- `git whatchanged src/` — Filtrer l'historique pour un sous-dossier précis
**Origine :** Git 1.0 (2005) — commande historique conservée par compatibilité, ancêtre direct de `git log --raw`.
**Subtilités/confusions :**
- Strictement équivalent à `git log --raw --no-merges` par défaut.
- Pratique pour voir d'un coup d'œil l'impact d'un commit sans encombler l'écran avec le diff ligne par ligne.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pour les nouveaux scripts, préférer `git log --raw` qui est l'interface moderne recommandée.
**Équivalents :** svn log -v, hg log --stat
**Voir aussi :** git log, git diff, git show

## `git replace` — Remplacer des objets Git [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 60 | **Aliases :** —
**Contextes :** scinder un historique historique trop lourd, greffer un ancien historique sur un nouveau dépôt sans réécrire les commits
**Rôle :** Créer une référence de remplacement disant à Git de faire comme si un objet (commit/arbre) en remplaçait un autre.
**Syntaxe :** `git replace [options] <objet-cible> <objet-remplaçant>`
**Cas réguliers :**
- `git replace 111111 222222` — Dire à Git d'afficher le commit `222222` à la place du commit `111111`
- `git replace -l` — Lister toutes les cartes de remplacement actives dans le dépôt
- `git replace -d 111111` — Supprimer un remplacement actif
- `git replace --graft <commit> [<parent>...]` — Réécrire les parents d'un commit virtuellement sans modifier son SHA
**Origine :** Git 1.6.5 (2009) — créé pour corriger les historiques cassés ou raccourcir la taille des clones sans invalider les SHA de commits existants.
**Subtilités/confusions :**
- Ne modifie PAS l'objet d'origine sur le disque : crée une référence sous `refs/replace/`.
- Permet de lier deux dépôts historiques séparés en faisant croire à Git que le premier commit de l'un dérive du dernier de l'autre.
- On peut ignorer les remplacements virtuels en exécutant Git avec `--no-replace-objects`.
**Urgences/dangers :** ⚠️ Les cartes de remplacement non partagées rendent la vision du dépôt différente entre deux développeurs.
**Précautions :** Pousser explicitement les références `refs/replace/` si l'on souhaite que toute l'équipe voie le même remplacement.
**Équivalents :** hg graft / hg convert (partiel)
**Voir aussi :** git log, git filter-repo, git commit

## `git instaweb` — Serveur web local instantané [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 65 | **Aliases :** —
**Contextes :** parcourir l'historique visuellement sans installer de client lourd, présenter un dépôt en démonstration locale
**Rôle :** Lancer instantanément un serveur web local temporaire (lighttpd/webrick/apache) et ouvrir l'interface Gitweb dans le navigateur.
**Syntaxe :** `git instaweb [options] [<start | stop | restart>]`
**Cas réguliers :**
- `git instaweb` — Démarrer le serveur web local et ouvrir le navigateur par défaut
- `git instaweb --httpd=webrick` — Spécifier le serveur web sous-jacent (Ruby Webrick, Lighttpd, etc.)
- `git instaweb --stop` — Arrêter le serveur web local temporaire
- `git instaweb --port=1234` — Choisir un port d'écoute spécifique
**Origine :** Git 1.5.0 (2007) — solution clé en main pour offrir un explorateur web de dépôt sans aucune configuration serveur.
**Subtilités/confusions :**
- Nécessite qu'un serveur web léger (comme `lighttpd`, `webrick` ou `python`) et `gitweb` soient installés sur la machine hôte.
- Le serveur s'exécute en local uniquement (127.0.0.1) et s'arrête proprement avec `git instaweb --stop`.
**Urgences/dangers :** — (processus local sans exposition distante automatique)
**Précautions :** Penser à exécuter `git instaweb --stop` une fois la démonstration terminée.
**Équivalents :** hg serve
**Voir aussi :** git gitweb, git log

## `git daemon` — Servir un dépôt via le protocole Git [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 62 | **Aliases :** —
**Contextes :** partager rapidement un dépôt en lecture seule sur un réseau local d'entreprise sans configurer de serveur SSH ou HTTP
**Rôle :** Lancer un serveur d'arrière-plan ultra-rapide servant des dépôts Git anonymes via le protocole natif `git://` (port 9418).
**Syntaxe :** `git daemon [options] [<dossier>...]`
**Cas réguliers :**
- `git daemon --reuseaddr --base-path=. --export-all` — Servir tous les dépôts du dossier courant en lecture seule sur le réseau local
- `touch .git/git-daemon-export-ok` — Autoriser explicitement la publication d'un dépôt donné via le daemon
- `git daemon --verbose` — Afficher les journaux détaillés des connexions entrantes
**Origine :** Git 1.0 (2005) — le serveur natif d'origine de Git, conçu pour une vitesse de transfert maximale sur réseau de confiance.
**Subtilités/confusions :**
- Le protocole `git://` n'offre AUCUN CHIFFREMENT ni AUCUNE AUTHENTIFICATION : tout le monde sur le réseau peut lire les données.
- Ne permet l'écriture (`push`) que si elle est explicitement activée avec `--enable=receive-pack` (extrêmement déconseillé sans pare-feu).
**Urgences/dangers :** ⚠️ Lancer `git daemon` sur un réseau Wi-Fi public expose l'intégralité de vos sources en clair à quiconque scanne le port 9418.
**Précautions :** Réservé exclusivement à des réseaux locaux fermés et de confiance ou pour du miroir public en lecture seule.
**Équivalents :** hg serve, svnserve
**Voir aussi :** git clone, git fetch, git http-backend

## `git http-backend` — Serveur Smart HTTP d'arrière-plan [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 68 | **Aliases :** —
**Contextes :** héberger son propre serveur Git d'entreprise derrière Apache ou Nginx avec le protocole HTTPS sécurisé
**Rôle :** Servir d'exécutable CGI/FastCGI pour gérer les requêtes de transfert Git (fetch/push) au-dessus du protocole Smart HTTP.
**Syntaxe :** Invoqué par le serveur web (Apache/Nginx/Caddy) via CGI.
**Cas réguliers :**
- Configurer Apache `ScriptAlias /git/ /usr/libexec/git-core/git-http-backend/` — Exposer les dépôts Git sur HTTPS
- `git config http.getanyfile true` — Autoriser le téléchargement des fichiers d'objets bruts par HTTP
**Origine :** Git 1.6.6 (2009) — a remplacé le protocole HTTP "Dumb" (lourd et lent) par le protocole "Smart HTTP" moderne capable de négocier les deltas.
**Subtilités/confusions :**
- Ce n'est pas un serveur web autonome : c'est un programme d'arrière-plan appelé par un vrai serveur web (Apache, Nginx, IIS).
- Gère l'authentification et les accès sécurisés en déléguant au serveur web hôte (Basic Auth, certificats TLS, OAuth).
**Urgences/dangers :** — (sécurité dépendante de la configuration du serveur web hôte)
**Précautions :** Toujours combiner avec un certificat TLS/SSL (HTTPS) pour protéger les mots de passe et les jetons de push.
**Équivalents :** git daemon, git clone, git push
**Voir aussi :** git daemon, git clone, git push

## `git fast-export` — Exporter le flux de données Git [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 62 | **Aliases :** —
**Contextes :** migrer un dépôt Git vers un autre système de contrôle de version, réécrire des historiques complets par script
**Rôle :** Convertir l'historique complet d'un dépôt Git en un flux textuel sérialisé structuré ultra-rapide.
**Syntaxe :** `git fast-export [options] <refs>`
**Cas réguliers :**
- `git fast-export --all > repo.dump` — Exporter la totalité des branches, tags et commits dans un fichier dump
- `git fast-export --signed-tags=strip HEAD` — Exporter en retirant la signature des tags
**Origine :** Git 1.5.4 (2008) — conçu pour permettre l'interopérabilité et le transfert de données à haute vitesse entre gestionnaires de révision.
**Subtilités/confusions :**
- Produit un flux textuel compréhensible par `git fast-import` ou d'autres outils de migration (Mercurial, Bazaar).
- Préserve la géométrie exacte du graphe des commits, les auteurs, les dates, les messages et les contenus des fichiers.
**Urgences/dangers :** — (lecture seule)
**Précautions :** S'assurer de disposer d'assez d'espace disque lors du dump d'un très grand dépôt.
**Équivalents :** hg out --template, svnadmin dump
**Voir aussi :** git fast-import, git filter-repo

## `git fast-import` — Importer un flux de données brutes [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 62 | **Aliases :** —
**Contextes :** importer un vieux dépôt SVN/CVS/Perforce vers Git à grande vitesse, créer des dépôts Git synthétiques par script
**Rôle :** Reconstruire à très haute vitesse une base d'objets Git à partir d'un flux de données sérialisées (provenant de `git fast-export` ou d'un script).
**Syntaxe :** `git fast-import [options] < repo.dump`
**Cas réguliers :**
- `git fast-import < repo.dump` — Reconstruire l'historique complet à partir d'un fichier de dump (le plus courant)
- `python3 convert_svn.py | git fast-import` — Injecter directement les commits convertis à la volée depuis un script
**Origine :** Git 1.5.4 (2008) — développé spécifiquement pour rendre les migrations vers Git des dizaines de fois plus rapides que par des commits individuels.
**Subtilités/confusions :**
- contourne les vérifications haut niveau de Git pour écrire directement les paquets d'objets (*packfiles*) : vitesse de traitement impressionnante.
- Nécessite que le flux d'entrée respecte rigoureusement la grammaire exacte du format `fast-import`.
**Urgences/dangers :** ⚠️ Importer un flux mal formé peut générer un dépôt corrompu : toujours valider le résultat avec `git fsck`.
**Précautions :** Exécuter `git fsck` immédiatement après la fin d'une opération `git fast-import`.
**Équivalents :** svnadmin load, hg import
**Voir aussi :** git fast-export, git fsck, git filter-repo

## `git filter-repo` — Réécrire l'historique du dépôt [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 82 | **Aliases :** —
**Contextes :** supprimer définitivement un mot de passe ou une clé privée commite par erreur, nettoyer les gros binaires de l'historique, scinder un dossier en dépôt séparé
**Rôle :** Réécrire profondément l'historique d'un dépôt Git de manière polyvalente, sûre et ultra-rapide (remplaçant officiel de `git filter-branch` et BFG).
**Syntaxe :** `git filter-repo [options]`
**Cas réguliers :**
- `git filter-repo --invert-paths --path .env` — Effacer définitivement le fichier `.env` de TOUS les commits de l'histoire du dépôt
- `git filter-repo --strip-blobs-bigger-than 50M` — Purger tous les fichiers de plus de 50 Mo de tout l'historique
- `git filter-repo --analyze` — Analyser le dépôt pour repérer les plus gros répertoires et extensions
- `git filter-repo --subdirectory-filter src/` — Transformer le sous-dossier `src/` en racine d'un nouveau dépôt propre
**Origine :** Michael Haggerty (2019) — créé pour remplacer la commande obsolète et dangereuse `git filter-branch` préconisée officiellement par l'équipe Git.
**Subtilités/confusions :**
- Outil Python externe officiellement recommandé par le projet Git (`pip install git-filter-repo`).
- `filter-repo` réécrit TOUS les SHA de commits affectés : tous les développeurs doivent ré-cloner le dépôt propre après son passage.
- Supprime automatiquement le lien `origin` par sécurité pour éviter un `git push` involontaire qui écraserait le serveur.
**Urgences/dangers :** ⚠️ Réécrit irréversiblement l'histoire du dépôt local : TOUJOURS faire une copie de sauvegarde complète du dossier `.git` avant !
**Précautions :** Effectuer la manipulation sur une copie fraîchement clonée du dépôt ; ré-inscrire les mots de passe et clés nettoyés (rotation).
**Équivalents :** BFG Repo-Cleaner, git filter-branch (obsolète), hg convert
**Voir aussi :** git reset, git reflog, git gc, git push

## `git send-email` — Envoyer des patchs par courriel [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 66 | **Aliases :** —
**Contextes :** contribuer au projet Linux, PostgreSQL ou Git, envoyer des séries de commits révisés par courriel via un serveur SMTP
**Rôle :** Envoyer une série de fichiers de patchs (générés par `git format-patch`) sous forme de courriels formatés via un serveur SMTP.
**Syntaxe :** `git send-email [options] <fichiers-patch|dossier>`
**Cas réguliers :**
- `git send-email --to="liste@kernel.org" 0001-fix.patch` — Envoyer un patch au destinataire spécifié
- `git send-email --annotate *.patch` — Réviser et éditer chaque courriel interactivement avant l'envoi
- `git config --global sendemail.smtpserver smtp.example.com` — Configurer son serveur SMTP de départ
**Origine :** Git 1.0 (2005) — l'outil privilégié de l'écosystème du logiciel libre fonctionnant par revue de code par courriel (Mailing Lists).
**Subtilités/confusions :**
- Envoie les patchs en texte brut sans altérer l'indentation ni les fins de ligne (ce que font souvent les clients courriels classiques comme Outlook).
- Conserve le fil des discussions (*threading*) en liant les courriels par les en-têtes `In-Reply-To`.
**Urgences/dangers :** ⚠️ Tester la configuration SMTP avec `--suppress-cc=all` ou vers sa propre adresse d'abord pour éviter le spam involontaire sur les listes publiques.
**Précautions :** Utiliser des jetons d'application (App Passwords) pour les serveurs Gmail ou Outlook sécurisés par 2FA.
**Équivalents :** hg email
**Voir aussi :** git am, git am, git config

## `git request-pull` — Résumé de demande d'intégration [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 68 | **Aliases :** —
**Contextes :** demander à un mainteneur d'intégrer une branche de fonctionnalités par courriel ou ticket sans passer par une Pull Request GitHub
**Rôle :** Générer un résumé synthétique de modifications (statistiques, commits, d'où puller) à soumettre à un mainteneur principal.
**Syntaxe :** `git request-pull <start> <url> [<end>]`
**Cas réguliers :**
- `git request-pull v1.0 https://github.com/mon-fork/app.git dev` — Générer la demande d'intégration de la branche `dev` depuis la version `v1.0`
- `git request-pull -p v1.0 https://github.com/mon-fork/app.git dev` — Inclure le patch complet (`-p`) pour une revue hors-ligne sans accès réseau
- `git request-pull v1.0 https://github.com/mon-fork/app.git` — Demande portant sur HEAD quand la branche finale est omise (fin implicite)
- `git request-pull HEAD~10 origin main > demande.txt` — Enregistrer la demande dans un fichier pour l'envoyer par courriel à un mainteneur
**Origine :** Git 1.0 (2005) — l'ancêtre direct du concept moderne de "Pull Request" popularisé par GitHub.
**Subtilités/confusions :**
- Ne fait AUCUNE ACTION sur le réseau : produit uniquement un texte récapitulatif à copier-coller ou à envoyer par courriel.
- Vérifie que la branche distante spécifiée est bien à jour avec les commits présentés dans la demande.
**Urgences/dangers :** — (lecture seule)
**Précautions :** S'assurer que le dépôt distant mentionné dans l'URL est accessible publiquement par le mainteneur.
**Équivalents :** GitHub Pull Request, GitLab Merge Request
**Voir aussi :** git send-email, git am, git log

## `git gitweb` — Interface web de consultation de dépôt [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 64 | **Aliases :** —
**Contextes :** consulter des dépôts sur un serveur Git auto-hébergé, offrir une interface web légère sans installer GitLab ou Gitea
**Rôle :** Script CGI en Perl fournissant une interface web d'exploration des dépôts Git (arborescence, commits, diffs, tags, auteurs).
**Syntaxe :** Exécuté par un serveur web CGI ou via `git instaweb`.
**Cas réguliers :**
- Accéder à l'interface `http://localhost/cgi-bin/gitweb.cgi` — Naviguer visuellement dans l'historique et les fichiers du dépôt
- `git instaweb --start` — Démarrer le serveur web local avec les réglages par défaut
- `git instaweb --httpd=webrick --port=1234` — Lancer l'interface web locale sans configurer Apache ni Nginx
- `git instaweb --stop` — Arrêter proprement l'instance locale après consultation
**Origine :** Kay Sievers & Kay Torvalds (2005) — première interface web historique développée pour l'écosystème Git.
**Subtilités/confusions :**
- Interface web très rustique mais d'une légèreté et d'une compatibilité inégalées.
- Base technique sous-jacente utilisée par `git instaweb`.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pour des besoins modernes d'équipe avec revue de code et gestion d'issues, lui préférer des forges modernes comme Forgejo, Gitea ou GitLab.
**Équivalents :** cgit, Gitea, GitLab, GitHub
**Voir aussi :** git instaweb, git daemon, git show

## `git rev-parse` — Analyser et extraire des références [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 74 | **Aliases :** —
**Contextes :** écrire des scripts Shell/Python pour Git, vérifier si l'on est dans un dépôt Git, obtenir le SHA absolu de HEAD
**Rôle :** Analyser et convertir des paramètres, noms de branches ou révisions relatives en objets SHA-1 ou chemins absolus du système.
**Syntaxe :** `git rev-parse [options] <args>`
**Cas réguliers :**
- `git rev-parse HEAD` — Obtenir le SHA complet à 40 caractères du commit actuel (très courant en CI/CD)
- `git rev-parse --show-toplevel` — Obtenir le chemin absolu de la racine du dépôt courant
- `git rev-parse --is-inside-work-tree` — Tester si le dossier courant est à l'intérieur d'un dépôt Git (renvoie `true` ou `false`)
- `git rev-parse --short HEAD` — Obtenir l'empreinte SHA courte (7 caractères) du dernier commit
**Origine :** Git 1.0 (2005) — l'outil de plomberie (*plumbing*) par excellence pour les auteurs de scripts et d'outils s'appuyant sur Git.
**Subtilités/confusions :**
- Outil essentiel de sécurisation des scripts : permet de valider qu'un argument est bien une référence Git valide avant d'exécuter d'autres commandes.
- `git rev-parse --git-dir` retourne le chemin du dossier `.git` (pratique pour cibler les hooks ou la conf).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser systématiquement `git rev-parse --is-inside-work-tree` au début des scripts d'automatisation.
**Équivalents :** hg identify --id
**Voir aussi :** git cat-file, git status, git log

## `git cat-file` — Inspecter le contenu brut des objets [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 70 | **Aliases :** —
**Contextes :** inspecter directement la base de données orientée objets de Git, écrire des outils de bas niveau, déboguer des objets corrompus
**Rôle :** Afficher le type, la taille ou le contenu brut d'un objet quelconque stocké dans la base d'objets `.git/objects/`.
**Syntaxe :** `git cat-file <type | -t | -s | -p> <objet>`
**Cas réguliers :**
- `git cat-file -p HEAD` — Inspecter le contenu textuel brut structuré du commit sur HEAD (arbre, parents, auteur, message)
- `git cat-file -t 4b2a1c` — Afficher le TYPE de l'objet Git (`commit`, `tree`, `blob` ou `tag`)
- `git cat-file -s HEAD` — Obtenir la taille exacte de l'objet en octets
- `git cat-file -p HEAD^{tree}` — Lister le contenu de l'objet arbre (*tree*) pointé par le dernier commit
**Origine :** Git 1.0 (2005) — commande fondamentale de l'architecture "Content-Addressable Filesystem" de Git inventée par Linus Torvalds.
**Subtilités/confusions :**
- Révèle la simplicité mécanique de Git : un commit n'est qu'un fichier texte contenant un pointeur vers un `tree`, des `parents` et un message.
- L'option `-p` (*pretty-print*) adapte l'affichage au type d'objet (décodes les arbres, affiche les blobs de code).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Outil de plomberie réservé au débogage interne et au développement d'outils intégrant Git.
**Équivalents :** git rev-parse, git show, git fsck
**Voir aussi :** git rev-parse, git show, git fsck










