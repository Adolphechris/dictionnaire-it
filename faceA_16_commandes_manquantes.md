# Face A — Commandes et fichiers manquants (liens voir aussi repares)

## `jq` — Traiter du JSON en ligne de commande [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contexte :** extraire un champ d'une réponse d'API, filtrer une sortie JSON dans un script, reformater un document
**Rôle :** Processeur JSON en ligne de commande : il filtre, transforme et reformate du JSON avec un langage de requêtes compact.
**Syntaxe :** `jq '.items[] | {nom, prix}' fichier.json`
**Cas réguliers :**
- `.champ.sous_champ` — Extraire une valeur en descendant la hiérarchie avec des points
- `.[] | .nom` — Parcourir un tableau et ne garder qu'un champ
- `select(.prix > 10)` — Filtrer les éléments selon une condition
- `-r` — Sortir en texte brut, sans guillemets JSON ni échappement
- `-c` — Sortie compacte sur une ligne, pratique pour des journaux
**Origine :** Créé par Stephen Dolan en 2012 ; son langage de filtres est devenu un standard de fait pour manipuler du JSON dans un shell.
**Subtilités/confusions :**
- jq manipule des flux : .[] parcourt un tableau, mais appliqué à un objet il parcourt ses valeurs — source de résultats inattendus.
- Sans -r, les chaînes ressortent entre guillemets JSON, ce qui casse les scripts qui réutilisent la valeur directement.
- Erreur classique : passer le filtre sans guillemets, le shell l'interprète alors lui-même (étoiles, espaces, parenthèses).
**Urgences/dangers :** ⚠️ Sur un très gros document, jq charge tout en mémoire : une boucle sur un fichier volumineux peut saturer la RAM de la machine.
**Précautions :** Valider le filtre sur un échantillon, préférer -r dans les scripts, prévoir un défaut pour les valeurs nulles et vérifier systématiquement le code retour.
**Équivalents :** yq (YAML/JSON), fx, python -m json.tool, jid
**Voir aussi :** yq, fx, JSON, curl, API REST, pup

## `python` — Interpréteur du langage Python [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** python3, CPython
**Contexte :** exécuter un script, évaluer une expression, créer un environnement virtuel, lancer un serveur de test
**Rôle :** Interpréteur du langage Python : il exécute un script, une expression courte ou ouvre une session interactive (REPL).
**Syntaxe :** `python3 script.py [args] / python3 -c 'print(2+2)'`
**Cas réguliers :**
- `python3 script.py` — Exécuter un fichier de script
- `python3 -c 'print(2+2)'` — Évaluer une expression sans créer de fichier
- `python3 -m venv .venv` — Créer un environnement virtuel isolé pour un projet
- `python3 -m http.server 8000` — Servir le dossier courant en HTTP pour un test rapide
- `python3 -i script.py` — Exécuter le script puis laisser la session interactive ouverte pour inspecter
**Origine :** Créé par Guido van Rossum à la fin des années 1980 et publié en 1991 ; Python 3 (2008) est la référence, Python 2 ayant cessé d'être maintenu en 2020.
**Subtilités/confusions :**
- Sur de nombreux systèmes, python désigne encore Python 2 ou n'existe pas : appeler python3 explicitement évite les mauvaises surprises.
- Installer des paquets globalement peut casser le système : chaque projet devrait utiliser son propre environnement virtuel.
- La conversion implicite est interdite (1 + '1' lève une erreur) : les erreurs apparaissent à l'exécution, pas à la compilation — d'où l'intérêt des tests.
**Urgences/dangers :** ⚠️ Un sudo pip install à la place du gestionnaire de paquets peut remplacer des bibliothèques utilisées par le système et rendre des outils inopérants.
**Précautions :** Créer un environnement virtuel par projet, épingler les dépendances (requirements.txt ou pyproject.toml) et réserver pipx aux outils en ligne de commande.
**Équivalents :** ipython (REPL enrichi), pypy (compilation JIT), node (autre écosystème)
**Voir aussi :** venv, pip, pipx, conda, uv, poetry, pyenv, jq

