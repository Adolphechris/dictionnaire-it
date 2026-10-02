## `apt-get` — Outil d'installation de paquets bas niveau et scriptable [Debian/Ubuntu]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** automatiser l'installation de logiciels dans des Dockerfiles ou scripts Bash sans interaction utilisateur
**Rôle :** Outil de gestion des paquets Debian optimisé pour la stabilité et l'automatisation par script.
**Syntaxe :** `apt-get [options] <commande> [paquets]`
**Cas réguliers :**
- `apt-get update && apt-get install -y --no-install-recommends curl` — Installation minimale sans paquets recommandés optionnels (standard Docker)
- `apt-get purge apache2` — Supprimer un paquet ET tous ses fichiers de configuration globale dans `/etc/`
- `apt-get autoremove -y` — Supprimer automatiquement les dépendances orphelines devenues inutiles
**Origine :** Brian White / Debian Project (1998) — acronyme de « Advanced Package Tool Get ».
**Subtilités/confusions :**
- `apt-get remove` conserve les fichiers de configuration sous `/etc/`, tandis que `apt-get purge` efface aussi la configuration.
- L'option `--no-install-recommends` évite d'installer des centaines de mégaoctets de dépendances secondaires non strictly obligatoires.
**Urgences/dangers :** —
**Précautions :** Définir la variable d'environnement `DEBIAN_FRONTEND=noninteractive` devant `apt-get install` dans les scripts automatisés pour éviter d'être bloqué par une invite TUI.
**Équivalents :** apt, dnf, pacman, yum
**Voir aussi :** apt, apt-cache, dpkg

## `apt-cache` — Interrogation du cache des paquets APT [Debian/Ubuntu]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** rechercher les dépendances requises par un paquet, vérifier quelle version exacte d'un binaire est disponible dans les dépôts
**Rôle :** Interroger et effectuer des recherches dans la base de données de cache locale des paquets APT.
**Syntaxe :** `apt-cache <commande> [paquets]`
**Cas réguliers :**
- `apt-cache search postgresql` — Lister tous les paquets dont le nom ou la description contient "postgresql"
- `apt-cache show nginx` — Afficher les métadonnées détaillées d'un paquet (version, taille, mainteneur, description)
- `apt-cache policy docker-ce` — Afficher les versions disponibles dans les dépôts et la version actuellement installée
**Origine :** Debian Project (1998) — abréviation de « Advanced Package Tool Cache ».
**Subtilités/confusions :**
- `apt-cache` ne modifie rien sur le système et n'a pas besoin des privilèges `sudo`.
- `apt-cache policy` est la meilleure commande pour vérifier si un dépôt PPA ou tiers est bien pris en compte avec la bonne priorité (*pinning*).
**Urgences/dangers :** —
**Précautions :** Lancer `apt-get update` au préalable pour s'assurer que le cache local interrogé est bien à jour.
**Équivalents :** apt search / apt show, dnf search, pacman -Ss
**Voir aussi :** apt, apt-get, dpkg

## `apt-mark` — Gestion de l'état d'installation des paquets APT [Debian/Ubuntu]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** marquer un paquet comme installé manuellement pour éviter qu'il ne soit supprimé par `autoremove`, bloquer la mise à jour d'un paquet critique (*hold*)
**Rôle :** Modifier ou consulter les états de marquage des paquets installés (ex: auto, manual, hold).
**Syntaxe :** `apt-mark <commande> [paquets]`
**Cas réguliers :**
- `apt-mark hold linux-image-generic` — Verrouiller la version actuelle du noyau Linux pour empêcher toute mise à jour automatique
- `apt-mark unhold linux-image-generic` — Déverrouiller les mises à jour pour ce paquet
- `apt-mark showauto` — Afficher la liste de tous les paquets installés automatiquement en tant que dépendances
**Origine :** Debian Project (2009) — composant d'apt.
**Subtilités/confusions :**
- Un paquet en état `hold` ne sera PAS mis à jour par `apt upgrade`, ce qui évite les régressions non désirées.
- Marquer un paquet en `manual` empêche `apt autoremove` de le supprimer si plus aucune autre application ne le requiert.
**Urgences/dangers :** ⚠️ Oublier qu'un paquet est en `hold` peut masquer des correctifs de sécurité critiques majeurs.
**Précautions :** Lister régulièrement les paquets maintenus avec `apt-mark showhold`.
**Équivalents :** dnf mark, pacman -D
**Voir aussi :** apt, apt-get, dpkg

## `apt-file` — Recherche du paquet contenant un fichier spécifique [Debian/Ubuntu]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** trouver quel paquet apt installer lorsque la compilation d'un programme échoue avec un en-tête manquant (ex: `fatal error: pcre.h: No such file`)
**Rôle :** Indexer et rechercher le nom du paquet Debian/Ubuntu contenant un fichier donné, même si le paquet n'est pas encore installé sur la machine.
**Syntaxe :** `apt-file <commande> [motif]`
**Cas réguliers :**
- `apt-file update` — Télécharger la liste indexée de tous les fichiers contenus dans l'ensemble des paquets des dépôts
- `apt-file search pcre.h` — Trouver les paquets fournissant le fichier d'en-tête `pcre.h` (ex: `libpcre3-dev`)
- `apt-file list nginx` — Lister la totalité des fichiers qui seraient créés si le paquet `nginx` était installé
**Origine :** Sebastien J. Gross / Debian Project (2001) — outil incontournable pour les développeurs et sysadmins.
**Subtilités/confusions :**
- `dpkg -S` ne cherche que dans les paquets DÉJÀ installés sur la machine localement, alors que `apt-file search` cherche dans TOUS les paquets de tous les dépôts distants.
**Urgences/dangers :** —
**Précautions :** Toujours exécuter `apt-file update` après l'installation initiale de l'outil pour créer l'index de recherche local.
**Équivalents :** dnf provides, pacman -F
**Voir aussi :** dpkg, apt-cache, apt

## `dnf` — Gestionnaire de paquets moderne RPM [RHEL/Fedora/CentOS]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** installer et gérer des logiciels sous Fedora, Red Hat Enterprise Linux (RHEL 8/9), Rocky Linux ou AlmaLinux
**Rôle :** Gestionnaire de paquets de nouvelle génération pour les distributions Linux basées sur les fichiers RPM (remplaçant historique de `yum`).
**Syntaxe :** `dnf [options] <commande> [paquets]`
**Cas réguliers :**
- `dnf check-update && dnf upgrade -y` — Rechercher et installer toutes les mises à jour du système
- `dnf install -y httpd` — Installer le serveur web Apache et toutes ses dépendances
- `dnf provides /usr/bin/htop` — Trouver quel paquet fournit l'exécutable spécifié (équivalent de `apt-file search`)
**Origine :** Red Hat / Fedora (2015) — acronyme de « Dandified YUM », basé sur hawkey et libsolv pour une résolution de dépendances ultra-rapide.
**Subtilités/confusions :**
- `dnf history` permet de visualiser l'historique complet des transactions d'installations et d'annuler une opération précise avec `dnf history undo <ID>`.
- Sur RHEL 8+, la commande `yum` n'est plus qu'un simple lien symbolique redirigeant vers `dnf`.
**Urgences/dangers :** —
**Précautions :** Utiliser `dnf groupinstall "Development Tools"` pour installer d'un coup l'ensemble de la chaîne de compilation C/C++.
**Équivalents :** yum, apt (Debian/Ubuntu), pacman (Arch), zypper (SUSE)
**Voir aussi :** yum, rpm, dnf-plugins-core

## `apk` — Gestionnaire de paquets ultra-léger Alpine Linux [Alpine Linux]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** installer des paquets dans des conteneurs Docker ultra-légers basés sur Alpine Linux
**Rôle :** Gestionnaire de paquets principal de la distribution minimale Alpine Linux, conçu pour une vitesse d'exécution extrême.
**Syntaxe :** `apk <commande> [options] [paquets]`
**Cas réguliers :**
- `apk update && apk add --no-cache curl` — Mettre à jour l'index et installer `curl` sans conserver le cache sur disque (optimisé Docker)
- `apk del python3` — Supprimer un paquet et nettoyer les fichiers inutilisés
- `apk search -v 'nginx*'` — Rechercher les paquets disponibles correspondant au motif
**Origine :** Natanael Copa / Alpine Linux (2005) — acronyme de « Alpine Package Keeper ».
**Subtilités/confusions :**
- Le drapeau `--no-cache` évite de devoir exécuter `rm -rf /var/cache/apk/*` à la fin d'un Dockerfile.
- Alpine utilise la bibliothèque C `musl` au lieu de `glibc` : certains binaires précompilés Linux standards peuvent nécessiter `gcompat`.
**Urgences/dangers :** —
**Précautions :** Toujours spécifier `--no-cache` lors des installations dans les Dockerfiles Alpine pour minimiser la taille de l'image finale.
**Équivalents :** apt-get, dnf, pacman
**Voir aussi :** docker, musl

