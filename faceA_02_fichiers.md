# Face A — Commandes : FICHIERS (créer, copier, déplacer, renommer, supprimer)

| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |
|---|---|---|---|---|---|---|
| cp | Linux/macOS | Copier un fichier | `cp [options] <source> <cible>` | `cp a.txt b.txt` · `cp -r dossier/ cible/` · `cp -a` (archive) | `-r` requis pour les dossiers ; `-p` préserve les attributs | Copy-Item (PowerShell) |
| cp -r | Linux/macOS | Copier récursivement un dossier | `cp -r <source> <cible>` | `cp -r src/ dest/` | — | — |
| cp -a | Linux/macOS | Copier en préservant attributs | `cp -a <source> <cible>` | `cp -a src/ dest/` | Équivalent à `-dR --preserve=all` | — |
| mv | Linux/macOS | Déplacer ou renommer | `mv [options] <source> <cible>` | `mv a.txt b.txt` · `mv dossier/ /nouveau/chemin/` | Écrase sans confirmation | Move-Item (PowerShell) |
| rm | Linux/macOS | Supprimer un fichier | `rm [options] <cible>` | `rm a.txt` · `rm -r dossier/` | ⚠️ Destructif — aucune corbeille | Remove-Item (PowerShell) |
| rm -rf | Linux/macOS | Supprimer récursivement et forcer | `rm -rf <cible>` | `rm -rf dossier/` · `rm -rf /tmp/*` | ⚠️ TRÈS DANGEREUX — peut tout effacer | — |
| rm -i | Linux/macOS | Supprimer avec confirmation | `rm -i <cible>` | `rm -i *.txt` | Plus sûr en script interactif | — |
| mkdir | Linux/macOS/Windows | Créer un répertoire | `mkdir [options] <nom>` | `mkdir projet` · `mkdir -p a/b/c` | `-p` crée les parents | md (Windows) |
| md | Windows (CMD) | Créer un répertoire | `md <nom>` | `md projet` · `md a\b\c` | — | mkdir |
| rmdir | Linux/macOS | Supprimer un dossier vide | `rmdir <nom>` | `rmdir vide` | Échoue si le dossier n'est pas vide | — |
| Remove-Item -Force | PowerShell | Supprimer un fichier/dossier | `Remove-Item -Force <cible>` | `Remove-Item -Force dossier\` | — | rm, rmdir |
| touch | Linux/macOS | Créer un fichier vide / maj date | `touch <nom>` | `touch nouveau.txt` · `touch -a a.txt` | Met à jour la date de dernier accès | — |
| ln | Linux/macOS | Créer un lien | `ln [options] <cible> <nom>` | `ln -s /path/fichier lien` | `-s` pour lien symbolique ; sans -s, lien dur | — |
| ln -s | Linux/macOS | Lien symbolique | `ln -s <cible> <nom>` | `ln -s /usr/bin/python3 python` | Le lien pointe vers la cible ; supprimer le lien ne supprime pas la cible | — |
| chmod | Linux/macOS | Modifier les permissions | `chmod [options] <mode> <fichier>` | `chmod 755 script.sh` · `chmod +x script.sh` · `chmod -R 755 dossier/` | Mode octal : u=rwx g=rwx o=rwx | — |
| chmod +x | Linux/macOS | Rendre exécutable | `chmod +x <fichier>` | `chmod +x script.sh` | — | — |
| chown | Linux/macOS | Changer le propriétaire | `chown [options] <utilisateur>[:<groupe>] <fichier>` | `chown root:root fichier` · `chown -R root dossier/` | Nécessite les privilèges root | — |
| chgrp | Linux/macOS | Changer le groupe | `chgrp <groupe> <fichier>` | `chgrp admin fichier` | — | chown |
| stat | Linux/macOS | Afficher les métadonnées | `stat <fichier>` | `stat /etc/hosts` | — | — |
| file | Linux/macOS | Détecter le type de fichier | `file <fichier>` | `file image.png` · `file script.sh` | — | — |
| wc | Linux/macOS | Compter lignes/mots/octets | `wc [options] <fichier>` | `wc -l a.txt` · `wc -w a.txt` · `wc -c a.txt` | `-l` lignes ; `-w` mots ; `-c` octets | — |
| head | Linux/macOS | Afficher le début | `head [options] <fichier>` | `head -n 20 a.txt` · `head -c 100 a.txt` | Par défaut 10 lignes | — |
| tail | Linux/macOS | Afficher la fin | `tail [options] <fichier>` | `tail -f app.log` · `tail -n 50 a.txt` | `-f` suit le fichier en temps réel (utile pour les logs) | — |