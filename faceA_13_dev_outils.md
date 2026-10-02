## `gcc` — Compilateur C/C++ de la suite GNU [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** —
**Contextes :** compiler du code source C en exécutable binaire, générer des bibliothèques statiques ou dynamiques sous Linux/UNIX
**Rôle :** Compilateur C historique du projet GNU (GNU Compiler Collection) traduisant le code C en binaire exécutable optimisé pour la plateforme cible.
**Syntaxe :** `gcc [options] fichier.c -o executable`
**Cas réguliers :**
- `gcc main.c -o app` — Compiler un fichier source C en binaire exécutable nommé `app`
- `gcc -Wall -Wextra -O2 main.c -o app` — Activer tous les avertissements recommandés (`-Wall -Wextra`) et l'optimisation de niveau 2 (`-O2`)
- `gcc -c module.c` — Compiler en fichier objet `.o` sans effectuer l'étape d'édition de liens (*linking*)
**Origine :** Richard Stallman (1987) — projet fondateur du système d'exploitation GNU.
**Subtilités/confusions :**
- `gcc` compile le C par défaut ; pour du C++, utiliser `g++` qui inclut automatiquement la libstdc++.
- L'option `-g` inclut les symboles de débogage nécessaires pour `gdb` ou `valgrind`.
**Urgences/dangers :** —
**Précautions :** Toujours utiliser `-Wall -Wextra -Werror` dans les builds CI pour traiter les avertissements comme des erreurs bloquantes.
**Équivalents :** clang, tcc, icc
**Voir aussi :** g++, clang, make, gdb

## `g++` — Compilateur C++ de la suite GNU [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** compiler des programmes C++ (du C++11 au C++23), lier automatiquement la bibliothèque standard C++ (`libstdc++`)
**Rôle :** Pilote de compilation GNU dédié au C++ qui invoque `gcc` avec la résolution de la bibliothèque standard C++ et des Runtime C++ pré-configurés.
**Syntaxe :** `g++ [options] fichier.cpp -o executable`
**Cas réguliers :**
- `g++ main.cpp -o app` — Compiler un fichier C++ en binaire exécutable
- `g++ -std=c++20 -Wall main.cpp -o app` — Forcer le standard C++20 et activer les avertissements
- `g++ -O3 -march=native main.cpp -o app` — Optimiser au maximum (`-O3`) pour le processeur local (`-march=native`)
**Origine :** Michael Tiemann (1987) — premier compilateur C++ natif open source.
**Subtilités/confusions :**
- Diffère de `gcc` car il lie automatiquement `libstdc++` et traite les fichiers `.c` comme du C++.
**Urgences/dangers :** —
**Précautions :** Spécifier explicitement le standard C++ (`-std=c++17` ou `-std=c++20`) pour garantir la répétabilité du build.
**Équivalents :** clang++, icpx, MSVC (cl.exe)
**Voir aussi :** gcc, clang++, cmake, gdb

## `clang` — Compilateur C/C++/Obj-C basé sur LLVM [Cross]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** compiler du code C/C++ avec des messages d'erreur ultra-clairs, utiliser des analyseurs statiques et sanitizers (ASan, TSan), remplacer GCC
**Rôle :** Front-end de compilation C/C++/Objective-C basé sur l'infrastructure LLVM, réputé pour sa vitesse de compilation, sa modularité et ses excellents diagnostics.
**Syntaxe :** `clang [options] fichier.c -o executable`
**Cas réguliers :**
- `clang main.c -o app` — Compiler un fichier C avec Clang
- `clang -fsanitize=address -g main.c -o app` — Compiler avec le détecteur d'erreurs mémoire (AddressSanitizer)
- `clang -emit-llvm -S main.c` — Générer la représentation intermédiaire (IR) LLVM en texte human-readable
**Origine :** Apple / Chris Lattner (2007) — créé pour remplacer GCC dans les outils Xcode d'Apple.
**Subtilités/confusions :**
- Compatible avec les drapeaux CLI de GCC (`-Wall`, `-O2`, `-o`…), ce qui permet de l'utiliser en remplacement direct dans la plupart des Makefiles.
**Urgences/dangers :** —
**Précautions :** Utiliser `-fsanitize=undefined` et `-fsanitize=address` en phase de test pour intercepter les comportements indéfinis.
**Équivalents :** gcc, tcc
**Voir aussi :** clang++, gcc, llvm-ar, scan-build

## `clang++` — Compilateur C++ basé sur LLVM [Cross]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** compiler du code C++ sous macOS (compilateur par défaut via Xcode), Linux ou Windows, intégrer l'écosystème d'outils LLVM
**Rôle :** Variante de Clang pré-configurée pour le C++, liant par défaut `libc++` (macOS) ou `libstdc++` (Linux).
**Syntaxe :** `clang++ [options] fichier.cpp -o executable`
**Cas réguliers :**
- `clang++ -std=c++20 main.cpp -o app` — Compiler en C++20 avec Clang++
- `clang++ -stdlib=libc++ main.cpp -o app` — Utiliser la bibliothèque standard C++ de LLVM (`libc++`)
**Origine :** Projet LLVM (2007).
**Subtilités/confusions :**
- Sous macOS, la commande `g++` est souvent un alias ou un wrapper pointeur vers `clang++`.
**Urgences/dangers :** —
**Précautions :** Faire attention aux incompatibilités d'ABI lors du mélange d'objets compilés avec GCC (libstdc++) et Clang (libc++).
**Équivalents :** g++, MSVC
**Voir aussi :** clang, g++, cmake

## `bear` — Générateur de base de données de compilation (`compile_commands.json`) [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** intercepter les commandes d'un Makefile pour générer automatiquement le fichier `compile_commands.json` requis par Clangd, Clang-Tidy, et les serveurs LSP
**Rôle :** Outil de capture de compilation qui intercepte les appels au compilateur lors du build de votre projet pour produire la base de données de compilation au format JSON.
**Syntaxe :** `bear -- <commande_build>`
**Cas réguliers :**
- `bear -- make` — Générer `compile_commands.json` en interceptant l'exécution de `make`
- `bear -- ninja -C build` — Générer la base de données de compilation à partir d'un build Ninja
**Origine :** László Nagy (2014) — créé pour alimenter les outils d'analyse statique C/C++ basés sur Clang.
**Subtilités/confusions :**
- Fonctionne en préchargeant une bibliothèque via `LD_PRELOAD` qui intercepte les appels système `execve` des compilateurs.
**Urgences/dangers :** —
**Précautions :** Toujours faire un `make clean` avant de lancer `bear -- make` pour forcer la re-compilation de tous les fichiers objets.
**Équivalents :** compiledb, cmake (-DCMAKE_EXPORT_COMPILE_COMMANDS=ON)
**Voir aussi :** cmake, clang-tidy, clang

## `cmake` — Générateur de fichiers de build multiplateforme [Cross]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** configurer la compilation de projets C/C++ complexes et multiplateformes, générer des Makefiles, fichiers Ninja ou projets Visual Studio / Xcode
**Rôle :** Moteur de méta-build qui lit un fichier `CMakeLists.txt` et génère les fichiers de build natifs de la plateforme cible.
**Syntaxe :** `cmake [options] <dossier_source>` ou `cmake --build <dossier_build>`
**Cas réguliers :**
- `cmake -B build -G Ninja` — Configurer le build dans le dossier `build/` en générant des fichiers pour Ninja
- `cmake --build build -j` — Compiler le projet configuré dans `build/` en utilisant tous les cœurs
- `cmake --install build --prefix /usr/local` — Installer les binaires compilés dans le système
**Origine :** Bill Hoffman / Kitware (2000) — créé pour automatiser le build de la bibliothèque de traitement d'images ITK.
**Subtilités/confusions :**
- `cmake` ne compile pas lui-même le code source : il génère les fichiers pour un outil de build effectif (Make, Ninja, MSVC).
**Urgences/dangers :** —
**Précautions :** Toujours privilégier les builds hors-source (`cmake -B build`) pour conserver un répertoire source propre.
**Équivalents :** meson, autotools, bazel
**Voir aussi :** make, ninja, gcc, clang

## `ninja` — Moteur de compilation ultra-rapide axé sur la vitesse [Cross]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** accélérer considérablement les temps de compilation des grands projets (Android, LLVM, Chromium, CMake) par rapport à Make
**Rôle :** Petit moteur de build conçu spécifiquement pour la vitesse maximale, lisant des fichiers de configuration simples générés par des méta-outils (CMake, Meson).
**Syntaxe :** `ninja [options] [cible]`
**Cas réguliers :**
- `ninja` — Compiler le projet configuré dans le dossier courant (lit `build.ninja`)
- `ninja -C build` — Se placer dans le dossier `build/` et exécuter la compilation
- `ninja -t targets` — Lister toutes les cibles de build disponibles
**Origine :** Evan Martin / Google (2011) — créé pour accélérer la compilation de Google Chrome.
**Subtilités/confusions :**
- Ninja n'est pas pensé pour être écrit à la main par des humains ; il est conçu pour être la cible de génération de CMake ou Meson.
- Utilise par défaut automatiquement tous les cœurs CPU disponibles sans avoir à spécifier `-j`.
**Urgences/dangers :** —
**Précautions :** Ne pas éditer manuellement le fichier `build.ninja` car il est régénéré par CMake/Meson.
**Équivalents :** make, samurai (samu)
**Voir aussi :** cmake, meson, make

## `bazel` — Moteur de build multi-langages et monorepo [Cross]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** gérer le build hermétique, reproductible et distribué de grands monorepos multi-langages (C++, Java, Go, Python, Rust)
**Rôle :** Moteur de build et de test à grande échelle développé par Google, garantissant la reproductibilité stricte grâce à la mise en cache granulaire des artefacts.
**Syntaxe :** `bazel <commande> [options] <cible>`
**Cas réguliers :**
- `bazel build //src:main` — Compiler la cible `main` définie dans le paquet `src`
- `bazel test //...` — Lancer tous les tests unitaires du projet
- `bazel run //src:app` — Compiler et exécuter immédiatement l'application
**Origine :** Google (2015) — version open source du système de build interne `Blaze` de Google.
**Subtilités/confusions :**
- Bazel impose un bac à sable strict : si une dépendance n'est pas déclarée explicitement dans le fichier `BUILD`, le build échoue.
**Urgences/dangers :** —
**Précautions :** Configurer un serveur de cache distant (*Remote Build Execution / RBE*) pour tirer pleinement parti de la vitesse de Bazel en équipe.
**Équivalents :** buck (Meta), pants, nx, msbuild
**Voir aussi :** cmake, make, cargo

