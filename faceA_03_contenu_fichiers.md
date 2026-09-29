# Face A — Commandes : CONTENU DES FICHIERS (affichage, recherche, édition)

| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |
|---|---|---|---|---|---|---|
| cat | Linux/macOS | Afficher / concaténer | `cat [options] <fichiers>` | `cat a.txt` · `cat a.txt b.txt` · `cat -n a.txt` (numéroter) | — | Get-Content (PowerShell) |
| Get-Content | PowerShell | Afficher un fichier | `Get-Content <fichier>` | `Get-Content log.txt` | Alias `cat`, `type` | cat |
| less | Linux/macOS | Parcourir un fichier page par page | `less <fichier>` | `less /var/log/syslog` | `q` pour quitter ; `f` / `b` pour descendre/monter | more |
| more | Linux/macOS/Windows | Parcourir page par page (plus simple) | `more <fichier>` | `more a.txt` | — | less |
| grep | Linux/macOS | Recherche de motif (regex) | `grep [options] <motif> <fichiers>` | `grep "error" *.log` · `grep -i "mot" a.txt` · `grep -r "mot" dossier/` · `grep -E "a|b"` | `-r` récursif ; `-i` insensible à la cas ; `-v` inverse | Select-String (PowerShell) |
| Select-String | PowerShell | Recherche de motif | `Select-String <motif> <fichier>` | `Select-String "error" *.log` | — | grep |
| find | Linux/macOS | Trouver des fichiers par nom/type | `find <chemin> [critères]` | `find . -name "*.txt"` · `find / -name "nginx.conf"` · `find . -type f -mtime -7` | Peut être lent sur de grands arborescences | — |
| locate | Linux/macOS | Recherche rapide (indexé) | `locate <motif>` | `locate nginx.conf` | Nécessite un index à jour (`updatedb`) ; moins précis que find | — |
| sed | Linux/macOS | Éditeur de flux (substitution) | `sed [options] 'commande' <fichier>` | `sed 's/ancien/nouveau/' a.txt` · `sed -i 's/a/b/g' a.txt` | `-i` modifie le fichier en place — attention à la sauvegarde | — |
| awk | Linux/macOS | Traitement de colonnes | `awk 'condition {action}' <fichier>` | `awk '{print $1}' a.txt` · `awk -F: '{print $1}' /etc/passwd` | — | — |
| cut | Linux/macOS | Extraire des colonnes | `cut [options] <fichier>` | `cut -d: -f1 /etc/passwd` · `cut -c1-10 a.txt` | — | — |
| sort | Linux/macOS/Windows | Trier les lignes | `sort [options] <fichier>` | `sort a.txt` · `sort -n a.txt` · `sort -k2 a.txt` | `-n` numérique ; `-r` inverse | — |
| uniq | Linux/macOS | Dédupliquer les lignes consécutives | `uniq [options] <fichier>` | `sort a.txt | uniq` · `uniq -c` (compter) | Doit être utilisé après `sort` | — |
| tr | Linux/macOS | Traduire des caractères | `tr [options] <ensemble1> <ensemble2>` | `tr 'a-z' 'A-Z'` · `tr -d '\n'` | — | — |
| diff | Linux/macOS | Comparer deux fichiers | `diff [options] <f1> <f2>` | `diff a.txt b.txt` · `diff -u a.txt b.txt` | — | — |
| cmp | Linux/macOS | Comparer octet par octet | `cmp [options] <f1> <f2>` | `cmp a.txt b.txt` | Affiche la première différence | — |
| nano | Linux/macOS | Éditeur de texte simple | `nano <fichier>` | `nano a.txt` | — | — |
| vim / vi | Linux/macOS | Éditeur de texte puissant | `vim <fichier>` | `vim a.txt` | Courbe d'apprentissage ; `:q!` pour quitter sans sauvegarder | — |
| emacs | Linux/macOS | Éditeur extensible | `emacs <fichier>` | `emacs a.txt` | — | — |
| code | Linux/macOS/Windows | Éditeur VS Code | `code [options] <chemin>` | `code a.txt` · `code dossier/` | — | — |
| notepad | Windows | Éditeur de texte | `notepad <fichier>` | `notepad a.txt` | — | — |
| notepad++ | Windows | Éditeur avancé | `notepad++ <fichier>` | `notepad++ a.txt` | — | — |