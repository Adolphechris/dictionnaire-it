# Face A — Commandes : AIDE, SHELL ET OUTILLAGE (fiches riches v3)

> Lot MVP #022 — **40/40 fiches ✅ TERMINÉ** (validé par `tools/parse_rich.py`, 40 fiches v3 conformes). Format : `## \`commande\` — titre [OS]` + 10 rubriques obligatoires.

## `man` — Manuel de référence d'une commande [Linux/macOS]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** manual
**Contextes :** interrogation d'options, apprentissage d'une commande, vérification d'un comportement avant action
**Rôle :** Afficher le manuel officiel d'une commande (sections 1 à 9 : commandes, appels système, formats...).
**Syntaxe :** `man [section] <commande>`
**Cas réguliers :**
- `man ls` — Manuel complet de ls (le plus courant)
- `man 5 passwd` — Section 5 : format du fichier /etc/passwd
- `man -k chmod` — Chercher dans les résumés (équivalent de apropos)
- `/mot` puis `n` — Rechercher dans le manuel puis résultat suivant (navigation vi)
**Origine :** Unix V1 (1971), écrit par Ken Thompson et Dennis Ritchie — le manuel d'UNIX a d'abord été un document papier imprimé ; les pages man en sont la transposition en ligne.
**Subtilités/confusions :**
- Sections utiles : 1 = commande, 5 = format de fichier, 8 = admin système — `man passwd` peut renvoyer la section 8 par défaut.
- La navigation interne utilise les touches de `vi` (/, n, q) — `q` pour quitter, piège des débutants.
- man n'affiche pas tout : `--help` résume, `info` détaille (GNU), les exemples sont souvent dans les autres sections.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Vérifier la section avant d'appliquer une option lue — les options varient entre versions.
**Équivalents :** --help (résumé), apropos (recherche), Get-Help (PowerShell)
**Voir aussi :** apropos, whatis, info, --help

## `--help` — Aide rapide en ligne de commande [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** -h, /?, help
**Contextes :** rappel de syntaxe en urgence, découverte des options, vérification d'un flag exact
**Rôle :** Afficher le résumé des options d'une commande — l'aide la plus rapide, toujours disponible.
**Syntaxe :** `<commande> --help` (ou `-h`, `/?` sous Windows CMD)
**Cas réguliers :**
- `ls --help` — Toutes les options de ls en 1 écran (le plus courant)
- `tar --help` — Vérifier le nom exact d'un flag avant une archivage critique
- `docker run --help` — Sous-commandes incluses
- `commande -h` — Version courte (souvent identique)
**Origine :** Convention GNU (années 1980) avec `--long-options` et traits d'union doubles ; la norme de facto aujourd'hui, même hors Unix (derniers outils Windows inclus).
**Subtilités/confusions :**
- `--help` ≠ `man` : l'aide est un résumé opérationnel, le manuel explique en profondeur (section, exemples, bugs connus).
- Certaines commandes interprètent `-h` autrement (gzip -h = historique… non, help ; mais `ssh -h` n'existe pas, c'est man ssh).
- `commande --help 2>&1 | less` si la sortie défile trop vite.
**Urgences/dangers :** — (lecture seule ; ATTENTION : `commande --help` sans rien après sur certains outils attend une entrée… rare)
**Précautions :** En cas de doute sur un flag destructeur, lire le man AVANT (ex. `rm --help` ne dit pas que -rf est dangereux).
**Équivalents :** man, help (PowerShell), /? (CMD)
**Voir aussi :** man, apropos, help

## `which` — Localiser un exécutable dans le PATH [Linux/macOS]
**Niveau :** debutant | **Popularité :** 78 | **Aliases :** where (CMD)
**Contextes :** debug "commande introuvable", vérification de la version utilisée, conflits de PATH
**Rôle :** Indiquer le chemin complet du binaire qui sera exécuté pour un nom de commande.
**Syntaxe :** `which <commande>`
**Cas réguliers :**
- `which python` — → /usr/bin/python ou un venv ? (le plus courant)
- `which -a git` — Afficher TOUTES les occurrences dans le PATH
- `which node` — Vérifier que nvm pointe bien vers la bonne version
**Origine :** BSD/Unix historique (déjà dans 4.3BSD, 1986) — remplacé côté GNU par `command -v` plus portable.
**Subtilités/confusions :**
- which vs type : `which` donne le CHEMIN, `type` explique le TYPE (binaire, alias, fonction) — en bash préférer `type -a`.
- which ne voit PAS les alias/fonctions du shell — `type` les trouve.
- En scripts, `command -v` est le portable (POSIX) : which n'est pas garanti partout.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Résoudre les PATH ambigus avant les scripts de prod (python2/python3 !).
**Équivalents :** command -v (POSIX), type (bash), Get-Command (PowerShell), where (CMD)
**Voir aussi :** type, command, PATH, env

## `type` — Dire ce qu'est un nom de commande [Linux/macOS]
**Niveau :** debutant | **Popularité :** 70 | **Aliases :** —
**Contextes :** débogage d'alias, comprendre pourquoi une commande "ne répond pas comme prévu", shell bash/zsh
**Rôle :** Afficher si un nom est un binaire, un alias, une fonction shell, un mot-clé ou un emplacement PATH.
**Syntaxe :** `type <commande>`
**Cas réguliers :**
- `type ls` — → « ls est alias à 'ls --color=auto' » (le plus courant : l'énigme de l'alias)
- `type -a git` — Toutes les définitions dans l'ordre de résolution
- `type cd` — → « cd est un mot-clé (builtin) »
**Origine :** Posix / shells Bourne (1979) — conçu pour rendre le mécanisme de résolution des commandes transparent à l'utilisateur.
**Subtilités/confusions :**
- L'alias est résolu AVANT le binaire : `type git` peut montrer un alias alors que tu penses appeler le binaire réel.
- `type` ne marche que dans les shells interactifs supportant les alias (bash, zsh) — pas un programme externe.
- `type -t` donne seulement le type (file, alias, keyword...) — utile dans les scripts bash.
**Urgences/dangers :** — (lecture seule)
**Précautions :** En cas de comportement surprenant d'une commande : `type commande` AVANT de réinstaller.
**Équivalents :** which, command -v, Get-Command (PowerShell)
**Voir aussi :** which, alias, command, PATH

## `history` — Historique des commandes tapées [Linux/macOS]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** —
**Contextes :** retrouver une commande oubliée, rejouer une manipulation, auditer ce qui a été fait
**Rôle :** Lister les commandes de la session et des sessions précédentes, avec leur numéro.
**Syntaxe :** `history [n]` / `!<numéro>`
**Cas réguliers :**
- `history | grep docker` — Retrouver la commande docker exacte (le plus courant)
- `!42` — Rejouer la commande n°42
- `!!` — Rejouer la dernière commande (souvent `sudo !!`)
- `history -d 100` — Supprimer la ligne 100 (nettoyage sensible)
**Origine :** Bourne Shell (1979) dès Unix V7 — persistance dans `~/.bash_history` ; `HISTSIZE` et `HISTCONTROL` règlent le comportement.
**Subtilités/confusions :**
- Commandes avec secrets tapés = historisées par défaut → `HISTCONTROL=ignoreboth`.
- `!!` reconstruit la commande EXACTE — vérifier avant de relancer sous sudo.
- Chaque shell a SON historique, flushé à la fermeture — deux sessions = deux fichiers en attente.
**Urgences/dangers :** ⚠️ `~/.bash_history` peut contenir des tokens — ne jamais le partager tel quel.
**Précautions :** Supprimer les lignes sensibles ; rotation du fichier ; `history -c` en cas de fuite avérée.
**Équivalents :** Get-History (PowerShell), Ctrl+R (recherche interactive)
**Voir aussi :** alias, source, HISTCONTROL, shell