## `meson` — Système de build moderne et rapide [Cross]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** configurer et compiler des projets C/C++/GNOME/GTK avec une syntaxe claire et conviviale en remplacement d'Autotools
**Rôle :** Système de build moderne et extrêmement rapide utilisant Python pour l'analyse et générant des fichiers Ninja pour la compilation.
**Syntaxe :** `meson setup <dossier_build>` et `meson compile -C <dossier_build>`
**Cas réguliers :**
- `meson setup build` — Configurer le projet défini par `meson.build` dans le répertoire `build/`
- `meson compile -C build` — Lancer la compilation (invoque Ninja)
- `meson test -C build` — Lancer la suite de tests du projet
**Origine :** Jussi Pakkanen (2012) — créé pour offrir une alternative moderne et lisible à CMake et Autotools.
**Subtilités/confusions :**
- La syntaxe du fichier `meson.build` est non Turing-complète par design pour éviter la complexité des scripts CMake.
**Urgences/dangers :** —
**Précautions :** Nécessite Python 3 et Ninja installés sur la machine hôte.
**Équivalents :** cmake, autotools
**Voir aussi :** ninja, cmake, gcc

## `watchexec` — Exécution automatique de commandes sur modification de fichiers [Cross]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** —
**Contextes :** relancer automatiquement des tests, re-compiler du code ou redémarrer un serveur local chaque fois qu'un fichier source du projet est modifié
**Rôle :** Outil CLI moderne et ultra-rapide écrit en Rust qui surveille une arborescence de fichiers et relance la commande spécifiée dès qu'un événement de fichier est détecté.
**Syntaxe :** `watchexec [options] -- <commande>`
**Cas réguliers :**
- `watchexec -e rs -- cargo test` — Relancer `cargo test` dès qu'un fichier `.rs` est modifié
- `watchexec -w src -r -- python3 app.py` — Redémarrer (`-r`) l'application Python si un fichier dans `src/` change
**Origine :** Félix Saparelli (2016) — écrit en Rust.
**Subtilités/confusions :**
- Ignore automatiquement les fichiers listés dans votre `.gitignore` sans aucune configuration supplémentaire.
**Urgences/dangers :** —
**Précautions :** Utiliser l'option `-r` (restart) pour tuer le processus précédent avant de relancer le nouveau si c'est un serveur long.
**Équivalents :** nodemon, entr, reflex
**Voir aussi :** just, cargo, uv

## `rustc` — Compilateur officiel du langage Rust [Cross]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** —
**Contextes :** compiler directement un fichier source Rust `.rs` sans passer par Cargo, inspecter le code assembleur ou la MIR générée
**Rôle :** Compilateur natif de Rust basé sur le back-end LLVM, responsable de l'analyse du vérificateur d'emprunts (*borrow checker*) et de la génération de code binaire.
**Syntaxe :** `rustc [options] fichier.rs`
**Cas réguliers :**
- `rustc main.rs -O -o app` — Compiler directement un fichier Rust en binaire optimisé
- `rustc --explain E0308` — Afficher une explication détaillée d'un code d'erreur de compilation Rust
- `rustc --emit asm main.rs` — Générer le code assembleur correspondant
**Origine :** Graydon Hoare / Mozilla (2010).
**Subtilités/confusions :**
- Dans 99% des cas, les développeurs utilisent `cargo` qui invoque `rustc` en arrière-plan avec les bons arguments.
**Urgences/dangers :** —
**Précautions :** Utiliser `rustc --explain` dès qu'un message d'erreur du compilateur n'est pas immédiatement clair.
**Équivalents :** gcc, clang, javac
**Voir aussi :** cargo, rustup, clang

## `javac` — Compilateur de bytecode du langage Java [Cross]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** compiler des fichiers de code source Java (`.java`) en fichiers de bytecode Java (`.class`) exécutables par la JVM
**Rôle :** Compilateur Java officiel distribué avec le JDK (Java Development Kit).
**Syntaxe :** `javac [options] Source.java`
**Cas réguliers :**
- `javac Main.java` — Compiler un fichier `Main.java` en fichier de bytecode `Main.class`
- `javac -d bin/ src/*.java` — Compiler tous les fichiers du dossier `src/` vers le dossier de sortie `bin/`
- `javac -cp "lib/*" Main.java` — Compiler en incluant des bibliothèques JAR dans le classpath
**Origine :** Sun Microsystems (1995) / désormais géré par Oracle et le projet OpenJDK.
**Subtilités/confusions :**
- `javac` produit du bytecode `.class`, non un binaire natif (exécutable ensuite avec `java Main`).
**Urgences/dangers :** —
**Précautions :** S'assurer d'utiliser la même version de `javac` et de `java` (`javac -version`) pour éviter les erreurs `UnsupportedClassVersionError`.
**Équivalents :** kotlinc (Kotlin), scalac (Scala)
**Voir aussi :** java, jar, maven, gradle

## `zig` — Compilateur et toolchain du langage Zig [Cross]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** —
**Contextes :** compiler du code Zig, utiliser Zig comme compilateur C/C++ multiplateforme ultra-performant (cross-compilation facile)
**Rôle :** Toolchain complète pour le langage Zig, intégrant un compilateur Zig, un compilateur C/C++ léger (`zig cc`), un gestionnaire de dépendances et un moteur de build.
**Syntaxe :** `zig <commande> [options]`
**Cas réguliers :**
- `zig build-exe main.zig` — Compiler un programme Zig en exécutable natif
- `zig cc -target x86_64-windows-gnu main.c -o app.exe` — Cross-compiler du code C pour Windows depuis Linux sans installer de toolchain MinGW !
- `zig test main.zig` — Lancer les tests unitaires intégrés au code source
**Origine :** Andrew Kelley (2015) — créé pour remplacer le C avec un langage simple, sans macro et sans comportement indéfini.
**Subtilités/confusions :**
- `zig cc` et `zig c++` sont des remplacements directs et redoutablement efficaces de `gcc`/`clang` pour la cross-compilation C/C++.
**Urgences/dangers :** —
**Précautions :** Le langage Zig est encore en évolution rapide (0.x) ; vérifier la version exacte utilisée.
**Équivalents :** gcc, clang, cargo
**Voir aussi :** gcc, clang, cargo

## `nvcc` — Compilateur NVIDIA CUDA C/C++ pour GPU [Linux/Windows]
**Niveau :** avance | **Popularité :** 88 | **Aliases :** —
**Contextes :** compiler du code C/C++ contenant des noyaux (*kernels*) d'exécution parallèle CUDA pour GPU NVIDIA (IA, calcul scientifique)
**Rôle :** Pilote de compilation NVIDIA qui sépare le code hôte (exécuté sur le CPU via GCC/MSVC) du code appareil (exécuté sur le GPU sous forme de bytecode PTX/cubin).
**Syntaxe :** `nvcc [options] fichier.cu -o executable`
**Cas réguliers :**
- `nvcc kernel.cu -o app` — Compiler un fichier source CUDA (`.cu`)
- `nvcc -arch=sm_80 kernel.cu -o app` — Cibler l'architecture GPU Ampere (ex: NVIDIA A100 / RTX 3080)
- `nvcc -O3 -Xcompiler -Wall kernel.cu -o app` — Passer des drapeaux au compilateur CPU hôte via `-Xcompiler`
**Origine :** NVIDIA (2007) — composant fondamental du toolkit CUDA pour le GPGPU.
**Subtilités/confusions :**
- Nécessite des pilotes NVIDIA compatibles et le toolkit CUDA installé sur le système hôte.
**Urgences/dangers :** —
**Précautions :** Vérifier l'architecture Compute Capability de votre GPU (`nvidia-smi`) et passer l'option `-arch=sm_XX` correspondante.
**Équivalents :** hipcc (AMD ROCm)
**Voir aussi :** gcc, clang, GPU

## `nasm` — Netwide Assembler pour l'architecture x86/x64 [Cross]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** assembler du code source en langage d'assemblage x86 ou x64 (syntaxe Intel) en fichier objet ELF, Mach-O ou Win64
**Rôle :** Assembleur modulaire et portable pour l'architecture x86/x64 utilisant la syntaxe Intel très lisible.
**Syntaxe :** `nasm -f <format> fichier.asm -o fichier.o`
**Cas réguliers :**
- `nasm -f elf64 main.asm -o main.o` — Assembler un fichier source en objet 64 bits sous Linux
- `nasm -f win64 main.asm -o main.obj` — Assembler pour Windows 64 bits
- `nasm -e main.asm` — Prétraiter les macros du fichier assembleur sans assembler
**Origine :** Simon Tatham et Julian Hall (1996) — créé pour combler le manque d'un bon assembleur syntaxe Intel sous Linux.
**Subtilités/confusions :**
- Diffère de `as` (GNU Assembler) qui utilise par défaut la syntaxe AT&T (`mov %rax, %rbx`) alors que NASM utilise la syntaxe Intel (`mov rax, rbx`).
**Urgences/dangers :** —
**Précautions :** Toujours lier le fichier objet `.o` généré avec `ld` ou `gcc` pour obtenir un binaire exécutable.
**Équivalents :** yasm, fasm, masm, as (GAS)
**Voir aussi :** gcc, gdb, objdump

