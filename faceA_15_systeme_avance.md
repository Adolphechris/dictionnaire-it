## `chroot` — Change Root Directory [Linux/macOS]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** change root
**Contextes :** réparation de système, construction d'environnements isolés, déploiement de conteneurs primitifs
**Rôle :** Modifie le répertoire racine apparent d'un processus et de ses descendants pour les isoler du reste du système de fichiers.
**Syntaxe :** `chroot <nouveau-racine> [commande]`
**Cas réguliers :**
- `chroot /mnt/system /bin/bash` — Ouvre un shell interactif dans le système installé sur /mnt pour réparer GRUB ou reinstaller des paquets
- `chroot /opt/buildenv make` — Compile un projet dans un environnement isolé sans contaminer le système hôte
**Origine :** Introduit dans Unix BSD 4.2 (1982) par Bill Joy pour l'isolation des processus.
**Subtilités/confusions :**
- chroot n'isole que le système de fichiers — les processus restent visibles et les namespaces réseau/PID ne sont pas séparés (contrairement aux conteneurs).
**Urgences/dangers :** ⚠️ Un processus root peut s'échapper d'un chroot avec `pivot_root` ou via des appels système non protégés — ne pas utiliser pour la sécurité sans namespaces supplémentaires.
**Précautions :** Monter `/proc`, `/sys` et `/dev` dans l'environnement chroot avant d'y entrer pour que les outils système fonctionnent correctement.
**Équivalents :** unshare + pivot_root (isolation complète), conteneurs (Docker/LXC)
**Voir aussi :** unshare, nsenter, pivot_root, mount

## `unshare` — Create New Linux Namespaces [Linux]
**Niveau :** expert | **Popularité :** 72 | **Aliases :** namespace isolation
**Contextes :** création de conteneurs légers, isolation de processus, tests réseau isolés, sécurité
**Rôle :** Crée de nouveaux namespaces Linux (PID, réseau, montage, UTS, IPC, utilisateur) pour isoler un processus sans hyperviseur.
**Syntaxe :** `unshare [options] [commande]`
**Cas réguliers :**
- `unshare --mount --pid --fork bash` — Lance un shell avec ses propres namespaces de montage et PID
- `unshare --net ip link` — Inspecte les interfaces réseau dans un namespace réseau vierge isolé
**Origine :** Appel système Linux basé sur les namespaces introduits progressivement depuis Linux 3.8 ; commande userland dans `util-linux`.
**Subtilités/confusions :**
- `unshare` crée de nouveaux namespaces pour le processus en cours — `nsenter` au contraire rejoint les namespaces d'un processus existant.
- Sans `--user`, les nouvelles opérations de namespace PID ou réseau nécessitent les privilèges root.
**Urgences/dangers :** —
**Précautions :** Combiner `unshare --user --map-root-user` pour créer des namespaces utilisateur non privilégiés sans sudo.
**Équivalents :** nsenter (joindre), clone(2) (appel système bas niveau)
**Voir aussi :** nsenter, chroot, pivot_root, lsns

## `nsenter` — Enter Existing Namespaces [Linux]
**Niveau :** expert | **Popularité :** 78 | **Aliases :** namespace enter
**Contextes :** debug de conteneurs, inspection de processus isolés, administration Docker/Kubernetes
**Rôle :** Rejoint les namespaces d'un processus existant (conteneur ou autre) pour y exécuter des commandes comme si on était à l'intérieur.
**Syntaxe :** `nsenter -t <PID> [--net|--pid|--mnt] <commande>`
**Cas réguliers :**
- `nsenter -t $(docker inspect -f '{{.State.Pid}}' mycontainer) --net ip addr` — Inspecte les interfaces réseau d'un conteneur Docker depuis l'hôte
- `nsenter -t 1234 --pid --mount bash` — Ouvre un shell dans les namespaces d'un processus pour le déboguer
**Origine :** Développé par Eric Biederman pour `util-linux` en parallèle du développement des namespaces Linux.
**Subtilités/confusions :**
- `nsenter` nécessite root ou CAP_SYS_PTRACE pour entrer dans les namespaces d'un autre processus.
- Idéal pour déboguer des conteneurs sans shell intégré (`docker exec` nécessite que le conteneur ait un shell disponible).
**Urgences/dangers :** ⚠️ Entrer dans un namespace de conteneur avec nsenter peut compromettre l'isolation si mal utilisé en production.
**Précautions :** Réserver à la phase de debugging ; ne jamais laisser des processus persistants tournant dans des namespaces de conteneurs de production.
**Équivalents :** `docker exec` (haut niveau), `kubectl exec` (Kubernetes)
**Voir aussi :** unshare, chroot, lsns, docker exec

## `lsns` — List Linux Namespaces [Linux]
**Niveau :** avance | **Popularité :** 67 | **Aliases :** list namespaces
**Contextes :** audit de conteneurs, debug d'isolation, administration système avancée
**Rôle :** Liste tous les namespaces Linux actifs sur le système avec leur type, PID propriétaire et nombre de processus.
**Syntaxe :** `lsns [options]` ou `lsns -t net`
**Cas réguliers :**
- `lsns -t net` — Affiche tous les namespaces réseau actifs et leurs processus propriétaires
- `lsns -p 1234` — Montre les namespaces utilisés par le processus de PID 1234
**Origine :** Utilitaire `util-linux` ajouté lors de la généralisation des namespaces Linux.
**Subtilités/confusions :**
- Chaque ligne représente un namespace unique — plusieurs processus peuvent partager le même namespace.
- Sans sudo, seuls les namespaces des processus de l'utilisateur courant sont visibles.
**Urgences/dangers :** —
**Précautions :** Utiliser `lsns -J` pour une sortie JSON exploitable par des scripts de supervision de namespaces.
**Équivalents :** `/proc/<pid>/ns/` (accès direct aux liens symboliques des namespaces)
**Voir aussi :** unshare, nsenter, ps, /proc

## `cgcreate` — Create Control Groups [Linux]
**Niveau :** expert | **Popularité :** 62 | **Aliases :** cgroup create, libcgroup
**Contextes :** gestion des ressources systèmes, isolation de processus, déploiement de conteneurs
**Rôle :** Crée des cgroups (control groups) Linux pour limiter et surveiller la consommation de ressources (CPU, mémoire, E/S) d'un groupe de processus.
**Syntaxe :** `cgcreate -g cpu,memory:<nom-cgroup>`
**Cas réguliers :**
- `cgcreate -g memory:myapp && cgset -r memory.limit_in_bytes=512M myapp` — Limite la mémoire d'un groupe de processus à 512 Mo
- `cgcreate -g cpu:batch && cgset -r cpu.shares=512 batch` — Alloue la moitié de la priorité CPU standard à un groupe de tâches de fond
**Origine :** Les control groups (cgroups) ont été développés par Paul Menage et Rohit Seth chez Google, intégrés au noyau Linux 2.6.24 en 2008.
**Subtilités/confusions :**
- cgroupsv1 et cgroupsv2 ont des hiérarchies et APIs radicalement différentes — systemd utilise cgroupsv2 par défaut depuis les distributions récentes.
- Les conteneurs Docker et Kubernetes utilisent les cgroups sous le capot pour l'isolation des ressources.
**Urgences/dangers :** —
**Précautions :** Préférer systemd-run avec `--property=MemoryLimit=` pour créer des cgroups via systemd sur les systèmes modernes plutôt que les outils libcgroup.
**Équivalents :** systemd-run (abstraction moderne), Docker --memory (abstraction conteneur)
**Voir aussi :** systemd-run, cgexec, systemctl, unshare

## `cgexec` — Execute in Control Group [Linux]
**Niveau :** expert | **Popularité :** 60 | **Aliases :** cgroup exec
**Contextes :** exécution de processus dans un cgroup existant, isolation de ressources
**Rôle :** Lance un processus dans un cgroup existant pour lui appliquer immédiatement les limites de ressources définies.
**Syntaxe :** `cgexec -g cpu,memory:<nom-cgroup> <commande>`
**Cas réguliers :**
- `cgexec -g memory:myapp python3 app.py` — Lance l'application Python dans le cgroup mémoire limitée
- `cgexec -g cpu:batch make -j8` — Compile un projet avec une priorité CPU réduite pour ne pas saturer le serveur
**Origine :** Partie de la suite `libcgroup-tools` développée en parallèle de l'introduction des cgroups dans le noyau Linux.
**Subtilités/confusions :**
- Le cgroup doit être préalablement créé avec `cgcreate` avant de pouvoir y exécuter un processus avec `cgexec`.
- Sur les systèmes systemd modernes, `systemd-run --scope --property=MemoryLimit=512M commande` est l'équivalent plus intégré.
**Urgences/dangers :** —
**Précautions :** Vérifier que le cgroup cible existe et a les bonnes permissions avant d'utiliser `cgexec`.
**Équivalents :** systemd-run (moderne), Docker/LXC run (abstraction)
**Voir aussi :** cgcreate, systemd-run, cgroups, unshare

## `prlimit` — Get/Set Process Resource Limits [Linux]
**Niveau :** avance | **Popularité :** 65 | **Aliases :** rlimit, resource limits
**Contextes :** tuning système, isolation de processus, limite de fichiers ouverts, débogage de ressources
**Rôle :** Affiche et modifie les limites de ressources d'un processus existant (fichiers ouverts, taille de pile, temps CPU, taille de fichier) via les rlimits du noyau.
**Syntaxe :** `prlimit --nofile=1024:4096 --pid <PID>` ou `prlimit --nofile=65536 commande`
**Cas réguliers :**
- `prlimit --nofile=65536 nginx` — Augmente la limite de fichiers ouverts pour un serveur Nginx avant son lancement
- `prlimit --pid 1234 --nofile` — Affiche la limite actuelle de fichiers ouverts du processus 1234
**Origine :** Basé sur l'appel système `prlimit(2)` introduit dans Linux 2.6.36 ; outil userland dans `util-linux`.
**Subtilités/confusions :**
- `prlimit` modifie les limites d'un processus existant via son PID — `ulimit` ne s'applique qu'au shell courant et à ses processus fils.
- Augmenter la soft limit au-delà de la hard limit nécessite CAP_SYS_RESOURCE.
**Urgences/dangers :** —
**Précautions :** Configurer les limites système via `/etc/security/limits.conf` ou les units systemd `LimitNOFILE=` pour les services persistants.
**Équivalents :** ulimit (shell uniquement), systemd LimitNOFILE (services)
**Voir aussi :** ulimit, systemctl, /proc/pid/limits

