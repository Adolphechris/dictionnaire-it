# Face A — ARCHIVES ET COMPRESSION (fiches riches v3 — 40 visées, lot 1 : 8)

## `tar` — Archiver et compresser des dossiers [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** sauvegarde serveur, distribution logicielle, backup avant migration, envoi de projet
**Rôle :** Créer, lister et extraire des archives (souvent compressées en .tar.gz).
**Syntaxe :** `tar [options] <archive> <fichiers>`
**Cas réguliers :**
- `tar -czf backup.tar.gz dossier/` — Sauvegarde compressée du dossier (backup quotidien, le plus courant)
- `tar -tzf backup.tar.gz` — Lister le contenu SANS extraire (vérification avant restauration)
- `tar -xzf backup.tar.gz -C /tmp/resto` — Extraire dans un dossier cible précis
- `tar -czf site-$(date +%F).tar.gz /var/www` — Backup daté d'un site web
**Origine :** Tape ARchive, Unix V7 (1979), bandes magnétiques ; devenu standard POSIX, omniprésent sur serveurs.
**Subtilités/confusions :**
- Sans -z/-j/-J, tar ne compresse PAS, il concatène seulement (archive .tar non compressée).
- tar vs zip : tar préserve permissions et liens Unix, zip non — préférer tar sur Linux.
- `-f` doit être immédiatement suivi du nom d'archive : `tar -czf arc.tar.gz` OK, `tar -cfz` piégeux.
- c=create, x=extract, t=list, z=gzip, j=bzip2, J=xz — un seul de c/x/t à la fois.
**Urgences/dangers :** ⚠️ `tar -xzf arc -C /` écrase le système — toujours lister avec -t avant d'extraire une archive inconnue.
**Précautions :** Vérifier la taille et le contenu avec `tar -tzf` avant extraction.
**Équivalents :** Compress-Archive (PowerShell), 7z (Windows)
**Voir aussi :** gzip, gunzip, zip, unzip, rsync