## `gdb` — Débogueur GNU pour C, C++ et Fortran [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** analyser un plantage d'application (*segfault*), inspecter la mémoire et la pile d'appels à un point d'arrêt, débugger des fichiers *core dump*
**Rôle :** Débogueur natif du projet GNU permettant d'interrompre l'exécution d'un programme, d'examiner ses variables, ses registres et de faire du pas-à-pas.
**Syntaxe :** `gdb [options] [executable] [core_dump]`
**Cas réguliers :**
- `gdb ./app` — Lancer le débogueur sur le binaire `app` (taper `run` pour démarrer)
- `gdb ./app core` — Analyser un fichier de core dump après un crash pour voir l'état exact au moment du segfault
- `gdb -p <pid>` — S'attacher à un processus en cours d'exécution
**Origine :** Richard Stallman (1986) — composant incontournable de l'écosystème C/C++ sous Linux.
**Subtilités/confusions :**
- Nécessite d'avoir compilé le programme avec l'option `-g` pour pouvoir faire correspondre les adresses mémoire au code source.
**Urgences/dangers :** S'attacher à un processus en production avec `gdb` le met en pause tant que vous êtes dans le débogueur.
**Précautions :** Utiliser la commande `bt` (backtrace) dans gdb pour obtenir immédiatement la pile d'appels lors d'un crash.
**Équivalents :** lldb, windbg (Windows), r2 (radare2)
**Voir aussi :** gcc, valgrind, lldb, strace

## `lldb` — Débogueur haute performance basé sur LLVM [Cross]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** débugger des programmes C, C++, Swift ou Rust sous macOS (débogueur par défaut de Xcode), Linux ou Windows
**Rôle :** Débogueur de nouvelle génération basé sur les bibliothèques LLVM et Clang, réputé pour sa vitesse et son parseur d'expressions C++/Swift intégré.
**Syntaxe :** `lldb [options] [executable]`
**Cas réguliers :**
- `lldb ./app` — Lancer LLDB sur un binaire (taper `r` pour exécuter)
- `lldb -p <pid>` — S'attacher à un processus en cours
- `lldb -c core ./app` — Analyser un fichier core dump
**Origine :** Apple / Projet LLVM (2010) — conçu pour remplacer GDB dans Xcode et l'écosystème LLVM.
**Subtilités/confusions :**
- La syntaxe des commandes diffère légèrement de GDB (ex: `breakpoint set -n main` dans LLDB contre `b main` dans GDB, bien que les alias courts existent).
**Urgences/dangers :** —
**Précautions :** Utiliser `command alias` dans `~/.lldbinit` pour créer des raccourcis similaires à GDB si besoin.
**Équivalents :** gdb, windbg
**Voir aussi :** clang, gdb, rustc

