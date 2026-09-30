## `CPU` — Central Processing Unit [Matériel]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Processeur Central
**Contextes :** désigner le composant matériel principal chargé de lire, interpréter et exécuter les instructions séquentielles des programmes informatiques
**Rôle :** Cerveau électronique de l'ordinateur assurant les calculs arithmétiques, logiques et le contrôle des entrées/sorties.
**Syntaxe :** `lscpu` (Linux) ou `sysctl -n machdep.cpu.brand_string` (macOS)
**Cas réguliers :**
- `Cœurs Physiques vs Virtuels` — Cœurs d'exécution réels vs threads logiques (Hyper-Threading / SMT)
- `Cache CPU (L1, L2, L3)` — Mémoire ultra-rapide intégrée au processeur pour réduire les temps d'accès à la RAM
**Origine :** John von Neumann / Architecture de von Neumann (1945).
**Subtilités/confusions :**
- Un CPU est optimisé pour traiter rapidement des tâches séquentielles complexes avec une faible latence ; un **GPU** est optimisé pour traiter des milliers de calculs simples en parallèle.
**Urgences/dangers :** —
**Précautions :** Surveiller la température CPU sous forte charge pour éviter la baisse de fréquence de protection (*thermal throttling*).
**Équivalents :** Microprocesseur, SoC
**Voir aussi :** GPU, RAM, lscpu, nproc

## `GPU` — Graphics Processing Unit [Matériel]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Carte Graphique / Processeur Graphique
**Contextes :** calculer le rendu graphique 3D/2D, accélérer les traitements vidéo et exécuter des calculs parallèles massifs (Deep Learning, IA, calcul scientifique)
**Rôle :** Processeur composé de milliers de petits cœurs de calcul conçus pour exécuter des opérations mathématiques vectorielles et matricielles hautement parallèles.
**Syntaxe :** `nvidia-smi` (NVIDIA) ou `rocm-smi` (AMD)
**Cas réguliers :**
- `GPGPU (General-Purpose GPU)` — Utilisation du processeur graphique pour du calcul scientifique non graphique (ex: via CUDA ou ROCm)
- `VRAM (Video RAM)` — Mémoire vive dédiée à haute bande passante intégrée sur la carte graphique (ex: GDDR6, HBM)
**Origine :** NVIDIA (GeForce 256 en 1999).
**Subtilités/confusions :**
- La mémoire VRAM est un élément critique en IA : un modèle de langage (LLM) doit tenir entièrement dans la VRAM du GPU pour une vitesse de réponse maximale.
**Urgences/dangers :** —
**Précautions :** Installer les pilotes propriétaires et les toolkits de calcul (CUDA/ROCm) adaptés à la version du noyau de votre système d'exploitation.
**Équivalents :** TPU, NPU, Carte Graphique
**Voir aussi :** CPU, TPU, NPU, nvidia-smi

## `TPU` — Tensor Processing Unit [Matériel/IA]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Google TPU
**Contextes :** accélérer spécifiquement les calculs matriciels complexes d'apprentissage profond (Deep Learning / réseaux de neurones) dans le cloud Google
**Rôle :** Circuit intégré spécifique (ASIC) conçu sur-mesure par Google pour accélérer de façon drastique l'entraînement et l'inférence des modèles d'IA (TensorFlow, PyTorch, Gemini).
**Syntaxe :** (Infrastructures IA Google Cloud Platform / Colab)
**Cas réguliers :**
- `TPU Pod` — Supercalculateur reliant des milliers de puces TPU interconnectées par un réseau à très haut débit
- `Calcul Systolique (Systolic Array)` — Architecture matérielle optimisée pour les multiplications de matrices 128×128 en une seule passe d'horloge
**Origine :** Google (2016).
**Subtilités/confusions :**
- Contrairement aux GPUs généraux, le TPU est un ASIC entièrement spécialisé dans la multiplication de matrices de tenseurs (opérations IA).
**Urgences/dangers :** —
**Précautions :** Formater vos données sous forme de tenseurs optimisés (ex: bfloat16) pour exploiter les unités de calcul matriciel du TPU à 100%.
**Équivalents :** GPU (NVIDIA H100/A100), NPU
**Voir aussi :** GPU, NPU, CPU, Cloud

## `NPU` — Neural Processing Unit [Matériel/IA]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Moteur Neural (Neural Engine)
**Contextes :** exécuter des modèles d'IA légers en local directement sur le processeur d'un smartphone, PC portable ou objet connecté (reconnaissance faciale, transcription vocale, Copilot+ PC)
**Rôle :** Co-processeur spécialisé à faible consommation d'énergie intégré dans les SoCs modernes (Apple Silicon Neural Engine, Qualcomm Hexagon, Intel AI Boost) pour accélérer l'inférence IA locale.
**Syntaxe :** (Composant matériel intégré aux SoCs modernes)
**Cas réguliers :**
- `Inférence On-Device` — Exécution de modèles d'IA en local sans envoyer de données vers un serveur cloud distant (respect de la vie privée)
- `Efficacité Énergétique` — Exécute des milliards d'opérations d'IA par seconde avec une consommation de quelques milliwatts seulement
**Origine :** Apple (A11 Bionic Neural Engine, 2017) / Qualcomm / ARM.
**Subtilités/confusions :**
- Le NPU est conçu pour consommer très peu d'énergie sur batterie pour l'**inférence**, alors que les gros GPU/TPU sont conçus pour la puissance brute de l'**entraînement**.
**Urgences/dangers :** —
**Précautions :** Utiliser des frameworks d'inférence adaptés au matériel (CoreML sous macOS/iOS, ONNX Runtime avec DirectML sous Windows).
**Équivalents :** TPU, GPU, AI Accelerator
**Voir aussi :** GPU, TPU, CPU

## `RAM` — Random Access Memory [Matériel]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Mémoire Vive
**Contextes :** stocker temporairement le code et les données des programmes en cours d'exécution pour un accès quasi-instantané par le processeur
**Rôle :** Mémoire principale volatile d'un système informatique offrant des temps d'accès très rapides (de l'ordre de quelques nanosecondes).
**Syntaxe :** `free -h` (Linux) ou `sysctl hw.memsize` (macOS)
**Cas réguliers :**
- `Volatilité` — Le contenu de la RAM est intégralement perdu lors de l'extinction du composant (coupure d'alimentation)
- `DDR4 / DDR5` — Normes actuelles de mémoire vive à double débit de données (*Double Data Rate*)
**Origine :** Robert Dennard (DRAM 1 cellule, IBM 1966).
**Subtilités/confusions :**
- Si la RAM est saturée, le système d'exploitation utilise le disque dur/SSD sous forme d'espace de pagination (**Swap**), ce qui ralentit considérablement la machine.
**Urgences/dangers :** —
**Précautions :** Dimensionner la RAM en fonction des exigences réelles de la charge applicative pour éviter le déclenchement de l'OOM Killer (*Out-Of-Memory*).
**Équivalents :** Mémoire Vive, VRAM (pour GPU)
**Voir aussi :** ROM, NVMe, free, vmstat

