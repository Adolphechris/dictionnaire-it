# Face A — Commandes : GIT ET CONTRÔLE DE VERSION (fiches riches v3)

> Lot MVP #024 — cible 60 fiches. Avancement : 14/60 (bloc 1 : socle Git — git, init, clone, status, add, commit, diff, push, pull, log, branch, switch, checkout, fetch). Format : `## \`commande\` — titre [OS]` + 10 rubriques obligatoires validées par `tools/parse_rich.py`.

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