## `valgrind` — Analyseur de mémoire et détecteur de fuites [Linux/macOS]
**Niveau :** avance | **Popularité :** 94 | **Aliases :** —
**Contextes :** détecter des fuites mémoire (*memory leaks*), des lectures/écritures hors-limites (*buffer overflow*), ou des accès à de la mémoire non initialisée
**Rôle :** Framework d'analyse dynamique de binaires qui simule un processeur virtuel pour surveiller chaque allocation et accès mémoire de votre programme sans recompilation.
**Syntaxe :** `valgrind [options] ./executable [args]`
**Cas réguliers :**
- `valgrind --leak-check=full ./app` — Exécuter le programme et afficher un rapport détaillé de toutes les fuites mémoire à la sortie
- `valgrind --tool=callgrind ./app` — Profiler les appels de fonctions (analysable ensuite avec KCachegrind)
- `valgrind --track-origins=yes ./app` — Tracer l'origine exacte des valeurs non initialisées utilisées
**Origine :** Julian Seward (2002) — récompensé par le prix ACM Software System Award.
**Subtilités/confusions :**
- Valgrind ralentit l'exécution de l'application de 10× à 50× (car il interprète le binaire sous forme d'instructions virtuelles).
**Urgences/dangers :** —
**Précautions :** Toujours compiler avec `-g` (symboles de débogage) et sans optimisations abusives (`-O0` ou `-O1`) pour des rapports lisibles.
**Équivalents :** AddressSanitizer (ASan), Heaptrack, Dr. Memory
**Voir aussi :** gdb, gcc, clang

## `strace` — Traçage des appels système (*syscalls*) [Linux]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** diagnostiquer pourquoi une application ne démarre pas, quel fichier de configuration manquant elle essaie d'ouvrir, ou pourquoi un processus est bloqué sur le réseau
**Rôle :** Diagnostiqueur et traceur d'appels système (*system calls*) et de signaux reçus par un processus Linux en temps réel.
**Syntaxe :** `strace [options] [commande]`
**Cas réguliers :**
- `strace -e openat ./app` — Intercepter et afficher uniquement les tentatives d'ouverture de fichiers
- `strace -p <pid>` — S'attacher à un processus en cours pour observer ses appels système en direct
- `strace -c ./app` — Générer un tableau récapitulatif du temps passé dans chaque appel système
**Origine :** Paul Kranenburg (1991) — outil de diagnostic fondamental de l'écosystème Linux.
**Subtilités/confusions :**
- `strace` filtre via `-e trace=network`, `-e trace=file`, `-e trace=process` pour réduire la quantité d'output.
**Urgences/dangers :** S'attacher à un processus très sollicité dégrade légèrement ses performances en raison du surcoût des interruptions `ptrace`.
**Précautions :** Rediriger la sortie avec `-o trace.log` car le volume de logs généré sur `stderr` peut être immense.
**Équivalents :** dtrace (macOS/Solaris), truss (BSD), procmon (Windows)
**Voir aussi :** ltrace, gdb, perf, lsof

## `ltrace` — Traçage des appels de bibliothèques dynamiques [Linux]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** intercepter les appels aux fonctions de bibliothèques partagées (`libc`, `openssl`, `libcurl`) effectuées par un programme utilisateur
**Rôle :** Outil de débogage dynamique qui affiche tous les appels de fonctions de bibliothèques dynamiques (`.so`) interceptés via la table de liaison PLT.
**Syntaxe :** `ltrace [options] [commande]`
**Cas réguliers :**
- `ltrace ./app` — Afficher tous les appels de bibliothèques exécutés par le programme (ex: `malloc`, `strcpy`, `printf`…)
- `ltrace -e malloc+free ./app` — Filtrer uniquement les allocations et libérations mémoire libc
- `ltrace -p <pid>` — S'attacher à un processus en cours
**Origine :** Juan Cespedes (1997).
**Subtilités/confusions :**
- `strace` intercepte les appels au noyau (`open`, `read`), alors que `ltrace` intercepte les appels aux fonctions C de l'espace utilisateur (`fopen`, `fread`).
**Urgences/dangers :** —
**Précautions :** Si le binaire est lié de manière statique (*statically linked*), `ltrace` ne verra aucun symbole de bibliothèque.
**Équivalents :** dtrace, latrace
**Voir aussi :** strace, gdb, ldd

## `perf` — Profiler de performance du noyau Linux [Linux]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** `perf_events`
**Contextes :** identifier les fonctions gourmandes en CPU (points chauds / *hotspots*), analyser les ratés de cache CPU (*cache misses*) et générer des Flamegraphs
**Rôle :** Outil de profilage de performance intégré au noyau Linux exploitant les compteurs matériels du processeur et les points de trace du noyau.
**Syntaxe :** `perf <subcommande> [options]`
**Cas réguliers :**
- `perf top` — Afficher les fonctions consommant le plus de CPU en temps réel (similaire à `top`, mais au niveau des fonctions du code !)
- `perf record -g ./app` — Enregistrer le profil d'exécution avec la pile d'appels pour analyse ultérieure
- `perf report` — Visualiser de manière interactive les résultats enregistrés par `perf record`
**Origine :** Ingo Molnar / noyau Linux (2009) — sous-système officiel du noyau Linux.
**Subtilités/confusions :**
- Nécessite souvent d'ajuster `sysctl kernel.perf_event_paranoid` ou de s'exécuter avec les privilèges root.
**Urgences/dangers :** —
**Précautions :** Compiler le code cible avec `-fno-omit-frame-pointer` pour obtenir des piles d'appels précises dans les Flamegraphs.
**Équivalents :** gprof, valgrind (callgrind), VTune (Intel)
**Voir aussi :** strace, valgrind, sysctl

## `hyperfine` — Outil de benchmarking CLI moderne [Cross]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** comparer scientifiquement les temps d'exécution de deux commandes ou scripts CLI (ex: `fd` vs `find`, `grep` vs `ripgrep`, `npm` vs `pnpm`)
**Rôle :** Outil de benchmark en ligne de commande moderne écrit en Rust, gérant le préchauffage du cache (*warmup*), l'analyse statistique et la détection d'anomalies.
**Syntaxe :** `hyperfine [options] <commande1> <commande2>...`
**Cas réguliers :**
- `hyperfine 'fd . /usr' 'find /usr'` — Comparer la vitesse de recherche de `fd` et `find`
- `hyperfine --warmup 3 'python3 script.py'` — Effectuer 3 exécutions de préchauffage du cache avant la mesure
- `hyperfine --export-json results.json 'make -j4' 'make -j8'` — Exporter les métriques au format JSON
**Origine :** David Peter « sharkdp » (2018) — créateur de `bat` et `fd`.
**Subtilités/confusions :**
- Calcule la moyenne, l'écart-type, le minimum et le maximum automatiquement sur plusieurs itérations.
**Urgences/dangers :** —
**Précautions :** Fermer les applications gourmandes en arrière-plan pendant la mesure pour éviter les biais de charge CPU.
**Équivalents :** time, bench
**Voir aussi :** time (bash), perf

## `webpack` — Bundler de modules JavaScript/Web [Cross]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** assembler des dépendances JavaScript/TypeScript, CSS et assets pour le navigateur web dans les applications Single Page (React, Vue, Angular)
**Rôle :** Bundler de modules statiques pour les applications JS modernes qui construit un graphe de dépendances et génère des paquets optimisés pour la production.
**Syntaxe :** `npx webpack [options]`
**Cas réguliers :**
- `npx webpack --mode production` — Compiler et minifier les paquets pour le déploiement en production
- `npx webpack serve` — Lancer le serveur de développement local avec rechargement à chaud (*Hot Module Replacement / HMR*)
**Origine :** Tobias Koppers (2012) — le bundler historique dominant de l'écosystème Node.js.
**Subtilités/confusions :**
- Très puissant mais réputé pour la complexité de son fichier de configuration `webpack.config.js`.
**Urgences/dangers :** —
**Précautions :** Utiliser la séparation de code (*code splitting*) via l'import dynamique pour éviter d'envoyer des bundles JS trop volumineux au navigateur.
**Équivalents :** vite, esbuild, rollup, rspack, parcel
**Voir aussi :** vite, esbuild, npm, pnpm

## `vite` — Bundler et serveur de dev web ultra-rapide [Cross]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** démarrer instantanément un serveur de développement pour React, Vue, Svelte ou TypeScript, builder pour la production avec Rollup/esbuild
**Rôle :** Outil de build frontend de nouvelle génération exploitant les ES Modules (ESM) natifs du navigateur pour un démarrage instantané en dev et Rollup/esbuild en prod.
**Syntaxe :** `npx vite [commande] [options]`
**Cas réguliers :**
- `npx vite` — Démarrer le serveur de dev ultra-rapide avec HMR instannée
- `npx vite build` — Générer les artefacts de production minifiés dans le dossier `dist/`
- `npx vite preview` — Prévisualiser en local le build de production généré
**Origine :** Evan You (créateur de Vue.js, 2020) — devenu le standard de fait de l'écosystème JS.
**Subtilités/confusions :**
- Ne re-bundler pas l'application entière en mode dev à chaque modification : seul le fichier modifié est transmis au navigateur via ESM natif.
**Urgences/dangers :** —
**Précautions :** Configurer `vite.config.js` pour gérer les variables d'environnement (préfixées par `VITE_` pour être accessibles côté client).
**Équivalents :** webpack, parcel, farm
**Voir aussi :** esbuild, webpack, pnpm, bun

## `esbuild` — Bundler JavaScript/TypeScript ultra-rapide en Go [Cross]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** —
**Contextes :** transpiler du TypeScript/JSX et bundler du JavaScript 10 à 100 fois plus vite que les outils JS traditionnels (Babel, Webpack)
**Rôle :** Bundler et minificateur JavaScript/TypeScript écrit en Go compilé en natif, conçu pour une vitesse de traitement extrême.
**Syntaxe :** `npx esbuild [options] fichier_entree`
**Cas réguliers :**
- `npx esbuild app.jsx --bundle --outfile=out.js` — Bundler un fichier JSX et ses dépendances en un fichier unique
- `npx esbuild app.ts --target=es2020 --minify --outfile=out.min.js` — Transpiler du TS et minifier
- `npx esbuild app.js --watch` — Mode écoute active avec re-compilation instantanée à chaque enregistrement
**Origine :** Evan Wallace (co-fondateur de Figma, 2020) — écrit en Go pour éviter le surcoût de la boucle d'événements et du garbage collector Node.js.
**Subtilités/confusions :**
- `esbuild` ne fait pas de vérification de types TypeScript (*type checking*) ; il supprime simplement les annotations de type (pour le checking, utiliser `tsc --noEmit`).
**Urgences/dangers :** —
**Précautions :** Intégré en sous-main comme moteur interne de Vite et d'autres frameworks modernes.
**Équivalents :** swc, webpack, rollup, rspack
**Voir aussi :** vite, swc, tsc

## `swc` — Compilateur JS/TS ultra-rapide écrit en Rust [Cross]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** transpiler et minifier du JavaScript/TypeScript à très grande vitesse dans des pipelines Next.js, Jest ou Webpack
**Rôle :** Compilateur extensible basé sur Rust capable de remplacer Babel pour la transpilation et Terser pour la minification (utilisé comme moteur principal de Next.js).
**Syntaxe :** `npx swc [options] fichier_source`
**Cas réguliers :**
- `npx swc script.ts -o script.js` — Transpiler un fichier TypeScript en JavaScript
- `npx swc src -d dist` — Transpiler tout un répertoire de sources
**Origine :** DongYoon Kang / Vercel (2018) — écrit en Rust pour offrir des performances maximales dans les builds Next.js.
**Subtilités/confusions :**
- Tout comme esbuild, SWC ne fait pas de contrôle de types TypeScript ; il se concentre sur la vitesse de transformation de la syntaxe.
**Urgences/dangers :** —
**Précautions :** Configurer `.swcrc` pour personnaliser les cibles ECMAScript et les plugins React (JSX transform).
**Équivalents :** babel, esbuild, tsc
**Voir aussi :** esbuild, tsc, vite

## `tsc` — Compilateur TypeScript officiel [Cross]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** vérifier la cohérence des types d'un projet TypeScript, générer les fichiers JavaScript correspondants ainsi que les définitions de types (`.d.ts`)
**Rôle :** Compilateur officiel distribué avec le paquet `typescript`, chargé de la vérification stricte du système de typage et de la transpilation vers JavaScript.
**Syntaxe :** `npx tsc [options]`
**Cas réguliers :**
- `npx tsc` — Compiler l'ensemble du projet en suivant les règles définies dans `tsconfig.json`
- `npx tsc --noEmit` — Effectuer uniquement la vérification des types sans générer de fichiers JavaScript (idéal en CI !)
- `npx tsc --watch` — Démarrer en mode observation pour ré-évaluer les types à chaque modification de fichier
**Origine :** Anders Hejlsberg / Microsoft (2012) — créateur du langage C# et de TypeScript.
**Subtilités/confusions :**
- Seul `tsc` garantit une vérification complète du graphe de types ; les transpileurs rapides (esbuild, SWC, Babel) ignorent la vérification des types.
**Urgences/dangers :** —
**Précautions :** Activer `"strict": true` dans le fichier `tsconfig.json` pour bénéficier de toute la protection contre les erreurs `null`/`undefined`.
**Équivalents :** swc, esbuild, babel
**Voir aussi :** esbuild, swc, pnpm

## `babel` — Transpileur JavaScript rétro-compatible [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** `babel-cli`
**Contextes :** convertir du code JavaScript moderne (ES6+, JSX, propositions récentes) en code compatible avec les anciennes versions des navigateurs web ou Node.js
**Rôle :** Transpileur source-à-source historique de l'écosystème JavaScript s'appuyant sur un vaste écosystème de plugins et de presets (`@babel/preset-env`).
**Syntaxe :** `npx babel <dossier_source> --out-dir <dossier_destination> [options]`
**Cas réguliers :**
- `npx babel src --out-dir lib` — Transpiler le répertoire `src/` vers `lib/`
- `npx babel script.js --out-file script-compiled.js` — Transpiler un fichier unique
**Origine :** Sebastian McKenzie (2014) — initialement appelé *6to5*.
**Subtilités/confusions :**
- Nécessite la présence d'un fichier de configuration `babel.config.json` ou `.babelrc` décrivant les presets et plugins à appliquer.
**Urgences/dangers :** —
**Précautions :** Pour les nouveaux projets, évaluer l'utilisation d'outils plus rapides comme SWC ou ESBuild sauf besoin spécifique d'un plugin Babel sur-mesure.
**Équivalents :** swc, esbuild, tsc
**Voir aussi :** swc, esbuild, webpack

## `tokei` — Compteur de lignes de code et statistiques de langage [Cross]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** —
**Contextes :** afficher rapidement un tableau récapitulatif du nombre de lignes de code, de commentaires et de lignes vides ventilées par langage dans un projet
**Rôle :** Outil CLI ultra-rapide écrit en Rust qui analyse un projet source et génère un rapport statistique détaillé sur le volume de code par langage.
**Syntaxe :** `tokei [options] [chemins]`
**Cas réguliers :**
- `tokei` — Analyser le répertoire courant et afficher les lignes de code par langage
- `tokei src/ --files` — Afficher les statistiques détaillées fichier par fichier
- `tokei -e target -e node_modules` — Exclure des répertoires volumineux
**Origine :** Xidorn Quan (2016) — écrit en Rust.
**Subtilités/confusions :**
- Plus de 100 fois plus rapide que les vieux outils en Perl comme `cloc`.
**Urgences/dangers :** —
**Précautions :** Idéal pour évaluer la taille et les langages prédominants d'un nouveau dépôt avant d'entamer une refactorisation.
**Équivalents :** scc, cloc, sloccount
**Voir aussi :** scc, git, hyperfine

## `ast-grep` — Recherche et refactoring de code basé sur l'AST (`sg`) [Cross]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** `sg`
**Contextes :** rechercher et remplacer des motifs de code complexes en comprenant la structure syntaxique (AST) au lieu d'utiliser de simples regex textuelles
**Rôle :** Outil de recherche et de réécriture de code structurel piloté par Tree-sitter, permettant de trouver et refactoriser du code dans 20+ langages.
**Syntaxe :** `ast-grep --pattern '<motif>' [options]`
**Cas réguliers :**
- `ast-grep --pattern 'console.log($A)'` — Trouver tous les appels à `console.log()` quel que soit l'argument `$A`
- `ast-grep --pattern 'if ($A == null)' --rewrite 'if ($A === null)'` — Remplacer l'égalité faible par l'égalité stricte en conservant la variable `$A`
**Origine :** Herrington Darkholme (2022) — écrit en Rust, basé sur les grammaires Tree-sitter.
**Subtilités/confusions :**
- `$A` est une métavariable qui capture n'importe quel nœud AST (expression, variable, fonction).
**Urgences/dangers :** —
**Précautions :** Tester les règles de remplacement avec `--interactive` avant d'appliquer les modifications en masse.
**Équivalents :** semgrep, comby, jscodeshift
**Voir aussi :** semgrep, grep, ripgrep

## `prettier` — Formateur de code opinionâtre multi-langages [Cross]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** harmoniser automatiquement le style de code (formatage, espaces, guillemets, point-virgules) dans un projet web ou multi-langages (JS, TS, HTML, CSS, JSON, Markdown, YAML)
**Rôle :** Formateur de code automatique qui réanalyse la syntaxe en AST et réimprime le code avec des règles de style strictes et cohérentes sans altérer la sémantique.
**Syntaxe :** `npx prettier [options] <fichiers>`
**Cas réguliers :**
- `npx prettier --write .` — Formater tous les fichiers pris en charge du projet en place
- `npx prettier --check "src/**/*.ts"` — Vérifier si les fichiers sont correctement formatés sans les modifier (idéal en CI)
**Origine :** James Long (2017) — inspiré de `gofmt` pour mettre fin aux débats de style dans les équipes web.
**Subtilités/confusions :**
- Prettier ne s'occupe QUE du style visuel (espaces, retours à la ligne) ; les erreurs de logique ou de variables non utilisées sont gérées par un linter comme `eslint`.
**Urgences/dangers :** —
**Précautions :** Définir un fichier `.prettierignore` pour exclure les répertoires de build (`dist/`, `node_modules/`, `.git/`).
**Équivalents :** ruff, black, clang-format, gofmt, biome
**Voir aussi :** eslint, ruff, black

## `eslint` — Linter statique pour JavaScript et TypeScript [Cross]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** —
**Contextes :** analyser le code source JavaScript/TypeScript à la recherche de bugs potentiels, de mauvaises pratiques, de variables inutilisées et d'incohérences
**Rôle :** Outil d'analyse statique configurable qui analyse l'AST de votre code pour repérer les erreurs de programmation et appliquer des règles de qualité.
**Syntaxe :** `npx eslint [options] <fichiers>`
**Cas réguliers :**
- `npx eslint src/` — Analyser tous les fichiers du dossier `src/` et afficher les avertissements/erreurs
- `npx eslint --fix src/` — Corriger automatiquement les erreurs qui peuvent l'être sans intervention humaine
- `npx eslint --init` — Répondre à un questionnaire interactif pour générer la configuration `eslint.config.js`
**Origine :** Nicholas C. Zakas (2013) — créé pour offrir un linter totalement modulaire et extensible par plugins.
**Subtilités/confusions :**
- Utiliser `@typescript-eslint` pour étendre ESLint au langage TypeScript.
**Urgences/dangers :** —
**Précautions :** Associer ESLint avec Prettier en désactivant les règles de formatage ESLint conflictuelles (`eslint-config-prettier`).
**Équivalents :** biome, oxlint, ruff (pour Python)
**Voir aussi :** prettier, tsc, swc

## `ruff` — Linter et formateur Python ultra-rapide en Rust [Cross]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** vérifier et formater du code Python 100 à 1000 fois plus vite que Flake8, Black, isort, pydocstyle et bandit réunis
**Rôle :** Linter et formateur de code Python d'une vitesse extrême réécrit en Rust par Astral, remplaçant une dizaine d'outils Python traditionnels.
**Syntaxe :** `ruff <subcommande> [options] [chemins]`
**Cas réguliers :**
- `ruff check .` — Analyser tout le projet Python et afficher les violations de règles
- `ruff check --fix .` — Corriger automatiquement les problèmes détectés (imports non utilisés, variables inutiles…)
- `ruff format .` — Formater l'ensemble des fichiers Python (remplacement direct et compatible avec `black`)
**Origine :** Charlie Marsh / Astral (2022) — devenu l'outil de linting standard adopté par la majorité des grands projets Python (FastAPI, Pandas, SciPy).
**Subtilités/confusions :**
- `ruff check` remplace Flake8/isort ; `ruff format` remplace Black.
**Urgences/dangers :** —
**Précautions :** Configurer les règles dans `pyproject.toml` sous la section `[tool.ruff]`.
**Équivalents :** flake8, black, isort, pylint, mypy
**Voir aussi :** uv, black, prettier

## `black` — Formateur de code Python intransigeant [Cross]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** formater automatiquement du code Python selon une norme stricte et déterministe pour éliminer toute discussion sur le style lors des revues de code
**Rôle :** Formateur de code Python auto-proclamé « intransigeant » (*uncompromising*) qui reformate l'intégralité du code selon une norme unique et non configurable.
**Syntaxe :** `black [options] <fichiers_ou_dossiers>`
**Cas réguliers :**
- `black .` — Formater tous les fichiers `.py` du répertoire courant
- `black --check .` — Vérifier si des fichiers ont besoin d'être formatés sans appliquer les modifications (pour la CI)
- `black --diff .` — Afficher le diff des modifications qui seraient appliquées par Black
**Origine :** Łukasz Langa (2018) — projet officiel hébergé sous l'organisation Python Software Foundation (PSF).
**Subtilités/confusions :**
- Black ne propose volontairement que très peu d'options de configuration (longueur de ligne maximale par défaut : 88 caractères).
**Urgences/dangers :** —
**Précautions :** Utiliser `black --check` dans les hooks de pré-commit et les pipelines de CI.
**Équivalents :** ruff format, yapf, autopep8
**Voir aussi :** ruff, prettier, uv

## `clang-format` — Formateur de code C, C++, Java, JS et C# [Cross]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** appliquer une règle de style de code unifiée (Google, LLVM, Mozilla, Chromium, GNU) à des fichiers source C, C++, Java, JavaScript ou Proto
**Rôle :** Outil de formatage automatique de code source basé sur le parseur Clang/LLVM, garantissant une mise en page parfaite selon un fichier `.clang-format`.
**Syntaxe :** `clang-format [options] <fichier>`
**Cas réguliers :**
- `clang-format -i main.cpp` — Formater le fichier `main.cpp` en place (`-i` pour in-place)
- `clang-format -style=Google main.cpp` — Afficher le fichier formaté selon le style de code Google
- `clang-format -style=llvm -dump-config > .clang-format` — Générer un fichier de configuration exemple basé sur le style LLVM
**Origine :** Projet LLVM (2012).
**Subtilités/confusions :**
- L'option `-i` modifie directement le fichier sur le disque sans demander de confirmation.
**Urgences/dangers :** —
**Précautions :** Placer le fichier de configuration `.clang-format` à la racine de votre dépôt Git pour que tous les développeurs et l'IDE utilisent les mêmes règles.
**Équivalents :** unrust, astyle, prettier
**Voir aussi :** clang, clang-tidy, gcc

## `clang-tidy` — Analyseur statique et linter C/C++ [Cross]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** détecter des erreurs de logique, des fuites de mémoire, des violations de règles C++ Core Guidelines et moderniser du code C++ ancien
**Rôle :** Outil d'analyse statique avancé basé sur Clang qui propose des diagnostics et des refactorisations automatiques (*modernize-use-auto*, *bugprone-*).
**Syntaxe :** `clang-tidy <fichier.cpp> -- [options_compilation]`
**Cas réguliers :**
- `clang-tidy main.cpp -- -std=c++20` — Analyser un fichier C++ avec les règles par défaut
- `clang-tidy -checks='*,-abseil-*' main.cpp -- -Iinclude` — Activer toutes les vérifications sauf celles spécifiques à Abseil
- `clang-tidy -fix main.cpp -- -std=c++17` — Appliquer automatiquement les corrections suggérées par le linter !
**Origine :** Projet LLVM (2014).
**Subtilités/confusions :**
- Nécessite de connaître les drapeaux de compilation de votre projet (souvent fourni automatiquement via un fichier `compile_commands.json` généré par CMake via `cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`).
**Urgences/dangers :** L'option `-fix` modifie le code source ; vérifier le `git diff` après exécution.
**Précautions :** Utiliser `clang-tidy` conjointement avec `compile_commands.json` pour des projets de grande taille.
**Équivalents :** cppcheck, flawfinder, infer (Meta)
**Voir aussi :** clang, clang-format, cmake

## `doxygen` — Générateur de documentation pour C/C++/Java [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** générer automatiquement une documentation HTML/PDF/LaTeX complète avec diagrammes de classes à partir des commentaires structurés du code source
**Rôle :** Standard de fait pour la génération de documentation technique des projets C, C++, Java, Python, Objective-C et C#.
**Syntaxe :** `doxygen [fichier_config]`
**Cas réguliers :**
- `doxygen -g Doxyfile` — Générer un fichier de configuration modèle nommé `Doxyfile`
- `doxygen Doxyfile` — Générer la documentation du projet selon les paramètres du `Doxyfile`
**Origine :** Dimitri van Heesch (1997) — créé pour offrir l'équivalent de Javadoc pour C++.
**Subtilités/confusions :**
- Utilise les blocs de commentaires avec double astérisque (`/** ... */`) ou triple slash (`/// ...`) et les balises `@param`, `@return`, `@brief`.
**Urgences/dangers :** —
**Précautions :** Si `graphviz` (commande `dot`) est installé sur la machine, Doxygen génère de magnifiques diagrammes d'héritage et d'appels de fonctions.
**Équivalents :** sphinx-build, javadoc, rustdoc
**Voir aussi :** sphinx-build, gcc, cmake

## `sphinx-build` — Générateur de documentation technique [Cross]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** `sphinx`
**Contextes :** générer des sites de documentation d'une qualité professionnelle (HTML, PDF, Read-the-Docs) à partir de fichiers reStructuredText ou Markdown
**Rôle :** Outil de génération de documentation du projet Python, largement utilisé pour documenter des projets open source dans tous les langages (Linux kernel, Python, OpenCV).
**Syntaxe :** `sphinx-build [options] <dossier_source> <dossier_sortie>`
**Cas réguliers :**
- `sphinx-build -b html docs/source docs/build/html` — Compiler la documentation source en site web HTML statique
- `sphinx-quickstart` — Assistant interactif pour créer l'arborescence initiale de documentation Sphinx
**Origine :** Georg Brandl / Python Software Foundation (2008) — conçu à l'origine pour documenter le langage Python lui-même.
**Subtilités/confusions :**
- Utilise par défaut le format `reStructuredText` (`.rst`), mais supporte le Markdown grâce à l'extension `myst-parser`.
**Urgences/dangers :** —
**Précautions :** Héberger gratuitement la documentation générée par Sphinx sur le service *Read the Docs* (`readthedocs.org`).
**Équivalents :** mkdocs, doxygen, jekyll
**Voir aussi :** mkdocs, doxygen, python3

## `yq` — Processeur YAML, JSON et XML en ligne de commande [Cross]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** extraire, modifier ou convertir des valeurs dans des fichiers de configuration YAML (Kubernetes manifests, Docker Compose, Ansible, CI/CD) en CLI
**Rôle :** Wrapper et équivalent de `jq` adapté au format YAML, permettant la manipulation de données structurées YAML, JSON et XML en ligne de commande.
**Syntaxe :** `yq '<expression>' <fichier.yaml>`
**Cas réguliers :**
- `yq '.metadata.name' deployment.yaml` — Extraire la valeur de la clé `metadata.name` d'un fichier YAML Kubernetes
- `yq eval '.spec.replicas = 5' -i deployment.yaml` — Modifier la valeur d'une clé directement dans le fichier (`-i` / in-place)
- `yq -o=json config.yaml` — Convertir un fichier YAML au format JSON
**Origine :** Mike Farah (version Go, 2017) / Andrey Kislyuk (version Python).
**Subtilités/confusions :**
- La version Go de Mike Farah (la plus populaire) possède une syntaxe d'expression très proche de `jq`.
**Urgences/dangers :** —
**Précautions :** L'option `-i` écrase le fichier source ; s'assurer que le fichier est sous contrôle de version Git avant modification.
**Équivalents :** jq, fx, dasel
**Voir aussi :** jq, fx, pup, sops

## `fx` — Visualiseur JSON interactif et processeur en CLI [Cross]
**Niveau :** debutant | **Popularité :** 85 | **Aliases :** —
**Contextes :** explorer visuellement de très gros fichiers JSON dans son terminal avec pliage/dépliage de nœuds, effectuer des requêtes avec du code JavaScript natif
**Rôle :** Outil TUI (Terminal User Interface) et CLI interactif pour la visualisation et la manipulation de données JSON.
**Syntaxe :** `fx [fichier.json]` ou `cat data.json | fx`
**Cas réguliers :**
- `fx data.json` — Ouvrir une interface TUI interactive permettant de naviguer dans l'arbre JSON avec les flèches du clavier
- `curl https://api.exemple.com/data | fx '.items.map(x => x.name)'` — Appliquer une fonction JavaScript anonyme sur la sortie JSON
**Origine :** Anton Medvedev (2018) — écrit en Go avec un moteur d'évaluation JavaScript léger.
**Subtilités/confusions :**
- Permet d'utiliser la syntaxe et les méthodes JavaScript standards (`.filter()`, `.map()`, `.find()`) directement en ligne de commande.
**Urgences/dangers :** —
**Précautions :** Idéal pour explorer des réponses d'API complexes avant de scripter avec `jq`.
**Équivalents :** jq, jless, yq
**Voir aussi :** jq, yq, curl

## `pup` — Processeur et sélecteur HTML en ligne de commande [Cross]
**Niveau :** intermediaire | **Popularité :** 81 | **Aliases :** —
**Contextes :** parser et extraire des éléments spécifiques d'une page web HTML brute (scraping léger) en utilisant des sélecteurs CSS depuis le terminal
**Rôle :** Outil CLI inspiré de `jq` qui lit du code HTML sur la sortie standard et filtre les éléments en utilisant des sélecteurs CSS (ex: `table.data td`).
**Syntaxe :** `curl -s <url> | pup '<sélecteur_css> [filtre]'`
**Cas réguliers :**
- `curl -s https://news.ycombinator.com | pup 'title text{}'` — Extraire le contenu texte de la balise `<title>` d'une page
- `curl -s https://exemple.com | pup 'a.link attr{href}'` — Récupérer toutes les URLs des liens répondant à la classe `a.link`
- `curl -s https://exemple.com | pup 'table.stats json{}'` — Convertir un tableau HTML en un objet JSON structuré !
**Origine :** Eric Chiang (2014) — écrit en Go.
**Subtilités/confusions :**
- Fonctionne avec des sélecteurs CSS standards (`div#id`, `a.class`, `h1 + p`), ce qui le rend très intuitif pour les développeurs web.
**Urgences/dangers :** —
**Précautions :** Combiner `curl`, `pup` et `jq` pour construire des scripts de scraping puissants sans installer de navigateur headless.
**Équivalents :** htmlq, xpath, xq
**Voir aussi :** curl, jq, yq

## `grpcurl` — Outil CLI d'interaction avec des serveurs gRPC [Cross]
**Niveau :** intermediaire | **Popularité :** 87 | **Aliases :** —
**Contextes :** tester des endpoints d'API gRPC (Protobuf), inspecter la réflexion de services gRPC et exécuter des requêtes RPC directement depuis le terminal
**Rôle :** Équivalent de `curl` pour le protocole gRPC, permettant de lister les services exposés et d'envoyer des messages JSON convertis en Protobuf.
**Syntaxe :** `grpcurl [options] <serveur:port> <service/methode>`
**Cas réguliers :**
- `grpcurl -plaintext localhost:50051 list` — Lister tous les services gRPC exposés par le serveur local (sans TLS)
- `grpcurl -plaintext localhost:50051 describe MonService` — Inspecter les méthodes et structures Protobuf d'un service
- `grpcurl -plaintext -d '{"id": 42}' localhost:50051 MonService.GetUser` — Exécuter la méthode `GetUser` en passant un payload JSON
**Origine :** FullStory (2017) — écrit en Go.
**Subtilités/confusions :**
- Si le serveur gRPC n'active pas le service de réflexion (*Server Reflection*), vous devez fournir le fichier `.proto` via l'option `-proto`.
**Urgences/dangers :** —
**Précautions :** Utiliser `-plaintext` uniquement en développement local HTTP non sécurisé.
**Équivalents :** evans, grpc-cli
**Voir aussi :** curl, protobuf (protoc), httpie

## `newman` — Runner de collections Postman en ligne de commande [Cross]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** exécuter automatiquement des suites de tests d'API REST/GraphQL exportées depuis Postman dans un pipeline CI/CD
**Rôle :** Exécuteur de collections Postman en CLI qui permet de lancer des tests d'API automatisés sans ouvrir l'interface graphique Postman.
**Syntaxe :** `newman run <collection.json> [options]`
**Cas réguliers :**
- `newman run ma_collection.json` — Lancer tous les tests d'une collection d'API Postman
- `newman run collection.json -e environnement.json` — Exécuter les tests en injectant un fichier de variables d'environnement Postman
- `newman run collection.json -r cli,html` — Générer un rapport d'exécution au format HTML
**Origine :** Postman Inc. (2014) — nommé en hommage au personnage de la série Seinfeld.
**Subtilités/confusions :**
- Permet d'intégrer des tests fonctionnels d'API créés visuellement par des développeurs dans des pipelines GitHub Actions ou GitLab CI.
**Urgences/dangers :** —
**Précautions :** Ne pas commiter de fichiers d'environnement Postman contenant des clés d'API ou tokens réels en clair.
**Équivalents :** hurl, Bruno CLI, k6
**Voir aussi :** hurl, curl, httpie

## `hurl` — Outil CLI de test d'API HTTP basé sur du texte brut [Cross]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** décrire et exécuter des scénarios de test d'API HTTP complexes (requêtes en chaîne, captures de variables, assertions sur le status et le JSON)
**Rôle :** Outil CLI basé sur `libcurl` et écrit en Rust qui exécute des fichiers de tests HTTP écrits dans un format texte très simple et lisible (`.hurl`).
**Syntaxe :** `hurl [options] test.hurl`
**Cas réguliers :**
- `hurl --test test.hurl` — Exécuter le fichier de test HTTP et vérifier toutes les assertions (status code, corps JSON, en-têtes)
- `hurl --variable token=XYZ login.hurl` — Passer des variables dynamiques lors de l'exécution du test
**Origine :** Orange / Fabrice Bellard & contribs (2020) — conçu pour offrir une alternative légère, rapide et orientée Git à Postman.
**Subtilités/confusions :**
- Format `.hurl` extrêmement lisible permettant d'enchaîner les requêtes (ex: capturer le token JWT de la réponse 1 pour l'injecter dans la requête 2).
**Urgences/dangers :** —
**Précautions :** Intégrer la commande `hurl --test *.hurl` directement dans vos tests d'intégration CI/CD.
**Équivalents :** newman, Bruno CLI, httpie
**Voir aussi :** curl, httpie, newman