## `alias` — Raccourci de commande personnalisé [Linux/macOS]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** unalias (suppression)
**Contextes :** éviter les options longues, protéger contre les coquilles (rm -i), personnaliser le shell
**Rôle :** Définir un raccourci nommé pour une commande (session locale ou fichier de config).
**Syntaxe :** `alias <nom>='<commande>'` / `unalias <nom>`
**Cas réguliers :**
- `alias ll='ls -la'` — Raccourci de listing (le plus courant)
- `alias gs='git status'` — Réflexe git quotidien
- `alias rm='rm -i'` — Sécuriser une commande destructive
- `unalias ll` — Supprimer un alias
**Origine :** Csh (Bill Joy, 1978) puis repris par Bourne/bash — standardisé POSIX pour le shell interactif.
**Subtilités/confusions :**
- Un alias n'existe PAS dans les scripts (`#!/bin/bash`) : utiliser une fonction shell.
- L'alias est résolu AVANT le binaire — diagnostiquer avec `type grep`.
- `alias` sans argument liste les aliases actifs — utile pour auditer sa config.
**Urgences/dangers :** ⚠️ Un alias destructeur masqué dans `.bashrc` (ex. rm surchargé) déroute lors des incidents — garder les aliases simples.
**Précautions :** Définir dans `~/.bashrc` (interactif seulement) ; documenter les aliases d'équipe.
**Équivalents :** fonction shell, Set-Alias (PowerShell), doskey (CMD)
**Voir aussi :** type, history, source, shell

## `export` — Variable propagée aux sous-processus [Linux/macOS]
**Niveau :** debutant | **Popularité :** 80 | **Aliases :** —
**Contextes :** variables d'environnement, configuration d'outils (JAVA_HOME, PATH), secrets temporaires
**Rôle :** Créer ou modifier une variable et la PROPAGER aux commandes lancées ensuite (enfants du shell).
**Syntaxe :** `export VAR=valeur` / `export -p`
**Cas réguliers :**
- `export PATH="$PATH:/mon/chemin"` — Ajouter au PATH (le plus courant)
- `export JAVA_HOME=/usr/lib/jvm/java-17` — Variable de config d'outil
- `export VAR && ./script.sh` — script.sh voit VAR
- `export -n VAR` — Ne plus exporter une variable
**Origine :** Bourne Shell (1979) — la distinction locale/exportée est héritée du modèle processus UNIX (fork + environnement transmis par execve).
**Subtilités/confusions :**
- `VAR=valeur` sans export = variable LOCALE : les scripts appelés ne la voient PAS — erreur n°1 des débutants.
- export ne persiste pas : persistance = écrire dans `~/.profile` ou `~/.bashrc`.
- Exporter un secret = le rendre visible à TOUS les enfants du processus — préférer lecture fichier.
**Urgences/dangers :** ⚠️ `export PATH=` mal vidé = plus aucune commande introuvable → garder une session ouverte pour corriger.
**Précautions :** Toujours préfixer `PATH="$PATH:/..."` ; tester dans une sous-session.
**Équivalents :** $env:VAR (PowerShell), setx (persistance Windows), printenv (lecture)
**Voir aussi :** env, set, PATH, shell

## `env` — Environnement du processus et exécution isolée [Linux/macOS]
**Niveau :** debutant | **Popularité :** 72 | **Aliases :** printenv
**Contextes :** audit des variables, lancer avec un env minimal, debug de build "ça marche chez moi"
**Rôle :** Afficher les variables d'environnement, ou exécuter une commande avec un environnement modifié/vide.
**Syntaxe :** `env` / `env -i VAR=1 <commande>`
**Cas réguliers :**
- `env | sort` — Lister l'environnement trié (le plus courant)
- `env -i ./configure` — Build avec environnement VIDE (reproductibilité)
- `env VAR=1 command` — Une seule variable pour cette commande
- `env | grep KEY` — Vérifier qu'une variable existe
**Origine :** Utils BSD/System III (années 1980) — reflet de la table d'environnement passée par `execve(2)` dans le noyau UNIX.
**Subtilités/confusions :**
- env ≠ export : export MODIFIE l'environnement du shell, env LIT (ou exécute avec un env neuf).
- `env -i` est l'outil des bugs de reproductibilité : env minimal = comportement reproductible.
- Les tokens CI et clés y apparaissent en CLAIR — rediriger avant tout partage de dump.
**Urgences/dangers :** ⚠️ Ne jamais coller la sortie de `env` dans un ticket public : tokens dedans.
**Précautions :** Filtrer avant partage (`env | grep -v TOKEN`) ; secrets via gestionnaire dédié en prod.
**Équivalents :** printenv, Get-ChildItem Env: (PowerShell), set (CMD)
**Voir aussi :** export, set, PATH, shell

## `echo` — Afficher du texte ou une variable [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** Write-Output (PowerShell)
**Contextes :** scripts shell, debug d'une variable, messages d'état, redirection de fichier
**Rôle :** Écrire une chaîne de caractères sur la sortie standard (ou dans un fichier par redirection).
**Syntaxe :** `echo [options] <texte>`
**Cas réguliers :**
- `echo "début du traitement"` — Message dans un script (le plus courant)
- `echo $PATH` — Afficher une variable
- `echo "texte" > fichier.txt` — Écraser un fichier (une ligne)
- `echo -e "ligne1\nligne2"` — Interpréter \n (bash)
**Origine :** Shell V1 (Ken Thompson, 1971) — l'une des toutes premières commandes UNIX ; POSIX en a standardisé le comportement, d'où les options divergentes.
**Subtilités/confusions :**
- `echo $VAR` sans guillemets = word splitting et globbing : toujours `echo "$VAR"` (erreur classique avec espaces).
- echo -e n'est PAS standard (dépend du shell : zsh l'impose, bash -e requis, dash l'ignore) → `printf` est le portable.
- `>` écrase, `>>` ajoute : une coquille avec > détruit un fichier de config en 1 frappe.
**Urgences/dangers :** ⚠️ `echo ... > /etc/fichier` en root = écrasement direct — réfléchir avant la redirection.
**Précautions :** Toujours guillemeter les variables ; préférer printf dans les scripts partagés.
**Équivalents :** printf (formatage), Write-Output (PowerShell), print (CMD)
**Voir aussi :** printf, redirection, cat, shell

## `printf` — Affichage formaté portable [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 60 | **Aliases :** —
**Contextes :** scripts multi-plates-formes, génération de CSV, formatage de nombres/dates, prompts
**Rôle :** Afficher du texte selon un modèle de format (%s, %d, \n...) — version fiable et universelle d'echo -e.
**Syntaxe :** `printf "<format>" <args>`
**Cas réguliers :**
- `printf "%s\n" "hello"` — Une ligne, portable partout (le plus courant)
- `printf "ID;%s;%d\n" "$nom" "$age"` — Ligne CSV (guillemets obligatoires)
- `printf "%-10s %5d\n" "nom" 42` — Colonnes alignées
- `printf "%.2f" 3.14159` — 2 décimales
**Origine :** C (printf, 1973) puis reporté aux shells POSIX (format identical) — devenu le choix des scripts où la portabilité compte.
**Subtilités/confusions :**
- printf n'ajoute PAS de saut de ligne final contrairement à echo → `\n` explicite souvent nécessaire.
- Les guillemets sont OBLIGATOIRES autour du format (sinon le shell interprète % et espaces).
- `printf -- "-texte"` : un texte commençant par - est pris pour une option sans le `--`.
**Urgences/dangers :** — (aucun risque propre ; format mal formé = sortie faussée silencieusement)
**Précautions :** Tester avec un échantillon avant d'écrire dans un fichier critique ; toujours guillemeter.
**Équivalents :** echo -e (non portable), Write-Host -f (PowerShell)
**Voir aussi :** echo, redirection, awk, shell

## `clear` — Nettoyer l'affichage du terminal [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 70 | **Aliases :** cls (CMD/PowerShell)
**Contextes :** remise à zéro visuelle, démonstration, fin de traitement verbeux
**Rôle :** Effacer l'écran du terminal et replacer le curseur en haut à gauche.
**Syntaxe :** `clear` / `cls` (Windows)
**Cas réguliers :**
- `clear` — Effacer avant une démo (le plus courant)
- `clear && command` — Sortie propre d'un script visuel
- `Ctrl+L` — Raccourci équivalent dans la plupart des shells
**Origine :** Terminals physiques (clear_string émis vers le tty, années 1970) — aujourd'hui émission des séquences ANSI dépendant de $TERM.
**Subtilités/confusions :**
- clear efface l'AFFICHAGE, pas l'historique : `history` retrouvera tout — ≠ effacement mémoire.
- Dans un terminal sans support ANSI ou un $TERM mal défini, clear ne fait rien ou affiche du code brut.
- Effacer ne supprime pas les sorties redirigées vers fichier — elles sont intactes.
**Urgences/dangers :** — (aucun)
**Précautions :** En démo, `clear` + pipe vers less est préférable pour les sorties longues.
**Équivalents :** cls (Windows), Ctrl+L, printf '\033[2J'
**Voir aussi :** less, script, terminal, history