## `dpkg-deb` — Inspection et manipulation de fichiers d'archives .deb [Debian/Ubuntu]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** extraire le contenu d'un paquet `.deb` sans l'installer, inspecter le fichier de contrôle d'un paquet Debian
**Rôle :** Fabriquer, inspecter et extraire les composants des archives de paquets Debian (`.deb`).
**Syntaxe :** `dpkg-deb <option> <fichier.deb> [destination]`
**Cas réguliers :**
- `dpkg-deb -x package.deb /tmp/extracted` — Extraire le contenu complet du système de fichiers du paquet dans `/tmp/extracted`
- `dpkg-deb -I package.deb` — Afficher les informations de contrôle et scripts de pré/post installation (*Info*)
- `dpkg-deb -b my_folder package_new.deb` — Compiler un dossier contenant la structure Debian en un binaire `.deb` utilisable
**Origine :** Ian Murdock / Debian Project (1995) — utilitaire bas niveau manipulant le format d'archive `ar`.
**Subtilités/confusions :**
- Un fichier `.deb` est physiquement une archive `ar` contenant trois fichiers : `debian-binary`, `control.tar.gz` et `data.tar.gz`.
**Urgences/dangers :** —
**Précautions :** Utiliser `dpkg-deb -x` pour auditer un fichier de paquet douteux avant de l'installer réellement sur le système.
**Équivalents :** rpm2cpio (RHEL/Fedora), ar, tar
**Voir aussi :** dpkg, apt, debuild

## `rpm2cpio` — Extraction du contenu d'un paquet RPM sans installation [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** récupérer un binaire spécifique dans un paquet `.rpm` sans installer le paquet sur le système
**Rôle :** Convertir une archive de paquet RPM au format de flux d'archive d'entrée/sortie cpio.
**Syntaxe :** `rpm2cpio <paquet.rpm> | cpio -idmv`
**Cas réguliers :**
- `rpm2cpio package.rpm | cpio -idmv` — Décompresser et extraire tous les fichiers du paquet RPM dans le répertoire courant
- `rpm2cpio package.rpm | cpio -t` — Lister tous les fichiers contenus dans l'archive RPM sans les décompresser sur disque
**Origine :** Red Hat Linux (1997) — outil de conversion pour les pipelines POSIX.
**Subtilités/confusions :**
- Ne s'exécute généralement pas seul : `rpm2cpio` écrit le flux CPIO sur la sortie standard (`stdout`), qui doit être transmise par pipe `|` à la commande `cpio`.
**Urgences/dangers :** —
**Précautions :** Lancer la commande dans un sous-dossier temporaire vide (ex: `/tmp/rpm_extract`) pour éviter d'éparpiller les fichiers extraits.
**Équivalents :** dpkg-deb -x (Debian), cpio
**Voir aussi :** rpm, cpio, dnf

## `alien` — Convertisseur de formats de paquets Linux [Linux]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** —
**Contextes :** convertir un paquet au format `.rpm` en `.deb` pour l'installer sur Ubuntu, ou inversement
**Rôle :** Convertir les paquets entre les formats d'installation Linux Red Hat (`.rpm`), Debian (`.deb`), Stampede (`.slp`) et Slackware (`.tgz`).
**Syntaxe :** `alien [options] <fichier_paquet>`
**Cas réguliers :**
- `alien --to-deb package.rpm` — Convertir un fichier RPM en paquet Debian `.deb`
- `alien -i package.rpm` — Convertir ET installer directement le paquet converti sur le système courant
- `alien --to-rpm package.deb` — Convertir un paquet Debian en archive RPM
**Origine :** Joey Hess / Debian (1996) — outil de portabilité trans-distribution.
**Subtilités/confusions :**
- Utile pour les logiciels propriétaires anciens fournis uniquement sous un seul format binaire.
- Les scripts de pré/post installation spécifiques au gestionnaire d'origine ne sont pas toujours traduits de manière 100% fidèle.
**Urgences/dangers :** ⚠️ Ne jamais utiliser `alien` pour convertir des paquets de base système (kernel, libc) sous peine de rendre le système instable.
**Précautions :** Réserver `alien` aux applications isolées hors-dépôts.
**Équivalents :** dpkg-deb, rpm2cpio
**Voir aussi :** dpkg, rpm, apt

## `dnf-plugins-core` — Extensions d'administration dnf (copr, builddep) [RHEL/Fedora]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** ajouter un dépôt communautaire COPR sous Fedora/RHEL, installer automatiquement toutes les dépendances de compilation d'un code source
**Rôle :** Ensemble de modules d'extension officiels étendant les fonctionnalités du gestionnaire de paquets `dnf`.
**Syntaxe :** `dnf <commande_plugin> [options]`
**Cas réguliers :**
- `dnf copr enable user/project` — Activer un dépôt communautaire COPR (équivalent des PPA sous Ubuntu)
- `dnf builddep nginx.spec` — Télécharger et installer automatiquement l'intégralité des dépendances de compilation listées dans le fichier spec
- `dnf config-manager --add-repo <url_repo>` — Ajouter rapidement l'URL d'un nouveau dépôt de paquets dans `/etc/yum.repos.d/`
**Origine :** Fedora / Red Hat (2014) — remplace les anciens `yum-utils`.
**Subtilités/confusions :**
- La sous-commande `dnf config-manager --enable <repo_id>` permet d'activer un dépôt désactivé par défaut (ex: `powertools` ou `crb`).
**Urgences/dangers :** —
**Précautions :** S'assurer de la confiance envers un mainteneur COPR avant d'exécuter `dnf copr enable`.
**Équivalents :** add-apt-repository (Ubuntu), yum-utils
**Voir aussi :** dnf, rpm

## `cask` — Extension Homebrew pour la gestion d'applications GUI macOS [macOS]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** brew cask
**Contextes :** installer des applications graphiques macOS (Visual Studio Code, Docker Desktop, Google Chrome, Slack) en ligne de commande
**Rôle :** Extension de Homebrew permettant d'installer des applications macOS compilées (`.app`, `.dmg`, `.pkg`).
**Syntaxe :** `brew install --cask <nom_application>`
**Cas réguliers :**
- `brew install --cask visual-studio-code` — Télécharger et installer l'application VS Code dans `/Applications`
- `brew list --cask` — Lister toutes les applications GUI installées via Homebrew Cask
- `brew upgrade --cask` — Mettre à jour toutes les applications macOS graphiques installées
**Origine :** Paul Entwistle & Phinze / Homebrew (2013) — intégré directement au cœur de la commande `brew`.
**Subtilités/confusions :**
- Depuis Homebrew 2.7.0, `brew cask install foo` est déprécié au profit de la syntaxe unifiée `brew install --cask foo`.
- Place les exécutables dans le dossier système `/Applications`.
**Urgences/dangers :** —
**Précautions :** Utiliser `brew search --casks <nom>` pour vérifier le slug exact de l'application avant installation.
**Équivalents :** mas, winget, flatpak (Linux)
**Voir aussi :** brew, mas

## `pkgutil` — Inspection et extraction des paquets macOS (.pkg) [macOS]
**Niveau :** avance | **Popularité :** 81 | **Aliases :** —
**Contextes :** inspecter ou extraire les fichiers d'un installateur d'application macOS `.pkg` sans l'exécuter, oublier les révisions de paquets installés
**Rôle :** Query et modifier la base de données des paquets d'installateurs natifs macOS (`.pkg`).
**Syntaxe :** `pkgutil [options] <commande>`
**Cas réguliers :**
- `pkgutil --expand installer.pkg /tmp/expanded` — Extraire le contenu brut d'un fichier installateur macOS `.pkg`
- `pkgutil --pkgs` — Lister les identifiants de tous les paquets logiciels installés sur le système macOS
- `pkgutil --pkg-info com.apple.pkg.CLTools_Executables` — Afficher la version exacte et la date d'installation d'un composant Apple
**Origine :** Apple Inc. (macOS 10.5 Leopard, 2007).
**Subtilités/confusions :**
- L'option `pkgutil --forget <pkg_id>` supprime l'enregistrement d'installation de la base de données sans supprimer physiquement les fichiers.
**Urgences/dangers :** —
**Précautions :** Utiliser `pkgutil --expand` pour examiner les scripts d'installation (*preinstall* / *postinstall*) inclus dans les paquets `.pkg`.
**Équivalents :** dpkg-deb (Linux), installer (macOS)
**Voir aussi :** brew, hdiutil