## `node` — Exécuter du JavaScript côté serveur [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** node.js, NodeJS
**Contexte :** exécuter du JavaScript hors navigateur, lancer un serveur de développement, tester un extrait de code
**Rôle :** Environnement d'exécution JavaScript fondé sur le moteur V8, qui exécute un fichier, un module ou une session interactive.
**Syntaxe :** `node app.js / node -e "console.log(process.version)" / node -v`
**Cas réguliers :**
- `node app.js` — Exécuter un script ou un serveur
- `node -e '...'` — Évaluer du code sans créer de fichier, pour un test rapide
- `node --inspect app.js` — Activer le débogueur (Chrome DevTools ou VS Code)
- `node -p 'process.memoryUsage()'` — Afficher le résultat d'une expression
- `node --test` — Lancer les tests natifs (Node 18 et suivants)
**Origine :** Créé par Ryan Dahl en 2009 en associant le moteur V8 de Google à une boucle d'événements non bloquante ; il a popularisé les entrées-sorties asynchrones côté serveur.
**Subtilités/confusions :**
- JavaScript s'exécute dans un seul thread : la concurrence vient des E/S asynchrones, pas du parallélisme — un calcul lourd bloque tout le processus.
- node_modules n'est pas versionné : il se reconstruit avec npm ci (ou yarn/pnpm) à partir du fichier de verrouillage.
- Changer de version majeure de Node impose souvent de réinstaller les dépendances natives : figer la version via .nvmrc.
**Urgences/dangers :** ⚠️ npm install exécute les scripts post-install déclarés par les paquets : installer une dépendance inconnue revient à exécuter du code arbitraire.
**Précautions :** Épingler la version de Node (.nvmrc), verrouiller les dépendances (package-lock.json), auditer (npm audit) et écarter les paquets non maintenus.
**Équivalents :** deno (sécurisé par défaut), bun, QuickJS, python (autre écosystème)
**Voir aussi :** npm, npx, nvm, yarn, pnpm, bun, fnm, nodenv, JS

## `java` — Lancer une application Java [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** JRE, JVM
**Contexte :** lancer une application Java, vérifier la version du JRE, exécuter une archive jar
**Rôle :** Lanceur de la machine virtuelle Java : il exécute une classe compilée ou une archive .jar sur un JRE installé.
**Syntaxe :** `java -jar application.jar / java -version`
**Cas réguliers :**
- `java -version` — Afficher la version et le fournisseur du JRE utilisé
- `java -jar app.jar` — Exécuter une application empaquetée en archive exécutable
- `java -cp build/classes fr.exemple.Main` — Lancer une classe en précisant le chemin de classes
- `java -Xmx2g -jar app.jar` — Fixer la mémoire maximale du tas Java à 2 Go
- `java -Dspring.profiles.active=prod -jar app.jar` — Passer une propriété système à l'application
**Origine :** Conçu par James Gosling chez Sun Microsystems (projet Oak, 1991) et publié en 1995 ; le slogan 'write once, run anywhere' repose sur la machine virtuelle.
**Subtilités/confusions :**
- JRE, JDK et JVM ne sont pas synonymes : le JRE exécute, le JDK compile et outille, la JVM est la machine virtuelle qui interprète le bytecode.
- Plusieurs versions de Java coexistent souvent : java, javac et JAVA_HOME doivent pointer vers la même installation, sinon les erreurs de classe sont déroutantes.
- Une limite de tas trop basse (-Xmx256m) provoque OutOfMemoryError alors que la machine a de la mémoire libre : la limite est celle de la JVM.
**Urgences/dangers :** ⚠️ Un jar non vérifié lancé avec java -jar exécute du code arbitraire avec les droits de l'utilisateur : ne jamais lancer un artefact de provenance inconnue.
**Précautions :** Épingler la version (JAVA_HOME, sdkman, jenv), surveiller l'usage du tas et du ramasse-miettes, et rester sur des versions LTS maintenues.
**Équivalents :** javac (compilateur), kotlin, scala, node (autre écosystème)
**Voir aussi :** javac, maven, gradle, sdkman, jenv