## `gzip` — Compresser un fichier avec gzip [Linux/macOS]
**Niveau :** debutant | **Popularité :** 80 | **Aliases :** —
**Contextes :** compression de logs, préparation d'archive tar.gz, économie d'espace disque
**Rôle :** Compresser un fichier (remplace l'original par .gz) et décompresser avec gunzip.
**Syntaxe :** `gzip [options] <fichier>`
**Cas réguliers :**
- `gzip acces.log` — Compresse le log (devient acces.log.gz, le plus courant en rotation de logs)
- `gzip -k rapport.csv` — Compresse en gardant l'original (-k = keep)
- `gzip -9 dump.sql` — Compression maximale pour archivage
**Origine :** GNU zip, 1992 (Deutsch/Gailly), successeur libre de compress ; algorithme DEFLATE, standard du web.
**Subtilités/confusions :**
- gzip écrase l'original par défaut — utiliser -k pour le garder.
- gzip = 1 seul fichier ; pour un dossier passer par tar (tar.gz).
- gzip vs bzip2 vs xz : gzip rapide, xz compresse mieux mais lent.
**Urgences/dangers :** — (écrase l'original mais c'est réversible avec gunzip, pas de danger système)
**Précautions :** Ajouter -k si l'original doit être conservé.
**Équivalents :** Compress-Archive (PowerShell)
**Voir aussi :** gunzip, tar, bzip2, xz

## `zip` — Créer des archives ZIP portables [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** envoi par e-mail, partage Windows-Linux, distribution multi-OS
**Rôle :** Créer des archives .zip lisibles partout (Windows, macOS, Linux).
**Syntaxe :** `zip [options] <archive.zip> <fichiers>`
**Cas réguliers :**
- `zip -r projet.zip projet/` — Zip récursif d'un dossier (le plus courant)
- `zip livrable.zip *.pdf` — Zip de fichiers précis pour envoi
- `zip -e secret.zip contrats/` — Archive chiffrée par mot de passe
**Origine :** Phil Katz, PKZIP 1989 (DOS) ; format devenu standard universel, intégré à Windows et macOS.
**Subtilités/confusions :**
- Oublier -r sur un dossier ne zippe que les fichiers racine, pas le contenu.
- zip vs tar.gz : zip portable multi-OS mais perd les permissions Unix — tar.gz sur serveurs Linux.
- -e chiffre faiblement (ZipCrypto) — pour du sensible préférer 7z AES-256.
**Urgences/dangers :** — (pas destructif ; attention aux mots de passe faibles avec -e)
**Précautions :** Toujours -r pour les dossiers ; vérifier avec `unzip -l`.
**Équivalents :** Compress-Archive (PowerShell), 7z (Windows)
**Voir aussi :** unzip, tar, 7z

## `apt` — Gérer les paquets sur Debian/Ubuntu [Linux]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** apt-get, apt-cache
**Contextes :** installation logicielle, mise à jour serveur Ubuntu/Debian, provisioning
**Rôle :** Installer, mettre à jour et supprimer les logiciels (.deb) depuis les dépôts.
**Syntaxe :** `sudo apt [update|upgrade|install|remove] [paquet]`
**Cas réguliers :**
- `sudo apt update && sudo apt upgrade -y` — Mise à jour complète du système (le rituel hebdo)
- `sudo apt install nginx` — Installer un logiciel depuis les dépôts
- `sudo apt remove --purge apache2` — Désinstaller + purger la configuration
- `apt search postgres` — Chercher un paquet disponible
**Origine :** Advanced Package Tool, Debian 1998 ; `apt` moderne (2014) fusionne apt-get/apt-cache en interface conviviale.
**Subtilités/confusions :**
- update ≠ upgrade : update recharge la LISTE, upgrade installe les MAJ — faire les deux dans l'ordre.
- apt vs apt-get : apt pour l'humain (barre de progression), apt-get pour les scripts (stable).
- remove garde la config, purge l'efface ; autoremove nettoie les dépendances orphelines.
**Urgences/dangers :** ⚠️ `apt upgrade` sur un serveur de prod sans snapshot peut casser un service — tester d'abord, upgrader en heure creuse.
**Précautions :** Toujours `update` avant `install` ; lire ce qui sera supprimé avant de valider.
**Équivalents :** yum/dnf (Fedora), pacman (Arch), brew (macOS)
**Voir aussi :** dpkg, snap, yum, brew

## `unzip` — Extraire une archive ZIP [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 85 | **Aliases :** —
**Contextes :** réception d'un livrable, déploiement d'un plugin, extraction de pièce jointe
**Rôle :** Extraire le contenu d'une archive .zip, lister ou tester son intégrité.
**Syntaxe :** `unzip [options] <archive.zip> [-d <dossier>]`
**Cas réguliers :**
- `unzip livrable.zip` — Extrait dans le dossier courant (le plus courant)
- `unzip livrable.zip -d /tmp/depot` — Extrait dans un dossier cible propre
- `unzip -l livrable.zip` — Liste le contenu SANS extraire (vérification)
- `unzip -q gros.zip` — Extraction silencieuse pour les scripts
**Origine :** Info-ZIP, 1989, compagnon libre de zip ; préinstallé sur la plupart des Linux et macOS.
**Subtilités/confusions :**
- Sans -d tout part dans le dossier courant et peut l'inonder — préférer -d.
- unzip vs tar -xzf : unzip pour .zip, tar pour .tar.gz — extensions différentes.
- Fichier avec mot de passe : `unzip -P motdepasse secret.zip` (le mot de passe reste visible dans l'historique).
**Urgences/dangers :** ⚠️ Zip Slip : une archive piégée peut écrire hors du dossier — toujours lister avec -l avant sur une archive inconnue.
**Précautions :** Lister avec -l avant d'extraire ; extraire dans un dossier dédié avec -d.
**Équivalents :** Expand-Archive (PowerShell)
**Voir aussi :** zip, tar, 7z

## `brew` — Gérer les paquets sur macOS [macOS]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** Homebrew
**Contextes :** poste développeur Mac, installation d'outils open source, environnement de dev
**Rôle :** Installer et mettre à jour logiciels et outils absents du Mac par défaut.
**Syntaxe :** `brew [install|upgrade|search|list] [formule]`
**Cas réguliers :**
- `brew install git` — Installer un outil manquant (le plus courant sur Mac neuf)
- `brew upgrade` — Tout mettre à jour (rituel hebdo)
- `brew search postgres` — Chercher un paquet
- `brew list` — Voir ce qui est installé
**Origine :** Homebrew, Max Howell 2009 ; devenu le gestionnaire de facto sur macOS ("le chaînon manquant d'Apple").
**Subtilités/confusions :**
- brew = outils en ligne de commande ; `brew install --cask` = vraies apps GUI (VS Code, Docker Desktop).
- Pas de sudo avec brew — il installe dans /opt/homebrew, jamais en root.
- brew vs MacPorts : brew plus simple et populaire, MacPorts plus isolé.
**Urgences/dangers :** — (n'installe qu'en espace utilisateur ; un `brew upgrade` peut changer une version d'outil et casser un projet — épingler avec `brew pin` si critique)
**Précautions :** `brew update` avant `brew upgrade` ; vérifier `brew doctor` si ça coince.
**Équivalents :** apt (Debian/Ubuntu), winget/choco (Windows)
**Voir aussi :** apt, winget, mas