## `whatis` — Résumé d'une commande en une ligne [Linux/macOS]
**Niveau :** debutant | **Popularité :** 55 | **Aliases :** man -f
**Contextes :** découverte rapide, rappel du rôle d'une commande, doute entre homonymes
**Rôle :** Afficher la description d'une ligne extraite de la section 1 des manuels (commandes) — réponse immédiate à "ça fait quoi ?".
**Syntaxe :** `whatis <commande>`
**Cas réguliers :**
- `whatis grep` — → « grep - print lines matching a pattern » (le plus courant)
- `whatis -r ls` — Chercher dans les NOMBRES des descriptions (regex)
- `whatis -k cron` — Recherche par mot-clé (comme apropos)
**Origine :** man-db (John Palm, années 1990) — base de données mandb accélère les recherches ; `man -f` est l'équivalent exact.
**Subtilités/confusions :**
- whatis ≠ apropos : whatis décrit UNE commande connue, apropos CHERCHE des commandes par mot-clé.
- Base vide après install → `sudo mandb` (ou mandoc) doit être lancé ; sinon whatis répond « nothing appropriate ».
- Une seule entrée par commande : les alias/sections multiples peuvent surprendre.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Si vide, mettre à jour la base (`mandb`) ; croiser avec apropos pour les recherches.
**Équivalents :** apropos (recherche), man -f, man (page complète)
**Voir aussi :** apropos, man, info, --help

## `apropos` — Chercher une commande par mot-clé [Linux/macOS]
**Niveau :** debutant | **Popularité :** 50 | **Aliases :** man -k
**Contextes :** on connaît la FONCTION mais pas le nom de la commande, découverte d'outils
**Rôle :** Rechercher dans les résumés de TOUS les manuels pour trouver des commandes correspondant à un mot.
**Syntaxe :** `apropos <mot-clé>`
**Cas réguliers :**
- `apropos "disk usage"` — → du, df, statfs... (le plus courant)
- `apropos -e memory` — Correspondance exacte du mot
- `apropos -w firewall` — Mot entier seulement
- `man -k cron` — Équivalent exact d'apropos
**Origine :** BSD (années 1980), aujourd'hui man-db — fonctionne sur la base `whatis` (section 1 des pages man) indexée par mandb.
**Subtilités/confusions :**
- apropos cherche dans les DESCRIPTIONS une ligne, pas dans le contenu complet des pages → les résultats dépendent de la qualité des résumés.
- Base non mise à jour = 0 résultat → `sudo mandb` après installation de paquets.
- En français : la base est en anglais sur la plupart des systèmes (« disque » ne trouve rien).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Croiser avec `whatis` et `--help` une fois la commande trouvée.
**Équivalents :** whatis (description unique), man -k, Get-Help -Category (PowerShell)
**Voir aussi :** whatis, man, info, --help

## `info` — Documentation GNU détaillée [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 45 | **Aliases :** —
**Contextes :** approfondir une commande GNU, lire les notes/options avancées, documentation hypertexte
**Rôle :** Afficher la documentation Info (hypertexte GNU) — plus détaillée que le man, organisée en nœuds.
**Syntaxe :** `info <commande>` / `info -f <commande>`
**Cas réguliers :**
- `info coreutils` — Manuel collectif GNU des utilitaires (le plus courant)
- `info ls` — Page info de ls (souvent plus longue que man)
- Navigation : `n` (nœud suivant), `m` (aller au nœud), `q` (quitter)
**Origine :** Projet GNU (Richard Stallman, fin 1980) — le format Info a remplacé le format doc GNU dans les manuels papier ; Texinfo en est le langage source.
**Subtilités/confusions :**
- info ≠ man : man = référence par commande (page unique), info = ouvrage relié (nœuds, liens, menus).
- Les pages GNU existent souvent dans LES DEUX — même contenu, formats différents.
- Navigation info basée sur Emacs (C-s, m, n, q) — déroutant hors Emacs.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pour une question rapide, man et --help restent plus rapides ; info pour l'approfondissement.
**Équivalents :** man, --help, Get-Help (PowerShell)
**Voir aussi :** man, whatis, apropos, --help

## `whereis` — Localiser binaire, source et manuel [Linux/macOS]
**Niveau :** debutant | **Popularité :** 45 | **Aliases :** —
**Contextes :** installation complète d'un outil, vérification des emplacements, debug de packaging
**Rôle :** Afficher les chemins du binaire, du code source et de la page man d'une commande.
**Syntaxe :** `whereis [options] <commande>`
**Cas réguliers :**
- `whereis python` — → binaire /usr/bin/python, src, man (le plus courant)
- `whereis -b vim` — Binaire seulement
- `whereis -m vim` — Manuel seulement
**Origine :** BSD (années 1970-80), maintenu dans util-linux — regard sur les répertoires standards du système, sans index complet (contrairement à `locate`).
**Subtilités/confusions :**
- whereis vs which : whereis cherche les 3 composants (binaire, source, man), which = chemin de l'exécutable exécuté.
- whereis ne suit pas le PATH exactement : il fouille des répertoires codés en dur — peut trouver des binaire jamais appelables.
- Inverse de `file` : whereis dit OÙ, file dit CE QUE C'EST.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pour savoir ce qui sera EXÉCUTÉ, utiliser `which`/`command -v` — whereis donne des chemins potentiels.
**Équivalents :** which, command -v, type, locate (index complet)
**Voir aussi :** which, type, locate, file

## `command` — Exécuter en contournant alias et fonctions [Linux/macOS]
**Niveau :** avance | **Popularité :** 55 | **Aliases :** —
**Contextes :** scripts POSIX, diagnostic d'alias, récupération du binaire d'origine, tests de PATH
**Rôle :** Mot-clé du shell : interroger ou forcer la résolution d'une commande (contourne alias et fonctions selon l'option).
**Syntaxe :** `command [-pVv] <commande>` / `command -v <nom>`
**Cas réguliers :**
- `command -v git` — Chemin du binaire git résolu (POSIX, le plus courant en scripts)
- `command ls` — Exécute ls en IGNORANT l'alias `ls` du shell
- `command -V python` — Type + emplacement complet
- `command -v ma_var` — Tester l'EXISTENCE d'une variable (usage avancé)
**Origine :** POSIX.2 (1992) — le standard imposé pour les scripts portables, là où `which` et les alias divergent entre systèmes.
**Subtilités/confusions :**
- command -v vs which : les deux donnent le chemin, mais command -v respecte alias/fonctions/builtins selon le shell et EST le standard POSIX.
- `command <nom>` sans option = appel direct du binaire : contournement d'alias, précieux pour diagnostiquer.
- Dans #!/bin/sh, utiliser command -v : which n'est pas garanti (Debian dash !).
**Urgences/dangers :** — (aucun ; lecture ou exécution standard)
**Précautions :** Toujours `command -v` dans les tests de prérequis de scripts de prod.
**Équivalents :** which, type, Get-Command (PowerShell)
**Voir aussi :** which, type, alias, PATH