## `venv` — Environnement virtuel Python [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** virtualenv, env Python
**Contexte :** isoler les dépendances d'un projet Python, éviter de polluer le système, reproduire un environnement à l'identique
**Rôle :** Module de la bibliothèque standard Python (3.3 et suivants) qui crée un dossier d'environnement virtuel doté de son propre interpréteur et de ses propres paquets.
**Syntaxe :** `python3 -m venv .venv && source .venv/bin/activate`
**Cas réguliers :**
- `python3 -m venv .venv` — Créer l'environnement dans le dossier .venv (à ignorer dans git)
- `source .venv/bin/activate` — Activer l'environnement sous Linux et macOS
- `.venv/Scripts/activate` — Script d'activation équivalent sous Windows (cmd ou PowerShell)
- `deactivate` — Quitter l'environnement et revenir au Python système
- `python3 -m venv --system-site-packages .venv` — Autoriser en plus l'accès aux paquets installés globalement
**Origine :** Ajouté à la bibliothèque standard en Python 3.3 (2012) pour remplacer progressivement virtualenv (Ian Bicking, 2007) ; pip et setuptools y sont installés par défaut.
**Subtilités/confusions :**
- venv et virtualenv remplissent le même rôle : virtualenv est plus ancien et propose des options supplémentaires, venv est fourni avec Python.
- L'activation ne vaut que pour le terminal courant : un script lancé ailleurs utilise le Python système s'il n'active pas l'environnement explicitement.
- Le dossier de l'environnement ne doit pas être versionné : il contient des chemins absolus et doit être recréé sur chaque machine.
**Urgences/dangers :** ⚠️ Un environnement virtuel copié ou déplacé vers une autre machine ne fonctionne plus (chemins et binaires absolus) : le recréer plutôt que le copier.
**Précautions :** Épingler les dépendances (requirements.txt, pip freeze) et ignorer le dossier dans .gitignore ; sur les projets modernes, préférer uv ou poetry avec pyproject.toml.
**Équivalents :** virtualenv, conda (environnements et binaires), uv (création très rapide), poetry
**Voir aussi :** python, pip, pipx, pyenv, uv, conda, poetry, .gitignore