## `mkdocs` — Générateur de sites de documentation static en Markdown [Cross]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** créer un site web de documentation d'une élégance exceptionnelle à partir de simples fichiers Markdown, héberger sur GitHub Pages
**Rôle :** Générateur de site statique rapide et ultra-simple écrit en Python, particulièrement populaire grâce à son thème d'une grande beauté `mkdocs-material`.
**Syntaxe :** `mkdocs <commande> [options]`
**Cas réguliers :**
- `mkdocs serve` — Démarrer le serveur de prévisualisation local avec rechargement automatique en temps réel à chaque modification Markdown
- `mkdocs build` — Générer les fichiers HTML/CSS/JS statiques dans le dossier `site/`
- `mkdocs gh-deploy` — Déployer automatiquement le site de documentation sur la branche `gh-pages` de votre dépôt GitHub !
**Origine :** Dougal Matthews (2014) — conçu pour être l'outil de documentation le plus simple d'emploi.
**Subtilités/confusions :**
- Toute la structure du site est pilotée par un fichier YAML central simple nommé `mkdocs.yml`.
**Urgences/dangers :** —
**Précautions :** Installer le paquet `mkdocs-material` (`pip install mkdocs-material`) pour bénéficier du thème moderne responsive avec mode sombre.
**Équivalents :** sphinx-build, docusaurus, vuepress, astro
**Voir aussi :** sphinx-build, python3

