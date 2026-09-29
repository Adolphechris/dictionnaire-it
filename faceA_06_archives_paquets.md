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

## `gunzip` — Décompresser un fichier .gz [Linux/macOS]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** gzip -d
**Contextes :** restauration de backup, déballage de paquet source, lecture de logs compressés
**Rôle :** Décompresser un fichier .gz (remplace l'archive .gz par le fichier original).
**Syntaxe :** `gunzip [options] <fichier.gz>`
**Cas réguliers :**
- `gunzip acces.log.gz` — Décompresse le log (redevient acces.log, le plus courant)
- `gunzip -k ancien.sql.gz.gz` — Décompresse en gardant le .gz (-k = keep)
- `zcat acces.log.gz | grep error` — Lit SANS décompresser (pipeline direct)
**Origine :** GNU gzip 1992, écrit par Jean-loup Gailly et Mark Adler — c'est la binaison naturelle de gzip.
**Subtilités/confusions :**
- gunzip ne lit pas les .zip ni les .tar.gz complets — pour .tar.gz utiliser tar -xzf directement.
- `-c` ou zcat : lire le contenu décompressé dans le terminal sans toucher au fichier.
- gunzip -f écrase un fichier existant sans avertissement.
**Urgences/dangers :** — (opération réversible ; gunzip -f peut écraser un fichier homonyme existant)
**Précautions :** Vérifier qu'aucun fichier du même nom n'existe déjà (ou utiliser -k).
**Équivalents :** Expand-Archive sur décompressé (PowerShell), 7z x (Windows)
**Voir aussi :** gzip, tar, zcat

## `7z` — Archives 7-Zip haute compression [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 70 | **Aliases :** 7za, p7zip
**Contextes :** archives volumineuses, envoi avec taille limitée, échange Windows-Linux avec chiffrement
**Rôle :** Créer/extraire des archives .7z (compression forte, chiffrement AES-256).
**Syntaxe :** `7z [a|x|l] <archive.7z> <fichiers>`
**Cas réguliers :**
- `7z a -t7z gros.7z dossier/` — Créer une archive 7z compressée au max
- `7z x gros.7z -o/tmp/extraire` — Extraire avec structure complète (-o sans espace !)
- `7z l gros.7z` — Lister le contenu (avant extraction, réflexe sécurité)
- `7z a -p secret.7z contrats/` — Archive chiffrée mot de passe + AES-256
**Origine :** Igor Pavlov, 1999, format ouvert 7z ; sur Linux c'est le paquet p7zip (`7z`).
**Subtilités/confusions :**
- `-o/tmp` sans espace : `7z x -o /tmp` crée un dossier " /tmp" fautif (bug classique).
- 7z vs zip : 7z compresse 30-50% mieux mais moins lisible nativement sur Windows ancien.
- `7z x` préserve les chemins complets, `7z e` extrait à plat — x recommandé.
**Urgences/dangers :** — (non destructif ; le danger vient du -o extrait par-dessus un dossier existant)
**Précautions :** Toujours `7z l` avant `7z x` sur une archive inconnue.
**Équivalents :** zip/unzip, tar, Compress-Archive (PowerShell)
**Voir aussi :** zip, tar, gzip

## `dpkg` — Paquets Debian au niveau bas [Linux]
**Niveau :** avance | **Popularité :** 60 | **Aliases :** —
**Contextes :** installation locale .deb hors dépôt, débogage de dépendances, scripts d'admin
**Rôle :** Installer/lister/supprimer les paquets .deb directement, sans gestion des dépendances.
**Syntaxe:** `sudo dpkg [ -i|-l|-r ] <paquet.deb|nom>`
**Cas réguliers :**
- `sudo dpkg -i outil.deb` — Installe un .deb téléchargé (le plus courant : driver, .deb maison)
- `dpkg -l | grep nginx` — Lister les paquets installés filtrés
- `sudo apt --fix-broken install` — Réparer après un dpkg -i qui a échoué sur une dépendance
**Origine :** Debian Package management, 1993, noyau historique de la distribution Debian ; base de RPM.
**Subtilités/confusions :**
- dpkg n'installe PAS les dépendances — d'où les erreurs "dependency problems" → utiliser apt.
- dpkg vs apt : dpkg = bas niveau (local, offline), apt = haut niveau (réseau, résolution).
- dpkg -r supprime le paquet, --purge efface aussi la configuration.
**Urgences/dangers :** ⚠️ `dpkg -r --force-depends` peut casser des paquets qui dépendent de celui-ci — utiliser avec méthode.
**Précautions :** Préférer apt install ./fichier.deb ; réparer avec `apt --fix-broken install`.
**Équivalents :** rpm (Fedora/RHEL), msiexec (Windows)
**Voir aussi :** apt, rpm, snap

## `winget` — Gestionnaire de paquets Windows officiel [Windows]
**Niveau :** debutant | **Popularité :** 78 | **Aliases :** Windows Package Manager
**Contextes :** poste Windows neuf, déploiement de logiciels, automatisation post-réinstallation
**Rôle :** Installer, mettre à jour et trouver des logiciels depuis le terminal Windows officiel.
**Syntaxe :** `winget [install|upgrade|search|uninstall] <paquet>`
**Cas réguliers :**
- `winget install Google.Chrome` — Installer un logiciel sans passer par le navigateur (le plus courant)
- `winget upgrade --all` — Tout mettre à jour
- `winget search vscode` — Chercher un paquet
- `winget export -o apps.json` — Sauvegarder la liste des apps (après réinstallation de Windows)
**Origine :** Microsoft, 2020 (preview), 2021 (stable) — réponse officielle à apt/brew, intégré à Windows 10/11.
**Subtilités/confusions :**
- winget vs Store Microsoft : winget = terminal, Store = GUI ; même source mais winget ouvre tout le catalogue MSI/EXE.
- winget vs choco/Scoop : winget natif (pas d'admin requis en général), choco plus vieux et orienté entreprise.
- Certains paquets installent en machine-wide → demande d'élévation UAC.
**Urgences/dangers :** ⚠️ `winget uninstall` peut retirer une app système si on tape mal — vérifier la liste avec `winget list` avant.
**Précautions :** Toujours `winget search` puis vérifier l'éditeur avant install.
**Équivalents :** apt (Linux), brew (macOS)
**Voir aussi :** choco, scoop, apt, brew

## `yum` / `dnf` — Paquets sur RHEL/CentOS/Fedora [Linux]
**Niveau :** intermediaire | **Popularité :** 65 | **Aliases :** dnf (successeur de yum)
**Contextes :** serveurs d'entreprise RHEL/CentOS/AlmaLinux, poste Fedora, provisioning serveur
**Rôle :** Installer et mettre à jour les paquets .rpm depuis les dépôts (l'équivalent apt des distros Red Hat).
**Syntaxe :** `sudo dnf [install|update|remove|search] <paquet>`
**Cas réguliers :**
- `sudo dnf install nginx` — Installer un service (Fedora/RHEL 8+, le plus courant)
- `sudo dnf update` — Mettre à jour le système complet
- `dnf search mysql` — Chercher un paquet
- `sudo yum install httpd` — Version historique sur CentOS 7 (toujours vu en prod)
**Origine :** Yellowdog Updater Modified (2003, années Yellow Dog), réécrit en Yum (2003) puis remplacé par DNF (2015, Fedora 21) — même public, gestionnaire plus rapide.
**Subtilités/confusions :**
- yum vs dnf : même rôle ; dnf est le successeur (CentOS 8+ / Fedora), yum reste sur CentOS 7.
- .rpm vs .deb : même concept, formats différents — un paquet .deb ne s'installe pas sur RHEL.
- dnf remove ≠ désinstallation complète : `dnf autoremove` nettoie les dépendances orphelines.
**Urgences/dangers :** ⚠️ `dnf update` sur un serveur de prod peut upgrer le kernel et demander un reboot — planifier la fenêtre de maintenance.
**Précautions :** Lire le plan d'update avant valider ; verrouiller les versions critiques (`versionlock`).
**Équivalents :** apt (Debian), zypper (openSUSE), pacman (Arch)
**Voir aussi :** apt, rpm, pacman

## `pacman` — Gestionnaire de paquets Arch Linux [Linux]
**Niveau :** intermediaire | **Popularité :** 55 | **Aliases :** —
**Contextes :** Arch Linux et dérivés (Manjaro, EndeavourOS), poste minimaliste d'experts, AUR
**Rôle :** Installer/gérer les paquets sur Arch — rapide, minimaliste, associé à l'AUR communautaire.
**Syntaxe :** `sudo pacman [-S|-Syu|-R] <paquet>`
**Cas réguliers :**
- `sudo pacman -Syu` — Mise à jour complète système+paquets (obligatoire, les 2 y = sync)
- `sudo pacman -S htop` — Installer un paquet des dépôts officiels
- `paru -S paquet-aur` — Installer depuis l'AUR (helper communautaire)
**Origine :** Judd Vinet, 2002, Arch Linux ; design minimaliste "KISS" — souvent cité comme le gestionnaire le plus rapide.
**Subtilités/confusions :**
- `-Syu` vs `-Sy` : installer -S + -y SANS -u désynchronise les dépôts → CASSE le système (erreur d'Arch classique).
- AUR ≠ dépôt officiel : des PKGBUILDs communautaires, à auditer avant install (risque de code).
- pacman vs apt : pas de "pacman update" séparé — tout passe par -Syu.
**Urgences/dangers :** ⚠️ NE JAMAIS faire `pacman -Sy pkg` sans u (paquets à moitié à jour = breakage). ⚠️ AUR sans vérification = exécution de code inconnu.
**Précautions :** Toujours `-Syu` ; lire le PKGBUILD de l'AUR ; sauvegarder avant grosse maj.
**Équivalents :** apt (Debian), dnf (Fedora), brew (macOS)
**Voir aussi :** apt, dnf, AUR, snap

## `snap` — Paquets universels Linux (Canonical) [Linux]
**Niveau :** intermediaire | **Popularité :** 60 | **Aliases :** Snappy
**Contextes :** Ubuntu, apps multi-distro sans dépendances, logiciels versions récentes sur LTS
**Rôle :** Installer des applications auto-contenues (sandbox) qui tournent partout sur Linux.
**Syntaxe :** `sudo snap [install|refresh|list|remove] <app>`
**Cas réguliers :**
- `sudo snap install code --classic` — VS Code à jour quelle que soit la distro (le plus courant)
- `sudo snap refresh` — Mettre à jour tous les snaps
- `snap list` — Voir les snaps installés
- `sudo snap remove firefox` — Supprimer un snap (souvent préinstallé sur Ubuntu)
**Origine :** Canonical (Ubuntu), 2014-2016 ; packagée comme réponse à Flatpak/Snapcraft, intégrée à Ubuntu 16.04+.
**Subtilités/confusions :**
- snap vs apt : snap = auto-contenu (gros, isolé, toujours à jour), apt = dépendances partagées (léger).
- `--classic` désactive la sandbox — nécessaire pour VS Code mais moins sûr.
- Snap est un daemon en fond (snapd) : peut ralentir le boot et manger du CPU à l'auto-refresh.
**Urgences/dangers :** — (pas destructif ; snap refresh en cours peut bloquer une app 30 secondes)
**Précautions :** Désactiver l'auto-refresh dans les environnements de prod (`snap set system refresh.hold=...`).
**Équivalents :** flatpak (multidistro), apt, brew
**Voir aussi :** flatpak, apt, AppImage

## `flatpak` — Apps universelles Linux (open) [Linux]
**Niveau :** intermediaire | **Popularité :** 55 | **Aliases :** —
**Contextes :** GNOME, Fedora, applications graphiques multi-distro, distribution indépendante des distros
**Rôle :** Installer des applications graphiques auto-contenues et sandboxées, compatibles sur toutes les distros Linux.
**Syntaxe :** `flatpak [install|update|list|run] <app>`
**Cas réguliers :**
- `flatpak install flathub org.gimp.GIMP` — Installer GIMP depuis Flathub (le plus courant)
- `flatpak update` — Tout mettre à jour
- `flatpak run org.mozilla.firefox` — Lancer une app flatpak
- `flatpak uninstall --unused` — Nettoyer les anciennes versions (elles s'accumulent !)
**Origine :** Red Hat + Collabora, 2015-2016 — réponse open à Snap, portée par Flathub (2017) comme magasin unique.
**Subtilités/confusions :**
- flatpak vs Snap : même concept ; flatpak open (Flathub) et plus léger, Snap propre à Canonical.
- Les flatpaks pèsent cher en disque : anciennes versions gardées → `--unused` régulièrement.
- Applications graphiques surtout : outils serveur (nginx...) restent en apt.
**Urgences/dangers :** — (non destructif ; désinstallation massive par erreur avec `flatpak uninstall --all` est possible mais rare)
**Précautions :** Réserver flatpak aux apps graphiques ; nettoyer avec `--unused` après chaque update.
**Équivalents :** snap, AppImage, brew
**Voir aussi :** snap, AppImage, brew

## `rpm` — Paquets bruts RPM [Linux]
**Niveau :** avance | **Popularité :** 50 | **Aliases :** —
**Contextes :** RHEL/CentOS/Fedora/SUSE, installation locale hors dépôt, audits de sécurité
**Rôle :** Installer/interroger individuellement les fichiers .rpm (l'équivalent dpkg côté Red Hat).
**Syntaxe :** `sudo rpm [-i|-q|-e] <paquet.rpm>`
**Cas réguliers :**
- `sudo rpm -i outil.rpm` — Installer un .rpm téléchargé (le plus courant : driver, firmware)
- `rpm -qa | grep kernel` — Lister les paquets installés (audit, nettoyage vieux kernels)
- `rpm -ql paquet` — Voir les fichiers installés par ce paquet
**Origine :** Red Hat Package Manager, 1997 — conçu pour la distribution Red Hat, devenu standard RPM (Fedora, SUSE, openSUSE).
**Subtilités/confusions :**
- rpm vs yum/dnf : rpm = bas niveau local (pas de dépendances), dnf = haut niveau (résout les dépendances).
- rpm -i échoue si dépendance manquante → `dnf install ./fichier.rpm` gère le cas.
- rpm -e désinstalle (erase) : sans vérifier les dépendants, casse les paquets qui en dépendent.
**Urgences/dangers :** ⚠️ `rpm -e --nodeps` casse la cohérence du système — réservé à la dépannage d'expert.
**Précautions :** Préférer dnf même en local ; vérifier `rpm -qR` avant suppression.
**Équivalents :** dpkg (Debian), msiexec (Windows)
**Voir aussi :** dpkg, dnf, yum

## `choco` — Gestionnaire de paquets Windows (Chocolatey) [Windows]
**Niveau :** intermediaire | **Popularité :** 65 | **Aliases :** Chocolatey
**Contextes :** poste Windows pro, déploiement d'outils dev, réinstallation après format
**Rôle :** Installer des logiciels Windows en ligne de commande, par scripts (l'apt de Windows).
**Syntaxe :** `choco [install|upgrade|uninstall] <paquet> [-y]`
**Cas réguliers :**
- `choco install vscode -y` — Installer VS Code sans cliquer (le plus courant)
- `choco upgrade all -y` — Tout mettre à jour
- `choco install python git nodejs -y` — Préparer un poste dev en 1 commande
**Origine :** Rob Reynolds, 2011 (ferventchocolate) — premier gros gestionnaire Windows communautaire, avant l'officiel winget (2020).
**Subtilités/confusions :**
- choco vs winget : choco = plus vieux, catalogue plus large (scripts NuGet) ; winget = officiel Microsoft intégré.
- -y évite les prompts — indispensable en script, sinon l'install s'attend à une validation.
- Les paquets choco exécutent souvent des scripts .ps1 : source de confiance = code exécuté (auditer).
**Urgences/dangers :** ⚠️ `choco uninstall` d'un paquet système mal identifié peut retirer un outil critique — `choco list` d'abord.
**Précautions :** Référencer les paquets nécessaires dans un script de bootstrap ; vérifier les sources.
**Équivalents :** winget, scoop (Windows), apt (Linux)
**Voir aussi :** winget, scoop, apt

## `npm` — Registre et outillage Node.js [Cross/Dev]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** Node Package Manager
**Contextes :** projets JavaScript/TypeScript, front React/Vue, back Node, scripts d'automatisation
**Rôle :** Installer les dépendances d'un projet JS et lancer les scripts définis dans package.json.
**Syntaxe :** `npm [install|i|run|init] <paquet> [--save-dev]`
**Cas réguliers :**
- `npm install` — Installer toutes les dépendances du projet (génère node_modules/ — le plus courant)
- `npm install express --save` — Ajouter une dépendance à package.json
- `npm run dev` — Lancer le script "dev" (watcher, serveur local...)
- `npm init -y` — Créer un package.json minimal
**Origine :** Isaac Z. Schlueter, 2010 chez Joyent — né du besoin de gérer les dépendances de Node.js (2009) ; le registre npm est le plus gros au monde (2M+ paquets).
**Subtilités/confusions :**
- node_modules/ = dents-de-l'âge : jamais commité (ajouter au .gitignore), pesant des Go.
- npm vs yarn vs pnpm : même rôle ; yarn ajoute des locks plus stricts, pnpm déduplique (disque).
- `npm install -g` : global = risque de conflits entre projets — préférer local + npx.
**Urgences/dangers :** ⚠️ `npm install` tire du code de n'importe qui — vérifier le lockfile et éviter les paquets typosquatés (even-node...).
**Précautions :** Commiter package.json + package-lock.json ; régénérer node_modules proprement.
**Équivalents :** pip (Python), maven (Java), yarn, pnpm
**Voir aussi :** node, yarn, pip, git