## `tmux` — Multiplexeur de terminaux [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** —
**Contexte :** garder une session de travail sur un serveur distant, organiser plusieurs terminaux, lancer un processus long qui survit à la déconnexion
**Rôle :** Multiplexeur de terminaux : il maintient des sessions détachables contenant plusieurs fenêtres et panneaux, indépendamment de la connexion SSH.
**Syntaxe :** `tmux new -s travail / tmux attach -t travail`
**Cas réguliers :**
- `tmux new -s travail` — Créer une session nommée, identifiable ensuite
- `tmux attach -t travail` — Se rattacher à une session après une déconnexion
- `Ctrl+b c puis Ctrl+b n` — Créer une fenêtre et passer à la suivante (préfixe par défaut Ctrl+b)
- `Ctrl+b d` — Détacher la session en laissant les programmes tourner
- `Ctrl+b %` — Diviser le panneau verticalement (" pour horizontal)
**Origine :** Écrit par Nicholas Marriott en 2007 comme alternative moderne, sous licence ISC, à GNU Screen (1987).
**Subtilités/confusions :**
- Détacher une session (Ctrl+b d) n'arrête rien : le programme continue tant que la session vit, contrairement à nohup qui perd l'interaction.
- Screen et tmux ne partagent ni configuration ni protocole : une session tmux n'est pas accessible depuis screen et inversement.
- Le préfixe Ctrl+b entre en conflit avec certains raccourcis d'éditeur : beaucoup de configurations le remplacent par Ctrl+a.
**Urgences/dangers :** ⚠️ Une session tuée (kill-session) ou un redémarrage de machine arrête tout ce qui y tourne : ne pas y faire tourner un service critique sans supervision.
**Précautions :** Nommer les sessions, choisir un préfixe sans conflit, fermer les sessions inutilisées et confier les services durables à systemd plutôt qu'à une session tmux.
**Équivalents :** GNU Screen, byobu (surcouche), zellij
**Voir aussi :** screen, nohup, fg, bg, disown, jobs, ssh, systemd

## `dd` — Copie bloc par bloc [Linux/macOS]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contexte :** écrire une image ISO sur une clé USB, cloner un disque, tester les performances d'écriture, créer un fichier de test
**Rôle :** Copie brute bloc par bloc entre un fichier, un périphérique ou un flux, avec contrôle de la taille de bloc et de la conversion des données.
**Syntaxe :** `dd if=image.iso of=/dev/sdX bs=4M status=progress conv=fsync`
**Cas réguliers :**
- `dd if=image.iso of=/dev/sdb bs=4M status=progress` — Écrire une image sur une clé USB (vérifier la cible avec lsblk avant)
- `dd if=/dev/zero of=test.img bs=1M count=1024` — Créer un fichier de 1 Gio pour un test
- `dd if=/dev/sda of=sauvegarde.img bs=64K conv=noerror,sync` — Cloner un disque en poursuivant malgré les erreurs de lecture
- `dd if=/dev/urandom of=/dev/sdX bs=4M` — Effacer un disque de façon irréversible
**Origine :** Présent dès Unix V5 (1974) ; le nom vient de l'instruction DD du langage JCL d'IBM (Data Definition), et non de 'disk destroyer', surnom mérité par ses effets.
**Subtilités/confusions :**
- dd ne demande aucune confirmation : intervertir if et of écrase les données du disque cible en une seconde.
- La taille de bloc (bs) influence fortement le débit : quelques mégaoctets valent bien mieux que la valeur par défaut de 512 octets.
- Sans status=progress, dd n'affiche rien pendant plusieurs minutes et semble bloqué alors qu'il travaille.
**Urgences/dangers :** ⚠️ `dd of=/dev/sda` mal ciblé peut détruire le disque système : identifier la cible par sa taille ou son UUID (lsblk, blkid) avant d'appuyer sur Entrée.
**Précautions :** Toujours vérifier le périphérique cible, utiliser status=progress et conv=fsync pour garantir l'écriture, et tester d'abord sur un fichier image.
**Équivalents :** cat (images simples), cp, ddrescue (récupération), cp --reflink
**Voir aussi :** lsblk, blkid, truncate, shred, mount, sync, mkfs

## `ffmpeg` — Convertir de l'audio et de la vidéo [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contexte :** convertir une vidéo ou un audio, extraire une piste, compresser un fichier trop lourd, générer des imagettes
**Rôle :** Boîte à outils multimédia en ligne de commande : elle décode, filtre, encode, découpe et remuxe presque tous les formats audio et vidéo.
**Syntaxe :** `ffmpeg -i entree.mp4 -c:v libx264 -crf 23 sortie.mp4`
**Cas réguliers :**
- `ffmpeg -i in.mkv -c copy out.mp4` — Remuxer sans réencoder : très rapide et sans perte de qualité
- `ffmpeg -i in.mp4 -vf scale=1280:-1 -crf 23 out.mp4` — Redimensionner et compresser en conservant les proportions
- `ffmpeg -ss 00:01:30 -t 30 -i in.mp4 -c copy extrait.mp4` — Extraire 30 secondes à partir d'une position donnée
- `ffmpeg -i in.mp4 -vn -acodec copy audio.m4a` — Extraire la piste audio sans la réencoder
- `ffmpeg -i video.mp4 -vf fps=1 img_%03d.png` — Générer une imagette par seconde
**Origine :** Créé par Fabrice Bellard en 2000, développé depuis par la communauté FFmpeg ; il sert de moteur à une grande partie des outils et plateformes multimédias.
**Subtilités/confusions :**
- Réencoder dégrade la qualité et prend du temps : quand les conteneurs le permettent, -c copy copie les flux tels quels.
- L'ordre des options compte : -ss placé avant -i est beaucoup plus rapide (recherche dans l'index) qu'après.
- Sans -crf ni débit explicite, un encodage x264 produit un fichier énorme : augmenter la valeur de -crf réduit fortement la taille sans différence visible.
**Urgences/dangers :** ⚠️ Un réencodage long sature tous les cœurs d'un serveur de production : limiter avec -threads ou planifier la tâche hors des heures de pointe.
**Précautions :** Travailler sur une copie, vérifier le résultat (durée, pistes, sous-titres) avant de remplacer l'original et conserver les sources si la conversion est destructive.
**Équivalents :** avconv (fork historique), HandBrakeCLI, mencoder (obsolète)
**Voir aussi :** MP4, MKV, H.264, H.265, AAC, FLAC, HLS, DASH, WEBM