## `flatpak-builder` — Outil de construction d'applications Flatpak [Linux]
**Niveau :** avance | **Popularité :** 75 | **Aliases :** —
**Contextes :** créer et packager une application Linux personnelle au format universel Flatpak depuis un manifeste YAML/JSON
**Rôle :** Outil de compilation et de packaging automatisé d'applications pour l'écosystème Flatpak à partir d'un manifeste source.
**Syntaxe :** `flatpak-builder [options] <dossier_build> <manifeste.json|yaml>`
**Cas réguliers :**
- `flatpak-builder build-dir org.example.App.json --force-clean` — Nettoyer le dossier et construire l'application selon le manifeste
- `flatpak-builder --run build-dir org.example.App.json my-app-binary` — Tester l'exécution du binaire dans l'environnement de sandbox construit
- `flatpak-builder --repo=my-repo build-dir org.example.App.json` — Exporter la construction vers un dépôt OSTree local
**Origine :** Alexander Larsson / GNOME & Red Hat (2016).
**Subtilités/confusions :**
- Télécharge automatiquement les dépendances et s'exécute dans un environnement de build isolé (*SDK runtime*).
**Urgences/dangers :** —
**Précautions :** Vérifier que les runtimes SDK correspondants (ex: `org.freedesktop.Sdk`) sont bien installés via Flatpak avant de lancer le build.
**Équivalents :** snapcraft, debuild, rpmbuild
**Voir aussi :** flatpak, snapcraft

## `snapcraft` — Outil de création et publication de paquets Snap [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** empaqueter un projet open-source au format Snap et le publier sur le Snap Store d'Ubuntu
**Rôle :** Outil en ligne de commande permettant de construire, tester et publier des paquets Snap à partir du fichier `snapcraft.yaml`.
**Syntaxe :** `snapcraft [commande] [options]`
**Cas réguliers :**
- `snapcraft` — Lire le fichier `snapcraft.yaml` dans le dossier courant et construire l'archive `.snap` (souvent via Multipass ou LXD)
- `snapcraft pack` — Compiler localement le paquet Snap sans lancer de conteneur d'isolation de build
- `snapcraft upload --release=stable my-app_1.0_amd64.snap` — Publier le fichier `.snap` directement sur le Snap Store officiel
**Origine :** Canonical / Ubuntu (2015).
**Subtilités/confusions :**
- Isole par défaut la compilation dans une machine virtuelle (Multipass) ou un conteneur (LXD) pour garantir la reproductibilité.
**Urgences/dangers :** —
**Précautions :** Tester le paquet localement avec `snap install --dangerous my-app.snap` avant de procéder au déploiement sur le Snap Store.
**Équivalents :** flatpak-builder, debuild, rpmbuild
**Voir aussi :** snap, flatpak-builder

## `debuild` — Outil de packaging et compilation de paquets Debian [Debian/Ubuntu]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** —
**Contextes :** compiler un paquet source Debian (`debian/control`, `debian/rules`) pour créer un paquet binaire `.deb` signé
**Rôle :** Wrapper d'empaquetage de la suite `devscripts` pour automatiser le nettoyage, la compilation et la signature GPG des paquets Debian.
**Syntaxe :** `debuild [options]`
**Cas réguliers :**
- `debuild -us -uc` — Compiler le paquet Debian sans signer le fichier `.changes` ni le paquet binaire (`-us` = unsigned source, `-uc` = unsigned changes)
- `debuild -b` — Compiler uniquement les binaires dépendants de l'architecture sans créer le paquet source
- `debuild clean` — Nettoyer les arborescences de compilation temporaires dans le dossier `debian/`
**Origine :** Julian Gilbey / Debian devscripts (1999).
**Subtilités/confusions :**
- Invoque en interne `dpkg-buildpackage`, `fakeroot`, `lintian` et `gpg`.
- Exécute automatiquement `lintian` à la fin de la compilation pour auditer le paquet contre les règles de politique Debian.
**Urgences/dangers :** —
**Précautions :** Corriger les avertissements et erreurs signalés par `lintian` à la fin de l'exécution de `debuild`.
**Équivalents :** rpmbuild, dpkg-buildpackage, snapcraft
**Voir aussi :** dpkg, dpkg-deb, apt

## `pnpm` — Gestionnaire de paquets JavaScript rapide et économe en espace [Cross]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** gérer les dépendances dans un Monorepo TypeScript/JavaScript sans dupliquer des gigaoctets dans `node_modules`
**Rôle :** Gestionnaire de paquets Node.js ultra-performant utilisant des liens durs (*hardlinks*) et symboliques vers un magasin centralisé.
**Syntaxe :** `pnpm <commande> [options] [paquets]`
**Cas réguliers :**
- `pnpm install` — Installer toutes les dépendances du projet en liant les paquets du store central
- `pnpm add -D typescript` — Ajouter TypeScript comme dépendance de développement
- `pnpm --filter web-app dev` — Exécuter un script spécifique au sein d'un monorepo pnpm-workspace
**Origine :** Zoltan Kochan (2016) — acronyme de « Performant npm ».
**Subtilités/confusions :**
- Contrairement à npm/yarn qui dupliquent les fichiers dans chaque projet, `pnpm` ne stocke chaque version de fichier qu'UNE SEULE FOIS sur le disque.
- Empêche l'accès aux dépendances fantômes (*phantom dependencies*) non déclarées dans le `package.json`.
**Urgences/dangers :** —
**Précautions :** Configurer un fichier `pnpm-workspace.yaml` pour l'administration propre des projets multi-paquets.
**Équivalents :** npm, yarn, bun
**Voir aussi :** npm, yarn, bun, npx

## `npx` — Exécuteur de paquets et binaires Node.js sans installation globale [Cross]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** initialiser un projet React/Next.js (`npx create-next-app`), lancer un binaire CLI une fois sans polluer la machine
**Rôle :** Exécuter des CLI et binaires de paquets npm directement depuis le registre distant sans installation permanente préalable.
**Syntaxe :** `npx <paquet_ou_binaire> [arguments]`
**Cas réguliers :**
- `npx create-next-app@latest my-app` — Générer une nouvelle application Next.js avec le dernier générateur officiel
- `npx eslint .` — Exécuter le linter ESLint local du projet sans installer ESLint en global
- `npx serve` — Démarrer un serveur HTTP statique temporaire dans le dossier courant
**Origine :** Kat Marchán / npm (2017) — intégré d'office avec npm v5.2.0+.
**Subtilités/confusions :**
- Cherche d'abord l'exécutable dans `./node_modules/.bin`, puis en global, et enfin le télécharge temporairement si absent.
- Utile pour garantir que tout le monde sur l'équipe utilise la version exacte de l'outil (`npx tool@1.2.3`).
**Urgences/dangers :** ⚠️ Exécuter `npx <script_inconnu>` télécharge et exécute immédiatement du code JS arbitraire en provenance de npm.
**Précautions :** Toujours vérifier le nom exact du paquet npm avant de lancer une commande `npx`.
**Équivalents :** bunx, pnpm dlx, yarn dlx
**Voir aussi :** npm, pnpm, bun

## `bun` — Runtime JavaScript tout-en-un et gestionnaire de paquets ultra-rapide [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** exécuter des scripts TypeScript/JS sans étape de transpilation Babel/tsc, remplacer `npm install` par une alternative 10x plus rapide
**Rôle :** Runtime JavaScript moderne, bundler, exécuteur de tests et gestionnaire de paquets tout-en-un basé sur JavaScriptCore (WebKit).
**Syntaxe :** `bun <run|install|test|build> [arguments]`
**Cas réguliers :**
- `bun install` — Installer les dépendances du `package.json` à une vitesse extrême
- `bun run index.ts` — Exécuter directement un fichier TypeScript sans configuration ni compilation préalable
- `bun test` — Lancer les tests unitaires avec le runner d'assertion ultra-rapide intégré
**Origine :** Jarred Sumner / Oven (2022) — écrit en Zig pour maximiser la vitesse d'exécution I/O et CPU.
**Subtilités/confusions :**
- Compatible avec le registre npm et la majorité des APIs Node.js et Web APIs standards (`fetch`, `WebSocket`).
- Génère un fichier de verrouillage binaire `bun.lockb` au lieu du JSON texte classique.
**Urgences/dangers :** —
**Précautions :** Tester les paquets ayant des modules natifs C++ Node-addon pour s'assurer de leur compatibilité avec Bun.
**Équivalents :** node, npm, pnpm, denon, tsx
**Voir aussi :** npm, pnpm, npx