## `protoc` — Compilateur Protocol Buffers (gRPC) [Cross]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** —
**Contextes :** générer du code source fortement typé (C++, Java, Python, Go, TypeScript) à partir de fichiers de définition `.proto` pour les communications gRPC
**Rôle :** Compilateur officiel de Google pour les schémas de sérialisation binaire Protocol Buffers.
**Syntaxe :** `protoc [options] --<lang>_out=<dossier_sortie> fichier.proto`
**Cas réguliers :**
- `protoc --go_out=. --go-grpc_out=. service.proto` — Générer les structures et stubs de service gRPC pour le langage Go
- `protoc --python_out=src/ service.proto` — Générer les liaisons Python à partir du schéma
- `protoc --descriptor_set_out=bundle.pb service.proto` — Générer un fichier binaire de descripteurs de schémas pour grpcurl
**Origine :** Google (2008) — format de sérialisation binaire interne de Google rendu open source.
**Subtilités/confusions :**
- Nécessite d'installer les plugins de langage spécifiques (ex: `protoc-gen-go`, `protoc-gen-grpc-web`) dans votre PATH pour chaque langage cible.
**Urgences/dangers :** —
**Précautions :** Respecter les règles de compatibilité descendante des numéros de champs Protobuf (ne jamais réorganiser ni supprimer un numéro de champ existant).
**Équivalents :** flatc (FlatBuffers), thrift
**Voir aussi :** grpcurl, gcc, cmake