## `ipconfig` — Configuration réseau IP [Windows]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** afficher l'adresse IP, le masque et la passerelle sous Windows, renouveler le bail DHCP, vider le cache DNS local
**Rôle :** Affiche et gère la configuration réseau des cartes IP sous Windows (adresse IP, masque, passerelle, bail DHCP et cache DNS).
**Syntaxe :** `ipconfig [/all | /flushdns | /release | /renew]`
**Cas réguliers :**
- `ipconfig /all` — Affiche la configuration réseau détaillée de toutes les cartes réseau (MAC, DHCP, DNS)
- `ipconfig /flushdns` — Vide le cache de résolution DNS local de Windows
- `ipconfig /release && ipconfig /renew` — Libère et renouvelle le bail DHCP de la carte réseau active
**Origine :** Utilitaire natif développé par Microsoft pour les systèmes d'exploitation Windows NT et suivants.
**Subtilités/confusions :**
- `ipconfig` est spécifique à Windows ; sur Linux et macOS, les équivalents sont `ip` ou `ifconfig`.
- Ne résout pas les problèmes de routage physique ou de pare-feu : il se limite à l'affichage et la réinitialisation de la couche IP du client.
**Urgences/dangers :** —
**Précautions :** Exécuter dans un terminal PowerShell ou CMD avec les privilèges d'administrateur pour renouveler les baux d'interfaces complexes.
**Équivalents :** ip (Linux), ifconfig (macOS/Unix), Get-NetIPAddress (PowerShell)
**Voir aussi :** ip, ifconfig, ping, nslookup, DHCP, DNS

## `who` — Utilisateurs connectés [Linux/macOS]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** —
**Contextes :** savoir qui est actuellement connecté sur le système, identifier les terminaux et l'heure de connexion
**Rôle :** Affiche la liste des utilisateurs actuellement connectés sur la machine avec le nom de terminal et la date de session.
**Syntaxe :** `who [options] [fichier]`
**Cas réguliers :**
- `who` — Affiche les utilisateurs connectés, leur pseudo, leur terminal (pts/0, tty1) et leur date de connexion
- `who -b` — Affiche la date et l'heure du dernier démarrage (boot) du système
- `who am i` — Affiche uniquement les informations de la session utilisateur courante
**Origine :** Présent dans la première version d'Unix AT&T (1971) et formalisé dans la norme POSIX.
**Subtilités/confusions :**
- `who` donne uniquement la liste des utilisateurs connectés ; `w` donne la même liste augmentée des commandes en cours d'exécution.
- `whoami` n'affiche que le nom de l'utilisateur courant, sans informations de terminal ni d'horodatage.
**Urgences/dangers :** —
**Précautions :** Surveiller `who` sur les serveurs de production pour détecter des connexions concurrentes suspectes.
**Équivalents :** w, whoami, id, last
**Voir aussi :** w, whoami, id, last, loginctl

## `w` — Utilisateurs et activités en cours [Linux/macOS]
**Niveau :** debutant | **Popularité :** 84 | **Aliases :** —
**Contextes :** surveiller les sessions actives, connaître la charge système et savoir quelle commande chaque utilisateur exécute
**Rôle :** Affiche l'uptime, la charge moyenne et la liste des utilisateurs connectés avec les processus qu'ils exécutent.
**Syntaxe :** `w [options] [user]`
**Cas réguliers :**
- `w` — Affiche l'en-tête de charge système (load average) et la table des sessions avec la commande courante (WHAT)
- `w adolphe` — Filtre l'affichage sur le seul utilisateur adolphe
- `w -h` — Masque l'en-tête pour faciliter le traitement dans un script
**Origine :** Écrit par Mark Horton pour BSD 3.0 (1980), intègre ensuite à toutes les distributions Linux/Unix.
**Subtilités/confusions :**
- La colonne `WHAT` affiche la ligne de commande du processus de premier plan exécuté par la session.
- La colonne `IDLE` indique le temps écoulé depuis la dernière interaction clavier de l'utilisateur sur le terminal.
**Urgences/dangers :** —
**Précautions :** Utile lors des interventions de maintenance pour vérifier qu'aucun autre administrateur n'exécute de tâche critique avant un reboot.
**Équivalents :** who, uptime, ps, top
**Voir aussi :** who, whoami, uptime, top, ps