## `pipenv` — Gestionnaire d'environnements virtuels et dépendances Python [Cross]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** gérer de manière déterministe les dépendances d'une application Python avec `Pipfile` et `Pipfile.lock`
**Rôle :** Outil unifiant `pip` et `virtualenv` pour isoler les packages Python et verrouiller les versions exactes.
**Syntaxe :** `pipenv <commande> [options]`
**Cas réguliers :**
- `pipenv install requests` — Créer l'environnement virtuel (si absent), installer `requests` et mettre à jour `Pipfile.lock`
- `pipenv run python script.py` — Exécuter un script Python au sein de l'environnement virtuel Pipenv isolé
- `pipenv shell` — Activer le Shell interactif de l'environnement virtuel courant
**Origine :** Kenneth Reitz & Python Packaging Authority (2017) — inspiré de Cargo (Rust) et Bundler (Ruby).
**Subtilités/confusions :**
- Remplace le traditionnel fichier `requirements.txt` par la paire `Pipfile` (lisible) et `Pipfile.lock` (empreintes cryptographiques sha256).
- Sépare proprement les dépendances de développement (`pipenv install --dev pytest`) des dépendances de prod.
**Urgences/dangers :** —
**Précautions :** Générer systématiquement le fichier `Pipfile.lock` avant le déploiement en production (`pipenv lock`).
**Équivalents :** poetry, uv, conda, venv
**Voir aussi :** pip, poetry, uv, conda

## `poetry` — Gestionnaire moderne de dépendances et de build Python [Cross]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** développer, empaqueter et publier une bibliothèque ou application Python respectant le standard PEP 518 (`pyproject.toml`)
**Rôle :** Outil tout-en-un de gestion des dépendances, des environnements virtuels et de la publication de paquets Python.
**Syntaxe :** `poetry <commande> [options]`
**Cas réguliers :**
- `poetry new my-package` — Créer l'arborescence complète d'un nouveau projet Python standardisé
- `poetry add fastapi uvicorn` — Résoudre et installer des dépendances tout en mettant à me jour `pyproject.toml`
- `poetry publish --build` — Compiler le paquet (wheel/sdist) et le publier directement sur PyPI
**Origine :** Sébastien Eustace (2018) — devenu la référence moderne pour la gestion de projets Python avec `pyproject.toml`.
**Subtilités/confusions :**
- Intègre un résolveur de dépendances déterministe ultra-strict évitant les conflits de sous-dépendances en cas de versions incompatibles.
- Ne nécessite pas de manipuler manuellement `activate` ou `virtualenv`.
**Urgences/dangers :** —
**Précautions :** Commiter les deux fichiers `pyproject.toml` et `poetry.lock` dans votre gestionnaire de version Git.
**Équivalents :** pipenv, uv, flit, hatch
**Voir aussi :** pip, pipenv, uv

## `pixi` — Gestionnaire de dépendances multi-langages rapide basé sur Conda [Cross]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** installer et isoler des projets scientifiques ou Data Science mélangeant du Python, C++, R et des binaires GPU CUDA
**Rôle :** Gestionnaire de dépendances et de projets ultra-rapide basé sur les dépôts Conda/prefix.dev et écrit en Rust.
**Syntaxe :** `pixi <commande> [options]`
**Cas réguliers :**
- `pixi init my-project` — Initialiser un projet avec le fichier manifeste `pixi.toml`
- `pixi add python numpy pytorch` — Ajouter des dépendances système et scientifiques résolues via conda-forge
- `pixi run start` — Exécuter une tâche définie dans le projet Pixi
**Origine :** prefix.dev / Wolf Vollprecht (2023) — basé sur la bibliothèque Rattler (Rust).
**Subtilités/confusions :**
- N'a pas besoin de l'installation lourde d'Anaconda/Miniconda : `pixi` est un binaire unique totalement autonome.
- Permet de cibler plusieurs environnements (ex: CPU vs GPU) au sein d'un même projet.
**Urgences/dangers :** —
**Précautions :** Préférer `pixi` à `conda` dans les pipelines CI/CD pour diviser le temps d'installation des dépendances par 10.
**Équivalents :** conda, poetry, uv
**Voir aussi :** conda, uv, poetry

## `go` — Outil de gestion des modules et compilateur Go [Cross]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** installer un outil CLI écrit en Go (`go install`), gérer les modules de dépendance d'un projet (`go mod`)
**Rôle :** L'outil universel de ligne de commande pour compiler, tester, formater et gérer les dépendances (modules) en langage Go.
**Syntaxe :** `go <commande> [arguments]`
**Cas réguliers :**
- `go mod init github.com/user/project` — Initialiser un nouveau module Go avec le fichier `go.mod`
- `go get github.com/gin-gonic/gin` — Télécharger et ajouter un module tiers dans les dépendances du projet
- `go install github.com/ffuf/ffuf/v2@latest` — Télécharger, compiler et installer un outil binaire Go dans `$GOPATH/bin`
**Origine :** Robert Griesemer, Rob Pike, Ken Thompson / Google (2009).
**Subtilités/confusions :**
- `go mod tidy` nettoie automatiquement le fichier `go.mod` en supprimant les modules inutilisés et en ajoutant les manquants.
- Produit des binaires exécutables autonomes statiques sans dépendances dynamiques système.
**Urgences/dangers :** —
**Précautions :** Lancer systématiquement `go mod tidy` et `go test ./...` avant de commiter des changements.
**Équivalents :** cargo (Rust), npm (Node), pip (Python)
**Voir aussi :** cargo, rustup

## `mix` — Outil de build et gestionnaire de dépendances Elixir [Cross]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** —
**Contextes :** créer une application web Phoenix ou un projet backend tolérant aux pannes en langage Elixir
**Rôle :** Outil d'automatisation de build, gestionnaire de dépendances (Hex) et runner de tests pour le langage Elixir.
**Syntaxe :** `mix <tâche> [arguments]`
**Cas réguliers :**
- `mix new my_app` — Générer la structure d'un nouveau projet Elixir
- `mix deps.get` — Télécharger toutes les dépendances déclarées dans `mix.exs` depuis le registre Hex.pm
- `mix phx.server` — Démarrer le serveur d'application Web Phoenix
**Origine :** José Valim / Elixir Core Team (2012).
**Subtilités/confusions :**
- Les dépendances et la configuration du projet sont rédigées en code Elixir natif dans le fichier `mix.exs`.
- Compile le code vers le bytecode BEAM de la machine virtuelle Erlang.
**Urgences/dangers :** —
**Précautions :** Utiliser `mix test` pour exécuter les doctests inclus directement dans la documentation du code.
**Équivalents :** cargo, rebar3 (Erlang), npm
**Voir aussi :** cargo, elixir

## `luarocks` — Gestionnaire de paquets pour le langage Lua [Cross]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** —
**Contextes :** installer des modules Lua (*rocks*) pour Neovim, Nginx OpenResty, Kong API Gateway ou des moteurs de jeux
**Rôle :** Gestionnaire de paquets officiel pour les modules et bibliothèques du langage Lua.
**Syntaxe :** `luarocks <commande> [options] [paquets]`
**Cas réguliers :**
- `luarocks install luasocket` — Télécharger et installer le module de socket réseau pour Lua
- `luarocks list` — Afficher la liste des roches (*rocks*) installées sur la machine
- `luarocks search json` — Chercher un module de traitement JSON dans le dépôt LuaRocks.org
**Origine :** Hisham Muhammad / Lua community (2007).
**Subtilités/confusions :**
- Peut installer des modules en mode système ou localement pour l'utilisateur courant (`--local`).
- Très utilisé pour étendre les fonctionnalités de la passerelle d'API Kong et du serveur Nginx/OpenResty.
**Urgences/dangers :** —
**Précautions :** Vérifier la version de Lua ciblée (Lua 5.1, 5.4 ou LuaJIT) car certains rocks ne sont pas compatibles avec toutes les révisions.
**Équivalents :** pip, npm, gem
**Voir aussi :** lua, nginx

