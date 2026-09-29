# Face A — Commandes : PROCESSUS ET SYSTÈME

| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |
|---|---|---|---|---|---|---|
| ps | Linux/macOS | Lister les processus | `ps [options]` | `ps` · `ps aux` · `ps -ef` · `ps -u root` | `ps aux` montre tous les processus (BSD style) | tasklist (Windows) |
| ps aux | Linux/macOS | Tous les processus (utilisateur, CPU, mémoire) | `ps aux` | `ps aux` | — | — |
| top | Linux/macOS | Surveillance CPU en temps réel | `top [options]` | `top` · `top -u root` | `q` pour quitter | htop (Linux) |
| htop | Linux | Interface graphique pour top | `htop` | `htop` | — | top |
| kill | Linux/macOS | Terminer un processus | `kill [options] <PID>` | `kill 1234` · `kill -9 1234` | `-9` (SIGKILL) force l'arrêt, non rattrapable | taskkill (Windows) |
| kill -9 | Linux/macOS | Forcer l'arrêt d'un processus | `kill -9 <PID>` | `kill -9 1234` | ⚠️ Impossible à ignorer ; pas de nettoyage | — |
| kill -15 | Linux/macOS | Signal par défaut (SIGTERM) | `kill -15 <PID>` | `kill 1234` (par défaut c'est -15) | Laisse le temps au processus de se terminer proprement | — |
| pkill | Linux/macOS | Tue les processus par nom | `pkill [options] <nom>` | `pkill nginx` · `pkill -9 chrome` | — | — |
| pgrep | Linux/macOS | Affiche les PID par nom | `pgrep <nom>` | `pgrep nginx` | — | — |
| tasklist | Windows (CMD) | Lister les processus | `tasklist` | `tasklist` · `tasklist /fi "pid eq 1234"` | — | ps |
| taskkill | Windows (CMD) | Terminer un processus | `taskkill [options] <PID|/im nom>` | `taskkill /PID 1234` · `taskkill /im chrome.exe /f` | `/f` force l'arrêt | kill |
| Get-Process | PowerShell | Lister les processus | `Get-Process [nom]` | `Get-Process` · `Get-Process notepad` | Alias `gps` | ps, tasklist |
| Stop-Process | PowerShell | Terminer un processus | `Stop-Process <PID|nom>` | `Stop-Process -Id 1234` · `Stop-Process notepad` | — | kill, taskkill |
| systemctl | Linux | Gestion des services systemd | `systemctl [commande] <service>` | `systemctl start nginx` · `systemctl status nginx` · `systemctl restart nginx` · `systemctl stop nginx` | — | service (ancien) |
| service | Linux/macOS | Gestion des services (ancien) | `service <service> <action>` | `service nginx start` | — | systemctl |
| launchctl | macOS | Gestion des services (launchd) | `launchctl [commande] <label>` | `launchctl start com.apple.cups` · `launchctl load plist` | — | systemctl |
| uname | Linux/macOS | Nom du système | `uname [options]` | `uname` · `uname -a` · `uname -s` · `uname -m` | — | — |
| hostname | Linux/macOS/Windows | Nom de la machine | `hostname [options]` | `hostname` · `hostname -f` | — | — |
| hostname -I | Linux | Adresse IP locale | `hostname -I` | `hostname -I` | N'existe pas sur macOS (utiliser `ipconfig getifaddr en0`) | ipconfig (Windows) |
| df | Linux/macOS | Espace disque utilisé | `df [options]` | `df -h` · `df -h /` | `-h` humainement lisible | — |
| du | Linux/macOS | Taille d'un répertoire | `du [options] <chemin>` | `du -sh .` · `du -sh *` | `-s` résume ; `-h` lisible | — |
| free | Linux | Mémoire utilisée | `free [options]` | `free -h` | N'existe pas en natif sur macOS (utiliser `vm_stat` ou `top`) | — |
| vmstat | Linux/macOS | Statistiques système | `vmstat [intervalle]` | `vmstat 1` | — | — |
| iostat | Linux/macOS | Statistiques E/S disque | `iostat [options]` | `iostat` · `iostat -x 1` | — | — |
| uptime | Linux/macOS | Temps de fonctionnement | `uptime` | `uptime` | — | — |
| whoami | Linux/macOS/Windows | Utilisateur courant | `whoami` | `whoami` | — | — |
| id | Linux/macOS | Identité de l'utilisateur | `id [options]` | `id` · `id root` | — | — |
| sudo | Linux/macOS | Exécuter en tant que root | `sudo [options] <commande>` | `sudo apt update` · `sudo -u postgres psql` | ⚠️ Accès root — utiliser avec précaution | — |
| su | Linux/macOS | Changer d'utilisateur | `su [options] <utilisateur>` | `su root` · `su - postgres` | `-` charge le profil de l'utilisateur | — |