# Face B — Abréviations et Acronymes (vague 1/4 : 55/200 — matériel, réseau, web, programmation)

| sigle | signification | catégorie | description | exemple | voir_aussi |
|---|---|---|---|---|---|
| CPU | Central Processing Unit | Matériel | Processeur, exécute les instructions des programmes | `Intel Core i7, AMD Ryzen 7` | GPU, RAM |
| RAM | Random Access Memory | Matériel | Mémoire vive de travail, effacée à l'arrêt | `16 Go de RAM DDR4` | ROM, SSD |
| ROM | Read Only Memory | Matériel | Mémoire non volatile, non modifiable en usage normal | `BIOS stocké en ROM` | RAM, BIOS |
| GPU | Graphics Processing Unit | Matériel | Processeur graphique, calcul parallèle et IA | `NVIDIA RTX 4060` | CPU |
| SSD | Solid State Drive | Stockage | Disque à mémoire flash, rapide et silencieux | `SSD NVMe 1 To` | HDD |
| HDD | Hard Disk Drive | Stockage | Disque magnétique rotatif, grande capacité pas chère | `HDD 2 To 7200 tr/min` | SSD |
| USB | Universal Serial Bus | Matériel | Connectique universelle pour périphériques | `Clé USB 3.0` | — |
| HDMI | High Definition Multimedia Interface | Matériel | Connectique audio-vidéo haute définition | `Câble HDMI 2.1` | — |
| OS | Operating System | Système | Système d'exploitation qui pilote le matériel | `Linux, Windows 11, macOS` | BIOS, CLI |
| BIOS | Basic Input Output System | Système | Firmware historique de démarrage du PC | `Accéder au BIOS avec F2` | UEFI |
| UEFI | Unified Extensible Firmware Interface | Système | Successeur moderne du BIOS avec Secure Boot | `Boot UEFI, Secure Boot` | BIOS |
| VM | Virtual Machine | Système | Machine virtuelle émulant un ordinateur complet | `VM Ubuntu sous VirtualBox` | OS |
| CLI | Command Line Interface | Système | Interface en ligne de commande au clavier | `Terminal, PowerShell` | GUI |
| GUI | Graphical User Interface | Système | Interface graphique avec fenêtres et souris | `Windows, GNOME` | CLI |
| IP | Internet Protocol | Réseau | Protocole d'adressage des machines en réseau | `192.168.1.1 et IPv6 ::1` | DNS, TCP |
| DNS | Domain Name System | Réseau | Annuaire qui traduit les noms en adresses IP | `google.com vers 142.250.x.x` | IP, DHCP |
| DHCP | Dynamic Host Configuration Protocol | Réseau | Attribution automatique des adresses IP | `La box distribue les IP en DHCP` | DNS, IP |
| TCP | Transmission Control Protocol | Réseau | Transport fiable en mode connecté | `HTTP sur TCP port 80` | UDP, IP |
| UDP | User Datagram Protocol | Réseau | Transport rapide sans connexion ni garantie | `DNS et streaming sur UDP` | TCP |
| LAN | Local Area Network | Réseau | Réseau local d'un bâtiment ou domicile | `LAN 192.168.1.0/24` | WAN |
| WAN | Wide Area Network | Réseau | Réseau étendu sur de longues distances | `Internet est un WAN` | LAN |
| WiFi | Wireless Fidelity (usage) | Réseau | Réseau local sans fil normalisé IEEE 802.11 | `WiFi 6 avec WPA3` | LAN |
| FTP | File Transfer Protocol | Réseau | Transfert de fichiers, non chiffré | `ftp serveur.fr port 21` | SSH |
| SSH | Secure SHell | Réseau | Shell distant chiffré et transfert sécurisé | `ssh ada@serveur.fr` | FTP, VPN |
| VPN | Virtual Private Network | Réseau | Tunnel chiffré vers un réseau distant | `WireGuard, OpenVPN` | SSH |
| HTTP | HyperText Transfer Protocol | Web | Protocole du Web non chiffré port 80 | `http://example.com` | HTTPS |
| HTTPS | HTTP Secure | Web | HTTP chiffré par TLS port 443 | `https://banque.fr` | HTTP, SSL |
| URL | Uniform Resource Locator | Web | Adresse complète d'une ressource | `https://site.fr/page?id=1` | URI, DNS |
| URI | Uniform Resource Identifier | Web | Identifiant de ressource, sur-ensemble d'URL | `mailto:contact@site.fr` | URL |
| HTML | HyperText Markup Language | Web | Langage de structure des pages Web | `<h1>Titre</h1>` | CSS, JS |
| CSS | Cascading Style Sheets | Web | Feuilles de style pour la présentation | `body { color: red; }` | HTML |
| JS | JavaScript | Programmation | Langage du Web interactif côté client et serveur | `console.log('bonjour')` | TS, HTML |
| TS | TypeScript | Programmation | JavaScript typé compilé par Microsoft | `const x: number = 1` | JS |
| JSON | JavaScript Object Notation | Programmation | Format d'échange léger clé-valeur | `{"nom": "Ada"}` | XML, YAML |
| XML | eXtensible Markup Language | Programmation | Format balisé extensible et verbeux | `<nom>Ada</nom>` | JSON |
| YAML | YAML Ain't Markup Language | Programmation | Format lisible pour la configuration | `nom: Ada` | JSON |
| API | Application Programming Interface | Programmation | Interface pour faire dialoguer des logiciels | `GET /api/users` | SDK, REST |
| SDK | Software Development Kit | Programmation | Kit de développement pour une plateforme | `Android SDK` | API |
| IDE | Integrated Development Environment | Programmation | Environnement de développement complet | `VS Code, IntelliJ` | CLI |
| SQL | Structured Query Language | Programmation | Langage des bases de données relationnelles | `SELECT * FROM users` | SGBD |
| SGBD | Système de Gestion de Base de Données | Programmation | Logiciel qui gère les bases de données | `PostgreSQL, MySQL` | SQL |
| ORM | Object Relational Mapping | Programmation | Pont entre objets code et tables SQL | `Prisma, SQLAlchemy` | SQL |
| REST | REpresentational State Transfer | Web | Style d'API HTTP avec verbes et ressources | `GET POST PUT DELETE` | API |
| SMTP | Simple Mail Transfer Protocol | Réseau | Envoi des e-mails port 25 | `Serveur SMTP smtp.site.fr` | IMAP |
| IMAP | Internet Message Access Protocol | Réseau | Lecture des e-mails conservés sur serveur | `Port 993 en TLS` | SMTP, POP3 |
| POP3 | Post Office Protocol v3 | Réseau | Téléchargement des e-mails port 110 | `Récupérer les mails en POP` | IMAP |
| SSL | Secure Sockets Layer | Sécurité | Ancien protocole de chiffrement, remplacé par TLS | `Ne plus utiliser SSL` | TLS, HTTPS |
| TLS | Transport Layer Security | Sécurité | Chiffrement moderne des échanges | `TLS 1.3 sur HTTPS` | SSL |
| MFA | Multi Factor Authentication | Sécurité | Double preuve d'identité pour se connecter | `Mot de passe + code SMS` | 2FA |
| 2FA | Two Factor Authentication | Sécurité | Cas particulier de MFA avec deux facteurs | `Code TOTP à 6 chiffres` | MFA |
| DDoS | Distributed Denial of Service | Sécurité | Attaque par saturation depuis un botnet | `Attaque DDoS 1 Tbps` | VPN, Firewall |
| IA | Intelligence Artificielle | Concept | Systèmes simulant des capacités cognitives | `LLM comme Muse` | ML |
| ML | Machine Learning | Concept | Apprentissage automatique à partir de données | `Régression, clustering` | IA, DL |
| DL | Deep Learning | Concept | Réseaux de neurones profonds | `CNN pour la vision` | ML |