## `cabal` — Gestionnaire de paquets et outil de build pour Haskell [Cross]
**Niveau :** avance | **Popularité :** 75 | **Aliases :** —
**Contextes :** développer, empaqueter et compiler des projets en langage fonctionnel Haskell
**Rôle :** Outil de ligne de commande pour construire et gérer les paquets de bibliothèques et applications Haskell via Hackage.
**Syntaxe :** `cabal <commande> [options]`
**Cas réguliers :**
- `cabal update` — Télécharger la dernière liste des paquets disponibles sur le registre Hackage
- `cabal build` — Compiler l'intégralité du projet Haskell courant et ses dépendances
- `cabal run` — Compiler et exécuter immédiatement l'application Haskell
**Origine :** Isaac Jones, Duncan Coutts et al. / Haskell community (2005) — acronyme de « Common Architecture for Building Applications and Libraries ».
**Subtilités/confusions :**
- `cabal.project` définit les options de build multi-paquets et les dépôts sources.
- Concurrencer ou compléter l'outil alternatif `stack`.
**Urgences/dangers :** —
**Précautions :** Lancer `cabal update` régulièrement pour synchroniser l'index des dépendances Hackage.
**Équivalents :** stack, cargo, ghc
**Voir aussi :** ghcup, cargo

## `opam` — Gestionnaire de paquets pour le langage OCaml [Cross]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** —
**Contextes :** installer le compilateur OCaml, gérer les bibliothèques et compilateurs spécifiques pour Coq, Dune ou Tezos
**Rôle :** Gestionnaire de paquets source flexible et multi-compilateurs pour le langage OCaml.
**Syntaxe :** `opam <commande> [options] [paquets]`
**Cas réguliers :**
- `opam init` — Initialiser l'environnement OPAM et créer le switch par défaut dans `~/.opam`
- `opam install dune utop` — Installer l'outil de build Dune et le Shell interactif utop
- `opam switch create 5.1.0` — Basculer ou créer un environnement isolé sous une version spécifique du compilateur OCaml
**Origine :** OCamlPro / OCaml core team (2012) — acronyme de « OCaml Package Manager ».
**Subtilités/confusions :**
- La fonction `switch` d'OPAM équivaut aux environnements virtuels (venv) ou gestionnaires de versions (pyenv/nvm).
- Compile les paquets depuis les sources en intégrant les dépendances système C natifs (`opam depext`).
**Urgences/dangers :** —
**Précautions :** Exécuter `eval $(opam env)` après l'initialisation pour mettre à jour les variables d'environnement dans le Shell courant.
**Équivalents :** cargo, cabal, dune
**Voir aussi :** dune, ocaml

## `nimble` — Gestionnaire de paquets du langage Nim [Cross]
**Niveau :** avance | **Popularité :** 72 | **Aliases :** —
**Contextes :** gérer les dépendances et automatiser la compilation de projets écrits en langage Nim
**Rôle :** Le gestionnaire de paquets et outil de build officiel pour l'écosystème du langage de programmation Nim.
**Syntaxe :** `nimble <commande> [options] [paquets]`
**Cas réguliers :**
- `nimble init` — Créer un nouveau projet avec le fichier de paquet `.nimble`
- `nimble install jester` — Télécharger et installer le framework web Jester
- `nimble build` — Compiler le projet Nim courant en binaire natif optimisé
**Origine :** Dominik Picheta / Nim core team (2012).
**Subtilités/confusions :**
- Utilise Git sous le capot pour récupérer directement les dépôts de paquets depuis GitHub/GitLab.
**Urgences/dangers :** —
**Précautions :** Déclarer les versions exactes requises dans le fichier `.nimble` (`requires "nim >= 2.0.0"`).
**Équivalents :** cargo, go, shards
**Voir aussi :** nim, cargo

## `shards` — Gestionnaire de dépendances pour le langage Crystal [Cross]
**Niveau :** avance | **Popularité :** 70 | **Aliases :** —
**Contextes :** installer des bibliothèques (shards) et compiler des applications écrites en langage Crystal
**Rôle :** Gestionnaire de dépendances officiel pour le langage Crystal basé sur le manifeste `shard.yml`.
**Syntaxe :** `shards <commande> [options]`
**Cas réguliers :**
- `shards install` — Télécharger et installer toutes les dépendances déclarées dans `shard.yml` et verrouiller dans `shard.lock`
- `shards check` — Vérifier si toutes les dépendances requises sont correctement installées
- `shards build` — Compiler les cibles d'exécutables définies dans le fichier de configuration
**Origine :** Manas Technology Solutions / Crystal community (2015).
**Subtilités/confusions :**
- Syntaxe du manifeste `shard.yml` très fortement inspirée du format `Gemfile` / `gemspec` de Ruby.
**Urgences/dangers :** —
**Précautions :** Commiter le fichier `shard.lock` dans le dépôt Git pour garantir la reproductibilité des builds.
**Équivalents :** gem, cargo, mix
**Voir aussi :** crystal, gem

## `repo` — Gestionnaire de dépôts Git multiples [Cross]
**Niveau :** avance | **Popularité :** 81 | **Aliases :** —
**Contextes :** administrer et synchroniser des projets géants composés de dizaines de dépôts Git (AOSP Android, Chromium)
**Rôle :** Outil écrit en Python au-dessus de Git pour simplifier le travail sur des projets répartis sur des dizaines de dépôts Git distincts.
**Syntaxe :** `repo <commande> [options]`
**Cas réguliers :**
- `repo init -u https://android.googlesource.com/platform/manifest` — Initialiser le client repo à partir d'un manifeste XML maître
- `repo sync -j8` — Synchroniser et mettre à jour en parallèle (8 threads) l'intégralité des sous-dépôts Git du projet
- `repo status` — Afficher l'état de modification de l'ensemble des dépôts contrôlés
**Origine :** Google / Android Open Source Project (AOSP) (2008).
**Subtilités/confusions :**
- `repo` n'est pas un remplaçant de Git, mais un outil d'orchestration piloté par un fichier manifeste XML (`manifest.xml`).
- Utilisé obligatoirement pour compiler Android OS ou le projet Chromium.
**Urgences/dangers :** —
**Précautions :** Passer le drapeau `-j` lors du `repo sync` pour paralléliser les téléchargements réseau.
**Équivalents :** git submodule, git-repo, git subtree
**Voir aussi :** git, git-submodule

## `rpmbuild` — Outil de construction de paquets binaires et sources RPM [Linux]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** compiler et empaqueter un binaire ou logiciel au format RPM officiel pour Red Hat, Fedora ou Rocky Linux
**Rôle :** Outil standard permettant de construire des paquets binaires (`.rpm`) et des paquets sources (`.src.rpm`) à partir d'un fichier de spécification (`.spec`).
**Syntaxe :** `rpmbuild <options> <fichier.spec>`
**Cas réguliers :**
- `rpmbuild -ba package.spec` — Compiler et générer à la fois le paquet binaire `.rpm` ET le paquet source `.src.rpm` (`-ba` = build all)
- `rpmbuild -bb package.spec` — Compiler uniquement le paquet binaire (`-bb` = build binary)
- `rpmbuild --rebuild package.src.rpm` — Recompiler directement un paquet source `.src.rpm` téléchargé
**Origine :** Erik Troan / Red Hat (1997) — autrefois intégré directement dans la commande `rpm`.
**Subtilités/confusions :**
- L'arborescence de travail par défaut se trouve dans `~/rpmbuild/` (avec les sous-dossiers `BUILD`, `RPMS`, `SOURCES`, `SPECS`, `SRPMS`).
- Le fichier `.spec` décrit les étapes `%prep`, `%build`, `%install` et les fichiers inclus `%files`.
**Urgences/dangers :** —
**Précautions :** Ne JAMAIS lancer `rpmbuild` avec les privilèges `sudo` ou compte root : toujours compiler en utilisateur simple dans son `HOME`.
**Équivalents :** debuild, dpkg-buildpackage, mock, flatpak-builder
**Voir aussi :** rpm, dnf, debuild

## `pyenv` — Gestionnaire de versions multiples pour Python [Cross]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** faire tourner plusieurs versions de Python (3.9, 3.11, 3.12) sur le même poste sans altérer le Python du système d'exploitation
**Rôle :** Basculer facilement entre plusieurs versions de Python installées côte à côte par utilisateur ou par répertoire de projet.
**Syntaxe :** `pyenv <commande> [options]`
**Cas réguliers :**
- `pyenv install 3.12.1` — Télécharger et compiler la version Python 3.12.1 dans `~/.pyenv/versions/`
- `pyenv local 3.12.1` — Fixer la version Python du projet courant via la création d'un fichier `.python-version`
- `pyenv global 3.11.0` — Définir la version Python par défaut pour l'utilisateur sur l'ensemble de la machine
**Origine :** Yamashita Yuu (2013) — basé sur la philosophie rbenv (Ruby).
**Subtilités/confusions :**
- `pyenv` ne remplace pas `virtualenv` ou `venv`, il gère la version du BINAIRE Python lui-même.
- Nécessite d'ajouter les shims `~/.pyenv/shims` en tête du `$PATH` Shell dans `.bashrc` / `.zshrc`.
**Urgences/dangers :** —
**Précautions :** Installer les bibliothèques d'en-tête C de développement (`libssl-dev`, `zlib1g-dev`) avant de compiler de nouvelles versions Python avec `pyenv install`.
**Équivalents :** asdf, mise, conda, uv
**Voir aussi :** pip, venv, venv, poetry