## `source` — Charger un fichier de config dans le shell courant [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 65 | **Aliases :** . (point)
**Contextes :** recharger .bashrc, appliquer des variables sans redémarrer, activer un environnement
**Rôle :** Exécuter les commandes d'un fichier DANS le shell courant — les effets (variables, aliases) persistent.
**Syntaxe :** `source <fichier>` ou `. <fichier>`
**Cas réguliers :**
- `source ~/.bashrc` — Recharger la config après modification (le plus courant)
- `. /etc/profile.d/proxy.sh` — Charger une variable d'entreprise
- `source .venv/bin/activate` — Activer un environnement Python
**Origine :** Bourne Shell (1979), le `.` historique — `source` vient des csh (BSD), aujourd'hui supporté par bash/zsh/fish.
**Subtilités/confusions :**
- source ≠ exécution : `./script.sh` tourne dans un sous-shell (effets perdus), source tourne ICI (effets gardés).
- Le point `.` est POSIX, `source` ne l'est pas toujours (dash/anciens sh) — en script portable utiliser `.`.
- source modifie l'état du shell en cours : une erreur dedans peut corrompre la session.
**Urgences/dangers :** ⚠️ Ne jamais source un script de TIERCE PARTIE : il s'exécute avec TES droits et modifie ton shell.
**Précautions :** Lire le fichier avant ; privilégier un redémarrage de terminal pour les configs sensibles.
**Équivalents :** . (POSIX), Import-Module (PowerShell), call (CMD)
**Voir aussi :** alias, export, shell, .bashrc

## `set` — Variables du shell et options de scripts [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 60 | **Aliases :** —
**Contextes :** debug de script (set -x), verrouillage d'options (set -euo pipefail), audit de variables
**Rôle :** Lister/modifier les variables du shell actif et activer des options de comportement du script.
**Syntaxe :** `set` / `set [-exu]` / `set -- args`
**Cas réguliers :**
- `set -euo pipefail` — Tête de script sécurisée (le plus courant)
- `set -x` — Tracer chaque commande exécutée (debug)
- `set +x` — Arrêter le trace
- `set -- a b c` — Positionner les paramètres du shell
**Origine :** Bourne Shell (1979) — options en "sifflets" 2 lettres ; `set -e` est devenu le standard de robustesse des scripts modernes.
**Subtilités/confusions :**
- `set -e` (erreur → exit) ≠ `set -u` (var non définie → erreur) ≠ `pipefail` (pipeline au 1er échec) : les 3 = rigueur maximale.
- `set -x` affiche les variables EXPANSÉES — tokens visibles dans les logs CI.
- grep sans match = code 1 : avec set -e, ça tue le script — connaître ce piège classique.
**Urgences/dangers :** ⚠️ `set -e` peut arrêter un script inopinément sur une commande qui "échoue" innocemment (`grep` sans résultat).
**Précautions :** `set -euo pipefail` en tête de tout script de prod ; `set +e` local pour les cas contrôlés.
**Équivalents :** $ErrorActionPreference (PowerShell), `set -o` (options bash)
**Voir aussi :** export, env, shell, pipefail

