# Face A — Commandes : NAVIGATION ET EXPLORATION

| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |
|---|---|---|---|---|---|---|
| cd | Linux/macOS/Windows | Changer de répertoire | `cd [option] <chemin>` | `cd /tmp` · `cd ..` · `cd ~` · `cd -` · `cd` (retour home) | `cd ..` remonte d'un niveau ; `cd -` revient au dernier répertoire | Set-Location (PowerShell) |
| pwd | Linux/macOS | Afficher le répertoire courant | `pwd` | `pwd` → /home/utilisateur/projet | — | — |
| ls | Linux/macOS | Lister le contenu d'un répertoire | `ls [options] <chemin>` | `ls` · `ls -la` · `ls -lh` · `ls -a` · `ls -R` | L'option `-l` montre les détails ; `-a` inclut les cachés | dir (Windows) |
| dir | Windows (CMD) | Lister le contenu | `dir [options] <chemin>` | `dir` · `dir /s` · `dir /b` | `/s` liste récursivement | ls (Linux) |
| Get-ChildItem | PowerShell | Lister le contenu | `Get-ChildItem [options] <chemin>` | `Get-ChildItem` · `Get-ChildItem -Recurse` · `gci -Force` | Alias `gci`, `ls` | dir, ls |
| tree | Linux/macOS/Windows | Afficher l'arborescence graphique | `tree [options] <chemin>` | `tree` · `tree -L 2` · `tree -a` · `tree -d` | `-L` limite la profondeur ; `-d` n'affiche que les dossiers | — |
| explorer.exe | Windows | Ouvrir l'Explorateur Windows | `explorer.exe <chemin>` | `explorer.exe C:\` · `explorer.exe .` | — | open (macOS) |
| open | macOS | Ouvrir un fichier ou dossier | `open <chemin>` | `open /Applications` · `open -e fichier.txt` | `-e` ouvre dans l'éditeur par défaut | explorer.exe (Windows) |
| realpath | Linux/macOS | Afficher le chemin absolu résolu | `realpath <chemin>` | `realpath ../foo` | Résout les liens symboliques | — |
| basename | Linux/macOS | Extraire le dernier composant | `basename <chemin>` | `basename /a/b/c.txt` → c.txt | — | — |
| dirname | Linux/macOS | Extraire le répertoire parent | `dirname <chemin>` | `dirname /a/b/c.txt` → /a/b | — | — |