## `rbenv` — Gestionnaire de versions légères pour Ruby [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** exécuter des projets Ruby on Rails nécessitant des révisions précises de l'interpréteur Ruby
**Rôle :** Gérer les environnements d'exécution multi-versions Ruby de manière simple, transparente et non-intrusive.
**Syntaxe :** `rbenv <commande> [options]`
**Cas réguliers :**
- `rbenv install 3.3.0` — Installer la version Ruby 3.3.0 (via le plugin `ruby-build`)
- `rbenv local 3.3.0` — Définir la version Ruby spécifique pour le dossier courant (`.ruby-version`)
- `rbenv rehash` — Régénérer les shims après l'installation de nouvelles gemmes contenant des exécutables CLI
**Origine :** Sam Stephenson / Basecamp (2011) — créé pour offrir une alternative plus épurée à RVM.
**Subtilités/confusions :**
- Utilise des scripts exécutables "shims" légers pour intercepter les appels aux binaires `ruby`, `gem` et `bundle`.
- Ne modifie pas la commande `cd` ni les variables d'environnement globales.
**Urgences/dangers :** —
**Précautions :** Toujours vérifier avec `rbenv version` la version active dans le terminal courant.
**Équivalents :** rvm, asdf, chruby
**Voir aussi :** gem, bundler, rvm

## `rvm` — Environnement complet de gestion de versions et gemsets Ruby [Cross]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** administrer de grands projets Ruby on Rails historiques nécessitant à la fois une version Ruby et un ensemble de gemmes isolé (*gemsets*)
**Rôle :** Outil complet de gestion des versions de l'interpréteur Ruby et de leurs collections de dépendances associées.
**Syntaxe :** `rvm <commande> [options]`
**Cas réguliers :**
- `rvm install 3.2.2` — Télécharger et compiler la version Ruby 3.2.2
- `rvm use 3.2.2@my_project --create` — Basculer sur Ruby 3.2.2 et créer un jeu de gemmes isolé nommé `my_project`
- `rvm list` — Afficher la liste de toutes les versions Ruby installées via RVM
**Origine :** Wayne E. Seguin (2007) — acronyme de « Ruby Version Manager ».
**Subtilités/confusions :**
- S'écarte du comportement Shell standard en surchargeant la fonction `cd` du Shell pour détecter les fichiers `.rvmrc`.
- Gère la notion de `gemset` pour isoler les bibliothèques sans avoir besoin de Bundler.
**Urgences/dangers :** —
**Précautions :** Charger RVM sous forme de fonction Shell dans `.bashrc` ou `.zshrc` (`source ~/.rvm/scripts/rvm`).
**Équivalents :** rbenv, chruby, asdf
**Voir aussi :** rbenv, gem

## `sdkman` — Gestionnaires des kits de développement Software Development Kit (Java, Kotlin, Scala, Gradle) [Cross]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** sdk
**Contextes :** installer et faire cohabiter plusieurs versions de JDK Java (Open JDK 8, 11, 17, 21), Gradle, Maven ou Spring Boot sur sa machine
**Rôle :** Outil CLI pour gérer les versions parallèles de multiples SDKs pour l'écosystème JVM sur systèmes Unix.
**Syntaxe :** `sdk <commande> [candidate] [version]`
**Cas réguliers :**
- `sdk install java 21.0.1-tem` — Installer la version JDK 21 de Temurin (Eclipse Adoptium)
- `sdk use java 17.0.9-tem` — Basculer la version Java du terminal courant sur le JDK 17
- `sdk default gradle 8.5` — Définir la version par défaut de Gradle pour toute la machine
**Origine :** Marco Vermeulen (2012) — autrefois appelé GVM (Groovy enVironment Manager).
**Subtilités/confusions :**
- Supporte un éventail impressionnant de candidats : `java`, `gradle`, `maven`, `kotlin`, `scala`, `groovy`, `micronaut`.
- Modifie dynamiquement les variables d'environnement `$JAVA_HOME` et `$PATH`.
**Urgences/dangers :** —
**Précautions :** Exécuter `sdk update` régulièrement pour maintenir l'index des versions distantes JDK à jour.
**Équivalents :** jenv, jabba, asdf
**Voir aussi :** java, javac, maven, gradle

## `rustup` — Installateur et gestionnaire de toolchains pour le langage Rust [Cross]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** installer le compilateur Rust (`rustc`), la bibliothèque standard, l'outil de build `cargo` ou cibler une compilation croisée (WebAssembly, ARM)
**Rôle :** Gestionnaire officiel des chaînes de compilation (*toolchains*) du langage de programmation Rust.
**Syntaxe :** `rustup <commande> [options]`
**Cas réguliers :**
- `rustup update` — Mettre à jour toutes les chaînes de compilation Rust installées (stable, beta, nightly)
- `rustup target add wasm32-unknown-unknown` — Ajouter la cible de compilation WebAssembly pour générer du Wasm
- `rustup override set nightly` — Forcer l'utilisation de la version Rust Nightly uniquement pour le dossier du projet courant
**Origine :** Diggory Blake, Alex Crichton / Rust Core Team (2016).
**Subtilités/confusions :**
- Gère automatiquement les trois canaux de publication : `stable`, `beta` et `nightly`.
- Installe également la documentation hors-ligne complète de Rust (ouvrable avec `rustup doc`).
**Urgences/dangers :** —
**Précautions :** Exécuter `rustup component add clippy rustfmt` pour installer les outils officiels de linter et formatage de code.
**Équivalents :** ghcup, pyenv, asdf
**Voir aussi :** cargo, rustc

## `ghcup` — Gestionnaire de chaînes de compilation Haskell [Cross]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** —
**Contextes :** installer et gérer les versions du compilateur Haskell GHC, de l'outil de build Cabal et du serveur de langage HLS
**Rôle :** Outil d'installation principal recommandé pour les outils de développement du langage fonctionnel Haskell (GHC, Cabal, Stack, HLS).
**Syntaxe :** `ghcup <commande> [options]`
**Cas réguliers :**
- `ghcup tui` — Ouvrir l'interface graphique en mode texte (TUI) interactive pour installer/activer les versions de GHC et Cabal
- `ghcup install ghc 9.6.3` — Télécharger et installer la version 9.6.3 du compilateur GHC
- `ghcup set ghc 9.6.3` — Activer la version 9.6.3 du compilateur GHC pour l'utilisateur courant
**Origine :** Julian Ospald (hasufell) / Haskell Foundation (2018).
**Subtilités/confusions :**
- L'interface TUI lancée via `ghcup tui` est l'un des moyens les plus simples et visuels pour piloter les environnements Haskell sous Linux/macOS.
**Urgences/dangers :** —
**Précautions :** Vérifier que HLS (*Haskell Language Server*) correspond exactement à la version du compilateur GHC sélectionné.
**Équivalents :** rustup, sdkman, asdf
**Voir aussi :** cabal, stack

## `asdf` — Gestionnaire de versions universel extensible par plugins [Cross]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** remplacer 10 gestionnaires de versions séparés (nvm, pyenv, rbenv, sdkman) par un seul outil universel unifié
**Rôle :** CLI de gestion de versions polyglotte permettant d'administrer les runtimes de multiples langages via des plugins.
**Syntaxe :** `asdf <commande> [plugin] [version]`
**Cas réguliers :**
- `asdf plugin add nodejs` — Ajouter le plugin de gestion des versions pour Node.js
- `asdf install nodejs 20.10.0` — Télécharger et installer la version Node.js 20.10.0
- `asdf local nodejs 20.10.0` — Écrire la version requise dans le fichier `.tool-versions` du projet courant
**Origine :** Rishabh Chhabra / HashiCorp & Open Source (2015).
**Subtilités/confusions :**
- Repose sur un fichier texte central par projet `.tool-versions` listant toutes les versions de tous les langages du projet.
- Nécessite d'exécuter `asdf reshim` après l'installation de nouveaux paquets globaux.
**Urgences/dangers :** —
**Précautions :** Installer les plugins officiels validés par la communauté pour garantir des téléchargements sécurisés.
**Équivalents :** mise, proto, rtx
**Voir aussi :** mise, pyenv, rbenv, nvm