## `chsh` — Change Login Shell [Linux/macOS]
**Niveau :** debutant | **Popularité :** 70 | **Aliases :** change shell
**Contextes :** personnalisation de l'environnement utilisateur, migration vers zsh/fish, administration de comptes
**Rôle :** Modifie le shell de connexion par défaut d'un utilisateur dans `/etc/passwd`.
**Syntaxe :** `chsh -s <shell> [utilisateur]`
**Cas réguliers :**
- `chsh -s /bin/zsh` — Change le shell de l'utilisateur courant vers zsh
- `chsh -s /usr/bin/fish adolphe` — Définit fish comme shell de connexion pour l'utilisateur adolphe (nécessite sudo)
**Origine :** Commande Unix classique présente dans tous les systèmes POSIX depuis les premières versions de BSD.
**Subtilités/confusions :**
- Le nouveau shell doit être listé dans `/etc/shells` pour être accepté — ajouter manuellement le chemin sinon.
- Le changement prend effet à la prochaine connexion, pas dans le shell courant.
**Urgences/dangers :** —
**Précautions :** Vérifier que le shell cible est installé et fonctionnel avant de changer — un shell manquant empêche la connexion.
**Équivalents :** usermod -s (admin), modification directe de /etc/passwd
**Voir aussi :** passwd, useradd, usermod, /etc/shells

## `chpasswd` — Change Passwords in Batch [Linux]
**Niveau :** intermediaire | **Popularité :** 68 | **Aliases :** batch password change
**Contextes :** administration système, provisionnement automatisé d'utilisateurs, scripts d'intégration
**Rôle :** Met à jour les mots de passe de plusieurs utilisateurs en une seule opération en lisant des paires `utilisateur:motdepasse` depuis l'entrée standard.
**Syntaxe :** `echo "user:newpassword" | chpasswd` ou `chpasswd < fichier_users.txt`
**Cas réguliers :**
- `echo "deploy:SecretPass123!" | chpasswd` — Définit le mot de passe de l'utilisateur deploy depuis un script d'automatisation
- `chpasswd < /tmp/users_passwords.txt` — Met à jour les mots de passe de 100 utilisateurs depuis un fichier CSV
**Origine :** Outil PAM-aware du paquet `shadow-utils` présent dans les distributions Linux modernes.
**Subtilités/confusions :**
- `chpasswd` prend des mots de passe en clair et les hache automatiquement — le fichier d'entrée ne doit JAMAIS être laissé sur disque.
- Utiliser `-e` pour fournir des mots de passe déjà hachés (format shadow hash) au lieu de mots de passe en clair.
**Urgences/dangers :** ⚠️ Ne jamais écrire les mots de passe en clair dans un fichier persistant sur disque — utiliser des pipes ou des fichiers en RAM (`/dev/shm`).
**Précautions :** Effacer immédiatement le fichier de mots de passe et vider le cache du shell (`history -c`) après utilisation.
**Équivalents :** passwd (interactif, un utilisateur à la fois)
**Voir aussi :** passwd, useradd, usermod, /etc/shadow

## `grub-install` — Install GRUB Bootloader [Linux]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** grub2-install
**Contextes :** réparation de système non-amorçable, migration de disque, installation OS, configuration dual-boot
**Rôle :** Installe le chargeur de démarrage GRUB2 sur un disque ou une partition pour rendre le système amorçable.
**Syntaxe :** `grub-install [--target=x86_64-efi] <périphérique>`
**Cas réguliers :**
- `grub-install /dev/sda` — Installe GRUB en mode BIOS/MBR sur le premier disque dur
- `grub-install --target=x86_64-efi --efi-directory=/boot/efi /dev/sda` — Installe GRUB pour les systèmes UEFI
**Origine :** GRUB (GRand Unified Bootloader) développé par Erich Stefan Boleyn en 1995, maintenu par le projet GNU.
**Subtilités/confusions :**
- Systèmes BIOS/MBR vs UEFI/GPT nécessitent des paramètres `--target` différents — choisir le mauvais rend le système non amorçable.
- Après `grub-install`, toujours exécuter `update-grub` (Debian/Ubuntu) ou `grub-mkconfig -o /boot/grub/grub.cfg` pour régénérer la configuration.
**Urgences/dangers :** ⚠️ Une erreur d'installation GRUB sur le mauvais disque écrase le MBR/EFI et rend le système non amorçable — toujours vérifier le périphérique cible.
**Précautions :** Effectuer depuis un environnement chroot (`chroot /mnt/system`) ou depuis un live USB pour réparer un GRUB cassé.
**Équivalents :** efibootmgr (UEFI uniquement), syslinux (alternative légère)
**Voir aussi :** update-grub, efibootmgr, chroot, fdisk

## `update-grub` — Update GRUB Configuration [Linux]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** grub-mkconfig, grub2-mkconfig
**Contextes :** mise à jour du menu de démarrage après installation d'un noyau, ajout d'OS en dual-boot
**Rôle :** Régénère automatiquement le fichier de configuration GRUB (`/boot/grub/grub.cfg`) en détectant les noyaux installés et autres systèmes d'exploitation.
**Syntaxe :** `update-grub` (Debian/Ubuntu) ou `grub-mkconfig -o /boot/grub/grub.cfg`
**Cas réguliers :**
- `update-grub` — Régénère la configuration après installation d'un nouveau noyau Linux
- `grub-mkconfig -o /boot/grub/grub.cfg` — Équivalent multi-distributions de update-grub
**Origine :** Script wrapper Debian/Ubuntu autour de `grub-mkconfig` de GNU GRUB2.
**Subtilités/confusions :**
- `update-grub` est un alias Debian/Ubuntu — les distributions Red Hat/Fedora/Arch utilisent `grub-mkconfig -o /boot/grub2/grub.cfg`.
- La détection des OS du script `os-prober` doit être activée dans `/etc/default/grub` pour détecter Windows dans un dual-boot.
**Urgences/dangers :** —
**Précautions :** Vérifier `/boot/grub/grub.cfg` généré et tester le démarrage avant de redémarrer en production.
**Équivalents :** grub-mkconfig (équivalent direct)
**Voir aussi :** grub-install, efibootmgr, /boot, kernel

## `efibootmgr` — Manage UEFI Boot Entries [Linux]
**Niveau :** avance | **Popularité :** 75 | **Aliases :** EFI Boot Manager
**Contextes :** gestion des entrées de démarrage UEFI, ordre de boot, réparation UEFI, dual-boot
**Rôle :** Affiche et modifie les entrées de démarrage stockées dans la mémoire NVRAM UEFI du firmware de la carte mère.
**Syntaxe :** `efibootmgr -v` ou `efibootmgr -n <boot-num>` ou `efibootmgr -o 0003,0001`
**Cas réguliers :**
- `efibootmgr -v` — Affiche toutes les entrées de boot UEFI avec leurs chemins EFI complets
- `efibootmgr -o 0003,0001,0002` — Définit l'ordre de démarrage UEFI (Linux en premier, puis Windows)
**Origine :** Développé par Matt Domsch pour les systèmes Linux basés sur UEFI dès 2001.
**Subtilités/confusions :**
- efibootmgr ne modifie pas le fichier GRUB — il gère directement les entrées du firmware UEFI dans la NVRAM de la carte mère.
- La partition EFI (ESP) doit être montée sur `/boot/efi` pour que les modifications soient prises en compte.
**Urgences/dangers :** ⚠️ Supprimer l'entrée de boot active rend le système non amorçable — toujours garder une entrée de secours.
**Précautions :** Sauvegarder la liste des entrées (`efibootmgr -v > efi_backup.txt`) avant toute modification.
**Équivalents :** bcdedit (Windows), grub-install --efi-directory
**Voir aussi :** grub-install, update-grub, fdisk, /boot/efi

## `keyctl` — Kernel Key Management [Linux]
**Niveau :** expert | **Popularité :** 60 | **Aliases :** kernel keyring
**Contextes :** authentification PAM, LUKS/dm-crypt, Kerberos, sécurité des clés cryptographiques
**Rôle :** Accède et gère le trousseau de clés du noyau Linux (kernel keyring) pour stocker des secrets de manière sécurisée sans les exposer sur le système de fichiers.
**Syntaxe :** `keyctl add user mykey "myvalue" @u` ou `keyctl show @s`
**Cas réguliers :**
- `keyctl add user deploy_key "$(cat id_rsa)" @u` — Stocke une clé privée SSH dans le keyring utilisateur sécurisé
- `keyctl show @s` — Affiche les clés dans le keyring de la session courante
**Origine :** Implémenté dans le noyau Linux 2.6.10 par David Howells de Red Hat en 2004.
**Subtilités/confusions :**
- Les clés dans le keyring noyau ne sont JAMAIS écrites sur disque — elles existent uniquement en mémoire noyau protégée.
- Il existe plusieurs keyrings : `@u` (user), `@s` (session), `@p` (process), `@t` (thread) avec des durées de vie différentes.
**Urgences/dangers :** —
**Précautions :** Utiliser `keyctl timeout` pour définir une durée de vie aux clés sensibles et éviter qu'elles restent en mémoire indéfiniment.
**Équivalents :** gpg-agent (GPG), ssh-agent (SSH), HashiCorp Vault (enterprise)
**Voir aussi :** gpg, ssh-keygen, openssl, LUKS

