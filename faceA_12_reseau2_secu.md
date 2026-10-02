## `tcpdump` — Capture et analyse de paquets réseau bas niveau [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** capturer le trafic réseau sur un serveur distant sans interface graphique, diagnostiquer des problèmes de poignée de main TCP (*handshake*) ou de requêtes DNS
**Rôle :** Analyseur de paquets de réseau informatique (sniffer) en ligne de commande permettant de capturer et d'inspecter les paquets reçus ou émis.
**Syntaxe :** `tcpdump [options] [expression_filtre]`
**Cas réguliers :**
- `tcpdump -i eth0 -n` — Capturer tout le trafic sur l'interface `eth0` sans résoudre les adresses IP en noms de domaine (`-n`)
- `tcpdump -i any port 80 or port 443` — Capturer uniquement le trafic HTTP (80) et HTTPS (443) sur toutes les interfaces
- `tcpdump -i eth0 -w capture.pcap` — Enregistrer les paquets bruts capturés dans un fichier PCAP pour analyse ultérieure sous Wireshark
**Origine :** Van Jacobson, Craig Leres & Steven McCanne / Lawrence Berkeley Lab (1988).
**Subtilités/confusions :**
- L'option `-n` évite les ralentissements dus à la résolution DNS inverse de chaque adresse IP capturée.
- L'expression de filtrage utilise la syntaxe BPF (*Berkeley Packet Filter*), permettant de combiner les filtres avec `and`, `or`, `not` (ex: `host 192.168.1.1 and tcp`).
**Urgences/dangers :** ⚠️ Capturer un trafic à très fort débit sans filtres stricts sur un serveur de production peut remplir rapidement le disque dur ou impacter les performances CPU.
**Précautions :** Toujours cibler l'interface (`-i`) et appliquer un filtre de port ou d'hôte pour limiter le volume de capture.
**Équivalents :** tshark, wireshark, dumpcap, pktmon (Windows)
**Voir aussi :** tshark, nmap, ss, netstat