## `mise` — Remplaçant ultra-rapide de asdf écrit en Rust [Cross]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** rtx
**Contextes :** gérer les versions de runtimes (Node, Python, Ruby, Go) et les variables d'environnement de projet avec des performances maximales
**Rôle :** Gestionnaire de versions et d'environnement polyglotte haute performance (anciennement appelé `rtx`), compatible avec asdf.
**Syntaxe :** `mise <commande> [arguments]`
**Cas réguliers :**
- `mise use node@20 python@3.12` — Définir et installer instantanément Node 20 et Python 3.12 pour le projet courant
- `mise ls` — Afficher tous les outils installés, leurs versions actives et leurs sources
- `mise run build` — Exécuter des tâches configurées directement dans le manifeste `.mise.toml`
**Origine :** Jeff Dickey (2023) — réécriture en Rust d'asdf pour éliminer les temps de latence des shims Bash.
**Subtilités/confusions :**
- Compatible à 100% avec les fichiers `.tool-versions` d'asdf et les fichiers `.python-version` / `.node-version`.
- Injection directe de variables d'environnement (`mise env`) sans ralentissement de shims au lancement de chaque commande.
**Urgences/dangers :** —
**Précautions :** Activer la fonction d'intégration Shell `mise activate bash` dans votre fichier de configuration de Shell.
**Équivalents :** asdf, proto, venv
**Voir aussi :** asdf, proto, pyenv

## `proto` — Gestionnaire de toolchains polyglotte de nouvelle génération [Cross]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** —
**Contextes :** unifier la gestion des outils de dev (Node, Bun, Go, Python, Rust) dans un Monorepo multi-langages moderne
**Rôle :** Outil de gestion des chaînes de outils (*toolchain manager*) multi-langages, rapide et sécurisé, développé par Moonrepo.
**Syntaxe :** `proto <commande> [outil] [version]`
**Cas réguliers :**
- `proto install node 20.0.0` — Télécharger et installer la version Node.js 20.0.0 dans le magasin Proto
- `proto pin python 3.11` — Enregistrer la version Python dans le fichier de configuration `.prototools`
- `proto run node -- script.js` — Exécuter une commande avec la version exacte d'un outil sans altérer le PATH global
**Origine :** Miles Johnson / Moonrepo (2023).
**Subtilités/confusions :**
- Détecte et télécharge automatiquement les checksums SHA256 pour vérifier l'intégrité de chaque binaire installé.
- Fichier de configuration maître au format `.prototools`.
**Urgences/dangers :** —
**Précautions :** Définir `proto setup` pour ajouter l'intégration propre des binaires au profil du Shell.
**Équivalents :** mise, asdf
**Voir aussi :** mise, asdf

## `jenv` — Gestionnaire d'environnements et versions Java [Cross]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** basculer entre plusieurs versions de JDK installés sur un poste macOS ou Linux (ex: Java 8 pour un projet hérité, Java 17 pour Spring Boot 3)
**Rôle :** Script d'administration de la variable `$JAVA_HOME` et des versions de JDK installées sur la machine.
**Syntaxe :** `jenv <commande> [version]`
**Cas réguliers :**
- `jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home` — Ajouter un JDK existant dans le catalogue jenv
- `jenv local 17.0` — Fixer la version Java active pour le répertoire courant (`.java-version`)
- `jenv enable-plugin maven` — Activer le plugin pour que Maven réutilise automatiquement la bonne version de `$JAVA_HOME`
**Origine :** Gilles Cornu (2012) — inspiré directement par la philosophie de `rbenv`.
**Subtilités/confusions :**
- Contrairement à SDKMAN, `jenv` NE TÉLÉCHARGE PAS les JDKs : il permet simplement d'ORGANISER et BASCULER entre les JDKs déjà présents sur le disque.
**Urgences/dangers :** —
**Précautions :** Toujours exécuter `jenv enable-plugin export` pour s'assurer que la variable `$JAVA_HOME` est bien mise à jour dynamiquement.
**Équivalents :** sdkman, asdf
**Voir aussi :** sdkman, java

## `goenv` — Gestionnaire de versions pour le langage Go [Cross]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** —
**Contextes :** faire tourner des projets Go nécessitant des révisions spécifiques de la chaîne de compilation Go (ex: Go 1.18 vs Go 1.22)
**Rôle :** Outil de basculement entre plusieurs versions de l'environnement Go par projet ou par utilisateur.
**Syntaxe :** `goenv <commande> [options]`
**Cas réguliers :**
- `goenv install 1.22.0` — Télécharger et installer la version Go 1.22.0
- `goenv local 1.22.0` — Fixer la version Go active dans le dossier courant (`.go-version`)
- `goenv versions` — Afficher les versions de Go installées sur la machine
**Origine :** Syu Kato (2016) — dérivé directement de `pyenv` et `rbenv`.
**Subtilités/confusions :**
- Met automatiquement à jour les variables `$GOROOT` et `$GOPATH` lors du changement de version active.
**Urgences/dangers :** —
**Précautions :** S'assurer que les shims `~/.goenv/shims` sont bien déclarés en priorité dans la variable `$PATH`.
**Équivalents :** gvm, asdf, mise
**Voir aussi :** go, pyenv, rbenv

## `tfenv` — Gestionnaire de versions pour Terraform [Cross]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** administrer de l'infrastructure as code (IaC) avec plusieurs projets Terraform exigeant des versions différentes (ex: 0.12 vs 1.6)
**Rôle :** Outil de gestion et de basculement transparent entre différentes versions du binaire `terraform`.
**Syntaxe :** `tfenv <commande> [version]`
**Cas réguliers :**
- `tfenv install 1.6.5` — Télécharger et installer la version 1.6.5 de HashiCorp Terraform
- `tfenv use 1.6.5` — Définir la version active pour le terminal courant
- `tfenv install latest` — Installer la toute dernière version stable de Terraform
**Origine :** Alex Rey (2016) / tfutils.
**Subtilités/confusions :**
- Lis automatiquement le fichier de version `.terraform-version` présent dans le dossier du projet d'infrastructure.
- Évite les erreurs irréversibles de mise à jour du fichier de statut d'infrastructure (`terraform.tfstate`).
**Urgences/dangers :** ⚠️ Exécuter Terraform avec une version trop récente peut mettre à jour le fichier `tfstate` et empêcher tout retour en arrière.
**Précautions :** Inclure un fichier `.terraform-version` dans la racine de chaque dépôt d'infrastructure IaC.
**Équivalents :** tgswitch, tenv, asdf
**Voir aussi :** terraform, asdf

## `phpenv` — Gestionnaire de versions multiples pour PHP [Cross]
**Niveau :** avance | **Popularité :** 75 | **Aliases :** —
**Contextes :** maintenir des applications Web PHP héritées (PHP 7.4) et modernes (PHP 8.2/8.3) sur le même poste de travail
**Rôle :** Outil de gestion des versions d'interpréteurs PHP isolées par utilisateur ou projet.
**Syntaxe :** `phpenv <commande> [options]`
**Cas réguliers :**
- `phpenv install 8.2.12` — Compiler et installer la version PHP 8.2.12 (via `php-build`)
- `phpenv local 8.2.12` — Définir la version PHP du dossier courant (`.php-version`)
- `phpenv versions` — Afficher les versions de PHP disponibles localement
**Origine :** Dominick D'Aniello (2012) — basé sur la philosophie rbenv.
**Subtilités/confusions :**
- Exige que les dépendances système de compilation (libxml2, openssl, cURL, bzip2) soient présentes lors de l'installation.
**Urgences/dangers :** —
**Précautions :** Lancer `phpenv rehash` après l'installation de nouveaux exécutables via Composer.
**Équivalents :** asdf, mise, brew
**Voir aussi :** composer, rbenv

## `nodenv` — Gestionnaire de versions léger pour Node.js [Cross]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** maintenir des projets Node.js exigeant des versions spécifiques de l'environnement d'exécution (ex: Node 16 LTS vs Node 20 LTS)
**Rôle :** Outil de basculement entre différentes versions de Node.js basé sur des shims (philosophie rbenv).
**Syntaxe :** `nodenv <commande> [options]`
**Cas réguliers :**
- `nodenv install 20.10.0` — Télécharger et installer la version 20.10.0 de Node.js (via `node-build`)
- `nodenv local 20.10.0` — Définir la version active pour le projet courant (`.node-version`)
- `nodenv rehash` — Régénérer les shims après l'installation d'un paquet CLI global via npm
**Origine :** Sam Stephenson & Sam Gleske (2014) — portage direct de rbenv pour Node.js.
**Subtilités/confusions :**
- Alternative plus légère et stricte que `nvm`, qui ne dépend pas d'une surcharge lourde du Shell.
**Urgences/dangers :** —
**Précautions :** Créer un fichier `.node-version` à la racine de vos projets Node pour automatiser la sélection de version sur l'équipe.
**Équivalents :** nvm, fnm, n, volta, asdf
**Voir aussi :** npm, nvm, fnm, volta