## `lsof` — List Open Files [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** list open files
**Contextes :** debug de processus bloqués, audit de sécurité, diagnostic réseau, identification de fichiers verrouillés
**Rôle :** Liste tous les fichiers ouverts par les processus actifs — incluant fichiers réguliers, sockets réseau, pipes et fichiers spéciaux.
**Syntaxe :** `lsof [options]` ou `lsof -p <PID>` ou `lsof -i :80`
**Cas réguliers :**
- `lsof -i :443` — Identifie le processus qui écoute sur le port HTTPS 443
- `lsof -p 1234` — Liste tous les fichiers et sockets ouverts par le processus 1234
**Origine :** Développé par Victor A. Abell, distribué librement depuis 1994 pour tous les Unix/Linux.
**Subtilités/confusions :**
- Sous Linux, tout est fichier — `lsof` liste donc aussi les sockets réseau, les pipes, les périphériques et les espaces mémoire partagés.
- `lsof +D /mnt/usb` permet de trouver tous les processus utilisant un point de montage, indispensable avant un `umount`.
**Urgences/dangers :** —
**Précautions :** Exécuter avec sudo pour voir tous les processus — sans privilèges, seuls les fichiers des processus de l'utilisateur courant sont visibles.
**Équivalents :** ss -p (sockets), fuser (fichiers montés), /proc/pid/fd (accès direct)
**Voir aussi :** ss, netstat, fuser, /proc

## `dstat` — Versatile System Resource Statistics [Linux]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** dstat, resource monitor
**Contextes :** monitoring temps réel de performances système, benchmarking, diagnostic de goulots d'étranglement
**Rôle :** Affiche en temps réel des statistiques de ressources système (CPU, mémoire, E/S disque, réseau) combinées dans un tableau coloré et actualisé.
**Syntaxe :** `dstat [options]` ou `dstat -cdngy` ou `dstat --top-cpu`
**Cas réguliers :**
- `dstat -cdngy 1 10` — Affiche CPU, disque, réseau, pages et système toutes les secondes pendant 10 itérations
- `dstat --top-cpu --top-io` — Montre en continu les processus consommant le plus de CPU et d'E/S
**Origine :** Développé par Dag Wieers comme alternative améliorée à vmstat, iostat et netstat combinés.
**Subtilités/confusions :**
- `dstat` est souvent remplacé par `dool` sur les distributions récentes (fork maintenu activement) car dstat n'est plus maintenu.
- Les plugins dstat (--top-mem, --top-cpu, --mysql-status) étendent considérablement ses capacités.
**Urgences/dangers :** —
**Précautions :** Utiliser `dstat --output fichier.csv` pour enregistrer les métriques dans un fichier CSV exploitable pour des analyses ultérieures.
**Équivalents :** vmstat, iostat, sar (analyses ponctuelles), glances (interface TUI riche)
**Voir aussi :** vmstat, iostat, top, glances, sar

## `glances` — System Monitoring Tool [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** glances monitor
**Contextes :** monitoring système interactif, supervision de serveur distant, vue d'ensemble en temps réel
**Rôle :** Outil de monitoring système multiplateforme à interface TUI (ou API web) affichant CPU, mémoire, disque, réseau, processus et alertes en un seul écran.
**Syntaxe :** `glances` ou `glances -w` (mode serveur web) ou `glances --client <host>`
**Cas réguliers :**
- `glances` — Lance l'interface TUI interactive avec toutes les métriques système en un seul écran
- `glances -w && glances --client http://serveur:61208` — Mode client/serveur pour superviser des hôtes distants
**Origine :** Développé par Nicolas Hennion (Nicolargo) en Python, publié en 2011 sur GitHub.
**Subtilités/confusions :**
- `glances` peut être utilisé comme API REST (`-w`) permettant à des outils comme Grafana de collecter les métriques.
- En mode TUI, la couleur des métriques change selon les seuils (vert/bleu → jaune → rouge) pour signaler les problèmes de performance.
**Urgences/dangers :** —
**Précautions :** Installer glances avec le flag de plugins `pip install glances[all]` pour activer la supervision Docker, GPU et les exports vers InfluxDB.
**Équivalents :** htop (simplifié), atop (enregistrement), Netdata (web temps réel)
**Voir aussi :** htop, atop, dstat, top, Prometheus

## `atop` — Advanced System & Process Monitor [Linux]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** advanced top
**Contextes :** analyse de performance historique, post-mortem d'incident, monitoring continu de serveur
**Rôle :** Moniteur système avancé enregistrant toutes les métriques système (CPU, mémoire, disque, réseau, processus) sur disque pour permettre des analyses historiques après incident.
**Syntaxe :** `atop` ou `atop -r /var/log/atop/atop_YYYYMMDD` ou `atopsar -c`
**Cas réguliers :**
- `atop -r /var/log/atop/atop_20261001` — Rejoue les métriques enregistrées le 1er octobre 2026 pour investiguer un incident passé
- `atopsar -c 1 60` — Affiche les statistiques CPU agrégées par intervalle de 1 seconde sur 60 secondes
**Origine :** Développé par Gerlof Langeveld pour les systèmes Linux ; disponible sous licence GPL.
**Subtilités/confusions :**
- Contrairement à `top` qui affiche l'état instantané, `atop` enregistre les données en continu (daemon `atopd`) permettant une analyse rétrospective.
- `atop` utilise le format de log propriétaire `.adb` — non compatible avec les formats Prometheus/InfluxDB sans conversion.
**Urgences/dangers :** —
**Précautions :** Configurer la rétention des logs `atop` dans `/etc/default/atop` et surveiller l'espace disque consommé par les fichiers `.adb`.
**Équivalents :** sar (sysstat), glances -w (temps réel réseau), Prometheus (écosystème cloud)
**Voir aussi :** top, htop, glances, sar, vmstat

## `sysdig` — System Call Tracer and Monitor [Linux]
**Niveau :** expert | **Popularité :** 75 | **Aliases :** sysdig trace, cloud-native monitoring
**Contextes :** sécurité et forensique Linux, debug de conteneurs, audit de comportements applicatifs
**Rôle :** Capture et analyse les appels système et événements noyau avec un puissant langage de filtrage et de script pour la sécurité et le debugging avancé.
**Syntaxe :** `sysdig [filtre]` ou `sysdig -p "%evt.time %proc.name %fd.name" fd.type=file`
**Cas réguliers :**
- `sysdig proc.name=nginx and fd.type=file` — Surveille tous les accès fichiers du processus nginx en temps réel
- `sysdig -c spy_users` — Affiche tous les frappes clavier des sessions utilisateurs actives (chisel intégré)
**Origine :** Développé par la société Sysdig Inc. (Draios), fondée par Loris Degioanni, co-créateur de Wireshark en 2013.
**Subtilités/confusions :**
- `sysdig` capture au niveau du noyau (syscalls) et est beaucoup plus bas niveau que `strace` (un seul processus) ou `tcpdump` (réseau seulement).
- Falco (outil open source de Sysdig) utilise les mêmes mécanismes pour la détection de menaces en temps réel dans les clusters Kubernetes.
**Urgences/dangers :** ⚠️ `sysdig` capture potentiellement des secrets, mots de passe et données sensibles transmis via des appels système — ne jamais laisser tourner sans supervision.
**Précautions :** Limiter les captures via des filtres précis ; utiliser Falco plutôt que sysdig en continu sur des environnements de production.
**Équivalents :** strace (processus unique), bpftrace (eBPF moderne), auditd (audit noyau)
**Voir aussi :** strace, bpftrace, auditd, auditctl, tcpdump