## `unset` — Supprimer une variable ou une fonction [Linux/macOS]
**Niveau :** debutant | **Popularité :** 55 | **Aliases :** —
**Contextes :** nettoyage d'environnement, purge de variable de travail, désactivation d'alias ou de hooks
**Rôle :** Retirer une variable ou une fonction du shell (ou de l'environnement enfant avec -f).
**Syntaxe :** `unset [options] <nom>`
**Cas réguliers :**
- `unset TEMP_VAR` — Oublier une variable de travail (le plus courant)
- `unset alias ll` — Retirer un alias (bash)
- `unset -f ma_fonction` — Supprimer une fonction (-f force le type fonction)
- `unset LD_PRELOAD` — Purger un hook avant un lancement sensible
**Origine :** Bourne Shell (1979), standard POSIX — l'opposé exact de `set`/`export`.
**Subtilités/confusions :**
- unset ne modifie PAS le processus parent : impossible de nettoyer l'environnement hérité d'un shell parent.
- unset ne sécurise pas la mémoire : la valeur peut subsister dans un swap/coredump — effacer ≠ garantir l'absence.
- `unset VAR` puis `set -u` : toute utilisation ultérieure devient une ERREUR (voulu dans les scripts rigoureux).
**Urgences/dangers :** ⚠️ `unset PATH` rend le shell inopérant — jamais sur une session de prod.
**Précautions :** Tester dans une sous-session ; ne pas compter sur unset pour la destruction de secrets.
**Équivalents :** Remove-Item Env:VAR (PowerShell), set VAR= (CMD, valeur vide)
**Voir aussi :** set, export, env, shell

## `eval` — Évaluer une chaîne comme commande [Linux/macOS]
**Niveau :** avance | **Popularité :** 50 | **Aliases :** —
**Contextes :** scripts avancés, construction dynamique de commandes, redirections variables
**Rôle :** Concaténer les arguments, interpréter la chaîne résultante comme une commande et l'exécuter (double interprétation).
**Syntaxe :** `eval <commande_construite>`
**Cas réguliers :**
- `eval "$CMD"` — Exécuter une commande stockée dans une variable (le plus courant, à risque)
- `eval "N=$N+1"` — Arithmétique dans les anciens sh (avant $(( )))
- `eval "printf '%s\n' \$$var"` — Déréférencement indirect de variable
**Origine :** Bourne Shell (1979) — hérité du besoin de construction dynamique dans les shells sans tableaux modernes.
**Subtilités/confusions :**
- eval = exécution de code à chaud : toute variable contrôlée par un utilisateur = INJECTION DE COMMANDES — piège n°1 d'eval.
- Deux passes d'interprétation : métacaractères interprétés DEUX fois (`$`, quotes, backticks).
- Le code moderne s'en passe : tableaux, `$(( ))`, expansion indirecte `${!var}`.
**Urgences/dangers :** ⚠️ ÉVITER eval sur toute donnée externe (form, args, API) — équivalent shell d'une injection SQL, faille critique récurrente.
**Précautions :** Si indispensable, whitelist stricte de l'entrée avant eval ; commenter le pourquoi.
**Équivalents :** Invoke-Expression (PowerShell — même danger), aucun équivalent recommandé
**Voir aussi :** set, shell, injection, script

## `test` / `[` — Conditions dans les scripts [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** [
**Contextes :** scripts shell, conditions if/while, vérification de fichiers et de chaînes
**Rôle :** Évaluer une expression booléenne (fichier existe, chaînes égales, nombres comparés) et renvoyer 0 (vrai) ou 1 (faux).
**Syntaxe :** `test <expr>` ou `[ <expr> ]`
**Cas réguliers :**
- `if [ -f "/etc/passwd" ]; then ... fi` — Le fichier existe (le plus courant)
- `[ "$var" = "valeur" ]` — Comparaison de chaînes (espaces critiques !)
- `[ -d "$dir" ] || mkdir -p "$dir"` — Créer si absent
- `[ "$n" -gt 10 ]` — Comparaison numérique (et non chaîne)
**Origine :** Shell V7 (1979) — le `[` est historiquement une commande alias de `test` fermée par `]`, d'où les espaces obligatoires.
**Subtilités/confusions :**
- Espaces OBLIGATOIRES après `[` et avant `]` : `[ "$a"="$b" ]` = syntaxe fausse silencieuse.
- `=` pour les chaînes, `-gt/-lt` pour les nombres : un test numérique sur du texte casse.
- `[[ ... ]]` (bash) est plus sûr (regex `=~`) mais non POSIX — en `#!/bin/sh` utiliser `[`.
**Urgences/dangers :** ⚠️ Un test qui passe à tort peut sauter une étape critique (backup, migration) — vérifier les codes de retour.
**Précautions :** Toujours guillemeter les variables ; `[[ ]]` en bash, `[ ]` en sh portable.
**Équivalents :** if (langage), [Test-Path] (PowerShell), if exist (CMD)
**Voir aussi :** if, expr, shell, script

## `expr` — Calcul et expressions en ligne de commande [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 45 | **Aliases :** —
**Contextes :** scripts anciens, arithmétique shell simple, extraction par regex, tests courts
**Rôle :** Évaluer une expression (arithmétique, comparaison, substr) et afficher le résultat.
**Syntaxe :** `expr <expression>`
**Cas réguliers :**
- `expr 2 + 3` — → 5 (espaces OBLIGATOIRES)
- `x=$(expr $x + 1)` — Incrément dans les anciens sh
- `expr "$f" : '\(.*\)\.txt'` — Extraction par regex (usage avancé)
- `expr "$a" \> "$b"` — Comparaison (le `>` doit être échappé !)
**Origine :** Unix V7 (1979) — l'ancêtre de `$(( ))` ; toujours présent pour la compatibilité des scripts hérités.
**Subtilités/confusions :**
- expr est REMPLACÉ par `$(( ))` en bash : `x=$((x+1))` est plus simple et sans subprocess.
- Espaces partout : `expr 2+3` affiche "2+3" (chaîne) au lieu de 5.
- `expr 0` retourne exit code 1 (faux) : l'usage comme test est une astuce classique mais piégeuse.
**Urgences/dangers :** — (aucun ; division par zéro = erreur gérée par le script)
**Précautions :** Scripts neufs = `$(( ))` et `[[ ]]` ; expr pour la maintenance du legacy.
**Équivalents :** $(( )) (bash), let (bash), calcul en langage de prog
**Voir aussi :** test, set, shell, script

## `bc` — Calculateur en précision arbitraire [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 40 | **Aliases :** —
**Contextes :** calculs flottants dans les scripts shell, pourcentages, conversions de bases, mathématiques précises
**Rôle :** Traitement de calcul (entiers, décimaux, bases) lu sur stdin — le calculateur des scripts shell sans flottants natifs.
**Syntaxe :** `echo "expression" | bc` / `bc -l`
**Cas réguliers :**
- `echo "10/3" | bc` — → 3 (division entière par défaut)
- `echo "scale=2; 10/3" | bc` — → 3.33 (2 décimales)
- `echo "obase=16; 255" | bc` — Conversion en hexadécimal
- `echo "a=5; b=3; a*b" | bc -l` — Programme multi-lignes avec -l
**Origine :** Bell Labs (Rob Pike et Belle, années 1970) — « calculator language » ; toujours l'outil GNU standard pour le calcul dans les pipelines.
**Subtilités/confusions :**
- Division entière par défaut : `scale` ou `-l` explicite SINON les résultats trompent silencieusement.
- bc ≠ expr : bc gère les flottants et les bases, expr fait du shell simple.
- En bash moderne, `awk` fait aussi le calcul : `awk 'BEGIN{print 10/3}'` — souvent plus pratique dans un pipe.
**Urgences/dangers :** — (aucun)
**Précautions :** Toujours `scale=` ou `-l` explicite ; vérifier la sortie avant de l'utiliser comme valeur de config.
**Équivalents :** awk BEGIN, $(( )) (entiers), python -c (complexe)
**Voir aussi :** expr, awk, date, shell

## `date` — Afficher ou formater la date et l'heure [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 85 | **Aliases :** Get-Date (PowerShell)
**Contextes :** horodatage dans les scripts, noms de fichiers datés, calculs de durée, logs
**Rôle :** Afficher la date courante, la formater selon un modèle, ou convertir un timestamp.
**Syntaxe :** `date [+"format"]` / `date -d <expr>`
**Cas réguliers :**
- `date +"%Y-%m-%d"` — 2026-09-29 ISO (le plus courant, pour les fichiers)
- `backup-$(date +%F).tar.gz` — Nom de backup daté
- `date -d "yesterday" +%F` — Hier (GNU date)
- `date +%s` — Epoch courant (calculs de durées)
**Origine :** Unix V7 (1979) — formats %Y/%m/%d hérités de `strftime` C ; GNU date (coreutils) a ajouté `-d` avec dates naturelles.
**Subtilités/confusions :**
- `date -d` (GNU/Linux) vs `date -j -f` (macOS/BSD) : « yesterday » n'est PAS portable entre les deux.
- En scripts multi-OS, préférer Python/ISO 8601 — les formats varient entre BSD et GNU.
- `%F` = %Y-%m-%d et `%T` = %H:%M:%S (raccourcis GNU) — indisponibles sur les vieux BSD.
**Urgences/dangers :** ⚠️ Horloge fausse = certificats TLS « expirés », logs incohérents, cron raté → vérifier NTP (`timedatectl`).
**Précautions :** Vérifier l'horloge avant les opérations planifiées critiques ; horodater les logs de manipulation.
**Équivalents :** Get-Date (PowerShell), date /T (CMD), strftime (C/Python)
**Voir aussi :** cron, log, timestamp, sleep

## `watch` — Répéter une commande en continu à l'écran [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 70 | **Aliases :** —
**Contextes :** suivi temps réel (files, processus, métriques), surveillance pendant un test, dashboards console
**Rôle :** Exécuter une commande à intervalle régulier et rafraîchir l'écran avec le résultat.
**Syntaxe :** `watch [-n <sec>] <commande>`
**Cas réguliers :**
- `watch -n 2 df -h` — Espace disque toutes les 2 s (le plus courant)
- `watch -n 1 'ls -la /var/log'` — Surveiller l'arrivée de logs (guillemets si pipe)
- `watch -d 'grep foo fichier'` — Mettre en évidence les DIFFÉRENCES entre rafraîchissements
- `watch -n 0.5 nvidia-smi` — Monitoring GPU (fraction de seconde)
**Origine :** procps (années 1990, Linux) — équivalent du `watch` BSD/Unix original pour la surveillance opérateur.
**Subtilités/confusions :**
- Les pipes et redirections nécessitent des GUILLEMETS : `watch ls | wc` ne fait pas ce que tu crois (watch n'exécute qu'une commande).
- Défaut = 2 s ; trop rapide sur une commande lourde = le rafraîchissement se chevauche.
- watch affiche à l'écran SEULEMENT : aucune sortie historisée (pas de log) — pour logger, utiliser une boucle + tee.
**Urgences/dangers :** — (aucun ; watch interroge en continu — éviter sur des appels réseau coûteux)
**Précautions :** Toujours guillemeter les commandes composées ; `Ctrl+C` pour quitter.
**Équivalents :** Clear-Host + boucle (PowerShell), `while true; do ...; done`
**Voir aussi :** top, tail, timeout, shell

## `timeout` — Limiter la durée d'exécution d'une commande [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 65 | **Aliases :** gtimeout (macOS/coreutils)
**Contextes :** scripts robustes, commandes réseau non bornées, protection contre les boucles infinies, CI
**Rôle :** Exécuter une commande et l'arrêter automatiquement si elle dépasse un délai, avec code de retour dédié.
**Syntaxe :** `timeout <durée> <commande>`
**Cas réguliers :**
- `timeout 5 curl https://site.fr` — Couper un curl bloqué (le plus courant)
- `timeout 300 ./job.sh` — Job plafonné à 5 min dans un cron
- `timeout --signal=KILL 10 cmd` — SIGKILL si SIGTERM ignoré (dernier recours)
- `timeout 60 ssh host 'long-task'` — SSH qui ne pend jamais
**Origine :** GNU coreutils (apparu vers 2008) — le besoin datait des scripts Unix qui pendaient sur les réseaux (années 1990).
**Subtilités/confusions :**
- Code de retour 124 = TIMEOUT (à tester explicitement avec `|| [ $? = 124 ]`).
- SIGTERM d'abord (propre), SIGKILL seulement avec --signal : une commande peut ignorer SIGTERM.
- macOS n'a pas `timeout` natif → `brew install coreutils` (gtimeout) ou `perl -e 'alarm...'`.
**Urgences/dangers :** ⚠️ timeout -9 brutal peut laisser des fichiers à moitié écrits — préférer un SIGTERM + logique de nettoyage.
**Précautions :** Toujours un délai dans les jobs cron critiques ; gérer le code 124.
**Équivalents :** Start-Process + Kill (PowerShell), timeout /t (CMD, limité)
**Voir aussi :** watch, cron, kill, shell

## `seq` — Générer une séquence de nombres [Linux/macOS]
**Niveau :** debutant | **Popularité :** 55 | **Aliases :** —
**Contextes :** boucles for, génération de fichiers tests, indexation, incréments
**Rôle :** Afficher une progression arithmétique (début, pas, fin) — un nombre par ligne.
**Syntaxe :** `seq [début] <fin>` / `seq -s <séparateur> début pas fin`
**Cas réguliers :**
- `seq 1 10` — 1 à 10 (le plus courant)
- `for i in $(seq 1 5); do echo $i; done` — Boucle for numérique
- `seq -s , 1 5` — 1,2,3,4,5 (séparateur virgule)
- `seq 10 -2 1` — Décrément de 2 (pas négatif)
**Origine :** GNU coreutils (1991) — remplace le moins lisible `i=1; while [ $i -le 10 ]` des scripts Bourne.
**Subtilités/confusions :**
- seq n'existe PAS nativement sur les vieux macOS/BSD → `jot 10` (BSD) ou `{1..10}` (bash).
- `{1..10}` (expansion de brace) est plus rapide et sans subprocess dans bash — seq reste plus flexible (pas non entier).
- seq ne crée PAS de fichier : il écrit sur stdout → rediriger si besoin.
**Urgences/dangers :** — (aucun)
**Précautions :** En bash pur, préférer `{1..n}` ; seq pour les pas décimaux (`seq 0 0.5 2`).
**Équivalents :** {1..10} (bash), jot (BSD), range (Python)
**Voir aussi :** for, expr, shell, script

## `sleep` — Attendre un nombre de secondes [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** Start-Sleep (PowerShell)
**Contextes :** temporisation dans les scripts, backoff entre tentatives, espacement de traitements, rate limit
**Rôle :** Suspendre l'exécution du script pendant une durée donnée (secondes, minutes, heures selon les versions).
**Syntaxe :** `sleep <durée>`
**Cas réguliers :**
- `sleep 5` — Attendre 5 s avant une vérification (le plus courant)
- `sleep 1 && check` — Laisser le temps au service de démarrer
- `for i in 1 2 3; do cmd || sleep $((2**i)); done` — Backoff exponentiel simple
- `sleep 1m` — Durée avec unité (GNU)
**Origine :** Unix V7 (1979) — l'une des commandes les plus simples ; GNU a ajouté les unités (s/m/h/d) en 2008.
**Subtilités/confusions :**
- BSD/macOS accepte `sleep 1.5` (décimal) mais pas toujours `sleep 1m` — GNU accepte les deux.
- sleep BLOQUE le shell : dans un serveur, préférer des timers/timerfd — le sleep en prod = code fragile.
- Sleeps dans un test = tests lents et suspects : souvent un symptôme de race condition cachée.
**Urgences/dangers :** ⚠️ `sleep` utilisé comme filet devant une condition non garantie (attente de démarrage) ne GARANTIT RIEN — préférer une boucle de health check.
**Précautions :** Remplacer les sleeps fixes par `wait_for()` avec timeout ; garder les durées courtes.
**Équivalents :** Start-Sleep (PowerShell), timeout /t (CMD), time.sleep (Python)
**Voir aussi :** timeout, cron, watch, shell

## `read` — Lire une saisie depuis le clavier ou un pipe [Linux/macOS]
**Niveau :** debutant | **Popularité :** 70 | **Aliases :** Read-Host (PowerShell)
**Contextes :** scripts interactifs, invite utilisateur, lecture ligne à ligne d'un fichier, parsing stdin
**Rôle :** Lire une ligne (ou un flux) et la stocker dans une variable — la saisie des scripts shell.
**Syntaxe :** `read [-options] variable`
**Cas réguliers :**
- `read -p "Mot de passe ? " mdp` — Invite (le plus courant)
- `read -s -p "PIN : " pin` — Saisie cachée (masque l'écho)
- `while read -r ligne; do echo "$ligne"; done < fichier` — Parcourir un fichier
- `IFS=: read -r u p rest < /etc/passwd` — Découpage sur séparateur
**Origine :** Bourne Shell (1979), POSIX — `read` est le seul moyen portable d'interagir avec un humain dans un script sh.
**Subtilités/confusions :**
- Toujours `-r` : sans lui, read interprète les antislashs et corrompt les chemins.
- `IFS=` devant read préserve les espaces en début/fin de ligne (lecture fidèle).
- read retourne 1 sur fin de fichier : la dernière ligne SANS newline est lue mais le while s'arrête — piège classique.
**Urgences/dangers :** ⚠️ Ne jamais évaluer (`eval`) ni injecter dans une commande une valeur lue avec read sans validation.
**Précautions :** `read -r` systématique ; valider la longueur et le contenu de la saisie.
**Équivalents :** Read-Host (PowerShell), input() (Python), scanf (C)
**Voir aussi :** while, IFS, set, shell

## `getopts` — Analyser les options d'un script [Linux/macOS]
**Niveau :** avance | **Popularité :** 45 | **Aliases :** —
**Contextes :** écrire des scripts avec des flags propres (-v, -f fichier), CLI shell portables
**Rôle :** Fonction intégrée au shell qui parse les arguments `-x` / `-x valeur` selon une spécification, de façon portable.
**Syntaxe :** `while getopts "ab:c" opt; do case $opt in ... esac; done`
**Cas réguliers :**
- `while getopts "vf:h" o; do case $o in v) VERBOSE=1;; f) FILE=$OPTARG;; h) usage;; esac; done` — Flags typés (le plus courant)
- `shift $((OPTIND-1))` — Récupérer les arguments positionnels restants
- `":vf:"` (deux-points en tête) — mode silencieux : le script gère ses erreurs
- `--` — Fin d'options pour passer des arguments commençant par `-`
**Origine :** Bourne Shell (1979) — la réponse d'Unix au parsing manuel d'argv, normalisée POSIX ; getopt_long (GNU) est apparu après.
**Subtilités/confusions :**
- `a:` = option A AVEC argument, `a` = sans argument : le deux-points est la signature de l'argument.
- getopts est une fonction interne du shell : elle ne parse que les options EN TÊTE des arguments.
- getopts = options COURTES uniquement ; pour `--verbose`, gérer manuellement ou utiliser getopt_long.
**Urgences/dangers :** — (aucun)
**Précautions :** Toujours implémenter `-h` et le cas `*` (option inconnue) + `exit 1`.
**Équivalents :** paramètres avancés (PowerShell), argparse (Python), clap (Rust)
**Voir aussi :** set, shift, test, shell

## `trap` — Exécuter du code sur un signal ou à la sortie [Linux/macOS]
**Niveau :** avance | **Popularité :** 55 | **Aliases :** —
**Contextes :** nettoyage de fichiers temporaires, gestion de Ctrl+C, hooks de sortie de script, signaux
**Rôle :** Enregistrer une commande à exécuter quand le shell reçoit un signal (INT, TERM, EXIT, etc.).
**Syntaxe :** `trap '<commande>' <signal...>`
**Cas réguliers :**
- `trap 'rm -f /tmp/$$.tmp' EXIT` — Nettoyage garanti à la sortie (le plus courant)
- `trap 'echo Annulé; exit 130' INT` — Réagir proprement à Ctrl+C
- `trap - EXIT` — Désinstaller le hook
- `trap '' HUP` — Rendre le script sourd à un signal
**Origine :** Bourne Shell (1979), POSIX — le mécanisme de gestion des signaux des scripts, hérité des signaux Unix (V7).
**Subtilités/confusions :**
- EXIT se déclenche aussi sur `exit` normal et sur erreur fatale : c'est le « finally » du shell.
- SIGKILL (9) et SIGSTOP ne peuvent JAMAIS être interceptés : aucun trap possible.
- Un trap déclaré dans une fonction peut rester actif après son retour (bash) : piège de scope.
**Urgences/dangers :** ⚠️ Un trap EXIT contenant un `rm -rf` mal construit supprime des données à CHAQUE sortie, y compris sur erreur.
**Précautions :** Tester le trap en tuant le script manuellement (Ctrl+C, kill) avant la mise en prod.
**Équivalents :** try/finally (langages), Register-EngineEvent (PowerShell)
**Voir aussi :** kill, signal, exec, shell

## `exec` — Remplacer le shell ou ouvrir des redirections durables [Linux/macOS]
**Niveau :** avance | **Popularité :** 45 | **Aliases :** —
**Contextes :** scripts wrapper, ouverture de descripteurs, fusion de flux, conteneurs
**Rôle :** (1) Remplacer le processus shell courant par une autre commande ; (2) établir des redirections persistantes.
**Syntaxe :** `exec <commande>` / `exec 3<fichier` / `exec >log`
**Cas réguliers :**
- `exec "$@"` — Fin de wrapper : le programme remplace le shell, un seul PID (le plus courant)
- `exec > >(tee log.txt)` — Logguer toute la suite du script
- `exec 3< fichier.txt` — Ouvrir un descripteur de fichier en lecture
- `exec 2>&1` — Fusionner stderr dans stdout pour tout le script
**Origine :** Bourne Shell (1979) — l'appel système `execve` exposé au shell : remplacement de processus sans fork.
**Subtilités/confusions :**
- exec ne crée PAS de sous-processus : après exec le script est MORT, rien de ce qui suit ne s'exécute.
- `exec >log` sans filet = plus de sortie console, les `echo` deviennent invisibles.
- Dans un conteneur, la forme exec du ENTRYPOINT évite un shell père qui ne relaie pas les signaux.
**Urgences/dangers :** ⚠️ `exec` dans un fichier `source` tue le shell appelant : ne jamais exec dans une config sourcée.
**Précautions :** Réserver exec aux fins de scripts et aux ouvertures de descripteurs ; tester en session jetable.
**Équivalents :** Start-Process (PowerShell, sans remplacement), os.execv (Python)
**Voir aussi :** source, nohup, signal, shell

## `ulimit` — Fixer les limites de ressources du shell [Linux/macOS]
**Niveau :** avance | **Popularité :** 45 | **Aliases :** limit (csh/tcsh)
**Contextes :** épuisement de descriptors, « too many open files », confinement d'un script, cores dumper
**Rôle :** Afficher ou fixer les plafonds de ressources (fichiers ouverts, mémoire, processus, taille de core) pour le shell et ses enfants.
**Syntaxe :** `ulimit [-a] [-n|-u|-f|-c] <valeur>`
**Cas réguliers :**
- `ulimit -a` — Lister toutes les limites (diagnostic, le plus courant)
- `ulimit -n 4096` — Plus de « too many open files » (besoin classique)
- `ulimit -c 0` — Désactive les core dumps (serveur sensible)
- `ulimit -f 1048576` — Plafonner un script qui écrit trop (1 Go)
**Origine :** BSD/Bourne (années 1980) — interface au système `setrlimit` d'Unix ; les limites système viennent de /etc/security/limits.conf (Linux PAM).
**Subtilités/confusions :**
- `ulimit -n X` ne peut AUGMENTER la dure (hard) qu'en root — sinon seule la limite souple monte.
- Les limites d'un SERVICE systemd ne viennent PAS du shell : se règle dans l'unit (LimitNOFILE=).
- ulimit est par session shell : non persistant, non global — souvent source de confusion « ça marche en SSH, pas en cron ».
**Urgences/dangers :** ⚠️ Baisser `ulimit -u` ou `-n` sur une machine vivante peut empêcher l'ouverture de fichiers critiques.
**Précautions :** Modifier en test d'abord ; documenter la valeur persistée (limits.conf / unit systemd).
**Équivalents :** Get-Process (lecture seule), quotas (Windows), limits.conf (Linux)
**Voir aussi :** kill, top, shell, systemd

## `jobs` — Lister les travaux du shell [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 60 | **Aliases :** —
**Contextes :** commandes lancées avec &, basculer une tâche entre premier et arrière-plan, reprendre un job arrêté
**Rôle :** Lister les processus fils gérés par le shell courant avec leur numéro, état et ligne de commande.
**Syntaxe :** `jobs [-l] [job...]`
**Cas réguliers :**
- `jobs` — Qui tourne, suspendu ou en arrière-plan (le plus courant)
- `jobs -l` — Afficher les PID en plus des numéros
- `sleep 300 &` puis `jobs` — Repérer `[1] Running`
- `kill %2` — Cibler un job par son numéro (pratique contre un PID inconnu)
**Origine :** Bourne Shell (1979) — la « job control » est arrivée avec le shell Bourne et le signal TSTP (Ctrl+Z) ; `jobs` en est l'inventaire.
**Subtilités/confusions :**
- `jobs` ne voit que les processus du shell COURANT : une autre fenêtre ou un autre terminal ne les voit pas.
- `%1` = job n°1 pour le shell ; `1` = PID pour `kill` : ce ne sont pas les mêmes numéros.
- Un job `Stopped (SIGTSTP)` occupe la mémoire et peut bloquer une ressource : reprendre (`fg`) ou tuer (`kill %1`).
**Urgences/dangers :** ⚠️ Fermer le terminal envoie SIGHUP aux jobs non `disown`/`nohup` : une sauvegarde en cours peut être tuée.
**Précautions :** Vérifier `jobs` avant de fermer une session ; `disown` ou `nohup` pour les longues tâches.
**Équivalents :** Get-Job / Start-Job (PowerShell), Ctrl+Z (interaction)
**Voir aussi :** fg, bg, nohup, kill

## `nohup` — Poursuivre une commande après déconnexion [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 65 | **Aliases :** —
**Contextes :** job long sur SSH, mission qui doit survivre à la fermeture du terminal, migration
**Rôle :** Lancer une commande en l'immunisant contre SIGHUP ; la sortie part dans nohup.out.
**Syntaxe :** `nohup <commande> [&]`
**Cas réguliers :**
- `nohup ./backup.sh &` — Le backup survit à la fermeture SSH (le plus courant)
- `nohup ./job.sh > job.log 2>&1 &` — Rediriger proprement la sortie (recommandé)
- `nohup long-task & disown` — Double protection
- `tail -f nohup.out` — Suivre la sortie par défaut
**Origine :** Unix System III (1980) — commande POSIX « no hang-up » née des lignes série : la coupure modem tuait tous les jobs.
**Subtilités/confusions :**
- nohup ne DÉTACHE pas le processus (contrairement à `setsid` ou `screen`) : le terminal se ferme, mais le job survit au SIGHUP.
- Sans redirection explicite, TOUT part dans `./nohup.out` : risque de disque plein et d'infos sensibles dans un fichier du dépôt.
- nohup ne remplace pas un service : pour un redémarrage automatique, utiliser systemd (unit).
**Urgences/dangers :** ⚠️ `nohup` en prod = job invisible hors terminal, non supervisé et non relancé. Préférer systemd/tmux.
**Précautions :** Toujours rediriger la sortie et noter le PID ; préférer tmux pour les jobs interactifs.
**Équivalents :** Start-Process (PowerShell), setsid, tmux/screen (detach)
**Voir aussi :** jobs, disown, tmux, systemd

## `fg` — Ramener un job au premier plan [Linux/macOS]
**Niveau :** debutant | **Popularité :** 60 | **Aliases :** —
**Contextes :** reprendre une commande suspendue avec Ctrl+Z, retrouver un shell rendu aveugle
**Rôle :** Remettre un job (suspendu ou d'arrière-plan) sur le terminal pour interagir avec lui.
**Syntaxe :** `fg [%job]`
**Cas réguliers :**
- `fg` — Reprendre le dernier job suspendu (le plus courant, après Ctrl+Z)
- `fg %2` — Reprendre le job n°2 de `jobs`
- Ctrl+Z puis `fg` — Reprendre l'éditeur/SSH gelé sans perdre la session
- `fg` sur un `vim` suspendu — Retrouver son terminal « cassé »
**Origine :** Bourne Shell (1979) — pair de `bg`, issu du job control des shells Unix avec le signal SIGCONT.
**Subtilités/confusions :**
- `fg` ne fonctionne que sur les jobs du shell courant (pas les processus lancés par systemd ou cron).
- Un job en arrière-plan qui lit le clavier s'arrête immédiatement (SIGTTIN) : il faut le remettre en `fg`.
- Si le terminal reste bizarre après un `fg` d'un programme plein écran : `reset` ou `clear`.
**Urgences/dangers :** ⚠️ Suspendre un client SSH avec Ctrl+Z puis oublier le job = session SSH encore ouverte et invisible.
**Précautions :** Vérifier `jobs` avant de fermer la session ; `fg` plutôt que relancer une tâche lourde.
**Équivalents :** Receive-Job (PowerShell), Ctrl+Z puis fg
**Voir aussi :** bg, jobs, kill, tmux

## `bg` — Reprendre un job en arrière-plan [Linux/macOS]
**Niveau :** debutant | **Popularité :** 55 | **Aliases :** —
**Contextes :** relancer un Ctrl+Z sans le remettre à l'écran, libérer le terminal pendant un calcul
**Rôle :** Reprendre l'exécution d'un job suspendu SANS le ramener sur le terminal.
**Syntaxe :** `bg [%job]`
**Cas réguliers :**
- Ctrl+Z puis `bg` — Laisser tourner la tâche gelée en arrière-plan (le plus courant)
- `bg %1` — Reprendre le job n°1 en arrière-plan
- `bg` après Ctrl+Z sur un build — Récupérer son shell immédiatement
- `jobs` puis `bg` — Vérifier puis relancer proprement
**Origine :** Bourne Shell (1979) — SIGCONT en arrière-plan ; le réflexe naturel de la génération Ctrl+Z.
**Subtilités/confusions :**
- `bg` sur un job qui ATTEND le clavier le re-suspend aussitôt (SIGTTIN) : c'est le comportement normal.
- `bg` n'ajoute pas `&` à la ligne de commande d'origine : il faut le faire pour les lancements futurs.
- Un job `bg` reste lié au terminal : fermer la fenêtre l'interrompt (SIGHUP) — combiner avec `disown` ou `nohup`.
**Urgences/dangers :** ⚠️ `bg` sur un job interactif (SSH, éditeur) le laisse dans un état demi-mort : préférer tmux.
**Précautions :** Rediriger les entrées/sorties du job avant `bg` ; vérifier `jobs` ensuite.
**Équivalents :** Start-Job / Resume-Job (PowerShell), Ctrl+Z puis bg
**Voir aussi :** fg, jobs, nohup, tmux

## `disown` — Retirer un job de la liste du shell [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 45 | **Aliases :** —
**Contextes :** sauver un job lancé trop tard, le rendre indépendant de la fenêtre, rattraper un oubli de nohup
**Rôle :** Oublier volontairement un job : le shell ne l'interrompra plus à la fermeture (plus de SIGHUP).
**Syntaxe :** `disown [-h] [%job]`
**Cas réguliers :**
- `long-task & disown` — Survivre à la fermeture du terminal (le plus courant)
- Ctrl+Z, `bg`, `disown` — Rattraper une tâche oubliée sans nohup
- `disown -h %1` — Ne pas lui envoyer SIGHUP (le job reste listé)
- `jobs` (vide) — Vérifier qu'il est bien désolidarisé
**Origine :** csh (1979), repris par bash/ksh — le complément de `nohup` pour les jobs DÉJÀ lancés.
**Subtilités/confusions :**
- disown ne protège PAS des autres signaux : un `kill` manuel fonctionne toujours.
- Après disown, le job disparaît de `jobs` : on ne retrouve plus son numéro, il faut `ps` pour le PID.
- disown n'existe pas en `sh` POSIX ni en dash : en script portable, utiliser `nohup` ou `setsid`.
**Urgences/dangers :** ⚠️ Un job disowné et oublié continue de consommer CPU/RAM en prod sans surveillance ni propriétaire identifié.
**Précautions :** Noter le PID (`echo $!`) après disown ; préférer tmux ou systemd pour les tâches durables.
**Équivalents :** Detaché (Start-Process), setsid, tmux detach
**Voir aussi :** jobs, nohup, fg, tmux

## `time` — Mesurer la durée d'exécution [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 70 | **Aliases :** time (mot-clé bash)
**Contextes :** benchmarker un script, comparer deux commandes, diagnostiquer une lenteur, valider une optimisation
**Rôle :** Mesurer le temps réel, utilisateur (CPU) et système (noyau) consommés par une commande.
**Syntaxe :** `time <commande>`
**Cas réguliers :**
- `time ./build.sh` — real/user/sys en fin de sortie (le plus courant)
- `time (make -j8)` — Chronométrer une commande composée (sous-shell)
- `\time -v ls` — Forcer le binaire /usr/bin/time et ses mesures détaillées
- `time curl -s site.fr -o /dev/null` — Mesurer un temps réseau
**Origine :** Unix V7 (1979, Ken) — les trois valeurs real/user/sys viennent des appels `times()`/`getrusage()` du noyau Unix.
**Subtilités/confusions :**
- `time` est tantôt un MOT-CLÉ du shell, tantôt le binaire `/usr/bin/time` : `\time` force le binaire (plus d'options).
- real = temps wall-clock, user+sys = temps CPU : real >> user+sys signifie attente (disque, réseau, lock).
- user+sys > real prouve un travail PARALLÈLE (multi-cœur) — souvent mal interprété comme une erreur.
**Urgences/dangers :** — (aucun ; `time` sur une commande lourde consomme deux fois le temps si on relance pour comparer)
**Précautions :** Une seule mesure ne vaut rien : répéter 3 fois, ignorer le 1er (cache froid).
**Équivalents :** Measure-Command (PowerShell), hyperfine (moderne), perf
**Voir aussi :** top, perf, watch, shell

## `wait` — Attendre la fin de processus [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 45 | **Aliases :** —
**Contextes :** parallélisation dans un script (tâches & + wait), collecte de codes de retour, synchronisation
**Rôle :** Suspendre le script jusqu'à la fin des jobs ou PID donnés, et récupérer leurs codes de retour.
**Syntaxe :** `wait [-n] [pid|job...]`
**Cas réguliers :**
- `cmd1 & cmd2 & wait` — Lancer en parallèle puis attendre les DEUX (le plus courant)
- `wait; echo "tout est fini"` — Barrière de synchronisation simple
- `wait -n; rc=$?` — Attendre LE PREMIER terminé (bash 4.3+) pour un pool
- `wait $PID` — Attendre un PID précis et son code de sortie
**Origine :** Bourne Shell (1979), POSIX — le « join » des shells, indispensable dès que le `&` apparait.
**Subtilités/confusions :**
- Sans argument, wait attend TOUS les jobs : un job oublié (boucle infinie) bloque le script pour toujours.
- `wait` retourne le code du dernier job attendu ; pour les avoir tous, stocker au fil de l'eau.
- wait ne voit que les enfants du shell courant : pas les processus d'un autre utilisateur ni les démons.
**Urgences/dangers :** ⚠️ `&` + `wait` sans timeout = script bloqué indéfiniment si un enfant reste vivant : ajouter un `timeout`.
**Précautions :** Combiner wait avec `trap` (nettoyage) et limiter le parallélisme (`xargs -P`, jobs -n).
**Équivalents :** Wait-Job (PowerShell), Promise.all (JS), join() (threads)
**Voir aussi :** jobs, nohup, timeout, xargs

## `yes` — Répéter une chaîne à l'infini [Linux/macOS]
**Niveau :** debutant | **Popularité :** 40 | **Aliases :** —
**Contextes :** répondre « oui » automatiquement à un prompt, générer des données de test, stresser un pipe
**Rôle :** Écrire en boucle une chaîne (par défaut `y`) suivie d'un saut de ligne, jusqu'à sa propre mort.
**Syntaxe :** `yes [chaîne]`
**Cas réguliers :**
- `yes | cp -i f* dir/` — Répondre oui à toutes les confirmations (le plus courant)
- `yes "ok" | head -5` — Générer 5 lignes de test (toujours borné par head)
- `yes | script.sh --assume` — Automatiser un outil interactif
- `yes > /dev/null` — Stress CPU (test de chauffe, 1 cœur à 100 %)
**Origine :** GNU coreutils (1991, par David MacKenzie) — l'outil des scripts d'installation non interactifs de l'ère des floppy disks.
**Subtilités/confusions :**
- yes consomme 100 % d'un CPU en écrivant sur un pipe bouché : le borner avec `head` ou une redirection.
- Mieux que yes : l'option `--yes`/`-y` native des gestionnaires (`apt-get -y`, `npm -y`) — plus sûr et plus lisible.
- `yes n` répond non aux prompts — mais beaucoup d'outils attendent autre chose (« o », « oui », etc.).
**Urgences/dangers :** ⚠️ `yes | rm -r ...` ou `yes | fdisk` : automatiser un OUI à une commande destructive = catastrophe silencieuse.
**Précautions :** Préférer les options de contournement (`--assume-yes`) ; ne jamais piping yes vers un outil destructeur.
**Équivalents :** echo "y" | (une seule réponse), --yes natif des CLI, expect (interaction fine)
**Voir aussi :** tee, head, cp, script