## `volta` — Gestionnaire d'outils JavaScript rapide et sans friction [Cross]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** épingler de façon stricte et automatique les versions de Node.js, npm, yarn ou pnpm au sein d'une équipe de développement Web
**Rôle :** Outil de gestion des outils JavaScript (*JavaScript Tool Manager*) ultra-rapide écrit en Rust.
**Syntaxe :** `volta <commande> [arguments]`
**Cas réguliers :**
- `volta install node@20` — Installer la version 20 de Node.js en global
- `volta pin node@20.10.0 npm@10.2.0` — Épingler les versions exactes de Node et npm dans la section `"volta"` du `package.json`
- `volta run node script.js` — Exécuter une commande avec l'environnement exact épinglé
**Origine :** Charles Lowell & Dave Herman / LinkedIn (2019) — anciennement nommé Notion.
**Subtilités/confusions :**
- Lorsque vous changez de projet dans le terminal (`cd`), Volta bascule IMMÉDIATEMENT la version de Node et npm sans aucun délai ni besoin de réexécuter de commande !
- Les versions sont enregistrées directement dans le fichier `package.json` standard du projet.
**Urgences/dangers :** —
**Précautions :** Utiliser `volta pin` pour garantir que tous les développeurs et les runners CI/CD utilisent strictement les mêmes versions de binaires.
**Équivalents :** fnm, nvm, nodenv, asdf
**Voir aussi :** npm, pnpm, nvm, fnm

## `fnm` — Fast Node Manager rapide écrit en Rust [Cross]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** basculer automatiquement de version Node.js au changement de dossier dans le terminal sans temps de latence
**Rôle :** Gestionnaire de versions Node.js haute performance écrit en Rust, conçu comme une alternative ultra-rapide à NVM.
**Syntaxe :** `fnm <commande> [arguments]`
**Cas réguliers :**
- `fnm install 20.10.0` — Télécharger et installer la version 20.10.0 de Node.js
- `fnm use 20.10.0` — Basculer la version Node.js active pour le Shell courant
- `fnm current` — Afficher la version de Node.js active dans la session
**Origine :** Gal Schlezinger (2019) — acronyme de « Fast Node Manager ».
**Subtilités/confusions :**
- Bascule automatiquement de version Node dès l'entrée dans un répertoire contenant un fichier `.node-version` ou `.nvmrc` si `--use-on-cd` est activé.
- Supporte tous les Shells majeurs (Bash, Zsh, Fish, PowerShell, CMD).
**Urgences/dangers :** —
**Précautions :** Évaluer `fnm env --use-on-cd` dans le fichier de profil de votre Shell (`.bashrc` / `.zshrc`) pour l'automatisation complète.
**Équivalents :** nvm, volta, nodenv, asdf
**Voir aussi :** nvm, volta, nodenv, npm

## `nix` — Gestionnaire de paquets déclaratif et reproductible [Linux/macOS]
**Niveau :** avance | **Popularité :** 88 | **Aliases :** —
**Contextes :** créer un environnement de développement pur et 100% reproductible sans polluer le système d'exploitation hôte
**Rôle :** Gestionnaire de paquets déclaratif, purement fonctionnel et totalement isolé pour Linux et macOS.
**Syntaxe :** `nix <sous-commande> [options]`
**Cas réguliers :**
- `nix-shell -p python3 git` — Lancer un Shell temporaire contenant Python 3 et Git sans les installer de façon permanente sur la machine !
- `nix run nixpkgs#htop` — Exécuter l'outil `htop` instantanément depuis le dépôt Nixpkgs sans installation préalable
- `nix-collect-garbage -d` — Purger l'ensemble des anciens paquets et versions inutilisés du magasin `/nix/store`
**Origine :** Eelco Dolstra / TU Delft & NixOS Foundation (2003).
**Subtilités/confusions :**
- Tous les paquets sont stockés sous `/nix/store/<hash>-<nom>-<version>` où le hash dépend de l'intégralité du graphe de dépendances et du code source.
- Garantit qu'un environnement de build fonctionnera à 100% de la même manière sur n'importe quel ordinateur portable ou serveur.
**Urgences/dangers :** —
**Précautions :** Nettoyer le store Nix avec `nix-collect-garbage` périodiquement pour éviter la saturation du disque par accumalation de builds.
**Équivalents :** guix, devbox, flox
**Voir aussi :** nix-env, guix

## `nix-env` — Manipulation des profils d'utilisateurs Nix [Linux/macOS]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** installer ou désinstaller de façon persistance des applications dans le profil utilisateur Nix sous n'importe quelle distribution Linux ou macOS
**Rôle :** Outil de gestion des profils d'utilisateurs et de l'état d'installation de paquets Nix.
**Syntaxe :** `nix-env <option> [arguments]`
**Cas réguliers :**
- `nix-env -iA nixpkgs.ripgrep` — Installer l'outil `ripgrep` dans le profil utilisateur courant (`-iA` = install attribute)
- `nix-env -q` — Afficher la liste des paquets actuellement installés dans le profil Nix de l'utilisateur
- `nix-env --rollback` — Annuler la dernière opération d'installation/mise à jour et revenir au profil précédent instantanément !
**Origine :** Eelco Dolstra / NixOS (2003).
**Subtilités/confusions :**
- `nix-env --rollback` permet de défaire instantanément n'importe quelle mise à jour qui a cassé un outil.
**Urgences/dangers :** —
**Précautions :** Privilégier `nix-shell` pour les environnements de dev éphémères et `nix-env` uniquement pour les binaires globaux.
**Équivalents :** nix, guix
**Voir aussi :** nix, guix

## `guix` — Gestionnaire de paquets fonctionnel et libre GNU [Linux]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** —
**Contextes :** déployer des environnements de calcul scientifique déclaratifs et audités 100% logiciels libres
**Rôle :** Le gestionnaire de paquets fonctionnel et système d'exploitation du projet GNU basé on le langage Guile Scheme.
**Syntaxe :** `guix <commande> [options] [arguments]`
**Cas réguliers :**
- `guix install gcc-toolchain` — Installer la chaîne de compilation GCC dans le profil utilisateur
- `guix shell python python-numpy -- python` — Démarrer un environnement interactif isolé contenant Python et NumPy
- `guix pull` — Mettre à jour la liste des définitions de paquets et l'outil Guix lui-même
**Origine :** Ludovic Courtès / GNU Project (2012) — acronyme de « GNU Guix ».
**Subtilités/confusions :**
- Tout comme Nix, Guix garantit des déploiements reproductibles et un retour en arrière (*rollback*) instantané sans risque de casse.
- Utilise Guile Scheme comme langage de configuration déclaratif au lieu du langage Nix expression.
**Urgences/dangers :** —
**Précautions :** Consulter `guix package --list-generations` pour gérer les révisions du profil système.
**Équivalents :** nix, nix-env
**Voir aussi :** nix, nix-env

## `n` — Gestionnaire de versions Node.js interactif et minimaliste [Cross]
**Niveau :** debutant | **Popularité :** 86 | **Aliases :** —
**Contextes :** changer de version Node.js sur sa machine de dev avec une interface TUI fléchée ultra-simple
**Rôle :** Outil de gestion des versions de Node.js interactif écrit sous forme de simple script Shell sans dépendances.
**Syntaxe :** `n [version|commande]`
**Cas réguliers :**
- `n` — Lancer le menu TUI interactif pour sélectionner la version de Node.js active avec les flèches du clavier
- `n lts` — Télécharger et basculer instantanément sur la toute dernière version Node.js LTS (Long Term Support)
- `n latest` — Installer et activer la version Node.js la plus récente (*Current*)
**Origine :** TJ Holowaychuk (2011) — outil culte pour sa simplicité désarmante.
**Subtilités/confusions :**
- Contrairement à nvm/rbenv, `n` remplace DIRECTEMENT le binaire `node` dans `/usr/local/bin/node` sans passer par des shims ou des fonctions Shell complexes.
**Urgences/dangers :** —
**Précautions :** Nécessite les droits d'écriture dans `/usr/local/bin` (ou la définition de `N_PREFIX`).
**Équivalents :** nvm, fnm, nodenv, volta
**Voir aussi :** nvm, fnm, nodenv, npm


