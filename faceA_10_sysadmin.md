# Face A — Commandes : ADMINISTRATION SYSTÈME LINUX ET SÉCURITÉ (fiches riches v3)

> Lot MVP #027 — cible 60 fiches. Avancement : 15/60 (bloc 1 Droits, Utilisateurs & Sécurité : chmod, chown, useradd, usermod, userdel, groupadd, passwd, su, sudo, visudo, id, whoami, umask, chgrp, chattr). Format : `## \`commande\` — titre [OS]` + 10 rubriques obligatoires validées par `tools/parse_rich.py`.

## `chmod` — Modifier les permissions d'un fichier [Linux/macOS]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** rendre un script exécutable (`+x`), restreindre l'accès à une clé SSH privée (`600`), sécuriser un dossier web
**Rôle :** Modifier les droits d'accès en lecture (r), écriture (w) et exécution (x) d'un fichier ou répertoire pour le propriétaire, le groupe et les autres.
**Syntaxe :** `chmod [options] <mode> <fichiers>`
**Cas réguliers :**
- `chmod +x script.sh` — Rendre un script exécutable pour tout le monde (le plus courant)
- `chmod 600 ~/.ssh/id_rsa` — Restreindre la clé SSH privée au propriétaire seul (lecture/écriture)
- `chmod 755 /var/www/html` — Accès complet pour le propriétaire, lecture/exécution pour le groupe et les autres
- `chmod -R 750 /opt/app` — Appliquer récursivement les droits à tout un dossier
**Origine :** AT&T Unix (1971) — acronyme de « Change Mode », système de permissions POSIX historique.
**Subtilités/confusions :**
- Deux modes : symbolique (`u+x`, `g-w`, `o=r`) vs octal (`7`=rwx, `6`=rw-, `5`=r-x, `4`=r--, `0`=---).
- Les dossiers exigent le droit d'exécution (`x`) pour pouvoir être traversés (`cd`) et lire leur contenu.
- Le Bit SUID (`chmod u+s`), SGID (`g+s`) et Sticky Bit (`chmod +t` sur `/tmp`) modifient le comportement d'exécution.
**Urgences/dangers :** ⚠️ `chmod -R 777 /` ou `chmod -R 777 var/` détruit la sécurité du système et rend SSH inopérant immédiatement.
**Précautions :** Toujours vérifier les permissions modifiées avec `ls -l` ; ne jamais appliquer `777` en production.
**Équivalents :** icacls (Windows PowerShell/CMD), Set-Acl
**Voir aussi :** chown, umask, ls, chattr
## `chown` — Changer le propriétaire d'un fichier [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** réattribuer un dossier web à l'utilisateur `www-data`, corriger les droits après une copie sous `root`
**Rôle :** Modifier le compte utilisateur et/ou le groupe propriétaire d'un fichier ou d'un répertoire.
**Syntaxe :** `chown [options] [utilisateur][:[groupe]] <fichiers>`
**Cas réguliers :**
- `chown www-data /var/www/html/index.html` — Changer uniquement l'utilisateur propriétaire (le plus courant)
- `chown -R www-data:www-data /var/www/html` — Changer l'utilisateur ET le groupe récursivement sur tout le dossier
- `chown :docker /var/run/docker.sock` — Changer uniquement le groupe propriétaire (raccourci avec `:`)
- `chown --reference=ref.txt cib.txt` — Copier les propriétaires d'un fichier de référence
**Origine :** AT&T Unix (1971) — acronyme de « Change Owner ».
**Subtilités/confusions :**
- Exige généralement les privilèges `root` ou `sudo` pour transférer la propriété d'un fichier à un autre utilisateur.
- Si le groupe est précédé d'un deux-points sans nom (`chown user: file`), le groupe principal de l'utilisateur est attribué.
- L'option `-h` modifie le propriétaire du lien symbolique lui-même au lieu de la cible pointée.
**Urgences/dangers :** ⚠️ `chown -R user:user /` détruit l'arborescence du système d'exploitation et exige une réinstallation.
**Précautions :** Toujours contrôler le chemin cible avant d'exécuter `chown -R` avec les privilèges `sudo`.
**Équivalents :** takeown (Windows CMD), Set-Acl (PowerShell)
**Voir aussi :** chmod, chgrp, id, ls
## `useradd` — Créer un compte utilisateur [Linux]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** adduser (wrapper interactif Debian/Ubuntu)
**Contextes :** provisionner un nouvel accès utilisateur sur un serveur Linux, créer un compte de service applicatif
**Rôle :** Créer un nouveau compte utilisateur système bas niveau en mettant à jour `/etc/passwd`, `/etc/shadow` et `/etc/group`.
**Syntaxe :** `useradd [options] <nom-utilisateur>`
**Cas réguliers :**
- `useradd -m -s /bin/bash adolphe` — Créer l'utilisateur avec son répertoire personnel (`-m`) et son shell par défaut
- `useradd -r -s /usr/sbin/nologin deploy` — Créer un utilisateur système sans dossier home ni accès shell (pour démon)
- `useradd -g devs -G docker,sudo dev1` — Créer l'utilisateur avec groupe principal `devs` et groupes secondaires `docker,sudo`
- `useradd -e 2026-12-31 stagiaire` — Définir une date d'expiration automatique du compte
**Origine :** AT&T System V Unix (1980) — utilitaire standard de gestion des comptes d'administration Linux.
**Subtilités/confusions :**
- `useradd` est la commande bas niveau binaire brute. Sur Debian/Ubuntu, `adduser` est un wrapper interactif convivial plus haut niveau.
- Un utilisateur nouvellement créé avec `useradd` est VERROUILLÉ tant qu'un mot de passe n'a pas été défini via `passwd`.
**Urgences/dangers :** ⚠️ Créer un utilisateur sans spécifier `-s /usr/sbin/nologin` pour un service applicatif lui donne un accès shell interactif inutile.
**Précautions :** Définir un mot de passe immédiatement avec `passwd <utilisateur>` après la création.
**Équivalents :** adduser, New-LocalUser (PowerShell), net user (Windows)
**Voir aussi :** usermod, userdel, passwd, groupadd
## `usermod` — Modifier un compte utilisateur [Linux]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** ajouter un utilisateur au groupe `docker` ou `sudo`, changer le shell par défaut, verrouiller un compte temporaire
**Rôle :** Modifier les paramètres d'un compte utilisateur Linux existant (groupes, shell, dossier personnel, statut).
**Syntaxe :** `usermod [options] <nom-utilisateur>`
**Cas réguliers :**
- `usermod -aG docker adolphe` — Ajouter l'utilisateur au groupe `docker` SANS le retirer de ses autres groupes (le plus courant)
- `usermod -s /bin/zsh adolphe` — Changer le shell de connexion par défaut
- `usermod -L adolphe` — Verrouiller le compte utilisateur (désactive la connexion par mot de passe)
- `usermod -U adolphe` — Déverrouiller le compte utilisateur
**Origine :** AT&T System V Unix (1980) — modification des entrées de la base de comptes Linux.
**Subtilités/confusions :**
- ⚠️ L'option `-G` (groupes secondaires) DOIT TOUJOURS être accompagnée de `-a` (*append*) : faire `usermod -G docker user` retire l'utilisateur de TOUS ses autres groupes (y compris `sudo` !)
- Les modifications de groupes ne prennent effet qu'à la PROCHAINE SESSION (déconnexion/reconnexion nécessaire ou `newgrp`).
**Urgences/dangers :** ⚠️ Oublier `-a` dans `usermod -G` retire l'administrateur du groupe `sudo` et lui fait perdre ses droits root !
**Précautions :** Toujours vérifier avec la commande `id <utilisateur>` après toute modification de groupe.
**Équivalents :** Add-LocalGroupMember (PowerShell), net localgroup (Windows)
**Voir aussi :** useradd, userdel, id, passwd
## `userdel` — Supprimer un compte utilisateur [Linux]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** deluser (wrapper Debian/Ubuntu)
**Contextes :** révoquer l'accès d'un collaborateur ayant quitté l'entreprise, nettoyer des comptes temporaires de test
**Rôle :** Supprimer la fiche d'un compte utilisateur système des fichiers d'administration `/etc/passwd` et `/etc/shadow`.
**Syntaxe :** `userdel [options] <nom-utilisateur>`
**Cas réguliers :**
- `userdel adolphe` — Supprimer le compte utilisateur en conservant son dossier personnel sur le disque (le plus courant)
- `userdel -r adolphe` — Supprimer le compte ET détruire son répertoire personnel (`/home/adolphe`) et sa boîte mail
- `userdel -f adolphe` — Forcer la suppression du compte même si l'utilisateur est actuellement connecté
**Origine :** AT&T System V Unix (1980) — suppression définitive d'un compte utilisateur.
**Subtilités/confusions :**
- Sans l'option `-r`, le dossier `/home/user` reste sur le disque avec un UID numérique orphelin.
- Si des fichiers appartiennent à l'UID supprimé ailleurs sur le disque, ils apparaissent désormais avec un numéro d'UID brut au lieu d'un nom (`ls -l` affichera `1002`).
**Urgences/dangers :** ⚠️ `userdel -r` détruit définitivement tout le dossier `/home/user` et tous les documents personnels de l'utilisateur.
**Précautions :** Archiver le répertoire personnel de l'utilisateur avant d'exécuter `userdel -r`.
**Équivalents :** Remove-LocalUser (PowerShell), net user /delete (Windows)
**Voir aussi :** useradd, usermod, groupdel
## `groupadd` — Créer un groupe d'utilisateurs [Linux]
**Niveau :** debutant | **Popularité :** 84 | **Aliases :** addgroup (wrapper Debian/Ubuntu)
**Contextes :** créer un groupe de partage pour un projet (`sysadmins`, `developers`), organiser les permissions d'accès aux dossiers
**Rôle :** Déclarer un nouveau groupe d'utilisateurs dans la base de sécurité du système (`/etc/group`).
**Syntaxe :** `groupadd [options] <nom-groupe>`
**Cas réguliers :**
- `groupadd developpeurs` — Créer un groupe utilisateur standard (le plus courant)
- `groupadd -r sys_audit` — Créer un groupe système (avec un GID inférieur à 1000)
- `groupadd -g 1500 compta` — Attribuer un identifiant numérique GID spécifique au groupe
**Origine :** AT&T System V Unix (1980) — structuration des rôles et des groupes sous Unix.
**Subtilités/confusions :**
- Un groupe nouvellement créé est vide : il faut y ajouter des membres avec `usermod -aG <groupe> <user>` ou `gpasswd -a`.
- Les GIDs de 0 à 999 sont réservés par convention aux groupes système et démons.
**Urgences/dangers :** — (création d'entrée dans `/etc/group`)
**Précautions :** Adopter une convention de nommage claire et en minuscules pour les groupes d'entreprise.
**Équivalents :** New-LocalGroup (PowerShell), net localgroup (Windows)
**Voir aussi :** usermod, groupdel, id, /etc/group
## `passwd` — Modifier le mot de passe d'un compte [Linux/macOS]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** changer son propre mot de passe, réinitialiser le mot de passe d'un utilisateur, forcer le changement à la prochaine connexion
**Rôle :** Mettre à jour le jeton d'authentification (mot de passe chiffré) d'un compte dans le fichier sécurisé `/etc/shadow`.
**Syntaxe :** `passwd [options] [utilisateur]`
**Cas réguliers :**
- `passwd` — Changer son propre mot de passe utilisateur (le plus courant)
- `passwd adolphe` — Réinitialiser le mot de passe d'un autre utilisateur (nécessite `root`/`sudo`)
- `passwd -l adolphe` — Verrouiller le mot de passe du compte (*lock*)
- `passwd -e adolphe` — Expirer immédiatement le mot de passe pour forcer son changement à la première reconnexion
**Origine :** AT&T Unix (1971) — gestion sécurisée des mots de passe Unix.
**Subtilités/confusions :**
- Un utilisateur standard ne peut changer que son propre mot de passe et doit saisir son ancien mot de passe.
- Le superutilisateur `root` peut changer le mot de passe de n'importe quel compte SANS connaître l'ancien mot de passe.
- Les mots de passe ne sont jamais stockés en clair : ils sont hachés avec un sel fort (ex: SHA-512 ou yescrypt) dans `/etc/shadow`.
**Urgences/dangers :** ⚠️ Oublier le mot de passe root d'une machine sans compte sudo exige un redémarrage en mode mono-utilisateur (*single-user*) via GRUB.
**Précautions :** Utiliser des mots de passe longs (passphrases) ou privilégier l'authentification par clés SSH sans mot de passe.
**Équivalents :** Set-LocalUser (PowerShell), net user (Windows)
**Voir aussi :** useradd, usermod, chage, /etc/shadow
## `su` — Basculer d'identité utilisateur [Linux/macOS]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** ouvrir une session complète en tant que `root`, basculer temporairement sur un compte de service (`postgres`, `www-data`)
**Rôle :** Démarrer un nouveau shell avec l'identité et les privilèges d'un autre compte utilisateur.
**Syntaxe :** `su [options] [-] [utilisateur]`
**Cas réguliers :**
- `su -` — Basculer en tant que `root` avec l'environnement complet et le répertoire de root (le plus courant)
- `su - postgres` — Basculer sur l'utilisateur `postgres` avec son environnement propre
- `su -c "ls /root" root` — Exécuter une commande unique sous l'identité cible sans ouvrir de shell
**Origine :** AT&T Unix (1971) — acronyme de « Switch User » ou « Substitute User ».
**Subtilités/confusions :**
- `su` (sans tiret) conserve l'environnement et les variables du compte d'ORIGINE ; `su -` (avec tiret) charge l'environnement PROPRE de l'utilisateur cible (recommandé).
- Exige de saisir le mot de passe de l'utilisateur CIBLE (sauf si exécuté par `root`).
- Sur Ubuntu/Debian modernes, le compte `root` n'a pas de mot de passe par défaut : utiliser `sudo -i` au lieu de `su -`.
**Urgences/dangers :** ⚠️ Travailler en permanence sous `su -` (root) fait perdre la traçabilité des commandes et augmente le risque de fausse manipulation système.
**Précautions :** Préférer `sudo` pour exécuter des commandes ciblées avec traçabilité dans les logs d'audit.
**Équivalents :** sudo -i, runas (Windows CMD)
**Voir aussi :** sudo, whoami, id, exit
## `sudo` — Exécuter une commande avec privilèges [Linux/macOS]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** —
**Contextes :** installer un paquet, modifier un fichier de configuration dans `/etc`, redémarrer un service système
**Rôle :** Exécuter une commande donnée avec les privilèges du superutilisateur `root` (ou d'un autre compte) selon les règles de `/etc/sudoers`.
**Syntaxe :** `sudo [options] <commande> [args]`
**Cas réguliers :**
- `sudo apt update` — Exécuter une commande système avec privilèges admin (le réflexe quotidien)
- `sudo -i` — Ouvrir un shell interactif root complet (équivalent de `su -`)
- `sudo -u www-data php artisan migrate` — Exécuter une commande sous l'identité d'un autre utilisateur que root
- `sudo -k` — Invalider le tampon de mot de passe en mémoire (force la resaisie du mot de passe au prochain sudo)
**Origine :** Robert Coggeshall & Cliff Spencer (1980) — acronyme de « Superuser Do ».
**Subtilités/confusions :**
- Exige la saisie du mot de passe de l'utilisateur COURANT (pas celui de root), qui est conservé en mémoire pendant 15 minutes par défaut.
- Toutes les commandes exécutées avec `sudo` sont consignées dans les journaux système (`/var/log/auth.log` ou `journalctl`) à des fins d'audit.
- La redirection avec `>` ne bénéficie pas de sudo (`sudo echo x > /etc/file` plante) : utiliser `echo x | sudo tee /etc/file`.
**Urgences/dangers :** ⚠️ Exécuter `sudo rm -rf /` ou `sudo chmod` sans vérifier les espaces peut détruire le système d'exploitation.
**Précautions :** N'accorder les privilèges sudo qu'aux utilisateurs de confiance et restreindre les commandes autorisées via `/etc/sudoers`.
**Équivalents :** runas (Windows CMD), Start-Process -Verb RunAs (PowerShell)
**Voir aussi :** visudo, su, whoami, /etc/sudoers
## `visudo` — Éditer le fichier sudoers en toute sécurité [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** accorder des droits d'administration à un utilisateur, configurer l'exécution de commandes sans mot de passe (`NOPASSWD`)
**Rôle :** Éditer le fichier de configuration des privilèges `/etc/sudoers` en verrouillant l'accès et en vérifiant la syntaxe avant sauvegarde.
**Syntaxe :** `visudo [options]`
**Cas réguliers :**
- `sudo visudo` — Éditer le fichier `/etc/sudoers` principal (le plus courant)
- `sudo visudo -f /etc/sudoers.d/devs` — Éditer un fichier de configuration sudo additionnel propre
- `sudo visudo -c` — Vérifier uniquement la syntaxe des fichiers sudoers sans les ouvrir
**Origine :** Bill Joy / Sudo Team (1989) — conçu spécifiquement pour empêcher le verrouillage accidentel du système sudo.
**Subtilités/confusions :**
- NE JAMAIS éditer `/etc/sudoers` avec `nano` ou `vim` directement : une seule faute de syntaxe bloque TOUS les accès `sudo` sur la machine !
- `visudo` valide la syntaxe à la sauvegarde : s'il repère une erreur, il refuse d'enregistrer et propose de rééditer.
- Utilise l'éditeur défini par la variable `EDITOR` ou `VISUAL` (ex: `EDITOR=nano visudo`).
**Urgences/dangers :** ⚠️ Casser le fichier sudoers en contournant `visudo` bloque le système et exige un redémarrage en mode de récupération GRUB.
**Précautions :** Placer vos règles personnalisées dans des fichiers séparés sous `/etc/sudoers.d/` plutôt que de modifier le fichier principal.
**Équivalents :** (spécifique à l'écosystème sudo Unix/Linux)
**Voir aussi :** sudo, /etc/sudoers
## `id` — Afficher l'identité et les groupes d'un utilisateur [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** vérifier à quels groupes appartient un utilisateur, trouver l'UID/GID numérique pour une configuration Docker ou NFS
**Rôle :** Afficher les identifiants numériques (UID, GID) et la liste des groupes associés à l'utilisateur courant ou spécifié.
**Syntaxe :** `id [options] [utilisateur]`
**Cas réguliers :**
- `id` — Afficher l'UID, le GID et les groupes de l'utilisateur actuel (le plus courant)
- `id adolphe` — Inspecter les identifiants et groupes d'un autre utilisateur
- `id -u` — Afficher uniquement l'UID numérique (pratique en script : `[ $(id -u) -eq 0 ]` pour tester si l'on est root)
- `id -Gn` — Afficher la liste des noms de tous les groupes auxquels appartient l'utilisateur
**Origine :** AT&T System V Unix (1980) — consultation rapide d'identité de processus.
**Subtilités/confusions :**
- `uid=0(root)` indique que la session possède les privilèges absolus du superutilisateur.
- Utile pour vérifier si un ajout de groupe (`usermod -aG`) a bien été pris en compte par la session courante.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `id -u` dans vos scripts shell d'administration pour bloquer l'exécution si le script n'est pas lancé en root.
**Équivalents :** whoami, Get-LocalUser (PowerShell)
**Voir aussi :** whoami, usermod, /etc/passwd
## `whoami` — Afficher l'utilisateur effectif courant [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** vérifier sous quelle identité s'exécute le shell actuel, vérifier si l'on est passé en `root` après un `sudo`
**Rôle :** Afficher le nom de l'utilisateur associé à l'ID effectif de la session courante.
**Syntaxe :** `whoami`
**Cas réguliers :**
- `whoami` — Afficher le nom de l'utilisateur courant (le réflexe simple)
- `sudo whoami` — Vérifier sous quelle identité s'exécute réellement une commande après élévation de privilèges
- `su postgres -c 'whoami'` — Vérifier l'identité effective après un changement d'utilisateur
- `ssh ada@srv whoami` — Vérifier quel utilisateur distant une connexion SSH utilise réellement
**Origine :** 2BSD Unix (1978) — raccourci historique pour « Who am I? ».
**Subtilités/confusions :**
- Équivalent strict à la commande `id -un`.
- Diffère de la commande `who am i` (avec espaces) qui affiche les détails de la connexion initiale du terminal (*tty* et heure).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser dans les scripts de journalisation pour marquer l'auteur des actions exécutées.
**Équivalents :** id -un, $env:USERNAME (PowerShell), whoami (Windows CMD)
**Voir aussi :** id, su, sudo, loginctl
## `umask` — Masque de création de fichiers par défaut [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** —
**Contextes :** définir les permissions par défaut attribuées aux nouveaux fichiers et dossiers créés par un utilisateur ou un service
**Rôle :** Définir ou afficher le masque binaire d'octets qui SOUSTRAIT des permissions par défaut lors de la création d'un fichier ou répertoire.
**Syntaxe :** `umask [-S] [masque-octal]`
**Cas réguliers :**
- `umask` — Afficher le masque octal courant (ex: `0022` ou `0027`)
- `umask -S` — Afficher le masque sous forme symbolique lisible (`u=rwx,g=rx,o=`)
- `umask 027` — Définir un masque strict : aucun droit pour les autres, pas d'écriture pour le groupe
**Origine :** AT&T Unix (1978) — acronyme de « User Mask ».
**Subtilités/confusions :**
- Le masque se SOUSTRAIT des permissions de départ (`666` pour les fichiers, `777` pour les dossiers).
- Un `umask 022` donne par défaut : fichiers = `644` (`rw-r--r--`), dossiers = `755` (`rwxr-xr-x`).
- Un `umask 077` garantit que tous les nouveaux fichiers créés seront lisibles UNIQUEMENT par leur propriétaire (`600`/`700`).
**Urgences/dangers :** ⚠️ Un `umask 000` crée tous les nouveaux fichiers en accès libre d'écriture pour tout le monde sur le serveur.
**Précautions :** Configurer un `umask 027` ou `077` dans `/etc/profile` ou `.bashrc` pour les serveurs manipulant des données confidentielles.
**Équivalents :** (spécifique aux permissions POSIX/Unix)
**Voir aussi :** chmod, chown, .bashrc
## `chgrp` — Changer le groupe d'un fichier [Linux/macOS]
**Niveau :** debutant | **Popularité :** 85 | **Aliases :** —
**Contextes :** partager un fichier avec une équipe sans modifier son propriétaire utilisateur, ajuster les droits de groupe d'un projet
**Rôle :** Modifier le groupe propriétaire d'un ou plusieurs fichiers ou répertoires.
**Syntaxe :** `chgrp [options] <groupe> <fichiers>`
**Cas réguliers :**
- `chgrp developpeurs /var/www/html/app.js` — Changer le groupe propriétaire du fichier (le plus courant)
- `chgrp -R sysadmins /opt/scripts` — Changer le groupe récursivement sur tout un dossier
- `chgrp --reference=model.txt target.txt` — Aligner le groupe sur celui d'un fichier modèle
**Origine :** AT&T Unix (1971) — acronyme de « Change Group ».
**Subtilités/confusions :**
- Version spécialisée de `chown` (équivalent strict à `chown :groupe fichier`).
- Un utilisateur non-root ne peut changer le groupe d'un fichier QUE vers un groupe dont il est lui-même membre.
**Urgences/dangers :** — (identique à `chown`)
**Précautions :** Vérifier les permissions du groupe (`chmod g+rw`) après avoir changé le groupe propriétaire.
**Équivalents :** chown :groupe, Set-Acl (PowerShell)
**Voir aussi :** chown, chmod, groups, id
## `chattr` — Attributs étendus de fichiers [Linux]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** rendre un fichier de configuration totalement inaltérable (même par root!), forcer un fichier de log en ajout seul (*append-only*)
**Rôle :** Modifier les attributs de système de fichiers étendus (ext4, xfs) d'un fichier Linux (immutabilité, journalisation, compression).
**Syntaxe :** `chattr [operator][attributs] <fichiers>`
**Cas réguliers :**
- `chattr +i /etc/resolv.conf` — Rendre le fichier IMMUTABLE (`+i`) : personne (pas même root !) ne peut le modifier, le supprimer ou le renommer
- `chattr -i /etc/resolv.conf` — Retirer le drapeau d'immutabilité (`-i`) pour autoriser à nouveau les modifications
- `chattr +a /var/log/custom.log` — Rendre un fichier modifiable uniquement en AJOUT SEUL (`+a`, append-only)
- `lsattr /etc/resolv.conf` — Consulter les attributs étendus d'un fichier
**Origine :** Remy Card (1993) — créé pour le système de fichiers ext2/ext3/ext4 de Linux.
**Subtilités/confusions :**
- L'attribut `+i` (*immutable*) bloque même le superutilisateur `root` : pour modifier le fichier, root doit D'ABORD faire `chattr -i`.
- Utile contre les malwares ou les scripts d'auto-configuration agressifs (ex: NetworkManager qui écrase `/etc/resolv.conf`).
- Ne fonctionne que sur les systèmes de fichiers Linux supportant les attributs ext (ext4, xfs, btrfs).
**Urgences/dangers :** ⚠️ Oublier qu'un fichier est marqué `+i` fait échouer les mises à jour système avec des erreurs trompeuses de type `Permission Denied`.
**Précautions :** Utiliser `lsattr` pour vérifier si un fichier "incapable d'être édité par root" n'est pas protégé par `+i`.
**Équivalents :** chflags (macOS/BSD), Set-ItemProperty -Attribute (Windows)
**Voir aussi :** lsattr, chmod, chown
## `systemctl` — Gestionnaire de services systemd [Linux]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** démarrer/arrêter un service web (Nginx/Apache), activer un service au démarrage du système, vérifier le statut d'un démon
**Rôle :** Contrôler l'init système et le gestionnaire de services systemd (units, services, targets, timers).
**Syntaxe :** `systemctl [commande] [nom_du_service]`
**Cas réguliers :**
- `systemctl status nginx` — Vérifier l'état, le PID et les dernières lignes de log du service Nginx (le plus courant)
- `systemctl restart docker` — Redémarrer un service pour appliquer une nouvelle configuration
- `systemctl enable --now postgresql` — Activer le service au démarrage système ET le démarrer immédiatement (`--now`)
**Origine :** Lennart Poettering & Kay Sievers (2010) — composant central du système d'initialisation modernisé systemd.
**Subtilités/confusions :**
- `systemctl reload` recharge la configuration sans couper le service (ex: SIGHUP), alors que `restart` tue et relance le processus.
- La cible de démarrage principale est appelée *target* (ex: `multi-user.target` au lieu de `runlevel 3`, `graphical.target` au lieu de `runlevel 5`).
**Urgences/dangers :** ⚠️ Relancer un service critique (ex: `systemctl restart sshd`) avec une erreur de configuration bloque toute reconnexion distante.
**Précautions :** Toujours valider les fichiers de configuration (ex: `nginx -t` ou `sshd -t`) avant d'exécuter `systemctl reload/restart`.
**Équivalents :** service, init, rc-service (Alpine/OpenRC), launchctl (macOS), Get-Service / Start-Service (PowerShell)
**Voir aussi :** journalctl, systemd-analyze, service, loginctl
## `journalctl` — Inspection du journal système systemd [Linux]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** diagnostiquer un crash de service, suivre en temps réel les logs d'une application systemd, filtrer les erreurs système
**Rôle :** Interroger et afficher les journaux d'événements centralisés collectés par le démon systemd-journald.
**Syntaxe :** `journalctl [options] [filtrage]`
**Cas réguliers :**
- `journalctl -u nginx.service -f` — Suivre (*follow*) les logs Nginx en direct (équivalent moderne de `tail -f /var/log/nginx/access.log`)
- `journalctl -p err..emerg -b` — Afficher toutes les erreurs critiques survenues depuis le dernier démarrage (`-b`)
- `journalctl --since "1 hour ago" --until "10 min ago"` — Filtrer les journaux sur une plage temporelle précise
**Origine :** systemd (2010) — remplace la dispersion des fichiers texte traditionnels `/var/log/syslog` par un format binaire indexé et structuré.
**Subtilités/confusions :**
- Les journaux sont au format binaire indexé : cela garantit des recherches temporelles instantanées et empêche la falsification facile des lignes.
- Si le dossier `/var/log/journal/` n'existe pas ou que `Storage=volatile`, les logs sont effacés au redémarrage (stockés en mémoire RAM `/run`).
**Urgences/dangers :** ⚠️ Un journal système saturé peut remplir la partition `/var` ou RAM si aucune rétention maximale n'est définie dans `journald.conf`.
**Précautions :** Purger les anciens journaux de sécurité avec `journalctl --vacuum-size=1G` ou `journalctl --vacuum-time=7d`.
**Équivalents :** dmesg, tail -f /var/log/syslog, Get-WinEvent (PowerShell)
**Voir aussi :** systemctl, dmesg, syslog-ng, logrotate
## `service` — Interface de contrôle des services (compatibilité Init/systemd) [Linux]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** —
**Contextes :** administrer un service sur d'anciens systèmes SysVinit ou scripts POSIX portables
**Rôle :** Exécuter un script d'initialisation SysVInit (`/etc/init.d/`) ou rediriger de manière transparente vers `systemctl` sous systemd.
**Syntaxe :** `service <nom_service> <action>`
**Cas réguliers :**
- `service apache2 status` — Consulter le statut du service apache2
- `service mysql restart` — Redémarrer la base de données MySQL
- `service --status-all` — Lister tous les services disponibles et leur statut (+ ou -)
**Origine :** Red Hat / SysVinit Unix (années 1990) — commande wrapper pour harmoniser la gestion sous `/etc/init.d/`.
**Subtilités/confusions :**
- Sur les distributions modernes (Debian/Ubuntu/RHEL), `service foo start` réécrit en réalité la commande vers `systemctl start foo.service`.
- Ne gère pas l'activation au démarrage (`enable`/`disable`), contrairement à `chkconfig` ou `systemctl`.
**Urgences/dangers :** —
**Précautions :** Préférer `systemctl` sur tous les systèmes modernes pour bénéficier de la gestion fine des dépendances systemd.
**Équivalents :** systemctl, init, rc-service (OpenRC), /etc/init.d/script
**Voir aussi :** systemctl, journalctl, chkconfig
## `crontab` — Planificateur de tâches périodiques [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** automatiser des sauvegardes nightly, exécuter un nettoyage de logs toutes les heures, générer des rapports périodiques
**Rôle :** Éditer et afficher la table de tâches planifiées (cron jobs) pour l'utilisateur courant ou un utilisateur cible.
**Syntaxe :** `crontab [-u utilisateur] <option>`
**Cas réguliers :**
- `crontab -e` — Éditer la table des tâches cron de l'utilisateur courant (ouvre l'éditeur par défaut `EDITOR` ou `nano`)
- `crontab -l` — Afficher la liste des tâches planifiées actives de l'utilisateur
- `crontab -r` — Supprimer complètement la table des tâches cron (attention sans confirmation !)
**Origine :** Ken Thompson / AT&T Unix (1975), popularisé par Paul Vixie (Vixie Cron, 1987).
**Subtilités/confusions :**
- La syntaxe temporelle à 5 étoiles est : `Minute Heure JourMois Mois JourSemaine` (ex: `0 3 * * *` = tous les jours à 03h00).
- Le Shell exécuté par cron est minimal (`/bin/sh`) et possède un `PATH` très restreint : il faut TOUJOURS utiliser des chemins absolus (ex: `/usr/bin/python3`).
- Toute sortie standard (stdout) ou d'erreur (stderr) non redirigée est envoyée par e-mail local (postfix/sendmail) à l'utilisateur.
**Urgences/dangers :** ⚠️ L'option `-r` efface TOUTES les tâches sans demande de confirmation sur certaines versions Linux.
**Précautions :** Toujours faire une sauvegarde préalable (`crontab -l > backup.cron`) avant d'exécuter `crontab -e` ou `crontab -r`.
**Équivalents :** systemd-timer, at, Schedule-Task (Windows)
**Voir aussi :** at, systemctl, logrotate
## `at` — Planification d'exécution unique différée [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 72 | **Aliases :** —
**Contextes :** programmer un redémarrage nocturne unique, lancer un script lourd à 2h du matin une seule fois
**Rôle :** Enregistrer une commande ou un script pour une exécution ponctuelle unique à une heure donnée dans le futur.
**Syntaxe :** `at <heure_ou_date>`
**Cas réguliers :**
- `echo "/opt/backup.sh" | at 02:30` — Programmer la sauvegarde pour 02h30 la nuit prochaine
- `atq` — Lister les travaux en attente d'exécution dans la file d'attente
- `atrm 5` — Annuler le travail numéro 5 présent dans la file d'attente `atq`
**Origine :** AT&T Unix System V (1979) — abréviation directe du mot anglais « at » (à [telle heure]).
**Subtilités/confusions :**
- Contrairement à `crontab` qui répète une tâche périodiquement, `at` n'exécute la tâche QU'UNE SEULE FOIS puis la supprime.
- Utilise le démon `atd` qui doit être actif (`systemctl status atd`).
- Supporte un langage naturel très riche : `at now + 30 minutes`, `at 4:00 PM tomorrow`, `at 08/15/2026`.
**Urgences/dangers :** ⚠️ Si le serveur est éteint au moment de l'heure programmée, la tâche n'est pas exécutée à l'extinction mais au prochain démarrage.
**Précautions :** Vérifier que le démon `atd` tourne bien en tâche de fond avant d'y planifier une tâche importante.
**Équivalents :** crontab (avec date fixe), systemd-run --on-calendar
**Voir aussi :** crontab, systemctl, sleep
## `systemd-analyze` — Analyse de performance et démarrage systemd [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** auditer le temps de boot d'un serveur Linux, identifier les services ralentisseurs au démarrage
**Rôle :** Profiler et mesurer le temps de démarrage du kernel et de l'espace utilisateur, et afficher le graphe des dépendances de boot.
**Syntaxe :** `systemd-analyze [commande] [options]`
**Cas réguliers :**
- `systemd-analyze` — Afficher le temps global écoulé dans le kernel, initrd et userland au dernier démarrage
- `systemd-analyze blame` — Afficher la liste des services triée par temps d'initialisation décroissant (trouver les ralentisseurs)
- `systemd-analyze critical-chain` — Afficher l'arbre des dépendances critiques bloquant l'atteinte de la cible finale
**Origine :** systemd (2010) — créé par Lennart Poettering pour optimiser le temps de démarrage des distributions Linux.
**Subtilités/confusions :**
- `blame` montre la durée absolue d'initialisation d'un service, mais pas strictly l'impact en parallèle sur le temps total de boot.
- Peut également générer un SVG visuel du démarrage avec `systemd-analyze plot > boot.svg`.
**Urgences/dangers :** —
**Précautions :** Ne pas désactiver un service essentiel (ex: `networking` ou `cloud-init`) sous prétexte qu'il apparaît en haut de `systemd-analyze blame`.
**Équivalents :** dmesg, bootchart
**Voir aussi :** systemctl, journalctl
## `hostnamectl` — Configuration du nom d'hôte système [Linux]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** renommer un serveur après son déploiement, vérifier l'architecture matérielle et la version exacte du kernel Linux
**Rôle :** Consulter et modifier le nom d'hôte de la machine ainsi que les métadonnées système associées (pretty hostname, icône, châssis).
**Syntaxe :** `hostnamectl [commande] [options]`
**Cas réguliers :**
- `hostnamectl` — Afficher les informations détaillées : hostname, OS, kernel, architecture, virtualization
- `hostnamectl set-hostname srv-db-prod01` — Définir définitivement le nouveau nom d'hôte du serveur
- `hostnamectl set-hostname "Serveur de Production" --pretty` — Définir un nom d'affichage lisible avec espaces/accents
**Origine :** systemd (2012) — remplace l'édition manuelle du fichier `/etc/hostname` et le redémarrage.
**Subtilités/confusions :**
- Modifie à la fois le hostname statique (`/etc/hostname`), le hostname transient (DHCP/mDNS) et le hostname pretty.
- N'écrase pas automatiquement les entrées correspondantes dans `/etc/hosts` : il faut souvent réaligner `/etc/hosts` après modification.
**Urgences/dangers :** ⚠️ Changer le hostname d'un serveur de base de données ou nœud Kubernetes/Cluster peut rompre les certificats SSL ou la résolutions DNS interne.
**Précautions :** Vérifier les références au nom d'hôte dans les applications critiques (SSL, DB, K8s) avant de renommer une machine en production.
**Équivalents :** hostname, scutil --set HostName (macOS), Rename-Computer (PowerShell)
**Voir aussi :** hostname, localectl, timedatectl
## `timedatectl` — Gestion de l'heure et du fuseau horaire [Linux]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** —
**Contextes :** changer le fuseau horaire d'un serveur Cloud (ex: UTC vers Europe/Paris), activer la synchronisation NTP
**Rôle :** Consulter et configurer l'heure du système, l'horloge matérielle (RTC) et la synchronisation NTP réseau.
**Syntaxe :** `timedatectl [commande] [options]`
**Cas réguliers :**
- `timedatectl` — Afficher l'heure locale, l'heure UTC, la RTC, le fuseau horaire actuel et le statut NTP
- `timedatectl set-timezone Europe/Paris` — Définir le fuseau horaire du système
- `timedatectl set-ntp true` — Activer la synchronisation automatique de l'heure via Network Time Protocol (NTP)
**Origine :** systemd (2011) — remplace les commandes traditionnelles `date`, `hwclock` et la modification de `/etc/localtime`.
**Subtilités/confusions :**
- `timedatectl list-timezones` permet de rechercher la chaîne exacte d'un fuseau horaire valide.
- Il est très vivement recommandé de conserver tous les serveurs de production sur le fuseau horaire `UTC` pour éviter les décalages de logs.
**Urgences/dangers :** ⚠️ Changer brutalement l'heure du système en arrière (*time jump*) peut corrompre des bases de données SQL ou perturber les jetons d'authentification JWT/Kerberos.
**Précautions :** Préférer la synchronisation progressive NTP plutôt qu me modification manuelle forcée de l'heure avec `set-time`.
**Équivalents :** date, hwclock, Set-Date / Set-TimeZone (PowerShell)
**Voir aussi :** date, hwclock, chronyc, ntpdate
## `localectl` — Configuration des paramètres régionaux et clavier [Linux]
**Niveau :** intermediaire | **Popularité :** 76 | **Aliases :** —
**Contextes :** changer la disposition du clavier en console TTY ou sous X11 (azerty/qwerty), définir les locales (langue `fr_FR.UTF-8`)
**Rôle :** Consulter et modifier les variables de locale système et les cartes de disposition du clavier.
**Syntaxe :** `localectl [commande] [options]`
**Cas réguliers :**
- `localectl` — Afficher la locale active (`LANG`), la carte clavier console (`VC Keymap`) et X11 Layout
- `localectl set-keymap fr` — Définir la disposition du clavier console en Français (AZERTY)
- `localectl set-locale LANG=fr_FR.UTF-8` — Définir la langue principale du système en français UTF-8
**Origine :** systemd (2012) — unifie la configuration des locales et du clavier autrefois dispersée selon les distributions Linux.
**Subtilités/confusions :**
- `localectl set-x11-keymap fr` applique automatiquement la disposition au serveur graphique X11 et Wayland.
- `localectl list-locales` liste toutes les locales générées sur la machine.
**Urgences/dangers :** —
**Précautions :** S'assurer que la locale ciblée est générée dans `/etc/locale.gen` via `locale-gen` avant de l'activer.
**Équivalents :** locale, dpkg-reconfigure locales (Debian/Ubuntu)
**Voir aussi :** locale, timedatectl, hostnamectl
## `loginctl` — Gestion des sessions utilisateurs systemd [Linux]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** —
**Contextes :** inspecter les sessions SSH/graphiques ouvertes, forcer la fermeture de la session d'un utilisateur bloqué, autoriser un processus en tâche de fond après déconnexion (*linger*)
**Rôle :** Inspecter et contrôler le gestionnaire de sessions et de connexions systemd-logind.
**Syntaxe :** `loginctl [commande] [ID_session|utilisateur]`
**Cas réguliers :**
- `loginctl list-sessions` — Lister toutes les sessions d'utilisateurs actuellement ouvertes sur le système
- `loginctl session-status 2` — Afficher les détails et l'arbre des processus de la session numéro 2
- `loginctl enable-linger adolphe` — Permettre aux services utilisateur de adolphe (ex: d'un conteneur Podman) de continuer à tourner après sa déconnexion SSH
**Origine :** systemd (2011) — composant de systemd-logind gérant la multiconnexions et les sièges (*seats*).
**Subtilités/confusions :**
- L'option `enable-linger` est indispensable sur les serveurs modernes pour faire tourner des conteneurs rootless (Podman/Docker rootless) sous un compte utilisateur non-root sans session SSH active.
- L execution avec les privilèges d administration doit être restreinte au strict nécessaire.
**Urgences/dangers :** ⚠️ `loginctl terminate-user <user>` tue instantanément TOUS les processus lancés par cet utilisateur sans ménagement.
**Précautions :** Prévenir les utilisateurs connectés avant d'exécuter `terminate-session` ou `terminate-user`.
**Équivalents :** w, who, logoff (Windows)
**Voir aussi :** systemctl, who, w, last
## `dmesg` — Affichage du tampon de messages du noyau [Linux]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** diagnostiquer une panne matérielle (disque HS, mémoire RAM défectueuse), vérifier la détection d'une clé USB ou carte réseau
**Rôle :** Afficher ou contrôler le tampon circulaire des messages du noyau Linux (*kernel ring buffer*).
**Syntaxe :** `dmesg [options]`
**Cas réguliers :**
- `dmesg -T` — Afficher les messages du noyau avec des horodatages lisibles (*human-readable timestamps*)
- `dmesg -l err,crit` — Filtrer l'affichage pour ne conserver que les erreurs et les messages critiques du noyau
- `dmesg | grep -i sda` — Rechercher les événements noyau liés à un disque matériel spécifique (`sda`)
**Origine :** BSD / AT&T Unix (1977) — acronyme de « Display Message ».
**Subtilités/confusions :**
- `dmesg` extrait les données en direct de la mémoire du kernel (`/proc/kmsg` ou `syslogd`).
- Sur les distributions récentes (Ubuntu 20.04+), l'accès à `dmesg` sans privilèges `sudo` peut être restreint par le sysctl `kernel.dmesg_restrict=1`.
- Les horodatages bruts par défaut sont affichés en secondes écoulées depuis le démarrage du kernel (`[ 12345.67890]`).
**Urgences/dangers :** —
**Précautions :** Toujours passer le drapeau `-T` ou `-H` pour convertir les timestamps bruts du noyau en dates intelligibles.
**Équivalents :** journalctl -k, Get-WinEvent -ProviderName Kernel-* (Windows)
**Voir aussi :** journalctl, lspci, lsusb, uptime
## `uptime` — Durée de fonctionnement et charge système [Linux/macOS]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** vérifier si un serveur a redémarré récemment, évaluer la charge moyenne (*load average*) du processeur
**Rôle :** Afficher depuis combien de temps le système tourne, le nombre d'utilisateurs connectés et la moyenne de charge processeur.
**Syntaxe :** `uptime [options]`
**Cas réguliers :**
- `uptime` — Afficher l'heure, la durée d'activité (up time), le nombre d'utilisateurs et les 3 moyennes de charge (1 min, 5 min, 15 min)
- `uptime -p` — Afficher uniquement la durée de fonctionnement dans un format lisible (*pretty*)
- `uptime -s` — Afficher la date et l'heure exactes du dernier démarrage système
**Origine :** BSD Unix (1980) — introduit dans 3.0BSD.
**Subtilités/confusions :**
- Les trois valeurs de *load average* (ex: `0.50, 1.20, 2.10`) représentent le nombre moyen de processus en attente d'exécution CPU ou I/O disque sur 1, 5 et 15 minutes.
- Une charge égale au nombre de cœurs CPU de la machine indique une utilisation à 100% (ex: load 4.0 sur un quad-core).
**Urgences/dangers :** —
**Précautions :** Si la load average dépasse largement le nombre de vCPUs tout en ayant une utilisation CPU faible, vérifier l'attente I/O disque (*iowait*).
**Équivalents :** top, w, (Get-CimInstance Win32_OperatingSystem).LastBootUpTime (PowerShell)
**Voir aussi :** top, w, who, dmesg
## `shutdown` — Extinction ou redémarrage planifié du système [Linux/macOS]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** éteindre proprement un serveur distant, programmer une coupure de maintenance dans 10 minutes avec avertissement aux utilisateurs
**Rôle :** Arrêter, éteindre ou redémarrer le système de manière sécurisée en notifiant les utilisateurs connectés.
**Syntaxe :** `shutdown [options] [heure] [message_avertissement]`
**Cas réguliers :**
- `shutdown -h now` — Arrêter et éteindre immédiatement la machine (`-h` = halt/poweroff)
- `shutdown -r +10 "Maintenance serveur dans 10 minutes"` — Redémarrer dans 10 minutes avec envoi d'un message murale à tous les TTYs
- `shutdown -c` — Annuler un arrêt ou redémarrage précédemment planifié
**Origine :** AT&T Unix (1977) — commande historique d'extinction ordonnée.
**Subtilités/confusions :**
- Ferme proprement les processus en leur envoyant `SIGTERM` puis `SIGKILL`, démonte les systèmes de fichiers et coupe l'alimentation matérielle.
- Bloque les nouvelles connexions d'utilisateurs 5 minutes avant l'échéance programmée.
**Urgences/dangers :** ⚠️ Lancer `shutdown -h now` sur un serveur distant sans accès Out-Of-Band (IPMI/KVM) rend la machine inaccessible jusqu'à une réintervention physique.
**Précautions :** Prévenir les utilisateurs et s'assurer que les données en mémoire vive sont écrites sur disque (`sync`) avant l'extinction.
**Équivalents :** poweroff, reboot, Stop-Computer (PowerShell), shutdown /s /t 0 (Windows CMD)
**Voir aussi :** reboot, poweroff, systemctl, sync
## `reboot` — Redémarrage immédiat du système [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** appliquer une mise à jour du noyau Linux, relancer un serveur après maintenance
**Rôle :** Redémarrer immédiatement le système d'exploitation.
**Syntaxe :** `reboot [options]`
**Cas réguliers :**
- `reboot` — Relancer immédiatement le système de manière propre
- `reboot -f` — Forcer le redémarrage immédiat sans passer par l'arrêt propre des dmons init (dangereux)
**Origine :** BSD Unix (1980) — raccourci historique pour `shutdown -r now`.
**Subtilités/confusions :**
- Sur les distributions modernes avec systemd, `reboot` est un lien symbolique ou un alias de `systemctl reboot`.
- `reboot -f` ne prévient pas les processus et ne démonte pas proprement les disques (risque de corruption FS).
**Urgences/dangers :** ⚠️ S'assurer qu'aucun traitement critique en cours (sauvegarde, transaction SQL, compilation) n'est interrompu.
**Précautions :** Exécuter `sync` avant `reboot` pour s'assurer que les tampons d'écriture sont vidés sur disque.
**Équivalents :** shutdown -r now, systemctl reboot, Restart-Computer (PowerShell)
**Voir aussi :** shutdown, poweroff, systemctl, sync
## `poweroff` — Extinction immédiate de l'alimentation [Linux/macOS]
**Niveau :** debutant | **Popularité :** 91 | **Aliases :** —
**Contextes :** éteindre un serveur physique ou une machine virtuelle une fois la maintenance terminée
**Rôle :** Arrêter le système d'exploitation et couper l'alimentation matérielle (ACPI).
**Syntaxe :** `poweroff [options]`
**Cas réguliers :**
- `poweroff` — Arrêter les dmons, démonter les partitions et éteindre le matériel immédiatement
- `poweroff -f` — Forcer l'extinction matérielle immédiate sans fermeture propre
**Origine :** System V / Linux (années 1990) — équivalent moderne de `shutdown -h now`.
**Subtilités/confusions :**
- Alias direct vers `systemctl poweroff` sous systemd.
- `halt` arrête le processeur mais peut laisser la carte mère sous tension, tandis que `poweroff` coupe complètement l'alimentation ACPI.
**Urgences/dangers :** ⚠️ N'éteindre une machine virtuelle ou un serveur que si l'accès à la console de gestion (vSphere, AWS, IPMI) est disponible pour la rallumer.
**Précautions :** Sauvegarder les travaux en cours et s'assurer qu'aucun autre utilisateur n'est connecté (`who` / `w`).
**Équivalents :** shutdown -h now, systemctl poweroff, Stop-Computer (PowerShell)
**Voir aussi :** shutdown, reboot, systemctl
## `lsblk` — Liste des périphériques de stockage en bloc [Linux]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** identifier la structure des partitions et disques durs, repérer un nom de disque (`/dev/sdb`, `/dev/nvme0n1`) avant formatage ou montage
**Rôle :** Lister sous forme d'arbre hiérarchique tous les périphériques de stockage bloc (disques, partitions, volumes LVM, boucles loop).
**Syntaxe :** `lsblk [options] [périphérique]`
**Cas réguliers :**
- `lsblk` — Afficher l'arborescence standard des disques, partitions et points de montage
- `lsblk -f` — Afficher le système de fichiers (ext4, xfs, vfat), le UUID et le point de montage de chaque partition
- `lsblk -b -o NAME,SIZE,FSTYPE,MOUNTPOINT` — Afficher les tailles exactes en octets avec colonnes personnalisées
**Origine :** util-linux (2009) — développé par Karel Zak pour remplacer la lecture manuelle complexe de `/sys/block`.
**Subtilités/confusions :**
- `lsblk` ne nécessite PAS les droits `sudo` pour lire la structure des disques.
- Distingue les types : `disk` (disque physique), `part` (partition), `lvm` (volume logique), `rom` (CD-ROM/ISO), `loop` (fichier image monté).
**Urgences/dangers :** —
**Précautions :** Toujours vérifier les noms de disques avec `lsblk` avant d'exécuter une commande destructrice comme `dd` ou `mkfs`.
**Équivalents :** fdisk -l, diskutil list (macOS), Get-Disk / Get-Partition (PowerShell)
**Voir aussi :** fdisk, blkid, df, parted
## `fdisk` — Manipulateur de tables de partitions MBR/GPT [Linux]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** créer une partition sur un nouveau disque dur, supprimer une partition, modifier les types de partition (Linux/Swap)
**Rôle :** Créer, modifier, afficher et supprimer les partitions sur un disque utilisant la table de partitions MBR (ou GPT depuis util-linux 2.23).
**Syntaxe :** `fdisk [options] <périphérique>`
**Cas réguliers :**
- `fdisk -l` — Lister toutes les partitions de tous les disques attachés au système (en mode lecture seule)
- `fdisk /dev/sdb` — Ouvrir le menu interactif pour partitionner le disque `/dev/sdb`
**Origine :** MS-DOS / IBM PC-DOS (1983), réécrit pour Linux par A. V. Le Blanc (1992).
**Subtilités/confusions :**
- `fdisk` fonctionne en mode interactif avec des commandes à une seule lettre : `p` (print table), `n` (new partition), `d` (delete), `w` (write changes to disk), `q` (quit without saving).
- Aucune modification n'est réellement écrite sur le disque tant que la commande `w` (*write*) n'est pas saisie.
**Urgences/dangers :** ⚠️ Exécuter `w` avec une mauvaise table de partitions détruit instantanément l'accès aux données du disque cible.
**Précautions :** Vérifier trois fois le périphérique cible (`/dev/sdX`) avant d'enregistrer avec `w`. Préférer `gdisk` ou `parted` pour les disques > 2 To (GPT).
**Équivalents :** gdisk, parted, diskutil (macOS), diskpart (Windows)
**Voir aussi :** gdisk, parted, lsblk, mkfs
## `gdisk` — Partitionnement GPT interactif [Linux]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** —
**Contextes :** partitionner des disques modernes de plus de 2 To avec UEFI, convertir une ancienne table MBR en GPT sans perte de données
**Rôle :** Manipulateur interactif de table de partitions GPT (*GUID Partition Table*), équivalent moderne de `fdisk` basé sur `GPT fdisk`.
**Syntaxe :** `gdisk <périphérique>`
**Cas réguliers :**
- `gdisk -l /dev/nvme0n1` — Lister la table de partitions GPT d'un SSD NVMe
- `gdisk /dev/sdb` — Entrer en mode interactif GPT (commandes similaires à fdisk : `p`, `n`, `d`, `w`)
**Origine :** Rod Smith (2009) — développé spécifiquement pour pallier les limitations MBR de l'ancien `fdisk`.
**Subtilités/confusions :**
- GPT permet jusqu'à 128 partitions primaires sans avoir besoin de partitions étendues/logiques, et supporte des disques jusqu'à 9,4 ZB.
- `sgdisk` est la variante non-interactive en ligne de commande de `gdisk` pour l'automatisation par script.
**Urgences/dangers :** ⚠️ Même danger que fdisk : la touche `w` écrit définitivement les changements de partitions.
**Précautions :** Toujours créer une sauvegarde de la table GPT avec `gdisk -b backup.gpt /dev/sdb` avant toute modification majeure.
**Équivalents :** fdisk, parted, diskpart (Windows)
**Voir aussi :** fdisk, parted, lsblk
## `parted` — Outil universel de partitionnement et redimensionnement [Linux]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** agrandir une partition en ligne de commande sans interface graphique, créer des partitions GPT/MBR dans des scripts d'installation automatique
**Rôle :** Manipuler, créer, redimensionner, vérifier et copier des partitions de disques (MBR et GPT) en mode interactif ou non-interactif.
**Syntaxe :** `parted [options] <périphérique> [commande]`
**Cas réguliers :**
- `parted /dev/sda print` — Afficher la table des partitions et le type d'étiquette (MBR/GPT) du disque `/dev/sda`
- `parted -s /dev/sdb mklabel gpt` — Créer une table de partition GPT de manière non-interactive (`-s` = script mode)
- `parted /dev/sdb resizepart 1 100%` — Redimensionner la partition 1 pour occuper 100% de l'espace disque disponible
**Origine :** GNU Project / Andrew Clausen & Lennert Buytenhek (1999) — acronyme de « PARTition EDitor ».
**Subtilités/confusions :**
- Contrairement à `fdisk`, certaines opérations sous `parted` s'appliquent IMMÉDIATEMENT sur le disque sans attendre de commande de sauvegarde globale !
- Supporte les unités dynamiques : `s` (secteurs), `B`, `MiB`, `GiB`, `%`.
**Urgences/dangers :** ⚠️ Attention : les commandes comme `mklabel` ou `rm` dans parted effacent la table de partition SANS confirmation de validation finale.
**Précautions :** Vérifier que la partition ciblée n'est pas montée (`umount`) avant de tenter un redimensionnement ou un déplacement.
**Équivalents :** fdisk, gdisk, GParted (GUI), diskpart (Windows)
**Voir aussi :** fdisk, gdisk, lsblk, resiz2fs
## `mkfs` — Formatage et création de systèmes de fichiers [Linux]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** formater une nouvelle partition en Ext4, XFS ou vFAT, préparer une clé USB ou un disque SSD fraîchement partitionné
**Rôle :** Construire un système de fichiers Linux sur un périphérique bloc (partition de disque, volume LVM, image disque).
**Syntaxe :** `mkfs -t <type_fs> [options] <partition>`
**Cas réguliers :**
- `mkfs.ext4 /dev/sdb1` — Formater la partition `/dev/sdb1` avec le système de fichiers Linux Ext4 (le plus courant)
- `mkfs.xfs -f /dev/nvme0n1p1` — Formater en XFS (très utilisé sur RHEL/Rocky/CentOS) avec écrasement forcé (`-f`)
- `mkfs.vfat -F 32 /dev/sdc1` — Formater une clé USB en FAT32 pour compatibilité universelle (Linux, Windows, macOS)
**Origine :** Linus Torvalds / Remy Card (1991) — abréviation de « Make File System ».
**Subtilités/confusions :**
- `mkfs` est en réalité une commande frontale (*frontend*) qui appelle l'exécutable spécifique au système de fichiers (ex: `mkfs.ext4`, `mkfs.xfs`, `mkfs.btrfs`).
- Le formatage réinitialise complètement les structures de métadonnées et la table d'allocation du système de fichiers.
**Urgences/dangers :** ⚠️ Exécuter `mkfs` sur la mauvaise partition (ex: `/dev/sda1` au lieu de `/dev/sdb1`) efface l'intégralité du système d'exploitation !
**Précautions :** Vérifier systématiquement l'identifiant du périphérique avec `lsblk -f` ou `blkid` avant de formater.
**Équivalents :** newfs (BSD), Format-Volume (PowerShell), format (Windows CMD)
**Voir aussi :** fdisk, lsblk, fsck, mount
## `mount` — Montage d'un système de fichiers dans l'arborescence [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** rendre accessible un disque externe, monter un partage réseau NFS ou Samba, rattacher une partition ISO/image système
**Rôle :** Attacher le système de fichiers situé sur un périphérique bloc à un répertoire (point de montage) de l'arborescence Linux/Unix.
**Syntaxe :** `mount [-t type] [-o options] <périphérique> <point_de_montage>`
**Cas réguliers :**
- `mount /dev/sdb1 /mnt/data` — Monter la partition `/dev/sdb1` dans le dossier `/mnt/data`
- `mount -a` — Monter TOUTES les partitions définies dans le fichier de configuration `/etc/fstab`
- `mount -o remount,ro /` — Remonter la partition racine en LECTURE SEULE (utile en cas de dépannage d'urgence)
**Origine :** AT&T Unix Version 1 (1971) — concept fondamental Unix « Tout est fichier ».
**Subtilités/confusions :**
- Le répertoire servant de point de montage doit idéalement être vide : si des fichiers y étaient présents, ils deviennent temporairement masqués jusqu'au démontage.
- Pour rendre un montage permanent au redémarrage, il faut ajouter sa configuration dans `/etc/fstab`.
**Urgences/dangers :** ⚠️ Erreur dans `/etc/fstab` combinée à `mount -a` manqué bloque le démarrage du serveur en mode d'urgence (*emergency shell*).
**Précautions :** Toujours valider les modifications de `/etc/fstab` avec `mount -a` avant de redémarrer la machine.
**Équivalents :** diskutil mount (macOS), Mount-DiskImage / New-PSDrive (PowerShell)
**Voir aussi :** umount, lsblk, df, fstab
## `umount` — Démontage d'un système de fichiers [Linux/macOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** éjecter en toute sécurité une clé USB ou un disque dur externe, démonter un partage NFS avant coupure réseau
**Rôle :** Detacher un système de fichiers précédemment monté de l'arborescence du système d'exploitation.
**Syntaxe :** `umount [options] <point_de_montage|périphérique>`
**Cas réguliers :**
- `umount /mnt/data` — Démonter le point de montage `/mnt/data` (écriture préalable des tampons RAM sur disque)
- `umount -l /mnt/stuck` — Effectuer un démontage paresseux (*lazy umount*) pour détacher le FS dès qu'il ne sera plus occupé
- `umount -f /mnt/nfs` — Forcer le démontage (particulièrement utile pour les partages NFS devenus inaccessibles)
**Origine :** AT&T Unix (1971) — abréviation de « Unmount » (attention à l'absence de "n" : `umount` et non `unmount`).
**Subtilités/confusions :**
- Nom de commande piège : la commande s'écrit `umount` (sans le premier "n").
- Si le message `target is busy` apparaît, cela signifie qu'un processus ou un Shell est actuellement ouvert dans le répertoire (utiliser `fuser -m /mnt/data` ou `lsof /mnt/data` pour trouver le coupable).
**Urgences/dangers :** —
**Précautions :** Ne jamais retirer physiquement une clé USB ou un disque sans avoir exécuté `umount` préalable (risque de corruption de fichiers).
**Équivalents :** diskutil unmount (macOS), Dismount-DiskImage (PowerShell)
**Voir aussi :** mount, lsblk, lsof, fuser
## `blkid` — Identification des attributs de block devices (UUID, LABEL) [Linux]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** récupérer l'UUID d'une partition pour l'inscrire dans `/etc/fstab`, identifier le type exact de système de fichiers d'un disque inconnu
**Rôle :** Détecter et afficher les attributs de métadonnées des périphériques bloc (UUID, LABEL, FSTYPE, TYPE de partition).
**Syntaxe :** `blkid [options] [périphérique]`
**Cas réguliers :**
- `blkid /dev/sda1` — Afficher l'UUID, le LABEL et le système de fichiers de la partition `/dev/sda1`
- `blkid -s UUID -o value /dev/sdb1` — Extraire uniquement la valeur brute de l'UUID (pratique pour l'injection dans des scripts)
- `blkid` — Lister les identifiants uniques de tous les périphériques bloc reconnus sur le système
**Origine :** libblkid / util-linux (2001) — abréviation de « Block Device ID ».
**Subtilités/confusions :**
- L'UUID (*Universally Unique Identifier*) est invariant même si l'ordre de détection physique des disques change (ex: `/dev/sdb` devenant `/dev/sdc`).
- Recommandé à 100% pour identifier les partitions dans `/etc/fstab` au lieu des noms de deviceno stables `/dev/sdX`.
**Urgences/dangers :** —
**Précautions :** Utiliser `blkid` pour s'assurer du système de fichiers réel avant de tenter un montage ou un formatage.
**Équivalents :** lsblk -f, Get-Volume (PowerShell)
**Voir aussi :** lsblk, mount, fstab
## `fsck` — Vérification et réparation de systèmes de fichiers [Linux/macOS]
**Niveau :** avance | **Popularité :** 87 | **Aliases :** —
**Contextes :** réparer une partition endommagée après une coupure de courant brutale, corriger les erreurs de bloc au démarrage du système
**Rôle :** Vérifier l'intégrité et réparer les erreurs de cohérence sur un système de fichiers Unix/Linux.
**Syntaxe :** `fsck [options] <partition>`
**Cas réguliers :**
- `fsck /dev/sdb1` — Vérifier la partition `/dev/sdb1` (demande confirmation pour chaque réparation)
- `fsck -y /dev/sdb1` — Réparer automatiquement toutes les erreurs détectées sans poser de questions (`-y` = yes)
- `touch /forcefsck` — Programmer une vérification complète du disque système racine au tout prochain redémarrage
**Origine :** AT&T Unix (1979) — acronyme de « File System Check ».
**Subtilités/confusions :**
- 🚨 REGLE D'OR : Ne JAMAIS exécuter `fsck` sur un système de fichiers actuellement MONTÉ ! Cela détruira irrémédiablement vos données.
- Tout comme `mkfs`, `fsck` est un wrapper qui appelle l'outil spécialisé (`e2fsck` pour Ext4, `xfs_repair` pour XFS, `fsck.vfat` pour FAT).
**Urgences/dangers :** ⚠️ Lancer `fsck` sur une partition montée en lecture/écriture peut déchiqueter la structure du système de fichiers.
**Précautions :** Toujours démonter la partition (`umount /dev/sdb1`) ou démarrer sur un Live-USB avant de lancer `fsck`.
**Équivalents :** e2fsck, xfs_repair, chkdsk (Windows CMD), Repair-Volume (PowerShell)
**Voir aussi :** mount, umount, mkfs, lsblk
## `df` — Occupation de l'espace disque des systèmes de fichiers [Linux/macOS]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** vérifier l'espace disque libre restant sur le serveur, diagnostiquer une alerte « Partition / pleine »
**Rôle :** Afficher la quantité d'espace disque disponible et utilisée sur les systèmes de fichiers montés.
**Syntaxe :** `df [options] [fichier|dossier]`
**Cas réguliers :**
- `df -h` — Afficher l'utilisation disque sous un format lisible par l'humain (`-h` = Ko, Mo, Go, To)
- `df -i` — Afficher l'occupation des Inodes au lieu de l'espace octets (diagnostiquer la saturation par trop de petits fichiers)
- `df -T` — Afficher la colonne du type de système de fichiers (ext4, xfs, overlay, tmpfs)
**Origine :** AT&T Unix Version 1 (1971) — abréviation de « Disk Free ».
**Subtilités/confusions :**
- Si `df -h` montre une partition pleine alors que `du` n'explique pas la consommation, des fichiers supprimés sont probablement maintenus ouverts par des processus actifs (fichiers fantômes résolus via `lsof +L1`).
- Une partition peut être saturée à 100% par épuisement d'inodes (`df -i`) même s'il reste plusieurs Giga-octets d'espace disque libre.
**Urgences/dangers :** —
**Précautions :** Surveiller à la fois l'espace octets (`df -h`) et la table d'inodes (`df -i`).
**Équivalents :** du, Get-PSDrive / Get-Volume (PowerShell)
**Voir aussi :** du, lsblk, mount, lsof
## `du` — Estimation de la taille des fichiers et répertoires [Linux/macOS]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** repérer le dossier ou le fichier volumineux qui prend toute la place sur le serveur, analyser la taille d'un projet
**Rôle :** Estimer et afficher la consommation d'espace disque des fichiers et répertoires de façon récursive.
**Syntaxe :** `du [options] [chemin]`
**Cas réguliers :**
- `du -sh /var/log` — Afficher la taille totale cumulée du dossier `/var/log` (`-s` = summary, `-h` = human-readable)
- `du -h --max-depth=1 /var` — Lister la taille de chaque sous-dossier direct de `/var` pour trouver le plus gros
- `du -ah . | sort -rh | head -n 10` — Afficher le Top 10 des plus gros fichiers/dossiers du répertoire courant
**Origine :** AT&T Unix Version 1 (1971) — acronyme de « Disk Usage ».
**Subtilités/confusions :**
- `du` mesure l'espace disque REELLEMENT ALLOUÉ en blocs sur le système de fichiers, ce qui peut différer de la taille logique brute (ex: fichiers de trou / *sparse files*).
- Sur macOS/BSD, `--max-depth=1` s'écrit `-d 1`.
**Urgences/dangers :** —
**Précautions :** Sur un arborescence énorme avec des millions de fichiers, `du /` peut consommer beaucoup d'I/O disque (utiliser avec précaution en prod).
**Équivalents :** ncdu (outil interactif TUI recommandable), Get-ChildItem | Measure-Object (PowerShell)
**Voir aussi :** df, ls, ncdu, find
## `pvcreate` — Initialisation d'un volume physique LVM [Linux]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** préparer une nouvelle partition ou un disque brut pour l'intégrer dans une architecture de stockage LVM (*Logical Volume Manager*)
**Rôle :** Initialiser un disque ou une partition en tant que volume physique LVM (*Physical Volume*).
**Syntaxe :** `pvcreate [options] <périphérique>`
**Cas réguliers :**
- `pvcreate /dev/sdb1` — Marquer la partition `/dev/sdb1` comme utilisable par LVM
- `pvs` — Lister rapidement les volumes physiques LVM configurés et leur espace disponible
- `pvdisplay` — Afficher les détails complets (Extent Size, UUID, Volume Group d'appartenance)
**Origine :** Heinz Mauelshagen (1998) / Red Hat LVM2 — acronyme de « Physical Volume Create ».
**Subtilités/confusions :**
- Écrit un en-tête LVM au début du périphérique bloc : les données existantes sur la partition seront rendues inaccessibles par les outils standards.
- Première étape de la chaîne d'administration LVM : `pvcreate` (Physical Volume) ➔ `vgcreate` (Volume Group) ➔ `lvcreate` (Logical Volume).
**Urgences/dangers :** ⚠️ Exécuter `pvcreate` sur un disque contenant déjà des données sans LVM écrase sa table de partitions.
**Précautions :** S'assurer avec `lsblk` ou `blkid` que la partition cible ne contient aucun système de fichiers actif.
**Équivalents :** pvs, pvdisplay, pvremove
**Voir aussi :** vgcreate, lvcreate, pvs, lsblk
## `vgcreate` — Création d'un groupe de volumes LVM [Linux]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** regrouper plusieurs disques physiques en un seul grand pool de stockage virtuel LVM
**Rôle :** Créer un groupe de volumes LVM (*Volume Group*) en assemblant un ou plusieurs volumes physiques (`pvcreate`).
**Syntaxe :** `vgcreate <nom_du_vg> <pv1> [pv2 ...]`
**Cas réguliers :**
- `vgcreate vg_data /dev/sdb1` — Créer le groupe de volumes nommé `vg_data` à partir du volume physique `/dev/sdb1`
- `vgcreate vg_pool /dev/sdb1 /dev/sdc1` — Agréger deux disques physiques dans un même groupe de volumes unifié
- `vgs` — Lister synthétiquement tous les groupes de volumes LVM actifs et leur capacité totale/libre
**Origine :** LVM2 Linux (2001) — acronyme de « Volume Group Create ».
**Subtilités/confusions :**
- Le Volume Group agit comme un "disque dur virtuel géant" dans lequel on découpera ensuite des volumes logiques (`lvcreate`).
- On peut facilement étendre un groupe de volumes existant ultérieurement avec la commande `vgextend vg_data /dev/sdd1`.
**Urgences/dangers :** —
**Précautions :** Choisir un nom explicite pour le VG (ex: `vg_system`, `vg_data`) pour éviter les confusions en environnement multi-disques.
**Équivalents :** vgs, vgdisplay, vgextend
**Voir aussi :** pvcreate, lvcreate, vgs, vgextend
## `lvcreate` — Création d'un volume logique LVM [Linux]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** tailler une partition logique sur mesure pour `/var` ou `/data`, créer un Snapshot LVM instantané avant mise à jour système
**Rôle :** Découper et créer un volume logique (*Logical Volume*) à partir de l'espace disponible dans un groupe de volumes (`vgcreate`).
**Syntaxe :** `lvcreate [options] -n <nom_du_lv> <nom_du_vg>`
**Cas réguliers :**
- `lvcreate -L 50G -n lv_app vg_data` — Créer un volume logique de 50 Giga-octets nommé `lv_app` dans le VG `vg_data`
- `lvcreate -l 100%FREE -n lv_data vg_data` — Créer un volume logique occupant la totalité (100%) de l'espace libre restant du VG
- `lvcreate -L 10G -s -n snap_root /dev/vg_system/lv_root` — Créer un SNAPSHOT lecture-écriture de 10 Go du volume racine
**Origine :** LVM2 Linux (2001) — acronyme de « Logical Volume Create ».
**Subtilités/confusions :**
- Le volume créé apparaît dans le système sous la forme du fichier bloc `/dev/mapper/vg_data-lv_app` ou `/dev/vg_data/lv_app`.
- Une fois le LV créé, il doit être formaté avec un système de fichiers (`mkfs.ext4 /dev/vg_data/lv_app`) puis monté (`mount`).
- LVM permet d'agrandir à chaud un LV et son filesystem en une seule commande avec `lvextend -r -L +20G /dev/vg_data/lv_app`.
**Urgences/dangers :** —
**Précautions :** Conserver toujours 10 à 20% d'espace non alloué dans le Volume Group pour la création de Snapshots d'urgence.
**Équivalents :** lvs, lvdisplay, lvextend, lvreduce
**Voir aussi :** pvcreate, vgcreate, lvs, lvextend, mkfs
## `swapon` — Activation des espaces d'échange Swap [Linux]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** activer une partition ou un fichier de Swap pour éviter les plantages OOM (*Out Of Memory*), étendre la mémoire virtuelle
**Rôle :** Activer les périphériques et fichiers de zone d'échange (*swap*) pour la mémoire virtuelle sous Linux.
**Syntaxe :** `swapon [options] [périphérique|fichier_swap]`
**Cas réguliers :**
- `swapon --show` — Afficher les espaces de Swap actuellement actifs avec leur taille, type et priorité d'utilisation
- `swapon /swapfile` — Activer le fichier de Swap nommé `/swapfile`
- `swapon -a` — Activer toutes les zones de Swap déclarées dans `/etc/fstab`
**Origine :** BSD / AT&T Unix System V (1980) — abréviation de « Swap On ».
**Subtilités/confusions :**
- Avant d'activer un nouveau fichier Swap avec `swapon`, il doit être créé (`fallocate` ou `dd`), sécurisé (`chmod 600`) et préparé avec `mkswap /swapfile`.
- `swapoff` effectue l'opération inverse (désactivation), ce qui réinjecte toutes les données du Swap vers la RAM physique (attention si la RAM est saturée !).
**Urgences/dangers :** ⚠️ Exécuter `swapoff -a` sur un serveur dont la RAM physique est déjà saturée provoque le crash du système par OOM-Killer.
**Précautions :** S'assurer que le fichier de Swap appartient strictly à `root` avec des permissions `0600` pour empêcher la lecture des clés/mots de passe en RAM.
**Équivalents :** swapoff, mkswap, Get-CimInstance Win32_PageFileSetting (PowerShell)
**Voir aussi :** swapoff, swap, free, sysctl
## `sysctl` — Configuration des paramètres du noyau à chaud [Linux]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** —
**Contextes :** optimiser la pile réseau TCP/IP, activer le forwarding IP pour un routeur/Docker, ajuster les limites de mémoire virtuelle (*swappiness*)
**Rôle :** Consulter et modifier dynamiquement les paramètres d'exécution du noyau Linux présentés sous `/proc/sys/`.
**Syntaxe :** `sysctl [options] [clé[=valeur]]`
**Cas réguliers :**
- `sysctl net.ipv4.ip_forward` — Consulter la valeur actuelle du routage IP v4
- `sysctl -w net.ipv4.ip_forward=1` — Modifier à chaud la valeur du paramètre sans redémarrer (effet immédiat jusqu'au prochain boot)
- `sysctl -p` — Recharger et appliquer tous les paramètres définis de façon permanente dans `/etc/sysctl.conf`
**Origine :** BSD Unix (1993) / Linux Kernel — acronyme de « System Control ».
**Subtilités/confusions :**
- L'utilisation de `-w` ne modifie le paramètre qu'en mémoire RAM : pour pérenniser le réglage au redémarrage, il faut l'inscrire dans `/etc/sysctl.d/99-custom.conf`.
- Les clés à points correspondent directement à l'arborescence du système de fichiers `/proc/sys/` (ex: `vm.swappiness` ➔ `/proc/sys/vm/swappiness`).
**Urgences/dangers :** ⚠️ Une mauvaise configuration de `vm.max_map_count` ou des filtres TCP SYN peut planter les bases de données (Elasticsearch) ou couper le réseau.
**Précautions :** Tester les paramètres à chaud avec `sysctl -w` avant de les consigner définitivement dans `/etc/sysctl.d/`.
**Équivalents :** sysctl (macOS/FreeBSD)
**Voir aussi :** dmesg, lsmod, ulimit
## `lsmod` — Liste des modules du noyau Linux chargés [Linux]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** —
**Contextes :** vérifier si un pilote matériel (ex: carte Nvidia, module Wi-Fi) ou système (ex: `iptable_filter`, `wireguard`) est actuellement chargé en mémoire
**Rôle :** Formater et afficher l'état des modules du noyau Linux actuellement chargés en mémoire (en lisant `/proc/modules`).
**Syntaxe :** `lsmod`
**Cas réguliers :**
- `lsmod` — Lister tous les modules noyau actifs avec leur taille et les dépendances d'utilisation
- `lsmod | grep -i kvm` — Vérifier si les modules de virtualisation matérielle KVM sont chargés
**Origine :** modutils / kmod (1995) — abréviation de « List Modules ».
**Subtilités/confusions :**
- `lsmod` est une commande passive en lecture seule qui ne nécessite aucun privilège root.
- Affiche trois colonnes principales : `Module` (nom), `Size` (octets mémoire), `Used by` (nombre de références et liste des modules dépendants).
**Urgences/dangers :** —
**Précautions :** Si un module a un compte d'utilisation `Used by` supérieur à 0, il ne pourra pas être déchargé directement sans stopper les services dépendants.
**Équivalents :** kldstat (FreeBSD), kmutil (macOS)
**Voir aussi :** modprobe, insmod, rmmod, dmesg
## `modprobe` — Chargement et déchargement intelligent de modules noyau [Linux]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** charger un pilote matériel avec résolution automatique de ses dépendances, bloquer un module vulnérable en liste noire (*blacklist*)
**Rôle :** Ajouter ou retirer des modules du noyau Linux de manière intelligente en gérant automatiquement leurs dépendances et alias.
**Syntaxe :** `modprobe [options] <nom_module>`
**Cas réguliers :**
- `modprobe overlay` — Charger le module de système de fichiers OverlayFS (requis pour Docker) et toutes ses dépendances
- `modprobe -r e1000e` — Retirer (*remove*) proprement le module carte réseau e1000e du noyau
- `modprobe -v wireguard` — Mode verbeux pour visualiser la résolution des dépendances et les fichiers `.ko` chargés
**Origine :** Rusty Russell / kmod (1998) — remplace les commandes bas niveau `insmod` et `rmmod`.
**Subtilités/confusions :**
- Différence majeure avec `insmod` : `modprobe` cherche automatiquement le fichier `.ko` dans `/lib/modules/$(uname -r)/` et charge toutes les dépendances requises.
- Les modules à ignorer au démarrage s'inscrivent dans `/etc/modprobe.d/blacklist.conf`.
**Urgences/dangers :** ⚠️ Décharger un module réseau ou de contrôleur disque actif (`modprobe -r`) coupe immédiatement l'accès au matériel concerné.
**Précautions :** Utiliser `modprobe` de préférence à `insmod` pour éviter les erreurs de symboles manquants.
**Équivalents :** kldload / kldunload (FreeBSD), kmutil load (macOS)
**Voir aussi :** lsmod, insmod, rmmod, dmesg
## `insmod` — Insertion brute d'un fichier module dans le noyau [Linux]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** —
**Contextes :** insérer un pilote sur mesure compilé à la main (`.ko`) hors de l'arborescence standard des modules
**Rôle :** Insérer un fichier module binaire (`.ko`) spécifique directement dans le noyau Linux.
**Syntaxe :** `insmod <chemin_vers_fichier.ko> [arguments_module]`
**Cas réguliers :**
- `insmod /root/drivers/custom_driver.ko` — Charger directement le module compilé spécifié par son chemin exact
- `insmod my_driver.ko debug=1` — Charger le module en lui passant un paramètre de configuration au démarrage
**Origine :** Linux kernel modutils (1995) — acronyme de « Insert Module ».
**Subtilités/confusions :**
- Contrairement à `modprobe`, `insmod` NE résout PAS les dépendances et n'accepte QU'UN chemin absolu/relatif vers un fichier `.ko`.
- Si des symboles noyau requis par le module ne sont pas déjà chargés, `insmod` échouera immédiatement avec une erreur `Unknown symbol in module`.
**Urgences/dangers :** ⚠️ Insérer un module noyau instable ou incompatible compilé manuellement peut provoquer un Kernel Panic immédiat.
**Précautions :** Réserver `insmod` au développement et test de drivers personnalisés ; utiliser `modprobe` en production.
**Équivalents :** modprobe, kldload (FreeBSD)
**Voir aussi :** rmmod, modprobe, lsmod, dmesg
## `rmmod` — Suppression brute d'un module du noyau [Linux]
**Niveau :** avance | **Popularité :** 68 | **Aliases :** —
**Contextes :** décharger un pilote de périphérique spécifique en cours de développement
**Rôle :** Décharger un module du noyau Linux sans vérifier les dépendances complexes d'alias.
**Syntaxe :** `rmmod [options] <nom_module>`
**Cas réguliers :**
- `rmmod custom_driver` — Retirer le module `custom_driver` de la mémoire vive du noyau
- `rmmod -f unstable_module` — Forcer le déchargement (*force*), même si le noyau estime que le module est toujours utilisé
**Origine :** Linux kernel modutils (1995) — acronyme de « Remove Module ».
**Subtilités/confusions :**
- `rmmod` prend le simple NOM du module (ex: `e1000e`) et non le chemin du fichier `.ko`.
- Préférer `modprobe -r` qui décharge aussi les sous-modules devenus inutiles.
**Urgences/dangers :** ⚠️ L'option `-f` (*force*) peut faire planter le système instantanément en laissant des pointeurs mémoire orphelins dans le kernel.
**Précautions :** S'assurer que le module a un compteur d'utilisation à zéro dans `lsmod` avant de le supprimer.
**Équivalents :** modprobe -r, kldunload (FreeBSD)
**Voir aussi :** insmod, modprobe, lsmod
## `lspci` — Lister les périphériques PCI et cartes matérielles [Linux]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** identifier la référence exacte d'une carte réseau, carte graphique (Nvidia/AMD), contrôleur RAID ou bus PCIe
**Rôle :** Afficher des informations détaillées sur tous les bus PCI et périphériques matériels connectés sur les bus PCI/PCIe de la carte mère.
**Syntaxe :** `lspci [options]`
**Cas réguliers :**
- `lspci` — Lister brièvement tous les périphériques PCI (nom du constructeur et puce)
- `lspci -vnn` — Afficher un niveau de détail élevé incluant les identifiants numériques Vendor/Device ID (pratique pour chercher le driver)
- `lspci -k` — Afficher pour chaque matériel le module noyau (`kernel driver in use`) actuellement chargé et actif
**Origine :** pciutils / Martin Mares (1997) — acronyme de « List PCI ».
**Subtilités/confusions :**
- L'option `-k` est indispensable pour diagnostiquer pourquoi un composant (ex: Wi-Fi ou GPU) ne fonctionne pas (détecter l'absence de driver).
- Ne nécessite pas les droits root pour la consultation de base, mais `sudo lspci -vvv` permet d'accéder au registre de configuration PCI complet.
**Urgences/dangers :** —
**Précautions :** Utiliser `lspci -nn` pour obtenir le `VendorID:DeviceID` exact (ex: `10de:1f08`) afin de télécharger le bon pilote propriétaire.
**Équivalents :** lsusb, lshw, system_profiler SPPCIDataType (macOS), Get-PnpDevice (PowerShell)
**Voir aussi :** lsusb, lscpu, lshw, lsmod
## `lsusb` — Lister les périphériques USB connectés [Linux]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** vérifier si un dongle Wi-Fi/Bluetooth, une clé USB, une caméra ou un lecteur de carte à puce est physique détecté
**Rôle :** Afficher des informations sur les bus USB du système et sur tous les périphériques USB qui y sont branchés.
**Syntaxe :** `lsusb [options]`
**Cas réguliers :**
- `lsusb` — Afficher la liste des périphériques USB avec leur numéro de bus, d'appareil et leur VendorID:ProductID
- `lsusb -t` — Afficher sous forme d'arbre physique (*tree*) les hubs USB et les vitesses de négociation (1.5M, 12M, 480M, 5000M)
- `lsusb -v -d 046d:c52b` — Afficher le descripteur USB ultra-détaillé d'un périphérique spécifique par son ID
**Origine :** usbutils / Thomas Sailer & Johannes Erdfelt (1999) — acronyme de « List USB ».
**Subtilités/confusions :**
- Si un appareil apparaît dans `lsusb` mais n'est pas utilisable, la couche matérielle est saine : le problème provient du module noyau ou du firmware.
- Les identifiants `ID xxxx:yyyy` correspondent au code fabriquant (Vendor) et produit (Product).
**Urgences/dangers :** —
**Précautions :** Combiner avec `dmesg -w` au moment du branchement USB pour observer la reconnaissance en temps réel.
**Équivalents :** lspci, lshw, system_profiler SPUSBDataType (macOS), Get-PnpDevice -Class USB (PowerShell)
**Voir aussi :** lspci, lshw, dmesg
## `lscpu` — Informations détaillées sur l'architecture processeur [Linux]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** vérifier le nombre de cœurs physiques/logiques (vCPU), la présence des instructions de virtualisation (VT-x/AMD-V) ou les cache L1/L2/L3
**Rôle :** Extraire de `/proc/cpuinfo` et `/sys/devices/system/cpu` une synthèse claire de l'architecture du processeur (CPU).
**Syntaxe :** `lscpu [options]`
**Cas réguliers :**
- `lscpu` — Afficher la fiche complète du processeur : modèle, vitesse MHz, nombre de cœurs/threads, flags d'instructions
- `lscpu -e` — Afficher un tableau synthétique par cœur CPU (état en ligne, fréquence max, socket)
**Origine :** util-linux / Cai Qian (2008) — acronyme de « List CPU ».
**Subtilités/confusions :**
- Permet de repérer instantanément la différence entre cœurs physiques (*Cores per socket*) et cœurs virtuels (*Threads per core* / Hyper-Threading).
- Affiche la colonne `Virtualization` (ex: `VT-x` ou `AMD-V`) et `Hypervisor vendor` (ex: `KVM`, `VMware`, `xen`) si tournant dans une VM.
**Urgences/dangers :** —
**Précautions :** Vérifier la ligne `Flags` (ex: `aes`, `sse4_2`, `avx2`) lors de l'optimisation d'applications gourmandes en calcul ou cryptographie.
**Équivalents :** sysctl -a | grep machdep.cpu (macOS), Get-CimInstance Win32_Processor (PowerShell)
**Voir aussi :** lsmem, lshw, lspci, top
## `lsmem` — Liste des blocs et de la disposition de la mémoire RAM [Linux]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** —
**Contextes :** inspecter les barrettes et blocs de mémoire vive sous Linux, auditer la mémoire Hotplug sur des machines virtuelles
**Rôle :** Lister l'état de la mémoire vive principale du système par blocs et son état d'activation (online/offline).
**Syntaxe :** `lsmem [options]`
**Cas réguliers :**
- `lsmem` — Afficher la quantité de mémoire totale, la taille d'un bloc mémoire et la liste des plages en ligne
- `lsmem -a` — Afficher également les blocs de mémoire hors ligne (*offline*)
**Origine :** util-linux / Heiko Carstens (2012) — acronyme de « List Memory ».
**Subtilités/confusions :**
- `lsmem` se concentre sur l'organisation matérielle par blocs mémoire du noyau Linux, contrairement à `free` qui se concentre sur la consommation applicative.
- Particulièrement utile dans les environnements Cloud/Hyperviseurs supportant l'ajout de RAM à chaud (*memory hotplugging*).
**Urgences/dangers :** —
**Précautions :** Utiliser `free -h` pour la consommation courante et `lsmem` pour l'architecture bloc hardware.
**Équivalents :** free, dmidecode --type memory, lshw -C memory
**Voir aussi :** free, lscpu, lshw, vmstat
## `lshw` — Inventaire matériel exhaustif du système [Linux]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** générer un rapport complet sur les composants d'un serveur physique (CPU, RAM, carte mère, disques, cartes réseau, BIOS)
**Rôle :** Récolter des informations très détaillées sur la configuration matérielle complète de la machine.
**Syntaxe :** `lshw [options]`
**Cas réguliers :**
- `lshw -short` — Afficher une vue synthétique d'une page de toute l'arborescence matérielle
- `lshw -class network` — Filtrer le rapport pour ne conserver que les composants d'une classe précise (ex: `network`, `disk`, `memory`, `processor`)
- `lshw -html > server_hardware.html` — Générer un rapport d'inventaire complet au format HTML Web
**Origine :** Lyonel Vincent (2002) — acronyme de « List Hardware ».
**Subtilités/confusions :**
- Doit être exécuté avec les privilèges `sudo` pour pouvoir interroger directement le BIOS/DMI et les registres matériels (sinon informations incomplètes).
- Extrait les données de `/proc`, `/sys`, DMI/SMBIOS et des bus PCI/USB.
**Urgences/dangers :** —
**Précautions :** Exécuter avec `sudo lshw -class network` pour récupérer l'adresse MAC et la révision de firmware d'une carte NIC.
**Équivalents :** dmidecode, system_profiler (macOS), Get-ComputerInfo (PowerShell)
**Voir aussi :** lspci, lsusb, lscpu, dmidecode
## `free` — Affichage de la mémoire RAM disponible et utilisée [Linux]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** vérifier la mémoire RAM vive disponible sur un serveur, diagnostiquer la saturation RAM ou le swap d'une application
**Rôle :** Afficher la quantité totale de mémoire vive (RAM) et de swap utilisée, libre, partagée, et les tampons/caches du noyau.
**Syntaxe :** `free [options]`
**Cas réguliers :**
- `free -h` — Afficher l'état de la mémoire RAM et Swap sous forme lisible (*human-readable* : Mo, Go)
- `free -m -s 3` — Afficher la consommation mémoire en Mégaoctets rafraîchie toutes les 3 secondes
- `free -t` — Afficher une ligne additionnelle totalisant RAM + Swap
**Origine :** procps / Linux Kernel (1992) — lit directement `/proc/meminfo`.
**Subtilités/confusions :**
- La colonne `available` (et non `free`) donne l'estimation réelle de la mémoire disponible pour lancer de nouveaux processus sans faire de swap.
- Linux utilise agressivement la RAM inoccupée pour le cache disque (`buff/cache`), mais libère cette mémoire instantanément si une application en a besoin.
**Urgences/dangers :** —
**Précautions :** Ne pas s'inquiéter si la colonne `free` semble basse tant que la colonne `available` reste élevée (phénomène *linuxatemyram*).
**Équivalents :** vm_stat (macOS), vmstat, (Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory (PowerShell)
**Voir aussi :** top, htop, vmstat, swapon, lsmem
## `syslog-ng` — Démon de journalisation système avancé [Linux]
**Niveau :** avance | **Popularité :** 81 | **Aliases :** —
**Contextes :** centraliser les logs de centaines de serveurs Linux sur un serveur SIEM central, filtrer et formater les logs système avant stockage
**Rôle :** Collecter, filtrer, transformer et acheminer les messages de journalisation (syslog) en local ou vers un serveur distant via réseau.
**Syntaxe :** `syslog-ng [options]`
**Cas réguliers :**
- `syslog-ng -s` — Tester et vérifier la syntaxe du fichier de configuration `/etc/syslog-ng/syslog-ng.conf`
- `syslog-ng -F` — Exécuter syslog-ng au premier plan (*foreground*) pour le débogage de la collecte de logs
**Origine :** Balázs Scheidler / BalaBit (1998) — extension moderne du démon Syslog traditionnel UNIX.
**Subtilités/confusions :**
- Repose sur une architecture puissante de blocs de configuration : `source {}` ➔ `filter {}` ➔ `destination {}` ➔ `log {}`.
- Concurrencer directement avec `rsyslog` et `systemd-journald`.
**Urgences/dangers :** ⚠️ Une mauvaise boucle d'acheminement réseau dans syslog-ng peut créer une tempête de logs et saturer la bande passante.
**Précautions :** Toujours valider la syntaxe avec `syslog-ng -s` avant de recharger le service.
**Équivalents :** rsyslog, systemd-journald, fluentd, logstash
**Voir aussi :** journalctl, logrotate, dmesg
## `logrotate` — Rotation et archivage automatique des journaux texte [Linux]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** compresser quotidiennement les logs applicatifs `/var/log/nginx/` pour éviter la saturation du disque, purger les logs plus vieux de 30 jours
**Rôle :** Automatiser la rotation, la compression (gzip), la sauvegarde et l'élimination systématique des fichiers de logs système.
**Syntaxe :** `logrotate [options] <fichier_configuration>`
**Cas réguliers :**
- `logrotate /etc/logrotate.conf` — Exécuter le traitement de rotation standard des journaux système
- `logrotate -f /etc/logrotate.d/nginx` — Forcer la rotation immédiate (*force*) des logs d'un service spécifique
- `logrotate -d /etc/logrotate.conf` — Exécuter en mode simulation (*debug*) sans modifier aucun fichier sur le disque
**Origine :** Red Hat Linux (1997) — outil standard adopté par la quasi-totalité des distributions Linux.
**Subtilités/confusions :**
- Généralement lancé une fois par jour via une tâche cron (`/etc/cron.daily/logrotate`) ou un timer systemd.
- Directives courantes : `daily`/`weekly`, `rotate 14` (conserver 14 archives), `compress` (gzip), `delaycompress`, `missingok`, `notifempty`.
**Urgences/dangers :** ⚠️ Si logrotate ne signale pas au démon (ex: `postrotate -> systemctl reload nginx`) d'ouvrir le nouveau fichier, le démon continuera d'écrire dans le fichier archivé !
**Précautions :** Utiliser l'option `-d` (*debug*) pour tester de nouvelles règles de rotation sans altérer les logs en production.
**Équivalents :** newsyslog (BSD/macOS)
**Voir aussi :** journalctl, crontab, syslog-ng
## `selinux` — Contrôle d'accès obligatoire SELinux (sestatus/setenforce) [Linux]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** sestatus, setenforce
**Contextes :** vérifier si la sécurité renforcée SELinux bloque un service web, basculer temporairement SELinux en mode permissif pour le diagnostic
**Rôle :** Interroger et basculer l'état du sous-système de sécurité à contrôle d'accès obligatoire SELinux (*Security-Enhanced Linux*).
**Syntaxe :** `sestatus` / `setenforce [Enforcing|Permissive|0|1]`
**Cas réguliers :**
- `sestatus` — Afficher le statut actuel de SELinux (Enforcing, Permissive, Disabled) et le nom de la politique active
- `setenforce 0` — Basculer temporairement SELinux en mode `Permissive` (log les violations d'accès sans les bloquer)
- `setenforce 1` — Réactiver le verrouillage strict de sécurité `Enforcing`
**Origine :** NSA (National Security Agency) & Red Hat (2000) — implémentation de MAC (*Mandatory Access Control*) dans le kernel Linux.
**Subtilités/confusions :**
- Les violations de contexte SELinux sont consignées dans `/var/log/audit/audit.log` (analysables via `ausearch -m avc` ou `sealert`).
- Désactiver SELinux dans `/etc/selinux/config` nécessite un redémarrage complet et impose un ré-étiquetage (*relabeling*) long au boot suivant.
**Urgences/dangers :** ⚠️ Ne JAMAIS passer SELinux à `Disabled` sur un serveur de production si un simple `setenforce 0` (Permissive) suffit pour diagnostiquer une panne.
**Précautions :** Utiliser `restorecon -R /var/www/html` pour corriger les contextes de fichiers erronés au lieu de désactiver SELinux.
**Équivalents :** apparmor_status (Ubuntu/Debian), getenforce, restorecon
**Voir aussi :** apparmor_status, chcon, restorecon, audit2allow
## `apparmor_status` — Inspection du profil de sécurité AppArmor [Linux]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** aa-status
**Contextes :** auditer quels dmons applicatifs (Docker, Snap, Ping, Mysql) sont restreints par un profil de sécurité AppArmor sous Debian/Ubuntu
**Rôle :** Afficher le statut global du module de sécurité AppArmor et la liste des profils chargés en mode blocage ou plainte.
**Syntaxe :** `apparmor_status` ou `aa-status`
**Cas réguliers :**
- `aa-status` — Lister le nombre de profils AppArmor chargés, en mode `enforce` ou `complain`, et les processus associés
- `aa-complain /etc/apparmor.d/usr.sbin.mysqld` — Passer le profil MySQL en mode observation (*complain*) sans bloquer les opérations
- `aa-enforce /etc/apparmor.d/usr.sbin.mysqld` — Réactiver le blocage strict du profil MySQL
**Origine :** Immunix / Novell / Canonical (1998) — alternative à SELinux basée sur les chemins de fichiers, très répandue sur Ubuntu et Debian.
**Subtilités/confusions :**
- Différence clé avec SELinux : AppArmor associe les restrictions de sécurité aux CHEMINS des fichiers exécutables et non à des étiquettes de métadonnées d'inodes.
- Mode `enforce` = bloque et log les violations ; Mode `complain` = autorise et log uniquement les violations.
**Urgences/dangers :** —
**Précautions :** Consulter `journalctl -k | grep -i apparmor` pour identifier les refus d'accès causés par AppArmor.
**Équivalents :** sestatus / getenforce (SELinux)
**Voir aussi :** selinux, journalctl, dmesg