## `tee` — Dupliquer la sortie standard [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** enregistrer les logs d'une commande tout en continuant de les voir à l'écran, écrire dans un fichier protégé via sudo
**Rôle :** Lit l'entrée standard et l'écrit simultanément sur la sortie standard et dans un ou plusieurs fichiers.
**Syntaxe :** `commande | tee [-a] fichier.log`
**Cas réguliers :**
- `echo "127.0.0.1 db" | sudo tee -a /etc/hosts` — Écrit dans un fichier système protégé en contournant les restrictions de redirection bash avec sudo
- `make 2>&1 | tee build.log` — Affiche la compilation en direct dans le terminal tout en l'enregistrant dans build.log
**Origine :** Présent dans Unix Version 6 (1975), son nom s'inspire des raccords en 'T' de la tuyauterie.
**Subtilités/confusions :**
- Sans l'option `-a` (append), `tee` écrase le fichier cible au lieu de s'y ajouter.
- `sudo echo "text" > /etc/hosts` échoue avec "Permission denied" car la redirection `>` est faite par le shell non-root ; `sudo tee` résout le problème.
**Urgences/dangers :** —
**Précautions :** Toujours utiliser `-a` quand on souhaite compléter un fichier journal sans écraser son historique existant.
**Équivalents :** redirection `>>` (sans affichage écran), script (capture de session)
**Voir aussi :** echo, cat, Redirection, sudo, script

## `sync` — Vider les tampons de disque [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** forcer l'écriture physique des données de la RAM vers le disque, préparer l'extinction d'un serveur ou le retrait d'une clé USB
**Rôle :** Force le noyau à vider tous les tampons de mémoire cache d'écriture (write buffers) vers le stockage physique.
**Syntaxe :** `sync [options] [fichier...]`
**Cas réguliers :**
- `sync` — Force le vidage de tous les tampons de tous les systèmes de fichiers montés
- `sync /media/usb` — Synchronise uniquement les tampons associés au point de montage spécifié
- `sync --data fichier.txt` — Force l'écriture des données d'un fichier spécifique sans forcer toutes les métadonnées
**Origine :** Présent depuis la première version d'Unix AT&T (1971) ; traditionnel dans les rituels d'arrêt système ("sync; sync; shutdown").
**Subtilités/confusions :**
- Le retour de la commande `sync` garantit que toutes les écritures en attente sont physiquement remises au stockage.
- Indispensable avant de débrancher une clé USB écrite avec `dd` ou `cp` sans passer par un démontage propre (`umount`).
**Urgences/dangers :** —
**Précautions :** Exécuter `sync` avant d'éteindre brutalement une machine virtuelle ou un serveur de test sans passer par shutdown.
**Équivalents :** umount (qui appelle sync automatiquement), fsync(2) (appel système)
**Voir aussi :** dd, umount, mount, RAM, Storage

