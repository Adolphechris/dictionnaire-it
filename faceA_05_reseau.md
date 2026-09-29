# Face A — Commandes : RÉSEAU (diagnostic, transfert, DNS, firewall)

| commande | OS | rôle | syntaxe | exemples | précautions | équivalents |
|---|---|---|---|---|---|---|
| ping | Linux/macOS/Windows | Tester la connectivité vers un hôte | `ping [options] <hôte>` | `ping google.com` · `ping -c 4 8.8.8.8` · `ping -t serveur` (Windows, continu) | `-c` compte sur Linux/macOS, continu par défaut sur Windows | Test-Connection (PowerShell) |
| curl | Linux/macOS/Windows | Transférer des données via URL | `curl [options] <url>` | `curl https://api.site.fr` · `curl -o fichier.zip https://site.fr/f.zip` · `curl -I https://site.fr` (headers) | `-o` écrit sur disque ; sans option affiche dans le terminal | Invoke-WebRequest (PowerShell) |
| wget | Linux/macOS | Télécharger des fichiers via HTTP/FTP | `wget [options] <url>` | `wget https://site.fr/f.zip` · `wget -r https://site.fr/docs/` (récursif) | `-r` peut aspirer un site entier | curl |
| ssh | Linux/macOS/Windows | Se connecter à un shell distant chiffré | `ssh [options] <user>@<hôte>` | `ssh ada@serveur.fr` · `ssh -p 2222 ada@serveur.fr` · `ssh -i cle.pem ada@serveur.fr` | Vérifier l'empreinte du serveur au premier contact | — |
| scp | Linux/macOS | Copier des fichiers via SSH | `scp [options] <source> <cible>` | `scp a.txt ada@srv:/tmp/` · `scp -r dossier/ ada@srv:/tmp/` | `-r` requis pour les dossiers | rsync, sftp |
| sftp | Linux/macOS | Transférer des fichiers en interactif via SSH | `sftp <user>@<hôte>` | `sftp ada@serveur.fr` · `put a.txt` · `get b.txt` (dans le shell sftp) | — | scp, FTP (non chiffré) |
| ip | Linux | Afficher et configurer le réseau (iproute2) | `ip [objet] [commande]` | `ip addr` · `ip route` · `ip link` | Remplace `ifconfig` et `route` obsolètes | ifconfig, Get-NetIPAddress (PowerShell) |
| ip addr | Linux | Afficher les adresses IP des interfaces | `ip addr [show <iface>]` | `ip addr` · `ip addr show eth0` · `ip -brief addr` | Lecture seule, sans risque | ifconfig, ipconfig (Windows) |
| ip route | Linux | Afficher et gérer la table de routage | `ip route [show|add|del]` | `ip route` · `ip route add 10.0.0.0/24 via 192.168.1.1` | ⚠️ Une mauvaise route coupe le réseau | route |
| ifconfig | Linux/macOS | Afficher les interfaces réseau (ancien) | `ifconfig [interface]` | `ifconfig` · `ifconfig eth0` | Obsolète sur Linux, préférer `ip addr` | ip addr |
| netstat | Linux/macOS/Windows | Afficher connexions et ports en écoute | `netstat [options]` | `netstat -tulpn` · `netstat -an` · `netstat -r` (routes) | Obsolète sur Linux, préférer `ss` | ss (Linux) |
| ss | Linux | Afficher sockets et ports (remplace netstat) | `ss [options]` | `ss -tulpn` · `ss -s` (résumé) · `ss -t state established` | — | netstat |
| dig | Linux/macOS | Interroger les serveurs DNS | `dig [@serveur] <nom> [type]` | `dig example.com` · `dig @8.8.8.8 example.com MX` · `dig +short example.com` | — | nslookup, host |
| nslookup | Linux/macOS/Windows | Interroger le DNS en interactif ou direct | `nslookup <nom> [serveur]` | `nslookup example.com` · `nslookup example.com 8.8.8.8` | Outil en mode déprécié, préférer `dig` sur Linux | dig, host |
| host | Linux/macOS | Résoudre un nom en adresse IP | `host <nom>` | `host example.com` · `host 8.8.8.8` (reverse) | — | dig, nslookup |
