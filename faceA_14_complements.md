## `hexdump` — Inspection binaire et hexadécimale de fichiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** inspecter le contenu binaire brut d'un fichier, analyser des en-têtes de fichiers corrompus ou vérifier des octets non imprimables
**Rôle :** Outil CLI d'inspection binaire qui affiche le contenu d'un fichier sous forme d'octets au format hexadécimal, octal, décimal ou ASCII.
**Syntaxe :** `hexdump [options] <fichier>`
**Cas réguliers :**
- `hexdump -C fichier.bin` — Affichage canonique hexadécimal et ASCII côte à côte
- `hexdump -n 64 -C fichier.bin` — Inspecter uniquement les 64 premiers octets du fichier
**Origine :** BSD / util-linux.
**Subtilités/confusions :**
- L'option `-C` (canonique) est la plus lisible car elle affiche l'offset, les octets hexadécimaux et leur équivalent ASCII imprimable.
**Urgences/dangers :** —
**Précautions :** Idéal pour vérifier la présence d'un *Byte Order Mark* (BOM) UTF-8 ou de caractères de retour chariot Windows (`\r\n`).
**Équivalents :** xxd, od, odump
**Voir aussi :** xxd, file, od

## `xxd` — Vidage hexadécimal et outil de réécriture binaire [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** convertir un fichier binaire en représentation hexadécimale, modifier des octets spécifiques, puis reconstruire le binaire d'origine (*patching binaire*)
**Rôle :** Générateur de vidages hexadécimaux et outil inverse capable de reconvertir du texte hexadécimal en binaire natif (`xxd -r`).
**Syntaxe :** `xxd [options] [fichier_entree] [fichier_sortie]`
**Cas réguliers :**
- `xxd image.png` — Afficher le vidage hexadécimal d'une image
- `xxd -p fichier.bin` — Exporter sous forme d'une simple chaîne hexadécimale continue sans offsets
- `xxd -r dump.hex binaire_reconstruit` — Reconstruire le fichier binaire d'origine à partir du texte hexadécimal !
**Origine :** Juergen Weigert (1990) — distribué historiquement avec l'éditeur Vim.
**Subtilités/confusions :**
- La fonction d'inversion (`-r`) fait de `xxd` un outil de choix pour patcher des binaires ou injecter des payloads dans des tests de sécurité.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Rediriger la sortie vers un fichier texte avant d'éditer les octets à modifier.
**Équivalents :** hexdump, od
**Voir aussi :** hexdump, file
## `dc` — Calculatrice en notation polonaise inverse (RPN) [Linux/macOS]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** effectuer des calculs mathématiques en ligne de commande en utilisant une pile et la notation polonaise inverse sans parenthèses
**Rôle :** Calculatrice en précision arbitraire utilisant la notation polonaise inverse (RPN / Reverse Polish Notation) fonctionnant sur une pile de données.
**Syntaxe :** `dc [options] [fichier_expression]`
**Cas réguliers :**
- `dc -e "5 3 + p"` — Empiler 5, empiler 3, ajouter (`+`), puis afficher le sommet de la pile (`p`) -> affiche 8
- `dc -e "100 20 / p"` — Diviser 100 par 20 et afficher le résultat
**Origine :** Robert Morris / Lorinda Cherry (Bell Labs, 1970) — le tout premier langage de programmation à avoir tourné sur le tout premier système UNIX !
**Subtilités/confusions :**
- Précède historiquement `bc` ; en fait, les premières versions de `bc` étaient un pré-processeur traduisant les expressions vers `dc` !
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Ne pas oublier la commande `p` à la fin d'une expression pour imprimer le résultat sur la sortie standard.
**Équivalents :** bc, expr
**Voir aussi :** bc, awk
## `factor` — Décomposition d'entiers en facteurs premiers [Linux/macOS]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** —
**Contextes :** décomposer un nombre entier en le produit de ses facteurs premiers lors de résolutions de problèmes mathématiques ou d'exercices d'algorithmique
**Rôle :** Utilitaire Coreutils qui calcule et affiche les facteurs premiers d'un ou plusieurs nombres entiers donnés en paramètre.
**Syntaxe :** `factor [nombre...]`
**Cas réguliers :**
- `factor 42` — Affiche `42: 2 3 7`
- `factor 2026` — Affiche `2026: 2 1013`
- `seq 1 10 | factor` — Traiter une série de nombres lus depuis l'entrée standard
**Origine :** Utilitaire UNIX historique (System V / GNU Coreutils).
**Subtilités/confusions :**
- Gère de très grands entiers arbitraires grâce aux algorithmes de factorisation modernes du projet GNU.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Sur de très grands entiers cryptographiques (ex: 2048 bits), la factorisation peut prendre un temps considérable.
**Équivalents :** bc, python3
**Voir aussi :** seq, expr
## `envsubst` — Substitution de variables d'environnement dans un modèle [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** générer des fichiers de configuration dynamiques (Nginx, Kubernetes, Docker Compose) à partir de modèles (*templates*) contenant des variables `$VAR`
**Rôle :** Outil du paquet GNU gettext qui remplace les références aux variables d'environnement shell (`$VAR` ou `${VAR}`) par leurs valeurs réelles dans un texte.
**Syntaxe :** `envsubst [SHELL-FORMAT] < template.conf > output.conf`
**Cas réguliers :**
- `envsubst < nginx.conf.template > /etc/nginx/nginx.conf` — Remplacer toutes les variables d'environnement dans le modèle Nginx
- `envsubst '$PORT $HOST' < config.template > config.json` — Remplacer EXCLUSIVEMENT les variables `$PORT` et `$HOST` sans toucher aux autres expressions `$` du fichier
**Origine :** Projet GNU gettext (1995).
**Subtilités/confusions :**
- Si un nom de variable à remplacer n'est pas spécifié avec la syntaxe restreinte `envsubst '$VAR'`, toutes les variables non définies seront remplacées par des chaînes vides !
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Toujours lister explicitement les variables à substituer (`envsubst '$VAR1 $VAR2'`) lorsqu'on traite des fichiers contenant des expressions JavaScript ou Bash.
**Équivalents :** sed, envtpl, gomplate
**Voir aussi :** sed, export, printenv
## `iconv` — Conversion du jeu de caractères / encodage de fichiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** convertir des fichiers texte encodés en ISO-8859-1 (Latin-1) ou Windows-1252 vers le standard moderne UTF-8 (ou inversement) pour éviter les caractères corrompus
**Rôle :** Outil standard de conversion d'encodage de caractères entre divers jeux (UTF-8, UTF-16, ISO-8859-15, ASCII, Shift-JIS…).
**Syntaxe :** `iconv -f <encodage_source> -t <encodage_cible> fichier.txt -o sortie.txt`
**Cas réguliers :**
- `iconv -f ISO-8859-1 -t UTF-8 fichier_latin1.txt -o fichier_utf8.txt` — Convertir un fichier Latin-1 vers UTF-8
- `iconv -l` — Lister tous les jeux de caractères supportés par le système
- `iconv -f UTF-8 -t ASCII//TRANSLIT entree.txt` — Translittérer les caractères accentués UTF-8 en ASCII pur (ex: `é` devient `e`)
**Origine :** Spécification Open Group / POSIX (1993) — implémenté par la GNU C Library (glibc).
**Subtilités/confusions :**
- L'option `//TRANSLIT` tente de remplacer les caractères indisponibles par des équivalents proches ; `//IGNORE` ignore les caractères non convertibles.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Vérifier l'encodage de départ avec la commande `file -i fichier.txt` avant de lancer `iconv`.
**Équivalents :** uchardet, recode
**Voir aussi :** file, dos2unix, enca
## `dos2unix` — Conversion des fins de lignes Windows (CRLF) en UNIX (LF) [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** corriger les erreurs de syntaxe des scripts shell édités sous Windows (erreur classique : `\r: command not found`) en supprimant les retours chariot `\r`
**Rôle :** Outil de conversion de format de fichier texte qui remplace les sauts de ligne Windows (`CRLF` / `\r\n`) par des sauts de ligne UNIX (`LF` / `\n`).
**Syntaxe :** `dos2unix [options] [fichier...]`
**Cas réguliers :**
- `dos2unix script.sh` — Convertir les fins de lignes de `script.sh` directement en place
- `dos2unix -n entree.txt sortie.txt` — Convertir tout en conservant le fichier d'origine intact
- `find . -type f -name "*.py" -exec dos2unix {} +` — Convertir tous les fichiers Python d'un projet
**Origine :** Benjamin Lin / Erwin Waterlander (1989) — utilitaire indispensable en environnement mixte Windows/Linux.
**Subtilités/confusions :**
- Modifie directement le fichier par défaut ; utiliser `-n` (new file) si l'on souhaite créer une copie.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Configurer `core.autocrlf` dans Git pour éviter de commiter des retours chariot Windows par inadvertance.
**Équivalents :** unix2dos, sed 's/\r$//', tr -d '\r'
**Voir aussi :** unix2dos, sed, iconv
## `unix2dos` — Conversion des fins de lignes UNIX (LF) en Windows (CRLF) [Linux/macOS]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** —
**Contextes :** convertir un fichier texte généré sous Linux pour qu'il s'affiche correctement dans le Bloc-notes de vieilles versions de Windows
**Rôle :** Outil inverse de `dos2unix` qui transforme les fins de lignes UNIX (`LF` / `\n`) en fins de lignes Windows (`CRLF` / `\r\n`).
**Syntaxe :** `unix2dos [options] [fichier...]`
**Cas réguliers :**
- `unix2dos document.txt` — Convertir le fichier texte en place avec fins de lignes Windows
- `unix2dos -n linux.txt windows.txt` — Convertir vers un nouveau fichier de sortie
**Origine :** Erwin Waterlander (1989).
**Subtilités/confusions :**
- Principalement utile lors de la préparation de fichiers de configuration ou de scripts destinés à être exécutés sur d'anciens systèmes Windows.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Ne pas appliquer `unix2dos` sur des scripts shell destinés à s'exécuter sous Linux.
**Équivalents :** dos2unix, sed
**Voir aussi :** dos2unix, iconv
## `fold` — Ajustement de la largeur des lignes d'un texte [Linux/macOS]
**Niveau :** debutant | **Popularité :** 76 | **Aliases :** —
**Contextes :** découper des lignes de texte trop longues à une largeur fixe donnée (ex: 80 colonnes) pour un affichage propre en terminal ou pour de l'impression
**Rôle :** Utilitaire Coreutils qui insère un saut de ligne dès qu'une ligne dépasse une largeur maximale spécifiée.
**Syntaxe :** `fold [options] [fichier]`
**Cas réguliers :**
- `fold -w 80 document.txt` — Découper les lignes de `document.txt` à 80 caractères de large
- `fold -s -w 70 document.txt` — Découper à 70 caractères en coupant aux espaces (*blank spaces*) sans couper au milieu d'un mot !
**Origine :** Utilitaire UNIX historique (BSD / GNU Coreutils).
**Subtilités/confusions :**
- Sans l'option `-s` (space), `fold` coupe brutalement au milieu des mots dès qu'il atteint la colonne spécifiée.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Toujours combiner `-s` avec `-w` pour obtenir une mise en page lisible de paragraphes.
**Équivalents :** fmt, column
**Voir aussi :** fmt, column, cut
## `fmt` — Reformateur et metteur en page de paragraphes de texte [Linux/macOS]
**Niveau :** debutant | **Popularité :** 81 | **Aliases :** —
**Contextes :** nettoyer et réaligner des paragraphes de texte brut, joindre des lignes coupées manuellement ou ajuster la largeur de documentation
**Rôle :** Formateur de texte simple qui rassemble et redistribue les mots d'un paragraphe pour obtenir des lignes d'une longueur équilibrée.
**Syntaxe :** `fmt [options] [fichier]`
**Cas réguliers :**
- `fmt document.txt` — Reformater les paragraphes du fichier à la largeur standard (75 colonnes)
- `fmt -w 60 document.txt` — Reformater les paragraphes avec une largeur maximale de 60 caractères
- `fmt -u document.txt` — Uniformiser les espaces : 1 espace entre les mots, 2 espaces après chaque point
**Origine :** Utilitaire UNIX historique (BSD 3.0, 1980 / GNU Coreutils).
**Subtilités/confusions :**
- Contrairement à `fold` qui coupe les lignes longues, `fmt` sait à la fois remplir les lignes courtes et découper les lignes longues pour former de vrais paragraphes.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Préserve les retours à la ligne vides séparant les paragraphes ainsi que l'indentation de début de paragraphe.
**Équivalents :** fold, column, par
**Voir aussi :** fold, column
## `column` — Formatage de données sous forme de tableau aligné [Linux/macOS]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** rendre lisible un fichier CSV, un fichier séparé par des deux-points (`/etc/passwd`) ou la sortie brute d'un script en l'alignant proprement sous forme de colonnes
**Rôle :** Utilitaire du paquet `util-linux` qui prend du texte brut délimité et le réorganise en un tableau visuellement parfait.
**Syntaxe :** `column [options] [fichier]`
**Cas réguliers :**
- `column -t -s: /etc/passwd` — Formater `/etc/passwd` en tableau aligné en utilisant `:` comme séparateur
- `cat donnees.csv | column -t -s,` — Formater un fichier CSV en tableau lisible dans le terminal
- `column -t -J -s, file.csv` — Convertir un fichier CSV en structure JSON !
**Origine :** BSD 4.3 (1989) / intégré dans util-linux.
**Subtilités/confusions :**
- L'option `-t` (table) est obligatoire pour activer l'alignement en colonnes réelles.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Idéal pour formater la sortie de vos propres scripts Bash pour les rendre lisibles.
**Équivalents :** awk, pr
**Voir aussi :** fmt, fold, awk, cut
## `expand` — Conversion des tabulations en espaces [Linux/macOS]
**Niveau :** debutant | **Popularité :** 78 | **Aliases :** —
**Contextes :** remplacer les tabulations d'un fichier source par un nombre fixe d'espaces (ex: 4 espaces) pour garantir un affichage uniforme dans tous les éditeurs
**Rôle :** Outil Coreutils qui remplace chaque caractère de tabulation (`\t`) d'un fichier par la quantité d'espaces correspondante.
**Syntaxe :** `expand [options] [fichier]`
**Cas réguliers :**
- `expand file.txt` — Remplacer les tabulations par des espaces (8 espaces par défaut)
- `expand -t 4 file.txt > file_spaces.txt` — Remplacer chaque tabulation par 4 espaces
**Origine :** BSD / GNU Coreutils.
**Subtilités/confusions :**
- Ne pas appliquer `expand` sur un `Makefile` (dont les règles exigent impérativement des tabulations).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser `unexpand` pour effectuer l'opération inverse (espaces vers tabulations).
**Équivalents :** unexpand, sed
**Voir aussi :** unexpand, fmt, fold
## `unexpand` — Conversion des espaces en tabulations [Linux/macOS]
**Niveau :** debutant | **Popularité :** 74 | **Aliases :** —
**Contextes :** convertir des espaces de début de ligne en caractères de tabulation pour se conformer aux règles de style de certains projets ou Makefiles
**Rôle :** Utilitaire Coreutils inverse d'`expand` qui remplace les séquences d'espaces par des caractères de tabulation (`\t`).
**Syntaxe :** `unexpand [options] [fichier]`
**Cas réguliers :**
- `unexpand -t 4 file.txt > file_tabs.txt` — Convertir des groupes de 4 espaces en une tabulation
- `unexpand -a file.txt` — Convertir TOUS les groupes d'espaces du fichier (et pas seulement ceux de début de ligne)
**Origine :** BSD / GNU Coreutils.
**Subtilités/confusions :**
- Par défaut sans `-a`, `unexpand` ne convertit que les espaces situés au début de chaque ligne (indentation).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Toujours vérifier le résultat avec `cat -A` pour distinguer visuellement les espaces (`.`) des tabulations (`^I`).
**Équivalents :** expand, sed
**Voir aussi :** expand, cat
## `rev` — Inversion de l'ordre des caractères de chaque ligne [Linux/macOS]
**Niveau :** debutant | **Popularité :** 79 | **Aliases :** —
**Contextes :** inverser le sens de lecture des caractères d'un texte, extraire des extensions de fichiers ou traiter des chaînes de droite à gauche
**Rôle :** Utilitaire Coreutils qui lit l'entrée standard ou un fichier et écrit chaque ligne avec ses caractères inversés de droite à gauche.
**Syntaxe :** `rev [fichier]`
**Cas réguliers :**
- `echo "Hello World" | rev` — Affiche `dlroW olleH`
- `echo "/path/to/file.tar.gz" | rev | cut -d. -f1 | rev` — Astuce classique pour extraire la dernière extension (`gz`) !
**Origine :** Utilitaire UNIX historique (BSD 4.3).
**Subtilités/confusions :**
- `rev` inverse l'ordre des **caractères sur une même ligne**, alors que `tac` inverse l'ordre des **lignes dans le fichier**.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Très utile combiné à `cut` pour cibler le dernier champ d'une ligne séparée par des délimiteurs variables.
**Équivalents :** tac (inversion des lignes)
**Voir aussi :** tac, cut, sed
## `tac` — Affichage d'un fichier de bas en haut (ligne par ligne inverse) [Linux/macOS]
**Niveau :** debutant | **Popularité :** 87 | **Aliases :** —
**Contextes :** lire un fichier de log ou un journal de transactions dans l'ordre chronologique inverse (les événements les plus récents en premier)
**Rôle :** Anagramme de `cat` qui affiche les lignes d'un fichier en ordre inverse (de la dernière ligne vers la première ligne).
**Syntaxe :** `tac [options] [fichier]`
**Cas réguliers :**
- `tac /var/log/syslog | head -n 20` — Afficher les 20 lignes les plus récentes d'un journal de log
- `tac fichier.txt` — Inverser complètement l'ordre des lignes
**Origine :** GNU Coreutils.
**Subtilités/confusions :**
- Ne pas confondre avec `rev` (qui inverse les caractères sur chaque ligne) ni avec `cat` (qui lit de haut en bas).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Sur macOS, si `tac` n'est pas disponible par défaut, utiliser `tail -r` ou installer `coreutils` via Homebrew (`gtac`).
**Équivalents :** tail -r, sed -n '1!G;h;$p'
**Voir aussi :** cat, rev, tail
## `comm` — Comparaison de deux fichiers triés ligne par ligne [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 83 | **Aliases :** —
**Contextes :** identifier les lignes uniques au fichier A, uniques au fichier B et communes aux deux fichiers (ex: comparer des listes de clients ou d'IPs)
**Rôle :** Outil Coreutils qui compare deux fichiers préalablement triés et affiche le résultat sur 3 colonnes (1: seulement dans A, 2: seulement dans B, 3: présent dans les deux).
**Syntaxe :** `comm [options] fichierA.txt fichierB.txt`
**Cas réguliers :**
- `comm fichierA.txt fichierB.txt` — Afficher la comparaison sur 3 colonnes
- `comm -12 fichierA.txt fichierB.txt` — Masquer les colonnes 1 et 2 pour n'afficher que les lignes COMMUNE AUX DEUX fichiers (intersection !)
- `comm -23 fichierA.txt fichierB.txt` — Afficher uniquement les lignes présentes dans A mais PAS dans B (différence d'ensembles !)
**Origine :** Utilitaire UNIX historique (AT&T Unix, 1970s / GNU Coreutils).
**Subtilités/confusions :**
- **IMPÉRATIF :** Les deux fichiers DOIVENT être triés (`sort`) avant d'exécuter `comm`, sinon le résultat est erroné.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser la substitution de processus pour trier à la volée : `comm -12 <(sort file1) <(sort file2)`.
**Équivalents :** diff, sdiff, cmp
**Voir aussi :** sort, diff, uniq
## `cmp` — Comparaison d'octet par octet de deux fichiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** vérifier si deux fichiers (binaires ou images) sont 100% identiques, ou trouver le tout premier octet où ils diffèrent
**Rôle :** Outil de comparaison binaire bas niveau qui indique la ligne et le numéro d'octet du premier écart rencontré entre deux fichiers.
**Syntaxe :** `cmp [options] fichier1 fichier2`
**Cas réguliers :**
- `cmp fichier1.bin fichier2.bin` — Afficher le premier octet et la première ligne où les deux fichiers divergent
- `cmp -s file1 file2` — Mode silencieux (`-s`) : ne rien afficher sur STDOUT, mais retourner le code de sortie `0` si identiques, `1` si différents
**Origine :** AT&T Unix (1970s).
**Subtilités/confusions :**
- Contrairement à `diff` (qui compare du texte ligne à ligne), `cmp` est conçu pour les fichiers binaires de n'importe quel type.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Pratique dans des scripts d'automatisation avec `cmp -s` pour tester l'égalité de deux fichiers sans générer de sortie texte.
**Équivalents :** diff, md5sum, sha256sum
**Voir aussi :** diff, comm, md5sum
## `paste` — Fusion ligne à ligne côte à côte de plusieurs fichiers [Linux/macOS]
**Niveau :** debutant | **Popularité :** 84 | **Aliases :** —
**Contextes :** combiner deux colonnes de données provenant de deux fichiers différents en un seul fichier (ex: joindre noms et adresses email)
**Rôle :** Outil Coreutils qui lit les lignes de plusieurs fichiers et les associe côte à côte en les séparant par des tabulations.
**Syntaxe :** `paste [options] fichier1 fichier2...`
**Cas réguliers :**
- `paste noms.txt emails.txt` — Associer la ligne 1 de `noms.txt` avec la ligne 1 de `emails.txt` séparées par une tabulation
- `paste -d',' noms.txt emails.txt` — Utiliser une virgule comme délimiteur à la place de la tabulation (génération de CSV !)
- `paste -s file.txt` — Joindre toutes les lignes d'un SEUL fichier en une unique ligne continue
**Origine :** AT&T Unix / GNU Coreutils.
**Subtilités/confusions :**
- Ne fait aucun rapprochement sémantique : il associe simplement la ligne N du fichier 1 avec la ligne N du fichier 2.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Si vous avez besoin de joindre deux fichiers selon une clé commune, utiliser `join` plutôt que `paste`.
**Équivalents :** join, column, pr
**Voir aussi :** join, cut, column
## `join` — Fusion de fichiers sur la base d'un champ clé commun [Linux/macOS]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** réaliser une opération équivalente au `INNER JOIN` de SQL sur deux fichiers texte plat ayant une colonne en commun (ex: ID utilisateur)
**Rôle :** Utilitaire de fusion relationnelle qui joint les lignes de deux fichiers triés qui partagent un champ clé identique.
**Syntaxe :** `join [options] fichier1.txt fichier2.txt`
**Cas réguliers :**
- `join -1 1 -2 1 users.txt roles.txt` — Joindre le fichier `users.txt` (clé dans col 1) et `roles.txt` (clé dans col 1)
- `join -t',' -1 2 -2 1 clients.csv commandes.csv` — Joindre deux fichiers CSV en utilisant une virgule comme séparateur
**Origine :** AT&T Unix / GNU Coreutils.
**Subtilités/confusions :**
- Tout comme `comm`, les deux fichiers de départ DOIVENT impérativement être triés sur leur champ de jointure respectif !
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Tri préalable indispensable via `sort -k` avant d'invoquer `join`.
**Équivalents :** awk, paste
**Voir aussi :** paste, sort, comm, awk
## `nl` — Numérotation des lignes d'un fichier avec options avancées [Linux/macOS]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** —
**Contextes :** ajouter des numéros de lignes à un document ou fichier source pour impression ou révision, avec contrôle sur la numérotation des lignes vides
**Rôle :** Filtre de numérotation de lignes plus puissant et configurable que `cat -n`.
**Syntaxe :** `nl [options] [fichier]`
**Cas réguliers :**
- `nl script.py` — Numéroter toutes les lignes non vides du fichier
- `nl -ba script.py` — Numéroter TOUTES les lignes (y compris les lignes entièrement vides)
- `nl -w3 -s": " file.txt` — Utiliser une largeur de 3 chiffres et le séparateur `: ` (ex: `001: Texte`)
**Origine :** System V / GNU Coreutils.
**Subtilités/confusions :**
- Par défaut (mode `-bt`), `nl` ne numérote pas les lignes vides, contrairement à `cat -n` qui numérote tout indifféremment.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Très pratique pour générer des extraits de code source numérotés pour des rapports ou documentations.
**Équivalents :** cat -n, awk '{print NR, $0}'
**Voir aussi :** cat, fold, fmt
## `shuf` — Mélange aléatoire de lignes de texte [Linux/macOS]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** tirer une ligne au sort dans un fichier, mélanger aléatoirement une liste de données (ex: dataset d'apprentissage Machine Learning)
**Rôle :** Générateur de permutations aléatoires qui mélange les lignes de son entrée standard ou d'un fichier.
**Syntaxe :** `shuf [options] [fichier]`
**Cas réguliers :**
- `shuf mots.txt` — Afficher l'intégralité des lignes du fichier dans un ordre aléatoire
- `shuf -n 1 /usr/share/dict/words` — Sélectionner un seul mot au hasard dans le dictionnaire
- `shuf -i 1-100 -n 5` — Générer 5 nombres aléatoires distincts compris entre 1 et 100
**Origine :** GNU Coreutils (Paul Eggert, 2006).
**Subtilités/confusions :**
- L'option `-i 1-N` évite d'avoir à créer un fichier de nombres au préalable.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser `--random-source` avec un fichier déterministe pour obtenir des mélanges répétables dans des tests automatisés.
**Équivalents :** sort -R, random
**Voir aussi :** sort, seq, head
## `csplit` — Découpage contextuel de fichiers basé sur des motifs [Linux/macOS]
**Niveau :** avance | **Popularité :** 77 | **Aliases :** —
**Contextes :** scinder un fichier massif en plusieurs petits fichiers à chaque apparition d'un séparateur ou d'une expression régulière (ex: scinder un fichier de logs par jour)
**Rôle :** Outil Coreutils qui découpe un fichier en sections définies par des lignes de séparation ou des motifs regex.
**Syntaxe :** `csplit [options] fichier motif...`
**Cas réguliers :**
- `csplit -z document.txt '/^## /' '{*}'` — Découper un document Markdown à chaque titre de niveau 2 (`## `) autant de fois que possible (`{*}`) !
- `csplit -f fiche_ fichier.txt '/CHAPTER/' '{5}'` — Découper aux 5 premières occurrences du mot `CHAPTER` avec le préfixe `fiche_`
**Origine :** System V / GNU Coreutils.
**Subtilités/confusions :**
- Diffère de `split` (qui découpe par taille en octets ou nombre de lignes fixe) en découpant de manière dynamique selon le contenu texte.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** L'option `-z` évite la création de fichiers de sortie vides si le motif correspond dès la première ligne.
**Équivalents :** split, awk
**Voir aussi :** split, awk, sed
## `truncate` — Modification explicite de la taille d'un fichier [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** vider instantanément un fichier de log saturé sans le supprimer (pour préserver les descripteurs ouverts), ou créer des fichiers creux (*sparse files*)
**Rôle :** Utilitaire Coreutils qui réduit ou agrandit la taille d'un fichier à la dimension exacte spécifiée.
**Syntaxe :** `truncate -s <taille> <fichier>`
**Cas réguliers :**
- `truncate -s 0 /var/log/app.log` — Vider instantanément le fichier de log à 0 octet sans le supprimer !
- `truncate -s 10G image.raw` — Créer un fichier de 10 Gigaoctets (fichier creux n'occupant pas d'espace physique tant qu'il n'est pas écrit)
- `truncate -s -1K fichier.txt` — Tronquer les 1024 derniers octets d'un fichier
**Origine :** FreeBSD / GNU Coreutils (Padraig Brady, 2008).
**Subtilités/confusions :**
- Faire `truncate -s 0 log.txt` est beaucoup plus propre que `rm log.txt` si un service est en train d'écrire dedans (évite d'invalider le file descriptor).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** ⚠️ Réduire la taille d'un fichier supprime définitivement les données situées au-delà de la nouvelle limite.
**Précautions :** Toujours vérifier deux fois la taille passée en paramètre.
**Équivalents :** fallocate, > file
**Voir aussi :** fallocate, stat, dd
## `fallocate` — Allocation rapide d'espace disque pour un fichier [Linux]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** pré-allouer instantanément un fichier de swap ou de stockage virtuel sans gaspiller de temps d'E/S CPU/Disque
**Rôle :** Utilitaire Linux (paquet `util-linux`) qui communique directement avec le système de fichiers (ext4, xfs) pour réserver des blocs physiques sur le disque sans écrire de zéro.
**Syntaxe :** `fallocate -l <taille> <fichier>`
**Cas réguliers :**
- `fallocate -l 4G /swapfile` — Créer et allouer instantanément un fichier de swap de 4 Gigaoctets en moins de 1 seconde !
- `fallocate -d fichier.img` — Détecter et libérer les trous de zéro dans un fichier (dé-allocation / hole punching)
**Origine :** Eric Sandeen / util-linux (2009) — s'appuie sur l'appel système `fallocate()`.
**Subtilités/confusions :**
- Contrairement à `dd if=/dev/zero`, `fallocate` ne fait pas d'écriture physique d'octets et s'exécute de manière quasi-instantanée quelle que soit la taille.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Certains systèmes de fichiers anciens ou virtuels ne supportent pas l'appel système `fallocate` ; utiliser `dd` en repli.
**Équivalents :** truncate, dd
**Voir aussi :** truncate, swapon, swap
## `stat` — Affichage détaillé des métadonnées et i-nœuds d'un fichier [Linux/macOS]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** vérifier la date d'accès, de modification et de changement de statut (atime, mtime, ctime), les permissions octales et le numéro d'i-nœud d'un fichier
**Rôle :** Outil de diagnostic qui extrait et affiche l'intégralité des métadonnées stockées dans la structure d'i-nœud (*inode*) d'un fichier.
**Syntaxe :** `stat [options] <fichier>`
**Cas réguliers :**
- `stat document.txt` — Afficher la taille, les blocs, les droits (octal/symbole), l'UID/GID, et les 3 horodatages (Access, Modify, Change)
- `stat -c "%a %n" *` — Afficher uniquement le masque de permissions octal (ex: `644`) et le nom de chaque fichier
- `stat -f /` — Afficher les métadonnées du système de fichiers hôte (espace libre, inodes disponibles)
**Origine :** François Pinard / GNU Coreutils (1993).
**Subtilités/confusions :**
- Distinguer `mtime` (modification du contenu) et `ctime` (changement de métadonnées/permissions).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** La syntaxe des options de formatage (`-c` sous Linux GNU contre `-f` sous macOS BSD) diffère légèrement selon l'OS.
**Équivalents :** ls -l, file
**Voir aussi :** file, ls, touch
## `file` — Détermination du type de fichier via les numéros magiques [Linux/macOS]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** identifier le format réel d'un fichier (ex: image, binaire, archive) même si son extension a été modifiée ou supprimée
**Rôle :** Outil d'inspection qui examine les premiers octets d'un fichier (*magic numbers*) et sa structure pour déterminer son type MIME ou son format réel.
**Syntaxe :** `file [options] <fichier>`
**Cas réguliers :**
- `file archive.unknown` — Affiche par exemple : `archive.unknown: gzip compressed data, speed top format`
- `file -i document.pdf` — Afficher le type MIME officiel (ex: `application/pdf; charset=binary`)
- `file /bin/bash` — Afficher le type de binaire exécutable (ex: `ELF 64-bit LSB executable, x86-64`)
**Origine :** Ian Darwin / Geoff Collyer (AT&T Unix 1973 / Fine Free File Command 1987).
**Subtilités/confusions :**
- `file` ne se fie JAMAIS à l'extension du fichier (ex: un binaire `.exe` renommé en `.png` sera correctement identifié comme binaire PE).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser `file -i` dans les scripts web pour valider le type des fichiers envoyés par les utilisateurs.
**Équivalents :** stat, hexdump
**Voir aussi :** stat, hexdump, xxd
## `pathchk` — Vérification de la portabilité et validité de chemins [Linux/macOS]
**Niveau :** avance | **Popularité :** 73 | **Aliases :** —
**Contextes :** s'assurer qu'un chemin de fichier ou nom de dossier ne contient pas de caractères invalides ou ne dépasse pas la longueur maximale autorisée sous d'autres OS
**Rôle :** Utilitaire Coreutils qui valide si un chemin de fichier est valide et portable sur les systèmes conformes à la norme POSIX.
**Syntaxe :** `pathchk [options] chemin...`
**Cas réguliers :**
- `pathchk /home/user/document.txt` — Vérifier si le chemin est valide sous le système courant
- `pathchk -p /home/user/Dépôt_Git/fichier.txt` — Vérifier la portabilité POSIX stricte (alerte si présence de caractères non-ASCII ou longueur > 255 caractères)
**Origine :** Spécification POSIX.1 / GNU Coreutils.
**Subtilités/confusions :**
- Ne vérifie pas si le fichier **existe**, mais uniquement si le **nom de chemin est légal et portable**.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Pratique dans des scripts d'archivage ou de création de paquets multiplateformes.
**Équivalents :** realpath, test -e
**Voir aussi :** realpath, readlink, dirname
## `realpath` — Résolution du chemin d'accès absolu canonique [Linux/macOS]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** convertir un chemin relatif (`./../dir/file.txt`) ou contenant des liens symboliques en son chemin absolu canonique unique sur le disque
**Rôle :** Utilitaire Coreutils qui résout tous les liens symboliques, les références `.` et `..` pour retourner le chemin d'accès absolu complet d'un fichier.
**Syntaxe :** `realpath [options] <chemin>`
**Cas réguliers :**
- `realpath ./config.json` — Affiche le chemin absolu complet (ex: `/home/adolphe/projet/config.json`)
- `realpath --relative-to=/var/www /var/www/html/index.html` — Calculer le chemin relatif entre deux dossiers
- `realpath -m /chemin/vers/fichier_inexistant` — Résoudre le chemin même si le fichier n'existe pas encore
**Origine :** GNU Coreutils (Padraig Brady, 2011).
**Subtilités/confusions :**
- Résout tous les niveaux de liens symboliques imbriqués pour atteindre la cible réelle finale sur le système de fichiers.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Incontournable dans les scripts Bash pour s'assurer que l'on manipule des chemins absolus non ambigus.
**Équivalents :** readlink -f, pwd -P
**Voir aussi :** readlink, dirname, basename
## `readlink` — Affichage de la cible d'un lien symbolique [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** vérifier vers quel fichier ou dossier pointe un lien symbolique (*symlink*) donné
**Rôle :** Outil CLI qui affiche la valeur textuelle enregistrée dans un lien symbolique.
**Syntaxe :** `readlink [options] <lien_symbolique>`
**Cas réguliers :**
- `readlink mon_lien` — Afficher la cible directe du lien symbolique
- `readlink -f mon_lien` — Suivre récursivement tous les liens pour afficher le chemin absolu final (équivalent à `realpath`)
**Origine :** OpenBSD / GNU Coreutils (Dmitry V. Levin, 2002).
**Subtilités/confusions :**
- Si le fichier spécifié n'est pas un lien symbolique, `readlink` sans option ne renvoie rien et sort avec le code d'erreur `1`.
- Consulter la documentation officielle pour vérifier la liste complète des options prises en charge.
**Urgences/dangers :** —
**Précautions :** Préférer `realpath` si le but est d'obtenir le chemin absolu d'un fichier quelconque (qu'il soit un lien ou non).
**Équivalents :** realpath, ls -l
**Voir aussi :** realpath, ln, ls
## `basename` — Extraction du nom de fichier pur depuis un chemin [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** isoler le nom de fichier (ex: `script.py`) en supprimant tous les répertoires d'en-tête d'un chemin complet
**Rôle :** Utilitaire Coreutils qui nettoie un chemin et ne conserve que le dernier composant (le nom du fichier).
**Syntaxe :** `basename <chemin> [suffixe_a_supprimer]`
**Cas réguliers :**
- `basename /home/user/documents/rapport.pdf` — Affiche `rapport.pdf`
- `basename /home/user/documents/rapport.pdf .pdf` — Affiche `rapport` (supprime le suffixe `.pdf`)
- `basename -s .jpg /images/*.jpg` — Traiter plusieurs fichiers en supprimant l'extension `.jpg`
**Origine :** AT&T Unix (1970s) / GNU Coreutils.
**Subtilités/confusions :**
- Outil complémentaire de `dirname` (qui conserve le répertoire et jette le nom de fichier).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Indispensable dans les boucles shell pour renommer des fichiers ou générer des noms de fichiers de sortie.
**Équivalents :** dirname (inverse), expansion de paramètre shell `${var##*/}`
**Voir aussi :** dirname, realpath
## `dirname` — Extraction du répertoire parent d'un chemin [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** obtenir le chemin du dossier contenant un fichier (ex: isoler le dossier d'un script Bash pour charger des modules relatifs)
**Rôle :** Utilitaire Coreutils qui jette le nom du fichier à la fin d'un chemin et retourne uniquement la partie dossier parent.
**Syntaxe :** `dirname <chemin>`
**Cas réguliers :**
- `dirname /home/user/documents/rapport.pdf` — Affiche `/home/user/documents`
- `DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)` — Idiome classique en Bash pour obtenir le chemin absolu du répertoire où se trouve le script exécuté !
**Origine :** AT&T Unix (1970s) / GNU Coreutils.
**Subtilités/confusions :**
- Complément direct de `basename` (qui conserve le nom du fichier et jette le dossier).
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Idéal pour s'assurer qu'un script s'exécute toujours depuis son propre répertoire quel que soit l'endroit d'où il est appelé.
**Équivalents :** realpath, expansion shell `${var%/*}`
**Voir aussi :** basename, realpath, pwd
## `getconf` — Consultation des paramètres de configuration POSIX et C [Linux/macOS]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** interroger les limites et constantes du système d'exploitation et de la bibliothèque C (taille de page mémoire, largeur de registre CPU, limites POSIX)
**Rôle :** Interface CLI d'accès aux variables système retournées par les fonctions C `sysconf()`, `pathconf()` et `confstr()`.
**Syntaxe :** `getconf <variable> [chemin]`
**Cas réguliers :**
- `getconf LONG_BIT` — Affiche `64` si le système et l'architecture sont en 64 bits (ou `32` en 32 bits)
- `getconf PAGE_SIZE` — Afficher la taille d'une page de mémoire RAM en octets (ex: 4096)
- `getconf PATH_MAX /home` — Afficher la longueur maximale autorisée pour un chemin de fichier
**Origine :** Spécification POSIX.2 / GNU C Library.
**Subtilités/confusions :**
- Permet de tester les limites physiques du système sans écrire de programme C.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser `getconf -a` pour afficher l'intégralité des variables de configuration système disponibles.
**Équivalents :** sysctl, ulimit
**Voir aussi :** sysctl, ulimit, nproc
## `printenv` — Affichage des variables d'environnement système [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** lister toutes les variables d'environnement du shell courant ou consulter la valeur exacte d'une variable spécifique
**Rôle :** Utilitaire Coreutils d'affichage des variables d'environnement actives transmis aux processus.
**Syntaxe :** `printenv [options] [variable...]`
**Cas réguliers :**
- `printenv` — Afficher toutes les variables d'environnement au format `CLÉ=VALEUR`
- `printenv PATH` — Afficher uniquement la valeur de la variable `$PATH`
- `printenv -0` — Séparer les variables par des octets nuls `\0` (utile pour traiter des valeurs contenant des retours à la ligne)
**Origine :** BSD 4.2 (1983) / GNU Coreutils.
**Subtilités/confusions :**
- `printenv` n'affiche QUE les variables exportées dans l'environnement, contrairement à `set` (qui affiche aussi les variables shell locales).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Ne pas faire un `printenv` brut dans des logs publics car il peut révéler des jetons d'API ou mots de passe présents en mémoire.
**Équivalents :** env, export, set
**Voir aussi :** env, export, direnv
## `nproc` — Affichage du nombre de processeurs disponibles [Linux]
**Niveau :** debutant | **Popularité :** 91 | **Aliases :** —
**Contextes :** déterminer le nombre de cœurs CPU accessibles pour passer l'option `-j` aux commandes de compilation (`make -j$(nproc)`, `cmake --build . -j$(nproc)`)
**Rôle :** Outil Coreutils qui affiche le nombre total de processeurs (cœurs physiques ou virtuels Hyper-Threading) disponibles pour le processus courant.
**Syntaxe :** `nproc [options]`
**Cas réguliers :**
- `nproc` — Afficher le nombre de cœurs CPU disponibles
- `nproc --ignore=1` — Afficher le nombre de cœurs moins 1 (pour réserver un cœur pour le système et ne pas tout saturer lors d'un build !)
**Origine :** GNU Coreutils (Paul Eggert, 2009).
**Subtilités/confusions :**
- Respecte les restrictions de quotas CPU appliquées aux conteneurs Docker/cgroups (contrairement à `/proc/cpuinfo` qui affiche les cœurs physiques de l'hôte).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser systématiquement `nproc` dans les scripts de build automatisés.
**Équivalents :** sysctl -n hw.ncpu (macOS), lscpu
**Voir aussi :** lscpu, make, cmake
## `stdbuf` — Contrôle de la mise en mémoire tampon des flux (buffering) [Linux/macOS]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** forcer l'affichage immédiat des sorties de commandes dans les pipelines (ex: `tail -f log | grep foo`) pour éviter que les données ne soient bloquées en tampon
**Rôle :** Outil Coreutils qui modifie la politique de mise en mémoire tampon (*buffering*) des flux STDIN, STDOUT et STDERR d'une commande sans modifier son code source.
**Syntaxe :** `stdbuf <options_tampon> <commande>`
**Cas réguliers :**
- `stdbuf -oL -eL command | grep foo` — Forcer STDOUT et STDERR en mode ligne par ligne (*line-buffered*) pour un affichage temps réel dans grep
- `stdbuf -o0 app` — Désactiver totalement le tampon sur STDOUT (mode non tamponné / *unbuffered*)
**Origine :** GNU Coreutils (Padraig Brady, 2009) — utilise `LD_PRELOAD` pour ajuster `setvbuf()`.
**Subtilités/confusions :**
- Élimine le problème classique des scripts où les données n'apparaissent dans un tuyau (`|`) qu'une fois le tampon de 4Ko rempli.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Désactiver totalement le tampon (`-o0`) peut dégrader les performances en cas d'E/S très fréquentes.
**Équivalents :** unbuffer (expect), script
**Voir aussi :** tail, grep, tee
## `tsort` — Tri topologique de graphes orientés [Linux/macOS]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** —
**Contextes :** déterminer un ordre d'exécution ou d'installation valide pour des éléments liés par des dépendances (ex: packages, tâches de build, graphes DAG)
**Rôle :** Utilitaire Coreutils qui effectue un tri topologique sur une liste de paires de dépendances orientées.
**Syntaxe :** `tsort [fichier]`
**Cas réguliers :**
- `tsort fichier_dependances.txt` — Classer les éléments dans un ordre où chaque dépendance apparaît avant l'élément qui en a besoin
- `printf "A B\nB C\n" | tsort` — Indique que A dépend de B, et B dépend de C -> sort `A`, `B`, `C` dans l'ordre d'évaluation
**Origine :** AT&T Unix (1970s) / GNU Coreutils.
**Subtilités/confusions :**
- Si le graphe contient un cycle (dépendance circulaire A -> B -> A), `tsort` affiche un avertissement de boucle.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Outil fondamental utilisé par les gestionnaires de paquets et les moteurs de compilation pour calculer l'ordre des cibles.
**Équivalents :** graphviz (visualisation), ldd
**Voir aussi :** sort, comm, make
## `chfn` — Modification des informations utilisateur (Finger) [Linux/macOS]
**Niveau :** debutant | **Popularité :** 72 | **Aliases :** —
**Contextes :** modifier le nom complet, le numéro de bureau ou le numéro de téléphone associé à un compte utilisateur dans `/etc/passwd` (champ GECOS)
**Rôle :** Commande de gestion de compte qui met à jour les informations du champ GECOS de l'utilisateur dans la base système.
**Syntaxe :** `chfn [options] [utilisateur]`
**Cas réguliers :**
- `chfn` — Lancer l'invite interactive pour mettre à jour son nom complet et coordonnées
- `chfn -f "Adolphe Chris" adolphe` — Définir le nom complet de l'utilisateur `adolphe`
**Origine :** BSD 4.0 (1980) / shadow-utils.
**Subtilités/confusions :**
- Met à jour le champ d'information de `/etc/passwd` sans altérer les droits ou le mot de passe du compte.
- L execution avec les privilèges d administration doit être restreinte au strict nécessaire.
**Urgences/dangers :** —
**Précautions :** Un utilisateur normal ne peut modifier que ses propres informations GECOS ; root peut modifier n'importe quel compte.
**Équivalents :** usermod -c, chsh
**Voir aussi :** usermod, chsh, passwd
## `taskset` — Attribution de l'affinité CPU d'un processus [Linux]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** lier l'exécution d'un processus gourmand ou critique à des cœurs CPU spécifiques (*CPU pinning*) pour optimiser le cache L3 ou éviter la contention
**Rôle :** Outil du paquet `util-linux` permettant d'extraire ou de définir le masque d'affinité processeur d'un processus en cours ou au démarrage.
**Syntaxe :** `taskset [options] [masque|liste_cpus] [commande|pid]`
**Cas réguliers :**
- `taskset -c 0,1 ./app` — Lancer l'application `app` en la restreignant EXCLUSIVEMENT aux cœurs CPU 0 et 1
- `taskset -cp 2 <pid>` — Modifier l'affinité d'un processus en cours pour le forcer sur le cœur 2
- `taskset -p <pid>` — Afficher le masque d'affinité CPU actuel d'un processus
**Origine :** Robert Love / util-linux (2002) — s'appuie sur `sched_setaffinity()`.
**Subtilités/confusions :**
- L'option `-c` accepte des listes de cœurs lisibles (`0,2,4-7`), évitant de devoir calculer des masques hexadécimaux.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** Restreindre un processus multi-thread à un seul cœur réduira drastiquement ses performances en calcul parallèle.
**Précautions :** Très utile en benchmarking pour isoler un test sur un cœur réservé et non perturbé par d'autres tâches.
**Équivalents :** numactl, chrt
**Voir aussi :** chrt, ionice, renice, nproc
## `chrt` — Modification des attributs d'ordonnancement temps réel [Linux]
**Niveau :** avance | **Popularité :** 81 | **Aliases :** —
**Contextes :** conférer des priorités d'ordonnancement temps réel (SCHED_FIFO, SCHED_RR, SCHED_DEADLINE) à des tâches critiques (traitement audio, robotique, trading)
**Rôle :** Outil de gestion des politiques et priorités d'ordonnancement du noyau Linux (`sched_setscheduler`).
**Syntaxe :** `chrt [options] [priorite] [commande|pid]`
**Cas réguliers :**
- `chrt -f -p 99 <pid>` — Assigner la politique Temps Réel FIFO (`SCHED_FIFO`) avec la priorité maximale (99) à un processus
- `chrt -r -p 50 <pid>` — Assigner la politique Temps Réel Round-Robin (`SCHED_RR`) avec la priorité 50
- `chrt -p <pid>` — Afficher la politique et la priorité d'ordonnancement actuelles d'un processus
**Origine :** Robert Love / util-linux (2002).
**Subtilités/confusions :**
- Un processus en `SCHED_FIFO` de priorité élevée préempte TOUS les processus normaux du système tant qu'il a du travail à effectuer !
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** ⚠️ Une boucle infinie dans un processus Temps Réel `SCHED_FIFO` peut figer complètement le système Linux.
**Précautions :** Nécessite les privilèges root ou la capacité `CAP_SYS_NICE`.
**Équivalents :** renice, taskset, ionice
**Voir aussi :** renice, taskset, ionice, top
## `ionice` — Modification de la classe et de la priorité d'E/S disque [Linux]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** réduire l'impact sur le disque dur/SSD de tâches de fond lourdes (sauvegardes, indexation) pour ne pas ralentir les applications utilisateur
**Rôle :** Outil de gestion des priorités d'E/S (Input/Output) pour l'ordonnanceur de disque du noyau Linux (BFQ/Kyber).
**Syntaxe :** `ionice -c <classe> [-n <priorite>] [-p pid | commande]`
**Cas réguliers :**
- `ionice -c 3 tar -czf backup.tar.gz /data` — Exécuter une sauvegarde en classe *Idle* (3) : elle n'utilise le disque QUE si aucun autre processus ne le sollicite !
- `ionice -c 2 -n 0 -p <pid>` — Accorder la priorité d'E/S maximale de la classe *Best-Effort* à un processus
**Origine :** Jens Axboe / util-linux (2005).
**Subtilités/confusions :**
- Les 3 classes sont : `1` (Realtime), `2` (Best-effort, défaut), `3` (Idle).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser systématiquement `ionice -c 3` sur vos scripts de sauvegarde cron ou d'indexation nocturne.
**Équivalents :** renice, taskset, chrt
**Voir aussi :** renice, taskset, nice
## `renice` — Modification de la priorité d'exécution d'un processus actif [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** réduire la priorité CPU d'un processus en cours d'exécution qui consomme trop de ressources, ou accélérer un traitement urgent
**Rôle :** Outil d'ajustement dynamique de la valeur *nice* (-20 à +19) d'un ou plusieurs processus déjà lancés.
**Syntaxe :** `renice [-n] <valeur_nice> -p <pid>`
**Cas réguliers :**
- `renice -n 19 -p 1234` — Baisser la priorité du processus 1234 au minimum (19 = très poli avec les autres)
- `renice -n -10 -p 1234` — Augmenter la priorité du processus 1234 (-10 = très prioritaire, nécessite root !)
- `renice -n 10 -u adolphe` — Modifier la priorité de TOUS les processus appartenant à l'utilisateur `adolphe`
**Origine :** BSD 4.0 (1980) / util-linux.
**Subtilités/confusions :**
- Les utilisateurs normaux ne peuvent qu'**augmenter** la valeur nice (réduire leur priorité) ; seul root peut **diminuer** la valeur nice sous 0.
- L execution avec les privilèges d administration doit être restreinte au strict nécessaire.
**Urgences/dangers :** —
**Précautions :** -20 est la priorité la plus élevée ; +19 est la priorité la plus basse.
**Équivalents :** nice, ionice, chrt
**Voir aussi :** top, htop, ionice, taskset
## `killall` — Envoi de signaux à tous les processus portant un nom [Linux/macOS]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** arrêter rapidement toutes les instances d'une application (ex: tous les processus `firefox` ou `nginx`) sans chercher leurs PIDs individuels
**Rôle :** Outil qui envoie un signal (SIGTERM par défaut) à tous les processus correspondant au nom d'exécutable exact spécifié.
**Syntaxe :** `killall [options] [nom_processus]`
**Cas réguliers :**
- `killall nginx` — Arrêter proprement toutes les instances du serveur Nginx (SIGTERM)
- `killall -9 python3` — Tuer violemment toutes les instances Python (`SIGKILL` / `-9`)
- `killall -u adolphe` — Tuer tous les processus appartenant à l'utilisateur `adolphe`
**Origine :** System V / Pkill package / psmisc.
**Subtilités/confusions :**
- Sous Solaris/Unix System V historique, `killall` tuait TOUS les processus du système ! Sous Linux (psmisc), il ne tue que ceux portant le nom spécifié.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** ⚠️ `killall -9` empêche les processus d'exécuter leurs routines de nettoyage (risque de corruption de fichiers/bases).
**Précautions :** Préférer `killall` sans `-9` en premier lieu pour laisser une chance au processus de s'arrêter proprement.
**Équivalents :** pkill, pidof, kill
**Voir aussi :** pkill, pgrep, pidof
## `pkill` — Envoi de signaux aux processus selon des motifs regex [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** cibler et envoyer un signal à des processus en utilisant une correspondance par expression régulière sur leur nom ou ligne de commande complète
**Rôle :** Outil de recherche et d'arrêt de processus basé sur des motifs regex et des attributs de processus (utilisateur, terminal, groupe).
**Syntaxe :** `pkill [options] <motif_regex>`
**Cas réguliers :**
- `pkill -f "node server.js"` — Tuer le processus correspondant au motif sur la ligne de commande complète (`-f`)
- `pkill -HUP syslogd` — Envoyer le signal `SIGHUP` à syslogd pour lui faire recharger sa configuration
- `pkill -u www-data` — Tuer tous les processus de l'utilisateur `www-data`
**Origine :** Solaris 7 (1998) / procps-ng.
**Subtilités/confusions :**
- Diffère de `killall` qui exige le nom binaire exact : `pkill` utilise des expressions régulières et supporte la recherche sur la ligne de commande complète (`-f`).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Exécuter d'abord `pgrep -l <motif>` pour vérifier quels processus correspondent au motif avant de lancer `pkill` !
**Équivalents :** pgrep, killall, kill
**Voir aussi :** pgrep, killall, pidof
## `pgrep` — Recherche de processus par motif et critères [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** trouver les PIDs des processus correspondant à un nom ou une ligne de commande pour les utiliser dans un script Bash
**Rôle :** Outil de recherche de processus qui retourne les PIDs des processus correspondant aux critères spécifiés.
**Syntaxe :** `pgrep [options] <motif_regex>`
**Cas réguliers :**
- `pgrep nginx` — Afficher les PIDs de toutes les instances Nginx
- `pgrep -l -f "python"` — Afficher les PIDs ET le nom complet de la ligne de commande de tous les processus contenant "python"
- `pgrep -u root sshd` — Lister les PIDs des processus `sshd` appartenant à `root`
**Origine :** Solaris 7 (1998) / procps-ng.
**Subtilités/confusions :**
- Évite l'idiome lourd et bancal `ps aux | grep node | grep -v grep`.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser `-l` pour afficher le nom du processus à côté du PID pour lever toute ambiguïté.
**Équivalents :** pidof, ps, pkill
**Voir aussi :** pkill, pidof, ps
## `pidof` — Recherche du PID exact d'un programme en cours [Linux/macOS]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** —
**Contextes :** récupérer rapidement le PID numérique exact d'un démon système (ex: `pidof systemd` ou `pidof mysqld`) dans des scripts d'administration
**Rôle :** Outil léger qui retourne le ou les PIDs des programmes exécutables correspondant au nom exact donné.
**Syntaxe :** `pidof [options] <nom_programme>`
**Cas réguliers :**
- `pidof nginx` — Afficher la liste des PIDs de Nginx séparés par des espaces (ex: `1234 1235 1236`)
- `pidof -s nginx` — Retourner uniquement le premier PID trouvé (Single shot)
- `kill -9 $(pidof mon_app)` — Tuer rapidement l'application en combinant `kill` et `pidof`
**Origine :** System V / procps-ng / SysVinit.
**Subtilités/confusions :**
- Ne prend pas en charge les expressions régulières : exige le nom exact du fichier binaire exécutable.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Si le programme n'est pas en cours d'exécution, `pidof` ne renvoie rien et sort avec le code de retour `1`.
**Équivalents :** pgrep, ps
**Voir aussi :** pgrep, pkill, killall
## `lsattr` — Affichage des attributs étendus de fichiers [Linux]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** vérifier si un fichier est marqué comme immuable (`i`), en écriture seule / append-only (`a`), ou crypté sur un système de fichiers ext2/ext3/ext4
**Rôle :** Outil du paquet `e2fsprogs` qui liste les attributs de niveau système de fichiers associés à des fichiers sous Linux.
**Syntaxe :** `lsattr [options] [fichier...]`
**Cas réguliers :**
- `lsattr /etc/shadow` — Afficher les attributs étendus du fichier d'authentification
- `lsattr -R /var/log` — Afficher les attributs récursivement dans les sous-dossiers
- `lsattr -d /etc` — Afficher les attributs du répertoire lui-même (et non de son contenu)
**Origine :** Remy Card / e2fsprogs (1993).
**Subtilités/confusions :**
- Les attributs `lsattr` sont distincts des permissions standard Unix (`chmod`) et des ACLs (`getfacl`).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Si un fichier ne peut pas être supprimé même par root (`Operation not permitted`), faire un `lsattr` pour vérifier si le drapeau `i` (immuable) est posé.
**Équivalents :** chattr, getfacl
**Voir aussi :** chattr, getfacl, stat
## `filefrag` — Diagnostic de fragmentation d'un fichier sur disque [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** vérifier en combien d'étendues / fragments disjoints (*extents*) un fichier massif ou une image de VM est découpé sur le stockage physique
**Rôle :** Utilitaire du paquet `e2fsprogs` qui interroge le système de fichiers pour rapporter le niveau de fragmentation des blocs d'un fichier.
**Syntaxe :** `filefrag [options] <fichier>`
**Cas réguliers :**
- `filefrag vm_disk.qcow2` — Affiche par exemple : `vm_disk.qcow2: 3 extents found`
- `filefrag -v image.iso` — Afficher la carte détaillée bloc par bloc des étendues physiques sur le disque
**Origine :** Theodore Ts'o / e2fsprogs (2003).
**Subtilités/confusions :**
- Les systèmes de fichiers Linux modernes (ext4, Btrfs, XFS) gèrent la fragmentation très efficacement, mais un nombre d'étendues très élevé (> 1000) peut ralentir les accès E/S séquentiels.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Utiliser `e4defrag` sur ext4 si un binaire critique présente un niveau de fragmentation excessif.
**Équivalents :** e4defrag, hdparm
**Voir aussi :** stat, lsattr, fallocate
## `getfacl` — Consultation des listes de contrôle d'accès (ACL) POSIX [Linux]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** —
**Contextes :** vérifier les autorisations fines d'un fichier lorsqu'un utilisateur spécifique a des droits d'accès non visibles via les droits standard `chmod` (`ls -l`)
**Rôle :** Outil de lecture des listes d'accès ACL POSIX permettant d'attribuer des droits distincts à plusieurs utilisateurs ou groupes sur un même fichier.
**Syntaxe :** `getfacl [options] <fichier_ou_dossier>`
**Cas réguliers :**
- `getfacl document.pdf` — Afficher l'ensemble des propriétaires, groupes et règles ACL spécifiques appliquées au fichier
- `getfacl -R /data` — Afficher les ACLs récursivement sur tout un dossier
- `getfacl file1.txt | setfacl --set-file=- file2.txt` — Copier à l'identique la configuration ACL de `file1` sur `file2` !
**Origine :** Spécification POSIX 1003.1e / paquet `acl` Linux.
**Subtilités/confusions :**
- Lorsqu'un fichier possède des ACLs étendues sous Linux, la commande `ls -l` affiche un petit signe plus `+` à la fin des permissions (`-rw-r--r--+`).
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Toujours vérifier `getfacl` si un accès utilisateur est refusé alors que `chmod` semble correct.
**Équivalents :** setfacl, ls -l
**Voir aussi :** setfacl, chmod, lsattr
## `setfacl` — Configuration des listes de contrôle d'accès POSIX (ACL) [Linux]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** accorder des droits de lecture/écriture sur un fichier ou dossier à un utilisateur spécifique sans le rendre propriétaire ni modifier le groupe principal du fichier
**Rôle :** Outil de modification des règles ACL POSIX autorisant une gestion granulaire des droits d'accès.
**Syntaxe :** `setfacl [options] [règles] <fichier_ou_dossier>`
**Cas réguliers :**
- `setfacl -m u:adolphe:rw document.pdf` — Accorder les droits de lecture/écriture (`rw`) à l'utilisateur `adolphe` sur `document.pdf`
- `setfacl -m d:g:devs:rwx /shared` — Définir des ACLs par défaut (`d:`) pour que tout nouveau fichier créé dans `/shared` appartienne au groupe `devs` en `rwx` !
- `setfacl -x u:adolphe document.pdf` — Retirer la règle ACL spécifique de l'utilisateur `adolphe`
**Origine :** Paquet `acl` Linux (Andreas Gruenbacher, 2002).
**Subtilités/confusions :**
- Les ACLs par défaut (`-m d:...`) s'appliquent uniquement aux répertoires et sont héritées par les nouveaux sous-dossiers et fichiers créés à l'intérieur.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** Des ACLs mal configurées peuvent contourner l'isolation de sécurité standard du système.
**Précautions :** Utiliser `setfacl -b fichier` pour supprimer TOUTES les ACLs étendues et revenir aux permissions POSIX standard.
**Équivalents :** getfacl, chmod, chown
**Voir aussi :** getfacl, chmod, chown
## `getcap` — Inspection des capacités noyau attribuées aux binaires [Linux]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** auditer la sécurité du système pour identifier quels executables disposent de privilèges noyau spécifiques (*Capabilities*) sans être lancés avec le SUID root
**Rôle :** Outil de lecture des capacités du noyau Linux (`libcap`) attribuées à des fichiers exécutables.
**Syntaxe :** `getcap [options] <fichier...>`
**Cas réguliers :**
- `getcap /usr/bin/ping` — Affiche `cap_net_raw+ep` (permet à ping d'envoyer des paquets ICMP bruts sans tourner en root !)
- `getcap -r / 2>/dev/null` — Scanner récursivement tout le système de fichiers pour lister tous les binaires possédant des capacités noyau
**Origine :** Andrew G. Morgan / paquet `libcap` (1997) — sous-système de sécurité POSIX Capabilities du noyau Linux.
**Subtilités/confusions :**
- Les capacités Linux découpent le pouvoir absolu de `root` en ~40 privilèges granulaires (`CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`, `CAP_NET_RAW`…).
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Auditer régulièrement les capacités pour détecter d'éventuelles élévations de privilèges non autorisées (*privilege escalation*).
**Équivalents :** setcap, ls -l (SUID check)
**Voir aussi :** setcap, chmod, sudo
## `setcap` — Attribution de capacités noyau à des binaires [Linux]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** autoriser un serveur web (ex: Nginx ou un binaire Go) à se lier sur le port 80/443 sans devoir l'exécuter en tant qu'utilisateur root !
**Rôle :** Outil d'attribution des capacités du noyau Linux (`libcap`) aux en-têtes d'un fichier exécutable.
**Syntaxe :** `setcap <capacite> <fichier>`
**Cas réguliers :**
- `setcap 'cap_net_bind_service=+ep' /usr/local/bin/mon_app` — Autoriser `mon_app` à écouter sur des ports réservés (< 1024) sans privilèges root !
- `setcap -r /usr/local/bin/mon_app` — Retirer toutes les capacités attribuées au binaire
**Origine :** Paquet `libcap` (Andrew G. Morgan, 1997).
**Subtilités/confusions :**
- Le drapeau `+ep` signifie **Effective** et **Permitted** (rend la capacité immédiatement active à l'exécution).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** ⚠️ Attribuer `cap_sys_admin` à un binaire non sécurisé équivaut pratiquement à lui donner les droits root complets.
**Précautions :** Préférer toujours `setcap` à l'utilisation du bit SUID (`chmod u+s`) car la portée des privilèges est strictement limitée.
**Équivalents :** getcap, chmod u+s
**Voir aussi :** getcap, chmod, sudo
## `vmstat` — Statistiques globales de mémoire virtuelle et processeur [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** diagnostiquer un ralentissement système global, identifier des goulots d'étranglement en swap, mémoire vive, interruptions E/S ou CPU
**Rôle :** Outil de surveillance en temps réel de la suite `procps` qui affiche un rapport compact des processus, de la mémoire, du pagination swap, des E/S et de l'activité CPU.
**Syntaxe :** `vmstat [options] [intervalle] [nombre_itérations]`
**Cas réguliers :**
- `vmstat 2` — Afficher une ligne récapitulative de l'état système toutes les 2 secondes en continu
- `vmstat -s` — Afficher une table d'événements mémoire et statistiques cumulées depuis le démarrage
- `vmstat -d` — Afficher des statistiques détaillées d'activité disque
**Origine :** BSD 3.0 / procps-ng (Henry Ware, 1991).
**Subtilités/confusions :**
- La première ligne affichée par `vmstat` est TOUJOURS la moyenne depuis le démarrage du système ; les lignes suivantes affichent les deltas de l'intervalle.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Surveiller les colonnes `si` (swap in) et `so` (swap out) : si elles sont élevées non nulles, le système manque cruellement de RAM.
**Équivalents :** free, iostat, mpstat, top
**Voir aussi :** free, iostat, mpstat, sar
## `iostat` — Statistiques d'entrée/sortie disque et sous-systèmes E/S [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** identifier quel disque dur ou SSD est saturé (temps d'attente E/S élevé, `%util` proche de 100%), mesurer les débits de lecture/écriture MB/s
**Rôle :** Outil du paquet `sysstat` qui surveille les débits et temps d'accès E/S des périphériques de stockage bloc.
**Syntaxe :** `iostat [options] [intervalle] [nombre_itérations]`
**Cas réguliers :**
- `iostat -xz 2` — Afficher les statistiques E/S étendues (`-x`) de tous les disques actifs (`-z`) toutes les 2 secondes
- `iostat -d -m 1` — Afficher les débits E/S uniquement en Mégaoctets par seconde (MB/s)
**Origine :** System V / paquet `sysstat` (Sebastien Godard, 1999).
**Subtilités/confusions :**
- La métrique `%util` indique le pourcentage de temps pendant lequel le disque a eu des requêtes E/S en cours (une valeur > 90% indique une saturation du disque).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Utiliser avec l'option `-x` pour obtenir les métriques de latence d'attente (`await`) indispensables au diagnostic de bases de données lentes.
**Équivalents :** iotop, vmstat, sar
**Voir aussi :** vmstat, mpstat, sar, pidstat
## `mpstat` — Statistiques d'utilisation processeur par cœur CPU [Linux]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** vérifier la répartition de la charge CPU sur un serveur multi-cœurs (ex: détecter si un seul cœur est saturé à 100% par une application mono-thread)
**Rôle :** Outil du paquet `sysstat` qui affiche l'utilisation processeur globale ou détaillée cœur par cœur (utilisateur, système, iowait, irq, idle).
**Syntaxe :** `mpstat [options] [intervalle] [nombre_itérations]`
**Cas réguliers :**
- `mpstat -P ALL 2` — Afficher l'état d'utilisation de TOUS les cœurs CPU individuels toutes les 2 secondes
- `mpstat 1` — Afficher la moyenne globale de tous les cœurs CPU chaque seconde
**Origine :** Solaris / paquet `sysstat` (Sebastien Godard, 1999).
**Subtilités/confusions :**
- `%iowait` indique le pourcentage de temps CPU perdu à attendre la réponse d'un composant de stockage (disque).
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Pratique pour vérifier si vos tâches parallèles exploitent correctement l'ensemble des cœurs CPU disponibles (`nproc`).
**Équivalents :** htop, lscpu, vmstat
**Voir aussi :** vmstat, iostat, sar, nproc
## `pidstat` — Statistiques de ressources filtrées par processus [Linux]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** identifier précisément quel processus consomme le plus d'E/S disque, de RAM ou génère des fautes de page (*page faults*) en temps réel
**Rôle :** Outil du paquet `sysstat` qui surveille la consommation individuelle de ressources (CPU, mémoire, I/O, changement de contexte) de chaque processus actif.
**Syntaxe :** `pidstat [options] [intervalle] [nombre_itérations]`
**Cas réguliers :**
- `pidstat 2` — Afficher la consommation CPU de tous les processus actifs toutes les 2 secondes
- `pidstat -d 1` — Afficher les débits de lecture et d'écriture disque de chaque processus chaque seconde !
- `pidstat -r -p <pid> 2` — Surveiller l'utilisation mémoire et les fautes de page d'un processus spécifique
**Origine :** Paquet `sysstat` (Sebastien Godard, 2007).
**Subtilités/confusions :**
- Contrairement à `top` qui rafraîchit tout l'écran, `pidstat` affiche une séquence d'historique en défilement continu idéal pour les logs d'analyse.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Inestimable pour débusquer un processus d'arrière-plan qui effectue des écritures disque masquées destructrices de performances.
**Équivalents :** top, htop, iotop
**Voir aussi :** iostat, vmstat, mpstat, sar
## `sar` — Collecteur et rapporteur d'activité système historique [Linux]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** —
**Contextes :** analyser a posteriori les performances du système lors d'une panne survenue la nuit dernière (charge CPU, RAM, trafic réseau, E/S disque)
**Rôle :** Le « couteau suisse » ultime de la suite `sysstat` qui enregistre en continu l'ensemble des compteurs de performance du système et génère des rapports historiques.
**Syntaxe :** `sar [options] [intervalle|fichier_archive]`
**Cas réguliers :**
- `sar -u 2 5` — Surveiller l'activité CPU en direct pendant 5 itérations de 2 secondes
- `sar -q -f /var/log/sysstat/sa15` — Analyser la charge moyenne du système le 15 du mois à partir des archives sysstat !
- `sar -n DEV` — Afficher les statistiques historiques du trafic sur les cartes réseau
**Origine :** System V / paquet `sysstat` (Sebastien Godard, 1999).
**Subtilités/confusions :**
- Nécessite d'activer le service `sysstat` (`systemctl enable --now sysstat`) pour qu'il enregistre les métriques en arrière-plan chaque minute.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Indispensable lors de l'investigation d'incidents (post-mortem) pour savoir exactement ce qui s'est passé à une heure précise.
**Équivalents :** vmstat, iostat, dstat
**Voir aussi :** vmstat, iostat, mpstat, pidstat
## `numactl` — Contrôle des politiques mémoire et CPU sur architectures NUMA [Linux]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** optimiser les accès mémoire sur les serveurs biprocesseurs (NUMA) pour s'assurer qu'un processus tourne sur le socket CPU directement relié à sa banque de RAM
**Rôle :** Outil de contrôle des politiques de placement de mémoire et d'exécutions CPU pour les architectures NUMA (*Non-Uniform Memory Access*).
**Syntaxe :** `numactl [options] <commande>`
**Cas réguliers :**
- `numactl --hardware` — Afficher la topologie NUMA du serveur (nœuds, processeurs associés et distances d'accès mémoire)
- `numactl --cpunodebind=0 --membind=0 postgresql` — Lancer PostgreSQL en le confinant sur le nœud NUMA 0 (CPU et RAM locaux)
- `numactl --interleave=all ./app` — Répartir les allocations mémoire de manière uniforme sur tous les nœuds NUMA
**Origine :** Andi Kleen / SuSE (2003) — paquet `numactl`.
**Subtilités/confusions :**
- Évite les pénalités de latence mémoire (jusqu'à 30% de ralentissement) dues aux traversées du bus inter-socket (QPI/UPI/Infinity Fabric).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Recommandé pour les bases de données haute performance (PostgreSQL, MySQL, Redis, Oracle) hébergées sur de gros serveurs bi-sockets.
**Équivalents :** taskset, lscpu
**Voir aussi :** taskset, lscpu, nproc
## `ldd` — Affichage des bibliothèques partagées dynamiques requises [Linux]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** diagnostiquer l'erreur classique `error while loading shared libraries`, ou lister toutes les dépendances `.so` requises par un binaire ELF
**Rôle :** Outil du chargeur dynamique (glibc) qui liste les bibliothèques partagées nécessaires à l'exécution d'un binaire et leur chemin de résolution sur le système.
**Syntaxe :** `ldd [options] <binaire_ou_so>`
**Cas réguliers :**
- `ldd /bin/ls` — Afficher toutes les bibliothèques partagées dynamiques requises par le binaire `ls`
- `ldd -u /bin/ls` — Afficher les bibliothèques dépendantes inutilisées (*unused direct dependencies*)
**Origine :** GNU C Library / SunOS.
**Subtilités/confusions :**
- Si une bibliothèque est manquante, `ldd` affiche `not found` en face de son nom.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** ⚠️ Ne jamais exécuter `ldd` sur un binaire binaire provenant d'une source non fiable (certaines implémentations de l'outil exécutent partiellement le code pour résoudre les dépendances !). Utiliser `objdump -p` ou `readelf -d` sur des binaires suspects.
**Précautions :** Pratique lors de la création d'images Docker minimalistes (*distroless* ou *chroot*) pour copier exactement les bibliothèques requises.
**Équivalents :** objdump -p, readelf -d, otool -L (macOS)
**Voir aussi :** readelf, objdump, gcc
## `readelf` — Inspection de la structure des fichiers binaires ELF [Linux]
**Niveau :** avance | **Popularité :** 88 | **Aliases :** —
**Contextes :** analyser la structure interne d'un fichier binaire binaire ELF (en-têtes, sections, symboles, dépendances) sans dépendre du chargeur dynamique
**Rôle :** Outil de la suite GNU Binutils d'analyse approfondie de fichiers au format binaire standard sous Linux (ELF / Executable and Linkable Format).
**Syntaxe :** `readelf <options> <binaire_elf>`
**Cas réguliers :**
- `readelf -h /bin/ls` — Afficher l'en-tête ELF principal (architecture CPU, type binaire, point d'entrée mémoire)
- `readelf -d /bin/ls` — Afficher la section dynamique et la liste des bibliothèques dépendantes (remplacement ultra-sûr de `ldd` !)
- `readelf -s /bin/ls` — Lister la table des symboles exportés et importés par le binaire
**Origine :** Nick Clifton / GNU Binutils (1999).
**Subtilités/confusions :**
- N'exécute JAMAIS le binaire analysé, ce qui en fait l'outil d'analyse statique et de reverse engineering le plus sûr de Linux.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Idéal pour vérifier si un binaire est compilé en mode position-indépendante (`PIE`) pour des raisons de sécurité.
**Équivalents :** objdump, ldd, nm
**Voir aussi :** ldd, nm, gcc, file
## `nm` — Liste des symboles des fichiers binaires et objets [Linux/macOS]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** diagnostiquer des erreurs d'édition de liens (*undefined reference to...*), vérifier si une fonction ou variable globale est présente dans une bibliothèque `.a` ou `.so`
**Rôle :** Outil GNU Binutils qui liste la table des symboles (noms de fonctions, variables globales) contenus dans un fichier binaire binaire ou fichier objet `.o`.
**Syntaxe :** `nm [options] <fichier_binaire_ou_objet>`
**Cas réguliers :**
- `nm -C libmoncode.so` — Lister et décoder (*demangle*) les noms de symboles C++ pour les rendre lisibles sous forme de fonctions C++
- `nm -u app` — Afficher uniquement les symboles non définis (`undefined`), c'est-à-dire importés depuis d'autres bibliothèques
- `nm -g app` — Lister uniquement les symboles externes / globaux
**Origine :** AT&T Unix (1970s) / GNU Binutils.
**Subtilités/confusions :**
- L'option `-C` (`--demangle`) est essentielle pour du C++ afin de convertir les noms internes mutilés (ex: `_Z3fooi`) en signatures de fonctions lisibles (ex: `foo(int)`).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Si un binaire a été dépouillé de ses symboles (`strip`), `nm` affichera `no symbols`.
**Équivalents :** readelf -s, objdump -t
**Voir aussi :** readelf, gcc, g++