## `rsync` — Synchroniser des fichiers et répertoires [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** faire des sauvegardes incrémentales, synchroniser des dossiers distants via SSH, migrer des données d'un serveur à un autre
**Rôle :** Outil puissant de copie et de synchronisation de fichiers à distance ou en local avec calcul de différence delta pour transférer uniquement les parties modifiées.
**Syntaxe :** `rsync [options] source/ destination/`
**Cas réguliers :**
- `rsync -avz --delete /data/ user@backup:/backup/` — Synchronise un dossier vers un serveur distant via SSH en supprimant les fichiers disparus
- `rsync -avP source.iso dest.iso` — Affiche la progression (`-P`) et permet de reprendre un transfert interrompu (`--partial`)
- `rsync -av --dry-run src/ dst/` — Simule la synchronisation sans modifier aucun fichier à destination
**Origine :** Développé par Andrew Tridgell et Paul Mackerras en 1996, célèbre pour son algorithme d'écart (delta-transfer algorithm).
**Subtilités/confusions :**
- La barre oblique finale est critique : `rsync src/ dst/` copie le CONTENU de src dans dst, alors que `rsync src dst/` copie le DOSSIER src lui-même dans dst.
- `--delete` efface les fichiers du dossier cible s'ils n'existent plus dans la source — toujours tester avec `--dry-run` au préalable.
**Urgences/dangers :** ⚠️ Une mauvaise syntaxe avec l'option `--delete` peut effacer par mégarde l'intégralité d'un dossier de destination critique.
**Précautions :** Toujours valider une nouvelle commande rsync avec `--dry-run` (`-n`) avant d'exécuter la synchronisation réelle.
**Équivalents :** scp (copie simple), rclone (cloud), robocopy (Windows)
**Voir aussi :** scp, sftp, SSH, tar, Cron, backup

## `fuser` — Identifier les processus utilisant un fichier [Linux]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** débloquer un point de montage impossible à démonter, trouver quel processus verrouille un fichier ou un port réseau
**Rôle :** Affiche les PIDs des processus qui utilisent un fichier, un répertoire ou un socket réseau spécifié.
**Syntaxe :** `fuser [options] <fichier|dossier|port>`
**Cas réguliers :**
- `fuser -v /mnt/usb` — Affiche sous forme détaillée la liste des processus utilisant le point de montage /mnt/usb
- `fuser 80/tcp` — Identifie le processus qui occupe le port TCP 80
- `fuser -k -9 /mnt/usb` — Tue immédiatement (`kill -9`) tous les processus qui bloquent le démontage du dossier
**Origine :** Utilitaire traditionnel Unix System V, intègre dans le paquet `psmisc` sous Linux.
**Subtilités/confusions :**
- Utile pour résoudre les erreurs "device is busy" lors de l'exécution de `umount`.
- `lsof` donne une vue plus exhaustive des fichiers ouverts, mais `fuser` permet d'exécuter l'action de kill directement (`-k`).
**Urgences/dangers :** ⚠️ L'option `-k` (kill) peut tuer des processus système vitaux si le chemin ciblé est mal configuré.
**Précautions :** Inspecter d'abord les processus avec `fuser -v` avant de décider d'utiliser l'option de nettoyage `-k`.
**Équivalents :** lsof, ss, killall
**Voir aussi :** lsof, umount, kill, ps, ss

## `objdump` — Inspecter les fichiers objets et binaires [Linux]
**Niveau :** expert | **Popularité :** 76 | **Aliases :** —
**Contextes :** ingénierie inverse, débogage bas niveau, inspection du code assembleur d'un exécutable ELF, analyse de sécurité
**Rôle :** Affiche les informations détaillées d'un fichier binaire ou objet (en-têtes, sections, instructions désassemblées).
**Syntaxe :** `objdump [options] <fichier-binaire>`
**Cas réguliers :**
- `objdump -d binaire` — Désassemble les sections d'instructions exécutables du binaire en langage assembleur
- `objdump -x binaire` — Affiche tous les en-têtes et la table des symboles du fichier ELF
- `objdump -M intel -d binaire` — Affiche le désassemblage avec la syntaxe Intel plutôt qu'AT&T
**Origine :** Fait partie de la suite d'outils GNU Binutils développée par la Free Software Foundation.
**Subtilités/confusions :**
- Nécessite un fichier au format binaire (ELF sous Linux, PE sous Windows) — ne fonctionne pas sur des scripts texte.
- Si le binaire est strippé (symboles retirés), les noms de fonctions apparaissent sous forme d'adresses brutes.
**Urgences/dangers :** —
**Précautions :** Combiner avec `gdb` ou `radare2` pour une analyse dynamique interactive des binaires complexes.
**Équivalents :** readelf, nm, gdb, radare2
**Voir aussi :** readelf, nm, gdb, gcc, clang