## `flatc` — Compilateur FlatBuffers pour sérialisation à accès direct [Cross]
**Niveau :** avance | **Popularité :** 83 | **Aliases :** —
**Contextes :** sérialiser des données binaires haute performance pour les jeux vidéo, les systèmes temps réel ou le Machine Learning sans surcoût de parsing
**Rôle :** Compilateur de schémas FlatBuffers qui génère du code source C++, Java, C#, Go, Python ou Rust permettant d'accéder aux données sérialisées directement depuis la mémoire sans étape de dépaquetage.
**Syntaxe :** `flatc [options] --<lang> schema.fbs`
**Cas réguliers :**
- `flatc --cpp schema.fbs` — Générer les en-têtes C++ à partir d'un schéma FlatBuffers
- `flatc -b schema.fbs data.json` — Convertir un fichier JSON de test en binaire FlatBuffers `.mon`
**Origine :** Wouter van Oortmerssen / Google (2014) — créé pour les besoins de performance extrême dans le développement de jeux vidéo (Android/OpenXR).
**Subtilités/confusions :**
- Contrairement à Protobuf ou JSON, FlatBuffers ne nécessite pas d'allouer de la mémoire ou d'analyser le buffer avant de lire une valeur.
**Urgences/dangers :** —
**Précautions :** Utiliser FlatBuffers lorsque la vitesse d'accès et la mémoire sont des facteurs critiques strictes.
**Équivalents :** protoc, capnproto
**Voir aussi :** protoc, gcc

## `graphql-codegen` — Générateur de code typé pour GraphQL [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** générer automatiquement des types TypeScript, des hooks React (Apollo, TanStack Query) ou des classes Java à partir de vos schémas et requêtes GraphQL
**Rôle :** Outil CLI qui analyse vos documents de requêtes et votre schéma GraphQL pour générer du code 100% typé à zéro maintenance manuelle.
**Syntaxe :** `npx graphql-codegen [options]`
**Cas réguliers :**
- `npx graphql-codegen --config codegen.ts` — Générer tout le code typé du projet selon la configuration `codegen.ts`
- `npx graphql-codegen --watch` — Générer automatiquement à chaque modification d'un fichier `.graphql`
**Origine :** Dotan Simha / The Guild (2016) — l'outil de référence de l'écosystème GraphQL.
**Subtilités/confusions :**
- Élimine totalement le besoin de définir manuellement les interfaces de réponses API dans le code frontend.
**Urgences/dangers :** —
**Précautions :** Exécuter le codegen dans vos pipelines CI pour garantir que les types frontend sont toujours synchronisés avec le serveur GraphQL.
**Équivalents :** openapi-generator-cli, apollo codegen
**Voir aussi :** tsc, prettier, eslint

## `openapi-generator-cli` — Générateur de SDKs et clients API OpenAPI [Cross]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** générer automatiquement des bibliothèques clientes (SDKs) dans plus de 50 langages (TypeScript, Python, Go, Java, Swift…) ou des stubs de serveur à partir d'une spécification OpenAPI/Swagger
**Rôle :** Générateur de code multi-langages puissant basé sur la spécification OpenAPI (v2, v3.0, v3.1).
**Syntaxe :** `npx @openapitools/openapi-generator-cli generate -i <spec.yaml> -g <langage> -o <dossier_sortie>`
**Cas réguliers :**
- `npx @openapitools/openapi-generator-cli generate -i api.yaml -g typescript-axios -o src/api` — Générer un client API TypeScript basé sur Axios
- `npx @openapitools/openapi-generator-cli generate -i api.yaml -g python -o sdk_python` — Générer un SDK Python complet avec documentation
**Origine :** Projet communautaire OpenAPITools (2018) — fork open source d'un project Swagger Codegen original.
**Subtilités/confusions :**
- Évite d'écrire à la main des milliers de lignes de code de sérialisation et d'appels d'API HTTP dans vos applications.
**Urgences/dangers :** —
**Précautions :** Ne pas modifier manuellement les fichiers générés dans le dossier de sortie : toujours régénérer via la spécification OpenAPI.
**Équivalents :** swagger-codegen, stainless, openapi-typescript
**Voir aussi :** curl, hurl, tsc

## `structurizr-cli` — Générateur de diagrammes d'architecture C4 [Cross]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** modéliser l'architecture d'un système logiciel sous forme de code (*Architecture as Code*) selon le modèle C4 (Context, Container, Component, Code)
**Rôle :** Outil en ligne de commande permettant de valider et d'exporter des modèles d'architecture décrits en langage Structurizr DSL vers PlantUML, Mermaid ou DOT.
**Syntaxe :** `structurizr-cli <subcommande> [options]`
**Cas réguliers :**
- `structurizr-cli export -w workspace.dsl -f mermaid` — Exporter un modèle d'architecture DSL au format diagramme Mermaid
- `structurizr-cli validate -w workspace.dsl` — Valider la syntaxe et les dépendances du modèle d'architecture
**Origine :** Simon Brown (2020) — créateur du célèbre modèle de visualisation d'architecture C4 Model.
**Subtilités/confusions :**
- Sépare la **modélisation** du système de la **représentation visuelle** (les diagrammes sont générés automatiquement sans dessiner de boîtes à la main).
**Urgences/dangers :** —
**Précautions :** Commiter les fichiers `.dsl` dans Git aux côtés du code source de l'application pour maintenir la documentation d'architecture à jour.
**Équivalents :** plantuml, mermaid-cli, c4builder
**Voir aussi :** plantuml, mermaid-cli, graphviz

## `plantuml` — Générateur de diagrammes UML à partir de texte [Cross]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** créer des diagrammes de séquence, de classes, de composants ou de cas d'usage à partir de descriptions textuelles lisibles
**Rôle :** Outil de génération de diagrammes de référence convertissant un langage de balisage texte simple en images PNG, SVG ou PDF.
**Syntaxe :** `plantuml [options] diagramme.puml`
**Cas réguliers :**
- `plantuml diagramme.puml` — Générer une image PNG du diagramme
- `plantuml -tsvg diagramme.puml` — Générer le diagramme au format vectoriel SVG
- `plantuml -gui` — Lancer l'interface graphique interactive d'édition et de prévisualisation
**Origine :** Arnaud Roques (2009) — écrit en Java.
**Subtilités/confusions :**
- Nécessite Java (JRE) et optionnellement Graphviz (`dot`) pour la disposition automatique de certains diagrammes complexes.
**Urgences/dangers :** —
**Précautions :** Intégrer les diagrammes PlantUML dans vos fichiers Markdown grâce aux extensions Sphinx ou MkDocs.
**Équivalents :** mermaid-cli, graphviz, d2
**Voir aussi :** graphviz, structurizr-cli, java

## `mermaid-cli` — Générateur CLI de diagrammes Mermaid (`mmdc`) [Cross]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** `mmdc`
**Contextes :** convertir des diagrammes Mermaid (séquence, flowchart, Gantt, ERD, Git graph) en images SVG/PNG dans des scripts automatiques ou des pipelines CI
**Rôle :** Interface en ligne de commande officielle (`mmdc`) basée sur Node.js et Puppeteer pour rendre des fichiers texte `.mmd` en images.
**Syntaxe :** `mmdc -i input.mmd -o output.png [options]`
**Cas réguliers :**
- `mmdc -i diagramme.mmd -o diagramme.svg` — Générer un fichier SVG vectoriel à partir du code Mermaid
- `mmdc -i diagramme.mmd -o diagramme.png -t dark` — Générer une image PNG avec le thème sombre
**Origine :** Knut Sveidqvist / Projet Mermaid (2015) — devenu le standard de fait de rendu de diagrammes dans GitHub Markdown.
**Subtilités/confusions :**
- La syntaxe Mermaid est rendue nativement par l'interface GitHub/GitLab, mais `mmdc` est nécessaire si vous devez générer des artefacts PNG/PDF pour des rapports imprimables.
**Urgences/dangers :** —
**Précautions :** Nécessite Node.js et un navigateur Chromium headless (géré par Puppeteer) pour l'étape de rendu.
**Équivalents :** plantuml, graphviz, d2
**Voir aussi :** plantuml, structurizr-cli, graphviz