## `ROM` — Read-Only Memory [Matériel]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** Mémoire Morte
**Contextes :** stocker de manière permanente et inaltérable les instructions de démarrage d'un équipement informatique (firmware BIOS/UEFI, routeurs, consoles)
**Rôle :** Mémoire informatique non volatile dont les données sont conservées même hors tension et ne peuvent pas être facilement modifiées en fonctionnement normal.
**Syntaxe :** (Mémoire non volatile embarquée)
**Cas réguliers :**
- `Flash ROM (EEPROM)` — Variante moderne réinscriptible électroniquement permettant la mise à jour des firmwares (*Flashage du BIOS*)
- `Boot ROM` — Première instruction exécutée par le microprocesseur dès la mise sous tension de l'équipement
**Origine :** Débuts de l'informatique / Mémoires à masques (années 1960).
**Subtilités/confusions :**
- Contrairement à la RAM (volatile et réinscriptible à l'infini), la ROM est non volatile et destinée à conserver du code système fixe.
**Urgences/dangers :** ⚠️ Interrompre l'alimentation électrique pendant le flashage d'une mémoire ROM (mise à jour BIOS) peut rendre l'équipement définitivement inexploitable (*brické*).
**Précautions :** Brancher l'équipement sur un onduleur (ASI) lors des mises à jour de firmware ROM.
**Équivalents :** EEPROM, Flash Memory
**Voir aussi :** RAM, BIOS, UEFI

## `NVMe` — Non-Volatile Memory Express [Matériel/Stockage]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** SSD NVMe
**Contextes :** stocker des données sur des disques SSD ultra-rapides connectés directement au bus PCIe du processeur (débits > 7000 MB/s)
**Rôle :** Spécification d'interface de communication ouverte et protocole optimisé spécifiquement pour les supports de stockage flash non volatils raccordés via le bus PCI Express.
**Syntaxe :** `nvme list` (paquet `nvme-cli` sous Linux)
**Cas réguliers :**
- `PCIe Gen4 / Gen5` — Bus de données offrant des bandes passantes allant jusqu'à 14 000 MB/s en lecture
- `Parallélisme Massif` — Supporte jusqu'à 64 000 files d'attente de 64 000 commandes chacune (contre 1 seule file de 32 commandes pour l'ancien protocole SATA/AHCI !)
**Origine :** Consortium NVM Express (Intel, Samsung, SanDisk, Dell, 2011).
**Subtilités/confusions :**
- M.2 est le **format physique** (la barrette) ; NVMe est le **protocole logique** de communication (passant par PCIe).
**Urgences/dangers :** —
**Précautions :** Utiliser des dissipateurs thermiques sur les SSD NVMe haute performance pour éviter les baisses de débit dues à la chauffe.
**Équivalents :** SATA (obsolète), SAS
**Voir aussi :** SSD, PCIe, HDD

## `SSD` — Solid-State Drive [Matériel/Stockage]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Disque Flash
**Contextes :** stocker de manière permanente les données et le système d'exploitation d'un ordinateur sans aucune pièce mécanique en mouvement
**Rôle :** Disque de stockage de masse constitué de puces de mémoire flash (NAND) conservant les données hors tension.
**Syntaxe :** `lsblk` ou `smartctl -a /dev/nvme0n1`
**Cas réguliers :**
- `Commande TRIM` — Commande du système d'exploitation indiquant au SSD les blocs de mémoire libérés pour optimiser la réécriture et la durée de vie
- `Cellules NAND (TLC/QLC)` — Technologies de stockage de 3 bits (TLC) ou 4 bits (QLC) par cellule mémoire
**Origine :** Dataram (Bulk Core 1976) / SanDisk (premier SSD Flash 1991).
**Subtilités/confusions :**
- Les SSD offrent des temps d'accès quasi-instantanés (< 0.1 ms) et des débits de 5 à 100 fois supérieurs aux anciens disques durs mécaniques (HDD).
**Urgences/dangers :** —
**Précautions :** S'assurer que le service de TRIM automatique (`fstrim.timer` sous Linux) est actif pour préserver la durée de vie des puces flash.
**Équivalents :** NVMe, HDD
**Voir aussi :** NVMe, HDD, RAID, lsblk

## `HDD` — Hard Disk Drive [Matériel/Stockage]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** Disque Dur Mécanique
**Contextes :** stocker de très grands volumes de données (archivage, NAS, serveurs de stockage capacitif) au meilleur coût par gigaoctet
**Rôle :** Organe de stockage de masse magnétique composé de plusieurs disques rigides en rotation (plateaux) et de têtes de lecture/écriture mobiles.
**Syntaxe :** `smartctl -a /dev/sda`
**Cas réguliers :**
- `Vitesse de Rotation (RPM)` — 5400 RPM (économique) ou 7200 RPM (serveurs)
- `Technologie CMR vs SMR` — CMR (Conventional Magnetic Recording / idéal pour NAS et RAID) vs SMR (Shingled / écriture plus lente)
**Origine :** IBM (IBM 350 RAMAC, 1956).
**Subtilités/confusions :**
- Très vulnérable aux chocs physiques et aux vibrations lorsqu'il est en cours de fonctionnement (risque d'atterrissage de tête / crash binaire).
**Urgences/dangers :** ⚠️ Un bruit de cliquètement répétitif ("Click of Death") indique une panne mécanique imminente de la tête de lecture.
**Précautions :** Surveiller l'état de santé du disque dur via les métriques S.M.A.R.T. (`smartctl`).
**Équivalents :** SSD, Ruban magnétique (Tape)
**Voir aussi :** SSD, RAID, smartctl

## `RAID` — Redundant Array of Independent Disks [Stockage/Infrastructure]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** Grappe de Disques Redondants
**Contextes :** regrouper plusieurs disques durs ou SSD en une seule unité logique pour améliorer les performances E/S, la capacité globale ou la tolérance aux pannes
**Rôle :** Ensemble de techniques de stockage associant plusieurs disques physiques en une grappe logique unique (RAID matériel ou logiciel via `mdadm`).
**Syntaxe :** `mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sda /dev/sdb /dev/sdc`
**Cas réguliers :**
- `RAID 0 (Agrégation / Striping)` — Découpe les données sur plusieurs disques (vitesse maximale, mais tolérance aux pannes NULLE : 1 disque mort = tout est perdu !)
- `RAID 1 (Miroir / Mirroring)` — Copie identique sur 2 disques (tolère la panne de 1 disque sur 2)
- `RAID 5 / RAID 6` — Répartition des données et des parités sur 3 disques ou plus (tolère la panne de 1 ou 2 disques)
**Origine :** David Patterson, Garth A. Gibson et Randy Katz (UC Berkeley, 1987).
**Subtilités/confusions :**
- **LE RAID N'EST PAS UNE SAUVEGARDE !** Si un fichier est effacé par erreur ou chiffré par un ransomware, la modification est répercutée immédiatement sur tous les disques de la grappe.
**Urgences/dangers :** ⚠️ Toujours remplacer immédiatement un disque défaillant dans une grappe RAID 5/6 avant qu'un deuxième disque ne tombe en panne.
**Précautions :** Prévoir un disque de secours à chaud (*Hot Spare*) dans le châssis pour démarrer la reconstruction automatiquement dès qu'une panne survient.
**Équivalents :** ZFS, Btrfs, Storage Spaces
**Voir aussi :** HDD, SSD, mdadm, stat

## `PCIe` — Peripheral Component Interconnect Express [Matériel]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** PCI Express
**Contextes :** connecter des composants matériels à très haut débit (cartes graphiques GPU, SSDs NVMe, cartes réseau 100G) directement à la carte mère et au processeur
**Rôle :** Standard de bus d'extension informatique série à haute vitesse remplaçant les anciens bus PCI et AGP.
**Syntaxe :** `lspci -v` (Linux)
**Cas réguliers :**
- `Lignes PCIe (Lanes x1, x4, x8, x16)` — Nombre de canaux de données en parallèle (ex: un GPU utilise un connecteur x16)
- `Générations (Gen3, Gen4, Gen5)` — Chaque génération double le débit par ligne (PCIe Gen5 = ~4 Go/s par ligne)
**Origine :** Intel, Dell, HP, IBM / PCI-SIG (2003).
**Subtilités/confusions :**
- Les lignes PCIe sont une ressource limitée du processeur : installer trop de SSDs NVMe peut réduire le nombre de lignes disponibles pour la carte graphique.
**Urgences/dangers :** —
**Précautions :** Vérifier que le connecteur PCIe de la carte mère supporte la génération et le nombre de lignes réclamés par le composant.
**Équivalents :** CXL (Compute Express Link), PCI (obsolète)
**Voir aussi :** GPU, NVMe, lspci

## `USB` — Universal Serial Bus [Matériel]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Bus Série Universel
**Contextes :** connecter, alimenter et échanger des données entre un ordinateur et des périphériques externes (clés USB, disques durs, claviers, souris, webcams, smartphones)
**Rôle :** Standard de bus série industriel de connexion Plug-and-Play et d'alimentation électrique pour périphériques.
**Syntaxe :** `lsusb` (Linux)
**Cas réguliers :**
- `USB-C` — Connecteur réversible moderne supportant la transmission de données (USB4 / Thunderbolt), la vidéo (DisplayPort Alt Mode) et la charge électrique (Power Delivery jusqu'à 240W)
- `USB 3.2 / USB4` — Normes de transfert de données à haut débit (10 à 40 Gbit/s)
**Origine :** Compaq, DEC, IBM, Intel, Microsoft, NEC, Nortel (1996).
**Subtilités/confusions :**
- Le nom commercial de l'USB 3.0 a été renommé à plusieurs reprises (USB 3.1 Gen 1, USB 3.2 Gen 1x1) désignant le même débit de 5 Gbit/s.
**Urgences/dangers :** ⚠️ Ne jamais brancher une clé USB inconnue trouvée dans la rue (risque d'attaque par émulation de clavier *Rubber Ducky* ou destruction électrique *USB Killer*).
**Précautions :** Utiliser des câbles USB certifiés "Power Delivery" pour recharger des ordinateurs portables sans surchauffe.
**Équivalents :** Thunderbolt, FireWire (obsolète)
**Voir aussi :** lsusb, NVMe, PCIe

## `UEFI` — Unified Extensible Firmware Interface [Matériel/Système]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** EFI
**Contextes :** initialiser le matériel informatique lors de la mise sous tension de la carte mère et charger l'exécutable d'amorçage du système d'exploitation
**Rôle :** Spécification de firmware moderne remplaçant l'ancien BIOS historique, offrant la prise en charge des disques de plus de 2 To (table de partition GPT), une interface graphique et des fonctions de sécurité avancées.
**Syntaxe :** `efibootmgr` (Linux)
**Cas réguliers :**
- `Secure Boot` — Fonctionnalité de l'UEFI qui vérifie la signature numérique du noyau OS avant de l'autoriser à démarrer (protection anti-rootkits)
- `ESP (EFI System Partition)` — Partition FAT32 obligatoire contenant les fichiers de démarrage `.efi` (ex: `/boot/efi`)
**Origine :** Intel (projet Extensible Firmware Interface / EFI, 1998) / Forum Unified EFI (2005).
**Subtilités/confusions :**
- Nécessite d'utiliser une table de partitionnement **GPT** (GUID Partition Table) au lieu de l'ancien format MBR.
**Urgences/dangers :** —
**Précautions :** Sauvegarder le contenu de la partition ESP avant toute mise à jour majeure du chargeur de démarrage (GRUB).
**Équivalents :** BIOS (obsolète), Coreboot
**Voir aussi :** BIOS, POST, efibootmgr, GPT

## `BIOS` — Basic Input/Output System [Matériel/Système]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Legacy BIOS
**Contextes :** désigner le microprogramme historique intégré à la carte mère chargé d'effectuer les autotests matériels (POST) et de lancer le système d'exploitation
**Rôle :** Firmware informatique historique stocké en mémoire morte (ROM) qui initialise les composants matériels de base et démarre le premier secteur du disque (MBR).
**Syntaxe :** (Touche `F2`, `F12` ou `Suppr` au démarrage du PC pour accéder au menu)
**Cas réguliers :**
- `Master Boot Record (MBR)` — Premier secteur de 512 octets du disque dur lu par le BIOS pour lancer le système
- `Legacy Mode` — Mode d'émulation BIOS présent sur les cartes mères UEFI pour assurer la compatibilité avec les anciens systèmes
**Origine :** Gary Kildall (CP/M OS, 1975) / Adopté par IBM PC (1981).
**Subtilités/confusions :**
- Le BIOS traditionnel ne pouvait pas démarrer sur des disques de plus de 2.2 Terabytes (limitation du MBR 32 bits).
**Urgences/dangers :** —
**Précautions :** Préférer le mode UEFI natif pour tous les nouveaux ordinateurs et serveurs.
**Équivalents :** UEFI, Coreboot
**Voir aussi :** UEFI, POST, ROM

## `POST` — Power-On Self-Test [Matériel]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** Autotest au Démarrage
**Contextes :** séquence automatique de tests matériels exécutée par le BIOS/UEFI immédiatement après l'appui sur le bouton d'allumage de l'ordinateur
**Rôle :** Diagnostic initial vérifiant le bon fonctionnement du processeur, des modules de mémoire RAM, du clavier, du contrôleur vidéo et du stockage avant d'autoriser le démarrage de l'OS.
**Syntaxe :** (Séquence automatique au démarrage / Bips de la carte mère)
**Cas réguliers :**
- `Bips du BIOS (Beep Codes)` — Série de bips sonores émis par le haut-parleur interne de la carte mère pour indiquer la panne d'un composant précis (ex: 3 bips courts = erreur de mémoire RAM)
- `Affichage POST (Debug LED)` — Codes hexadécimaux affichés sur la carte mère pour identifier les blocages au boot
**Origine :** Premiers micro-ordinateurs personnels (années 1970).
**Subtilités/confusions :**
- Si le POST échoue (ex: RAM mal insérée ou processeur non détecté), l'ordinateur ne peut même pas afficher d'image à l'écran.
**Urgences/dangers :** —
**Précautions :** Consulter le manuel de la carte mère pour interpréter la signification exacte de la séquence de bips ou de LEDs d'erreur.
**Équivalents :** Boot Diagnostic
**Voir aussi :** BIOS, UEFI, RAM, CPU

## `GPT` — GUID Partition Table [Stockage/Système]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Table de Partitionnement GUID
**Contextes :** partitionner des disques de grande capacité (> 2 Terabytes) et démarrer des systèmes d'exploitation modernes en mode UEFI
**Rôle :** Format standard moderne de table de partitionnement de disque remplaçant le vieux MBR, offrant la prise en charge de disques jusqu'à 9.4 Zettabytes et de 128 partitions principales.
**Syntaxe :** `gdisk /dev/sda` ou `parted /dev/sda mklabel gpt`
**Cas réguliers :**
- `Support UEFI` — Table de partitionnement obligatoire pour le démarrage en mode UEFI natif
- `Sauvegarde d'En-tête` — Stocke une copie de secours de la table de partitionnement à la toute fin du disque dur
**Origine :** Intel / Spécification Unified EFI (années 2000).
**Subtilités/confusions :**
- Contrairement au MBR qui limitait à 4 partitions principales, GPT permet d'en créer jusqu'à 128 sans recourir aux partitions étendues.
**Urgences/dangers :** —
**Précautions :** Utiliser l'outil `gdisk` ou `parted` plutôt que le vieux `fdisk` pour manipuler des disques au format GPT.
**Équivalents :** MBR (obsolète)
**Voir aussi :** MBR, UEFI, parted, fdisk

## `MBR` — Master Boot Record [Stockage/Système]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** Premier Secteur de Démarrage
**Contextes :** désigner le premier secteur de 512 octets d'un disque dur traditionnel contenant la table de partition historique et le code d'amorçage du BIOS
**Rôle :** Premier secteur physique (secteur 0) d'un disque dur contenant le programme de démarrage initial et la table décrivant les partitions du disque.
**Syntaxe :** `fdisk -l /dev/sda`
**Cas réguliers :**
- `Limitation 2.2 To` — Ne peut pas gérer des disques d'une capacité supérieure à 2.2 Terabytes (adresses LBA 32 bits)
- `4 Partitions Principales` — Limité à 4 partitions principales (ou 3 principales + 1 étendue découpée en lecteurs logiques)
**Origine :** IBM (PC DOS 2.0, 1983).
**Subtilités/confusions :**
- Format désormais obsolète remplacé par **GPT** sur tous les ordinateurs et serveurs modernes.
**Urgences/dangers :** ⚠️ Si le MBR est écrasé ou corrompu, le BIOS affiche `No bootable device found`.
**Précautions :** Sauvegarder le secteur MBR avec `dd if=/dev/sda of=mbr_backup.bin bs=512 count=1`.
**Équivalents :** GPT (successeur)
**Voir aussi :** GPT, BIOS, fdisk

## `FAT32` — File Allocation Table 32 [Stockage/Système]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** FAT32
**Contextes :** formater des clés USB et des cartes mémoire SD pour garantir une lisibilité universelle sur tous les appareils (Windows, macOS, Linux, télévisions, autoradios)
**Rôle :** Système de fichiers historique léger développé par Microsoft, universellement supporté par la totalité des équipements électroniques du marché.
**Syntaxe :** `mkfs.vfat -F 32 /dev/sdb1`
**Cas réguliers :**
- `Limitation Fichier 4 Go` — Impossible de stocker un fichier individuel d'une taille supérieure à 4 Gigaoctets ! (ex: une image ISO ou vidéo HD)
- `ESP (EFI Partition)` — La partition de démarrage UEFI doit obligatoirement être formatée en FAT32/FAT16
**Origine :** Microsoft (Windows 95 OSR2, 1996).
**Subtilités/confusions :**
- Très simple et sans gestion de permissions de fichiers Unix (pas de `chmod` ou `chown` possible sur un volume FAT32).
**Urgences/dangers :** —
**Précautions :** Formater les cartes SD de plus de 32 Go en **exFAT** pour dépasser la limite de 4 Go par fichier tout en conservant une grande compatibilité.
**Équivalents :** exFAT, NTFS, ext4
**Voir aussi :** NTFS, ext4, UEFI

## `NTFS` — New Technology File System [Stockage/Système]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Système de Fichiers Windows
**Contextes :** formater les partitions système et disques durs sous Microsoft Windows avec gestion des droits d'accès, de la journalisation et des gros fichiers
**Rôle :** Système de fichiers propriétaire par défaut des systèmes d'exploitation Windows depuis Windows NT.
**Syntaxe :** `mkfs.ntfs /dev/sdb1` ou lecture sous Linux via `ntfs-3g`
**Cas réguliers :**
- `Journalisation` — Journal de transactions empêchant la corruption des fichiers lors d'une coupure de courant soudaine
- `ACLs Windows` — Gestion fine des autorisations d'accès aux fichiers et dossiers pour les utilisateurs Windows
**Origine :** Gary Kimura et Tom Miller / Microsoft (Windows NT 3.1, 1993).
**Subtilités/confusions :**
- Sous macOS, les disques NTFS sont lisibles nativement en lecture seule, mais nécessitent des pilotes tiers pour l'écriture.
**Urgences/dangers :** —
**Précautions :** Monter les volumes NTFS sous Linux en utilisant le pilote moderne intégré au noyau `ntfs3` ou l'outil `ntfs-3g`.
**Équivalents :** ext4, APFS (macOS), ReFS
**Voir aussi :** FAT32, ext4, Btrfs

## `ext4` — Fourth Extended File System [Stockage/Linux]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** ext4fs
**Contextes :** formater le système de fichiers principal de la plupart des distributions Linux (Ubuntu, Debian, Red Hat) pour une stabilité et des performances éprouvées
**Rôle :** Système de fichiers journalisé standard de facto du noyau Linux, supportant des volumes jusqu'à 1 Exabyte et des fichiers jusqu'à 16 Terabytes.
**Syntaxe :** `mkfs.ext4 /dev/sda1`
**Cas réguliers :**
- `Journalisation` — Évite les vérifications complètes de disque (`fsck`) au démarrage après un arrêt brutal
- `Allocation par Étendues (Extents)` — Remplace les blocs individuels par des plages de blocs contigus pour réduire la fragmentation
**Origine :** Theodore Ts'o et Mingming Cao / Noyau Linux (2008 / évolution de ext3).
**Subtilités/confusions :**
- Le système de fichiers Linux le plus robuste, éprouvé et rapide pour les usages serveurs et de bureau généraux.
**Urgences/dangers :** —
**Précautions :** Réserver un pourcentage d'espace pour le compte `root` (par défaut 5%) pour éviter qu'un disque saturé ne bloque le démarrage de l'OS.
**Équivalents :** Btrfs, XFS, ZFS, NTFS
**Voir aussi :** Btrfs, ZFS, fsck, stat

## `Btrfs` — B-tree File System [Stockage/Linux]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** ButterFS
**Contextes :** bénéficier de fonctionnalités de stockage avancées sous Linux (snapshots instantanés, déduplication, RAID logiciel intégré, auto-réparation des données)
**Rôle :** Système de fichiers moderne basé sur le principe du Copy-on-Write (CoW), développé pour offrir les fonctionnalités de ZFS de manière native dans le noyau Linux.
**Syntaxe :** `mkfs.btrfs /dev/sda` ou `btrfs subvolume snapshot / /snapshots/v1`
**Cas réguliers :**
- `Copy-on-Write (CoW)` — Toute modification crée une nouvelle copie des données modifiées sans écraser les anciennes
- `Snapshots Instantanés` — Prise d'instantannés du système de fichiers en une fraction de seconde ne consommant pas d'espace disque supplémentaire tant que les données ne changent pas !
**Origine :** Chris Mason / Oracle (2007) / Adopté comme système de fichiers par défaut dans Fedora et Synology NAS.
**Subtilités/confusions :**
- Intègre son propre moteur de gestion de volumes et de RAID, rendant l'usage de LVM ou `mdadm` superflu.
**Urgences/dangers :** —
**Précautions :** Défragmenter ou désactiver CoW sur les fichiers de bases de données (PostgreSQL, MySQL) ou d'images de machines virtuelles pour maintenir de bonnes performances E/S.
**Équivalents :** ZFS, XFS, APFS
**Voir aussi :** ZFS, ext4, RAID

## `ZFS` — Zettabyte File System [Stockage/Infrastructure]
**Niveau :** avance | **Popularité :** 95 | **Aliases :** OpenZFS
**Contextes :** gérer de très grands pools de stockage d'entreprise (NAS, serveurs de stockage TrueNAS, clusters Proxmox) avec une intégrité des données absolue
**Rôle :** Système de fichiers et gestionnaire de volumes logique combiné de niveau professionnel, célèbre pour sa protection contre la corruption silencieuse de données (*Bit rot*).
**Syntaxe :** `zpool create monpool mirror /dev/sdb /dev/sdc`
**Cas réguliers :**
- `Auto-Réparation (Self-Healing)` — Détecte les blocs corrompus via des checksums et les répare automatiquement à partir d'un disque miroir
- `ZPOOL & ZFS Subvolumes` — Fusion de la couche disque physique et de la couche système de fichiers
- `ARC (Adaptive Replacement Cache)` — Algorithme de mise en cache mémoire RAM ultra-performant
**Origine :** Matthew Ahrens et Jeff Bonwick / Sun Microsystems (2001) / Projet open source OpenZFS.
**Subtilités/confusions :**
- ZFS consomme une quantité importante de mémoire RAM pour son cache ARC (compter environ 1 Go de RAM par Terabyte de stockage géré).
**Urgences/dangers :** ⚠️ Ne jamais utiliser ZFS au-dessus d'un contrôleur RAID matériel qui masque l'accès direct aux disques physiques (*HBA / IT Mode requis*).
**Précautions :** Utiliser des cartes HBA en mode IT (pass-through) pour laisser ZFS gérer directement les disques physiques.
**Équivalents :** Btrfs, Storage Spaces Direct
**Voir aussi :** Btrfs, RAID, HDD, SSD

## `NFS` — Network File System [Réseau/Stockage]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Partage de Fichiers NFS / RFC 7530
**Contextes :** partager un répertoire de fichiers sur un réseau local Linux/UNIX de manière transparente (montage de volumes partagés sur des serveurs web ou Kubernetes)
**Rôle :** Protocole de système de fichiers distribué permettant à un ordinateur client d'accéder à des fichiers stockés sur un serveur distant comme s'il s'agissait de son propre disque local.
**Syntaxe :** `mount -t nfs 192.168.1.10:/data /mnt/data`
**Cas réguliers :**
- `Fichier /etc/exports` — Fichier de configuration serveur définissant les répertoires partagés et les autorisations par IP
- `NFSv4` — Version moderne fonctionnant sur un port unique (TCP 2049) avec support de l'authentification Kerberos
**Origine :** Sun Microsystems (1984 / RFC 1094).
**Subtilités/confusions :**
- NFS est le protocole de partage de fichiers natif de l'écosystème **Linux/UNIX** ; **SMB** est le protocole natif de l'écosystème **Windows**.
**Urgences/dangers :** —
**Précautions :** Restreindre l'accès dans `/etc/exports` aux sous-réseaux IP autorisés et utiliser `noexec` sur les points de montage si nécessaire.
**Équivalents :** SMB/CIFS, SSHFS
**Voir aussi :** SMB, NAS, mount, showmount

## `SMB` — Server Message Block [Réseau/Stockage]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** CIFS, Partage Windows (Samba)
**Contextes :** partager des fichiers et des imprimantes sur un réseau local entre des systèmes Windows, macOS et Linux
**Rôle :** Protocole de partage de réseau et d'accès aux fichiers à distance développé à l'origine par IBM et Microsoft, implémenté sous Linux par la suite logicielle **Samba**.
**Syntaxe :** `smbclient //192.168.1.10/partage -U utilisateur`
**Cas réguliers :**
- `SMBv3` — Version moderne sécurisée intégrant le chiffrement des échanges et la haute disponibilité
- `CIFS (Common Internet File System)` — Nom donné par Microsoft à une ancienne variante de SMB (SMBv1, désormais obsolète)
**Origine :** Barry Feigenbaum / IBM (1983) / Microsoft / Andrew Tridgell (Samba, 1992).
**Subtilités/confusions :**
- Ne plus utiliser SMBv1 qui a été le vecteur de propagation mondial du fameux ransomware WannaCry (faille EternalBlue).
**Urgences/dangers :** ⚠️ Désactiver impérativement SMBv1 sur tous les postes Windows et serveurs Samba.
**Précautions :** Filtrer le port TCP 445 aux frontières du réseau pour empêcher l'exposition des partages SMB sur Internet.
**Équivalents :** NFS, AFP (macOS obsolète)
**Voir aussi :** NFS, NAS, Samba

## `iSCSI` — Internet Small Computer System Interface [Stockage/Réseau]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** RFC 3720
**Contextes :** connecter un serveur à un SAN (Storage Area Network) via le réseau Ethernet TCP/IP pour lui présenter des disques de stockage bruts (*LUNs*)
**Rôle :** Protocole de réseau de stockage (SAN) qui transporte les commandes SCSI de bas niveau au-dessus des paquets réseau TCP/IP standards.
**Syntaxe :** `iscsiadm -m discovery -t sendtargets -p 192.168.1.50`
**Cas réguliers :**
- `Target iSCSI` — Le serveur de stockage qui fournit le disque brut
- `Initiator iSCSI` — Le serveur client qui monte le disque iSCSI comme s'il s'agissait d'un disque local (`/dev/sdb`)
- `LUN (Logical Unit Number)` — Le volume de stockage individuel découpé sur le SAN
**Origine :** IBM et Cisco (2001 / Standardisé IETF RFC 3720 en 2004).
**Subtilités/confusions :**
- Contrairement à NFS ou SMB (qui partagent des **fichiers et dossiers**), iSCSI partage du **stockage bloc brut** que le client doit formater lui-même.
**Urgences/dangers :** —
**Précautions :** Isoler le trafic iSCSI sur un réseau VLAN physique dédié ou utiliser des jumboframes (MTU 9000) pour maximiser le débit E/S.
**Équivalents :** Fibre Channel (FC), NVMe-oF
**Voir aussi :** SAN, NAS, SCSI, iscsiadm

## `SAN` — Storage Area Network [Stockage/Infrastructure]
**Niveau :** avance | **Popularité :** 93 | **Aliases :** Réseau de Stockage Dédié
**Contextes :** interconnecter des serveurs d'entreprise et des baies de stockage haute performance via un réseau dédié à très haut débit et très faible latence
**Rôle :** Réseau informatique spécialisé à haut débit offrant un accès de niveau bloc (*Block-level*) à des baies de stockage partagées.
**Syntaxe :** (Architecture réseau de stockage haute performance)
**Cas réguliers :**
- `Fibre Channel (FC)` — Technologie de réseau optique dédiée à très faible latence (16/32/64 Gbit/s)
- `iSCSI` — Protocoles SAN opérant au-dessus des réseaux Ethernet classiques
**Origine :** Années 1990 / Évolution du stockage DAS (Direct-Attached Storage).
**Subtilités/confusions :**
- Le **SAN** présente du stockage **BLOC brut** à formater ; le **NAS** présente des **FICHIERS** partagés sur le réseau local via un système de fichiers.
**Urgences/dangers :** —
**Précautions :** Multiplier les chemins d'accès au stockage (*Multipathing / MPIO*) pour éviter la déconnexion des serveurs en cas de coupure de câble.
**Équivalents :** NAS, DAS (Direct-Attached Storage)
**Voir aussi :** NAS, iSCSI, SSD, HDD

## `NAS` — Network-Attached Storage [Stockage/Infrastructure]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Boîtier de Stockage Réseau
**Contextes :** stocker, partager et sauvegarder des fichiers au sein d'un réseau local pour plusieurs utilisateurs ou serveurs (Synology, QNAP, TrueNAS)
**Rôle :** Équipement de stockage autonome connecté à un réseau local fournissant un accès aux fichiers via des protocoles réseau standards (NFS, SMB).
**Syntaxe :** (Boîtier de stockage physique ou virtuel)
**Cas réguliers :**
- `NAS d'Entreprise / Grand Public` — Boîtier rackable ou de bureau intégrant des disques en RAID et un OS orienté stockage
- `Partage Multi-Protocoles` — Partage simultané des mêmes dossiers en SMB pour Windows et NFS pour Linux
**Origine :** Auspex Systems / Network Appliance (NetApp, 1992).
**Subtilités/confusions :**
- Un NAS intègre son propre système d'exploitation et processeur pour gérer les fichiers et le RAID.
**Urgences/dangers :** —
**Précautions :** Ne pas exposer l'interface de gestion d'un NAS directement sur Internet sans filtrage IP ou VPN.
**Équivalents :** SAN, Cloud Storage (S3)
**Voir aussi :** SAN, NFS, SMB, RAID

## `LAN` — Local Area Network [Réseau]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Réseau Local
**Contextes :** désigner l'infrastructure réseau reliant les ordinateurs, imprimantes et équipements au sein d'un même espace géographique restreint (maison, bureau, bâtiment)
**Rôle :** Réseau informatique limité à une zone géographique restreinte offrant des débits élevés et de faibles latences.
**Syntaxe :** (Infrastructure réseau physique et sans fil)
**Cas réguliers :**
- `Ethernet (IEEE 802.3)` — Connexion par câble réseau RJ45 à des débits de 1 à 10 Gbit/s
- `Wi-Fi (IEEE 802.11)` — Extension sans fil du réseau local
- `Adresses IP Privées` — Plages d'adresses d'administration réseau local (ex: `192.168.x.x`, `10.x.x.x`)
**Origine :** Ethernet (Xerox PARC, 1973) / Standardisé par l'IEEE 802.
**Subtilités/confusions :**
- Séparé du réseau étendu (**WAN** / Internet) par un routeur ou une passerelle effectuant de la traduction d'adresse (**NAT**).
**Urgences/dangers :** —
**Précautions :** Segmenter les grands réseaux locaux en **VLANs** distincts pour réduire les domaines de diffusion (*broadcast domains*) et renforcer la sécurité.
**Équivalents :** WLAN (Wi-Fi), WAN, MAN
**Voir aussi :** WAN, VLAN, ip, route

## `WAN` — Wide Area Network [Réseau]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Réseau Étendu
**Contextes :** désigner les réseaux de télécommunications couvrant de grandes distances géographiques (villes, pays, continent), Internet étant le plus grand WAN au monde
**Rôle :** Réseau informatique s'étendant sur une grande zone géographique, interconnectant plusieurs réseaux locaux (LAN).
**Syntaxe :** (Infrastructures de télécommunications longue distance)
**Cas réguliers :**
- `Internet` — Le WAN public mondial interconnectant tous les réseaux de la planète
- `Liaisons Spécialisées (MPLS, Fibre dédiée)` — Connexions louées auprès d'opérateurs pour relier des sites d'entreprise distants
**Origine :** ARPANET (1969) / Télécommunications mondiales.
**Subtilités/confusions :**
- Les débits WAN sont généralement plus faibles et les latences plus élevées que sur un LAN en raison des distances physiques franchies.
**Urgences/dangers :** —
**Précautions :** Chiffrer systématiquement tout le trafic transitant sur le WAN au moyen de VPN (IPsec, WireGuard) ou TLS.
**Équivalents :** Internet, MAN (Metropolitan Area Network)
**Voir aussi :** LAN, SD-WAN, VPN, IPsec

## `VLAN` — Virtual Local Area Network [Réseau]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** Réseau Local Virtuel / IEEE 802.1Q
**Contextes :** séparer logiquement plusieurs réseaux indépendants sur les mêmes équipements physiques (switchs réseau) pour isoler le trafic (ex: VLAN Utilisateurs, VLAN Serveurs, VLAN Wi-Fi Invités)
**Rôle :** Méthode de découpage logique d'un réseau local physique au niveau de la couche 2 (liaisons de données), identifié par un tag (VLAN ID de 1 à 4094).
**Syntaxe :** `ip link add link eth0 name eth0.10 type vlan id 10`
**Cas réguliers :**
- `Port Access` — Port de switch configuré pour appartenir à un seul VLAN non taggué (pour brancher un PC)
- `Port Trunk` — Port de switch véhiculant plusieurs VLANs taggués (pour relier deux switchs ou un hyperviseur)
- `Isolation de Sécurité` — Les machines de deux VLANs différents ne peuvent PAS communiquer sans passer par un routeur ou pare-feu !
**Origine :** IEEE 802.1Q (1998).
**Subtilités/confusions :**
- Permet de créer de la sécurité et d'endiguer les tempêtes de broadcast sans acheter des switchs physiques séparés.
**Urgences/dangers :** ⚠️ Attention aux attaques de "VLAN Hopping" si les configurations de ports Trunk ne sont pas sécurisées.
**Précautions :** Ne jamais utiliser le VLAN 1 par défaut pour le trafic d'administration du réseau.
**Équivalents :** VXLAN (extension Cloud)
**Voir aussi :** LAN, WAN, ip, route

## `WLAN` — Wireless Local Area Network [Réseau]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** Wi-Fi Network, IEEE 802.11
**Contextes :** administration réseau sans-fil, déploiement de bornes Wi-Fi, réseau d'entreprise et domicile
**Rôle :** Réseau local sans-fil basé sur les normes IEEE 802.11 permettant la connectivité sans câble physique via ondes radio (2.4 GHz, 5 GHz, 6 GHz).
**Syntaxe :** `iwconfig` ou `nmcli device wifi list`
**Cas réguliers :**
- `Connexion à un SSID WPA3` — Association sécurisée d'un client à un point d'accès via négociation SAE
- `VLAN Guest isolé` — Diffusion d'un SSID séparé pour visiteurs sur un VLAN dédié sans accès au LAN interne
**Origine :** Spécifié par l'IEEE 802.11 dès 1997, popularisé sous la marque Wi-Fi de la Wi-Fi Alliance dès 1999.
**Subtilités/confusions :**
- Confusion entre WLAN (réseau local sans-fil IEEE 802.11) et WWAN (réseau mobile cellulaire 4G/5G).
- Les bandes 2.4 GHz (longue portée, plus lente) et 5/6 GHz (courte portée, très rapide) répondent à des usages différents.
**Urgences/dangers :** ⚠️ Un SSID sans chiffrement expose tout le trafic à l'écoute passive (attaque Evil Twin / Rogue AP).
**Précautions :** Utiliser WPA3 ou WPA2-Enterprise (802.1X) ; désactiver WPS qui présente des vulnérabilités d'attaque par brute force.
**Équivalents :** Wi-Fi (marque commerciale)
**Voir aussi :** LAN, WAN, VLAN, Bluetooth, NFC

## `Bluetooth` — IEEE 802.15.1 WPAN [Réseau sans-fil]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** BT, IEEE 802.15.1
**Contextes :** connexion de périphériques à courte portée (écouteurs, claviers, souris, IoT), transfert de fichiers, audio sans-fil
**Rôle :** Technologie de réseau personnel sans-fil (WPAN) à courte portée (10–100 m) et faible consommation pour connecter des appareils sans câble.
**Syntaxe :** `bluetoothctl` (Linux) ou `hcitool scan`
**Cas réguliers :**
- `Appairage sécurisé SSP` — Association d'un casque audio via code PIN ou Simple Secure Pairing (Numeric Comparison)
- `BLE pour IoT` — Communication ultra-basse consommation d'un capteur de température vers un hub domotique
**Origine :** Développé par Ericsson en 1994, nommé d'après le roi viking Harald Bluetooth qui unifia des tribus danoises.
**Subtilités/confusions :**
- Différence critique entre Bluetooth Classic (haut débit, audio) et BLE/Bluetooth Low Energy (ultra-basse consommation, IoT) — ce sont deux modes de communication distincts.
- La portée annoncée varie fortement selon la classe de puissance : Class 1 (100 m), Class 2 (10 m), Class 3 (1 m).
**Urgences/dangers :** ⚠️ Bluebugging et Bluesnarfing permettent d'accéder aux données d'appareils Bluetooth mal sécurisés.
**Précautions :** Désactiver le mode découvrable dès que l'appairage est terminé ; mettre à jour le firmware des périphériques.
**Équivalents :** BLE, Zigbee (IoT), ANT+
**Voir aussi :** NFC, WLAN, WPAN, iwconfig

## `NFC` — Near Field Communication [Réseau sans-fil]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Communication en Champ Proche, ISO/IEC 18092
**Contextes :** paiement sans contact, contrôle d'accès bâtiment, lecture de tags d'information, appairage rapide de périphériques
**Rôle :** Technologie de communication sans-fil à très courte portée (< 10 cm) à 13.56 MHz permettant des échanges bidirectionnels ou la lecture de puces passives.
**Syntaxe :** (API Android NFC / iOS CoreNFC ; outil `nfc-list` sur Linux avec libnfc)
**Cas réguliers :**
- `Paiement mobile sans contact` — Échange sécurisé de jetons de paiement (tokenisation APDU) via Apple Pay / Google Pay
- `Badge d'accès RFID/NFC` — Lecture du numéro UID de la puce par le lecteur de porte sécurisée
**Origine :** Extension de la norme RFID ISO/IEC 14443 co-développée par Sony, NXP et Nokia en 2004.
**Subtilités/confusions :**
- Le NFC opère à 13.56 MHz (bande HF) tandis que le RFID couvre des bandes multiples (LF 125 kHz, HF 13.56 MHz, UHF 860-960 MHz).
- Le mode Peer-to-Peer NFC permet des échanges bidirectionnels alors que le RFID passif standard est unidirectionnel.
**Urgences/dangers :** ⚠️ Relay Attack : un attaquant peut relayer une communication NFC légitime à distance pour usurper un badge.
**Précautions :** Protéger les cartes NFC/RFID bancaires dans des étuis blindés RFID ; utiliser des applications nécessitant confirmation (biométrie, PIN).
**Équivalents :** RFID (superset), Bluetooth LE (appairage)
**Voir aussi :** RFID, Bluetooth, WLAN, ISO 14443

## `RFID` — Radio Frequency Identification [Réseau sans-fil]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Radio-identification, Étiquette Radio
**Contextes :** logistique, traçabilité d'inventaire, contrôle d'accès bâtiment, gestion d'animaux, anti-vol de marchandises
**Rôle :** Méthode d'identification à distance via des balises/puces radio (tags) pouvant être lues sans contact par un lecteur émettant un champ radio.
**Syntaxe :** (lecteurs propriétaires ; outil `proxmark3` pour analyse forensique)
**Cas réguliers :**
- `Inventaire automatique de stock entrepôt` — Lecture simultanée de centaines de tags UHF 915 MHz sans ligne de vue directe
- `Badge d'accès LF 125 kHz` — Lecture d'une puce EM4100 à la porte via un lecteur Wiegand
**Origine :** Origines dans les systèmes IFF (Identification Friend or Foe) militaires de la Seconde Guerre mondiale ; commercialisé dans les années 1980-90.
**Subtilités/confusions :**
- Tags passifs (alimentés par le champ RF du lecteur, portée faible) vs tags actifs (avec batterie interne, portée de dizaines de mètres).
- La bande UHF (860-960 MHz) permet des lectures à plusieurs mètres tandis que le LF (125 kHz) et HF (13.56 MHz) se limitent à quelques centimètres/mètres.
**Urgences/dangers :** ⚠️ Les cartes d'accès LF 125 kHz (EM4100, HID Prox) sont très facilement clonables avec un Proxmark3 ou un lecteur économique.
**Précautions :** Migrer vers des cartes à cryptographie embarquée (MIFARE DESFire, iClass Seos) résistantes au clonage.
**Équivalents :** NFC (sous-ensemble HF), Barcode (visuel)
**Voir aussi :** NFC, Bluetooth, IoT, Proxmark

## `5G` — 5th Generation Mobile Network [Télécoms]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** 5G NR, IMT-2020
**Contextes :** télécommunications mobiles, Edge Computing industriel, véhicules connectés, IoT massif, slice réseau
**Rôle :** Cinquième génération de standards de téléphonie mobile offrant très haut débit (> 10 Gbps), ultra-basse latence (< 1 ms) et connexion massive de terminaux IoT.
**Syntaxe :** (API opérateur, outils de drive test comme XCAL ; `mmcli` sur Linux)
**Cas réguliers :**
- `Network Slicing industriel` — Création d'une tranche réseau virtuelle dédiée à l'industrie 4.0 avec garanties de latence et débit
- `Déploiement gNodeB` — Connexion d'une station de base 5G New Radio au cœur de réseau 5G Core (5GC)
**Origine :** Normalisé par le 3GPP (Release 15 en 2018) pour succéder à la 4G LTE (Release 8).
**Subtilités/confusions :**
- Différence fondamentale entre 5G NSA (Non-Standalone : s'appuie sur le cœur de réseau 4G existant) et 5G SA (Standalone : cœur de réseau nativement 5G avec toutes les fonctionnalités).
- Ne pas confondre la 5G cellulaire (bande Sub-6 GHz ou mmWave) avec la bande Wi-Fi 5 GHz (WLAN IEEE 802.11ac/ax).
**Urgences/dangers :** ⚠️ Les terminaux 5G NSA restent vulnérables aux attaques IMSI Catcher héritées du réseau 4G sous-jacent.
**Précautions :** Pour les déploiements critiques (usine, santé), privilégier la 5G SA privée (Private 5G) avec contrôle total de l'infrastructure.
**Équivalents :** LTE-A Pro (prédécesseur), Wi-Fi 6E (concurrent en intérieur)
**Voir aussi :** LTE, 4G, eMBB, URLLC, Edge Computing

## `LTE` — Long Term Evolution [Télécoms]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** 4G, LTE-Advanced, LTE-A
**Contextes :** réseau mobile cellulaire 4G, communication de données mobiles, VoLTE, M2M/IoT
**Rôle :** Norme de télécommunication mobile de 4ème génération (4G) permettant des débits théoriques de 150 Mbps à plusieurs Gbps (LTE-Advanced Pro).
**Syntaxe :** (interface opérateur ; `mmcli -m 0` pour modem LTE sous Linux)
**Cas réguliers :**
- `Agrégation de porteuses LTE-Advanced` — Combinaison de plusieurs bandes fréquentielles pour multiplier le débit downlink
- `VoLTE (Voice over LTE)` — Transmission de la voix téléphonique sous forme de paquets IP sur le réseau de données LTE
**Origine :** Standardisé par le 3GPP dans la Release 8 en 2008, déployé commercialement par TeliaSonera en 2009.
**Subtilités/confusions :**
- Le LTE initial ne répondait pas strictement aux critères IMT-Advanced de l'UIT (il fut accepté par convention) ; seul LTE-Advanced est réellement 4G IMT-Advanced.
- VoLTE nécessite une prise en charge IMS (IP Multimedia Subsystem) de l'opérateur, non disponible partout.
**Urgences/dangers :** ⚠️ Des vulnérabilités LTE (attaques aLTEr, ReVoLTE) permettent d'intercepter des communications voix et données.
**Précautions :** Utiliser des applications de communication chiffrées de bout en bout (Signal, Element) même sur LTE.
**Équivalents :** 4G, HSPA+ (3G amélioré), WiMAX
**Voir aussi :** 5G, VoLTE, WLAN, GSM

## `PAT` — Port Address Translation [Réseau]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** NAPT, NAT Overload, NAT avec surcharge de ports
**Contextes :** routage réseau, translation d'adresses NAT, accès Internet partagé depuis un réseau privé
**Rôle :** Extension du NAT permettant à de nombreuses adresses IP privées d'être représentées par une seule adresse IP publique, grâce à des numéros de ports TCP/UDP distincts.
**Syntaxe :** (configuration routeur/pare-feu ; `iptables -t nat -A POSTROUTING -j MASQUERADE`)
**Cas réguliers :**
- `Redirection de port entrant (DNAT)` — Renvoi du port externe 8080 vers le port 80 du serveur web interne 192.168.1.10
- `Partage Internet multi-hôtes (SNAT/Masquerade)` — 50 postes utilisent la même IP publique avec des ports sources distincts
**Origine :** Développé pour contourner la pénurie d'adresses IPv4 dans les années 1990 ; formalisé dans la RFC 3022.
**Subtilités/confusions :**
- PAT est également nommé NAPT (Network Address and Port Translation) ou NAT Overloaded selon les constructeurs.
- Le PAT modifie à la fois l'adresse IP source ET le numéro de port source dans chaque paquet — cassant les protocoles qui intègrent l'IP dans leur payload applicatif (ex: SIP, FTP actif).
**Urgences/dangers :** ⚠️ Le PAT rend difficile le suivi de connexion (forensics réseau) car de nombreux hôtes partagent la même IP publique.
**Précautions :** Loguer les associations port→IP privée côté pare-feu pour conserver la traçabilité légale (RGPD, obligation légale de conservation des logs).
**Équivalents :** NAT Masquerade, NAPT
**Voir aussi :** NAT, IP, iptables, nftables

## `ICMP` — Internet Control Message Protocol [Réseau]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** ICMPv4, RFC 792
**Contextes :** diagnostic réseau, détection de joignabilité, analyse de route, gestion d'erreurs IP
**Rôle :** Protocole de la couche réseau (Layer 3) utilisé par les équipements IP pour envoyer des messages d'erreur et d'information de contrôle sans utiliser TCP ni UDP.
**Syntaxe :** `ping 8.8.8.8` ou `traceroute -I host.example.com`
**Cas réguliers :**
- `Test de joignabilité (ping)` — Envoi de requêtes ICMP Echo Request (type 8) et réception de Echo Reply (type 0)
- `Analyse de route (traceroute TTL)` — Réception successive de messages ICMP Time Exceeded (type 11) à chaque saut de routeur
**Origine :** Défini dans la RFC 792 de 1981 pour IPv4 ; ICMPv6 redéfini dans la RFC 4443 pour IPv6.
**Subtilités/confusions :**
- ICMP n'utilise ni TCP ni UDP : il s'encapsule directement dans des datagrammes IP avec le numéro de protocole 1.
- Bloquer entièrement ICMP dans un pare-feu casse le mécanisme Path MTU Discovery (PMTUD) et empêche les messages de fragmentation nécessaire.
**Urgences/dangers :** ⚠️ ICMP peut être utilisé pour des canaux de communication furtifs (ICMP tunneling) ou pour du Smurf DDoS.
**Précautions :** Filtrer sélectivement ICMP : autoriser les types essentiels (Echo, Destination Unreachable, Time Exceeded) ; bloquer Redirect et Timestamp.
**Équivalents :** ICMPv6, NDPv6
**Voir aussi :** ping, traceroute, IP, TTL

## `NDP` — Neighbor Discovery Protocol [Réseau IPv6]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** IPv6 ND, RFC 4861
**Contextes :** réseau IPv6, résolution d'adresses, découverte de routeurs, autoconfiguration SLAAC
**Rôle :** Protocole IPv6 remplaçant intégralement ARP pour la résolution d'adresses de couche 2 et assurant de nombreuses autres fonctions réseau.
**Syntaxe :** `ip -6 neigh show` ou `rdisc6 eth0`
**Cas réguliers :**
- `Résolution d'adresse (Neighbor Solicitation/Advertisement)` — Découverte de l'adresse MAC associée à une adresse IPv6 voisine
- `Autoconfiguration SLAAC` — Réception de messages Router Advertisement (RA) contenant le préfixe réseau pour configurer automatiquement l'interface
**Origine :** Spécifié dans la RFC 4861 en 2007 comme composant fondamental d'IPv6.
**Subtilités/confusions :**
- NDP utilise des messages ICMPv6 (et non des trames broadcast ARP) pour l'ensemble de ses fonctions de découverte de voisinage.
- NDP intègre nativement la Détection d'Adresses Dupliquées (DAD) pour vérifier l'unicité avant d'utiliser une adresse IPv6.
**Urgences/dangers :** ⚠️ Les attaques NDP Spoofing (équivalent d'ARP Poisoning en IPv4) permettent l'interception du trafic IPv6 sur un segment réseau.
**Précautions :** Activer la protection RA Guard sur les commutateurs réseau pour bloquer les faux Router Advertisements malveillants.
**Équivalents :** ARP (équivalent IPv4)
**Voir aussi :** ARP, IPv6, ICMPv6, SLAAC

## `BGP` — Border Gateway Protocol [Réseau]
**Niveau :** expert | **Popularité :** 91 | **Aliases :** BGP-4, RFC 4271, EGP
**Contextes :** routage inter-opérateurs (Internet), interconnexion d'Autonomous Systems, peering entre FAI, routage des datacenters cloud
**Rôle :** Protocole de routage à vecteur de chemin (Path-Vector) utilisé pour échanger des informations de routage entre Autonomous Systems (AS) distincts sur Internet.
**Syntaxe :** (démons BGP : `gobgp`, `bird`, `frrouting` ; `show bgp summary` sur Cisco/Juniper)
**Cas réguliers :**
- `Peering eBGP entre deux FAI` — Échange de tables de routage complètes entre deux Autonomous Systems distincts via session TCP 179
- `Annonce de préfixe IP` — Publication d'un bloc d'adresses IPv4/IPv6 propre par un AS vers ses pairs BGP
**Origine :** Apparu en 1989, version BGP-4 finalisée dans la RFC 4271 — il constitue la colonne vertébrale du routage Internet mondial.
**Subtilités/confusions :**
- Différence fondamentale entre eBGP (External BGP : sessions entre AS différents, TTL=1) et iBGP (Internal BGP : sessions à l'intérieur du même AS, nécessitant une full-mesh ou des Route Reflectors).
- BGP ne choisit pas la route la plus rapide mais la meilleure selon une suite de critères de sélection de chemin : LOCAL_PREF, AS_PATH, MED, etc.
**Urgences/dangers :** ⚠️ Le BGP Hijacking (détournement de préfixe) permet à un AS malveillant d'annoncer illégitimement des blocs d'adresses IP appartenant à d'autres — menaçant la stabilité d'Internet.
**Précautions :** Déployer RPKI (Resource Public Key Infrastructure) pour valider cryptographiquement l'origine des annonces BGP.
**Équivalents :** OSPF (interne, IGP), EGP (prédécesseur obsolète)
**Voir aussi :** AS, OSPF, RIP, RPKI, IP

## `OSPF` — Open Shortest Path First [Réseau]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** OSPFv2, OSPFv3, IGP Link-State
**Contextes :** routage interne d'entreprise, FAI, campus réseau, datacenter interne
**Rôle :** Protocole de routage interne à état de lien (Link-State IGP) calculant les meilleures routes via l'algorithme de Dijkstra (SPF).
**Syntaxe :** (démons : `ospfd` (Quagga/FRR) ; `show ip ospf neighbor` sur Cisco)
**Cas réguliers :**
- `Calcul de table de routage SPF` — Exécution de l'algorithme de Dijkstra sur la LSDB (Link State Database) pour trouver les chemins les plus courts
- `Découpage en Areas OSPF` — Configuration de l'Area 0 (backbone) et d'areas secondaires pour réduire la taille des tables de routage
**Origine :** Développé par l'IETF ; OSPFv2 défini dans la RFC 2328 (IPv4), OSPFv3 dans la RFC 5340 (IPv6).
**Subtilités/confusions :**
- OSPF exige obligatoirement que toutes ses Areas soient connectées à l'Area 0 (backbone) — une Area non reliée à Area 0 ne peut pas fonctionner correctement.
- Contrairement à BGP (inter-AS), OSPF est un protocole IGP réservé à l'administration interne d'un seul domaine.
**Urgences/dangers :** ⚠️ Un routeur OSPF malveillant injecté sur le réseau peut annoncer des routes frauduleuses et dévier le trafic.
**Précautions :** Authentifier les échanges OSPF entre routeurs (MD5 ou SHA-HMAC) pour empêcher l'injection de routes non autorisées.
**Équivalents :** IS-IS (protocole similaire chez les opérateurs), RIP (obsolète)
**Voir aussi :** BGP, RIP, Dijkstra, Router, AS

## `IGMP` — Internet Group Management Protocol [Réseau]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** RFC 3376, Multicast Group Management
**Contextes :** streaming IPTV, multicast applicatif, réseau d'entreprise utilisant des flux Multicast IP
**Rôle :** Protocole de gestion des groupes Multicast IPv4 permettant aux hôtes de signaler leur souhait de recevoir des flux multicast à leur routeur local.
**Syntaxe :** (configuration routeur : `ip igmp version 3` ; analyse : `tcpdump -i eth0 igmp`)
**Cas réguliers :**
- `Adhésion à un flux IPTV` — Envoi d'un IGMP Membership Report (Join) par le décodeur TV vers le routeur pour recevoir le flux multicast
- `IGMP Snooping sur switch` — Interception des messages IGMP par le commutateur pour limiter le flux multicast aux seuls ports abonnés
**Origine :** Défini successivement dans la RFC 1112 (v1), RFC 2236 (v2) et RFC 3376 (v3) de 2002.
**Subtilités/confusions :**
- IGMP opère entre l'hôte et le routeur local pour la gestion des adhésions — ce n'est pas lui qui gère le routage multicast inter-domaines (rôle de PIM, Protocol Independent Multicast).
- En IPv6, IGMP est intégralement remplacé par MLD (Multicast Listener Discovery), utilisant des messages ICMPv6.
**Urgences/dangers :** ⚠️ En l'absence d'IGMP Snooping sur les switches, tous les ports reçoivent les flux multicast, saturant la bande passante.
**Précautions :** Activer IGMP Snooping sur tous les commutateurs qui acheminent du trafic multicast pour optimiser la bande passante.
**Équivalents :** MLD (équivalent IPv6)
**Voir aussi :** Multicast, PIM, ICMPv6, VLAN

## `TTL` — Time to Live [Réseau]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Hop Limit (IPv6), Time-to-Live
**Contextes :** contrôle de boucles de routage IP, diagnostic réseau, sécurité, enregistrements DNS
**Rôle :** Valeur numérique dans l'en-tête IPv4 (ou Hop Limit IPv6) décrémentée à chaque saut de routeur pour limiter la durée de vie d'un paquet et éviter les boucles de routage infinies.
**Syntaxe :** `ping -t 64 host` ou `traceroute --ttl 1-30 host`
**Cas réguliers :**
- `Prévention de boucle de routage` — Abandon du paquet et envoi d'un message ICMP Time Exceeded quand TTL atteint 0
- `Fingerprinting d'OS (TTL initial)` — Linux démarre à TTL=64, Windows à TTL=128, certains Cisco à TTL=255
**Origine :** Défini dans la RFC 791 (1981) avec le protocole IPv4.
**Subtilités/confusions :**
- En IPv6, le champ s'appelle Hop Limit (sémantique plus précise) et non plus TTL — mais le comportement est identique.
- Le TTL réseau (en sauts de routeurs) est radicalement différent du TTL DNS (durée de vie d'un enregistrement en cache, en secondes).
**Urgences/dangers :** —
**Précautions :** Ne pas se fier au TTL observé pour fingerprinter un OS de manière certaine : des proxies, VPN ou NAT peuvent altérer la valeur.
**Équivalents :** Hop Limit (IPv6)
**Voir aussi :** IP, ICMP, ping, traceroute, DNS

## `MTU` — Maximum Transmission Unit [Réseau]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** Maximum Transfer Unit, Path MTU
**Contextes :** administration réseau, configuration VPN, optimisation de performances réseau
**Rôle :** Taille maximale en octets d'un paquet de couche réseau (L3) pouvant être transmis en une seule trame réseau physique sans fragmentation.
**Syntaxe :** `ip link set eth0 mtu 1400` ou `ping -M do -s 1472 8.8.8.8`
**Cas réguliers :**
- `Configuration MTU Ethernet standard` — Paramétrage à 1500 octets (valeur par défaut Ethernet IEEE 802.3)
- `Ajustement MTU pour VPN IPSec/WireGuard` — Réduction à 1420 octets pour tenir compte des en-têtes de tunneling et éviter la fragmentation
**Origine :** Spécifié dans les normes réseau Ethernet et TCP/IP ; Path MTU Discovery défini dans la RFC 1191.
**Subtilités/confusions :**
- Un paquet IP dépassant le MTU de l'interface sera fragmenté (si bit DF=0) ou rejeté avec message ICMP (si bit DF=1) — ce qui casse les VPN si le MTU n'est pas correctement ajusté.
- Le MTU Ethernet standard est 1500 octets, mais les Jumbo Frames permettent d'atteindre 9000 octets sur des réseaux configurés en conséquence.
**Urgences/dangers :** ⚠️ Un MTU mal configuré sur un tunnel VPN provoque des connexions lentes, aléatoires ou des coupures inexpliquées car les paquets trop grands sont silencieusement abandonnés.
**Précautions :** Toujours ajuster le MSS TCP (TCP MSS Clamping) côté pare-feu pour éviter les problèmes de fragmentation avec les VPN.
**Équivalents :** MSS (Maximum Segment Size, couche TCP)
**Voir aussi :** IP, Ethernet, VPN, ICMP, Jumbo Frames

## `MAC Address` — Media Access Control Address [Réseau]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Adresse MAC, Hardware Address, Physical Address, Adresse physique
**Contextes :** communication Ethernet, filtrage réseau, ARP/NDP, identification de périphérique réseau, Wi-Fi
**Rôle :** Identifiant physique unique sur 48 bits (6 octets en hexadécimal) attribué à chaque interface réseau par son fabricant pour identifier de manière unique un équipement sur un segment réseau.
**Syntaxe :** `ip link show eth0` ou `ifconfig eth0` ou `macchanger -s eth0`
**Cas réguliers :**
- `Filtrage d'accès réseau par MAC` — Restriction d'accès Wi-Fi aux seules cartes réseau dont l'adresse MAC est pré-enregistrée
- `Analyse des 3 premiers octets (OUI)` — Identification du fabricant de la carte réseau via l'Organizationally Unique Identifier
**Origine :** Défini par l'IEEE dans les standards 802 (Ethernet, Wi-Fi) pour les adresses de couche 2 (Data Link Layer).
**Subtilités/confusions :**
- L'adresse MAC est normalement unique et gravée en usine (burned-in address), mais elle peut être usurpée (MAC Spoofing) au niveau logiciel sans privilège physique.
- Le filtrage réseau par adresse MAC n'est pas un mécanisme de sécurité fiable car l'adresse est transmise en clair et facilement clonée avec des outils comme `macchanger`.
**Urgences/dangers :** ⚠️ Le MAC Spoofing permet de contourner les filtrages par adresse MAC et de se faire passer pour un équipement légitime sur le réseau.
**Précautions :** Ne pas utiliser le filtrage MAC comme seule mesure de sécurité ; combiner avec 802.1X/EAP pour une authentification réseau robuste.
**Équivalents :** BSSID (adresse MAC d'un point d'accès Wi-Fi)
**Voir aussi :** Ethernet, ARP, NDP, IP, WLAN

## `SRAM` — Static Random Access Memory [Matériel]
**Niveau :** avance | **Popularité :** 79 | **Aliases :** Static RAM, Cache RAM
**Contextes :** caches CPU (L1/L2/L3), registres, mémoires embarquées haute vitesse dans les microcontrôleurs
**Rôle :** Mémoire vive utilisant des bascules logiques (flip-flops) à 6 transistors, extrêmement rapide et stable, ne nécessitant aucun rafraîchissement électrique périodique.
**Syntaxe :** (interne au CPU, non adressable directement ; `lscpu | grep cache`)
**Cas réguliers :**
- `Cache CPU L1 d'instruction et données` — Accès en 1 à 4 cycles d'horloge, stockage des instructions et données les plus fréquemment utilisées
- `Registres de microcontrôleur` — Stockage ultra-rapide de variables temporaires dans les SoC embarqués
**Origine :** Développée dans les années 1960 par Robert H. Norman chez Fairchild Semiconductor, précédant la DRAM.
**Subtilités/confusions :**
- La SRAM est 5 à 10 fois plus rapide que la DRAM mais occupe jusqu'à 6 fois plus de surface de silicium pour le même nombre de bits — d'où son coût prohibitif en grande quantité.
- La SRAM conserve ses données tant qu'elle est alimentée électriquement (mémoire volatile) sans avoir besoin de cycles de rafraîchissement.
**Urgences/dangers :** —
**Précautions :** Le dimensionnement du cache SRAM est critique pour les performances CPU — un miss de cache L1 peut coûter 10 à 100 cycles de latence supplémentaires.
**Équivalents :** DRAM (alternative moins chère et plus dense)
**Voir aussi :** DRAM, CPU, L1/L2/L3 Cache, ALU

## `DRAM` — Dynamic Random Access Memory [Matériel]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** DDR SDRAM, Mémoire Dynamique
**Contextes :** mémoire vive principale des ordinateurs (RAM système), serveurs, smartphones
**Rôle :** Mémoire vive utilisant des condensateurs pour stocker les bits, offrant une haute densité d'intégration et un faible coût par gigaoctet, mais nécessitant un rafraîchissement électrique constant.
**Syntaxe :** `dmidecode --type 17` ou `lshw -class memory`
**Cas réguliers :**
- `RAM principale système (DDR4/DDR5)` — Stockage temporaire de tout le code et des données des programmes en cours d'exécution
- `Cycle de rafraîchissement DRAM` — Recharge électrique périodique des condensateurs (toutes les quelques millisecondes) pour éviter la perte de données
**Origine :** Inventée par Robert Dennard à l'IBM Thomas J. Watson Research Center en 1966, brevet déposé en 1968.
**Subtilités/confusions :**
- Contrairement à la SRAM, la DRAM perd progressivement sa charge et doit être rafraîchie en permanence — d'où le terme "dynamique".
- L'évolution SDRAM → DDR → DDR2 → DDR3 → DDR4 → DDR5 a multiplié le débit et réduit la tension d'alimentation à chaque génération.
**Urgences/dangers :** ⚠️ Les attaques Rowhammer exploitent les fuites électriques des cellules DRAM pour faire basculer des bits dans des lignes mémoire adjacentes, compromettant la sécurité.
**Précautions :** Utiliser des modules ECC RAM sur les serveurs pour détecter et corriger automatiquement les erreurs de bit dues aux rayons cosmiques ou à la dégradation des cellules.
**Équivalents :** SRAM (plus rapide mais plus chère), LPDDR (variante basse consommation pour mobile)
**Voir aussi :** SRAM, ECC RAM, DIMM, RAM

## `VRAM` — Video Random Access Memory [Matériel]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** GPU Memory, GDDR, HBM
**Contextes :** rendu graphique 3D, jeux vidéo haute résolution, entraînement de modèles IA, calcul GPGPU
**Rôle :** Mémoire vive haute bande passante dédiée au GPU pour le stockage des textures, frame buffers, shaders et modèles IA pendant le rendu ou le calcul.
**Syntaxe :** `nvidia-smi --query-gpu=memory.total,memory.used --format=csv` ou `rocm-smi --showmeminfo vram`
**Cas réguliers :**
- `Chargement de textures 4K pour rendu temps réel` — Stockage de dizaines de Go de textures et maillages 3D dans la GDDR6X du GPU
- `Entraînement d'un LLM` — Les poids du modèle doivent tenir dans la VRAM pour un entraînement direct (ex: 70B paramètres ≈ 140 Go en FP16)
**Origine :** Conçue dans les années 1980 pour éliminer les conflits d'accès entre le processeur système et le circuit d'affichage.
**Subtilités/confusions :**
- Les technologies VRAM modernes incluent GDDR6/6X (optimisée débit) et HBM3 (empilée, bande passante extrême à latence réduite) — ce sont des technologies physiquement très différentes.
- Manquer de VRAM oblige le GPU à décharger vers la RAM système via PCIe : le débit chute dramatiquement (de 1000 Go/s à 30 Go/s), multipliant par 30 le temps de calcul.
**Urgences/dangers :** —
**Précautions :** Surveiller l'utilisation VRAM via `nvidia-smi` ; dimensionner la VRAM selon les exigences du modèle ou de la résolution cible avant l'achat du GPU.
**Équivalents :** GDDR6X (NVIDIA RTX), HBM3 (H100/MI300X), LPDDR5 (GPU mobile)
**Voir aussi :** GPU, RAM, PCIe, DRAM

## `ECC RAM` — Error-Correcting Code RAM [Matériel]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** ECC Memory, Registered ECC, RDIMM
**Contextes :** serveurs, stations de travail professionnelles, centres de données, calcul scientifique critique
**Rôle :** Mémoire vive équipée d'un circuit de correction d'erreurs capable de détecter et corriger automatiquement les inversions de bits simples (Single Bit Error) et de détecter les erreurs multiples.
**Syntaxe :** `edac-util -s` (Linux) ou `dmidecode --type 17 | grep Error`
**Cas réguliers :**
- `Correction automatique d'erreur SBE` — Correction silencieuse d'un bit inversé par rayons cosmiques sans interruption du service
- `Détection d'erreur MBE non corrigeable` — Journalisation d'une erreur multi-bits grave et alerte d'urgence sur le serveur
**Origine :** Basée sur les codes de Hamming développés chez Bell Labs par Richard Hamming dans les années 1950.
**Subtilités/confusions :**
- L'ECC RAM nécessite un contrôleur mémoire compatible sur le CPU et une carte mère supportant ECC (généralement uniquement les plateformes Xeon, EPYC ou Threadripper Pro).
- L'ECC ne protège pas contre les pannes matérielles complètes du module mémoire — seul le RAID mémoire ou la duplication offre ce niveau de redondance.
**Urgences/dangers :** ⚠️ Des erreurs de bits silencieuses (bit flips) en RAM non-ECC peuvent corrompre des données critiques — bases de données, résultats scientifiques — sans aucun avertissement.
**Précautions :** Surveiller régulièrement les compteurs d'erreurs ECC corrigées via `edac-util` ou IPMI — une augmentation soudaine signale un module défaillant à remplacer.
**Équivalents :** RDIMM (avec registre tampon), LRDIMM (Load-Reduced DIMM)
**Voir aussi :** DRAM, DIMM, SRAM, RAM, Server

## `DIMM` — Dual In-line Memory Module [Matériel]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** Barrette mémoire, SO-DIMM, RDIMM
**Contextes :** assemblage PC et serveur, upgrade mémoire RAM, diagnostic matériel
**Rôle :** Format standard de barrette de mémoire vive (RAM) pour les ordinateurs de bureau, serveurs et postes de travail, comportant des circuits indépendants sur les deux faces du PCB.
**Syntaxe :** `dmidecode --type 17` ou `lshw -class memory`
**Cas réguliers :**
- `Installation en mode Dual-Channel` — Insertion de deux barrettes DIMM identiques sur les slots de couleurs identiques pour doubler la bande passante mémoire
- `Choix entre DIMM et SO-DIMM` — Sélection du format compact SO-DIMM pour un ordinateur portable versus le format pleine taille DIMM pour un PC de bureau
**Origine :** Introduit à la fin des années 1990 pour remplacer les anciens modules SIMM (Single In-line Memory Module) à 32 bits.
**Subtilités/confusions :**
- Les barrettes SO-DIMM (Small Outline DIMM) pour portables sont physiquement incompatibles avec les slots DIMM pour PC de bureau malgré le même type de DRAM.
- Les modules RDIMM (Registered DIMM) pour serveurs intègrent un registre tampon supplémentaire permettant de connecter plus de modules mais avec 1 cycle de latence supplémentaire.
**Urgences/dangers :** —
**Précautions :** Toujours installer les barrettes par paires dans les bons slots (consulter le manuel de la carte mère) pour bénéficier du mode Dual-Channel.
**Équivalents :** SO-DIMM (portable), RDIMM (serveur), LRDIMM (très grand serveur)
**Voir aussi :** DRAM, ECC RAM, RAM, Motherboard

## `SoC` — System on Chip [Matériel]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** System-on-a-Chip, Puce System
**Contextes :** smartphones, tablettes, systèmes embarqués, IoT, ordinateurs Apple Silicon, Raspberry Pi
**Rôle :** Circuit intégré rassemblant sur un seul et même dé de silicium le CPU, GPU, mémoire, contrôleurs d'E/S, puces radio et souvent une NPU — éliminant le besoin de multiples composants séparés.
**Syntaxe :** `cat /proc/cpuinfo | grep "Model name"` ou `system_profiler SPHardwareDataType` (macOS)
**Cas réguliers :**
- `Apple M-series (Mac/iPad)` — Architecture SoC unifiée intégrant CPU, GPU, NPU et mémoire unifiée sur une seule puce à haute efficacité énergétique
- `Qualcomm Snapdragon (Android)` — SoC mobile intégrant le modem 5G, CPU ARM, GPU Adreno et DSP dans un package unique
**Origine :** Émergé dans les années 1990 avec le développement de la micro-électronique pour la téléphonie mobile ; popularisé par ARM et ses partenaires de licence.
**Subtilités/confusions :**
- La mémoire dite "Unified Memory" des SoC Apple Silicon est physiquement intégrée au package du SoC, permettant un accès partagé CPU/GPU à très faible latence — ce n'est pas de la RAM ordinaire DIMM.
- Les composants d'un SoC sont gravés ensemble et non évolutifs individuellement — contrairement à un PC où CPU, GPU et RAM sont des composants distincts interchangeables.
**Urgences/dangers :** —
**Précautions :** Vérifier la compatibilité matérielle des logiciels avant d'acquérir un appareil à SoC ARM (notamment pour la compatibilité x86 via émulation Rosetta 2 / WSL2).
**Équivalents :** MCU (Microcontroller Unit, version embarquée simplifiée)
**Voir aussi :** CPU, GPU, NPU, ARM, PCIe

## `ASIC` — Application-Specific Integrated Circuit [Matériel]
**Niveau :** expert | **Popularité :** 83 | **Aliases :** Circuit Intégré Spécifique, Custom IC
**Contextes :** minage de cryptomonnaie, commutateurs réseau haute vitesse, traitement du signal numérique, automobile
**Rôle :** Circuit intégré entièrement personnalisé et optimisé pour une tâche ou un algorithme unique, offrant les meilleures performances énergétiques mais sans possibilité de reprogrammation.
**Syntaxe :** (n/a — matériel ; `ethtool -i eth0` pour identifier une puce ASIC réseau)
**Cas réguliers :**
- `Minage Bitcoin par ASIC` — Exécution d'algorithmes SHA-256 à des vitesses de plusieurs pétahashes/seconde impossibles avec un CPU ou GPU
- `ASIC de commutation réseau` — Commutation de paquets Ethernet à la vitesse du fil (line-rate) dans les switches datacenter
**Origine :** Développé à partir des années 1980 grâce à la progression de la lithographie VLSI ; coûts de développement NRE (Non-Recurring Engineering) très élevés.
**Subtilités/confusions :**
- Un ASIC ne peut pas être modifié ou reprogrammé après sa fabrication — contrairement à un FPGA qui est reconfigurable, ou à un CPU qui est entièrement programmable.
- Le coût NRE d'un ASIC (design + masques de gravure) peut dépasser plusieurs millions d'euros, justifié uniquement par de très grands volumes de production.
**Urgences/dangers :** —
**Précautions :** Pour une application dont les spécifications évoluent, privilégier le FPGA (prototypage) avant de valider un design ASIC pour la production en volume.
**Équivalents :** FPGA (reconfigurable), SoC (générique)
**Voir aussi :** FPGA, SoC, GPU, CPU

## `FPGA` — Field-Programmable Gate Array [Matériel]
**Niveau :** expert | **Popularité :** 80 | **Aliases :** Réseau de Portes Programmables, Logic Array
**Contextes :** prototypage matériel, traitement du signal DSP, trading haute fréquence, aéronautique/défense, accélération réseau
**Rôle :** Circuit intégré contenant une matrice de blocs logiques configurables post-fabrication, permettant d'implémenter des circuits numériques personnalisés via des langages de description matérielle (VHDL, Verilog).
**Syntaxe :** (chaînes de synthèse : Vivado (Xilinx/AMD), Quartus (Intel) ; déploiement via JTAG)
**Cas réguliers :**
- `Prototypage d'architecture RISC-V` — Implémentation et simulation d'un nouveau processeur RISC-V sur carte FPGA avant gravure en ASIC
- `Accélération de traitement réseau SmartNIC` — Déchargement du traitement des paquets OVS/DPDK directement sur la puce FPGA de la carte réseau
**Origine :** Inventé par Ross Freeman et Bernard Vonderschmitt, co-fondateurs de Xilinx, en 1984.
**Subtilités/confusions :**
- Contrairement aux microprocesseurs (exécution séquentielle), un FPGA s'exécute de manière massivement parallèle en matériel — chaque bloc logique opère simultanément.
- La programmation FPGA se fait en VHDL ou Verilog (HDL), des langages qui décrivent des circuits matériels et non des séquences d'instructions logicielles.
**Urgences/dangers :** —
**Précautions :** Valider la conception avec des simulations (ModelSim, Questa) et prendre en compte les contraintes de timing et de placement avant la synthèse.
**Équivalents :** CPLD (Complex Programmable Logic Device, moins dense), ASIC (non reconfigurable)
**Voir aussi :** ASIC, SoC, VHDL, Verilog

## `ALU` — Arithmetic Logic Unit [Architecture CPU]
**Niveau :** expert | **Popularité :** 78 | **Aliases :** Unité d'Arithmétique et de Logique, UAL
**Contextes :** architecture de processeur, enseignement informatique, conception de CPU, compilation
**Rôle :** Composant fondamental du processeur effectuant toutes les opérations arithmétiques (addition, soustraction) et logiques (AND, OR, XOR, NOT) sur des opérandes binaires.
**Syntaxe :** (interne au CPU — observable via `perf stat -e instructions,cycles ./programme`)
**Cas réguliers :**
- `Exécution d'instruction ADD sur registres` — Sommation de deux valeurs 64 bits en un cycle d'horloge via l'ALU entière
- `Mise à jour des drapeaux CPU (Flags)` — Positionnement du flag Zero (Z), Carry (C), Overflow (V) après comparaison logique par l'ALU
**Origine :** Conceptualisée par le mathématicien John von Neumann en 1945 dans son rapport fondateur sur l'architecture EDVAC.
**Subtilités/confusions :**
- L'ALU ne traite que les nombres entiers (opérations en virgule fixe) ; les calculs à virgule flottante sont délégués à une unité spécialisée distincte : la FPU (Floating Point Unit).
- L'ALU est contrôlée par l'Unité de Contrôle (Control Unit) du processeur qui lui fournit les opérandes depuis les registres et le signal d'opération à effectuer.
**Urgences/dangers :** —
**Précautions :** Lors de la conception de code critique (cryptographie, calcul financier), valider les comportements d'overflow et de carry de l'ALU pour chaque architecture cible.
**Équivalents :** FPU (virgule flottante), SIMD/AVX (calcul vectoriel parallèle)
**Voir aussi :** CPU, FPU, Registers, SoC, FPGA

## `L1/L2/L3 Cache` — Multi-Level CPU Cache [Architecture CPU]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** Cache CPU, Mémoire Cache, CPU Cache
**Contextes :** architecture processeur, performance logicielle, optimisation d'algorithmes, tuning système
**Rôle :** Hiérarchie de mémoires tampons ultra-rapides (SRAM) intégrées au processeur pour réduire la latence d'accès à la RAM principale en stockant les instructions et données les plus fréquemment utilisées.
**Syntaxe :** `lscpu | grep -i cache` ou `cat /sys/devices/system/cpu/cpu0/cache/index*/size`
**Cas réguliers :**
- `Hit de cache L1 en 1-4 cycles` — Accès à une donnée résidant dans le L1 d'instruction/données sans latence RAM
- `Miss L2/L3 → accès RAM` — Latence de 30 à 300 cycles supplémentaires lors d'un défaut de cache vers la RAM principale
**Origine :** Introduit progressivement : cache L1 sur processeur Intel 80486 (1989), L2 sur Pentium Pro (1995), L3 généralisé avec Intel Xeon et Core 2 Extreme.
**Subtilités/confusions :**
- L1 est partagé entre le cœur et unique (split I-cache / D-cache, 32-64 KB) ; L2 est par cœur ; L3 est partagé entre tous les cœurs du processeur — chaque niveau équilibre vitesse et capacité.
- La cohérence des caches multi-cœurs est maintenue par des protocoles matériels comme MESI (Modified-Exclusive-Shared-Invalid) — transparent pour le développeur sauf pour la programmation concurrente.
**Urgences/dangers :** ⚠️ Les attaques Spectre et Meltdown exploitent les comportements du cache CPU pour exfiltrer des données confidentielles entre processus isolés.
**Précautions :** Aligner les structures de données critiques en mémoire sur les lignes de cache (64 octets) pour maximiser les taux de hit et éviter le false sharing entre threads.
**Équivalents :** TLB (Translation Lookaside Buffer, cache MMU)
**Voir aussi :** CPU, SRAM, DRAM, ALU, RAM

## `S.M.A.R.T.` — Self-Monitoring Analysis and Reporting Technology [Stockage]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** SMART, Self-Monitoring
**Contextes :** diagnostic disque dur HDD, surveillance SSD, prévention de panne de stockage, monitoring infrastructure
**Rôle :** Système d'autosurveillance intégré aux disques HDD et SSD permettant de détecter les signes précoces de défaillance imminente via des attributs de santé standardisés.
**Syntaxe :** `smartctl -a /dev/sda` ou `smartctl -t short /dev/sda` (test court)
**Cas réguliers :**
- `Vérification de la santé du SSD` — Lecture du Percentage Used (% de cycles d'écriture consommés) et des secteurs réalloués
- `Analyse d'un disque HDD suspect` — Détection d'augmentation des Reallocated Sectors Count (attribut 5) et des Uncorrectable Errors (attribut 187)
**Origine :** Développé conjointement par IBM, Compaq, Seagate et Western Digital à la fin des années 1990 pour anticiper les pannes mécaniques des HDD.
**Subtilités/confusions :**
- S.M.A.R.T. peut fournir des faux négatifs critiques : un disque peut présenter tous les attributs SMART dans les normes et tomber en panne brutalement.
- Les seuils des attributs SMART varient selon les constructeurs et les technologies (SATA HDD vs NVMe SSD) — seul un historique d'évolution est vraiment significatif, pas une valeur instantanée.
**Urgences/dangers :** ⚠️ Un attribut SMART "FAIL" ou une augmentation rapide des secteurs réalloués signifie une panne imminente — sauvegarder immédiatement les données.
**Précautions :** Configurer des alertes automatiques via `smartd` (démon Linux) pour être notifié par email avant la panne physique d'un disque.
**Équivalents :** NVMe Health Information Log (standard NVMe équivalent)
**Voir aussi :** HDD, SSD, NVMe, smartctl, RAID

## `AHCI` — Advanced Host Controller Interface [Stockage]
**Niveau :** avance | **Popularité :** 76 | **Aliases :** SATA AHCI, Mode AHCI
**Contextes :** contrôleur de stockage SATA, configuration BIOS, pilotes système, disques HDD et SSD SATA
**Rôle :** Standard d'interface matérielle Intel spécifiant le comportement du contrôleur SATA pour exposer les fonctionnalités avancées des disques (Native Command Queuing, hot-plug) au système d'exploitation.
**Syntaxe :** (paramètre BIOS/UEFI : Storage Configuration → SATA Mode → AHCI)
**Cas réguliers :**
- `Activation AHCI avant installation OS` — Configuration du BIOS en mode AHCI pour bénéficier du NCQ (Native Command Queuing) et des pilotes optimaux
- `Branchement à chaud de disque SATA` — Insertion d'un disque SATA sans éteindre le serveur grâce au support hot-plug AHCI
**Origine :** Défini par Intel et un consortium d'entreprises du secteur du stockage en 2004 pour remplacer le mode IDE/PATA.
**Subtilités/confusions :**
- Le mode AHCI doit absolument être activé dans le BIOS avant l'installation du système d'exploitation — le changer après coup entraîne un BSOD ou un kernel panic au démarrage.
- AHCI a été conçu pour les disques rotatifs mécaniques et s'avère un goulot d'étranglement pour les SSD NVMe dont les performances transcendent ses capacités.
**Urgences/dangers :** ⚠️ Passer de IDE à AHCI après installation de Windows provoque un écran bleu INACCESSIBLE_BOOT_DEVICE sans préparation préalable.
**Précautions :** Pour les SSD modernes, migrer vers le mode NVMe/PCIe natif (protocole NVMe) qui offre des files d'attente et des performances considérablement supérieures à AHCI.
**Équivalents :** NVMe (protocole supérieur), IDE (protocole obsolète)
**Voir aussi :** SATA, NVMe, SSD, HDD, BIOS

## `SAS` — Serial Attached SCSI [Stockage]
**Niveau :** avance | **Popularité :** 77 | **Aliases :** Serial SCSI, SAS-3
**Contextes :** serveurs entreprise, baies de stockage, SAN, RAID matériel haute disponibilité
**Rôle :** Technologie de connexion série point-à-point pour disques durs et SSD d'entreprise, offrant double attachement (Dual-Port), fiabilité accrue et support de baies d'extension via SAS Expander.
**Syntaxe :** `lsscsi -t` ou `sg_map -x`
**Cas réguliers :**
- `Disque SAS dual-port en cluster HA` — Connexion redondante d'un disque à deux contrôleurs SAS pour zéro SPOF (Single Point of Failure)
- `Chaîne de baies via SAS Expander` — Extension d'un contrôleur SAS à 100+ disques via des modules d'expansion SAS en cascade
**Origine :** Développé au début des années 2000 pour remplacer le bus SCSI parallèle ; standardisé par le T10 SCSI Trade Association.
**Subtilités/confusions :**
- Les disques SAS possèdent des connecteurs avec détrompeur spécifique rendant impossible leur insertion dans un port SATA — mais un port SAS peut physiquement accueillir des disques SATA (compatibilité descendante).
- Les disques SAS entreprise tournant à 10k ou 15k RPM offrent une fiabilité MTBF (Mean Time Between Failures) très supérieure aux disques SATA grand public.
**Urgences/dangers :** —
**Précautions :** Vérifier la compatibilité de la carte contrôleur SAS (HBA ou RAID) avec les disques sélectionnés — la Vendor Compatibility List (VCL) du serveur est la référence.
**Équivalents :** NVMe/SAS (SAS 4 annonce des capacités NVMe), iSCSI (réseau)
**Voir aussi :** SATA, SCSI, SAN, RAID, AHCI

## `DisplayPort` — DisplayPort Video Interface [Matériel]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** DP, Mini-DP, VESA DP
**Contextes :** connexion moniteur PC, multi-écrans professionnels, stations de travail, gaming haute fréquence
**Rôle :** Interface numérique vidéo et audio haute performance conçue par la VESA permettant la transmission de signaux vidéo jusqu'à 8K et de l'audio, avec support du MST (daisy-chaining de moniteurs).
**Syntaxe :** (commandes : `xrandr --query` ou `wlr-randr` sous Wayland)
**Cas réguliers :**
- `Affichage 4K 144Hz via DP 2.1` — Connexion d'un moniteur gaming ultra-haute résolution en fréquence de rafraîchissement maximale
- `Daisy-Chaining MST multi-moniteurs` — Chaînage de deux ou trois écrans sur un seul port DisplayPort via Multi-Stream Transport
**Origine :** Créé par la VESA en 2006 pour remplacer les interfaces analogiques DVI et VGA ; standard ouvert sans redevances.
**Subtilités/confusions :**
- Contrairement au HDMI soumis à des redevances de licence, DisplayPort est un standard complètement ouvert développé par la VESA.
- DisplayPort et USB-C/Thunderbolt partagent parfois le même connecteur physique (Alternate Mode) — mais ce sont des protocoles distincts nécessitant des câbles adaptés.
**Urgences/dangers :** —
**Précautions :** Vérifier la version DP (1.4, 2.0, 2.1) supportée par le GPU et le moniteur pour garantir la bande passante nécessaire à la résolution et fréquence cibles.
**Équivalents :** HDMI (grand public/TV), Thunderbolt (multifonction haut de gamme)
**Voir aussi :** HDMI, Thunderbolt, GPU, VESA, xrandr

## `Thunderbolt` — Thunderbolt Hardware Interface [Matériel]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** TB4, Light Peak, Intel Thunderbolt
**Contextes :** stations d'accueil (docks), eGPU, transferts de données ultra-rapides, connexion multi-écrans 8K
**Rôle :** Interface de connexion haut débit combinant PCIe, DisplayPort et alimentation USB-C Power Delivery sur un seul connecteur USB-C pour des transferts jusqu'à 120 Gbps (TB5).
**Syntaxe :** `boltctl list` (Linux) ou `system_profiler SPThunderboltDataType` (macOS)
**Cas réguliers :**
- `Station d'accueil Thunderbolt 4` — Connexion d'un laptop via un seul câble USB-C fournissant réseau, écrans, périphériques et charge 100W
- `eGPU (GPU externe) via Thunderbolt 3+` — Tunneling de 4 lignes PCIe 3.0 pour alimenter une carte graphique externe portable
**Origine :** Développé par Intel sous le nom de code Light Peak depuis 2009, lancé commercialement avec les MacBook Pro 2011 (Apple/Intel).
**Subtilités/confusions :**
- Tous les ports USB-C ne supportent pas Thunderbolt : vérifier la présence du logo ⚡ ou TB sur le port — l'absence de ce logo signifie USB-C simple ou USB4.
- Thunderbolt autorise le DMA (Direct Memory Access) depuis les périphériques connectés — une menace sécuritaire (Thunderspy attack) nécessitant IOMMU/Kernel DMA Protection.
**Urgences/dangers :** ⚠️ L'attaque Thunderspy permet un accès direct à la RAM du système via DMA en contournant le chiffrement disque (Bitlocker/FileVault) sur les machines en veille.
**Précautions :** Activer Kernel DMA Protection (Intel) dans le BIOS et désactiver l'autorisation automatique de nouveaux appareils Thunderbolt dans les paramètres système.
**Équivalents :** USB4 (version ouverte très similaire à TB3), DisplayPort Alt Mode (vidéo seule)
**Voir aussi :** USB, PCIe, DisplayPort, Type-C, eGPU

## `RJ45` — Registered Jack 45 [Réseau]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** 8P8C, Connecteur Ethernet, RJ-45
**Contextes :** câblage réseau Ethernet, infrastructure informatique, connexion de postes, baie de brassage
**Rôle :** Connecteur physique standardisé à 8 contacts (8P8C) utilisé universellement pour le câblage réseau Ethernet cuivre des catégories Cat5e à Cat8.
**Syntaxe :** (outil : pince à sertir + câble Cat6A ; vérificateur de câbles réseau)
**Cas réguliers :**
- `Sertissage de câble Cat6A selon T568B` — Raccordement des 8 fils cuivre dans l'ordre normalisé orange/blanc-orange/vert/blanc-bleu/bleu/blanc-vert/marron/blanc-marron
- `Patch panel et baie de brassage` — Connexion et organisation des prises RJ45 provenant des postes de travail vers les équipements actifs (switch, routeur)
**Origine :** Standardisé à l'origine par la FCC (Federal Communications Commission) pour la téléphonie cuivre avant d'être repris pour l'Ethernet par l'IEEE.
**Subtilités/confusions :**
- Le terme exact est "connecteur 8P8C" (8 positions, 8 contacts) — RJ45 désigne à l'origine un standard téléphonique de l'interface physique mais le terme s'est imposé dans l'usage pour Ethernet.
- La catégorie du câble (Cat5e, Cat6, Cat6A, Cat7, Cat8) détermine les débits et distances maximaux supportés — un câble Cat5e limite à 1 Gbps, Cat6A permet 10 Gbps jusqu'à 100m.
**Urgences/dangers :** —
**Précautions :** Respecter la longueur maximale de 100 m par segment de câble Ethernet cuivre (UTP/STP) et vérifier l'impédance du câble avec un testeur avant installation.
**Équivalents :** SFP (fibre optique), DAC (câble cuivre direct), SFP28
**Voir aussi :** Ethernet, Cat6, Switch, SFP, PoE

## `SFP` — Small Form-factor Pluggable [Réseau]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** Transceiver SFP, SFP+, SFP28, QSFP
**Contextes :** commutateurs réseau entreprise, interconnexions datacenter, liaison fibre optique, uplinks réseau
**Rôle :** Module transcepteur optique ou cuivre compact échangeable à chaud permettant de sélectionner le type de liaison physique (fibre monomode, multimode, cuivre DAC) selon le besoin.
**Syntaxe :** `ethtool eth1 | grep Speed` ou `ip link show sfp0`
**Cas réguliers :**
- `Lien inter-switch 10 GbE via SFP+` — Insertion de deux modules SFP+ Monomode LC dans les ports uplink et connexion par fibre optique LC-LC
- `Interconnexion serveur haute vitesse via DAC` — Câble cuivre Direct Attach (DAC) SFP28 25 GbE pour courte distance sans convertisseur optique
**Origine :** Défini par le groupe SFF (Small Form Factor Committee) via des accords MSA (Multi-Source Agreement) pour garantir l'interopérabilité multi-constructeurs.
**Subtilités/confusions :**
- Il existe plusieurs générations : SFP (1 Gbps), SFP+ (10 Gbps), SFP28 (25 Gbps), QSFP28 (100 Gbps), QSFP112 (400 Gbps) — non interchangeables mécaniquement pour les formats QSFP.
- Certains constructeurs (Cisco notamment) bloquent les modules SFP tiers non officiels via un encodage d'EEPROM propriétaire, causant des erreurs "Unsupported transceiver".
**Urgences/dangers :** ⚠️ Ne jamais regarder directement dans un module SFP optique actif — le faisceau laser est invisible à l'œil nu et peut causer des lésions oculaires permanentes.
**Précautions :** Toujours insérer le bouchon plastique de protection dans les ports SFP non utilisés pour éviter la poussière sur les connecteurs optiques.
**Équivalents :** RJ45 (cuivre courte distance), QSFP (très haut débit)
**Voir aussi :** Ethernet, RJ45, Switch, Fibre Optique, QSFP

## `PoE` — Power over Ethernet [Réseau]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** IEEE 802.3af, PoE+, PoE++
**Contextes :** déploiement de bornes Wi-Fi, caméras IP, téléphonie VoIP, contrôle d'accès, affichage dynamique
**Rôle :** Technologie standardisée IEEE permettant d'alimenter électriquement un équipement réseau (PD) directement via son câble Ethernet RJ45 en provenance d'un switch PoE (PSE).
**Syntaxe :** (vérification : `lldptool -t -i eth0 -V poed` ou console switch PoE)
**Cas réguliers :**
- `Alimentation de borne Wi-Fi PoE+` — Fourniture de 30W IEEE 802.3at sur le câble Cat6 d'une borne tri-bande d'entreprise
- `Caméra IP PoE sans alimentation dédiée` — Installation simplifiée d'une caméra de surveillance avec un seul câble réseau portant données + alimentation
**Origine :** Premier standard IEEE 802.3af publié en 2003 (15.4W) ; évolué en 802.3at PoE+ (30W en 2009) puis 802.3bt PoE++ (60/90W en 2018).
**Subtilités/confusions :**
- Le PSE (switch PoE) et le PD (équipement alimenté) négocient leur puissance via LLDP ou IEEE classification avant d'envoyer la tension — un équipement non-PoE n'est jamais endommagé par un port PoE.
- Le PoE++ 802.3bt Type 4 peut fournir jusqu'à 90W, suffisant pour alimenter des écrans tactiles, des mini-PC ou des caméras PTZ motorisées.
**Urgences/dangers :** —
**Précautions :** Calculer la puissance totale consommée par tous les équipements PoE avant de dimensionner le switch — le budget PoE total du switch est limité (ex: 370W pour 24 ports).
**Équivalents :** Alimentation dédiée AC (alternative non PoE)
**Voir aussi :** Ethernet, RJ45, Switch, WLAN, IEEE 802.3

## `UPS` — Uninterruptible Power Supply [Infrastructure IT]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** Onduleur, Alimentation Sans Interruption, ASI
**Contextes :** protection des serveurs, salle de datacenter, protection de postes de travail critiques, continuité de service
**Rôle :** Équipement électrique fournissant une alimentation de secours par batterie interne en cas de coupure secteur, filtrant les microcoupures et les surtensions pour protéger les équipements.
**Syntaxe :** `upsc ups@localhost` (Network UPS Tools) ou `apcaccess status` (apcupsd)
**Cas réguliers :**
- `Basculement automatique sur batterie` — Maintien de l'alimentation de la baie serveur pendant une coupure de 10 minutes pour permettre l'arrêt propre
- `Arrêt propre automatisé via NUT/apcupsd` — Envoi d'un signal d'arrêt SSH/SNMP aux serveurs quand la charge batterie descend sous 20%
**Origine :** Développé dans les années 1960 avec l'émergence des premiers grands calculateurs centraux ; commercialisé sous forme d'unité rackable depuis les années 1980.
**Subtilités/confusions :**
- Différence technique entre UPS Off-line (bascule en quelques millisecondes — économique mais avec bref délai), Line-Interactive (filtre les surtensions en temps réel) et On-line Double Conversion (isolation complète du réseau électrique en permanence — le plus fiable).
- Un UPS n'est pas un groupe électrogène — il fournit l'autonomie (généralement 5 à 30 minutes) nécessaire pour démarrer le groupe électrogène ou effectuer un arrêt propre.
**Urgences/dangers :** ⚠️ Les batteries de plomb d'un UPS vieillissent et peuvent tomber en défaut sans signe apparent — les tester régulièrement et les remplacer tous les 3 à 5 ans.
**Précautions :** Configurer NUT (Network UPS Tools) sur tous les serveurs reliés à l'UPS pour un arrêt automatique et coordonné en cas de panne secteur prolongée.
**Équivalents :** PDU (distribue le courant), Groupe Électrogène (autonomie longue durée)
**Voir aussi :** PDU, SNMP, Rack 19, Datacenter, NUT

## `KVM` — Keyboard Video Mouse [Infrastructure IT]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** KVM Switch, Console Switch, KVM over IP
**Contextes :** administration de salle serveur, gestion de baies multi-serveurs, accès console hors-bande
**Rôle :** Commutateur physique ou protocole réseau permettant de contrôler plusieurs ordinateurs ou serveurs distincts depuis un seul jeu de périphériques (clavier, écran, souris).
**Syntaxe :** (accès via : `ipmitool -I lanplus -H idrac-ip sol activate` ou interface web KVM over IP)
**Cas réguliers :**
- `Gestion console de 16 serveurs en baie` — Bascule de l'affichage et du clavier d'un serveur à l'autre via un commutateur KVM rackable 16 ports 1U
- `KVM over IP (hors bande)` — Accès à la console vidéo BIOS/POST d'un serveur distant même si l'OS est planté ou en cours d'installation
**Origine :** Apparu dans les années 1980 dans les salles de serveurs pour économiser l'espace, l'énergie et le budget moniteurs/claviers.
**Subtilités/confusions :**
- Ne pas confondre le KVM matériel Keyboard-Video-Mouse (commutateur de console) avec le KVM logiciel Kernel-based Virtual Machine (hyperviseur Linux de virtualisation).
- Le KVM over IP fonctionne indépendamment de l'état du système d'exploitation hôte — c'est un accès console matériel via IPMI/iDRAC/iLO.
**Urgences/dangers :** —
**Précautions :** Sécuriser l'accès au KVM over IP sur un VLAN d'administration dédié et isolé, inaccessible depuis le réseau de production.
**Équivalents :** iDRAC/iLO (intégré aux serveurs Dell/HPE), IPMI BMC
**Voir aussi :** iDRAC, ILO, IPMI, Rack 19, SSH

## `PDU` — Power Distribution Unit [Infrastructure IT]
**Niveau :** intermediaire | **Popularité :** 79 | **Aliases :** Bandeau de prises, Répartiteur d'Alimentation
**Contextes :** baie informatique 19 pouces, salle serveur, datacenter, gestion de l'énergie
**Rôle :** Bandeau de distribution électrique rackable fournissant plusieurs prises secteur normalisées aux équipements montés en baie, avec en option mesure de consommation et commande à distance.
**Syntaxe :** (console web PDU ; `snmpwalk -v2c -c public pdu-ip .1.3.6.1.4.1.318`)
**Cas réguliers :**
- `Mesure de consommation par prise (PDU Metered)` — Lecture en temps réel de la consommation en Watts/Ampères de chaque serveur via SNMP
- `Redémarrage à distance d'un serveur (PDU Switched)` — Cycle d'alimentation (power cycle) d'une prise commandable depuis la console de supervision
**Origine :** Conçu pour répondre aux contraintes de haute densité et de gestion granulaire d'énergie des centres de données modernes.
**Subtilités/confusions :**
- PDU basique (distribution simple sans mesure), PDU Metered (mesure de la consommation), PDU Switched (commande individuelle des prises) et PDU Switched+Metered (les deux) — des niveaux de fonctionnalité très différents.
- Les PDU datacenter utilisent souvent des connecteurs verrouillables C13/C19 (IEC 60320) pour éviter tout débranchement accidentel.
**Urgences/dangers :** ⚠️ Calculer précisément la charge électrique totale avant de brancher des équipements — dépasser la capacité du PDU risque de déclencher le disjoncteur de la baie, coupant tout le rack.
**Précautions :** Répartir les équipements critiques sur deux PDU distincts alimentés par deux circuits électriques indépendants pour la redondance d'alimentation.
**Équivalents :** UPS (protection batterie), Multiprise industrielle
**Voir aussi :** UPS, Rack 19, SNMP, Datacenter, C13/C19

## `Rack 19` — 19-inch Server Rack [Infrastructure IT]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** Baie 19 pouces, EIA-310, Armoire Réseau
**Contextes :** salle serveur, datacenter, local technique, hébergement d'équipements actifs (serveurs, switches, firewalls)
**Rôle :** Structure métallique normalisée EIA-310 permettant de monter et d'organiser des équipements informatiques et réseau de largeur standard 19 pouces (48,26 cm) en unités U empilables.
**Syntaxe :** (dimensionnement : 1U = 44.45 mm de hauteur ; baie standard = 42U)
**Cas réguliers :**
- `Montage d'un serveur 2U en baie` — Vissage d'un serveur sur les rails coulissants de la baie pour faciliter l'intervention future
- `Gestion du flux thermique` — Installation de panneaux obturateurs 1U dans les emplacements libres pour prévenir le recyclage d'air chaud entre les équipements
**Origine :** Standardisé par l'EIA (Electronic Industries Alliance) sous la norme EIA-310 dans les années 1960.
**Subtilités/confusions :**
- Une Unité Rack (1U) mesure exactement 44.45 mm (1.75 pouces) de hauteur — une baie standard de 42U fait donc environ 1.87 m de hauteur utile.
- La largeur standard de 19 pouces désigne l'espacement entre les montants du rack, pas la largeur totale du bâti.
**Urgences/dangers :** ⚠️ Une baie mal lestée ou mal fixée au sol peut basculer lors de travaux — toujours travailler de bas en haut pour les équipements lourds et ancrer la baie au sol.
**Précautions :** Documenter précisément chaque emplacement (slot diagram) de la baie et gérer les câbles avec des guides et attaches pour faciliter les interventions futures.
**Équivalents :** Baie ouverte (Open Frame Rack), Armoire fermée à serrure
**Voir aussi :** PDU, UPS, Blade Server, Datacenter, EIA-310

## `Blade Server` — Blade Server Architecture [Infrastructure IT]
**Niveau :** avance | **Popularité :** 79 | **Aliases :** Serveur Lame, Blade Computing
**Contextes :** datacenter haute densité, hébergement d'entreprise, virtualisation à grande échelle
**Rôle :** Serveur modulaire ultra-compact (lame) conçu pour s'insérer dans un châssis partagé (blade enclosure) qui mutualise l'alimentation, le refroidissement, les switchs réseau et la gestion.
**Syntaxe :** (console de gestion : Onboard Administrator HPE, Dell CMC/OME-M, Cisco UCS Manager)
**Cas réguliers :**
- `Déploiement haute densité (20 serveurs en 10U)` — Insertion de 20 lames de calcul dans un châssis HPE Synergy ou Dell PowerEdge MX occupant 10U de baie
- `Mise à jour de firmware centralisée` — Mise à jour simultanée du BIOS et des drivers de toutes les lames depuis la console de gestion du châssis
**Origine :** Pionnérisé par RLX Technologies en 2001 ; popularisé ensuite par HP BladeSystem et IBM BladeCenter dans les datacenters des années 2000-2010.
**Subtilités/confusions :**
- Les serveurs lame dépendent entièrement du châssis pour l'alimentation, le réseau et le refroidissement — la panne du châssis entraîne la panne de toutes les lames simultanément.
- Le coût initial d'un infrastructure blade est élevé (châssis + lames), mais la densité, la gestion centralisée et la consommation mutualisée justifient l'investissement à grande échelle.
**Urgences/dangers :** ⚠️ Le châssis blade représente un Single Point of Failure majeur si l'alimentation et les switchs réseau intégrés ne sont pas redondants.
**Précautions :** Configurer obligatoirement les modules d'alimentation et switchs en double exemplaire redondant dans le châssis blade pour garantir la haute disponibilité.
**Équivalents :** Rack Server (serveur 1U/2U classique), Hyperconverged Infrastructure (HCI)
**Voir aussi :** Rack 19, Bare Metal, Hypervisor, Datacenter

## `Bare Metal` — Bare Metal Server [Cloud / Infrastructure]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** Serveur Dédié, Physical Server, Dedicated Host
**Contextes :** cloud computing haute performance, bases de données enterprise, HPC, charges de travail nécessitant l'accès direct au matériel
**Rôle :** Serveur physique dédié à un unique client, sans aucune couche de virtualisation intermédiaire, fournissant l'intégralité des ressources matérielles avec des performances prévisibles.
**Syntaxe :** (provisionnement API cloud : `openstack baremetal node list` / IBM Cloud Bare Metal)
**Cas réguliers :**
- `Serveur Bare Metal Cloud provisionné en 5 min` — Allocation automatisée via API d'une machine physique complète sans partage de ressources
- `Oracle Database sur Bare Metal` — Exécution directe du moteur de BDD sur le matériel pour zéro surcoût d'hyperviseur et performances maximales
**Origine :** Terme réémergé dans le vocabulaire cloud pour distinguer les serveurs physiques dédiés des instances de machines virtuelles (VMs) partagées.
**Subtilités/confusions :**
- Bare Metal s'oppose aux instances virtuelles (VMs) qui partagent le matériel avec d'autres clients — il offre des performances matérielles brutes sans bruit de voisinage (noisy neighbor effect).
- Le provisionnement Bare Metal Cloud peut durer quelques minutes avec des outils comme Ironic (OpenStack) — plus long qu'une VM mais proche d'un serveur dédié classique.
**Urgences/dangers :** —
**Précautions :** Planifier soigneusement les besoins avant provisionnement — redimensionner un Bare Metal est bien plus contraignant que de modifier une VM cloud.
**Équivalents :** VM (instance virtuelle mutualisée), Dedicated Host (équivalent AWS)
**Voir aussi :** Hypervisor, VM, IaaS, Cloud, OpenStack

## `Hypervisor` — Hypervisor / Hyperviseur [Virtualisation]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** VMM, Virtual Machine Monitor, Superviseur de Machines Virtuelles
**Contextes :** virtualisation de serveurs, cloud computing, développement et test, isolation de charges de travail
**Rôle :** Logiciel ou micrologiciel qui crée et gère des machines virtuelles (VMs) en abstrayant et en partageant le matériel physique (CPU, RAM, Réseau, Stockage) entre plusieurs OS invités isolés.
**Syntaxe :** `virsh list --all` (KVM/libvirt) ou `esxcli vm process list` (VMware ESXi)
**Cas réguliers :**
- `Déploiement d'hyperviseur Type 1 sur serveur nu` — Installation de Proxmox VE ou VMware ESXi directement sur un serveur physique vierge
- `Exécution d'une VM Linux sous VirtualBox` — Lancement d'un OS invité dans une fenêtre de l'OS hôte Windows ou macOS (Type 2)
**Origine :** Concept développé par IBM dans les années 1960 pour ses mainframes CP-40 et System/360 ; généralisé à l'architecture x86 par VMware en 2001.
**Subtilités/confusions :**
- Différence fondamentale entre Type 1 Bare-Metal (s'exécute directement sur le matériel physique : VMware ESXi, Proxmox, Hyper-V) et Type 2 Hosted (tourne comme un processus dans un OS hôte : VirtualBox, VMware Workstation).
- L'hyperviseur exploite les instructions d'assistance matérielle des processeurs Intel VT-x et AMD-V pour garantir l'isolation sécurisée des VMs.
**Urgences/dangers :** ⚠️ Une faille d'évasion de VM (VM Escape) permet à un code malveillant dans une VM de compromettre l'hyperviseur et l'ensemble de l'hôte physique.
**Précautions :** Maintenir rigoureusement l'hyperviseur à jour avec les correctifs de sécurité — les vulnérabilités d'évasion VM sont des vecteurs d'attaque critiques.
**Équivalents :** Container Runtime (Docker/LXC — isolation légère sans VM complète), Unikernel
**Voir aussi :** VM, Bare Metal, KVM, Proxmox, vCPU

## `vCPU` — Virtual Central Processing Unit [Virtualisation]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** CPU Virtuel, Virtual Core
**Contextes :** hyperviseur, cloud computing, dimensionnement de machines virtuelles, conteneurs
**Rôle :** Unité de traitement logique assignée par un hyperviseur à une machine virtuelle, correspondant généralement à un thread d'exécution (core logique) du processeur physique hôte.
**Syntaxe :** `virsh vcpuinfo <vm-name>` ou interface cloud (AWS, GCP, Azure instance types)
**Cas réguliers :**
- `Allocation de 4 vCPU à une VM applicative` — Attribution de 4 threads logiques à une VM web sur un hôte physique disposant de 64 cœurs logiques
- `Calcul de ratio d'over-commitment vCPU` — Configuration d'un ratio 3:1 (3 vCPU alloués pour 1 cœur physique) pour maximiser la densité de VMs
**Origine :** Concept indissociable des hyperviseurs modernes VMware, Xen, KVM — émergé avec la virtualisation x86 généralisée au début des années 2000.
**Subtilités/confusions :**
- Un vCPU correspond à un thread d'exécution logique de l'hôte, pas nécessairement à un cœur physique complet — l'Hyper-Threading fournit 2 threads par cœur physique.
- Un sur-engagement excessif de vCPU (CPU Overcommit) entraîne du CPU Steal Time et CPU Ready — du temps d'attente de la VM pour obtenir du temps CPU réel, dégradant les performances.
**Urgences/dangers :** ⚠️ Un ratio vCPU/pCPU trop élevé provoque une dégradation des performances difficile à diagnostiquer — surveiller le CPU Ready/CPU Steal via les métriques de l'hyperviseur.
**Précautions :** Monitorer le CPU Ready (VMware) ou CPU Steal (`top` colonne `st` sous Linux) pour détecter la saturation en ressources CPU de l'hôte physique.
**Équivalents :** vCore (terminologie alternative), CPU limit (conteneurs Kubernetes)
**Voir aussi :** Hypervisor, CPU, VM, Cloud, Bare Metal

## `SNMP` — Simple Network Management Protocol [Supervision]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** SNMPv3, RFC 3411, Network Management Protocol
**Contextes :** supervision réseau, monitoring d'infrastructure IT, gestion d'équipements (switches, routeurs, UPS, PDU)
**Rôle :** Protocole standard de supervision permettant de collecter des métriques et de recevoir des alertes (Traps) depuis les équipements réseau et serveurs via une structure d'informations hiérarchique (MIB).
**Syntaxe :** `snmpget -v3 -u user -l authPriv -a SHA -x AES -A pass -X pass host OID` ou `snmpwalk -v2c -c public host`
**Cas réguliers :**
- `Collecte de métriques d'interface réseau` — Lecture des compteurs d'octets entrants/sortants et de la charge d'interface d'un switch via SNMP Get
- `Réception d'alerte SNMP Trap` — Réception instantanée d'une notification d'interruption de lien (Link Down) sur le serveur de supervision Zabbix/Nagios
**Origine :** Développé par l'IETF en 1988 (RFC 1157 SNMPv1) ; version sécurisée SNMPv3 standardisée dans la RFC 3411.
**Subtilités/confusions :**
- SNMPv1 et v2c transmettent les community strings (mots de passe) en clair dans les trames réseau — SNMPv3 est le seul à fournir authentification (SHA) et chiffrement (AES) corrects.
- Les MIB (Management Information Base) définissent l'arborescence des OID (Object Identifiers) par équipement — chaque constructeur peut avoir des MIB propriétaires à importer dans l'outil de supervision.
**Urgences/dangers :** ⚠️ Laisser la community string "public" par défaut accessible depuis Internet expose l'intégralité des informations de configuration et de topologie réseau à tout attaquant.
**Précautions :** Toujours utiliser SNMPv3 avec authentification et chiffrement ; filtrer l'accès SNMP aux seules adresses IP des serveurs de supervision via ACL et VLAN de gestion dédié.
**Équivalents :** Prometheus/OpenMetrics (pull HTTP moderne), gNMI/gRPC (réseau nouvelle génération)
**Voir aussi :** MIB, Zabbix, Nagios, SIEM, Syslog

## `Syslog` — System Logging Protocol [Supervision]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** RFC 5424, rsyslog, syslog-ng
**Contextes :** centralisation de journaux, SIEM, supervision de sécurité, audit de conformité, débogage d'infrastructure
**Rôle :** Standard de protocole et de formatage pour l'envoi, la réception et le stockage centralisé des journaux d'événements système générés par les équipements réseau et serveurs.
**Syntaxe :** `logger -p local0.info "test message"` ou `rsyslogd -n` ; réception sur port UDP/TCP 514
**Cas réguliers :**
- `Centralisation de logs Linux vers serveur rsyslog` — Configuration de `/etc/rsyslog.conf` pour envoyer tous les messages système vers un serveur central
- `Filtrage par niveau de sévérité` — Tri des événements de Emergency (sévérité 0) à Debug (sévérité 7) pour alerter sur les niveaux Critical et supérieurs
**Origine :** Développé à l'origine par Eric Allman pour le logiciel Sendmail dans les années 1980 ; formalisé dans la RFC 3164 puis modernisé dans la RFC 5424.
**Subtilités/confusions :**
- Les messages Syslog UDP (port 514) sont transmis sans accusé de réception ni chiffrement — utiliser TCP + TLS (RFC 5425) pour les environnements nécessitant l'intégrité et la confidentialité des logs.
- Chaque message Syslog comporte un code Facility (indiquant l'origine : kernel, mail, auth, daemon…) et une Severity (gravité de 0 à 7) encodés ensemble dans un champ Priority.
**Urgences/dangers :** ⚠️ Un attaquant ayant compromis un système peut effacer les logs locaux — la centralisation Syslog vers un serveur distant protégé est essentielle pour la forensique.
**Précautions :** Stocker les logs centralisés sur un système en écriture seule (WORM) ou un SIEM pour garantir leur intégrité légale (chaîne de custody pour les investigations).
**Équivalents :** Journald (systemd, format binaire), Windows Event Log (équivalent Microsoft)
**Voir aussi :** SIEM, rsyslog, journalctl, SNMP, Logs

## `PXE` — Preboot Execution Environment [Infrastructure IT]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** Network Boot, iPXE, Network Install
**Contextes :** déploiement automatisé de serveurs, clients légers diskless, provisionnement de datacenter, boot réseau
**Rôle :** Environnement standardisé permettant à un ordinateur de démarrer et d'installer un système d'exploitation en réseau via sa carte réseau, sans avoir besoin de support physique (DVD/USB).
**Syntaxe :** (configuration BIOS/UEFI : Boot Device → Network/PXE ; serveur : `dnsmasq` + TFTP + iPXE)
**Cas réguliers :**
- `Déploiement automatisé de 50 serveurs` — Démarrage PXE de 50 machines vierges qui reçoivent leur OS et configuration via kickstart/preseed depuis le réseau
- `Client léger Diskless` — Poste sans disque chargeant l'intégralité de son OS en RAM via NFS root après boot PXE
**Origine :** Spécification développée par Intel et Microsoft en 1999 dans le cadre de l'initiative Wired for Management (WfM).
**Subtilités/confusions :**
- PXE s'appuie sur DHCP (option 66/67 pour l'adresse du serveur TFTP et le nom du fichier bootloader) et TFTP (port 69 UDP) pour charger le premier fichier amorce — ce sont deux services réseau distincts à configurer.
- En environnement UEFI moderne, le bootloader PXE téléchargé est grub2-efi ou shim.efi et non plus pxelinux.0 (BIOS legacy).
**Urgences/dangers :** ⚠️ Un serveur DHCP/TFTP malveillant sur le réseau peut proposer un bootloader piégé et compromettre toutes les machines qui démarrent en PXE.
**Précautions :** Activer UEFI Secure Boot et valider les certificats des fichiers bootloader PXE pour empêcher le boot d'images non signées provenant d'un serveur compromis.
**Équivalents :** USB Live (alternative hors réseau), Cobbler/Foreman (outils de provisionnement PXE)
**Voir aussi :** DHCP, TFTP, UEFI, Kickstart, Preseed

## `IPMI` — Intelligent Platform Management Interface [Infrastructure IT]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** BMC, Baseboard Management Controller, Out-of-Band Management
**Contextes :** supervision matériel hors-bande, administration de serveurs, gestion d'infrastructure datacenter
**Rôle :** Interface standardisée de gestion hors-bande permettant de surveiller et contrôler un serveur (température, tensions, alimentation, console) indépendamment de l'état de son système d'exploitation.
**Syntaxe :** `ipmitool -I lanplus -H bmc-ip -U admin -P pass chassis status` ou `ipmitool sensor list`
**Cas réguliers :**
- `Mise sous tension à distance d'un serveur éteint` — `ipmitool chassis power on` sans avoir à accéder physiquement au datacenter
- `Lecture des sondes de température et tensions` — Surveillance des capteurs matériels (CPU temp, fan speed, voltages) indépendamment de l'OS
**Origine :** Spécification co-développée par Intel, Dell, HP et NEC ; version IPMI 2.0 publiée en 2004, précurseur de Redfish.
**Subtilités/confusions :**
- IPMI s'exécute sur le BMC (Baseboard Management Controller), une puce autonome présente sur la carte mère et alimentée dès que le câble secteur est branché — indépendante du CPU principal.
- Le protocole IPMI 1.5/2.0 expose des vulnérabilités connues (authentification faible, cipher 0, UDP 623) — son accès doit être strictement isolé sur un réseau d'administration dédié.
**Urgences/dangers :** ⚠️ IPMI expose un accès complet au matériel physique — une interface IPMI accessible depuis Internet constitue une faille critique permettant la prise de contrôle totale du serveur.
**Précautions :** Isoler le port IPMI/BMC sur un VLAN d'administration totalement séparé, non routable depuis Internet ; désactiver les ciphers IPMI faibles et utiliser Redfish en remplacement.
**Équivalents :** Redfish (successeur API REST moderne), iDRAC (Dell), iLO (HPE)
**Voir aussi :** iDRAC, ILO, KVM, Syslog, SNMP

## `iDRAC` — Integrated Dell Remote Access Controller [Hardware / Administration]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** Dell iDRAC, iDRAC9
**Contextes :** administration de serveurs Dell PowerEdge, gestion hors-bande, maintenance datacenter
**Rôle :** Carte de gestion matérielle autonome intégrée aux serveurs Dell permettant la prise de main à distance, la console KVM HTML5 et le diagnostic matériel sans OS.
**Syntaxe :** (console web dédiée ou `racadm -r <ip> -u <user> -p <pass> <command>`)
**Cas réguliers :**
- `Montage d'ISO virtuel à distance` — Connexion d'un fichier ISO d'installation via l'interface iDRAC pour installer un OS à distance
- `Redémarrage électrique forcé` — Exécution de `racadm serveraction powercycle` en cas de plantage total du noyau
**Origine :** Développé par Dell pour remplacer les anciennes cartes ERA/DRAC sur la gamme PowerEdge.
**Subtilités/confusions :**
- L'iDRAC s'exécute sur son propre processeur ARM indépendant sous tension permanente, avec son propre port Ethernet dédié.
- Certaines fonctionnalités (KVM virtuel multi-utilisateurs, export de profil serveur) nécessitent une licence iDRAC Enterprise.
**Urgences/dangers :** ⚠️ L'iDRAC ne doit jamais être exposé directement sur Internet car il donne le contrôle matériel total du serveur.
**Précautions :** Toujours placer les interfaces iDRAC sur un VLAN d'administration isolé et sécuriser l'accès avec MFA/TLS.
**Équivalents :** ILO (HPE), IPMI, Redfish
**Voir aussi :** ILO, IPMI, KVM, Server

## `ILO` — Integrated Lights-Out [Hardware / Administration]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** HPE iLO, iLO 5, iLO 6
**Contextes :** administration de serveurs HPE ProLiant, gestion matérielle hors-bande, datacenter
**Rôle :** Carte et processeur d'administration à distance intégrés aux serveurs HPE ProLiant offrant l'accès console KVM, le suivi des sondes et l'inventaire matériel.
**Syntaxe :** (interface web iLO ou CLI `hponcfg` sous Linux)
**Cas réguliers :**
- `Mise à jour du firmware BIOS/iLO` — Flashage du firmware du serveur depuis la console iLO sans interruption de l'OS hôte
- `Inspection des journaux IML` — Consultation des journaux d'événements matériels (Integrated Management Log) pour identifier une barrette mémoire défaillante
**Origine :** Développé par Hewlett Packard Enterprise (HPE) à partir de 2002 pour remplacer les cartes RILOE.
**Subtilités/confusions :**
- iLO possède sa propre adresse IP et son port Ethernet physique distinct du système d'exploitation hôte.
- Conforme aux standards IPMI et Redfish pour l'automatisation RESTful.
**Urgences/dangers :** ⚠️ Un accès iLO compromis permet d'éteindre le serveur, d'effacer les disques ou de flasher un firmware malveillant.
**Précautions :** Restreindre l'accès réseau à l'iLO via des ACLs strictes et maintenir son firmware à jour.
**Équivalents :** iDRAC (Dell), IPMI, Redfish
**Voir aussi :** iDRAC, IPMI, KVM, Redfish

## `NAT Gateway` — Network Address Translation Gateway [Cloud / Réseau]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** Cloud NAT, Passerelle NAT
**Contextes :** architectures cloud (AWS, GCP, Azure), VPC, sous-réseaux privés, sécurité des accès sortants
**Rôle :** Service réseau géré dans le cloud permettant aux instances situées dans un sous-réseau privé d'accéder à Internet (mises à jour, APIs) sans recevoir de connexions entrantes.
**Syntaxe :** (Console Cloud / Terraform `aws_nat_gateway` / `google_compute_router_nat`)
**Cas réguliers :**
- `Mise à jour de paquets sur serveur BDD privé` — Les instances BDD privées téléchargent les maj de sécurité via la NAT Gateway sans exposer d'IP publique
- `Attribution d'une IP publique sortante fixe` — Utilisation d'une IP élastique (EIP) fixe sur la NAT Gateway pour le whitelisting auprès de partenaires externes
**Origine :** Service cloud géré introduit par AWS en 2015 pour remplacer les instances EC2 NAT manuelles.
**Subtilités/confusions :**
- La NAT Gateway autorise uniquement le trafic sortant (initié depuis le réseau privé) — aucune connexion initiée depuis Internet ne peut traverser.
- La facturation dépend de la durée de réservation et du volume de gigaoctets transférés.
**Urgences/dangers :** —
**Précautions :** Déployer une NAT Gateway par zone de disponibilité (AZ) pour garantir la haute disponibilité en cas de panne d'une zone.
**Équivalents :** Instance NAT (auto-hébergée), PAT / Masquerade
**Voir aussi :** NAT, VPC, Subnet, Gateway

## `VPC` — Virtual Private Cloud [Cloud / Réseau]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Cloud Private Network, Réseau Virtuel Privé
**Contextes :** cloud computing (AWS, GCP, Azure, OpenStack), isolation de réseau, architecture multi-tiers
**Rôle :** Réseau virtuel isolé logiquement dédié à un compte utilisateur dans un cloud public, permettant de structurer ses ressources en sous-réseaux et règles de sécurité.
**Syntaxe :** (Console Cloud / Terraform `aws_vpc` / `google_compute_network`)
**Cas réguliers :**
- `Architecture Web 3-tiers` — Découpage du VPC en sous-réseau public (Load Balancer), privé (App) et isolé (Database)
- `VPC Peering` — Connexion directe et chiffrée entre deux VPC distincts sans passer par Internet
**Origine :** Concept pionnérisé par Amazon Web Services (AWS VPC) en 2009.
**Subtilités/confusions :**
- Un VPC est un réseau virtuel purement logiciel (SDN) qui isole le trafic entre clients au niveau de l'hyperviseur.
- Ne pas confondre VPC (réseau cloud privé) et VPN (tunnel de connexion sécurisé).
**Urgences/dangers :** —
**Précautions :** Bien planifier la plage CIDR initiale du VPC (ex: 10.0.0.0/16) pour éviter les chevauchements d'adresses lors d'interconnexions futures (VPN/Peering).
**Équivalents :** VNet (Azure Virtual Network), Tenant Network (OpenStack)
**Voir aussi :** Subnet, CIDR, Gateway, VPN

## `CIDR` — Classless Inter-Domain Routing [Réseau]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Notation CIDR, Masque de sous-réseau
**Contextes :** adressage IP, sous-réseaux, routage Internet, configuration VPC/Cloud
**Rôle :** Méthode d'allocation d'adresses IP et de notation de sous-réseaux (ex: `/24`) remplaçant l'ancien système rigide par classes (Class A, B, C).
**Syntaxe :** `ipcalc 192.168.1.0/24` ou `10.0.0.0/16`
**Cas réguliers :**
- `Notation 192.168.1.0/24` — Représente un bloc de 256 adresses IP avec un masque de 24 bits (255.255.255.0)
- `Agrégation de routes (Supernetting)` — Regroupement de plusieurs blocs `/24` en un seul bloc `/20` annoncé en BGP
**Origine :** Spécifié par l'IETF en 1993 (RFC 1519) pour freiner l'épuisement des adresses IPv4.
**Subtilités/confusions :**
- Le nombre après le slash (ex: `/28`) indique le nombre de bits fixes de la partie réseau — plus le chiffre est grand, plus le sous-réseau est petit.
- Un bloc IPv4 `/24` offre 254 adresses hôtes exploitables (2 adresses réservées pour réseau et broadcast).
**Urgences/dangers :** —
**Précautions :** Utiliser un outil comme `ipcalc` pour valider les plages d'adresses et éviter les erreurs de chevauchement de sous-réseaux.
**Équivalents :** Subnet Mask (masque décimal traditionnel)
**Voir aussi :** Subnet, IP, BGP, VPC

## `Subnet` — IP Subnetwork [Réseau]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** Sous-réseau, Subnetwork
**Contextes :** architecture réseau, découpage IP, sécurité, VLAN, sous-réseaux cloud
**Rôle :** Division logique d'un réseau IP plus vaste en segments plus petits pour optimiser le routage et améliorer la sécurité.
**Syntaxe :** `ip route show` ou configuration d'interface réseau
**Cas réguliers :**
- `Création d'un sous-réseau DMZ /28` — Isolation de 14 adresses IP pour les serveurs publics
- `Sous-réseau privé Cloud` — Sous-réseau d'un VPC sans route directe vers la passerelle Internet
**Origine :** Défini dans la RFC 950 en 1985 pour réduire les domaines de diffusion (broadcast).
**Subtilités/confusions :**
- Les hôtes d'un même sous-réseau communiquent directement en couche 2 (Ethernet) sans passer par un routeur.
- Pour communiquer entre deux sous-réseaux différents, le trafic doit obligatoirement traverser un routeur ou pare-feu (couche 3).
**Urgences/dangers :** —
**Précautions :** Réserver des adresses IP d'administration fixes en dehors des plages attribuées par le serveur DHCP dans chaque sous-réseau.
**Équivalents :** VLAN (équivalent couche 2)
**Voir aussi :** CIDR, IP, Gateway, VLAN

## `Gateway` — Default Gateway / Passerelle [Réseau]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Passerelle par défaut, Default Route
**Contextes :** configuration IP, routage local, accès Internet, réseau d'entreprise
**Rôle :** Équipement réseau (routeur ou pare-feu) servant de point de sortie pour acheminer les paquets destinés à des réseaux externes.
**Syntaxe :** `ip route add default via 192.168.1.1` ou `route -n`
**Cas réguliers :**
- `Passerelle par défaut 192.168.1.1` — Adresse de la box ou du routeur local vers laquelle tous les paquets non locaux sont envoyés
- `Configuration de route par défaut 0.0.0.0/0` — Règle de routage redirigeant tout le trafic inconnu vers la passerelle
**Origine :** Concept fondamental du modèle TCP/IP présent depuis les premiers réseaux de l'ARPANET.
**Subtilités/confusions :**
- Une machine sans passerelle par défaut configurée ne peut communiquer qu'avec les équipements de son propre sous-réseau local.
- La passerelle effectue la résolution ARP de sa propre adresse MAC pour recevoir les paquets destinés à l'extérieur.
**Urgences/dangers :** ⚠️ Une mauvaise IP de passerelle coupe instantanément tout accès réseau externe et Internet.
**Précautions :** Tester la joignabilité de la passerelle avec `ping <ip-gateway>` lors de tout diagnostic de panne réseau.
**Équivalents :** Default route (0.0.0.0/0)
**Voir aussi :** IP, Router, route, NAT

## `DMZ` — Demilitarized Zone [Sécurité / Réseau]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** Zone Démilitarisée, Perimeter Network
**Contextes :** architecture de sécurité réseau, hébergement de services publics (Web, Mail, DNS), pare-feu
**Rôle :** Sous-réseau physique ou logique isolé contenant les services exposés à Internet, situé entre le réseau externe non sécurisé et le réseau interne de l'entreprise.
**Syntaxe :** (configuration de zones sur pare-feu : WAN / DMZ / LAN)
**Cas réguliers :**
- `Hébergement d'un serveur Web en DMZ` — Si le serveur Web est compromis par un pirate, l'isolation DMZ l'empêche de rebondir vers le LAN interne
- `Filtrage strict DMZ → LAN` — Règle de pare-feu interdisant toute connexion initiée depuis la DMZ vers le réseau interne d'entreprise
**Origine :** Concept adapté du vocabulaire militaire et appliqué à la sécurité informatique au début des années 1990.
**Subtilités/confusions :**
- Le trafic depuis le LAN vers la DMZ est généralement autorisé, mais le trafic initié depuis la DMZ vers le LAN doit être strictement bloqué ou filtré.
- Une "DMZ" sur une box Internet grand public désigne souvent simplement une redirection de tous les ports vers une seule IP (pas une vraie DMZ d'entreprise).
**Urgences/dangers :** —
**Précautions :** Ne jamais stocker de bases de données contenant des données sensibles directement dans des serveurs situés en DMZ.
**Équivalents :** Perimeter Network, Public Subnet (Cloud)
**Voir aussi :** Firewall, LAN, Bastion Host

## `Firewall` — Network Firewall [Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Pare-feu, NGFW, WAF
**Contextes :** sécurité réseau, protection de périmètre, filtrage de paquets, contrôle d'accès
**Rôle :** Dispositif matériel ou logiciel contrôlant et filtrant le trafic réseau entrant et sortant selon des règles de sécurité prédéfinies.
**Syntaxe :** `ufw status` ou `iptables -L -n -v` ou `nft list ruleset`
**Cas réguliers :**
- `Pare-feu à état (Stateful Firewall)` — Autorise automatiquement les réponses entrantes aux connexions légitimement initiées depuis l'intérieur
- `Filtrage applicatif NGFW / WAF` — Inspection du contenu des paquets jusqu'à la couche 7 pour bloquer les attaques applicatives (SQLi, XSS)
**Origine :** Développé à la fin des années 1980 chez DEC et Bell Labs pour protéger les réseaux d'entreprises connectés à ARPANET/Internet.
**Subtilités/confusions :**
- Pare-feu réseau (filtre les flux entre sous-réseaux) vs pare-feu hôte (logiciel comme iptables/UFW/Windows Firewall protégeant une seule machine).
- La règle d'or d'un pare-feu est le "Default Drop" : tout ce qui n'est pas explicitement autorisé est bloqué.
**Urgences/dangers :** ⚠️ Une règle de pare-feu mal configurée (`iptables -P INPUT DROP` sans autoriser SSH) peut vous verrouiller hors d'un serveur distant.
**Précautions :** Toujours tester les règles de pare-feu temporairement avec un script de rollback automatique avant de les rendre permanentes.
**Équivalents :** Security Group (Cloud), ACL
**Voir aussi :** iptables, nftables, ufw, DMZ

## `Proxy` — Proxy Server / Serveur Mandataire [Sécurité / Réseau]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Serveur Mandataire, Forward Proxy, Reverse Proxy
**Contextes :** filtrage web d'entreprise, cache HTTP, anonymisation, répartition de charge, sécurité
**Rôle :** Application ou serveur intermédiaire agissant comme relais entre des clients et des serveurs cibles pour filtrer, mettre en cache ou sécuriser les échanges.
**Syntaxe :** `export http_proxy="http://proxy.example.com:8080"`
**Cas réguliers :**
- `Forward Proxy d'entreprise (Squid)` — Intercepte les requêtes web des salariés pour bloquer les sites malveillants et mettre les contenus en cache
- `Reverse Proxy (Nginx/HAProxy)` — Intercepte le trafic entrant pour répartir la charge sur plusieurs serveurs web et gérer le chiffrement TLS
**Origine :** Développé au début des années 1990 pour économiser la bande passante et contrôler les accès Internet dans les réseaux d'entreprises.
**Subtilités/confusions :**
- Forward Proxy (côté client : protège et filtre les utilisateurs sortants) vs Reverse Proxy (côté serveur : protège et équilibre les serveurs entrants).
- Un proxy transparent intercepte le trafic sans nécessiter de configuration sur le poste client.
**Urgences/dangers :** —
**Précautions :** Pour le déchiffrement HTTPS par un proxy d'inspection (SSL Interception), déployer l'autorité de certification (CA) du proxy sur tous les postes clients.
**Équivalents :** Gateway applicative, Reverse Proxy
**Voir aussi :** Reverse Proxy, Nginx, HAProxy, CDN

## `Bastion Host` — Jump Server / Bastion [Sécurité]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** Jump Box, Jump Server, Serveur Rebond
**Contextes :** administration à distance sécurisée, accès aux serveurs cloud/datacenter, audit SSH
**Rôle :** Serveur fortement durci et surveillé constituant le point d'entrée unique obligatoire pour les administrateurs accédant à un réseau privé.
**Syntaxe :** `ssh -J user@bastion.example.com user@internal-server`
**Cas réguliers :**
- `ProxyJump SSH` — Utilisation de l'option `-J` pour rebondir de manière transparente à travers le bastion vers un serveur interne non exposé
- `Journalisation et audit des sessions` — Enregistrement de toutes les commandes et sessions SSH exécutées à travers le bastion pour la conformité
**Origine :** Formalisé dans la littérature de sécurité Unix des années 1990 comme composant clé des architectures de périmètre.
**Subtilités/confusions :**
- Le bastion doit avoir une surface d'attaque minimale : aucun service inutile, mises à jour automatiques et authentification par clé SSH + MFA obligatoire.
- Un bastion ne doit pas être utilisé comme serveur de stockage ou de build — c'est uniquement une passerelle d'accès.
**Urgences/dangers :** ⚠️ La compromission d'un Bastion Host donne accès à l'ensemble du réseau interne — il doit bénéficier du plus haut niveau de durcissement.
**Précautions :** Désactiver l'authentification par mot de passe au profit de clés SSH protégées et exiger l'authentification multifacteur (MFA).
**Équivalents :** AWS Systems Manager Session Manager (alternative sans bastion), Teleport
**Voir aussi :** SSH, MFA, DMZ, VPC

## `VRRP` — Virtual Router Redundancy Protocol [Réseau]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** RFC 5798, Redondance de Routeur
**Contextes :** haute disponibilité réseau, redondance de passerelle par défaut, basculement automatique
**Rôle :** Protocole réseau permettant à plusieurs routeurs ou pare-feux de partager une adresse IP virtuelle (VIP) pour fournir une passerelle hautement disponible sans interruption.
**Syntaxe :** (Démon Linux `keepalived` : configuration dans `/etc/keepalived/keepalived.conf`)
**Cas réguliers :**
- `Cluster Keepalived Master/Backup` — Deux pare-feux Linux partagent une VIP ; si le Master tombe, le Backup reprend la VIP en moins de 3 secondes
- `Basculement de passerelle par défaut` — Les postes clients gardent la même IP de passerelle sans reconfiguration lors d'une panne matérielle
**Origine :** Spécifié par l'IETF dans la RFC 2338 (v2) puis RFC 5798 (v3) comme standard ouvert.
**Subtilités/confusions :**
- VRRP est un standard IETF ouvert, alors que HSRP (Hot Standby Router Protocol) est un protocole propriétaire Cisco très similaire.
- Seul le routeur Master actif répond aux requêtes ARP pour l'adresse IP virtuelle à un instant donné (via une adresse MAC virtuelle).
**Urgences/dangers :** ⚠️ Si les paquets d'annonces VRRP sont bloqués par un pare-feu entre les deux routeurs, les deux passeront en mode Master (Split-Brain), créant un conflit d'IP.
**Précautions :** Autoriser le protocole IP 112 (VRRP) dans les règles de pare-feu locales entre les membres du cluster.
**Équivalents :** HSRP (Cisco), CARP (BSD/pfSense)
**Voir aussi :** Gateway, Keepalived, HA, IP

## `LACP` — Link Aggregation Control Protocol [Réseau]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** IEEE 802.3ad, IEEE 802.1AX, NIC Bonding
**Contextes :** agrégation de liens Ethernet, haute disponibilité, augmentation de bande passante, switches/serveurs
**Rôle :** Protocole réseau permettant de regrouper plusieurs câbles/interfaces Ethernet physiques en un seul canal logique pour multiplier la bande passante et offrir une tolérance aux pannes.
**Syntaxe :** `ip link add bond0 type bond mode 802.3ad` (Linux)
**Cas réguliers :**
- `Agrégation 4x10 GbE en un canal 40 GbE` — Regroupement de 4 cartes réseau 10 GbE sur un serveur pour obtenir un lien haut débit et redondant
- `Basculement transparent en cas de coupure câble` — Si un câble est débranché, le trafic bascule instantanément sur les autres liens du groupe sans perte de connexion
**Origine :** Standardisé par l'IEEE sous la norme 802.3ad en 2000, révisé sous la norme 802.1AX.
**Subtilités/confusions :**
- LACP nécessite que la configuration soit activée des DEUX côtés de la liaison (sur le serveur ET sur le commutateur réseau).
- La répartition du trafic utilise un algorithme de hachage (ex: IP source/dest + Port) — une seule connexion TCP ne dépassera pas la vitesse d'une seule interface physique.
**Urgences/dangers :** —
**Précautions :** Configurer le mode LACP dynamique (mode 4 / 802.3ad) plutôt qu'un bonding statique pour garantir la négociation d'état entre équipements.
**Équivalents :** EtherChannel (Cisco), Trunking (HP)
**Voir aussi :** Ethernet, Switch, HA, Bonding

## `Spanning Tree` — Spanning Tree Protocol [Réseau]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** STP, RSTP, IEEE 802.1D, IEEE 802.1w
**Contextes :** commutation Ethernet, prévention des boucles réseau, topologie redondante inter-switchs
**Rôle :** Protocole de couche 2 empêchant la formation de boucles de commutation dans les réseaux Ethernet comportant des liaisons redondantes, en bloquant logiquement certains ports.
**Syntaxe :** (Console switch : `spanning-tree mode rstp` ou `mstp`)
**Cas réguliers :**
- `Prévention de tempête de broadcast` — Bloque automatiquement un port redondant entre deux switchs pour éviter que les trames ne tournent en boucle indéfiniment
- `Basculement RSTP en cas de coupure de câble` — Débloque le port de secours en moins d'une seconde si la liaison principale est coupée
**Origine :** Inventé par Radia Perlman chez Digital Equipment Corporation (DEC) en 1985 ; standardisé par l'IEEE 802.1D.
**Subtilités/confusions :**
- Le STP classique (802.1D) mettait 30 à 50 secondes à reconverger ; Rapid STP (RSTP / 802.1w) réduit ce délai à quelques millisecondes.
- Une boucle de commutation sans STP paralyse l'intégralité du réseau local en quelques secondes (saturation CPU des switchs et 100% de bande passante consommée).
**Urgences/dangers :** ⚠️ Désactiver le Spanning Tree sur un switch d'entreprise est une cause majeure de pannes réseau globales dévastatrices.
**Précautions :** Activer BPDU Guard et PortFast sur les ports d'accès reliés aux postes utilisateurs pour éviter les attaques ou l'injection involontaire de switchs grand public.
**Équivalents :** RSTP (Rapid STP), MSTP (Multiple STP)
**Voir aussi :** Switch, Ethernet, VLAN, Loop

## `Jumbo Frames` — Jumbo Ethernet Frames [Réseau]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** Trame Géante, MTU 9000
**Contextes :** réseaux de stockage SAN/NAS (iSCSI, NFS), sauvegarde haut débit, interconnexion datacenter
**Rôle :** Trames Ethernet dont la charge utile (MTU) est supérieure au standard de 1500 octets, atteignant généralement 9000 octets pour réduire le surcoût CPU lié au traitement des en-têtes.
**Syntaxe :** `ip link set eth0 mtu 9000`
**Cas réguliers :**
- `Optimisation de stockage iSCSI/NFS` — Configuration du MTU à 9000 sur le réseau dédié au stockage pour augmenter le débit de transfert et libérer du CPU
- `Réduction des interruptions CPU par seconde` — Divise par 6 le nombre de paquets à traiter pour un même volume de données (9000 octets vs 1500 octets)
**Origine :** Introduit par Alteon WebSystems à la fin des années 1990 pour les réseaux Gigabit Ethernet.
**Subtilités/confusions :**
- TOUS les équipements du chemin réseau (cartes réseau hôtes, switchs, routeurs) doivent être configurés avec le même MTU 9000.
- Si un seul switch intermédiaire reste à MTU 1500, les Jumbo Frames seront rejetées ou sévèrement fragmentées, chutant l'efficacité.
**Urgences/dangers :** ⚠️ Une mauvaise configuration partielle de Jumbo Frames entraîne des pertes de paquets silencieuses et des connexions bloquées.
**Précautions :** Réserver l'utilisation des Jumbo Frames aux réseaux locaux dédiés (VLAN de stockage iSCSI/NFS) et ne jamais les activer sur des réseaux routés vers Internet.
**Équivalents :** Standard Ethernet Frame (MTU 1500)
**Voir aussi :** MTU, Ethernet, iSCSI, NAS

## `VLAN Tagging` — IEEE 802.1Q VLAN Tagging [Réseau]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** 802.1Q Tagging, Trunking, Frame Tagging
**Contextes :** commutation Ethernet, virtualisation, hyperviseurs, transport multi-VLANs sur câble unique
**Rôle :** Insertion d'un champ d'en-tête 802.1Q de 4 octets dans la trame Ethernet pour identifier le numéro de VLAN (VLAN ID) auquel elle appartient lors du transit sur un lien Trunk.
**Syntaxe :** `ip link add link eth0 name eth0.10 type vlan id 10`
**Cas réguliers :**
- `Lien Trunk entre Switchs` — Transport simultané du trafic de 20 VLANs différents sur un unique câble 10 GbE en marquant chaque trame avec son Tag 802.1Q
- `VLAN Tagging sur Hyperviseur` — L'hyperviseur marque les trames des VMs avec le VLAN ID approprié avant de les envoyer vers le switch physique
**Origine :** Standardisé par l'IEEE sous la norme 802.1Q en 1998.
**Subtilités/confusions :**
- Port Access (trames non marquées / Untagged : pour ordinateurs) vs Port Trunk (trames marquées / Tagged : entre switchs ou vers hyperviseurs).
- Le champ VLAN ID est codé sur 12 bits, ce qui limite le nombre maximum de VLANs à 4094 par domaine de diffusion.
**Urgences/dangers :** ⚠️ Des attaques de "VLAN Hopping" (double marquage 802.1Q) permettent à un attaquant d'injecter du trafic dans un autre VLAN si le Native VLAN n'est pas sécurisé.
**Précautions :** Définir un Native VLAN inutilisé et différent du VLAN 1 sur tous les ports Trunk.
**Équivalents :** VXLAN (extension d'encapsulation pour le cloud)
**Voir aussi :** VLAN, Switch, Ethernet, 802.1Q

## `BGP Hijacking` — Border Gateway Protocol Hijacking [Sécurité / Réseau]
**Niveau :** expert | **Popularité :** 80 | **Aliases :** Détournement BGP, Route Hijacking, IP Hijacking
**Contextes :** sécurité du routage Internet, cyberattaques d'infrastructure, interception de trafic mondial
**Rôle :** Attaque réseau consistant à annoncer de manière illégitime un bloc d'adresses IP appartenant à un autre organisme via BGP, pour détourner ou intercepter son trafic Internet.
**Syntaxe :** (Détection via BGPmon, RPKI Validator, `bgpstream`)
**Cas réguliers :**
- `Détournement de trafic DNS/Crypto` — Un AS annonce un préfixe `/24` plus spécifique appartenant à un service cible pour intercepter le trafic et délivrer de faux certificats
- `Erreur de configuration (Route Leak)` — Annonce involontaire de routes privées par un FAI perturbant le routage mondial
**Origine :** Faille intrinsèque de la conception initiale de BGP-4 qui repose sur la confiance implicite entre Autonomous Systems.
**Subtilités/confusions :**
- Le BGP Hijacking s'appuie sur la règle BGP qui privilégie toujours les annonces de préfixes les plus spécifiques (ex: un `/24` l'emporte sur un `/22`).
- Peut être malveillant (espionnage, vol de cryptomonnaie) ou accidentel (erreur humaine d'un opérateur FAI).
**Urgences/dangers :** ⚠️ Permet l'interception massive de données, le Man-in-the-Middle mondial et la délivrance de certificats TLS frauduleux.
**Précautions :** Déployer RPKI (ROA - Route Origin Authorization) et filtrer les annonces BGP entrantes avec ROV (Route Origin Validation).
**Équivalents :** DNS Spoofing (au niveau nom de domaine)
**Voir aussi :** BGP, AS, RPKI, IP

## `QoS` — Quality of Service [Réseau]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** Qualité de Service, DiffServ, CoS
**Contextes :** priorisation du trafic réseau, VoIP, visioconférence, streaming, congestion réseau
**Rôle :** Ensemble de mécanismes réseau (marquage, classification, file d'attente, façonnage) permettant d'accorder une priorité et des garanties de débit/latence à certains flux critiques.
**Syntaxe :** `tc qdisc add dev eth0 root handle 1: htb default 12` (Linux Traffic Control)
**Cas réguliers :**
- `Priorisation de la VoIP (DSCP EF)` — Marquage des paquets de téléphonie avec le code DiffServ EF (Expedited Forwarding) pour éliminer les saccades audio
- `Limitation du trafic P2P / Sauvegarde` — Relégation des gros transferts non prioritaires dans une file d'attente à bas débit en cas de saturation du lien
**Origine :** Développé par l'IETF avec les modèles IntServ (RFC 1633) puis DiffServ (RFC 2474).
**Subtilités/confusions :**
- La QoS ne crée pas de bande passante supplémentaire : elle gère la répartition et le sacrifice du trafic en cas de saturation de la liaison.
- DiffServ marque les paquets au niveau de la couche 3 (champ DSCP dans l'en-tête IP) tandis que 802.1p CoS marque en couche 2 (trame Ethernet).
**Urgences/dangers :** —
**Précautions :** Appliquer le marquage QoS au plus près de la source (sur le poste ou le premier switch) pour un traitement optimal tout au long du chemin.
**Équivalents :** Traffic Shaping, Bandwidth Limiting
**Voir aussi :** DSCP, VoIP, Router, Network

## `ZFS Pool` — ZFS Storage Pool (zpool) [Stockage]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** zpool, ZFS Pool
**Contextes :** stockage d'entreprise, Proxmox, TrueNAS, gestionnaires de fichiers ZFS, tolérance aux pannes
**Rôle :** Pool de stockage virtuel ZFS regroupant plusieurs disques physiques (VDEVs) pour fournir un espace unifié performant et sécurisé avec auto-réparation des données (self-healing).
**Syntaxe :** `zpool status` ou `zpool create mypool mirror /dev/sdb /dev/sdc`
**Cas réguliers :**
- `Création d'un pool RAID-Z2` — Regroupement de 6 disques en tolérant la panne simultanée de 2 disques avec vérification de checksums à la volée
- `Remplacement à chaud d'un disque défectueux` — `zpool replace mypool /dev/sdb /dev/sdg` pour lancer le résilvering automatique
**Origine :** Développé par Sun Microsystems pour Solaris en 2001 (Matthew Ahrens et Jeff Bonwick) ; maintenu sous OpenZFS.
**Subtilités/confusions :**
- Dans ZFS, on ne crée pas de systèmes de fichiers sur des partitions fixes : tous les datasets ZFS partagent dynamiquement la totalité de l'espace du zpool.
- La détection de corruption silencieuse de données (Bit Rot) est automatique grâce au hachage de chaque bloc de données.
**Urgences/dangers :** ⚠️ Ne jamais détruire un VDEV de type Stripe dans un zpool sous peine de perdre l'intégralité des données du pool complet.
**Précautions :** Toujours prévoir au moins 20% d'espace libre dans un zpool ZFS pour éviter les dégradations majeures de performances.
**Équivalents :** LVM VG (Volume Group), Btrfs pool
**Voir aussi :** ZFS, RAID, LVM, SSD, RAID-Z

## `Ceph` — Ceph Distributed Object Store [Stockage / Cloud]
**Niveau :** expert | **Popularité :** 85 | **Aliases :** Ceph Storage, RADOS, Ceph cluster
**Contextes :** stockage cloud distribué, OpenStack, Proxmox VE, stockage objet S3, block devices distribués
**Rôle :** Plateforme de stockage distribué open-source hautement évolutive fournissant du stockage Objet (RADOS), Bloc (RBD) et Fichier (CephFS) sans point unique de défaillance.
**Syntaxe :** `ceph status` ou `ceph osd status` ou `rbd list`
**Cas réguliers :**
- `Stockage de disques de VMs Proxmox sur RBD` — Fourniture de volumes block virtuels haute disponibilité répliqués sur 3 nœuds Ceph
- `Stockage Objet S3 avec Ceph RadosGW` — Exposition d'une API compatible Amazon S3 pour le stockage de fichiers applicatifs
**Origine :** Créé par Sage Weil dans le cadre de sa thèse de doctorat à l'UC Santa Cruz en 2004 ; maintenu par la Fondation Linux.
**Subtilités/confusions :**
- Ceph n'utilise pas de serveur central de métadonnées pour trouver les données : il utilise l'algorithme déterministe CRUSH pour calculer l'emplacement des blocs.
- Nécessite au minimum 3 nœuds avec des démons MON (moniteurs) et OSD (storage daemons) pour garantir un quorum et une réplication saine.
**Urgences/dangers :** ⚠️ Un réseau d'interconnexion Ceph (cluster network) lent ou instable provoque le flapping des OSDs et peut paralyser les accès stockage.
**Précautions :** Déployer un réseau 10 GbE ou 25 GbE dédié exclusivement au trafic de réplication interne du cluster Ceph.
**Équivalents :** GlusterFS, MinIO (objet uniquement), VMware vSAN
**Voir aussi :** OpenStack, S3, ZFS, Proxmox

## `LVM` — Logical Volume Manager [Stockage / Linux]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** LVM2, Logical Volume, Volume Group
**Contextes :** administration de stockage Linux, redimensionnement dynamique de partitions, snapshots, chiffrement LUKS
**Rôle :** Couche d'abstraction de stockage Linux permettant de regrouper des disques physiques en pools (Volume Groups) et de créer des volumes logiques redimensionnables à chaud.
**Syntaxe :** `pvs` (Physical Volumes), `vgs` (Volume Groups), `lvs` (Logical Volumes)
**Cas réguliers :**
- `Extension à chaud d'un volume logique` — `lvextend -r -L +10G /dev/vg0/root` pour agrandir la partition et le système de fichiers sans reboot
- `Création d'un instantané (Snapshot LVM)` — `lvcreate -s -n snap_root -L 5G /dev/vg0/root` pour faire une sauvegarde avant mise à jour
**Origine :** Développé par Heinz Mauelshagen en 1998 pour Linux, largement inspiré du LVM d'HP-UX Unix.
**Subtilités/confusions :**
- Hiérarchie LVM à 3 niveaux : PV (Physical Volume = disque/partition) → VG (Volume Group = pool d'espace) → LV (Logical Volume = partition virtuelle).
- Les snapshots LVM classiques utilisent le Copy-on-Write (CoW) et doivent être surveillés pour ne pas saturer.
**Urgences/dangers :** ⚠️ Si l'espace alloué à un snapshot LVM traditionnel atteint 100% de saturation, le snapshot est définitivement corrompu et invalide.
**Précautions :** Utiliser des thin pools LVM (`thin provisioning`) pour des instantanés et volumes plus flexibles et économes en espace.
**Équivalents :** ZFS (système de fichiers avec gestionnaire intégré), Btrfs
**Voir aussi :** ext4, ZFS, partition, disk, fdisk

## `swap` — Swap Space / Espace de Pagination [Système]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** Swap file, Swap partition, Espace d'échange
**Contextes :** gestion de la mémoire sous Linux/Unix, prévention d'OOM (Out Of Memory), mise en veille prolongée (hibernation)
**Rôle :** Espace disque (partition ou fichier) utilisé par le système d'exploitation pour déplacer les pages mémoire RAM inactives afin de libérer de la mémoire vive physique.
**Syntaxe :** `swapon --show` ou `free -m` ou `mkswap /swapfile && swapon /swapfile`
**Cas réguliers :**
- `Création d'un fichier swap 4 Go` — `fallocate -l 4G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile`
- `Réglage de la réactivité swappiness` — `sysctl vm.swappiness=10` pour éviter que le système n'utilise trop rapidement le disque
**Origine :** Concept de mémoire virtuelle présent depuis les premiers systèmes Unix de la fin des années 1960.
**Subtilités/confusions :**
- La vitesse d'accès au swap (même sur SSD NVMe) reste des dizaines de fois plus lente que la RAM physique — un système qui "swappe" massivement ralentit fortement.
- Kubernetes exige généralement de désactiver complètement le swap (`swapoff -a`) sur les nœuds du cluster.
**Urgences/dangers :** —
**Précautions :** Régler le paramètre `vm.swappiness` (entre 10 et 30 sur serveur) pour limiter l'utilisation du swap tant que la RAM n'est pas presque pleine.
**Équivalents :** Pagefile.sys (Windows), swapfile (macOS)
**Voir aussi :** RAM, free, sysctl, memory, OOM

## `IOPS` — Input/Output Operations Per Second [Stockage]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** Operations d'E/S par seconde
**Contextes :** benchmark de disque, performance SSD/NVMe/HDD, dimensionnement de bases de données, stockage cloud (EBS)
**Rôle :** Unité de mesure de performance caractérisant le nombre d'opérations individuelles de lecture ou d'écriture qu'un système de stockage peut exécuter en une seconde.
**Syntaxe :** (mesure avec `fio --name=randread --ioengine=libaio --rw=randread --bs=4k --iodepth=64 ...`)
**Cas réguliers :**
- `Benchmark SSD NVMe 4K` — Mesure de performance atteignant 500 000 IOPS en lecture aléatoire avec des blocs de 4 Ko
- `Provisionnement cloud (AWS EBS gp3)` — Réservation d'un volume de stockage avec 3 000 IOPS garanties pour une base de données MySQL
**Origine :** Métrique standard d'évaluation de la performance du matériel de stockage informatique depuis les premiers disques magnétiques.
**Subtilités/confusions :**
- Les IOPS doivent toujours être associées à la taille du bloc (ex: 4 Ko vs 64 Ko) et au type d'accès (aléatoire vs séquentiel).
- Un disque dur mécanique HDD plafonne à ~150-200 IOPS en aléatoire due au déplacement physique des têtes, contre > 1 000 000 IOPS pour un SSD NVMe.
**Urgences/dangers :** —
**Précautions :** Pour les bases de données (accès aléatoire en petits blocs), privilégier des IOPS élevées ; pour la vidéo (gros fichiers), privilégier le débit (Throughput en Mo/s).
**Équivalents :** TPS (Transactions Per Second)
**Voir aussi :** SSD, HDD, NVMe, Throughput, fio

## `Throughput` — Data Throughput / Débit [Réseau / Stockage]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** Débit, Bandwidth Utilization, Transfer Rate
**Contextes :** mesure de performance réseau, vitesse de transfert de stockage, sauvegardes, streaming
**Rôle :** Quantité réelle de données utiles transmises avec succès à travers un canal de communication ou un système de stockage par unité de temps (ex: Mo/s, Gbps).
**Syntaxe :** `iperf3 -c server-ip` (réseau) ou `dd if=/dev/zero of=test bs=1G count=1 oflag=direct` (disque)
**Cas réguliers :**
- `Validation de débit réseau 10 GbE` — Mesure avec `iperf3` confirmant un débit effectif de 9.41 Gbps sur un câble Cat6A
- `Transfert séquentiel de disque SSD` — Lecture continue de gros fichiers à un débit de 3 500 Mo/s sur bus PCIe Gen4
**Origine :** Concept fondamental de la théorie de l'information et des télécommunications.
**Subtilités/confusions :**
- Bande passante (Bandwidth = capacité théorique maximale du canal) vs Débit (Throughput = vitesse réelle mesurée des données utiles).
- Le débit utile (Goodput) exclut les en-têtes de protocoles (TCP/IP/Ethernet) et les retransmissions d'erreurs.
**Urgences/dangers :** —
**Précautions :** Faire attention à la confusion courante entre bits par seconde (b/s, Gbps pour le réseau) et octets par seconde (B/s, Mo/s pour le stockage).
**Équivalents :** Goodput, Bitrate
**Voir aussi :** IOPS, Latency, iperf3, nload

## `Latency` — Network & System Latency [Réseau / Système]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** Latence, RTT, Temps de réponse, Delay
**Contextes :** performance réseau, jeux en ligne, trading haute fréquence, réactivité applicative, accès mémoire
**Rôle :** Délai temporel s'écoulant entre l'émission d'une requête ou d'une instruction et la réception de la réponse correspondante (ex: en millisecondes ou nanosecondes).
**Syntaxe :** `ping host` ou `mtr host` ou `curl -w "%{time_total}\n" -o /dev/null -s https://example.com`
**Cas réguliers :**
- `Mesure de latence RTT ping` — Temps de retour aller-retour de 2 ms entre deux instances situées dans le même datacenter cloud
- `Latence d'accès mémoire` — Accès à la cache L1 (1 ns), RAM (50 ns), SSD NVMe (50 µs), HDD (10 ms)
**Origine :** Propriété physique fondamentale de la propagation des signaux électroniques et lumineux.
**Subtilités/confusions :**
- Augmenter la bande passante (débit) n'améliore pas la latence si celle-ci est limitée par la distance physique et la vitesse de la lumière dans la fibre.
- En réseau, la latence est souvent mesurée en RTT (Round Trip Time = temps d'aller-retour complet).
**Urgences/dangers :** —
**Précautions :** Déployer des CDN et héberger les applications au plus près des utilisateurs pour réduire la latence réseau liée à la distance géographique.
**Équivalents :** RTT (Round Trip Time), Lag
**Voir aussi :** ping, mtr, Throughput, QoS

## `NVMe-oF` — NVMe over Fabrics [Stockage / Réseau]
**Niveau :** expert | **Popularité :** 80 | **Aliases :** NVMf, NVMe over RoCE, NVMe over TCP
**Contextes :** stockage SAN ultra-hautes performances, datacenters cloud, NVMe distribué, RoCEv2
**Rôle :** Spécification réseau permettant d'étendre le protocole et les commandes NVMe à très faible latence sur des réseaux haut débit (Ethernet, Fibre Channel, InfiniBand).
**Syntaxe :** `nvme connect -t tcp -n <iqn> -a <ip> -s 4420`
**Cas réguliers :**
- `NVMe over TCP` — Connexion d'un volume de stockage SSD NVMe distant sur un réseau Ethernet 100 GbE standard sans matériel spécialisé
- `NVMe over RoCEv2 (RDMA)` — Accès à un pool de stockage NVMe distant avec une latence sub-10 microsecondes via des cartes réseau RDMA
**Origine :** Spécifié par le consortium NVM Express Inc. et publié en 2016 pour dépasser les limites d'iSCSI et de Fibre Channel.
**Subtilités/confusions :**
- Transporte les commandes NVMe natives directement sur le réseau sans encapsuler dans SCSI, éliminant la surcouche de traduction de protocole.
- NVMe-oF/TCP fonctionne sur du matériel Ethernet standard ; NVMe-oF/RDMA nécessite des cartes réseau prenant en charge RoCEv2 ou iWARP.
**Urgences/dangers :** —
**Précautions :** Activer les fonctionnalités Priority Flow Control (PFC) sur les switches Ethernet lors de l'utilisation de NVMe over RoCE.
**Équivalents :** iSCSI (plus ancien, latence plus élevée), Fibre Channel
**Voir aussi :** NVMe, iSCSI, SAN, SSD, RDMA

## `iSCSI Target` — iSCSI Storage Target [Stockage / Réseau]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** Cible iSCSI, LUN Target, targetcli
**Contextes :** stockage SAN sur réseau IP, baies de stockage, virtualisation (VMware, Proxmox), stockage bloc partagé
**Rôle :** Serveur ou baie de stockage qui expose des volumes de stockage bloc (LUNs) sur un réseau IP via le protocole iSCSI à destination de clients (initiateurs).
**Syntaxe :** `targetcli` (administration Linux) ou `iscsiadm -m discovery -t st -p <ip>`
**Cas réguliers :**
- `Publication d'un volume SAN pour cluster Proxmox` — Exportation d'un disque virtuel bloc via iSCSI Target pour l'hébergement de VMs
- `Configuration d'initiateur iSCSI sous Linux` — Connexion de l'initiateur au serveur iSCSI Target et montage du disque `/dev/sdb` apparu sur le système
**Origine :** Spécifié par l'IETF dans la RFC 3720 en 2004 pour transporter les commandes SCSI sur le protocole TCP/IP (port 3260).
**Subtilités/confusions :**
- Initiateur iSCSI (client qui consomme le stockage) vs Cible/Target iSCSI (serveur qui héberge et fournit le stockage).
- iSCSI fournit du stockage bloc brut (Block Storage) — le système client doit le formater lui-même (ext4, NTFS, VMFS), contrairement au NAS qui fournit des fichiers (NFS, SMB).
**Urgences/dangers :** ⚠️ Monter le même LUN iSCSI non-clusterisé en écriture sur deux serveurs différents en même temps corrompt instantanément le système de fichiers.
**Précautions :** Utiliser l'authentification CHAP et restreindre l'accès à la cible iSCSI par le nom IQN de l'initiateur autorisé.
**Équivalents :** NVMe-oF (alternative moderne plus rapide), Fibre Channel Target
**Voir aussi :** SAN, NAS, iSCSI, LUN, targetcli