## `tshark` — Version en ligne de commande de l'analyseur Wireshark [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** —
**Contextes :** décoder et analyser finement des fichiers de captures réseau `.pcap` en ligne de commande ou dans des scripts automatiques
**Rôle :** Outil d'analyse de protocole réseau et de capture en ligne de commande basé sur le moteur d'analyse de Wireshark.
**Syntaxe :** `tshark [options] [filtres_capture]`
**Cas réguliers :**
- `tshark -r capture.pcap -Y "http.request"` — Lire un fichier PCAP et filtrer uniquement les requêtes HTTP avec les filtres d'affichage Wireshark
- `tshark -i eth0 -f "tcp port 22"` — Capturer en direct le trafic du port SSH
- `tshark -r capture.pcap -z conv,ip` — Générer des statistiques de conversations d'adresses IP à partir d'un fichier de capture
**Origine :** Wireshark team / Gerald Combs (2006) — autrefois nommé tethereal.
**Subtilités/confusions :**
- Accepte deux types distincts de filtres : les filtres de capture BPF (`-f`) et les filtres d'affichage complexes Wireshark (`-Y`).
- Capable de décoder des centaines de protocoles applicatifs complexes (TLS, HTTP/2, gRPC, DNS, SMB).
**Urgences/dangers :** —
**Précautions :** Utiliser `-Y` pour appliquer la puissance des filtres de dissection Wireshark lors de l'analyse post-mortem de fichiers `.pcap`.
**Équivalents :** tcpdump, wireshark, dumpcap
**Voir aussi :** tcpdump, nmap
## `traceroute` — Traçage d'itinéraire de paquets IP [Linux/macOS]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** identifier où s'arrête le routage d'un paquet vers un serveur distant, déterminer la latence induite par chaque routeur intermédiaire
**Rôle :** Afficher l'itinéraire et mesurer les délais de transit des paquets à travers le réseau IP jusqu me la destination ciblée.
**Syntaxe :** `traceroute [options] <hôte_ou_ip>`
**Cas réguliers :**
- `traceroute 8.8.8.8` — Tracer l'itinéraire des sauts (*hops*) vers le serveur DNS de Google
- `traceroute -n google.com` — Désactiver la résolution DNS inverse des routeurs pour accélérer le diagnostic
- `traceroute -T -p 443 google.com` — Utiliser des paquets TCP SYN sur le port 443 (HTTPS) pour traverser les pare-feux qui bloquent UDP/ICMP
**Origine :** Van Jacobson (1987) — basé sur la manipulation du champ TTL (*Time To Live*) des en-têtes IP.
**Subtilités/confusions :**
- Par défaut sous Linux, `traceroute` envoie des paquets UDP sur des ports élevés (33434+), alors que `tracert` sous Windows envoie des paquets ICMP Echo Request.
- Les lignes avec des étoiles `* * *` indiquent qu'un routeur intermédiaire filtre les réponses ICMP Time Exceeded sans pour autant couper la connexion.
**Urgences/dangers :** —
**Précautions :** Utiliser le mode TCP (`traceroute -T -p 80`) lorsque les paquets UDP/ICMP par défaut sont bloqués par les pare-feux réseau.
**Équivalents :** tracert (Windows), mtr, tcptraceroute
**Voir aussi :** tracert, mtr, ping, ip
## `tracert` — Traçage d'itinéraire de paquets sous Windows [Windows]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** diagnostiquer des pannes de routage réseau ou des lenteurs de sauts d'interconnexion depuis un poste Windows
**Rôle :** Outil utilitaire sous Windows permettant de déterminer le chemin emprunté par des paquets ICMP vers une destination réseau.
**Syntaxe :** `tracert [options] <nom_hote|adresse_ip>`
**Cas réguliers :**
- `tracert 1.1.1.1` — Afficher la liste des sauts de routeurs jusqu'au DNS Cloudflare
- `tracert -d 8.8.8.8` — Empêcher la résolution de nom des adresses IP des routeurs (`-d` = don't resolve)
- `tracert -h 15 target.com` — Limiter le nombre maximal de sauts (*max hops*) à 15
**Origine :** Microsoft Windows NT (1993) — version Windows de traceroute.
**Subtilités/confusions :**
- Utilise exclusivement des requêtes ICMP Echo Request (contrairement au `traceroute` Linux qui utilise UDP par défaut).
- L'option `-d` est essentielle sous Windows pour obtenir un affichage quasi-immédiat sans attendre les timeouts DNS inversés.
**Urgences/dangers :** —
**Précautions :** Lancer dans une invite de commande Windows (CMD) ou PowerShell.
**Équivalents :** traceroute (Linux/macOS), mtr, Test-NetConnection -TraceRoute (PowerShell)
**Voir aussi :** traceroute, ping, mtr
## `mtr` — Traçage d'itinéraire et diagnostic réseau en temps réel [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** surveiller les pertes de paquets (*packet loss*) et les gitter de latence sur une liaison réseau longue durée
**Rôle :** Outil interactif combinant les fonctionnalités des commandes `ping` et `traceroute` avec mise à jour statistique continue.
**Syntaxe :** `mtr [options] <hôte>`
**Cas réguliers :**
- `mtr google.com` — Démarrer l'interface interactive TUI affichant en direct les statistiques de pertes et de latence pour chaque saut
- `mtr -n --report -c 100 8.8.8.8` — Générer un rapport texte imprimable après l'envoi de 100 paquets pings sans résolution DNS
- `mtr --tcp -P 443 target.com` — Effectuer le traçage en envoyant des paquets TCP vers le port HTTPS 443
**Origine :** Matt Kimball / Roger Wolff (1997) — acronyme de « My TraceRoute » (initialement Matt's TraceRoute).
**Subtilités/confusions :**
- Les colonnes `Loss%`, `Snt`, `Last`, `Avg`, `Best`, `Wrst`, `StDev` permettent d'isoler avec une précision chirurgicale le routeur responsable de la dégradation réseau.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Une perte de paquets affichée sur un saut intermédiaire qui disparaît sur les sauts suivants indique un simple rate-limiting ICMP du routeur et non une vraie perte de réseau.
**Équivalents :** traceroute, pathping (Windows)
**Voir aussi :** traceroute, ping, iperf3
## `nc` — Le couteau suisse des connexions réseau TCP/UDP [Linux/macOS]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** netcat
**Contextes :** tester si un port distant est ouvert (`nc -zv`), transférer un fichier entre deux machines, ouvrir une écoute sur un port TCP
**Rôle :** Utilitaire universel pour lire et écrire des données à travers des connexions réseau en utilisant les protocoles TCP ou UDP.
**Syntaxe :** `nc [options] <hôte> <port>`
**Cas réguliers :**
- `nc -zv 192.168.1.50 80` — Tester rapidement la disponibilité du port HTTP 80 sans envoyer de payload (`-z` = zero-I/O, `-v` = verbose)
- `nc -l -p 4444` — Ouvrir un serveur en écoute sur le port local 4444 (*listen mode*)
- `nc -w 3 10.0.0.1 22` — Tester la connexion au port SSH avec un délai d'expiration (*timeout*) de 3 secondes
**Origine :** Hobbit / Cult of the Dead Cow (1995) — légendaire "couteau suisse réseau".
**Subtilités/confusions :**
- Existe sous deux variantes majeures sous Linux : OpenBSD netcat (`netcat-openbsd`) et GNU netcat (`netcat-traditional`).
- Utile pour créer à la volée des bannières HTTP, des bannières SSH ou des tunnels de données improvisés.
**Urgences/dangers :** ⚠️ Les fonctionnalités comme `nc -e /bin/bash` (shell inversé / *reverse shell*) sont souvent exploitées en cybersécurité et bloquées par les antivirus.
**Précautions :** Privilégier `nc -zv` pour les vérifications de ports réseau dans les scripts d'administration.
**Équivalents :** ncat (Nmap), socat, Test-NetConnection (PowerShell)
**Voir aussi :** ncat, socat, nmap, ss
## `nmap` — Scanner d'exploration réseau et d'audit de sécurité [Cross]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** découvrir les hôtes actifs sur un réseau local, identifier les ports ouverts et les services/versions qui y tournent
**Rôle :** Outil de référence mondial pour la découverte de réseau, l'audit de sécurité et le balayage de ports IP.
**Syntaxe :** `nmap [types_scan] [options] <cible>`
**Cas réguliers :**
- `nmap -sn 192.168.1.0/24` — Balayer le réseau local pour découvrir toutes les machines actuellement allumées (*Ping sweep*)
- `nmap -sV -sC -p 80,443,22 10.0.0.1` — Scanner les ports spécifiés avec détection de version des services (`-sV`) et scripts par défaut (`-sC`)
- `nmap -O target.com` — Tenter la détection de l'empreinte du système d'exploitation de la cible (*OS fingerprinting*)
**Origine :** Gordon Lyon (Fyodor) (1997) — acronyme de « Network Mapper ».
**Subtilités/confusions :**
- Le scan SYN discret par défaut (`-sS`) nécessite les droits `sudo` car il forge des paquets TCP bruts.
- La suite Nse (*Nmap Scripting Engine*) permet d'exécuter des centaines de scripts de détection de vulnérabilités (ex: `--script vuln`).
**Urgences/dangers :** ⚠️ Scanner un réseau ou des serveurs distants sans autorisation préalable explicite est illégal et détecté par les systèmes IDS/IPS.
**Précautions :** Restreindre la plage de ports scannés (ex: `-p 1-1024` ou `-F`) pour accélérer le scan et réduire le bruit réseau.
**Équivalents :** masscan, rustscan, zenmap (GUI)
**Voir aussi :** nc, masscan, tshark, ss
## `ss` — Inspection des sockets et connexions réseau Linux [Linux]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** vérifier quels ports sont en écoute sur un serveur, trouver quel processus utilise le port 8080 (remplaçant moderne de `netstat`)
**Rôle :** Afficher des statistiques détaillées sur les sockets réseau en extraire directement les informations du noyau Linux (`iproute2`).
**Syntaxe :** `ss [options] [filtres]`
**Cas réguliers :**
- `ss -tulpn` — Afficher tous les ports TCP (`-t`) et UDP (`-u`) en ÉCOUTE (`-l`), avec adresses numériques (`-n`) et noms des PROCESSUS (`-p`)
- `ss -ta` — Afficher l'ensemble des sockets TCP (en écoute et connexions établies)
- `ss -s` — Afficher une synthèse globale du nombre de sockets par état (ESTAB, TIME-WAIT, LISTEN)
**Origine :** Alexey Kuznetsov / iproute2 (2001) — acronyme de « Socket Statistics ».
**Subtilités/confusions :**
- `ss` est infiniment plus rapide que l'historique `netstat` car il interroge les structures `netlink` du noyau au lieu de lire `/proc/net/dev`.
- L'option `-p` nécessite les droits `sudo` pour afficher le nom et le PID du processus propriétaire de la socket.
**Urgences/dangers :** —
**Précautions :** Remplacer systématiquement la commande obsolète `netstat -tulpn` par `ss -tulpn` dans tous les scripts Linux.
**Équivalents :** netstat, lsof -i, Get-NetTCPConnection (PowerShell)
**Voir aussi :** netstat, lsof, ip, nc
## `netstat` — Statistique des connexions réseau et tables de routage [Cross]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** inspecter les connexions réseau actives et la table de routage sous Windows, macOS ou anciens systèmes Unix
**Rôle :** Afficher les connexions réseau actives (TCP/UDP), les tables de routage et les statistiques d'interfaces.
**Syntaxe :** `netstat [options]`
**Cas réguliers :**
- `netstat -ano` — Afficher toutes les connexions actives avec les adresses numériques et le PID sous Windows (le plus courant sous CMD/PowerShell)
- `netstat -r` — Afficher la table de routage IP du système d'exploitation
- `netstat -i` — Afficher les statistiques de trafic et erreurs sur les cartes réseau
**Origine :** BSD Unix (1983) — acronyme de « Network Statistics ».
**Subtilités/confusions :**
- Déprécié sous Linux au profit de `ss` et `ip route`, mais demeure l'outil natif standard incontournable sous Windows.
- Sous Windows, combiner avec `tasklist /FI "PID eq <PID>"` pour identifier le binaire propriétaire de la connexion.
**Urgences/dangers :** —
**Précautions :** Utiliser `ss` sous Linux et `netstat -ano` sous Windows.
**Équivalents :** ss (Linux), Get-NetTCPConnection (PowerShell), lsof -i
**Voir aussi :** ss, ip, lsof
## `ip` — Suite universelle d'administration réseau Linux [Linux]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** afficher l'adresse IP d'une machine (`ip a`), activer/désactiver une interface réseau, modifier la table de routage
**Rôle :** Consulter et configurer les interfaces réseau, l'adressage IP, le routage et les tunnels du noyau Linux (`iproute2`).
**Syntaxe :** `ip [options] <objet> <commande>`
**Cas réguliers :**
- `ip a` — Afficher toutes les cartes réseau et leurs adresses IPv4/IPv6 (*ip address show*)
- `ip r` — Afficher la table de routage IP et la passerelle par défaut (*ip route show*)
- `ip link set eth0 up` — Activer la carte réseau `eth0`
**Origine :** Alexey Kuznetsov / iproute2 (1999) — remplace totalement `ifconfig`, `route` et `arp`.
**Subtilités/confusions :**
- La commande s'articule autour d'objets : `addr` (adresses), `link` (interfaces physiques/virtuelles), `route` (routage), `neigh` (table ARP).
- Les modifications effectuées via la commande `ip` s'appliquent immédiatement en mémoire mais ne sont PAS persistantes au redémarrage (configurer Netplan/NetworkManager pour pérenniser).
**Urgences/dangers :** ⚠️ Exécuter `ip addr flush dev eth0` ou `ip route del default` sur une machine distante via SSH coupe immédiatement la session distante.
**Précautions :** Valider la syntaxe et s'assurer d'avoir un accès console de secours avant d'altérer les routes principales.
**Équivalents :** ifconfig, route, netsh (Windows), Get-NetIPAddress (PowerShell)
**Voir aussi :** ifconfig, route, ss, nmcli
## `ifconfig` — Configuration historique des interfaces réseau [Linux/macOS]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** consulter son adresse IP sous macOS, administrer d'anciens systèmes Unix ou BSD
**Rôle :** Configurer et afficher les paramètres des interfaces réseau (adresse IP, masque de sous-réseau, MTU, statut).
**Syntaxe :** `ifconfig [interface] [options] [adresse_ip]`
**Cas réguliers :**
- `ifconfig` — Lister les interfaces réseau actives et leurs adresses IP (sous macOS et BSD)
- `ifconfig eth0 up` — Activer l'interface réseau `eth0`
- `ifconfig eth0 192.168.1.100 netmask 255.255.255.0` — Attribuer manuellement une adresse IPv4 et son masque
**Origine :** BSD Unix (1982) — acronyme de « Interface Configuration ».
**Subtilités/confusions :**
- Déprécié sur les distributions Linux modernes au profit de la suite `ip` (`ip a`).
- Reste l'outil de ligne de commande standard natif pour interroger les cartes réseau sous macOS et FreeBSD.
**Urgences/dangers :** —
**Précautions :** Utiliser `ip a` sous Linux et `ifconfig` sous macOS.
**Équivalents :** ip addr (Linux), ipconfig (Windows), Get-NetIPAddress (PowerShell)
**Voir aussi :** ip, route, ipconfig
## `route` — Consultation et gestion de la table de routage IP [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** ajouter une route statique pour joindre un réseau privé à travers une passerelle ou un VPN
**Rôle :** Consulter et modifier la table de routage IP du système d'exploitation.
**Syntaxe :** `route [options] <add|del> [destination] [gw passerelle]`
**Cas réguliers :**
- `route -n` — Afficher la table de routage réseau sous forme numérique sous Linux (`-n` évite les résolutions DNS)
- `route add -net 10.8.0.0 netmask 255.255.0.0 gw 192.168.1.254` — Ajouter une route statique vers le sous-réseau 10.8.0.0/16
- `route add default gw 192.168.1.1` — Définir la passerelle par défaut (*default gateway*)
**Origine :** BSD Unix (1983) / System V.
**Subtilités/confusions :**
- Déprécié sous Linux au profit de `ip route`.
- Sur macOS, la syntaxe d'ajout diffère légèrement : `route add -net 10.8.0.0/16 192.168.1.254`.
**Urgences/dangers :** ⚠️ Une erreur de manipulation de la passerelle par défaut coupe instantanément les accès internet et SSH distants.
**Précautions :** Utiliser `ip route` sous Linux moderne.
**Équivalents :** ip route (Linux), route (Windows CMD), New-NetRoute (PowerShell)
**Voir aussi :** ip, ifconfig, netstat
## `arp` — Table de correspondance entre adresses IP et adresses physiques MAC [Cross]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** vérifier l'adresse MAC physique d'un équipement sur le réseau local, diagnostiquer une attaque par empoisonnement ARP (*ARP spoofing*)
**Rôle :** Consulter et manipuler la table de cache du protocole ARP (*Address Resolution Protocol*) du système d'exploitation.
**Syntaxe :** `arp [options] [adresse_ip]`
**Cas réguliers :**
- `arp -a` — Afficher la totalité de la table du cache ARP local (adresses IP associées aux adresses MAC physiques)
- `arp -d 192.168.1.50` — Supprimer l'entrée de cache ARP d'une adresse IP spécifique
- `arp -s 192.168.1.1 00:11:22:33:44:55` — Ajouter une entrée ARP statique permanente pour verrouiller l'adresse de la passerelle
**Origine :** BSD Unix (1983) / RFC 826.
**Subtilités/confusions :**
- La table ARP est construite dynamiquement par les échanges broadcast de la couche 2 sur le réseau local (LAN).
- Sous Linux moderne, remplacé par `ip neigh`.
**Urgences/dangers :** —
**Précautions :** Vider le cache ARP (`arp -d *` sous Windows ou `ip neigh flush all` sous Linux) en cas de remplacement d'un équipement réseau ayant gardé la même IP.
**Équivalents :** ip neigh (Linux), Get-NetNeighbor (PowerShell)
**Voir aussi :** ip, arping, ifconfig
## `ethtool` — Configuration et diagnostic des cartes réseau Ethernet [Linux]
**Niveau :** avance | **Popularité :** 84 | **Aliases :** —
**Contextes :** vérifier la vitesse de négociation d'un câble Ethernet (100 Mbps vs 1 Gbps / 10 Gbps), forcer le mode Full-Duplex, identifier le clignotement de la LED du port
**Rôle :** Consulter et modifier les paramètres de la carte réseau physique et de son pilote (vitesse, duplex, autonégociation, offloading).
**Syntaxe :** `ethtool [options] <interface>`
**Cas réguliers :**
- `ethtool eth0` — Afficher l'état matériel de la carte `eth0` (vitesse link, mode duplex, détection de câble branché)
- `ethtool -p eth0 10` — Faire clignoter la LED physique du port réseau pendant 10 secondes pour l'identifier dans la baie de brassage
- `ethtool -K eth0 tso off gso off` — Désactiver le déchargement de segmentation TCP (*offloading*) en cas de bogue de carte NIC
**Origine :** David Miller / Linux Kernel network maintainers (1998).
**Subtilités/confusions :**
- `Link detected: yes` est le test ultime pour valider si le câble réseau physique est correctement branché et alimenté.
- Nécessite les droits privilèges `sudo` pour la modification des paramètres matériels.
**Urgences/dangers :** ⚠️ Forcer la vitesse ou le duplex (`speed 1000 duplex full autoneg off`) sur un commutateur qui n'a pas la même configuration provoque une perte totale de lien.
**Précautions :** Conserver `autoneg on` dans 99% des cas modernes.
**Équivalents :** networksetup (macOS), Get-NetAdapterAdvancedProperty (PowerShell)
**Voir aussi :** ip, lspci, dmesg
## `iwconfig` — Inspection et configuration des cartes réseau sans fil Wi-Fi [Linux]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** —
**Contextes :** vérifier la qualité du signal Wi-Fi (dBm), le nom du point d'accès (ESSID) et la fréquence sous Linux
**Rôle :** Définir et afficher les paramètres d'une interface réseau sans fil Wi-Fi (802.11).
**Syntaxe :** `iwconfig [interface] [options]`
**Cas réguliers :**
- `iwconfig` — Lister les cartes sans fil disponibles et leurs paramètres de connexion (ESSID, Fréquence, Bit Rate, Link Quality)
- `iwconfig wlan0 essid "MonReseauWiFi"` — Connecter l'interface au réseau Wi-Fi spécifié
**Origine :** Jean Tourrilhes / Wireless Tools for Linux (1996) — équivalent de `ifconfig` pour le sans-fil.
**Subtilités/confusions :**
- Déprécié sur les systèmes Linux récents au profit de l'outil moderne `iw` et du dmon `nmcli` / `NetworkManager`.
- Ne gère pas directement le chiffrement moderne WPA2/WPA3 (qui requiert `wpa_supplicant`).
**Urgences/dangers :** —
**Précautions :** Préférer `iw dev` ou `nmcli` sur les distributions Linux modernes.
**Équivalents :** iw (Linux), nmcli, wdutil (macOS), netsh wlan (Windows)
**Voir aussi :** nmcli, ifconfig, ip
## `dig` — Interrogation DNS avancée (*Domain Information Groper*) [Linux/macOS]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** diagnostiquer la résolution d'un nom de domaine (A, AAAA, MX, TXT, CNAME), auditer la propagation DNS globale
**Rôle :** Outil d'interrogation et de résolution de serveurs de noms de domaine (DNS) souple et complet.
**Syntaxe :** `dig [@serveur_dns] <domaine> [type_enregistrement]`
**Cas réguliers :**
- `dig google.com` — Interroger le serveur DNS système pour obtenir l'enregistrement IPv4 `A` de google.com
- `dig @8.8.8.8 example.com MX +short` — Interroger spécifiquement les serveurs DNS de Google pour les enregistrements MX avec sortie courte
- `dig -x 1.1.1.1` — Effectuer une recherche DNS inversée (*PTR lookup*) pour trouver le nom associé à une adresse IP
**Origine :** Steve Hotz / BIND / ISC (1990) — acronyme de « Domain Information Groper ».
**Subtilités/confusions :**
- Contrairement à `nslookup`, `dig` interroge directement les serveurs DNS autoritaires sans passer par les mécanismes de cache du système d'exploitation (`/etc/hosts`).
- L'option `+trace` permet de visualiser l'intégralité de la chaîne de résolution récursive depuis les serveurs racines DNS (*Root Servers*).
**Urgences/dangers :** —
**Précautions :** Passer l'option `+short` dans les scripts shell pour récupérer uniquement la valeur brute (ex: adresse IP) sans l'en-tête de réponse.
**Équivalents :** nslookup, host, Resolve-DnsName (PowerShell)
**Voir aussi :** nslookup, host, ping
## `nslookup` — Recherche d'enregistrements d'adresses DNS [Cross]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** tester rapidement si un domaine pointe sur la bonne adresse IP sous Windows, Linux ou macOS
**Rôle :** Outil interactif ou ponctuel de requête sur les serveurs de noms de domaine DNS.
**Syntaxe :** `nslookup <domaine> [serveur_dns]`
**Cas réguliers :**
- `nslookup github.com` — Afficher l'adresse IP associée au domaine `github.com` via le serveur DNS par défaut
- `nslookup -type=MX gmail.com 1.1.1.1` — Rechercher les serveurs de messagerie (MX) en interrogeant le DNS Cloudflare
- `nslookup` — Ouvrir l'interpréteur interactif pour exécuter plusieurs requêtes DNS consécutives
**Origine :** Andrew Cherenson / BIND (1989) — acronyme de « Name Server Lookup ».
**Subtilités/confusions :**
- Déprécié un temps par le groupe BIND au profit de `dig`, mais conservé en raison de son omniprésence native sur Windows.
- Lit les paramètres DNS configurés dans l'OS et prend en compte le fichier `/etc/hosts` sous certaines plateformes.
**Urgences/dangers :** —
**Précautions :** Utiliser `dig` sur les systèmes Unix/Linux et `nslookup` ou `Resolve-DnsName` sur Windows.
**Équivalents :** dig, host, Resolve-DnsName (PowerShell)
**Voir aussi :** dig, host
## `host` — Utilitaire de résolution de nom de domaine simple [Linux/macOS]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** —
**Contextes :** vérifier la correspondance simple entre un nom de domaine et son IP dans un script Bash
**Rôle :** Outil simple et concis pour effectuer des recherches de résolution de nom DNS inverse et directe.
**Syntaxe :** `host [options] <domaine|ip> [serveur_dns]`
**Cas réguliers :**
- `host google.com` — Convertir un nom de domaine en ses adresses IPv4 et IPv6 correspondantes
- `host 8.8.8.8` — Effectuer une résolution DNS inverse de l'adresse IP vers le nom d'hôte (`dns.google`)
- `host -t txt example.com` — Consulter spécifiquement les enregistrements TXT (ex: SPF, DKIM, DMARC)
**Origine :** Eric Wassenaar / BIND (1991).
**Subtilités/confusions :**
- Produit une sortie en langage naturel très facile à lire et parser en script (ex: `google.com has address 142.250.179.206`).
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Préférer `host` à `dig` pour un affichage humain minimaliste en une seule ligne.
**Équivalents :** dig, nslookup
**Voir aussi :** dig, nslookup
## `whois` — Consultation des enregistrements de propriété de domaines et d'IP [Cross]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** identifier le propriétaire ou le registrar d'un nom de domaine, connaître la date d'expiration d'un domaine ou le bloc IP d'un FAI
**Rôle :** Interroger la base de données publique du protocole WHOIS pour obtenir les informations d'enregistrement des noms de domaines et blocs IP.
**Syntaxe :** `whois [options] <domaine|adresse_ip>`
**Cas réguliers :**
- `whois wikipedia.org` — Afficher le nom du registrar, la date de création, d'expiration et les serveurs DNS autoritaires
- `whois 8.8.8.8` — Identifier le Registre Internet Régional (ARIN, RIPE NCC) et l'entité propriétaire du bloc d'adresses IP
**Origine :** DARPA / SRI-NIC (1982) — formalisé par la RFC 812 puis RFC 3912.
**Subtilités/confusions :**
- En raison des réglementations RGPD / GDPR, de nombreuses informations personnelles d'individus (nom, adresse, téléphone) sont désormais masquées par défaut.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Interroger le serveur qui convient en cas de domaines de premier niveau spécifiques (ex: `whois -h whois.afnic.fr domaine.fr`).
**Équivalents :** rdap (protocol moderne JSON), Get-Whois
**Voir aussi :** dig, nslookup
## `curl` — Transfert de données universel via URL [Cross]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** —
**Contextes :** tester une API REST, télécharger un fichier, inspecter les en-têtes HTTP/S, déboguer des webservices
**Rôle :** Outil en ligne de commande et bibliothèque (libcurl) pour transférer des données en utilisant une multitude de protocoles réseau (HTTP, HTTPS, FTP, SFTP, SMTP).
**Syntaxe :** `curl [options] <url>`
**Cas réguliers :**
- `curl -I https://example.com` — Récupérer uniquement les en-têtes HTTP de réponse (*HTTP HEAD request*)
- `curl -sSL https://get.docker.com | sh` — Suivre les redirections (`-L`) silencieusement (`-s`) et passer le script à l'interpréteur Shell
- `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/data` — Envoyer une requête HTTP POST avec un corps JSON
**Origine :** Daniel Stenberg (1996) — l'un des logiciels open-source les plus déployés au monde (milliards de machines).
**Subtilités/confusions :**
- Par défaut, `curl` écrit le corps de la réponse sur la sortie standard `stdout` (utiliser `-o fichier` pour enregistrer sur disque).
- L'option `-k` (`--insecure`) permet de ignorer les erreurs de validation des certificats SSL/TLS (à réserver au dev local !).
**Urgences/dangers :** ⚠️ Exécuter aveuglément des scripts téléchargés via `curl | sh` sans audit préalable présente un risque de sécurité élevé.
**Précautions :** Passer `-f` (`--fail`) dans les scripts Bash pour que `curl` retourne un code d'erreur Shell en cas de réponse HTTP 4xx ou 5xx.
**Équivalents :** wget, httpie, Invoke-WebRequest (PowerShell)
**Voir aussi :** wget, httpie, openssl
## `wget` — Téléchargeur de fichiers réseau non-interactif [Cross]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** télécharger de gros fichiers ou ISO en tâche de fond, aspirer la totalité d'un site web de manière récursive
**Rôle :** Utilitaire non-interactif de téléchargement de fichiers depuis le Web via les protocoles HTTP, HTTPS et FTP.
**Syntaxe :** `wget [options] <url>`
**Cas réguliers :**
- `wget https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso` — Télécharger un fichier et l'enregistrer directement sur le disque avec son nom d'origine
- `wget -c https://example.com/bigfile.zip` — Reprendre un téléchargement interrompu en cours de route (`-c` = continue)
- `wget -m -k -p https://site.example.com` — Météoriser/aspirer un site web complet pour une consultation hors-ligne (`-m` = mirror, `-k` = convert links)
**Origine :** Hrvoje Nikšić (1996) — acronyme de « World Wide Web Get ».
**Subtilités/confusions :**
- Contrairement à `curl` qui écrit sur `stdout`, `wget` enregistre PAR DÉFAUT le contenu téléchargé dans un fichier sur le disque.
- Gère de manière native la reconnexion automatique en cas de coupure réseau temporaire.
**Urgences/dangers :** —
**Précautions :** Passer l'option `-q` (*quiet*) dans les scripts d'arrière-plan pour masquer la barre de progression.
**Équivalents :** curl, Invoke-WebRequest (PowerShell)
**Voir aussi :** curl, aria2
## `httpie` — Client HTTP en ligne de commande moderne et lisible [Cross]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** http, https
**Contextes :** tester des APIs web JSON en développement avec une coloration syntaxique et un formatage automatique
**Rôle :** Client HTTP en ligne de commande intuitif et moderne conçu pour rendre l'interaction avec les services web aussi simple que possible.
**Syntaxe :** `http [flags] [METHODE] URL [item=valeur ...]`
**Cas réguliers :**
- `http GET api.example.com/users` — Envoyer une requête HTTP GET avec affichage coloré et formaté du résultat JSON
- `http POST api.example.com/users name="John Doe" email="john@example.com"` — Envoyer du JSON sans syntaxe lourde d'échappement
- `http -a user:password https://api.example.com/protected` — Effectuer une requête avec authentification HTTP Basic
**Origine :** Jakub Roztocil (2012) — créé pour offrir une alternative moderne à la syntaxe verbeuse de `curl`.
**Subtilités/confusions :**
- Détecte automatiquement les réponses JSON et les formate avec indentation et couleurs.
- Fournit deux exécutables distincts : `http` (HTTP) et `https` (HTTPS par défaut).
**Urgences/dangers :** —
**Précautions :** Passer `--offline` pour construire et afficher la requête HTTP générée sans l'envoyer sur le réseau.
**Équivalents :** curl, wget, curlie, postman
**Voir aussi :** curl, wget
## `ping` — Vérification de l'accessibilité ICMP entre hôtes [Cross]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** —
**Contextes :** vérifier si un serveur est allumé et joignable sur le réseau local ou distant, évaluer le temps d'aller-retour (*Round Trip Time*)
**Rôle :** Envoyer des paquets de requêtes ICMP Echo Request vers une cible réseau pour vérifier l'accessibilité et la latence.
**Syntaxe :** `ping [options] <hôte_ou_ip>`
**Cas réguliers :**
- `ping 8.8.8.8` — Envoyer des pings ICMP en continu vers le DNS de Google (interrompre avec Ctrl+C)
- `ping -c 4 google.com` — Limiter l'envoi à exactement 4 paquets pings sous Linux/macOS (`-c` = count)
- `ping -i 0.2 192.168.1.1` — Envoyer des pings à un intervalle rapide de 200 millisecondes pour diagnostiquer un micro-coupure
**Origine :** Mike Muuss / US Army Ballistic Research Lab (1983) — nommé d'après le son du sonar sous-marin.
**Subtilités/confusions :**
- Sous Windows, `ping` s'arrête par défaut après 4 paquets ; sous Linux/macOS, il tourne indéfiniment jusqu'à l'interruption par l'utilisateur.
- De nombreux pare-feux et serveurs Cloud (ex: AWS EC2 Security Groups) bloquent les pings ICMP par défaut même si les services TCP (HTTP/SSH) fonctionnent parfaitement.
**Urgences/dangers :** ⚠️ L'option `ping -f` (*flood ping*) envoie des milliers de paquets par seconde (nécessite root) et peut paralyser un réseau lent.
**Précautions :** Ne pas conclure qu'un serveur est éteint si le ping échoue : tester également le port TCP avec `nc -zv`.
**Équivalents :** fping, arping, Test-Connection (PowerShell)
**Voir aussi :** fping, arping, traceroute, mtr
## `arping` — Envoi de requêtes d'exploration ARP sur le réseau local [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** —
**Contextes :** découvrir l'adresse IP d'un équipement sur le même réseau Ethernet même si son pare-feu interne bloque les pings ICMP
**Rôle :** Envoyer des requêtes ARP (*Address Resolution Protocol*) au niveau de la couche 2 d'une interface réseau locale.
**Syntaxe :** `arping [options] -I <interface> <adresse_ip>`
**Cas réguliers :**
- `arping -I eth0 192.168.1.1` — Envoyer des pings ARP à la passerelle via la carte `eth0`
- `arping -D -I eth0 192.168.1.100` — Détecter si une adresse IP est déjà utilisée par une autre machine sur le réseau local (*Duplicate Address Detection*)
**Origine :** Thomas Habets / Alexey Kuznetsov (2000).
**Subtilités/confusions :**
- Ne fonctionne QUE sur le sous-réseau local direct (couche 2 Ethernet), car les paquets ARP ne traversent pas les routeurs.
- Contourne les filtres de pare-feu applicatifs hôtes qui bloquent les pings ICMP standards.
**Urgences/dangers :** —
**Précautions :** Utiliser `arping -D` avant d'assigner une adresse IP statique à un serveur pour éviter les conflits d'adresses IP.
**Équivalents :** ping, fping, nmap -sn
**Voir aussi :** ping, arp, ip
## `fping` — Envoi simultané de requêtes ICMP à de multiples cibles [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** vérifier en une seule commande la connectivité d'une liste de 100 serveurs ou d'un sous-réseau complet `/24`
**Rôle :** Outil semblable à `ping` optimisé pour envoyer des requêtes ICMP en parallèle à un grand nombre d'hôtes réseau.
**Syntaxe :** `fping [options] [cibles]`
**Cas réguliers :**
- `fping -a -g 192.168.1.0/24` — Afficher uniquement la liste des adresses IP vivantes (*alive*) sur le sous-réseau local
- `fping server1 server2 server3` — Pinger rapidement une liste d'hôtes spécifiés en ligne de commande
- `fping -f host_list.txt` — Lire la liste des adresses IP à pinger depuis un fichier texte
**Origine :** Roland Schemers (1992) — conçu pour surmonter la lenteur séquentielle de `ping`.
**Subtilités/confusions :**
- Très utilisé dans les scripts de monitoring (Zabbix, Nagios) pour tester des fermes de serveurs sans temps d'attente bloquant.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Passer le drapeau `-a` pour ne conserver dans la sortie que les machines qui répondent au ping.
**Équivalents :** ping, nmap -sn, gping
**Voir aussi :** ping, arping, nmap
## `iperf3` — Outil de mesure de débit et bande passante réseau [Cross]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** iperf
**Contextes :** tester la bande passante maximale réelle (en Mbps ou Gbps) entre deux serveurs ou à travers une liaison VPN
**Rôle :** Mesurer les performances et le débit maximal atteignable sur des réseaux IP (TCP et UDP).
**Syntaxe :** `iperf3 -s` (serveur) / `iperf3 -c <ip_serveur>` (client)
**Cas réguliers :**
- `iperf3 -s` — Lancer iperf3 en mode serveur en écoute sur le port par défaut 5201
- `iperf3 -c 192.168.1.50` — Lancer le test de débit depuis le client vers le serveur pendant 10 secondes
- `iperf3 -c 192.168.1.50 -R -P 4` — Tester le débit en téléchargement (*Reverse mode*) avec 4 flux TCP parallèles
**Origine :** NAEI / NLANG / ESnet (2014) — acronyme de « Internet Performance ».
**Subtilités/confusions :**
- Nécessite l'exécution de l'outil des deux côtés : un serveur (`-s`) et un client (`-c`).
- `iperf3` est une réécriture complète d'iperf2 et n'est pas rétro-compatible avec le protocole iperf2 original.
**Urgences/dangers :** ⚠️ Exécuter un test `iperf3` en mode UDP à débit forcé (`-u -b 10G`) peut saturer complètement le lien réseau physique et impacter la production.
**Précautions :** Privilégier les tests TCP par défaut qui adaptent automatiquement leur fenêtre de congestion.
**Équivalents :** netperf, nttcp, speedtest-cli
**Voir aussi :** mtr, ping, bandwhich
## `socat` — Relais bidirectionnel de flux de données et sockets [Linux/macOS]
**Niveau :** avance | **Popularité :** 85 | **Aliases :** —
**Contextes :** rediriger un port TCP local vers une socket Unix ou un port distant, créer un proxy SSL/TLS improvisé, déboguer des liaisons séries
**Rôle :** Relais polyvalent qui établit deux flux de données bidirectionnels entre deux points de terminaison réseau ou système.
**Syntaxe :** `socat [options] <adresse1> <adresse2>`
**Cas réguliers :**
- `socat TCP-LISTEN:8080,fork TCP:192.168.1.50:80` — Transmettre le trafic du port 8080 local vers le port 80 du serveur distant (proxy TCP)
- `socat - OPENSSL-LISTEN:443,cert=server.pem,verify=0` — Créer un serveur d'écoute SSL/TLS temporaire
- `socat UNIX-LISTEN:/tmp/docker.sock,fork TCP:localhost:2375` — Rediriger une socket Unix vers un port TCP
**Origine :** Gerhard Rieger (2001) — acronyme de « SOcket CAT ».
**Subtilités/confusions :**
- Surnommé "Netcat sous stéroïdes" : supporte les fichiers, descripteurs, tuyaux, sockets IPv4/IPv6, SSL/TLS, pty et sockets Unix domain.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Ajouter l'option `fork` pour que socat accepte plusieurs connexions successives sans s'arrêter après la première.
**Équivalents :** nc, ncat
**Voir aussi :** nc, ncat, openssl
## `ncat` — Implémentation moderne de Netcat par l'équipe Nmap [Cross]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** établir des connexions TCP/UDP sécurisées avec chiffrement SSL/TLS natif, créer des tunnels d'accès
**Rôle :** Réécriture moderne, sécurisée et améliorée de Netcat fournie officiellement par le projet Nmap.
**Syntaxe :** `ncat [options] [hôte] [port]`
**Cas réguliers :**
- `ncat --ssl google.com 443` — Se connecter à un serveur web HTTPS en négociant directement une couche chiffrée SSL/TLS
- `ncat -l 8443 --ssl --exec /bin/bash` — Ouvrir un Shell d'écoute chiffré en TLS sur le port 8443
- `ncat --proxy-type http --proxy 192.168.1.254:8080 target.com 80` — Rediriger la connexion à travers un proxy HTTP
**Origine :** Nmap Project / Gordon Lyon (2009) — conçu pour remplacer les différentes variantes incompatibles de netcat.
**Subtilités/confusions :**
- Intègre de manière native le support du chiffrement SSL/TLS (`--ssl`) et des proxys HTTP/SOCKS.
- L utilisation dans des scripts automatisés nécessite de gérer le code de retour et d éventuels timeouts.
**Urgences/dangers :** —
**Précautions :** Préférer `ncat` à `nc` lorsque le support natif de SSL/TLS est nécessaire sans recourir à `openssl s_client`.
**Équivalents :** nc, socat
**Voir aussi :** nc, nmap, socat
## `bandwhich` — Affichage de l'utilisation de la bande passante par processus [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** identifier en temps réel quel processus ou conteneur consomme toute la bande passante réseau du serveur
**Rôle :** Utilitaire TUI affichant en temps réel la consommation de bande passante réseau ventilée par processus, connexion et adresse distante.
**Syntaxe :** `bandwhich [options]`
**Cas réguliers :**
- `bandwhich` — Ouvrir l'interface dynamique TUI affichant la vitesse de téléchargement/téléversement par processus
- `bandwhich -i eth0` — Surveiller exclusivement la carte réseau `eth0`
- `bandwhich --raw` — Générer un flux de données brut pour le traitement dans des scripts
**Origine :** Aram Drevekenin (2019) — écrit en Rust, autrefois nommé `what-system-is-doing-on-the-network`.
**Subtilités/confusions :**
- Nécessite les privilèges `sudo` pour capturer les paquets bruts et associer les sockets aux PIDs des processus.
- L execution avec les privilèges d administration doit être restreinte au strict nécessaire.
**Urgences/dangers :** —
**Précautions :** Idéal pour repérer un transfert Docker ou un processus en arrière-plan qui sature la ligne.
**Équivalents :** iftop, nethogs, iptraf-ng
**Voir aussi :** iftop, top, htop
## `iftop` — Affichage en temps réel de l'utilisation de la bande passante par interface [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** visualiser sous forme de graphique texte le trafic réseau entrant et sortant par paire d'hôtes distants
**Rôle :** Afficher l'utilisation de la bande passante sur une interface réseau sous forme de tableau mis à jour en temps réel (style `top`).
**Syntaxe :** `iftop [options]`
**Cas réguliers :**
- `iftop -i eth0` — Lancer l'interface TUI de surveillance de la carte `eth0`
- `iftop -n` — Masquer la résolution DNS des noms d'hôtes pour afficher directement les adresses IP numériques
- `iftop -P` — Afficher les numéros de ports réseau en plus des adresses IP
**Origine :** Paul Warren / Chris Lightfoot (2002) — acronyme de « Interface Top ».
**Subtilités/confusions :**
- Affiche trois moyennes de débit (ex: 2s, 10s, 40s) et des barres visuelles représentant le volume de données échangées.
- Nécessite les privilèges `sudo`.
**Urgences/dangers :** —
**Précautions :** Passer l'option `-n` pour éviter les ralentissements liés aux requêtes DNS inverses.
**Équivalents :** bandwhich, nethogs, bmon, nload
**Voir aussi :** bandwhich, top, iperf3
## `openssl` — Boîte à outils cryptographique SSL/TLS et gestion des certificats [Cross]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** —
**Contextes :** générer des paires de clés RSA/ECC, créer une demande de signature de certificat (CSR), vérifier la date d'expiration d'un certificat HTTPS distant
**Rôle :** Outil en ligne de commande de référence pour les fonctions cryptographiques de la bibliothèque OpenSSL (chiffrement, PKI, certificats X.509, hachage).
**Syntaxe :** `openssl <commande> [options]`
**Cas réguliers :**
- `openssl req -new -newkey rsa:4096 -nodes -keyout server.key -out server.csr` — Générer une clé privée RSA 4096 bits et sa demande CSR sans mot de passe (`-nodes`)
- `openssl x509 -in cert.pem -text -noout` — Décoder et afficher les métadonnées lisibles d'un certificat X.509
- `openssl s_client -connect example.com:443 -servername example.com` — Tester la poignée de main SSL/TLS distante avec SNI et afficher la chaîne de certificats
**Origine :** Mark J. Cox, Eric A. Young, Tim Hudson / OpenSSL Project (1998) — successeur de SSLeay.
**Subtilités/confusions :**
- `openssl s_client` est le couteau suisse ultime pour diagnostiquer les erreurs de chaîne de certificats manquante (*Intermediate CA*).
- L'option `-servername` est indispensable pour envoyer l'extension TLS SNI (*Server Name Indication*) lors du test d'un hôte virtuel HTTPS.
**Urgences/dangers :** ⚠️ Laisser une clé privée `server.key` lisible par d'autres utilisateurs (`chmod 644`) compromet la confidentialité de tout le trafic TLS.
**Précautions :** Sécuriser l'accès aux clés privées avec `chmod 600` ou `chmod 400`.
**Équivalents :** mkcert, cfssl, certbot
**Voir aussi :** certbot, ssh-keygen, gpg
## `iptables` — Administration des filtres de paquets du noyau Linux [Linux]
**Niveau :** avance | **Popularité :** 96 | **Aliases :** —
**Contextes :** configurer les règles de pare-feu réseau Linux, bloquer des adresses IP malveillantes, configurer la redirection de ports (*NAT / port forwarding*)
**Rôle :** Configurer les tables de filtrage de paquets IPv4 et la redirection du sous-système netfilter du noyau Linux.
**Syntaxe :** `iptables [-t table] <action> <chaîne> [critères] -j <cible>`
**Cas réguliers :**
- `iptables -L -n -v` — Lister toutes les règles actives avec adresses numériques (`-n`) et compteurs de paquets (`-v`)
- `iptables -A INPUT -p tcp --dport 22 -j ACCEPT` — Autoriser le trafic entrant sur le port SSH 22
- `iptables -A INPUT -s 192.168.1.50 -j DROP` — Bloquer instantanément tout paquet provenant de l'adresse IP spécifiée
**Origine :** Rusty Russell / Netfilter Core Team (1998) — remplace `ipchains` pour le noyau Linux 2.4+.
**Subtilités/confusions :**
- S'articule autour de tables (`filter`, `nat`, `mangle`, `raw`) et de chaînes d'étapes (`INPUT`, `OUTPUT`, `FORWARD`, `PREROUTING`, `POSTROUTING`).
- Les modifications de règles sont volatiles : pour les rendre permanentes au redémarrage, utiliser `iptables-save > /etc/iptables/rules.v4` ou `netfilter-persistent`.
**Urgences/dangers :** ⚠️ Executer `iptables -F` (flush) alors que la politique par défaut de la chaîne est `DROP` bloque immédiatement et définitivement la session SSH active !
**Précautions :** Toujours vérifier les règles avec `iptables -L -n` et programmer un redémarrage automatique d'urgence (`at now + 5 min`) lors de modifications à risque à distance.
**Équivalents :** nftables, ufw, firewall-cmd, pf (macOS/BSD)
**Voir aussi :** nftables, ufw, firewalld, fail2ban-client
## `nftables` — Sous-système moderne de filtrage de paquets Linux [Linux]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** nft
**Contextes :** construire des règles de pare-feu ultra-rapides et unifiées (IPv4 + IPv6) sous Linux moderne
**Rôle :** Remplaçant moderne et performant d'iptables pour le filtrage de paquets, le NAT et la classification de trafic (`nft`).
**Syntaxe :** `nft <commande> [arguments]`
**Cas réguliers :**
- `nft list ruleset` — Afficher l'ensemble du jeu de règles de pare-feu nftables actif sur le système
- `nft add rule inet filter input tcp dport 22 accept` — Ajouter une règle autorisant le port SSH en IPv4 et IPv6 unifiés (`inet`)
- `nft flush ruleset` — Réinitialiser et vider la totalité des tables et chaînes de règles
**Origine :** Patrick McHardy / Netfilter Core Team (2014) — intégré au noyau Linux 3.13+.
**Subtilités/confusions :**
- Unifie dans une seule syntaxe propre et une seule machine virtuelle noyau les anciens outils séparés (`iptables`, `ip6tables`, `arptables`, `ebtables`).
- Les opérations de mise à jour du jeu de règles sont atomiques (ex: `nft -f /etc/nftables.conf`).
**Urgences/dangers :** —
**Précautions :** Utiliser la table `inet` pour appliquer simultanément les règles de sécurité aux paquets IPv4 et IPv6.
**Équivalents :** iptables, ufw, firewalld
**Voir aussi :** iptables, ufw, firewalld
## `ufw` — Pare-feu simplifié Uncomplicated Firewall [Linux]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** sécuriser facilement un serveur Ubuntu ou Debian sans devoir maîtriser la complexité d'iptables
**Rôle :** Interface en ligne de commande simplifiée (*Uncomplicated Firewall*) pour la gestion de pare-feu sous Linux.
**Syntaxe :** `ufw <commande> [règle]`
**Cas réguliers :**
- `ufw status verbose` — Afficher le statut du pare-feu (actif/inactif) et la liste des règles de sécurité numérotées
- `ufw allow 22/tcp && ufw enable` — Autoriser le port SSH puis ACTIVER le pare-feu
- `ufw allow from 192.168.1.0/24 to any port 3306` — Autoriser l'accès à MySQL (3306) uniquement depuis le réseau local
**Origine :** Canonical / Ubuntu (2008) — conçu pour offrir un pare-feu simple d'utilisation pour le grand public et sysadmins.
**Subtilités/confusions :**
- `ufw allow OpenSSH` supporte les profils d'applications prédéfinis dans `/etc/ufw/applications.d/`.
- Les règles `ufw` sont automatiquement enregistrées et conservées au redémarrage du système.
**Urgences/dangers :** ⚠️ Exécuter `ufw enable` sans avoir préalablement autorisé le port SSH (22) verrouille l'accès distant au serveur.
**Précautions :** Toujours exécuter `ufw allow ssh` ou `ufw allow 22/tcp` AVANT d'activer avec `ufw enable`.
**Équivalents :** firewalld, iptables, nftables
**Voir aussi :** iptables, firewalld, fail2ban-client
## `firewalld` — Pare-feu dynamique par zones [RHEL/Fedora/CentOS]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** firewall-cmd
**Contextes :** administrer le pare-feu par zones sous Red Hat Enterprise Linux, Fedora, Rocky Linux ou AlmaLinux
**Rôle :** Démon de pare-feu dynamique gérant les zones réseau et les règles de filtrage via l'utilitaire `firewall-cmd`.
**Syntaxe :** `firewall-cmd [options]`
**Cas réguliers :**
- `firewall-cmd --state` — Vérifier si le démon de pare-feu est actuellement en cours d'exécution
- `firewall-cmd --permanent --add-service=http --add-service=https && firewall-cmd --reload` — Autoriser les services Web HTTP/HTTPS de manière permanente
- `firewall-cmd --zone=public --list-all` — Afficher l'ensemble des règles et services autorisés dans la zone publique
**Origine :** Thomas Woerner / Red Hat (2011) — remplace les scripts d'initialisation statiques iptables sur la famille Red Hat.
**Subtilités/confusions :**
- Si le drapeau `--permanent` n'est pas spécifié, la règle ajoutée sera perdue au prochain redémarrage ou rechargement !
- Utilise le concept de "zones" de confiance (`public`, `internal`, `trusted`, `dmz`, `drop`).
**Urgences/dangers :** —
**Précautions :** Toujours exécuter `firewall-cmd --reload` après avoir ajouté des règles avec l'option `--permanent`.
**Équivalents :** ufw, iptables, nftables
**Voir aussi :** ufw, iptables, nftables
## `fail2ban-client` — PRÉVENTION contre les attaques par force brute [Linux]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** bannir automatiquement les adresses IP d'attaquants qui tentent de deviner des mots de passe SSH ou web
**Rôle :** Outil de gestion et de contrôle du démon Fail2ban, qui surveille les journaux d'erreurs et modifie le pare-feu pour bannir les IP malveillantes.
**Syntaxe :** `fail2ban-client <commande> [jail] [action]`
**Cas réguliers :**
- `fail2ban-client status` — Afficher la liste des prisons de sécurité (*jails*) actives (ex: sshd, nginx-http-auth)
- `fail2ban-client status sshd` — Afficher le nombre d'échecs détectés et la liste complète des adresses IP actuellement bannie dans la prison SSH
- `fail2ban-client set sshd unbanip 192.168.1.50` — Débannir manuellement l'adresse IP d'un administrateur bloqué par erreur
**Origine :** Cyril Jaquier (2004) — outil défensif incontournable sur Linux.
**Subtilités/confusions :**
- Fail2ban écrit dynamiquement des règles d'interdiction provisoires dans `iptables` ou `nftables` pour une durée configurable (`bantime`).
- Les règles d'analyse d'échecs sont configurées dans `/etc/fail2ban/jail.local`.
**Urgences/dangers :** —
**Précautions :** Ajouter l'adresse IP de votre réseau d'administration dans la directive `ignoreip` de `jail.local` pour éviter de vous bannir vous-même.
**Équivalents :** sshguard, denylosts
**Voir aussi :** iptables, ufw, firewalld
## `wireguard` — Configuration du protocole VPN moderne et rapide [Cross]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** wg, wg-quick
**Contextes :** établir un tunnel VPN chiffré ultra-rapide entre deux serveurs ou pour sécuriser les connexions mobiles
**Rôle :** Consulter, configurer et administrer les interfaces du protocole de réseau privé virtuel moderne WireGuard (`wg`).
**Syntaxe :** `wg [commande]` / `wg-quick [up|down] <interface>`
**Cas réguliers :**
- `wg` — Afficher l'état du tunnel VPN, la clé publique de la machine, les pairs (*peers*) connectés et le volume de trafic échangé
- `wg-quick up wg0` — Démarrer et monter l'interface VPN à partir du fichier de configuration `/etc/wireguard/wg0.conf`
- `wg genkey | tee privatekey | wg pubkey > publickey` — Générer en une ligne la paire de clés cryptographiques privée et publique
**Origine :** Jason A. Donenfeld (2015) — intégré directement dans le noyau Linux 5.6+.
**Subtilités/confusions :**
- Écrit avec seulement ~4 000 lignes de code (contre des centaines de milliers pour OpenVPN/IPsec), offrant des performances et une sécurité incomparables.
- Repose entièrement sur la cryptographie moderne par courbe elliptique (Curve25519, ChaCha20, Poly1305).
**Urgences/dangers :** —
**Précautions :** Conserver la clé privée `privatekey` strictement confidentielle et ne partager QUE la clé publique `publickey` avec les pairs VPN.
**Équivalents :** openvpn, tailscale, ipsec
**Voir aussi :** openvpn, ip, openssl
## `openvpn` — Démon de réseau virtuel VPN basé sur SSL/TLS [Cross]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** raccorder un poste client distant au réseau de l'entreprise via un tunnel VPN TLS sécurisé
**Rôle :** Solution logicielle complète de réseau privé virtuel (VPN) créant des tunnels chiffrés routés ou bridgés.
**Syntaxe :** `openvpn [options] --config <fichier.ovpn>`
**Cas réguliers :**
- `openvpn --config client.ovpn` — Établir la connexion VPN à partir du fichier de configuration client `.ovpn`
- `openvpn --genkey secret static.key` — Générer une clé partagée pré-partagée pour un tunnel VPN point-à-point simple
**Origine :** James Yonan (2001) — solution VPN open-source historique multiplateforme.
**Subtilités/confusions :**
- Peut fonctionner sur n'importe quel port TCP ou UDP (souvent configuré sur UDP 1194 ou TCP 443 pour contourner les pare-feux stricts).
- Fonctionne au niveau de la couche 3 (mode `tun`, routé) ou de la couche 2 (mode `tap`, pont Ethernet).
**Urgences/dangers :** —
**Précautions :** Préférer le mode UDP pour limiter la latence et les problèmes d'effondrement de fenêtre TCP (*TCP meltdowns*).
**Équivalents :** wireguard, tailscale, ipsec
**Voir aussi :** wireguard, openssl
## `ssh-keygen` — Génération et gestion de paires de clés d'authentification SSH [Cross]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** —
**Contextes :** créer une clé d'accès sécurisée pour se connecter à des serveurs distants ou à des services Git (GitHub/GitLab) sans mot de passe
**Rôle :** Générer, gérer et convertir des paires de clés d'authentification pour le protocole OpenSSH.
**Syntaxe :** `ssh-keygen [options]`
**Cas réguliers :**
- `ssh-keygen -t ed25519 -C "admin@company.com"` — Générer une clé SSH ultra-sécurisée basée sur l'algorithme Ed25519 (recommandation moderne)
- `ssh-keygen -t rsa -b 4096` — Générer une clé d'ancienne génération RSA de 4096 bits
- `ssh-keygen -R 192.168.1.50` — Supprimer l'empreinte de la clé d'hôte du fichier `known_hosts` en cas de changement de serveur distant
**Origine :** Tatu Ylönen / OpenSSH Team (1999).
**Subtilités/confusions :**
- Génère deux fichiers : la clé PRIVÉE `id_ed25519` (à garder SECRÈTE) et la clé PUBLIQUE `id_ed25519.pub` (à déployer sur le serveur).
- L'algorithme `Ed25519` est aujourd'hui plus rapide, plus court et plus sécurisé que les clés RSA traditionnelles.
**Urgences/dangers :** ⚠️ Ne JAMAIS partager ou commiter votre clé privée SSH (fichier sans extension `.pub`).
**Précautions :** Protéger toujours votre clé privée SSH avec une phrase de passe (*passphrase*) solide.
**Équivalents :** puttygen (Windows)
**Voir aussi :** ssh-copy-id, ssh, openssl
## `ssh-copy-id` — Installation automatisée de clé publique SSH sur un serveur distant [Linux/macOS]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** autoriser la connexion SSH sans mot de passe à un nouveau serveur Linux venant d'être provisionné
**Rôle :** Copier automatiquement la clé publique SSH locale dans le fichier `~/.ssh/authorized_keys` du compte distant.
**Syntaxe :** `ssh-copy-id [-i fichier_cle] [utilisateur@]serveur`
**Cas réguliers :**
- `ssh-copy-id user@192.168.1.50` — Copier la clé publique par défaut sur le serveur distant (demande le mot de passe distant une dernière fois)
- `ssh-copy-id -i ~/.ssh/id_ed25519.pub -p 2222 user@remote.com` — Spécifier une clé publique exacte et un port SSH personnalisé (`-p 2222`)
**Origine :** Phil Hands / OpenSSH project (1999).
**Subtilités/confusions :**
- S'assure automatiquement que les permissions des dossiers distant `~/.ssh` (`0700`) et `authorized_keys` (`0600`) sont correctement restreintes.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Tester la connexion SSH (`ssh user@server`) dans un NOUVEAU terminal sans fermer la session courante pour vérifier que la clé fonctionne.
**Équivalents :** ssh, cat id_rsa.pub | ssh user@host "cat >> ~/.ssh/authorized_keys"
**Voir aussi :** ssh-keygen, ssh
## `gpg` — Chiffrement, déchiffrement et signature numérique OpenPGP [Cross]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** gpg2
**Contextes :** chiffrer un fichier confidentiel avant envoi par mail, signer un commit Git (`git commit -S`), vérifier les signatures de paquets Linux
**Rôle :** L'outil libre d'implémentation de la norme OpenPGP pour le chiffrement et la signature numérique de données et communications.
**Syntaxe :** `gpg [options] [commande]`
**Cas réguliers :**
- `gpg -c file.txt` — Chiffrer un fichier avec un mot de passe symétrique fort (génère `file.txt.gpg`)
- `gpg -d file.txt.gpg > file.txt` — Déchiffrer un fichier protégé
- `gpg --full-generate-key` — Générer une paire de clés d'authentification asymétrique PGP (publique/privée)
**Origine :** Werner Koch (1997) — acronyme de « GNU Privacy Guard ».
**Subtilités/confusions :**
- Permet à la fois le chiffrement symétrique par mot de passe (`-c`) et le chiffrement asymétrique par paire de clés (`-e -r recipient`).
- La version `gpg2` est la version moderne standardisée liée à `gpg-agent`.
**Urgences/dangers :** ⚠️ Perdre sa clé privée GPG ou sa passphrase rend la lecture des fichiers chiffrés définitivement impossible.
**Précautions :** Sauvegarder votre certificat de révocation et votre clé privée dans un coffre-fort sécurisé.
**Équivalents :** age, sops, openssl
**Voir aussi :** age, sops, openssl, git
## `certbot` — Automatisation des certificats SSL/TLS gratuits Let's Encrypt [Linux]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** —
**Contextes :** obtenir et renouveler automatiquement un certificat HTTPS sécurisé Let's Encrypt pour Nginx ou Apache
**Rôle :** Agent client officiel de l'autorité de certification Let's Encrypt automatisant l'obtention et le renouvellement de certificats TLS/SSL gratuits.
**Syntaxe :** `certbot [commande] [options]`
**Cas réguliers :**
- `certbot --nginx -d example.com -d www.example.com` — Obtenir un certificat SSL et modifier automatiquement la configuration Nginx
- `certbot certonly --standalone -d api.example.com` — Obtenir le certificat en mode autonome sans toucher à la configuration du serveur web
- `certbot renew --dry-run` — Tester la simulation du renouvellement automatique de tous les certificats installés
**Origine :** EFF (Electronic Frontier Foundation) / Let's Encrypt (2015) — autrefois nommé letsencrypt.
**Subtilités/confusions :**
- Les certificats Let's Encrypt expirent après 90 jours : `certbot` installe un timer systemd ou cron pour exécuter `certbot renew` automatiquement deux fois par jour.
- Les certificats obtenus sont enregistrés sous `/etc/letsencrypt/live/domaine/`.
**Urgences/dangers :** ⚠️ Dépasser les limites d'appels de l'API Let's Encrypt (*Rate Limits*) bloque les demandes de certificats pour le même domaine pendant 7 jours.
**Précautions :** Tester les nouvelles configurations avec le drapeau `--staging` ou `--dry-run` pour éviter d'atteindre les quotas de production.
**Équivalents :** acme.sh, lego, Caddy (intégré)
**Voir aussi :** openssl, nginx
## `vault` — Outil HashiCorp de gestion sécurisée des secrets et identités [Cross]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** —
**Contextes :** stocker de manière chiffrée des clés d'API, mots de passe de BDD et jetons d'accès dans un coffre-fort centralisé d'entreprise
**Rôle :** Outil de gestion des secrets, d'accès privilégiés et de chiffrement des données de l'écosystème Cloud Native.
**Syntaxe :** `vault <commande> [sous_commande] [options]`
**Cas réguliers :**
- `vault kv get secret/db_credentials` — Récupérer un secret stocké dans le magasin Key-Value de Vault
- `vault kv put secret/db_credentials password="SuperSecretPassword"` — Enregistrer une nouvelle paire clé/valeur de secret chiffré
- `vault status` — Afficher l'état de verrouillage (*seal status*) et la santé de l'instance Vault
**Origine :** Mitchell Hashimoto & Armon Dadgar / HashiCorp (2015).
**Subtilités/confusions :**
- Un serveur Vault démarré est initialement dans un état "scellé" (*sealed*) et doit être déverrouillé (*unsealed*) avec un quorum de clés Shamir.
- Génère dynamiquement des identifiants d'accès temporaires à durée de vie limitée (*leases*).
**Urgences/dangers :** —
**Précautions :** Conserver les clés de déverrouillage (*unseal keys*) entre les mains de plusieurs administrateurs distincts.
**Équivalents :** AWS Secrets Manager, SOPS, Bitwarden CLI
**Voir aussi :** sops, age, consul
## `age` — Outil moderne et simple de chiffrement de fichiers [Cross]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** chiffrer rapidement un fichier de sauvegarde ou une archive avant de la stocker sur un Cloud public
**Rôle :** Outil de chiffrement de fichiers simple, moderne et sécurisé conçu comme une alternative légère à GPG.
**Syntaxe :** `age [options] [fichier]`
**Cas réguliers :**
- `age -p secret.txt > secret.txt.age` — Chiffrer un fichier avec une simple mot de passe symétrique saisi au clavier
- `age -d secret.txt.age > secret.txt` — Déchiffrer le fichier protégé
- `age -r age1qqqq... backup.tar.gz > backup.tar.gz.age` — Chiffrer un fichier à destination d'une clé publique `age` spécifique
**Origine :** Filippo Valsorda (2019) — acronyme de « Actually Good Encryption ».
**Subtilités/confusions :**
- Utilise des clés publiques et privées courtes très lisibles (format `age1...`).
- Conçu pour remplacer les options complexes et historiques de GPG par une syntaxe UNIX moderne et épurée.
**Urgences/dangers :** —
**Précautions :** Conserver la clé privée `key.txt` générée par `age-keygen` en lieu sûr.
**Équivalents :** gpg, sops, openssl enc
**Voir aussi :** gpg, sops
## `sops` — Chiffrement de fichiers de configuration structurés (JSON/YAML) [Cross]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** chiffrer uniquement les valeurs sensibles de fichiers de configuration Kubernetes/Ansible/YAML dans Git tout en laissant les clés visibles
**Rôle :** Outil d'édition et de chiffrement de fichiers de configuration structurés (YAML, JSON, ENV, INI) intégrant AWS KMS, GCP KMS, Vault et Age/GPG.
**Syntaxe :** `sops [options] <fichier>`
**Cas réguliers :**
- `sops secrets.yaml` — Ouvrir et modifier le fichier YAML chiffré dans l'éditeur : les valeurs sont déchiffrées en mémoire puis rechiffrées à la sauvegarde !
- `sops -e -i --age age1... config.yaml` — Chiffrer en place (`-i`) les valeurs du fichier avec une clé `age`
- `sops -d secrets.yaml` — Déchiffrer et afficher le contenu brut sur la sortie standard
**Origine :** Mozilla / Julien Vehent (2015) — acronyme de « Secrets OPerationS ».
**Subtilités/confusions :**
- La magie de SOPS est de ne chiffrer QUE les VALEURS des clés YAML/JSON, permettant de faire des `git diff` lisibles sur la structure du fichier sans exposer les secrets.
- Vérifier le code de retour (0 ou exit status) dans les scripts shell pour détecter les échecs de commande.
**Urgences/dangers :** —
**Précautions :** Définir le fichier de règles `.sops.yaml` à la racine de votre dépôt Git pour attribuer automatiquement les bonnes clés de chiffrement.
**Équivalents :** git-secret, git-crypt, vault, age
**Voir aussi :** age, vault, gpg, git


## `nmcli` — Contrôle de NetworkManager en ligne de commande [Linux]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** configurer des connexions réseau filaires ou Wi-Fi sur un serveur Linux sans interface graphique, créer des VPN ou des hotspots, scripter la gestion réseau
**Rôle :** Interface CLI pour NetworkManager : affiche l'état des périphériques réseau, crée/modifie/active des connexions (Ethernet, Wi-Fi, VPN, Bond, Bridge).
**Syntaxe :** `nmcli [options] <objet> <commande> [args]`
**Cas réguliers :**
- `nmcli device status` — Lister tous les périphériques réseau et leur état (connecté, déconnecté, géré…)
- `nmcli connection show` — Afficher toutes les connexions configurées (profils)
- `nmcli connection up "Ma Connexion"` — Activer une connexion par son nom
**Origine :** Projet NetworkManager (Red Hat, 2004) — outil de gestion réseau dynamique pour Linux.
**Subtilités/confusions :**
- `nmcli device` concerne les interfaces physiques ; `nmcli connection` concerne les profils de configuration.
- `nmcli general hostname nouveau-nom` change le nom d'hôte de façon persistante.
**Urgences/dangers :** `nmcli connection delete` supprime un profil de façon irréversible.
**Précautions :** Tester les modifications réseau en local avant de les appliquer sur un serveur distant (risque de déconnexion SSH).
**Équivalents :** ip, ifup/ifdown, netplan apply (Ubuntu), systemd-networkd
**Voir aussi :** ip, networkctl, resolvectl
## `networkctl` — Inspection des liens réseau gérés par systemd-networkd [Linux]
**Niveau :** intermediaire | **Popularité :** 72 | **Aliases :** —
**Contextes :** inspecter l'état des interfaces réseau sur un système utilisant `systemd-networkd` (serveurs minimalistes, conteneurs), vérifier les adresses IP, le débit et la qualité du lien
**Rôle :** Outil de contrôle et d'inspection de `systemd-networkd` : liste les liens réseau, affiche leur configuration IP et leur état opérationnel.
**Syntaxe :** `networkctl [options] [commande] [lien]`
**Cas réguliers :**
- `networkctl list` — Lister tous les liens réseau avec leur état (routable, degraded, carrier…)
- `networkctl status eth0` — Afficher les détails d'une interface : adresses IP, passerelle, DNS, statistiques
- `networkctl reload` — Recharger la configuration de `systemd-networkd` sans redémarrer le service
**Origine :** Projet systemd (Lennart Poettering, 2014) — composant `systemd-networkd` dédié à la configuration réseau des systèmes embarqués et serveurs.
**Subtilités/confusions :**
- `networkctl` ne fonctionne que si le service `systemd-networkd` est actif ; ne remplace pas NetworkManager.
- L'état `degraded` signifie qu'au moins un lien n'est pas pleinement opérationnel, mais que d'autres le sont.
**Urgences/dangers :** —
**Précautions :** Sur les systèmes avec NetworkManager (Desktop Ubuntu), utiliser `nmcli` à la place.
**Équivalents :** nmcli, ip link
**Voir aussi :** nmcli, resolvectl, systemctl
## `resolvectl` — Diagnostic et contrôle du résolveur DNS systemd [Linux]
**Niveau :** intermediaire | **Popularité :** 75 | **Aliases :** `systemd-resolve`
**Contextes :** diagnostiquer des problèmes de résolution DNS sur un poste ou serveur Linux moderne, vérifier quels serveurs DNS sont utilisés pour chaque interface, vider le cache DNS
**Rôle :** Interface CLI pour `systemd-resolved` : effectue des requêtes DNS, affiche l'état du résolveur, vide le cache et configure les serveurs DNS par interface.
**Syntaxe :** `resolvectl [commande] [args]`
**Cas réguliers :**
- `resolvectl status` — Afficher la configuration DNS globale et par interface (serveurs, domaines, DNSSEC)
- `resolvectl query exemple.com` — Résoudre un nom de domaine via le résolveur systemd-resolved
- `resolvectl flush-caches` — Vider le cache DNS de systemd-resolved
**Origine :** Projet systemd (2016) — composant `systemd-resolved` pour la résolution DNS moderne avec support DNSSEC et DNS-over-TLS.
**Subtilités/confusions :**
- Remplace l'ancienne commande `systemd-resolve` (disponible comme alias).
- Si `/etc/resolv.conf` n'est pas un lien symbolique vers `/run/systemd/resolve/stub-resolv.conf`, les résolutions peuvent diverger.
**Urgences/dangers :** —
**Précautions :** Vérifier que `systemd-resolved` est actif (`systemctl status systemd-resolved`) avant d'utiliser `resolvectl`.
**Équivalents :** dig, nslookup, host
**Voir aussi :** dig, nmcli, networkctl
## `ipset` — Gestion de jeux d'adresses IP pour iptables [Linux]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** —
**Contextes :** bloquer efficacement des milliers d'adresses IP ou plages CIDR en une seule règle iptables, maintenir des listes noires dynamiques, implémenter du geo-blocking
**Rôle :** Outil de gestion de « jeux » d'adresses IP, de ports ou de réseaux permettant d'écrire des règles iptables/nftables compactes et performantes pour filtrer de très grandes listes.
**Syntaxe :** `ipset [commande] [nom_set] [options]`
**Cas réguliers :**
- `ipset create blocklist hash:net` — Créer un jeu nommé `blocklist` de type réseau (hash de plages CIDR)
- `ipset add blocklist 192.168.1.0/24` — Ajouter une plage CIDR au jeu
- `ipset list blocklist` — Afficher le contenu du jeu et ses statistiques
**Origine :** Projet Netfilter (Jozsef Kadlecsik, 2003) — extension du noyau Linux pour la gestion de jeux IP.
**Subtilités/confusions :**
- Un jeu `ipset` seul ne filtre rien ; il doit être référencé dans une règle `iptables -m set --match-set blocklist src -j DROP`.
- Les types `hash:ip`, `hash:net`, `hash:ip,port` couvrent les cas d'usage courants.
**Urgences/dangers :** Un jeu mal configuré peut bloquer des adresses légitimes, provoquant une perte d'accès réseau.
**Précautions :** Tester les règles en environnement de préproduction ; sauvegarder les jeux avec `ipset save > backup.ipset`.
**Équivalents :** nftables sets, firewalld rich rules
**Voir aussi :** iptables, nftables, firewalld
## `masscan` — Scan de ports ultra-rapide sur internet [Linux]
**Niveau :** avance | **Popularité :** 80 | **Aliases :** —
**Contextes :** scanner des plages entières d'adresses internet pour découvrir des hôtes exposant des ports ouverts (usage : audit de surface d'attaque, red team), pentesting autorisé
**Rôle :** Scanner de ports asynchrone de type « stateless » capable de scanner l'intégralité d'Internet en moins de 6 minutes grâce à une pile TCP/IP personnalisée haute performance.
**Syntaxe :** `masscan <cible> -p <ports> [options]`
**Cas réguliers :**
- `masscan 192.168.1.0/24 -p 80,443,22` — Scanner un sous-réseau local sur 3 ports courants
- `masscan 10.0.0.0/8 -p 0-65535 --rate=1000` — Scanner toute la plage 10.0.0.0/8 à 1000 paquets/s
- `masscan 192.168.1.0/24 -p 443 -oJ results.json` — Exporter les résultats en JSON
**Origine :** Robert David Graham (2013) — conçu pour battre nmap en vitesse sur de très grandes plages.
**Subtilités/confusions :**
- `masscan` ne fait pas de détection de service (pas de `-sV` comme nmap) ; il ne détecte que les ports ouverts.
- Le paramètre `--rate` est crucial : des valeurs trop élevées saturent les routeurs et déclenchent des alertes IDS.
**Urgences/dangers :** ⚠️ Scanner des réseaux sans autorisation explicite est illégal. Usage uniquement sur vos propres infrastructures ou avec permission écrite.
**Précautions :** Toujours obtenir une autorisation écrite avant tout scan. Limiter le débit (`--rate`) pour éviter de saturer les équipements réseau.
**Équivalents :** nmap, rustscan, zmap
**Voir aussi :** nmap, rustscan, ncat
## `rustscan` — Scanner de ports moderne en Rust [Cross]
**Niveau :** intermediaire | **Popularité :** 76 | **Aliases :** —
**Contextes :** scanner rapidement tous les ports ouverts d'une cible avant de passer nmap uniquement sur les ports détectés, accélérer les phases de reconnaissance en CTF ou pentest autorisé
**Rôle :** Scanner de ports ultra-rapide écrit en Rust qui détecte les ports ouverts puis passe automatiquement la main à nmap pour la détection de services.
**Syntaxe :** `rustscan -a <cible> [options] -- [options_nmap]`
**Cas réguliers :**
- `rustscan -a 192.168.1.1` — Scanner tous les 65535 ports de l'hôte cible rapidement
- `rustscan -a 192.168.1.1 -- -sV -sC` — Scanner puis passer les ports ouverts à nmap avec détection de version et scripts
- `rustscan -a 192.168.1.0/24 -p 22,80,443` — Scanner un sous-réseau sur des ports spécifiques
**Origine :** Brandon Pfeifer (2020) — écrit en Rust pour la performance ; adopté en CTF.
**Subtilités/confusions :**
- `rustscan` n'effectue lui-même que la détection de ports ; tout ce qui suit `--` est transmis directement à nmap.
- Plus rapide que nmap seul mais nécessite nmap installé pour la phase d'analyse de service.
**Urgences/dangers :** ⚠️ Même avertissement que nmap et masscan : usage réservé aux cibles autorisées.
**Précautions :** Vérifier les permissions légales avant tout scan.
**Équivalents :** nmap, masscan, zmap
**Voir aussi :** nmap, masscan
## `nikto` — Scanner de vulnérabilités de serveurs web [Cross]
**Niveau :** intermediaire | **Popularité :** 82 | **Aliases :** —
**Contextes :** auditer un serveur web pour détecter des fichiers sensibles exposés, des en-têtes HTTP manquants, des versions obsolètes de logiciels ou des configurations dangereuses ; usage : tests de pénétration web autorisés
**Rôle :** Scanner de vulnérabilités web open source qui effectue plus de 6700 tests : fichiers dangereux, versions obsolètes, erreurs de configuration HTTP et problèmes de sécurité connus.
**Syntaxe :** `nikto -h <hôte> [options]`
**Cas réguliers :**
- `nikto -h http://192.168.1.1` — Lancer un scan complet de vulnérabilités sur un serveur web
- `nikto -h https://mon-site.com -ssl` — Scanner un site HTTPS
- `nikto -h 192.168.1.1 -o rapport.html -Format html` — Exporter les résultats en HTML
**Origine :** Chris Sullo (2001, CIRT.net) — l'un des scanners web open source les plus anciens et encore largement utilisés.
**Subtilités/confusions :**
- Nikto est bruyant et non furtif : il laisse des traces massives dans les logs du serveur ciblé.
- Il produit beaucoup de faux positifs ; les résultats doivent être vérifiés manuellement.
**Urgences/dangers :** ⚠️ Utiliser uniquement sur des cibles pour lesquelles vous avez une autorisation explicite.
**Précautions :** Coupler avec d'autres outils (nmap, gobuster) pour une analyse complète ; vérifier chaque finding manuellement.
**Équivalents :** wpscan (WordPress), skipfish, nuclei
**Voir aussi :** nmap, gobuster, curl
## `gobuster` — Brute-force de répertoires et sous-domaines web [Cross]
**Niveau :** intermediaire | **Popularité :** 84 | **Aliases :** —
**Contextes :** découvrir des répertoires cachés, des fichiers exposés ou des sous-domaines non référencés sur un serveur web lors d'un test de pénétration autorisé ou d'un audit de sécurité
**Rôle :** Outil de brute-force de chemins web, sous-domaines (DNS) et buckets S3 utilisant des listes de mots (wordlists) pour découvrir des ressources non liées.
**Syntaxe :** `gobuster <mode> -u <url> -w <wordlist> [options]`
**Cas réguliers :**
- `gobuster dir -u http://cible.com -w /usr/share/wordlists/dirb/common.txt` — Brute-forcer les répertoires d'un site avec la wordlist common.txt
- `gobuster dns -d cible.com -w /usr/share/wordlists/subdomains.txt` — Découvrir des sous-domaines via DNS
- `gobuster dir -u http://cible.com -w common.txt -x php,html,txt` — Chercher des extensions de fichiers spécifiques
**Origine :** OJ Reeves (2015) — écrit en Go pour la performance ; concurrent populaire de dirb et dirbuster.
**Subtilités/confusions :**
- Les modes `dir` (répertoires), `dns` (sous-domaines) et `s3` (buckets) ont des syntaxes légèrement différentes.
- L'option `-x` est cruciale en mode `dir` pour tester des extensions spécifiques (`.php`, `.bak`, `.sql`…).
**Urgences/dangers :** ⚠️ Usage uniquement sur des cibles autorisées ; le brute-force peut déclencher des bans IP ou des alertes WAF.
**Précautions :** Utiliser des wordlists adaptées au contexte (CMS, langages de programmation) pour de meilleurs résultats.
**Équivalents :** ffuf, dirb, feroxbuster, dirsearch
**Voir aussi :** nikto, ffuf, curl, nmap
## `hashcat` — Craquage de hachages par GPU [Cross]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** —
**Contextes :** récupérer des mots de passe à partir de hachages lors d'un test de pénétration autorisé, tester la robustesse de la politique de mots de passe d'une organisation
**Rôle :** Outil de récupération de mots de passe (cracking) exploitant la puissance des GPU via OpenCL/CUDA pour attaquer des centaines de types de hachages (MD5, bcrypt, NTLM, SHA-256…).
**Syntaxe :** `hashcat -m <mode> -a <attaque> <hachage_ou_fichier> <wordlist_ou_masque>`
**Cas réguliers :**
- `hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt` — Attaque par dictionnaire sur des hachages MD5 (mode 0) avec rockyou.txt
- `hashcat -m 1000 -a 3 hash.txt ?u?l?l?l?d?d` — Attaque par masque sur un hash NTLM (1 majuscule + 3 minuscules + 2 chiffres)
- `hashcat -m 3200 -a 0 bcrypt.txt rockyou.txt --show` — Afficher les mots de passe déjà craqués (bcrypt, mode 3200)
**Origine :** Jens Steube « atom » (2009) — devenu le standard industriel du craquage de hachages.
**Subtilités/confusions :**
- `-m` = type de hachage (`hashcat --help | grep MD5`) ; `-a` = type d'attaque (0=dict, 1=combo, 3=masque, 6=hybride).
- Les GPU sont 10 à 100× plus rapides que les CPU pour le craquage.
**Urgences/dangers :** ⚠️ Utiliser uniquement sur des hachages que vous êtes légalement autorisé à tester.
**Précautions :** Surveiller la température GPU pendant les sessions longues ; sur VM sans GPU, utiliser `-D 1` (CPU uniquement).
**Équivalents :** john (John the Ripper), ophcrack, crunch
**Voir aussi :** john, gpg, openssl
## `john` — John the Ripper, craquage de mots de passe [Cross]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** `john the ripper`, `jtr`
**Contextes :** récupérer des mots de passe à partir de fichiers `/etc/shadow` ou de hachages extraits d'une base de données lors d'un audit de sécurité autorisé, identifier les mots de passe faibles
**Rôle :** Outil de craquage de mots de passe polyvalent supportant plus de 400 formats de hachages : attaques par dictionnaire, par force brute, par règles et incrémentale (mode intelligent).
**Syntaxe :** `john [options] <fichier_hachages>`
**Cas réguliers :**
- `john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt` — Attaque par dictionnaire sur un fichier shadow Linux
- `john --show shadow.txt` — Afficher les mots de passe déjà craqués
- `unshadow /etc/passwd /etc/shadow > combined.txt && john combined.txt` — Combiner passwd et shadow puis lancer john
**Origine :** Solar Designer / Openwall Project (1997) — l'un des outils de sécurité les plus anciens et réputés.
**Subtilités/confusions :**
- `john` auto-détecte souvent le format de hachage ; utiliser `--format=` pour forcer si nécessaire.
- La commande `unshadow` (incluse) est nécessaire pour préparer les fichiers shadow Linux.
**Urgences/dangers :** ⚠️ Usage légal uniquement (test de vos propres systèmes ou avec autorisation écrite).
**Précautions :** Définir une politique de mots de passe robuste (longueur ≥12, complexité) pour que le craquage soit impraticable.
**Équivalents :** hashcat, hydra, ophcrack
**Voir aussi :** hashcat, hydra (si présent), openssl
## `lynis` — Audit de sécurité complet d'un système Linux [Linux/macOS]
**Niveau :** intermediaire | **Popularité :** 83 | **Aliases :** —
**Contextes :** auditer la sécurité d'un serveur Linux avant une mise en production, obtenir un score de durcissement (hardening), identifier les configurations non sécurisées et les vulnérabilités courantes
**Rôle :** Outil d'audit de sécurité système open source qui analyse plus de 300 points de contrôle : authentification, réseau, noyau, services, journaux, chiffrement, permissions, conformité (PCI-DSS, CIS).
**Syntaxe :** `lynis [commande] [options]`
**Cas réguliers :**
- `lynis audit system` — Lancer un audit complet du système (nécessite root pour les tests complets)
- `lynis audit system --quick` — Audit rapide sans interaction
- `lynis show details <TEST-ID>` — Afficher les détails et recommandations d'un test spécifique
**Origine :** Michael Boelen / CISOfy (2007) — successeur de rkhunter pour l'audit de durcissement.
**Subtilités/confusions :**
- Lynis ne modifie rien ; il analyse et recommande seulement.
- Le score de durcissement (`Hardening index`) va de 0 à 100 ; viser ≥ 75 en production.
**Urgences/dangers :** —
**Précautions :** Exécuter en tant que root pour accéder à tous les fichiers système et obtenir un audit complet.
**Équivalents :** openscap, tiger, rkhunter, chkrootkit
**Voir aussi :** auditd, fail2ban-client, ufw
## `auditd` — Démon d'audit de sécurité Linux [Linux]
**Niveau :** avance | **Popularité :** 78 | **Aliases :** `auditctl`, `ausearch`, `aureport`
**Contextes :** tracer l'accès aux fichiers sensibles (`/etc/passwd`, clés SSH), auditer les appels système suspects pour la conformité (PCI-DSS, SOX, HIPAA), détecter des intrusions post-incident
**Rôle :** Sous-système d'audit du noyau Linux qui enregistre les événements de sécurité (accès fichiers, appels système, connexions, escalades de privilèges) dans un journal inaltérable.
**Syntaxe :** `auditctl [options]` (configuration des règles), `ausearch [options]` (recherche), `aureport [options]` (rapports)
**Cas réguliers :**
- `auditctl -w /etc/passwd -p wa -k passwd_changes` — Surveiller les écritures et modifications d'attributs sur `/etc/passwd`
- `ausearch -k passwd_changes` — Rechercher tous les événements liés à la clé `passwd_changes`
- `aureport --auth` — Générer un rapport d'authentification (tentatives réussies et échouées)
**Origine :** Red Hat / Steve Grubb (2003) — intégré au noyau Linux 2.6 comme sous-système `audit`.
**Subtilités/confusions :**
- `auditd` est le démon ; `auditctl` configure les règles ; `ausearch` recherche dans les logs ; `aureport` génère des rapports statistiques.
- Les règles `auditctl` sont temporaires ; les rendre persistantes dans `/etc/audit/rules.d/*.rules`.
**Urgences/dangers :** Des règles trop nombreuses peuvent dégrader les performances du système (I/O).
**Précautions :** Archiver régulièrement les logs d'audit (`/var/log/audit/audit.log`) pour la conformité réglementaire.
**Équivalents :** sysdig, falco, osquery
**Voir aussi :** lynis, fail2ban-client, sops
## `last` — Historique des dernières connexions utilisateur [Linux/macOS]
**Niveau :** debutant | **Popularité :** 86 | **Aliases :** —
**Contextes :** vérifier qui s'est connecté sur un serveur et quand, détecter des connexions suspectes depuis des adresses IP inconnues, auditer les horaires d'accès après un incident de sécurité
**Rôle :** Affiche l'historique des connexions et déconnexions utilisateur en lisant le fichier binaire `/var/log/wtmp`, avec les horaires, la durée de session et l'adresse IP d'origine.
**Syntaxe :** `last [options] [utilisateur] [tty]`
**Cas réguliers :**
- `last` — Afficher tout l'historique des connexions (plus récent en premier)
- `last -n 20` — Afficher les 20 dernières connexions
- `last root` — Afficher uniquement les connexions du compte root
**Origine :** Utilitaire UNIX historique (AT&T Unix, 1970s) — disponible sur pratiquement tous les systèmes UNIX/Linux.
**Subtilités/confusions :**
- `lastb` (Last Bad) affiche les tentatives de connexion échouées (fichier `/var/log/btmp`), souvent plus intéressant pour détecter des attaques.
- `lastlog` affiche la dernière connexion de CHAQUE utilisateur (non l'historique complet).
**Urgences/dangers :** —
**Précautions :** Le fichier `wtmp` peut être effacé ou falsifié par un attaquant ayant les droits root ; ne pas s'y fier comme seule source de vérité forensique.
**Équivalents :** lastlog, who, w, journalctl
**Voir aussi :** lastlog, who, auditd, ssh
## `lastlog` — Dernière connexion de chaque compte utilisateur [Linux/macOS]
**Niveau :** debutant | **Popularité :** 78 | **Aliases :** —
**Contextes :** vérifier que des comptes de service ou des comptes dormants ne se sont jamais connectés (ou ne se sont pas connectés récemment), auditer les comptes système inactifs
**Rôle :** Affiche la date, l'heure et l'adresse IP de la dernière connexion pour CHAQUE utilisateur du système en lisant le fichier binaire `/var/log/lastlog`.
**Syntaxe :** `lastlog [options]`
**Cas réguliers :**
- `lastlog` — Afficher la dernière connexion de tous les utilisateurs du système
- `lastlog -u adolphe` — Afficher la dernière connexion d'un utilisateur spécifique
- `lastlog -b 30` — Afficher les utilisateurs qui ne se sont pas connectés depuis plus de 30 jours (candidats à la désactivation)
**Origine :** Utilitaire UNIX historique — composant du paquet `shadow-utils` / `util-linux`.
**Subtilités/confusions :**
- Affiche « **Never logged in** » pour les comptes système qui ne se connectent jamais (daemon, www-data…) — c'est normal.
- `-b <jours>` (before) et `-t <jours>` (time) permettent de filtrer par ancienneté de connexion.
**Urgences/dangers :** —
**Précautions :** Identifier et désactiver régulièrement les comptes humains avec « Never logged in » ou une connexion > 90 jours.
**Équivalents :** last, who, w
**Voir aussi :** last, auditd, lynis
## `auditctl` — Configuration des règles d'audit noyau Linux en temps réel [Linux]
**Niveau :** avance | **Popularité :** 73 | **Aliases :** —
**Contextes :** ajouter ou supprimer des règles d'audit dynamiquement sans redémarrer `auditd`, tester de nouvelles règles de surveillance avant de les rendre persistantes, lister les règles actives
**Rôle :** Outil de contrôle du sous-système d'audit Linux permettant de définir des règles de surveillance en temps réel : surveiller des appels système, des fichiers, des répertoires ou des exécutables.
**Syntaxe :** `auditctl [options]`
**Cas réguliers :**
- `auditctl -l` — Lister toutes les règles d'audit actuellement actives
- `auditctl -w /etc/shadow -p wa -k shadow_access` — Surveiller les écritures/modifications d'attributs sur `/etc/shadow`
- `auditctl -a always,exit -F arch=b64 -S execve -k exec_log` — Tracer tous les appels système `execve` (exécution de programmes) sur architecture 64 bits
**Origine :** Red Hat / Steve Grubb (2003) — composant userspace du sous-système `audit` du noyau Linux 2.6.
**Subtilités/confusions :**
- Les règles `auditctl` sont perdues au redémarrage ; les persister dans `/etc/audit/rules.d/audit.rules` via `augenrules --load`.
- `auditctl -D` supprime TOUTES les règles actives (pratique pour réinitialiser, dangereux en production).
**Urgences/dangers :** ⚠️ `auditctl -D` en production supprime instantanément toute surveillance ; toujours recharger les règles persistantes immédiatement après.
**Précautions :** Tester les règles en environnement de développement pour mesurer leur impact sur les performances I/O avant de les déployer.
**Équivalents :** auditd (gestion globale), falco, osquery
**Voir aussi :** auditd, ausearch, aureport, lynis