## `graphviz` — Outil de disposition et tracé de graphes (`dot`) [Cross]
**Niveau :** avance | **Popularité :** 94 | **Aliases :** `dot`, `neato`
**Contextes :** visualiser automatiquement des structures de données complexes (arbres, graphes orientés, dépendances de paquets, graphes d'appels de fonctions)
**Rôle :** Suite logicielle d'agencement automatique de graphes décrits en langage texte DOT.
**Syntaxe :** `dot -T<format> graphe.dot -o image.<format>`
**Cas réguliers :**
- `dot -Tpng graph.dot -o graph.png` — Générer une image PNG à partir d'un fichier de description de graphe orienté en syntaxe DOT
- `dot -Tsvg graph.dot -o graph.svg` — Exporter au format SVG
- `neato -Tpng graph.dot -o graph.png` — Utiliser l'algorithme de disposition non orientée par modèle de ressorts
**Origine :** AT&T Labs Research (1991) — l'un des plus anciens et puissants moteurs de rendu de graphes au monde.
**Subtilités/confusions :**
- `dot` est la commande pour les graphes orientés hiérarchiques ; `neato`, `fdp` et `circo` sont d'autres moteurs inclus dans le paquet Graphviz pour des dispositions circulaires ou en réseaux.
**Urgences/dangers :** —
**Précautions :** Composant requis par Doxygen, Valgrind/Callgrind et de nombreux autres outils pour générer leurs visuels.
**Équivalents :** plantuml, mermaid-cli
**Voir aussi :** doxygen, plantuml, valgrind

## `semgrep` — Analyseur statique de code basé sur des motifs sémantiques [Cross]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** rechercher des failles de sécurité (SAST), des violations de secrets ou des anti-patterns dans le code source (30+ langages) avec une syntaxe proche du code lui-même
**Rôle :** Moteur d'analyse statique rapide et open source qui permet d'écrire des règles de sécurité sur-mesure en utilisant la syntaxe naturelle du langage analysé.
**Syntaxe :** `semgrep scan [options] --config <regles> [chemin]`
**Cas réguliers :**
- `semgrep scan --config auto` — Lancer une analyse de sécurité avec les règles communautaires recommandées
- `semgrep -e 'exec("...")' --lang python .` — Chercher toutes les exécutions de la fonction dangereuse `exec()` dans du code Python
- `semgrep scan --config p/ci .` — Lancer le jeu de règles optimisé pour les pipelines d'intégration continue
**Origine :** Yoann Padioleau / r2c (now Semgrep Inc., 2020) — inspiré par l'outil `coccinelle`.
**Subtilités/confusions :**
- Contrairement aux regex ordinaires (grep), `semgrep` comprend la structure syntaxique (AST) : il ignore les commentaires et les espaces et comprend l'équivalence des variables.
**Urgences/dangers :** —
**Précautions :** Exécuter dans les workflows GitHub Actions pour bloquer l'introduction de failles de sécurité avant le merge.
**Équivalents :** SonarQube, CodeQL, Snyk
**Voir aussi :** trivy, syft, ruff

## `trivy` — Scanner de vulnérabilités pour conteneurs et code [Cross]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** auditer la sécurité d'une image Docker, d'un système de fichiers, d'un dépôt Git, d'un cluster Kubernetes ou d'un fichier de dépendances (SCA)
**Rôle :** Outil de sécurité tout-en-un réputé pour sa simplicité et sa précision, détectant les vulnérabilités majeures (CVE), erreurs de configuration (IaC) et fuites de secrets.
**Syntaxe :** `trivy <cible> [options] <nom>`
**Cas réguliers :**
- `trivy image mon-app:latest` — Scanner une image conteneur Docker à la recherche de CVE connues
- `trivy fs .` — Scanner le système de fichiers du projet courant (dépendances et erreurs de config IaC)
- `trivy k8s --report summary cluster` — Générer un rapport de sécurité global d'un cluster Kubernetes
**Origine :** Teppei Fukuda / Aqua Security (2019) — rapidement devenu le scanner de conteneurs open source de référence.
**Subtilités/confusions :**
- Met à jour automatiquement sa base de données de vulnérabilités CVE au démarrage de chaque scan.
**Urgences/dangers :** —
**Précautions :** Utiliser `--severity HIGH,CRITICAL` pour ne faire échouer le pipeline CI qu'en présence de vulnérabilités sévères.
**Équivalents :** grype, clair, snyk, docker scout
**Voir aussi :** grype, syft, cosign, docker

## `syft` — Générateur de Software Bill of Materials (SBOM) [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** générer un inventaire complet et normalisé des logiciels et dépendances (SBOM) d'une image Docker ou d'un répertoire pour la conformité et la sécurité
**Rôle :** Outil open source développé par Anchore permettant de cataloguer les paquets système (dpkg, rpm, apk) et applicatifs (npm, PyPI, Cargo, Go) dans une image conteneur ou un projet.
**Syntaxe :** `syft [cible] [options]`
**Cas réguliers :**
- `syft mon-image:latest` — Générer un tableau récapitulatif de toutes les dépendances présentes dans l'image conteneur
- `syft mon-image:latest -o spdx-json > sbom.spdx.json` — Exporter le SBOM au format standardisé ISO SPDX JSON
- `syft dir:. -o cyclonedx-json > sbom.json` — Exporter au format standardisé CycloneDX
**Origine :** Anchore (2020) — créé pour répondre aux exigences réglementaires de sécurité de la chaîne d'approvisionnement logicielle (*Software Supply Chain Security*).
**Subtilités/confusions :**
- `syft` génère l'inventaire des composants (le SBOM) ; `grype` prend ce SBOM pour y rechercher les vulnérabilités CVE correspondantes.
**Urgences/dangers :** —
**Précautions :** Archiver les fichiers SBOM générés lors de chaque release logicielle pour la traçabilité légale.
**Équivalents :** cdxgen, spdx-tools
**Voir aussi :** grype, trivy, cosign

## `grype` — Scanner de vulnérabilités basé sur SBOM et conteneurs [Cross]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** analyser un SBOM généré par Syft ou scanner directement une image Docker pour identifier les vulnérabilités CVE de la chaîne d'approvisionnement
**Rôle :** Outil de détection de vulnérabilités de la suite Anchore, conçu pour s'appairer parfaitement avec `syft`.
**Syntaxe :** `grype [cible] [options]`
**Cas réguliers :**
- `grype mon-image:latest` — Scanner une image Docker et lister toutes les vulnérabilités CVE trouvées
- `grype sbom:sbom.spdx.json` — Analyser un fichier SBOM pré-généré sans ré-analyser l'image conteneur !
- `grype mon-image:latest --fail-on critical` — Retourner un code de sortie d'erreur (1) si au moins une CVE critique est présente
**Origine :** Anchore (2020).
**Subtilités/confusions :**
- Scanner un SBOM pré-généré avec Grype prend une fraction de seconde, ce qui est idéal pour surveiller en continu des milliers d'images sans les re-télécharger.
**Urgences/dangers :** —
**Précautions :** Exécuter `grype db update` pour mettre à jour la base locale de CVE.
**Équivalents :** trivy, snyk, clair
**Voir aussi :** syft, trivy, cosign

## `cosign` — Signature binaire et vérification d'images conteneur [Cross]
**Niveau :** avance | **Popularité :** 88 | **Aliases :** —
**Contextes :** signer numériquement des images conteneur Docker dans un registre (OCI) et vérifier leur authenticité dans Kubernetes avant déploiement
**Rôle :** Outil de signature de la fondation OpenSSF (projet Sigstore) permettant la signature sans gestion de clé lourde (*Keyless signing*) grâce à OIDC (GitHub, Google, Microsoft).
**Syntaxe :** `cosign <commande> [options]`
**Cas réguliers :**
- `cosign generate-key-pair` — Générer une paire de clés publique/privée pour la signature
- `cosign sign --key cosign.key mon-registre.com/mon-app:v1.0` — Signer une image conteneur dans un registre
- `cosign verify --key cosign.pub mon-registre.com/mon-app:v1.0` — Vérifier la signature d'une image avant son exécution
**Origine :** Projet Sigstore / OpenSSF (2021) — soutenu par Google, Red Hat et Chainguard pour sécuriser la Software Supply Chain.
**Subtilités/confusions :**
- Stocke les signatures directement sous forme d'artefacts dans le registre OCI à côté de l'image elle-même.
**Urgences/dangers :** —
**Précautions :** Configurer un contrôleur d'admission dans Kubernetes (ex: Kyverno ou Conftest) pour interdire tout conteneur non signé par Cosign.
**Équivalents :** notary (Docker Trust)
**Voir aussi :** trivy, syft, gpg

## `direnv` — Chargeur dynamique d'environnement shell par dossier [Linux/macOS]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** charger et décharger automatiquement des variables d'environnement spécifiques (`.envrc`) dès que l'on entre ou sort d'un répertoire dans le terminal
**Rôle :** Outil d'extension de shell qui inspecte le dossier courant à chaque changement de répertoire et applique les variables définies dans `.envrc`.
**Syntaxe :** `direnv <commande>`
**Cas réguliers :**
- `direnv allow .` — Approuver l'exécution du fichier `.envrc` du dossier courant pour des raisons de sécurité
- `direnv status` — Afficher l'état d'activation de direnv et du shell hôte
- `direnv reload` — Recharger le fichier `.envrc` après modification
**Origine :** Fabien Framery (2014) — écrit en Go.
**Subtilités/confusions :**
- Par sécurité, tout nouveau fichier `.envrc` ou toute modification nécessite de taper `direnv allow` avant d'être pris en compte.
**Urgences/dangers :** Ne jamais faire `direnv allow` sur un dépôt dont vous n'avez pas audité le fichier `.envrc` (risque d'exécution de code malveillant).
**Précautions :** Ajouter `.envrc` dans votre `.gitignore` global pour éviter de commiter des secrets par inadvertance.
**Équivalents :** dotenv, autoenv, shadowenv
**Voir aussi :** uv, rbenv, pyenv

## `just` — Command runner moderne et alternative propre à Make [Cross]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** `justfile`
**Contextes :** définir et exécuter des raccourcis de commandes spécifiques à un projet (ex: `just build`, `just test`, `just lint`) via un fichier `justfile` lisible
**Rôle :** Outil d'exécution de recettes et de scripts écrit en Rust, conçu spécifiquement comme un exécuteur de commandes (et non un système de build basé sur les dépendances de fichiers).
**Syntaxe :** `just [options] [recette]`
**Cas réguliers :**
- `just` — Lister toutes les recettes disponibles dans le `justfile` avec leurs commentaires
- `just build` — Exécuter la recette `build` définie dans le `justfile`
- `just test foo` — Exécuter la recette `test` en passant un argument
**Origine :** Casey Rodarmor (2016) — créé pour remplacer l'utilisation détournée de `make` comme simple lanceur de scripts.
**Subtilités/confusions :**
- Contrairement à Make, `just` n'a pas de syntaxe complexe de gestion de dépendances de fichiers et autorise les recettes dans n'importe quel langage (bash, python, node).
**Urgences/dangers :** —
**Précautions :** Placer le fichier `justfile` à la racine de votre dépôt Git pour documenter toutes les commandes utiles de l'application.
**Équivalents :** make, task (Taskfile), npm run
**Voir aussi :** make, cargo, npm