## `pivot_root` — Pivot System Root Filesystem [Linux]
**Niveau :** expert | **Popularité :** 65 | **Aliases :** pivot root
**Contextes :** démarrage système initramfs, conteneurs, remplacement à chaud du système de fichiers racine
**Rôle :** Deplace le point de montage de la racine actuelle vers un répertoire temporaire et installe le nouveau répertoire comme nouvelle racine du système.
**Syntaxe :** `pivot_root <nouvelle_racine> <ancienne_racine_repertoire>`
**Cas réguliers :**
- `pivot_root . old_root` — Execution dans un initramfs pour basculer la racine temporaire en RAM vers la vraie racine sur disque
- `pivot_root /container_root /container_root/old_root` — Isolement d'un conteneur avec sa propre racine de système de fichiers
**Origine :** Appel système Linux `pivot_root(2)` introduit dans la version 2.3.41 pour le support du démarrage initrd.
**Subtilités/confusions :**
- `pivot_root` modifie la racine globale de tous les processus du namespace de montage courant, contrairement a `chroot` qui ne change la racine que pour le processus cible et ses enfants.
- `nouvelle_racine` et `ancienne_racine_repertoire` ne doivent pas être sur le même système de fichiers.
**Urgences/dangers :** ⚠️ Une mauvaise manipulation de pivot_root pendant le boot bloque l'initialisation du système et provoque un kernel panic.
**Précautions :** Apres pivot_root, démonter l'ancienne racine avec `umount -l /old_root` pour liberer la mémoire RAM de l'initramfs.
**Équivalents :** chroot (isolation de processus plus simple), switch_root (utilitaire d'initramfs)
**Voir aussi :** chroot, unshare, mount, initrd

## `pwconv` — Convert to Shadow Passwords [Linux]
**Niveau :** avance | **Popularité :** 60 | **Aliases :** shadow convert
**Contextes :** sécurité système, gestion des comptes utilisateurs, conversion shadow
**Rôle :** Active et convertit les mots de passe utilisateurs du fichier `/etc/passwd` vers le fichier chiffré et sécurisé `/etc/shadow`.
**Syntaxe :** `pwconv`
**Cas réguliers :**
- `pwconv` — Transfère les mots de passe hachés de `/etc/passwd` vers `/etc/shadow` et masque les empreintes dans `/etc/passwd` avec un 'x'
- `pwunconv` — Operation inverse (obsolete et déconseillée) restaurant les hachages directement dans `/etc/passwd`
**Origine :** Développé dans la suite `shadow-utils` pour masquer les hachages de mots de passe aux utilisateurs non privilégies.
**Subtilités/confusions :**
- `/etc/passwd` doit être lisible par tout le monde, alors que `/etc/shadow` n'est accessible que par root (mode 0600) — d'où l'importance vitale du shadow password.
- `pwconv` met aussi a jour les champs de péremption des mots de passe.
**Urgences/dangers :** ⚠️ Ne jamais exécuter `pwunconv` en production car cela réexpose les hachages de mots de passe dans `/etc/passwd` lisible par tous.
**Précautions :** Vérifier que `/etc/shadow` a des permissions strictes (root:root 0600 ou root:shadow 0640) après l'exécution.
**Équivalents :** grpconv (équivalent pour les groupes)
**Voir aussi :** grpconv, passwd, useradd, /etc/shadow

## `grpconv` — Convert to Shadow Groups [Linux]
**Niveau :** avance | **Popularité :** 58 | **Aliases :** gshadow convert
**Contextes :** sécurité système, gestion des groupes, masquage des mots de passe de groupes
**Rôle :** Active et synchronise les mots de passe et membres de groupes du fichier `/etc/group` vers le fichier sécurisé `/etc/gshadow`.
**Syntaxe :** `grpconv`
**Cas réguliers :**
- `grpconv` — Crée ou met a jour `/etc/gshadow` a partir de `/etc/group` et masque les mots de passe de groupes
- `grpunconv` — Desactive gshadow et remet les données dans `/etc/group`
**Origine :** Développé dans le paquet `shadow-utils` sous Linux.
**Subtilités/confusions :**
- Tout comme `/etc/shadow` pour les utilisateurs, `/etc/gshadow` stocke les mots de passe de groupes et administrateurs de groupes de façon protégée (mode 0640).
- Rarement utilisé directement au quotidien car géré automatiquement par les outils `groupadd` / `groupmod`.
**Urgences/dangers :** —
**Précautions :** S'assurer que les permissions de `/etc/gshadow` restent restreintes au groupe shadow ou root.
**Équivalents :** pwconv (pour les utilisateurs)
**Voir aussi :** pwconv, groupadd, groupmod, /etc/gshadow

## `sulogin` — Single User Login [Linux]
**Niveau :** avance | **Popularité :** 72 | **Aliases :** rescue login
**Contextes :** mode dépannage, secours système, démarrage en mode Single User / Emergency
**Rôle :** Invite l'administrateur a saisir le mot de passe root pour ouvrir un shell de secours lorsque le système démarre en mode dégrade ou d'urgence.
**Syntaxe :** `sulogin [device]`
**Cas réguliers :**
- `Démarrage systemd emergency.target` — Invoqué automatiquement par systemd quand une partition critique (/etc/fstab) échoue au montage
- `sulogin /dev/tty1` — Ouvre l'invite de mot de passe de secours sur la console virtuelle 1
**Origine :** Outil classique SysVinit / System V présent dans `util-linux` et intègre aux cibles de secours de systemd.
**Subtilités/confusions :**
- Si le compte root est verrouille ou sans mot de passe (comme sur Ubuntu par défaut), `sulogin` peut bloquer ou nécessiter le paramétrage de `SYSTEMD_SULOGIN_FORCE=1`.
- S'exécute généralement avec un système de fichiers racine monte en lecture seule.
**Urgences/dangers :** —
**Précautions :** Définir un mot de passe root fort pour éviter qu'un accès physique avec `init=/bin/sh` ou mode rescue n'ouvre une console sans authentification.
**Équivalents :** systemd-emergency.service
**Voir aussi :** systemctl, passwd, /etc/fstab, single

## `runlevel` — Print Current and Previous SysV Runlevel [Linux]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** init level
**Contextes :** administration système legacy, compatibilité SysVinit, vérification d'état système
**Rôle :** Affiche le niveau d'exécution (runlevel) précédent et actuel du système.
**Syntaxe :** `runlevel`
**Cas réguliers :**
- `runlevel` — Renvoie par exemple `N 3` (pas de niveau précédent, niveau actuel 3 multi-utilisateur texte) ou `3 5` (passage du mode texte au mode graphique)
- `Vérification mode maintenance` — Affiche `N 1` ou `N S` quand le système est en mode mono-utilisateur
**Origine :** Hérité du système System V Unix (SysVinit).
**Subtilités/confusions :**
- Sous systemd, les runlevels sont émulés par des cibles (targets) : Runlevel 3 = `multi-user.target`, Runlevel 5 = `graphical.target`, Runlevel 1 = `rescue.target`.
- Renvoie `N` pour le niveau précédent si le système n'a pas changé de niveau depuis le boot.
**Urgences/dangers :** —
**Précautions :** Utiliser `systemctl get-default` sur les systèmes modernes pour connaître la cible de démarrage au lieu de se fier a `runlevel`.
**Équivalents :** systemctl get-default, systemctl list-units --type=target
**Voir aussi :** telinit, systemctl, systemd, who -r

## `telinit` — Change SysV Runlevel [Linux]
**Niveau :** intermediaire | **Popularité :** 70 | **Aliases :** init runlevel change
**Contextes :** changement de mode d'exécution, basculement en mode maintenance, redémarrage legacy
**Rôle :** Envoie un signal au démon d'initialisation (`init` ou `systemd`) pour changer le niveau d'exécution du système.
**Syntaxe :** `telinit <0|1|2|3|4|5|6|S>`
**Cas réguliers :**
- `telinit 1` — Bascule le système en mode mono-utilisateur / maintenance pour effectuer des réparations
- `telinit 5` — Bascule en mode multi-utilisateur graphique avec gestionnaire de connexion (GDM/LightDM)
- `telinit 6` — Demande le redémarrage du système
**Origine :** Commande d'administration d'initialisation System V Unix.
**Subtilités/confusions :**
- Sur les systèmes systemd modernes, `telinit` est un lien symbolique vers `systemctl` qui traduit les chiffres de runlevel en cibles systemd (`telinit 3` → `systemctl isolate multi-user.target`).
- `telinit 0` arrête le système, `telinit 6` redémarre.
**Urgences/dangers :** ⚠️ `telinit 0` ou `telinit 6` coupe immédiatement les services sans avertissement préalable aux utilisateurs connectes.
**Précautions :** Privilégier `systemctl isolate <target>` ou `shutdown` pour une gestion propre des notifications et arrêts de services.
**Équivalents :** systemctl isolate, shutdown, reboot
**Voir aussi :** runlevel, systemctl, shutdown, systemd

## `kexec` — Direct Kernel Executive [Linux]
**Niveau :** expert | **Popularité :** 68 | **Aliases :** fast reboot, kexec-tools
**Contextes :** redémarrage rapide sans repasser par le BIOS/UEFI, kdump en cas de crash, serveurs haute disponibilité
**Rôle :** Charge et exécute un nouveau noyau Linux directement depuis le noyau en cours d'exécution, en ignorant l'étape d'initialisation matérielle BIOS/UEFI.
**Syntaxe :** `kexec -l /boot/vmlinuz --initrd=/boot/initrd.img --command-line="..."` puis `kexec -e`
**Cas réguliers :**
- `kexec -l /boot/vmlinuz-6.8.0 --initrd=/boot/initrd.img-6.8.0 --reuse-cmdline && kexec -e` — Redémarre sur un nouveau noyau en quelques secondes
- `kdump crash dump` — Chargement automatique d'un noyau de secours kdump en mémoire pour capturer un vmcore lors d'un Kernel Panic
**Origine :** Développé par Eric Biederman en 2002 et intègre au noyau Linux 2.6.13.
**Subtilités/confusions :**
- `kexec -l` charge le noyau en mémoire RAM ; `kexec -e` déclenche le saut effectif vers le nouveau noyau.
- Les périphériques matériels ne sont pas réinitialisés par le BIOS, ce qui peut poser des problèmes avec certains pilotes mal conçus.
**Urgences/dangers :** ⚠️ Si les pilotes des cartes réseau ou contrôleurs de stockage ne gèrent pas correctement le reset logiciel, la machine peut se bloquer au saut kexec.
**Précautions :** Toujours fermer les services et démonter les systèmes de fichiers (`systemctl kexec`) avant d'exécuter `kexec -e`.
**Équivalents :** systemctl kexec (wrapper sécurisé systemd)
**Voir aussi :** reboot, systemctl, crash, initrd

## `dracut` — Infrastructure for Building Initramfs Images [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** initramfs generator (Fedora/RHEL/Arch)
**Contextes :** génération d'images initramfs/initrd, mise a jour de noyau, support du chiffrement LUKS / LVM au boot
**Rôle :** Génère une image initramfs (initial RAM file system) contenant les pilotes et scripts nécessaires au démarrage du noyau Linux.
**Syntaxe :** `dracut [options] [<image-initramfs> [<version-noyau>]]`
**Cas réguliers :**
- `dracut --regenerate-all --force` — Régénère toutes les images initramfs pour tous les noyaux installes
- `dracut --add-drivers "nvme" /boot/initramfs-custom.img` — Génère une image en forçant l'inclusion des pilotes NVMe
**Origine :** Développé par Harald Hoyer chez Red Hat en 2009 pour remplacer `mkinitrd` et unifier la création d'initramfs entre distributions.
**Subtilités/confusions :**
- dracut est l'outil standard sur Red Hat, Fedora, CentOS, Rocky, SuSE et Arch, alors que Debian/Ubuntu utilise `update-initramfs` (mkinitramfs).
- dracut est hautement modulaire : les modules (luks, lvm, nfs, systemd) sont automatiquement inclus selon la configuration de la machine hôte (`--hostonly`).
**Urgences/dangers :** ⚠️ Régénérer une image initramfs incomplète (pilote de disque manquant) rend la machine incapable de monter la racine au boot.
**Précautions :** Toujours conserver une ancienne image initramfs fonctionnelle dans `/boot` avant de régénérer.
**Équivalents :** update-initramfs (Debian/Ubuntu), mkinitcpio (Arch Linux)
**Voir aussi :** mkinitcpio, update-grub, initrd, lsinitrd

## `mkinitcpio` — Modular Initramfs Creation Utility [Linux]
**Niveau :** avance | **Popularité :** 75 | **Aliases :** arch initramfs generator
**Contextes :** Arch Linux, Manjaro, génération d'images initramfs, personnalisation des hooks de démarrage
**Rôle :** Génère les images initramfs pour Arch Linux et ses dérivées en assemblant des hooks et des modules noyau spécifies dans `/etc/mkinitcpio.conf`.
**Syntaxe :** `mkinitcpio -p <preset>` ou `mkinitcpio -P` (tous les presets)
**Cas réguliers :**
- `mkinitcpio -P` — Régénère toutes les images d'initialisation pour tous les profils de noyaux installes (linux, linux-lts)
- `mkinitcpio -g /boot/initramfs-linux-custom.img -k 6.8.1-arch1-1` — Génère une image pour une version de noyau spécifique
**Origine :** Créé spécifiquement par et pour le projet Arch Linux pour remplacer l'ancien `mkinitrd`.
**Subtilités/confusions :**
- La configuration dans `/etc/mkinitcpio.conf` utilise des `HOOKS=(base udev autodetect modconf block encrypt lvm2 filesystems fsck)` dont l'ordre est critique.
- L'ordre des hooks dans `HOOKS=()` détermine la séquence exacte de chargement au boot (ex: `encrypt` doit précéder `lvm2`).
**Urgences/dangers :** ⚠️ Un ordre incorrect des HOOKS dans `/etc/mkinitcpio.conf` (ex: lvm2 avant encrypt) empêche le déchiffrement du disque au boot.
**Précautions :** Lancer `mkinitcpio -P` après toute modification de `/etc/mkinitcpio.conf` ou mise a jour du microcode processeur.
**Équivalents :** dracut (RHEL/Fedora), update-initramfs (Debian)
**Voir aussi :** dracut, pacman, initrd, grub-install

## `mokutil` — Machine Owner Key Utility [Linux]
**Niveau :** avance | **Popularité :** 73 | **Aliases :** MOK manager, UEFI Secure Boot keys
**Contextes :** UEFI Secure Boot, signature de modules noyau tiers (NVIDIA, VirtualBox, ZFS), gestion des clés MOK
**Rôle :** Gère la liste des clés MOK (Machine Owner Key) utilisées par le bootloader Shim pour valider et charger des modules noyau non signés officiellement sous UEFI Secure Boot.
**Syntaxe :** `mokutil [options]`
**Cas réguliers :**
- `mokutil --import MOK.der` — Enregistre une clé publique MOK personnalisée pour autoriser le chargement du pilote NVIDIA sous Secure Boot
- `mokutil --sb-state` — Affiche si UEFI Secure Boot est actuellement active ou désactive
**Origine :** Développé par Red Hat (Gary Ching-Pang Lin, Matthew Garrett) pour l'écosystème Shim / UEFI Secure Boot sous Linux.
**Subtilités/confusions :**
- `mokutil` prépare la demande d'enregistrement dans la NVRAM, mais l'enrôlement effectif de la clé nécessite de confirmer un mot de passe dans l'écran bleu MOK Management au redémarrage physique de la machine.
- Utile uniquement sur les systèmes démarrés en mode UEFI avec Secure Boot active.
**Urgences/dangers :** —
**Précautions :** Définir un mot de passe simple et temporaire lors de `mokutil --import` car le clavier dans l'écran MOK au reboot peut être en QWERTY US.
**Équivalents :** sbctl (Arch Linux Secure Boot key manager)
**Voir aussi :** efibootmgr, systemctl, Secure Boot, Shim

## `lsipc` — List IPC Facilities [Linux]
**Niveau :** avance | **Popularité :** 60 | **Aliases :** list inter-process communication
**Contextes :** administration système, audit de mémoire partagée, inspection des sémaphores et files de messages IPC
**Rôle :** Liste les ressources de communication inter-processus (IPC System V et POSIX) actives sur le système : mémoires partagées, sémaphores et files de messages.
**Syntaxe :** `lsipc [options]` ou `lsipc -m` (mémoire partagée)
**Cas réguliers :**
- `lsipc -m` — Liste les segments de mémoire partagée (shm) avec leurs tailles, identifiants (shmid) et PIDs créateurs
- `lsipc -s` — Affiche les ensembles de sémaphores System V actifs
**Origine :** Ajoute a la suite `util-linux` pour remplacer l'ancienne commande `ipcs` avec un formatage moderne et des options d'export.
**Subtilités/confusions :**
- `lsipc` fournit des informations plus claires et exportables (format JSON avec `-J`) que l'utilitaire traditionnel `ipcs`.
- Les segments de mémoire partagée orphelins (créés par des processus plantes) continuent de consommer de la RAM jusqu'à suppression avec `ipcrm`.
**Urgences/dangers :** —
**Précautions :** Examiner régulièrement les ressources IPC inutilisées consommant de la RAM sur les serveurs de base de données (PostgreSQL, Oracle).
**Équivalents :** ipcs (legacy), ipcmk, ipcrm
**Voir aussi :** ipcs, ipcrm, ipcmk, /proc/sysvipc

## `ipcmk` — Create IPC Resources [Linux]
**Niveau :** avance | **Popularité :** 55 | **Aliases :** make IPC resource
**Contextes :** développement C/C++, création de mémoires partagées pour tests, sémaphores
**Rôle :** Crée des ressources de communication inter-processus (IPC System V) : segments de mémoire partagée, sémaphores ou files de messages depuis la ligne de commande.
**Syntaxe :** `ipcmk -M <taille_octets>` ou `ipcmk -S <nb_semaphores>`
**Cas réguliers :**
- `ipcmk -M 1048576` — Crée un segment de mémoire partagée System V de 1 Mo et affiche son shmid
- `ipcmk -S 5` — Crée un ensemble de 5 sémaphores
**Origine :** Outil de la suite `util-linux` pour manipuler l'IPC System V en ligne de commande.
**Subtilités/confusions :**
- Le segment mémoire crée par `ipcmk` reste alloué en RAM jusqu'à sa suppression explicite via `ipcrm` ou le redémarrage du système.
**Urgences/dangers :** —
**Précautions :** Toujours supprimer le segment IPC avec `ipcrm -m <shmid>` après les tests pour éviter les fuites de mémoire RAM.
**Équivalents :** shmget / semget (appels système C)
**Voir aussi :** ipcs, ipcrm, lsipc, /dev/shm

## `ipcrm` — Remove IPC Resources [Linux]
**Niveau :** avance | **Popularité :** 68 | **Aliases :** remove IPC resource
**Contextes :** nettoyage de ressources IPC orphelines, débogage de bases de données, libération de mémoire RAM
**Rôle :** Supprime un segment de mémoire partagée, un ensemble de sémaphores ou une file de messages IPC System V ou POSIX.
**Syntaxe :** `ipcrm -m <shmid>` ou `ipcrm -s <semid>` ou `ipcrm -a` (tout supprimer)
**Cas réguliers :**
- `ipcrm -m 32768` — Supprime le segment de mémoire partagée identifié par le shmid 32768
- `ipcrm -s 65536` — Libère l'ensemble de sémaphores d'identifiant 65536
**Origine :** Commande Unix classique System V présente dans `util-linux`.
**Subtilités/confusions :**
- Un segment de mémoire partagée supprime avec `ipcrm` ne sera physiquement détruit que lorsque le dernier processus y étant attache se déconnectera.
- Nécessite d'être le propriétaire de la ressource IPC ou root pour pouvoir la supprimer.
**Urgences/dangers :** ⚠️ Supprimer un segment de mémoire partagée activement utilisé par une base de données en cours d'exécution (Oracle, PostgreSQL) provoque le crash de l'application.
**Précautions :** Vérifier avec `lsipc` ou `ipcs -p` qu'aucun processus n'est rattaché a la ressource avant de la supprimer.
**Équivalents :** lsipc, ipcs
**Voir aussi :** ipcs, lsipc, ipcmk, /dev/shm

## `ipcs` — Show IPC Facilities Status [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** IPC status
**Contextes :** diagnostic de bases de données, audit de mémoire partagée, inspection des ressources d'inter-processus
**Rôle :** Affiche des informations sur les ressources de communication inter-processus (IPC System V) actives : mémoires partagées, sémaphores et files de messages.
**Syntaxe :** `ipcs -a` ou `ipcs -m` (mémoire) ou `ipcs -u` (résumé d'utilisation)
**Cas réguliers :**
- `ipcs -m` — Liste les segments de mémoire partagée actifs, leurs clés (key), ID (shmid), propriétaire et taille
- `ipcs -p` — Affiche les PIDs des processus ayant crée ou modifié les ressources IPC
**Origine :** Commande standard POSIX / System V Unix présente sur tous les systèmes Unix.
**Subtilités/confusions :**
- `ipcs` affiche les ressources System V IPC — pour les objets POSIX IPC (shm_open), consulter `/dev/shm`.
- `lsipc` est l'alternative moderne recommandée sous Linux pour un affichage plus lisible et adaptable.
**Urgences/dangers :** —
**Précautions :** Utiliser `ipcs -l` pour consulter les limites maximales de mémoire partagée imposées par le noyau (`shmmax`, `shmall`).
**Équivalents :** lsipc (moderne), sysctl kernel.shmmax
**Voir aussi :** lsipc, ipcrm, ipcmk, sysctl

## `systemd-run` — Run Programs in Transient Systemd Units [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** systemd transient unit
**Contextes :** isolation ponctuelle de ressources, exécution de tâches en arrière-plan sous systemd, conteneurisation légère
**Rôle :** Lance une commande dans une unité éphémère (service ou scope) gérée par systemd, en lui appliquant des limites de ressources ou des contraintes de sécurité.
**Syntaxe :** `systemd-run [options] <commande> [args...]`
**Cas réguliers :**
- `systemd-run --property=MemoryMax=512M python3 script.py` — Exécute un script Python dans un service temporaire limite a 512 Mo de RAM
- `systemd-run --user -t bash` — Ouvre un shell interactif dans une unité éphémère utilisateur
**Origine :** Développé par Lennart Poettering dans le projet systemd (v209, 2014).
**Subtilités/confusions :**
- `--unit=<nom>` permet de nommer le service éphémère pour pouvoir le consulter avec `journalctl -u <nom>`.
- `--scope` exécute la commande de façon synchrone dans le shell courant plutôt que de créer un service d'arrière-plan autonome.
**Urgences/dangers :** —
**Précautions :** Utiliser `--remember` si vous souhaitez conserver l'état et les logs de l'unité éphémère après sa terminaison.
**Équivalents :** cgexec (cgroups direct), systemctl, nohup
**Voir aussi :** systemctl, journalctl, cgroups, systemd-cgls

## `systemd-cgls` — Recursively Show Control Group Contents [Linux]
**Niveau :** intermediaire | **Popularité :** 74 | **Aliases :** systemd cgroup list
**Contextes :** inspection de la hiérarchie cgroups, diagnostic de processus enfants, administration systemd
**Rôle :** Affiche sous forme d'arbre récursif la hiérarchie des control groups (cgroups) et les processus associés sous systemd.
**Syntaxe :** `systemd-cgls [unit|cgroup]`
**Cas réguliers :**
- `systemd-cgls` — Affiche l'arborescence complète des cgroups systemd avec tous les PIDs associés
- `systemd-cgls /system.slice/nginx.service` — Montre uniquement les processus et threads associés au service Nginx
**Origine :** Outil d'inspection de l'architecture cgroups intègre a systemd.
**Subtilités/confusions :**
- Montre exactement comment systemd organise la hiérarchie des processus en tranches (slices), services et sessions utilisateurs.
- Très utile pour trouver tous les processus fils dérivant d'un service systemd complexe.
**Urgences/dangers :** —
**Précautions :** Combiner avec `ps` ou `pstree` pour avoir les détails complets des arguments de ligne de commande.
**Équivalents :** systemd-cgtop (vue temps réel avec métriques), pstree -p
**Voir aussi :** systemd-cgtop, systemctl, ps, cgroups

## `systemd-cgtop` — Show Top Control Groups by Resource Usage [Linux]
**Niveau :** intermediaire | **Popularité :** 76 | **Aliases :** systemd cgroup top
**Contextes :** monitoring de consommation par service, identification de services gourmands, diagnostic systemd
**Rôle :** Affiche en temps réel les cgroups et services systemd classés par consommation de ressources (CPU, mémoire, E/S disque).
**Syntaxe :** `systemd-cgtop [options]`
**Cas réguliers :**
- `systemd-cgtop` — Affiche l'écran temps réel des services et cgroups classes par utilisation CPU
- `systemd-cgtop -m` — Trie la liste des services par consommation de mémoire RAM
**Origine :** Développé dans le projet systemd pour fournir un équivalent de `top` au niveau des services et cgroups.
**Subtilités/confusions :**
- Contrairement a `top` qui liste les processus individuels, `systemd-cgtop` cumule la consommation de TOUS les processus appartenant a un même service ou slice.
- Permet d'identifier immédiatement quel service systemd (ex: mariadb.service vs nginx.service) consomme les ressources du serveur.
**Urgences/dangers :** —
**Précautions :** Utiliser les touches `c` (CPU), `m` (Memory), `i` (IO) en mode interactif pour changer le critère de tri.
**Équivalents :** top / htop (par processus), glances
**Voir aussi :** systemd-cgls, top, htop, systemctl

## `systemd-inhibit` — Execute Program with Inhibition Lock [Linux]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** systemd inhibitor
**Contextes :** empêchement d'extinction/mise en veille pendant des sauvegardes ou mises a jour critiques
**Rôle :** Exécute une commande en posant un verrou d'inhibition auprès de systemd pour empêcher la mise en veille, l'extinction ou le changement d'état du système pendant l'opération.
**Syntaxe :** `systemd-inhibit --why="Raison" <commande>`
**Cas réguliers :**
- `systemd-inhibit --why="Sauvegarde en cours" rsync -a /data /backup` — Empêche la mise en veille ou l'arrêt automatique du serveur pendant le transfert rsync
- `systemd-inhibit --what=shutdown apt upgrade -y` — Bloque toute tentative d'extinction pendant une mise a jour majeure de paquets
**Origine :** Introduit dans systemd/logind (v183) pour gérer proprement les verrous d'inhibition d'état d'alimentation.
**Subtilités/confusions :**
- `--what=` accepte : `shutdown`, `sleep`, `idle`, `handle-power-key`, `handle-suspend-key`, `handle-lid-switch`.
- Un arrêt forcé par root avec `systemctl poweroff -i` outrepassera le verrou d'inhibition.
**Urgences/dangers :** —
**Précautions :** Toujours fournir une explication claire avec `--why=` pour que les administrateurs sachent pourquoi l'extinction est bloquée.
**Équivalents :** caffeinate (macOS)
**Voir aussi :** systemctl, shutdown, loginctl

## `systemd-nspawn` — Spawn a Namespace Container [Linux]
**Niveau :** avance | **Popularité :** 77 | **Aliases :** nspawn, systemd container
**Contextes :** conteneurisation légère, chroot amélioré, tests de distributions, debugging de boot
**Rôle :** Lance une commande ou un système d'exploitation complet dans un conteneur basé sur les namespaces Linux et cgroups, comme un chroot sous stéroïdes.
**Syntaxe :** `systemd-nspawn -D <repertoire-racine> [options]`
**Cas réguliers :**
- `systemd-nspawn -D /var/lib/machines/debian-tree -b` — Démarre un conteneur Debian complet avec son propre init systemd (boot complet)
- `systemd-nspawn -D /mnt/target apt update` — Exécute une commande dans une racine cible avec isolation réseau et système de fichiers automatique
**Origine :** Développé par Lennart Poettering dans le projet systemd pour les besoins d'intégration et de test.
**Subtilités/confusions :**
- `systemd-nspawn` monte automatiquement les systèmes de fichiers virtuels (`/proc`, `/sys`, `/dev`) et isole les namespaces — beaucoup plus propre et sûr qu'un `chroot` manuel.
- Ce n'est pas un remplacement direct de Docker/Podman pour la production, mais un outil formidable pour les builds et environnements de test OS.
**Urgences/dangers :** —
**Précautions :** Utiliser `-b` pour démarrer l'init du conteneur en mode boot complet ; utiliser `--private-network` pour isoler la pile réseau.
**Équivalents :** chroot (basique), LXC (conteneurs système), Docker (conteneurs applicatifs)
**Voir aussi :** chroot, unshare, machinectl, systemctl

## `systemd-resolve` — Resolve Hostnames and Service Records [Linux]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** resolvectl, systemd-resolved
**Contextes :** diagnostic DNS, inspection de la résolution de noms, vidage du cache DNS local, DNSSEC
**Rôle :** Interroge le service de résolution de noms local `systemd-resolved` pour résoudre des noms d'hôtes, adresses IP ou enregistrements DNSSEC.
**Syntaxe :** `systemd-resolve <hostname>` ou `resolvectl status`
**Cas réguliers :**
- `resolvectl status` — Affiche la configuration DNS détaillée par interface réseau (serveurs DNS, domaines de recherche, DNSSEC)
- `resolvectl flush-caches` — Vide immédiatement le cache DNS local maintenu par systemd-resolved
**Origine :** Déposé dans le cadre du composant `systemd-resolved` de la suite systemd.
**Subtilités/confusions :**
- `systemd-resolve` est renommé `resolvectl` sur les distributions récentes (systemd >= 239) — `systemd-resolve` reste présent comme lien symbolique.
- Interroge le cache local et les routeurs configurés via systemd-resolved, contrairement a `dig` qui interroge directement un serveur DNS spécifie en réseau.
**Urgences/dangers :** —
**Précautions :** Utiliser `resolvectl query example.com` pour tester la résolution exacte utilisée par les applications du système hôte.
**Équivalents :** dig, nslookup, host, getent hosts
**Voir aussi :** dig, nslookup, host, networkctl

## `arp-scan` — ARP Network Scanner [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** arp scanner
**Contextes :** découverte d'hôtes sur le réseau local, audit réseau, détection d'équipements connectes sans IP connue
**Rôle :** Envoie des requêtes ARP à toutes les adresses IP d'un sous-réseau local et affiche les adresses IP, MAC et fabricants des équipements qui répondent.
**Syntaxe :** `arp-scan [options] --interface=<iface> <cible-réseau>`
**Cas réguliers :**
- `arp-scan --localnet` — Scanne automatiquement l'ensemble du sous-réseau local associé a l'interface par défaut
- `arp-scan --interface=eth0 192.168.1.0/24` — Découvre tous les hôtes actifs sur le segment 192.168.1.0/24 via ARP
**Origine :** Développé par Roy Hills chez NTA Monitor, publié sous licence GPL.
**Subtilités/confusions :**
- `arp-scan` opère au niveau de la couche 2 (liaison de données) — il découvre les hôtes même si leur pare-feu local bloque les pings ICMP !
- Ne fonctionne que sur un segment de réseau local (niveau 2) ; ne peut pas traverser les routeurs.
**Urgences/dangers :** —
**Précautions :** Lancer avec privilèges root (ou CAP_NET_RAW) pour pouvoir émettre des trames ARP brutes.
**Équivalents :** nmap -sn (scan ICMP/ARP), fping -g
**Voir aussi :** arp, nmap, fping, ip neigh

## `tcpick` — TCP Stream Sniffer and Connection Tracker [Linux]
**Niveau :** avance | **Popularité :** 65 | **Aliases :** tcp stream capture
**Contextes :** analyse de trafic TCP, réassemblage de flux réseau, forensique, débogage de protocoles en texte clair
**Rôle :** Capture les paquets réseau TCP et réassemble les flux de données entre hôtes sous forme de texte ou de fichiers séparés.
**Syntaxe :** `tcpick -i <iface> "Cible-BPF"`
**Cas réguliers :**
- `tcpick -i eth0 -C -u "port 80"` — Affiche les conversations HTTP en clair en colorant les flux entrant et sortant
- `tcpick -i eth0 -wR "port 21"` — Extrait et sauvegarde les fichiers réassemblés transférés via une session FTP
**Origine :** Développé par Giuseppe D'Angelo en C pour l'analyse de flux réseau sous Linux.
**Subtilités/confusions :**
- `tcpick` est spécialisé dans le réassemblage visuel des sessions TCP texte — contrairement a `tcpdump` qui affiche paquet par paquet.
- Ne déchiffre pas les flux chiffrés TLS/HTTPS.
**Urgences/dangers :** ⚠️ La capture de flux réseau peut intercepter des identifiants confidentiels transmis en clair.
**Précautions :** Utiliser sur des réseaux d'audit autorisés avec des filtres BPF stricts pour cibler uniquement le trafic pertinent.
**Équivalents :** tshark (Wireshark CLI), tcpflow, ngrep
**Voir aussi :** tcpdump, tshark, ngrep, nc

## `ngrep` — Network Grep [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** network grep
**Contextes :** recherche de motifs dans le trafic réseau, inspection de paquets, debug d'APIs HTTP, SIP et DNS
**Rôle :** Applique la puissance des expressions régulières (grep) directement sur les trames réseau capturées en temps réel.
**Syntaxe :** `ngrep [options] '<regex>' '<filtre-bpf>'`
**Cas réguliers :**
- `ngrep -q -W byline 'GET|POST' 'port 80'` — Capture et affiche joliment les requêtes HTTP GET et POST en temps réel
- `ngrep -d eth0 'error' 'udp port 53'` — Recherche le terme 'error' dans les paquets DNS UDP sur eth0
**Origine :** Écrit par Jordan Ritter en 1999 pour combiner la simplicité de grep et la puissance de pcap.
**Subtilités/confusions :**
- `ngrep` prend deux arguments distincts : la regex pour le contenu applicatif, et le filtre BPF pcap pour le ciblage réseau (ex: 'port 80').
- Utiliser `-W byline` pour que les retours a la ligne des protocoles texte (HTTP, SIP) soient lisibles à l'écran.
**Urgences/dangers :** —
**Précautions :** Utiliser le flag `-q` (quiet) pour éviter l'affichage de points de progression lors du silence réseau.
**Équivalents :** tcpdump -A, tshark -Y
**Voir aussi :** tcpdump, tshark, grep, tcpick

## `vnstat` — Console Network Traffic Monitor [Linux]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** network traffic logger
**Contextes :** suivi de consommation de bande passante, statistiques réseau long terme, surveillance de quotas de données
**Rôle :** Enregistre en arrière-plan la consommation du trafic réseau (entrées/sorties) et génère des rapports par heure, jour, mois ou année.
**Syntaxe :** `vnstat [options]` ou `vnstat -d` (journalier) ou `vnstat -m` (mensuel)
**Cas réguliers :**
- `vnstat -l` — Affiche l'utilisation du débit réseau en temps réel à l'écran
- `vnstat -m` — Affiche le volume total de données transférées pour chaque mois écoulé
**Origine :** Développé par Teemu Toivola depuis 2002 sous licence GPL.
**Subtilités/confusions :**
- `vnstat` ne capture pas les paquets réseau (pas de surcharge CPU/RAM) — il lit périodiquement les statistiques d'interfaces fournies par le noyau dans `/proc/net/dev`.
- Conserve son historique dans une base SQLite légère (`/var/lib/vnstat/vnstat.db`).
**Urgences/dangers :** —
**Précautions :** S'assurer que le service `vnstat.service` est active pour que l'historique soit régulièrement alimente.
**Équivalents :** nload (temps réel uniquement), bmon, iftop
**Voir aussi :** nload, bmon, nethogs, iftop, ip

## `bmon` — Bandwidth Monitor and Rate Estimator [Linux/macOS]
**Niveau :** debutant | **Popularité :** 80 | **Aliases :** bmon monitor
**Contextes :** visualisation graphique en terminal de la bande passante, surveillance réseau multi-interfaces
**Rôle :** Affiche une vue graphique en caractères ASCII temps réel du débit entrant et sortant pour toutes les interfaces réseau.
**Syntaxe :** `bmon [options]`
**Cas réguliers :**
- `bmon` — Lance l'interface ncurses avec graphiques ASCII du débit réseau pour chaque carte
- `bmon -p eth0` — Concentre l'affichage uniquement sur l'interface eth0
**Origine :** Développé par Thomas Graf en C sous licence modifiée GPL/BSD.
**Subtilités/confusions :**
- Permet de visualiser sous forme de graphiques en barres ASCII l'évolution du trafic sans avoir besoin d'interface graphique (GUI).
- Affiche également les compteurs d'erreurs d'interfaces et de paquets abandonnés (drop).
**Urgences/dangers :** —
**Précautions :** Utiliser les flèches haut/bas pour naviguer entre les différentes interfaces réseau affichées.
**Équivalents :** nload, vnstat, iftop
**Voir aussi :** nload, vnstat, iftop, nethogs

## `nload` — Display Network Usage in Real Time [Linux/macOS]
**Niveau :** debutant | **Popularité :** 84 | **Aliases :** nload traffic monitor
**Contextes :** contrôle visuel rapide du débit réseau, suivi de transferts de fichiers, diagnostic de vitesse
**Rôle :** Affiche le débit entrant et sortant courant, moyen et maximal sous forme de deux graphiques ASCII séparés actualisés en temps réel.
**Syntaxe :** `nload [interfaces]`
**Cas réguliers :**
- `nload` — Ouvre le moniteur de débit temps réel sur l'interface par défaut
- `nload eth0 wlan0` — Permet de basculer entre eth0 et wlan0 avec les touches fléchées gauche/droite
**Origine :** Développé par Roland Riegel en C++ pour les systèmes Unix/Linux.
**Subtilités/confusions :**
- `nload` se concentre exclusivement sur la vitesse instantanée du débit (Incoming / Outgoing), contrairement a `vnstat` qui privilégie les volumes cumulés.
- Possibilité de régler les unités d'affichage (Bit/s vs Byte/s) via la touche `u`.
**Urgences/dangers :** —
**Précautions :** Utiliser `nload -u M` pour forcer l'affichage en Mégabytes/s au lieu de la conversion automatique.
**Équivalents :** bmon, iftop, vnstat -l
**Voir aussi :** bmon, vnstat, iftop, nethogs

## `iptstate` — Display IP Tables State Table [Linux]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** netfilter state monitor
**Contextes :** inspection des tables de suivi de connexions (conntrack), sécurité réseau, debug pare-feu iptables/nftables
**Rôle :** Affiche en temps réel l'état de la table de suivi de connexions de Netfilter (conntrack) dans un style similaire a `top`.
**Syntaxe :** `iptstate [options]`
**Cas réguliers :**
- `iptstate` — Affiche la liste des connexions actives suivies par le pare-feu avec leurs IP source/dest, ports et états (ESTABLISHED, TIME_WAIT)
- `iptstate -s` — Trie la liste des connexions par IP source pour identifier un hôte saturant les connexions
**Origine :** Développé par Phil Dibowitz pour inspecter la table conntrack de Netfilter sous Linux.
**Subtilités/confusions :**
- `iptstate` s'appuie sur le sous-système netfilter conntrack du noyau — si le module conntrack n'est pas charge, iptstate ne peut rien afficher.
- Permet de fermer (drop) une connexion active directement depuis l'interface interactive avec la touche `d`.
**Urgences/dangers :** —
**Précautions :** Nécessite les privilèges root pour accéder aux états conntrack du noyau.
**Équivalents :** conntrack -L (commande brute), netstat, ss
**Voir aussi :** iptables, nftables, ss, netstat

## `nethogs` — Net Top by Process Traffic [Linux]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** network top by process
**Contextes :** identification de processus gourmands en bande passante, diagnostic de consommation réseau inexplicable
**Rôle :** Règle le problème de savoir quel processus ou programme consomme la bande passante réseau en regroupant la vitesse de transfert par PID.
**Syntaxe :** `nethogs [interface]`
**Cas réguliers :**
- `nethogs` — Affiche le classement des processus consommant du débit sur toutes les interfaces
- `nethogs eth0` — Analyse uniquement le trafic transitant par l'interface eth0
**Origine :** Développé par Arnout Engelen en C++ pour Linux.
**Subtilités/confusions :**
- Contrairement a `iftop` qui classe le débit par adresse IP distante, `nethogs` classe le débit par processus local (PID et nom d'exécutable).
- Très efficace pour débusquer un processus d'arrière-plan (ex: mise a jour cachée, malware, rsync) qui sature la connexion.
**Urgences/dangers :** —
**Précautions :** Nécessite les privilèges root (ou CAP_NET_RAW + CAP_NET_ADMIN) pour associer les sockets réseau aux PIDs.
**Équivalents :** iftop (par IP), bmon (par interface), lsof -i
**Voir aussi :** iftop, bmon, nload, lsof, top

## `tcptrack` — Monitor TCP Connections on Network Interface [Linux]
**Niveau :** intermediaire | **Popularité :** 74 | **Aliases :** tcp connection track
**Contextes :** surveillance de connexions TCP actives, analyse de débits par session, diagnostic serveur web/base de données
**Rôle :** Affiche la liste des connexions TCP actives sur une interface réseau avec leurs adresses, ports, état et débit instantané.
**Syntaxe :** `tcptrack -i <iface> [filtre-bpf]`
**Cas réguliers :**
- `tcptrack -i eth0` — Affiche toutes les sessions TCP établies sur eth0 avec leur vitesse de transfert
- `tcptrack -i eth0 port 443` — Filtre uniquement les sessions HTTPS actives
**Origine :** Développé par Steve J. Kondik chez Information Security Partners.
**Subtilités/confusions :**
- `tcptrack` calcule le débit de chaque connexion TCP individuelle en temps réel par capture passive de trames pcap.
- Ne montre que les connexions TCP (pas le trafic UDP ou ICMP).
**Urgences/dangers :** —
**Précautions :** Sur un serveur avec des dizaines de milliers de connexions simultanées, le suivi tcptrack peut consommer une quantité significative de CPU.
**Équivalents :** iftop, iptstate, nethogs
**Voir aussi :** iftop, nethogs, iptstate, tcpdump

## `speedtest-cli` — Command Line Interface for Speedtest.net [Linux/macOS]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** speedtest
**Contextes :** mesure de débit Internet, test de bande passante montante/descendante, diagnostic de connexion distante
**Rôle :** Mesure la latence, le débit descendant (download) et le débit montant (upload) de la connexion Internet depuis le terminal via la plateforme Speedtest.net.
**Syntaxe :** `speedtest-cli [options]` ou `speedtest` (binaire officiel Ookla)
**Cas réguliers :**
- `speedtest-cli --simple` — Affiche rapidement Ping, Download et Upload de façon concorde
- `speedtest-cli --json` — Exporte le résultat des mesures de débit au format JSON pour intégration dans un script de monitoring
**Origine :** Développé par Matt Martz en Python ; complété plus tard par l'utilitaire natif officiel d'Ookla en C++.
**Subtilités/confusions :**
- `speedtest-cli` (script Python) peut plafonner sur les connexions très haut débit (> 500 Mbps) en raison des limites de Python — préférer le binaire officiel `speedtest` d'Ookla pour le Gigabit.
- Sélectionne automatiquement le serveur le plus proche géographiquement pour minimiser la latence.
**Urgences/dangers :** —
**Précautions :** Ne pas lancer pendant des transferts de données de production importants car le test consomme la totalité de la bande passante disponible pendant quelques secondes.
**Équivalents :** fast-cli (Fast.com / Netflix), iperf3 (test point-à-point privé)
**Voir aussi :** iperf3, ping, mtr, curl

## `shred` — Securely Overwrite a File to Hide Contents [Linux]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** secure delete file
**Contextes :** destruction sécurisée de fichiers sensibles, effacement de clés privées, nettoyage de disques avant réaffectation
**Rôle :** Écrase répétitivement un fichier avec des motifs de données aléatoires pour rendre sa récupération impossible par analyse forensique, puis le supprime facultativement.
**Syntaxe :** `shred [options] <fichier>`
**Cas réguliers :**
- `shred -u -n 3 secret.key` — Écrase 3 fois le fichier secret.key avec des données aléatoires puis le supprime (`-u`)
- `shred -v -z -n 5 /dev/sdb1` — Écrase une partition complète avec 5 passes d'aléatoire puis une passe finale de zéros (`-z`)
**Origine :** Fait partie du paquet `coreutils` de GNU, basé sur l'algorithme de Gutmann et les normes d'effacement du DoD.
**Subtilités/confusions :**
- Sur les SSD modernes et les systèmes de fichiers avec journalisation (ext4, btrfs, zfs), la réécriture physique sur le même emplacement n'est pas garantie en raison du wear leveling de la puce SSD.
- `shred` s'applique aux fichiers ou aux périphériques blocs bruts (`/dev/sdX`).
**Urgences/dangers :** ⚠️ Lancer `shred` sur un périphérique bloc (/dev/sda) détruit définitivement toutes les données sans confirmation ni possibilité de restauration.
**Précautions :** Pour effacer un SSD de façon sécurisée, utiliser la commande `blkdiscard` ou la fonction Secure Erase du contrôleur NVMe plutôt que `shred`.
**Équivalents :** srm, wipe, dd if=/dev/urandom
**Voir aussi :** srm, wipe, dd, SSD

## `srm` — Secure Remove [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 76 | **Aliases :** secure rm
**Contextes :** suppression sécurisée de fichiers et dossiers, remplacement sécurisé de `rm`
**Rôle :** Supprime des fichiers et répertoires en écrasant préalablement les zones mémoires occupées selon les normes de sécurité (DoD 5220.22-M ou Gutmann).
**Syntaxe :** `srm [options] <fichiers|dossiers>`
**Cas réguliers :**
- `srm -r /tmp/confidential_dir` — Supprime récursivement un dossier et tous ses fichiers en écrasant leurs données au préalable
- `srm -z file.txt` — Écrase le fichier avec des zéros après destruction pour masquer l'utilisation de srm
**Origine :** Développé par Matthew G. Marsh comme alternative sécurisée drop-in a la commande standard `rm`.
**Subtilités/confusions :**
- `srm` est un remplacement sécurisé direct de `rm` (supporte `-r`, `-f`) — il supprime le fichier ET son contenu physique sur disque.
- Propose 4 modes d'effacement : simple passe, DoD 7 passes, Gutmann 35 passes.
**Urgences/dangers :** ⚠️ Les fichiers supprimes avec `srm` sont irrécupérables — aucune corbeille ou outil d'undelete ne pourra les restaurer.
**Précautions :** Vérifier attentivement les chemins transmis avec `-r` pour éviter d'effacer accidentellement des dossiers système.
**Équivalents :** shred, wipe, rm (non sécurisé)
**Voir aussi :** shred, wipe, rm, dd

## `fdupes` — Find Duplicate Files [Linux/macOS]
**Niveau :** debutant | **Popularité :** 86 | **Aliases :** duplicate file finder
**Contextes :** nettoyage d'espace disque, déduplication de collections de fichiers, suppression de doublons
**Rôle :** Recherche les fichiers identiques (doublons) dans un ou plusieurs répertoires en comparant les tailles puis les empreintes MD5 et enfin le contenu octet par octet.
**Syntaxe :** `fdupes [options] <repertoire...>`
**Cas réguliers :**
- `fdupes -r /data/photos` — Cherche récursivement tous les fichiers en double dans le dossier photos
- `fdupes -rdN /data/downloads` — Recherche les doublons, supprime automatiquement les copies et conserve le premier fichier trouve sans confirmation (`-N`)
**Origine :** Écrit par Adrian Lopez en C sous licence MIT.
**Subtilités/confusions :**
- Compare les tailles d'abord, puis les hachages MD5 des fichiers de même taille, et enfin effectue une comparaison octet par octet pour garantir une correspondance à 100% sans faux positifs.
- L'option `-L` permet de remplacer les doublons par des liens durs (hardlinks) au lieu de les supprimer, économisant l'espace sans effacer de références.
**Urgences/dangers :** ⚠️ L'utilisation de l'option de suppression automatique `-d -N` doit être faite avec précaution pour ne pas effacer des copies légitimes voulues dans des arborescences distinctes.
**Précautions :** Toujours exécuter `fdupes -r` sans le flag `-d` en premier lieu pour inspecter la liste des doublons avant toute suppression.
**Équivalents :** rmlint (plus rapide, multithread), czkawka
**Voir aussi :** rm, ln, find, du

## `ncdu` — NCurses Disk Usage [Linux/macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** ncurses du, disk usage analyzer
**Contextes :** analyse d'occupation d'espace disque, nettoyage rapide de serveur, arborescence interactive
**Rôle :** Analyse l'utilisation de l'espace disque d'un répertoire et présente une interface ncurses interactive pour naviguer et supprimer les fichiers/dossiers volumineux.
**Syntaxe :** `ncdu [options] [repertoire]`
**Cas réguliers :**
- `ncdu /var` — Analyse interactive de l'espace disque du répertoire `/var` pour trouver les logs ou bases volumineuses
- `ncdu -x /` — Analyse la partition racine en restant sur un seul système de fichiers (`-x` évite de scanner les montages réseau/externe)
**Origine :** Développé par Yoran Heling en C (et réécrit en Zig) pour offrir un remplacement rapide et interactif a `du -sh *`.
**Subtilités/confusions :**
- Permet d'ordonner les dossiers par taille et d'effacer directement un dossier volumineux avec la touche `d` après confirmation.
- L'option `-x` est primordiale pour ne pas scanner inutilement les systèmes de fichiers virtuels (`/proc`, `/sys`) ou les points de montage NFS/CIFS distants.
**Urgences/dangers :** ⚠️ La touche `d` dans ncdu supprime définitivement le fichier/dossier sélectionné sur le disque.
**Précautions :** Exécuter avec `sudo ncdu -x /` pour que les répertoires restreints (ex: `/root`, `/var/lib/docker`) soient comptabilisés dans la taille.
**Équivalents :** du (brut), dua-cli, gdu (version Go ultra-rapide)
**Voir aussi :** du, df, fdupes, ls

## `wipe` — Secure File Wiping Utility [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 72 | **Aliases :** wipe file
**Contextes :** effacement sécurisé de fichiers, nettoyage forensique de partitions et disques
**Rôle :** Écrase les fichiers ou périphériques blocs avec des motifs spécifiques, détruit les métadonnées et désalloue les blocs pour empêcher la récupération de données.
**Syntaxe :** `wipe [options] <fichiers|peripheriques>`
**Cas réguliers :**
- `wipe -r /tmp/private_data` — Efface de manière sécurisée le dossier et tout son contenu récursif
- `wipe -q /dev/sdc1` — Efface rapidement une partition de disque dur en écrasant les structures de fichiers
**Origine :** Développé par Berke Durak pour les systèmes Unix/Linux.
**Subtilités/confusions :**
- `wipe` s'assure également de vider le cache écriture de la machine (fsync) pour garantir que les motifs d'écrasement sont physiquement écrits sur les plateaux magnétiques.
- Tout comme `shred`, l'efficacité sur SSD est limitée par la couche de Wear Leveling de la mémoire flash.
**Urgences/dangers :** ⚠️ Les données effacées par `wipe` ne peuvent en aucun cas être récupérées.
**Précautions :** Vérifier minutieusement le chemin du fichier ou du périphérique avant de valider la commande.
**Équivalents :** shred, srm, dd if=/dev/zero
**Voir aussi :** shred, srm, dd, SSD

## `scrub` — Disk and File Scrubbing Utility [Linux/macOS]
**Niveau :** avance | **Popularité :** 68 | **Aliases :** disk scrub
**Contextes :** conformité aux normes gouvernementales d'effacement de données, nettoyage de disques réreformés
**Rôle :** Écrase les fichiers ou les périphériques de stockage bruts en appliquant des motifs d'écriture conformes aux normes d'effacement officielles (NIST, DoD 5220.22-M, NNSA, Gutmann).
**Syntaxe :** `scrub [options] <fichier|peripherique>`
**Cas réguliers :**
- `scrub -p dod /dev/sdb` — Écrase l'intégralité du disque `/dev/sdb` selon le schéma de 7 passes de la norme DoD 5220.22-M
- `scrub -p gutmann confidential.pdf` — Écrase un fichier selon le schéma de 35 passes de Gutmann
**Origine :** Développé par Jim Garlick au Lawrence Livermore National Laboratory (LLNL).
**Subtilités/confusions :**
- Permet de choisir explicitement la norme de sécurité d'effacement via l'option `-p` (`dod`, `nnsa`, `gutmann`, `fillzero`).
- Particulièrement adapte pour la préparation des disques durs magnétiques avant mise au rebut ou retour sous garantie.
**Urgences/dangers :** ⚠️ L'effacement d'un disque entier avec scrub prend plusieurs heures et détruit irrémédiablement l'intégralité du contenu.
**Précautions :** S'assurer d'avoir sélectionné le bon disque cible (`/dev/sdX`) avec `lsblk` avant de lancer `scrub`.
**Équivalents :** shred, wipe, srm
**Voir aussi :** shred, wipe, srm, lsblk
