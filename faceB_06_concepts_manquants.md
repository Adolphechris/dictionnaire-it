# Face B — Concepts manquants (liens voir aussi repares)

## `Cloud` — Cloud Computing [Cloud]
**Catégorie :** Cloud | **Niveau :** debutant | **Popularité :** 96
**Signification :** Cloud Computing (informatique en nuage)
**Contextes :** héberger une application sans datacenter propre, absorber des pics de charge, tester une idée sans acheter de matériel, consommer des services managés (base, file de messages, IA)
**Définition :** Mise à disposition à la demande de ressources informatiques (calcul, stockage, réseau, services) via un réseau, facturées à l'usage et administrées par le fournisseur.
**Syntaxe :** `aws ec2 run-instances / gcloud compute instances create / az vm create`
**Cas réguliers :**
- `Service public (AWS, Azure, GCP)` — Louer des VMs, du stockage objet ou des bases managées, facturés à l'heure
- `Cloud privé (OpenStack, vSphere)` — Reproduire le modèle cloud dans son propre datacenter, pour la conformité ou le coût
- `Multi-cloud / hybride` — Répartir une charge entre plusieurs fournisseurs ou entre cloud et sur-site pour éviter la dépendance
**Origine :** Terme popularisé en 2006 (Amazon EC2, Google Docs) ; définition de référence : NIST SP 800-145 (2011). Précurseurs : SaaS Salesforce (1999), virtualisation x86 (VMware, 1998).
**Subtilités/confusions :**
- Le cloud ce n'est pas seulement des serveurs ailleurs : ses 5 critères NIST sont le libre-service à la demande, l'accès réseau étendu, la mutualisation, l'élasticité rapide et le service mesuré.
- Les 3 modèles de service : IaaS (machine), PaaS (plateforme d'exécution), SaaS (application prête) — confondre les trois fausse tout devis.
- Le coût réel vient surtout du trafic sortant (egress), du stockage et des ressources oubliées, pas du CPU comme on le croit souvent.
**Urgences/dangers :** ⚠️ Sans budget ni alarme, une fuite de trafic sortant ou des VMs zombies peuvent générer des milliers d'euros en quelques jours.
**Précautions :** Garder des garde-fous dès le premier déploiement : alarme de budget, tags de coût obligatoires, quotas par projet, revue mensuelle des ressources inutilisées.
**Équivalents :** IaaS, PaaS, SaaS (modèles), On-premise (inverse)
**Voir aussi :** IaaS, PaaS, SaaS, Cloud Native, FinOps, Serverless, Datacenter

## `BDD` — Base de Données [Data]
**Catégorie :** Data | **Niveau :** debutant | **Popularité :** 95
**Signification :** Base De Données (Database)
**Contextes :** stocker l'état d'une application, requêter avec SQL, garantir la cohérence des écritures concurrentes, alimenter du reporting
**Définition :** Ensemble organisé de données persistantes, structuré par un schéma et administré par un SGBD qui garantit intégrité, concurrence d'accès et durabilité.
**Syntaxe :** `psql -c 'SELECT * FROM clients' / mysql -e 'SELECT COUNT(*) FROM commandes'`
**Cas réguliers :**
- `BDD relationnelle (PostgreSQL, MySQL, SQL Server)` — Schéma strict, jointures et transactions ACID : le choix par défaut des données métier
- `BDD NoSQL (MongoDB, Redis, Cassandra)` — Documents, clé-valeur ou colonnes larges : souplesse de schéma et montée en charge horizontale
- `BDD analytique (Snowflake, BigQuery)` — Stockage en colonnes et agrégations massives pour la BI, séparée de la base transactionnelle
**Origine :** Modèle relationnel formalisé par Edgar F. Codd (IBM, 1970) ; premier SGBD relationnel commercial : Oracle (1979), après le prototype System R d'IBM (1974).
**Subtilités/confusions :**
- SGBD et base ne sont pas synonymes : PostgreSQL est le logiciel, la base est l'ensemble des données qu'il héberge sur une instance.
- NoSQL ne veut pas dire sans schéma : le schéma existe mais il est implicite et porté par le code applicatif, donc plus fragile.
- Chaque index accélère les lectures mais ralentit les écritures et consomme du disque : indexer tous les champs est une erreur classique.
**Urgences/dangers :** ⚠️ Un DROP ou TRUNCATE lancé sur la mauvaise base (prod au lieu de recette) est irréversible : vérifier l'hôte et le schéma avant d'exécuter.
**Précautions :** Sauvegardes réellement restaurées lors d'un test, compte applicatif à droits minimaux, migrations de schéma versionnées et relues.
**Équivalents :** SGBD (le logiciel qui la gère), Tableur (petit volume), Data Warehouse (analytique)
**Voir aussi :** SGBD, SQL, NoSQL, ACID, CRUD, ORM, DBA, Data Warehouse, PostgreSQL, MySQL, Backup

## `API REST` — Interface HTTP REST [Web/Développement]
**Catégorie :** Web | **Niveau :** intermediaire | **Popularité :** 94
**Signification :** Representational State Transfer (style d'architecture HTTP)
**Contextes :** exposer des données à un front web ou mobile, connecter des services entre eux, publier une API pour des partenaires
**Définition :** Interface HTTP exposant des ressources identifiées par des URL, manipulées par les verbes standards (GET, POST, PUT, PATCH, DELETE) et décrites par des réponses JSON ou XML.
**Syntaxe :** `curl -H 'Accept: application/json' https://api.exemple.fr/v1/users/42`
**Cas réguliers :**
- `GET /v1/users/42` — Lire une ressource : sans effet de bord (idempotent, cachable)
- `POST /v1/users` — Créer une ressource : réponse 201 avec l'en-tête Location
- `PATCH /v1/users/42` — Modifier partiellement : n'envoyer que les champs qui changent
- `DELETE /v1/users/42` — Supprimer la ressource : réponse 204 sans corps
**Origine :** Style architectural décrit par Roy Fielding dans sa thèse (2000), co-auteur du protocole HTTP ; REST désigne des contraintes, pas un format de données.
**Subtilités/confusions :**
- REST n'est pas synonyme de JSON : c'est un ensemble de contraintes (sans état, cachable, interface uniforme) ; une API qui renvoie du JSON peut ne pas être REST.
- Le piège classique : utiliser GET pour une opération qui modifie l'état — un préchargeur de navigateur ou un crawler peut la déclencher.
- Mettre le verbe dans l'URL (/getUser) casse l'idempotence et la mise en cache : préférer /users/42 avec le verbe HTTP.
**Urgences/dangers :** ⚠️ Sans limite de débit ni pagination, une API exposée peut être épuisée en quelques minutes (coût, déni de service) : voir Rate Limiting.
**Précautions :** Versionner l'API (/v1), authentifier (clé, OAuth2), limiter le débit, paginer les listes et publier le contrat (OpenAPI/Swagger).
**Équivalents :** GraphQL, gRPC, SOAP, RPC
**Voir aussi :** REST, API, HTTP, HTTPS, GraphQL, gRPC, SOAP, API Gateway, Webhook, Rate Limiting

## `Ethernet` — Réseau local filaire IEEE 802.3 [Réseau]
**Catégorie :** Réseau | **Niveau :** intermediaire | **Popularité :** 92
**Signification :** Ethernet (IEEE 802.3)
**Contextes :** relier postes, serveurs et équipements en local, câblage cuivre ou fibre, VLAN et agrégation de liens
**Définition :** Famille de standards de réseau local filaire (IEEE 802.3) définissant le câblage, les trames et les débits, de 10 Mb/s aux 400 Gb/s actuels.
**Syntaxe :** `ethtool eth0 / ip -s link show eth0`
**Cas réguliers :**
- `1000BASE-T (1 Gb/s sur RJ45)` — Câble cuivre Cat 5e/6 jusqu'à 100 m : le standard des postes de travail
- `10GBASE-LR (fibre optique)` — Liaison 10 Gb/s entre switches et serveurs, ou sur plusieurs centaines de mètres
- `Agrégation LACP 2 x 1 Gb/s` — Additionner des liens pour la bande passante et la redondance
- `VLAN 802.1Q sur un trunk` — Faire circuler plusieurs réseaux logiques sur un même câble
**Origine :** Conçu par Bob Metcalfe au Xerox PARC (1973), normalisé IEEE 802.3 (1983) ; le nom vient de l'éther, milieu supposé transporter les données.
**Subtilités/confusions :**
- Ethernet définit la couche 2 (trames, adresses MAC), pas l'adressage IP : la confusion avec Internet est fréquente.
- Un câble Cat 5e ne tient pas 10 Gb/s : au-delà de 1 Gb/s, il faut Cat 6a/7 ou de la fibre, et des distances courtes.
- Les trames Ethernet n'ont pas d'acquittement : c'est TCP qui détecte la perte et retransmet.
**Urgences/dangers :** ⚠️ Une boucle de câblage entre deux switches sans Spanning Tree provoque une tempête de broadcast qui sature tout le réseau en quelques secondes.
**Précautions :** Étiqueter les liens, activer Spanning Tree et LACP, documenter les VLAN et surveiller les erreurs CRC via les compteurs d'interface.
**Équivalents :** WiFi (sans fil), Fiber Channel (stockage), Token Ring (obsolète)
**Voir aussi :** LAN, MAC Address, RJ45, MTU, Switch, WiFi, PoE, VLAN, LACP, Spanning Tree

## `Switch` — Commutateur réseau [Réseau]
**Catégorie :** Réseau | **Niveau :** intermediaire | **Popularité :** 90
**Signification :** Network Switch (commutateur)
**Contextes :** interconnecter les postes d'un bâtiment, segmenter en VLAN, agréger des liens serveurs, constituer un cœur de réseau
**Définition :** Équipement de couche 2 qui apprend les adresses MAC connectées à chacun de ses ports et commute chaque trame vers le seul port concerné, contrairement au hub qui répète tout.
**Syntaxe :** `show mac address-table / bridge fdb show`
**Cas réguliers :**
- `Switch d'accès 24 ports` — Brancher les postes d'un étage, un VLAN par service
- `Switch de cœur 10/40 Gb/s` — Relier les switches d'accès et les serveurs, avec redondance
- `Switch empilable (stack)` — Administrer plusieurs châssis comme un seul équipement
- `PoE pour téléphones et bornes WiFi` — Alimenter les équipements en 48 V directement par le câble réseau
**Origine :** Descendant du pont (bridge) Ethernet ; premier switch Ethernet commercial : Kalpana EtherSwitch (1990), avant le rachat de Kalpana par Cisco (1994).
**Subtilités/confusions :**
- Un switch ne filtre pas par IP : il commute sur l'adresse MAC. Pour filtrer par IP ou par port, il faut un routeur, un pare-feu ou des ACL.
- Un switch de niveau 3 route entre VLAN sans remonter vers un routeur externe, mais avec des fonctions de routage plus limitées.
- Un hub répète la trame sur tous les ports (collisions, écoute passive) : ne jamais le confondre avec un switch, même s'il y ressemble physiquement.
**Urgences/dangers :** ⚠️ Débrancher un lien trunk ou d'agrégation en production coupe tout un étage : identifier les ports en amont (LLDP) et annoncer la fenêtre de maintenance.
**Précautions :** Sauvegarder la configuration avant modification, étiqueter les ports, désactiver les ports inutilisés et activer le DHCP snooping.
**Équivalents :** Hub (obsolète), Pont (bridge), Routeur (couche 3), Borne WiFi
**Voir aussi :** Ethernet, LAN, VLAN, VLAN Tagging, LACP, Spanning Tree, MAC Address, PoE, Routeur

## `Routeur` — Router (couche 3) [Réseau]
**Catégorie :** Réseau | **Niveau :** intermediaire | **Popularité :** 89
**Signification :** Router
**Contextes :** relier deux réseaux différents, sortir vers Internet, filtrer et traduire le trafic, gérer le multihoming
**Définition :** Équipement de couche 3 qui choisit le meilleur chemin pour chaque paquet entre réseaux distincts, en s'appuyant sur une table de routage.
**Syntaxe :** `ip route show / show ip route`
**Cas réguliers :**
- `Route par défaut 0.0.0.0/0` — Envoyer vers la passerelle tout ce qui n'est pas dans une route connue
- `Routage statique` — Route écrite à la main pour une destination précise
- `Routage dynamique (OSPF, BGP)` — Échanger automatiquement les routes et réagir aux pannes de lien
- `NAT sortant` — Faire sortir un réseau privé vers Internet derrière une adresse publique
**Origine :** L'ancêtre est l'IMP d'ARPANET (1969), premier nœud de commutation de paquets ; le premier routeur multi-protocoles commercial est le Cisco AGS (1986).
**Subtilités/confusions :**
- Routeur (couche 3, choisit un chemin par adresse IP) et switch (couche 2, commute par adresse MAC) ne font pas le même travail ; les switchs de niveau 3 cumulent les deux.
- L'ordre des routes compte (correspondance de préfixe la plus longue) : deux routes qui se chevauchent donnent un comportement qui semble aléatoire en cas d'erreur.
- Passerelle (gateway) désigne un rôle, souvent tenu par un routeur : la passerelle par défaut d'un poste est simplement l'entrée 0.0.0.0/0 de sa table.
**Urgences/dangers :** ⚠️ Une route par défaut erronée sur un routeur de production dévie tout le trafic (blackhole) et coupe le site : prévoir un accès hors bande pour corriger.
**Précautions :** Documenter les routes statiques, surveiller les sessions de routage dynamique et filtrer les annonces (route filtering, RPKI).
**Équivalents :** Switch de niveau 3, pare-feu, box domestique
**Voir aussi :** Gateway, NAT, OSPF, BGP, AS, CIDR, Subnet, Firewall, Switch

## `NAT` — Network Address Translation [Réseau]
**Catégorie :** Réseau | **Niveau :** intermediaire | **Popularité :** 88
**Signification :** Network Address Translation (traduction d'adresses réseau)
**Contextes :** faire sortir un réseau privé vers Internet, publier un service interne, pallier la pénurie d'adresses IPv4
**Définition :** Traduction des adresses (et généralement des ports) au passage d'un équipement réseau, permettant à de nombreuses machines privées de partager une adresse publique.
**Syntaxe :** `iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`
**Cas réguliers :**
- `NAT sortant (masquerading / NAPT)` — Tout un LAN en 192.168.x sort sous une seule adresse publique
- `Redirection de port (DNAT)` — Joindre un serveur interne depuis Internet via l'IP publique et un port choisi
- `NAT statique 1 pour 1` — Associer durablement une adresse publique à une machine interne
- `Carrier-Grade NAT (FAI)` — Partager une adresse entre plusieurs abonnés, au prix d'un port entrant impossible
**Origine :** Normalisé par la RFC 1631 (1994) face à l'épuisement annoncé des adresses IPv4 ; généralisé par les box ADSL à partir des années 2000.
**Subtilités/confusions :**
- NAT et pare-feu sont deux fonctions distinctes : le NAT réécrit les adresses, il ne filtre rien — les box les cumulent, ce qui entretient la confusion.
- Le NAT casse le modèle de bout en bout : aucune connexion entrante n'est possible sans règle explicite, d'où la complexité de VoIP, P2P et IPsec.
- La traduction porte aussi sur les ports (NAPT/PAT) : ce que l'on appelle NAT en pratique est presque toujours un NAPT.
**Urgences/dangers :** ⚠️ Retirer une redirection de port en production coupe l'accès externe à un service (site, VPN, mail) : sauvegarder la table NAT avant modification.
**Précautions :** Limiter les redirections au strict nécessaire, journaliser chaque changement et privilégier IPv6 quand il est disponible, car il supprime le besoin de NAT.
**Équivalents :** PAT/NAPT (avec ports), proxy applicatif, routage IPv6 (sans NAT)
**Voir aussi :** NAT Gateway, Gateway, Firewall, PAT, CIDR, IP, VPN, Routeur

## `AS` — Autonomous System [Réseau]
**Catégorie :** Réseau | **Niveau :** avance | **Popularité :** 84
**Signification :** Autonomous System (système autonome)
**Contextes :** comprendre le routage entre fournisseurs d'accès, annoncer un bloc d'adresses, gérer le multihoming
**Définition :** Ensemble de réseaux IP administrés par une même organisation, présentés à Internet avec une politique de routage unique et identifiés par un numéro (ASN).
**Syntaxe :** `whois AS15169 / show ip bgp summary`
**Cas réguliers :**
- `AS public (ex. AS15169 = Google)` — Identifier l'organisation responsable d'une plage d'adresses annoncée
- `eBGP` — Échanger les routes entre systèmes autonomes, par exemple entre un client et ses deux FAI
- `iBGP` — Diffuser en interne les routes apprises de l'extérieur
- `AS privé (64512 à 65534)` — Numérotation interne lorsque l'ASN mondial n'est pas nécessaire
**Origine :** Notion héritée d'ARPANET, formalisée avec BGP (1989) ; les numéros d'AS sont attribués par les registres régionaux (RIPE, ARIN, APNIC, LACNIC, AFRINIC).
**Subtilités/confusions :**
- Un AS n'est pas un réseau physique mais un périmètre administratif et politique : une même entreprise peut en exploiter plusieurs.
- Les ASN publics sont attribués par les registres régionaux ; les plages privées 64512-65534 ne circulent jamais sur l'Internet global.
- Une fuite de routes entre AS (BGP hijacking) détourne le trafic sans couper la connectivité : la panne est silencieuse et se voit surtout en latence.
**Urgences/dangers :** ⚠️ Annoncer un préfixe plus spécifique que celui du voisin détourne son trafic (route leak) : filtrer systématiquement les annonces sortantes.
**Précautions :** Filtrer les annonces BGP (prefix-list, RPKI/ROA), surveiller les changements de routes et conserver un plan d'adressage documenté.
**Équivalents :** Domaine de routage, zone administrative
**Voir aussi :** BGP, BGP Hijacking, OSPF, CIDR, IP, Gateway, Routeur, Datacenter

## `Datacenter` — Centre de données [Infrastructure]
**Catégorie :** Infrastructure | **Niveau :** debutant | **Popularité :** 87
**Signification :** Datacenter (centre de données)
**Contextes :** héberger des serveurs en propre ou en colocation, dimensionner énergie et refroidissement, planifier la redondance
**Définition :** Site regroupant serveurs, stockage, réseau et alimentation, conçu pour la disponibilité : climatisation, onduleurs, groupes électrogènes et liens redondants.
**Syntaxe :** `ipmitool chassis status`
**Cas réguliers :**
- `Salle en colocation` — Louer quelques baies chez un opérateur plutôt que construire son bâtiment
- `Baie Rack 19 (42 U)` — Alimentation A/B, brassage réseau et baies optiques documentées
- `Zones de disponibilité` — Répartir les serveurs géographiquement pour survivre à la panne d'un site
- `Certification Tier III / Tier IV` — Niveau de redondance électrique et de maintenance à chaud exigé au contrat
**Origine :** Héritier des salles informatiques des années 1950-1960 (SABRE, 1960) ; le modèle de colocation moderne s'est développé à la fin des années 1990 (Equinix, 1998).
**Subtilités/confusions :**
- La redondance électrique coûte cher : le premier poste budgétaire, devant le refroidissement, mesuré par l'indicateur PUE (énergie totale / énergie des serveurs).
- Une zone de disponibilité n'est pas forcément un bâtiment distinct : c'est une séparation logique d'alimentation et de réseau, parfois dans un même site.
- Le premier risque n'est ni le feu ni le vol mais l'erreur de configuration : c'est ce qui justifie l'automatisation et la revue par les pairs.
**Urgences/dangers :** ⚠️ Couper l'alimentation d'un serveur pour un simple redémarrage peut corrompre des données si le cache d'écriture n'est pas vidé : préférer un arrêt propre.
**Précautions :** Onduleurs testés, groupes électrogènes en essai de charge, plan d'adressage et d'alimentation documenté, accès physiques tracés.
**Équivalents :** Salle serveur, cloud public (alternative), site de secours (PRA)
**Voir aussi :** Rack 19, PDU, UPS, Blade Server, Bare Metal, Cloud, S3, Backup, PRA

## `Cache` — Mémoire cache [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 89
**Signification :** Cache (mémoire temporaire rapide)
**Contextes :** accélérer un processeur ou un disque, réduire la latence d'un site web, éviter de recalculer ou de requêter à chaque appel
**Définition :** Mémoire rapide et de faible capacité intercalée entre un producteur lent et un consommateur rapide, qui conserve les données les plus fréquemment utilisées.
**Syntaxe :** `free -h / iostat -x / varnishstat`
**Cas réguliers :**
- `Cache processeur L1/L2/L3` — De quelques kilo-octets à plusieurs mégaoctets, partagés ou non entre les cœurs
- `Page cache du noyau` — Les blocs lus récemment restent en RAM, d'où une mémoire libre faible sous Linux
- `Cache HTTP / CDN` — Servir les contenus au plus près de l'utilisateur sans repasser par l'origine
- `Cache applicatif (Redis, Memcached)` — Éviter de recalculer une réponse ou d'interroger la base à chaque appel
**Origine :** Le terme est proposé par Maurice Wilkes en 1965 ; les premières implémentations commerciales apparaissent avec l'IBM System/360 Model 85 (1968).
**Subtilités/confusions :**
- Cache et mémoire vive ne sont pas synonymes : le cache est un niveau intermédiaire, la RAM est la mémoire principale de travail.
- Une invalidation ratée affiche des données périmées (cache stale) : c'est la première cause de bug des architectures à cache, avant la question de la taille.
- Le taux de succès (hit ratio) compte plus que la capacité : un cache mal clé ou trop petit peut dégrader les performances au lieu de les améliorer.
**Urgences/dangers :** ⚠️ Vider un cache en production (Redis flushall, purge CDN) renvoie toute la charge sur la base ou l'origine, qui peut tomber immédiatement.
**Précautions :** Définir une politique d'expiration et d'invalidation explicite, prévoir un réchauffement après purge et mesurer le hit ratio en supervision.
**Équivalents :** Tampon (buffer, plutôt en écriture), CDN (cache géographique), index de base (optimisation différente)
**Voir aussi :** L1/L2/L3 Cache, CDN, Redis, Latency, IOPS, Throughput, Scalability, Monitoring

## `Image` — Image de conteneur ou de système [Cloud/DevOps]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 85
**Signification :** Image (conteneur ou système)
**Contextes :** construire et distribuer une application conteneurisée, préinstaller un système, figer un état de machine
**Définition :** Artefact immuable et empilé de couches qui sert de modèle pour démarrer un conteneur (image Docker/OCI) ou une machine (image système).
**Syntaxe :** `docker build -t mon-app:1.0 . / docker image ls`
**Cas réguliers :**
- `docker build -t mon-app:1.0 .` — Construire l'image depuis un Dockerfile, couche par couche
- `docker push registry/mon-app:1.0` — Publier l'image dans un registre pour la déployer ailleurs
- `Image de base alpine ou slim` — Partir d'un système minimal pour réduire taille et surface d'attaque
- `Image système ISO ou qcow2` — Installer ou démarrer une machine virtuelle depuis une image disque
**Origine :** Le modèle d'image par couches vient des systèmes de fichiers union ; Docker l'a popularisé en 2013 et le format a été standardisé par l'Open Container Initiative (OCI, 2017).
**Subtilités/confusions :**
- Une image est en lecture seule : le conteneur ajoute par-dessus une couche d'écriture éphémère qui disparaît à l'arrêt.
- L'étiquette latest n'est pas la plus récente : c'est le tag par défaut, qui peut pointer vers n'importe quelle version — à ne jamais utiliser en production.
- Chaque instruction du Dockerfile crée une couche : regrouper les commandes évite les images obèses et les secrets figés dans l'historique.
**Urgences/dangers :** ⚠️ Un secret (clé, jeton) présent dans une couche reste extractible depuis l'image publiée, même s'il est supprimé du Dockerfile ensuite : il doit être considéré comme compromis.
**Précautions :** Épingler les versions (jamais latest en production), scanner les vulnérabilités, utiliser un registre privé et signer les images.
**Équivalents :** Snapshot de machine virtuelle, archive applicative (jar, war), gabarit système
**Voir aussi :** Registry, Docker, Docker Compose, Kubernetes, SBOM, CVE, Serverless, Artifact

## `Event-Driven` — Architecture événementielle [Architecture]
**Catégorie :** Architecture | **Niveau :** avance | **Popularité :** 86
**Signification :** Event-Driven Architecture (architecture pilotée par les événements)
**Contextes :** découpler des services, réagir à des faits métier en temps réel, absorber des pics de charge, alimenter plusieurs consommateurs
**Définition :** Style d'architecture où les composants communiquent en publiant et consommant des événements (des faits passés) via un bus ou une file, au lieu de s'appeler directement.
**Syntaxe :** `kafka-console-producer.sh --topic commandes < evenement.json`
**Cas réguliers :**
- `Publication / abonnement (pub-sub)` — Un service publie commande.créée, plusieurs consommateurs réagissent indépendamment
- `File de messages (RabbitMQ, SQS)` — Traiter une file de tâches à son rythme, avec reprise sur erreur
- `Journal d'événements (Kafka)` — Conserver un historique ordonné et rejouable des événements
- `Event Sourcing + CQRS` — Reconstruire l'état par rejeu et séparer lectures et écritures
**Origine :** Le concept descend des files de messages d'entreprise (IBM MQ Series, 1993) ; il a été popularisé par les architectures microservices et le Reactive Manifesto (2014).
**Subtilités/confusions :**
- Événement (fait passé, immuable) et commande (intention adressée à un service) ne se traitent pas de la même manière.
- Sans idempotence, un message livré deux fois crée un doublon : la livraison 'au moins une fois' est le mode par défaut des bus.
- L'ordre n'est garanti qu'à l'intérieur d'une partition : deux messages liés publiés dans des partitions différentes peuvent arriver inversés.
**Urgences/dangers :** ⚠️ Un consommateur en panne sur une file sans limite fait gonfler le backlog jusqu'à saturer le disque du broker : surveiller le décalage (lag) en permanence.
**Précautions :** Rendre les traitements idempotents, prévoir une file de rebut (DLQ), surveiller le lag et versionner le schéma des événements.
**Équivalents :** Appels synchrones REST/gRPC (inverse), traitement par lots (batch)
**Voir aussi :** Kafka, RabbitMQ, Webhook, Microservices, Event Sourcing, CQRS, DLQ, Idempotency, Serverless

## `Sécurité` — Cybersécurité [Sécurité]
**Catégorie :** Sécurité | **Niveau :** debutant | **Popularité :** 95
**Signification :** Sécurité de l'information (cybersécurité)
**Contextes :** protéger des données et des systèmes, répondre à une exigence de conformité, construire une défense en profondeur
**Définition :** Ensemble des moyens techniques et organisationnels qui protègent la confidentialité, l'intégrité et la disponibilité des systèmes et des données.
**Syntaxe :** `lynis audit system / auditctl -l`
**Cas réguliers :**
- `Défense en profondeur` — Cumuler pare-feu, authentification, chiffrement, sauvegardes et supervision plutôt qu'une barrière unique
- `Moindre privilège` — N'accorder que le strict nécessaire, à un utilisateur comme à un service
- `Zero Trust et MFA` — Vérifier en continu et ne jamais se fier au seul fait d'être dans le réseau interne
- `Réponse à incident` — Détecter, contenir, éradiquer, restaurer puis analyser (post-mortem) sans chercher un coupable
**Origine :** La triade confidentialité / intégrité / disponibilité est formalisée par les travaux des années 1970 (Saltzer et Schroeder, 1975), puis déclinée en normes (ISO 27001, NIST CSF).
**Subtilités/confusions :**
- Sécurité et conformité ne sont pas synonymes : on peut être conforme (RGPD, PCI-DSS) et rester vulnérable — l'audit vérifie des processus, pas la robustesse réelle.
- Le maillon faible est rarement la cryptographie : c'est le facteur humain (hameçonnage, mot de passe partagé) et les configurations par défaut.
- Une vulnérabilité reste exposée des mois avant correction : la détection et la réaction comptent autant que la prévention.
**Urgences/dangers :** ⚠️ Une clé SSH privée ou un jeton d'API publié sur un dépôt public est exploité automatiquement en quelques minutes par des robots de scan.
**Précautions :** Corriger rapidement, chiffrer les données sensibles au repos et en transit, limiter les accès, sauvegarder hors ligne et tester la restauration.
**Équivalents :** Cybersécurité, sûreté (safety, notion différente), conformité (cadre légal)
**Voir aussi :** Zero Trust, MFA, Firewall, WAF, IAM, RBAC, PKI, SIEM, EDR, DevSecOps, CVE, AES

## `Shell` — Interpréteur de commandes [Système]
**Catégorie :** Système | **Niveau :** debutant | **Popularité :** 96
**Signification :** Shell (interpréteur de commandes)
**Contextes :** dialoguer avec un système sans interface graphique, enchaîner des commandes, écrire des scripts d'automatisation
**Définition :** Programme placé entre l'utilisateur (ou un script) et le noyau : il interprète les commandes, lance les processus et fournit variables, boucles et redirections.
**Syntaxe :** `bash / zsh / powershell.exe / cmd.exe`
**Cas réguliers :**
- `bash et sh` — Shell par défaut de la quasi-totalité des distributions Linux et des conteneurs
- `zsh et fish` — Shells interactifs modernes avec complétion et suggestions avancées
- `PowerShell` — Shell objet de Windows : le pipeline transporte des objets, pas du texte brut
- `cmd.exe` — Shell historique de Windows, limité mais toujours utilisé par les scripts .bat
**Origine :** Le premier shell apparaît dans Unix (Thompson, 1971), remplacé par le Bourne shell (1977), puis bash (1989) ; PowerShell (projet Monad) arrive sur Windows en 2006.
**Subtilités/confusions :**
- Shell de connexion et shell d'automatisation ne se confondent pas : .bashrc s'exécute en interactif, alors qu'un script suit le shebang de sa première ligne.
- PowerShell n'est pas cmd.exe : il manipule des objets .NET avec une syntaxe Verbe-Nom (Get-ChildItem) et non des chaînes de texte.
- Une variable non protégée par des guillemets et contenant un espace casse le découpage des arguments : c'est la première source de scripts fragiles.
**Urgences/dangers :** ⚠️ Un script lancé avec sudo qui utilise une variable vide (rm -rf "$DIR") peut détruire le système : tester avec set -u et un mode simulation.
**Précautions :** Démarrer les scripts par set -euo pipefail, entourer les variables de guillemets, valider les entrées et versionner les scripts avec le projet.
**Équivalents :** Interpréteur de commandes, REPL (interactif), terminal (émulateur), cmd.exe
**Voir aussi :** test, eval, source, export, PATH, alias, Redirection, bash?

## `Réseau` — Réseau informatique [Réseau]
**Catégorie :** Réseau | **Niveau :** debutant | **Popularité :** 93
**Signification :** Réseau (network)
**Contextes :** relier des machines, comprendre les couches, diagnostiquer une panne de connectivité
**Définition :** Ensemble d'équipements et de liaisons permettant à des machines d'échanger des données, organisé en couches : câblage, adressage, transport, application.
**Syntaxe :** `ip addr / ip route / ping -c4 8.8.8.8 / ss -tulpn`
**Cas réguliers :**
- `Réseau local (LAN)` — Un même domaine de diffusion, par exemple 192.168.1.0/24 ou 10.0.0.0/8
- `Réseau étendu (WAN / Internet)` — Interconnexion de sites via un opérateur ou un FAI
- `Réseau virtuel (VLAN, VPC)` — Segmenter logiquement sans modifier le câblage
- `Réseau superposé (VPN, WireGuard)` — Rendre joignables des machines isolées via un tunnel chiffré
**Origine :** ARPANET (1969), puis la bascule générale vers TCP/IP le 1er janvier 1983, constituent la naissance du réseau moderne ; le modèle en couches est normalisé par l'ISO (modèle OSI, 1984).
**Subtilités/confusions :**
- Le modèle OSI à 7 couches est un cadre pédagogique : en pratique, TCP/IP raisonne en 4 couches.
- Une machine joignable par adresse IP mais pas par son nom n'a pas un problème réseau mais un problème DNS.
- Le ping teste ICMP et peut être bloqué par un pare-feu : 'je ne pingue pas' ne signifie pas 'je ne peux pas me connecter'.
**Urgences/dangers :** ⚠️ Modifier l'adressage ou la passerelle d'un serveur distant en SSH coupe la session en cours : préparer un accès console (IPMI/KVM) avant toute modification.
**Précautions :** Documenter le plan d'adressage, réserver les plages, surveiller les équipements et tester régulièrement la connectivité de bout en bout.
**Équivalents :** Internet (réseaux publics), interconnexion de stockage (SAN), bus local (loopback)
**Voir aussi :** LAN, WAN, VLAN, IP, CIDR, DNS, Gateway, Firewall, TCP, UDP, Ethernet

## `Kernel` — Noyau du système d'exploitation [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 90
**Signification :** Kernel (noyau)
**Contextes :** comprendre l'abstraction matérielle, gérer modules et paramètres, diagnostiquer un blocage ou un pilote manquant
**Définition :** Cœur du système d'exploitation : il gère les processus, la mémoire, les systèmes de fichiers, le réseau et les pilotes, et sert d'interface entre les applications et le matériel.
**Syntaxe :** `uname -r / lsmod / sysctl -a`
**Cas réguliers :**
- `Noyau monolithique (Linux)` — Tout le code essentiel dans l'espace noyau, complété par des modules chargeables à chaud
- `Micro-noyau (seL4, QNX)` — Services isolés en espace utilisateur et surface noyau minimale, adapté au temps réel
- `Noyau hybride (Windows NT, XNU)` — Compromis entre performances et isolation
- `Noyau temps réel (PREEMPT_RT, VxWorks)` — Latence maximale bornée pour l'industrie et l'embarqué critique
**Origine :** Le noyau Unix naît avec Unix (Thompson et Ritchie, années 1970) ; MINIX (Tanenbaum, 1987) sert d'enseignement et inspire le noyau Linux de Linus Torvalds (1991).
**Subtilités/confusions :**
- Le noyau n'est pas le système d'exploitation complet : la distribution y ajoute les bibliothèques, les outils et la configuration.
- Un module noyau défaillant fait tomber toute la machine (kernel panic), alors qu'une application qui plante n'entraîne qu'elle-même.
- Mettre à jour le noyau sans reconstruire les pilotes hors arbre (NVIDIA, VirtualBox) peut empêcher le démarrage de l'affichage.
**Urgences/dangers :** ⚠️ Retirer un module utilisé par le stockage ou le réseau (modprobe -r) en production coupe immédiatement l'accès aux données ou à la session.
**Précautions :** Conserver au moins un noyau précédent installé pour pouvoir démarrer en secours, tester les mises à jour hors production et tracer les paramètres sysctl modifiés.
**Équivalents :** Micro-noyau, hyperviseur (virtualisation), firmware (code embarqué dans le matériel)
**Voir aussi :** OS, systemd, lsmod, sysctl, modprobe, initrd, Hypervisor, VM, swap

## `Signal` — Signal Unix [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 86
**Signification :** Signal (interruption logicielle envoyée à un processus)
**Contextes :** arrêter proprement un processus, comprendre un processus qui refuse de mourir, faire réagir un script
**Définition :** Message asynchrone envoyé à un processus par le noyau ou par un autre processus pour lui notifier un événement : arrêt demandé, erreur, réveil.
**Syntaxe :** `kill -SIGTERM 1234 / kill -9 1234 / trap 'rm -f /tmp/verrou' EXIT`
**Cas réguliers :**
- `SIGTERM (15)` — Demande d'arrêt propre : le processus libère ses ressources et ferme ses fichiers
- `SIGKILL (9)` — Arrêt immédiat, non interceptable : dernier recours
- `SIGHUP (1)` — Recharger la configuration d'un démon, héritage du téléphone raccroché
- `SIGINT (2)` — Ctrl+C dans un terminal : interruption interactive
**Origine :** Les signaux font partie d'Unix depuis les années 1970 (Unix V7, 1979) ; leur numérotation et leur sémantique sont aujourd'hui normalisées par POSIX.
**Subtilités/confusions :**
- SIGTERM et SIGKILL ne sont pas équivalents : le premier laisse le processus nettoyer, le second tue sans préavis et peut laisser des verrous ou des fichiers temporaires.
- Un processus peut intercepter un signal (trap) sauf SIGKILL et SIGSTOP : un démon peut donc ignorer SIGTERM et sembler impossible à arrêter.
- La numérotation varie légèrement selon les systèmes : préférer les noms (SIGTERM) aux nombres dans les scripts.
**Urgences/dangers :** ⚠️ Un kill -9 sur une base de données ou un serveur de fichiers empêche l'écriture du cache : corruption possible des données.
**Précautions :** Préférer SIGTERM, laisser un délai puis envoyer SIGKILL si nécessaire, et nettoyer les ressources via trap dans les scripts d'arrêt.
**Équivalents :** Exception (notion différente), événement noyau, communication inter-processus
**Voir aussi :** kill, kill -9, kill -15, killall, pkill, trap, systemd, pgrep

## `systemd` — Gestionnaire de services Linux [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 91
**Signification :** System Daemon (gestionnaire d'init et de services)
**Contextes :** gérer les services au démarrage, exprimer des dépendances entre unités, automatiser des tâches par timer
**Définition :** Gestionnaire d'init et de services de la plupart des distributions Linux : il démarre les unités (services, sockets, timers, montages) en respectant leurs dépendances.
**Syntaxe :** `systemctl status nginx / systemctl enable --now mon.service`
**Cas réguliers :**
- `systemctl enable --now mon.service` — Activer au démarrage et démarrer immédiatement
- `Unité .timer` — Remplacer cron par une unité planifiée, journalisée et interrogeable
- `Dépendances d'unités` — After=, Wants= et Requires= ordonnent et conditionnent le démarrage
- `Ressources par service` — MemoryMax=, CPUQuota= limitent un service via les cgroups
**Origine :** Développé par Lennart Poettering (2010), adopté par Fedora 15 (2011) puis par la majorité des distributions ; il remplace l'init SysV et Upstart.
**Subtilités/confusions :**
- systemd n'est pas seulement l'init : il fournit aussi journald (journaux), logind (sessions), udev (périphériques) et les timers.
- Un service 'actif' n'est pas forcément 'sain' : systemd peut afficher actif si le processus principal vit encore malgré des erreurs applicatives.
- Modifier directement un fichier .service fourni par un paquet casse à la mise à jour : passer par systemctl edit qui crée une surcouche.
**Urgences/dangers :** ⚠️ Arrêter un service critique (sshd, réseau, base de données) coupe l'accès ou la production : vérifier les dépendances avant (systemctl list-dependencies).
**Précautions :** Utiliser systemctl edit pour les surcharges, définir Restart=on-failure, limiter les ressources et diagnostiquer avec journalctl -u <service>.
**Équivalents :** SysV init (obsolète), Upstart (obsolète), OpenRC, launchd (macOS), Planificateur de tâches (Windows)
**Voir aussi :** systemctl, journalctl, systemd-analyze, systemd-run, Cron, cgroups, Kernel, OS, launchctl

## `initrd` — Initial ramdisk [Système]
**Catégorie :** Système | **Niveau :** avance | **Popularité :** 80
**Signification :** initial ramdisk (système de fichiers de démarrage)
**Contextes :** démarrer quand le pilote du disque racine n'est pas dans le noyau, monter une racine chiffrée, démarrer sur le réseau
**Définition :** Petit système de fichiers chargé en mémoire par le chargeur d'amorçage, exécuté avant le montage de la racine pour charger les pilotes et les outils nécessaires au démarrage.
**Syntaxe :** `dracut -f /boot/initramfs-$(uname -r).img $(uname -r) / mkinitcpio -P`
**Cas réguliers :**
- `initramfs généré par dracut` — À regénérer après tout changement de pilote, de carte réseau ou de chiffrement
- `Racine chiffrée LUKS` — L'initramfs demande la phrase secrète avant de monter la racine
- `Démarrage réseau (PXE, iSCSI)` — Le noyau récupère l'initramfs sur le réseau puis monte une racine distante
- `Redémarrage de secours` — Démarrer un noyau précédent avec son propre initramfs en cas de kernel panic
**Origine :** initrd apparaît avec le noyau Linux 2.0 (1996) ; il est progressivement remplacé par initramfs, ensemble d'archives cpio intégrées aux noyaux 2.6 dans les années 2000.
**Subtilités/confusions :**
- initrd (image disque montée) et initramfs (archive cpio extraite en RAM) sont souvent confondus : les distributions modernes utilisent initramfs.
- Un initramfs obsolète après mise à jour du noyau provoque 'Unable to mount root fs' ou un écran noir : sa régénération fait partie de la mise à jour.
- Il contient uniquement ce qui est nécessaire au démarrage : ajouter un module dans l'initramfs ne le rend pas disponible une fois le système démarré.
**Urgences/dangers :** ⚠️ Régénérer l'initramfs d'un serveur distant sans vérifier la présence des modules de stockage et de réseau peut rendre la machine non démarrable à distance.
**Précautions :** Conserver le noyau et l'initramfs précédents, tester un redémarrage avant de quitter un accès local ou une console distante, et journaliser les changements.
**Équivalents :** initramfs (moderne), rootfs (système réel), WinPE (équivalent Windows)
**Voir aussi :** Kernel, dracut, mkinitcpio, pivot_root, kexec, mount, fsck, Bootloader?

## `cgroups` — Control groups [Système]
**Catégorie :** Système | **Niveau :** avance | **Popularité :** 85
**Signification :** Control Groups (groupes de contrôle du noyau Linux)
**Contextes :** limiter la mémoire ou le CPU d'un service, isoler des conteneurs, mesurer la consommation, imposer des quotas
**Définition :** Fonctionnalité du noyau Linux qui organise les processus en groupes hiérarchisés pour limiter, répartir et mesurer leurs ressources (CPU, mémoire, E/S, PIDs).
**Syntaxe :** `cat /sys/fs/cgroup/memory.current / systemd-cgls / systemd-run --scope -p MemoryMax=1G`
**Cas réguliers :**
- `Limiter la mémoire d'un service` — MemoryMax=512M et MemorySwapMax=0 sur une unité systemd
- `Limiter le CPU` — CPUQuota=50% borne un service à la moitié d'un cœur
- `Isoler un conteneur` — Docker, Podman et Kubernetes posent leurs limites via les cgroups
- `Mesurer la consommation` — Lire memory.current et cpu.stat pour un groupe donné
**Origine :** Développé chez Google (Paul Menage, Rohit Seth, 2006-2007) puis intégré au noyau Linux 2.6.24 (2008) ; cgroups v2 unifie la hiérarchie depuis le noyau 4.5 (2016).
**Subtilités/confusions :**
- cgroups et namespaces sont complémentaires mais différents : les cgroups limitent les ressources, les namespaces isolent la visibilité.
- cgroups v1 (une hiérarchie par contrôleur) et v2 (hiérarchie unifiée) coexistent encore : les chemins sous /sys/fs/cgroup diffèrent selon la version.
- Limiter la mémoire sans traiter le swap donne un comportement surprenant : les processus sont tués par l'OOM killer au lieu de paginer.
**Urgences/dangers :** ⚠️ Une limite mémoire trop basse fait tuer le processus par l'OOM killer en pleine production, souvent sans message applicatif : ajuster par paliers et surveiller memory.events.
**Précautions :** Fixer des limites réalistes après mesure, surveiller les événements (oom, throttling) et préférer les directives systemd aux manipulations directes de /sys.
**Équivalents :** Namespaces (isolation), ulimit (par processus), nice/ionice (priorité), quotas disque
**Voir aussi :** systemd, systemd-cgls, systemd-run, cgcreate, cgexec, Docker, Kubernetes, Kernel, VM

## `nginx` — Serveur web et reverse proxy [Web/Infrastructure]
**Catégorie :** Web | **Niveau :** intermediaire | **Popularité :** 92
**Signification :** nginx (engine-x)
**Contextes :** servir un site statique, faire reverse proxy vers une application, terminer TLS, répartir la charge
**Définition :** Serveur web et reverse proxy à architecture événementielle : un seul processus suit des milliers de connexions, d'où une empreinte mémoire très faible.
**Syntaxe :** `nginx -t && systemctl reload nginx`
**Cas réguliers :**
- `Serveur de contenus statiques` — Servir un site HTML/CSS/JS sans processus applicatif
- `Reverse proxy vers une application` — proxy_pass http://127.0.0.1:3000 en transmettant X-Forwarded-For et X-Forwarded-Proto
- `Terminaison TLS` — Gérer les certificats et rediriger HTTP vers HTTPS
- `Répartition de charge` — Bloc upstream avec plusieurs serveurs et vérification de santé
**Origine :** Écrit par Igor Sysoev entre 2002 et 2004 et publié en open source en 2004, pour répondre au problème C10K (10 000 connexions simultanées) chez Rambler.
**Subtilités/confusions :**
- nginx est événementiel (quelques processus pour des milliers de connexions), là où Apache historique démarrait un processus par connexion : la logique de configuration en découle.
- Modifier la configuration ne suffit pas : il faut valider (nginx -t) puis recharger, sinon l'erreur ne se révèle qu'au prochain redémarrage.
- En reverse proxy, l'application ne voit que 127.0.0.1 si les en-têtes X-Forwarded-* ne sont pas transmis : logs et redirections deviennent faux.
**Urgences/dangers :** ⚠️ Recharger une configuration invalide peut empêcher nginx de redémarrer après une mise à jour : toujours exécuter nginx -t avant reload.
**Précautions :** Valider la configuration avant rechargement, fixer des limites (client_max_body_size, timeouts), journaliser et surveiller les codes 5xx.
**Équivalents :** Apache HTTP Server, Caddy, Traefik, IIS, Lighttpd
**Voir aussi :** Reverse Proxy, Load Balancer, HTTPS, TLS, WAF, CDN, Docker, certbot

## `containerd` — Daemon de conteneurs [Cloud/DevOps]
**Catégorie :** Cloud | **Niveau :** avance | **Popularité :** 83
**Signification :** containerd (daemon de gestion de conteneurs)
**Contextes :** comprendre la pile d'exécution des conteneurs, exploiter Kubernetes, déboguer un nœud sans Docker
**Définition :** Daemon qui gère le cycle de vie complet des conteneurs (récupération d'images, création, exécution, suppression) pour Docker, Kubernetes et nerdctl.
**Syntaxe :** `ctr images list / ctr containers list / nerdctl run -it alpine sh`
**Cas réguliers :**
- `Moteur de Docker et de Kubernetes` — Le même daemon exécute les conteneurs des deux outils, via l'interface CRI pour Kubernetes
- `ctr pour le débogage` — Inspecter images et conteneurs directement, sans passer par le démon Docker
- `nerdctl comme alternative à Docker` — Même moteur, interface compatible Docker et prise en charge des fichiers Compose
- `Namespaces Kubernetes (k8s.io)` — Les conteneurs de Kubernetes vivent dans un namespace dédié
**Origine :** Extrait du moteur Docker en 2016 et confié à la CNCF (projet gradué en 2019) ; il s'appuie sur runc, implémentation de référence de la spécification OCI.
**Subtilités/confusions :**
- containerd n'est pas un remplacement complet de Docker : il n'embarque ni la construction d'images ni une interface conviviale.
- Sous Kubernetes, les images sont dans le namespace k8s.io : elles n'apparaissent pas dans docker images, il faut crictl images.
- Le daemon ne gère pas directement les processus : il délègue à un shim runc, ce qui permet de le redémarrer sans tuer les conteneurs en cours.
**Urgences/dangers :** ⚠️ Redémarrer le daemon containerd tue les conteneurs qu'il pilote, y compris ceux de Kubernetes : planifier une interruption de service.
**Précautions :** Superviser le daemon (journalctl -u containerd), séparer les namespaces de travail et privilégier crictl sur les nœuds Kubernetes.
**Équivalents :** Docker Engine (pile complète), CRI-O (moteur Kubernetes alternatif), Podman (sans daemon)
**Voir aussi :** Docker, Kubernetes, crictl, nerdctl, Image, Registry, Serverless

## `Firebase` — Plateforme BaaS de Google [Cloud/Web]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 84
**Signification :** Firebase (Backend-as-a-Service de Google)
**Contextes :** prototyper une application sans écrire de back-end, authentifier des utilisateurs, synchroniser des données hors ligne
**Définition :** Plateforme de services back-end managés : base de données temps réel, authentification, stockage de fichiers, hébergement et notifications, pensés pour des clients mobiles et web.
**Syntaxe :** `firebase deploy / firebase emulators:start / npm i firebase`
**Cas réguliers :**
- `Cloud Firestore` — Base documentaire temps réel avec synchronisation hors ligne et cache local
- `Firebase Authentication` — Connexion e-mail, Google, Apple ou téléphone sans écrire de service d'authentification
- `Cloud Storage` — Stockage de fichiers protégé par des règles déclaratives
- `Hosting et émulateurs` — Déployer une PWA et tester localement la pile complète
**Origine :** Fondé en 2011 par James Tamplin et Andrew Lee sous le nom Envolve, racheté par Google en 2014 ; Firestore succède à la Realtime Database en 2017-2018.
**Subtilités/confusions :**
- Firestore et Realtime Database sont deux produits distincts : Firestore est le successeur, avec des requêtes plus riches et une meilleure montée en charge.
- La facturation des lectures se compte par document lu : une requête mal bornée ou une animation mal cadencée peut faire exploser la facture.
- La sécurité est portée par des règles côté service : un back-end qui les contourne expose toute la base en lecture publique.
**Urgences/dangers :** ⚠️ Une base laissée en mode test (lecture et écriture publiques) expose l'intégralité des données : la verrouiller avant toute mise en production.
**Précautions :** Écrire et tester les règles de sécurité avec l'émulateur, limiter le nombre de lectures par requête, activer les alertes de budget et versionner les règles avec le code.
**Équivalents :** Supabase (PostgreSQL managé), AWS Amplify, Appwrite, back-end maison
**Voir aussi :** Firestore, Supabase, BaaS, Serverless, S3, IAM, PWA

## `Next.js` — Framework React [Web/Développement]
**Catégorie :** Web | **Niveau :** intermediaire | **Popularité :** 88
**Signification :** Next.js (framework React)
**Contextes :** construire un site React rendu côté serveur, soigner le référencement, générer des pages statiques, livrer une application full-stack
**Définition :** Framework bâti sur React qui prend en charge le routage, le rendu (SSR, SSG, ISR), le découpage du code et l'optimisation des images, avec la possibilité d'écrire des routes serveur.
**Syntaxe :** `npx create-next-app@latest / next build && next start`
**Cas réguliers :**
- `SSR (rendu côté serveur)` — La page est générée à chaque requête : nécessaire pour des données personnalisées
- `SSG (génération statique)` — Pages produites au build, idéales pour un blog ou une documentation
- `ISR (régénération incrémentale)` — Pages statiques revalidées périodiquement sans reconstruire tout le site
- `Routes API` — Exposer des points d'entrée HTTP dans le même projet
**Origine :** Créé par Vercel (alors Zeit) en 2016 pour éviter la configuration manuelle de React ; les React Server Components arrivent avec l'App Router (2023).
**Subtilités/confusions :**
- Next.js n'est pas React : c'est un framework construit dessus, qui impose ses conventions de routage, de rendu et de données.
- Choisir le SSR par défaut coûte des ressources serveur : si la page est statique, SSG ou ISR est plus rapide et moins cher.
- Composants serveur et client ne s'exécutent pas au même endroit : un hook d'état dans un composant serveur provoque une erreur au build.
**Urgences/dangers :** ⚠️ Toute variable d'environnement préfixée NEXT_PUBLIC_ est embarquée dans le bundle client : n'y placer aucun secret.
**Précautions :** Séparer explicitement composants serveur et client, éviter les chaînes d'appels de données, surveiller les Core Web Vitals et versionner les variables d'environnement.
**Équivalents :** Nuxt (Vue), Remix, SvelteKit, Angular Universal, Astro
**Voir aussi :** SSR, SSG, ISR, Jamstack, SPA, PWA, SEO, npm

## `Cron` — Démon de planification [Système]
**Catégorie :** Système | **Niveau :** debutant | **Popularité :** 90
**Signification :** cron (démon de planification de tâches)
**Contextes :** exécuter une tâche périodique sur un serveur, planifier une sauvegarde nocturne, lancer un script de maintenance
**Définition :** Démon des systèmes Unix qui exécute des tâches planifiées à des heures ou intervalles définis, sans qu'aucun utilisateur ne soit connecté.
**Syntaxe :** `crontab -e / systemctl status cron / journalctl -u cron`
**Cas réguliers :**
- `crontab système (/etc/cron.d, /etc/cron.daily)` — Planification globale, utilisée par les paquets (logrotate, mises à jour)
- `crontab utilisateur (crontab -e)` — Tâches propres à un compte, exécutées avec ses droits
- `@reboot` — Lancer une commande au démarrage de la machine
- `Timer systemd en remplacement` — Planification journalisée, avec dépendances et rattrapage si la machine était éteinte
**Origine :** Apparu dans Unix V7 (1979, Ken Thompson et Brian Kernighan), d'où les cinq champs minutes, heures, jour, mois et jour de semaine ; l'implémentation Linux de référence est Vixie cron (1987).
**Subtilités/confusions :**
- cron ne dispose pas de l'environnement d'un shell de connexion : PATH et variables diffèrent, d'où des tâches qui fonctionnent à la main mais échouent une fois planifiées.
- Une tâche manquée n'est pas rattrapée si la machine était éteinte, contrairement aux timers systemd configurés en Persistent=true.
- Les crontabs ne sont pas journalisés par défaut : sans redirection de la sortie, erreurs et avertissements disparaissent silencieusement.
**Urgences/dangers :** ⚠️ Une erreur de syntaxe dans un crontab peut faire exécuter une tâche coûteuse en boucle : tester la commande à la main, avec les mêmes droits et le même environnement.
**Précautions :** Utiliser des chemins absolus, rediriger la sortie vers un journal, verrouiller les tâches longues (flock) et préférer un timer systemd quand la traçabilité importe.
**Équivalents :** Timers systemd (moderne), launchd (macOS), Planificateur de tâches (Windows), Airflow (orchestration)
**Voir aussi :** crontab, systemd, at, Airflow, logrotate, Backup, journalctl

## `Linux` — Famille de systèmes d'exploitation libres [Système]
**Catégorie :** Système | **Niveau :** debutant | **Popularité :** 99
**Signification :** Linux (noyau et systèmes d'exploitation associés)
**Contextes :** choisir un système serveur, comprendre les distributions, administrer un parc hétérogène
**Définition :** Famille de systèmes d'exploitation libres bâties sur le noyau Linux (1991), déclinées en distributions qui partagent les outils GNU et les standards POSIX.
**Syntaxe :** `uname -a && cat /etc/os-release`
**Cas réguliers :**
- `Debian / Ubuntu (apt)` — Grande stabilité et dépôts immenses : le choix courant en serveur comme sur le poste
- `RHEL / Rocky / Alma (dnf)` — Support commercial de longue durée, standard du monde de l'entreprise
- `Alpine (apk, musl)` — Distribution minuscule, devenue la base des images de conteneurs légères
- `Arch / Fedora` — Versions récentes et cycle court, appréciées des développeurs
**Origine :** Noyau écrit par Linus Torvalds (annonce du 25 août 1991) et distribué sous GPLv2 ; les premières distributions apparaissent en 1992-1993 (Slackware, Debian, Red Hat).
**Subtilités/confusions :**
- Linux désigne strictement le noyau : la formule GNU/Linux rappelle que les outils utilisateur viennent largement du projet GNU.
- Les distributions ne sont pas interchangeables : gestionnaire de paquets, emplacements de fichiers et versions diffèrent, un script doit souvent être adapté.
- La durée de maintenance dépend de la distribution : une Ubuntu LTS est suivie cinq ans, une version intermédiaire neuf mois seulement.
**Urgences/dangers :** ⚠️ Mélanger les dépôts de plusieurs distributions ou forcer une version de paquet (--force) peut casser irrémédiablement les dépendances du système.
**Précautions :** Installer depuis les dépôts officiels, privilégier les versions LTS en production, épingler les versions critiques et tester les montées de version majeures en recette.
**Équivalents :** macOS (héritage BSD), Windows (noyau NT), BSD (FreeBSD, OpenBSD)
**Voir aussi :** OS, Kernel, apt, dnf, pacman, Docker, systemd, VM

## `Script` — Fichier de commandes automatisées [Système]
**Catégorie :** Système | **Niveau :** debutant | **Popularité :** 85
**Signification :** Script (fichier de commandes exécuté par un interpréteur)
**Contextes :** automatiser une tâche répétitive, enchaîner des commandes avec contrôle d'erreur, outiller un déploiement ou une sauvegarde
**Définition :** Fichier texte de commandes exécuté par un interpréteur (shell, Python, PowerShell) pour automatiser une suite d'actions de façon reproductible.
**Syntaxe :** `./deploy.sh / bash -x deploy.sh (trace d'exécution)`
**Cas réguliers :**
- `Script shell de sauvegarde` — Enchaîner archivage, copie distante et purge en vérifiant chaque code retour
- `Script Python d'administration` — Appeler des API ou traiter des fichiers complexes plus lisiblement qu'en shell
- `Script PowerShell de parc` — Appliquer une configuration à de nombreux postes Windows
- `Script d'amorçage cloud (cloud-init)` — Configurer une machine au premier démarrage : utilisateur, paquets, clés
**Origine :** La notion vient des scripts de commandes Unix (sh, années 1970) ; le terme s'est étendu à tout automate interprété (Perl, Python, PowerShell).
**Subtilités/confusions :**
- Un script shell n'est pas portable tel quel entre bash, dash, zsh et PowerShell : shebang et syntaxe ([[ ]], tableaux) diffèrent.
- Sans gestion d'erreur, un script poursuit après un échec : set -e ou la vérification de $? est indispensable avant toute action destructrice.
- Les scripts lancés par cron ou systemd n'ont pas l'environnement interactif : ce qui fonctionne à la main peut échouer une fois planifié.
**Urgences/dangers :** ⚠️ Un script d'automatisation lancé en production sans journal ni mode simulation propage une erreur à grande échelle en quelques secondes.
**Précautions :** Versionner les scripts avec le projet, journaliser et tracer (set -x en débogage), proposer un mode simulation et gérer explicitement les erreurs.
**Équivalents :** Script shell, playbook Ansible, pipeline CI, Makefile
**Voir aussi :** Shell, exec, source, PATH, alias, Cron, systemd, Docker

## `Redirection` — Flux d'entrée et de sortie [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 88
**Signification :** Redirection (détournement des flux standards du shell)
**Contextes :** écrire un résultat dans un fichier, chaîner des commandes, séparer erreurs et sortie standard
**Définition :** Mécanisme du shell qui détourne les flux standards d'un processus (entrée, sortie, erreurs) vers un fichier, un autre processus ou le terminal.
**Syntaxe :** `commande > sortie.txt 2> erreurs.log ; commande | grep motif`
**Cas réguliers :**
- `> fichier` — Écrire la sortie standard en écrasant le contenu existant du fichier
- `>> fichier` — Ajouter à la fin d'un fichier sans écraser son contenu
- `2> erreurs.log` — Rediriger le flux d'erreurs (descripteur 2) séparément
- `2>&1` — Envoyer les erreurs vers la même destination que la sortie standard
- `commande | autre` — Connecter la sortie d'une commande à l'entrée de la suivante (tube)
**Origine :** Redirections et tubes existent depuis les premiers shells Unix (Thompson, 1971-1973) ; ils reposent sur les descripteurs de fichiers et sur le principe 'tout est fichier'.
**Subtilités/confusions :**
- > écrase sans avertir : confondre > et >> peut effacer un journal ou une configuration en une seule frappe.
- La sortie d'erreurs n'est pas redirigée par > : sans 2> ou 2>&1, les messages d'erreur s'affichent à l'écran ou se perdent.
- Dans un pipeline, c'est le code retour de la dernière commande qui est renvoyé, sauf si pipefail est activé : un échec en amont peut passer inaperçu.
**Urgences/dangers :** ⚠️ Une redirection > sur un fichier de production le vide immédiatement, avant même l'exécution réussie de la commande : vérifier le chemin avant de valider.
**Précautions :** Tester en écrivant vers un fichier temporaire ou via tee, activer set -o pipefail dans les scripts et se méfier des variables non vérifiées dans les chemins.
**Équivalents :** Tube (pipe), tee (double sortie), substitution de processus
**Voir aussi :** Shell, echo, printf, tee, grep, test, PATH

## `PATH` — Variable d'environnement des exécutables [Système]
**Catégorie :** Système | **Niveau :** debutant | **Popularité :** 96
**Signification :** System Executable Search Path
**Contextes :** exécuter une commande sans préciser son chemin absolu, ajouter des outils au terminal, configurer des environnements de développement
**Définition :** Variable d'environnement listant les répertoires séparés par `:` (Unix) ou `;` (Windows) dans lesquels le shell recherche les exécutables à lancer sans leur chemin absolu.
**Syntaxe :** `echo $PATH / export PATH="$HOME/bin:$PATH"`
**Cas réguliers :**
- `export PATH="$HOME/.local/bin:$PATH"` — Ajouter un répertoire personnel en tête du PATH pour donner la priorité aux outils installés localement
- `echo $PATH | tr ':' '\n'` — Lister de façon lisible les dossiers analysés par le shell
- `which commande` — Trouver quel dossier du PATH héberge le binaire exécuté par le shell
**Origine :** Présent depuis les premières versions d'Unix AT&T et formalisé dans la norme POSIX.
**Subtilités/confusions :**
- L'ordre des répertoires dans PATH est crucial : le shell s'arrête au premier exécutable correspondant trouvé.
- Mettre le répertoire courant (`.`) dans le PATH est une faille de sécurité majeure car un exécutable malveillant peut y être inséré.
**Urgences/dangers :** ⚠️ Écraser la variable avec `export PATH="/mon/dossier"` (sans réinclure `$PATH`) rend les commandes de base (`ls`, `cat`, `sudo`) introuvables dans la session.
**Précautions :** Toujours concaténer l'ancien `$PATH` lors de modifications (`export PATH="/nouveau:$PATH"`).
**Équivalents :** %PATH% (Windows CMD), $env:PATH (PowerShell)
**Voir aussi :** export, printenv, Shell, env, which

## `.gitignore` — Fichier d'exclusion Git [Git]
**Catégorie :** Git | **Niveau :** debutant | **Popularité :** 96
**Signification :** Git Ignore File
**Contextes :** ignorer les dépendances installées (node_modules, venv), masquer les fichiers temporaires et compilés, prévenir la fuite de secrets
**Définition :** Fichier de configuration texte situé à la racine ou dans les sous-dossiers d'un dépôt Git, définissant les motifs de fichiers et répertoires que Git ne doit pas suivre.
**Syntaxe :** `cat .gitignore`
**Cas réguliers :**
- `node_modules/` — Ignorer un dossier entier et tous ses fichiers
- `*.log` — Ignorer tous les fichiers ayant l'extension .log
- `.env` — Empêcher la publication de fichiers contenant des clés API et des secrets
**Origine :** Intégré à Git par Linus Torvalds pour faciliter la gestion des artefacts de compilation du noyau Linux.
**Subtilités/confusions :**
- `.gitignore` n'a aucun effet sur les fichiers DÉJÀ suivis (tracked) par Git — il faut utiliser `git rm --cached <file>` pour cesser de suivre un fichier déjà validé.
- Une ligne commençant par `!` annule l'exclusion pour un fichier spécifique.
**Urgences/dangers :** ⚠️ Ne pas inclure `.env` ou `credentials.json` dans `.gitignore` risque de publier des mots de passe en clair sur un dépôt public.
**Précautions :** Utiliser des modèles `.gitignore` éprouvés (ex: de gitignore.io) dès l'initialisation (`git init`) du projet.
**Équivalents :** .dockerignore, .helmignore, .npmignore
**Voir aussi :** git, git status, git rm, Git

## `/etc/shadow` — Fichier des mots de passe chiffrés [Sécurité / Système]
**Catégorie :** Sécurité | **Niveau :** avance | **Popularité :** 92
**Signification :** Shadow Password File
**Contextes :** stockage sécurisé des hachages de mots de passe sous Linux, règles d'expiration de comptes, audit de sécurité
**Définition :** Fichier système protégé (mode 0600, accessible uniquement par root) contenant les empreintes chiffrées (hashes) et les paramètres d'expiration des mots de passe utilisateurs.
**Syntaxe :** `sudo cat /etc/shadow`
**Cas réguliers :**
- `user:$6$hashes...:19500:0:90:7:::` — Ligne shadow montrant le hachage SHA-512 (`$6$`), la date de dernière modification et le délai d'expiration (90 jours)
- `user:!:19500:0:90:7:::` — Le symbole `!` ou `*` indique un compte dont le mot de passe est verrouillé
**Origine :** Développé dans le cadre de la suite shadow-utils sous Linux pour masquer les mots de passe hors de `/etc/passwd` qui est lisible par tous.
**Subtilités/confusions :**
- `/etc/passwd` contient la liste des utilisateurs et leurs shells (lisible par tous) ; `/etc/shadow` stocke les mots de passe chiffrés (lisible par root seul).
- Le hachage commence par un préfixe indiquant l'algorithme : `$1$` (MD5), `$5$` (SHA-256), `$6$` (SHA-512), `$y$` (yescrypt).
**Urgences/dangers :** ⚠️ Si les permissions de `/etc/shadow` sont altérées (ex: lisible par tous), n'importe quel utilisateur local peut extraire les hachages et tenter une attaque par dictionnaire offline (John the Ripper / Hashcat).
**Précautions :** Vérifier régulièrement que `/etc/shadow` a les permissions `0600` (ou `0640` avec le groupe shadow).
**Équivalents :** /etc/gshadow (pour les groupes), SAM (Windows)
**Voir aussi :** pwconv, passwd, hashcat, john, Sécurité

## `/etc/sudoers` — Fichier de configuration des droits sudo [Sécurité / Système]
**Catégorie :** Sécurité | **Niveau :** avance | **Popularité :** 94
**Signification :** Sudoers Configuration File
**Contextes :** accorder des privilèges d'administration ciblés à des utilisateurs ou groupes sans leur donner le mot de passe root
**Définition :** Fichier de configuration définissant les règles d'élévation de privilèges de la commande `sudo`.
**Syntaxe :** `sudo visudo`
**Cas réguliers :**
- `%wheel ALL=(ALL) ALL` — Autorise tous les membres du groupe wheel à exécuter n'importe quelle commande via sudo
- `deploy ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx` — Autorise l'utilisateur deploy à redémarrer nginx sans saisir de mot de passe
**Origine :** Développé avec l'utilitaire `sudo` par Robert Coggeshall et Cliff Spencer en 1980.
**Subtilités/confusions :**
- Ne JAMAIS éditer ce fichier directement avec un éditeur classique comme `nano` ou `vim` : toujours utiliser `visudo` qui vérifie la syntaxe avant d'enregistrer.
- Une erreur de syntaxe dans `/etc/sudoers` bloque immédiatement tous les accès `sudo` du système.
**Urgences/dangers :** ⚠️ Éditer `/etc/sudoers` sans `visudo` peut casser sudo et bloquer toute administration de la machine si le compte root n'est pas directement accessible.
**Précautions :** Déposer de préférence les règles personnalisées dans des fichiers séparés sous `/etc/sudoers.d/` gérés par `visudo -f`.
**Équivalents :** PolicyKit (polkit)
**Voir aussi :** sudo, su, visudo, Sécurité

## `fstab` — Table des systèmes de fichiers [Système]
**Catégorie :** Système | **Niveau :** intermediaire | **Popularité :** 95
**Signification :** File System Table (/etc/fstab)
**Contextes :** monter automatiquement les partitions disques, volumes LVM, échanges swap et partages réseau (NFS/CIFS) au démarrage du système
**Définition :** Fichier de configuration Linux stocké sous `/etc/fstab` qui liste les systèmes de fichiers à monter automatiquement au boot avec leurs options.
**Syntaxe :** `cat /etc/fstab`
**Cas réguliers :**
- `UUID=3a2b... /ext4 defaults 0 2` — Montage d'une partition par son identifiant unique UUID
- `192.168.1.100:/data /mnt/nfs nfs defaults 0 0` — Montage d'un partage réseau NFS distant au démarrage
**Origine :** Présent depuis Unix V7 pour automatiser le montage des disques au boot.
**Subtilités/confusions :**
- Il est fortement recommandé d'utiliser les UUIDs (`UUID=...`) plutôt que les noms de périphériques bruts (`/dev/sda1`) qui peuvent changer au redémarrage.
- L'option `nofail` est cruciale pour les montages réseau (NFS/CIFS) afin d'éviter de bloquer le boot si le serveur distant est hors ligne.
**Urgences/dangers :** ⚠️ Une erreur de syntaxe ou un UUID erroné dans `/etc/fstab` provoque un échec de boot et bascule le système en mode emergency `sulogin`.
**Précautions :** Toujours tester la configuration avec `mount -a` après modification de `/etc/fstab` avant de redémarrer le système.
**Équivalents :** systemd.mount (unités de montage modernes)
**Voir aussi :** mount, umount, blkid, lsblk, sulogin, System

## `.bashrc` — Script d'initialisation du shell Bash [Shell]
**Catégorie :** Shell | **Niveau :** debutant | **Popularité :** 94
**Signification :** Bash Run Control File
**Contextes :** personnaliser l'invite de commande (PS1), définir des alias de commandes, ajouter des variables d'environnement pour les sessions Bash interactives
**Définition :** Script shell exécuté automatiquement à l'ouverture de chaque nouvelle session interactive du shell Bash.
**Syntaxe :** `cat ~/.bashrc && source ~/.bashrc`
**Cas réguliers :**
- `alias ll='ls -la'` — Définir un raccourci de commande personnalisé
- `export PATH="$HOME/bin:$PATH"` — Ajouter un dossier au PATH utilisateur
- `source ~/.bashrc` — Recharger immédiatement les modifications sans fermer le terminal
**Origine :** Développé avec le GNU Bash shell par Brian Fox en 1989.
**Subtilités/confusions :**
- `.bashrc` est exécuté pour les shells interactifs non-login ; `.bash_profile` ou `.profile` est exécuté pour les shells de connexion (login).
- Placer des affichages texte (echo) dans `.bashrc` peut casser les connexions non interactives scp ou rsync.
**Urgences/dangers :** —
**Précautions :** Sauvegarder `.bashrc` avant modification et éviter les boucles infinies de commandes dans le script.
**Équivalents :** .zshrc (Zsh), config.fish (Fish)
**Voir aussi :** alias, export, Shell, PATH, bash

## `.gitattributes` — Attributs des fichiers Git [Git]
**Catégorie :** Git | **Niveau :** avance | **Popularité :** 82
**Signification :** Git Attributes File
**Contextes :** gérer les fins de lignes (LF vs CRLF) entre Windows et Linux, configurer Git LFS pour les fichiers volumineux, personnaliser les diffs
**Définition :** Fichier de configuration permettant d'associer des attributs spécifiques à des motifs de fichiers dans un dépôt Git.
**Syntaxe :** `cat .gitattributes`
**Cas réguliers :**
- `* text=auto eol=lf` — Forcer les fins de ligne en LF Unix pour tous les fichiers texte du dépôt
- `*.psd filter=lfs diff=lfs merge=lfs -text` — Déléguer la gestion des fichiers binaires volumineux à Git LFS
**Origine :** Ajouté au projet Git pour résoudre les problèmes de compatibilité multi-plateformes.
**Subtilités/confusions :**
- Permet d'éviter que les développeurs Windows et Linux ne modifient constamment les fins de lignes de tout le projet à chaque commit.
- Peut également servir à ignorer certains fichiers lors de la génération d'archives (`git archive`).
**Urgences/dangers :** —
**Précautions :** Normaliser `.gitattributes` dès la création du dépôt pour éviter les conflits de fins de ligne massifs.
**Équivalents :** .gitignore (pour l'exclusion)
**Voir aussi :** git, git archive, Git, .gitignore

## `/proc` — Système de fichiers virtuel de processus [Système]
**Catégorie :** Système | **Niveau :** avance | **Popularité :** 93
**Signification :** Process Virtual File System (procfs)
**Contextes :** inspecter l'état du noyau Linux et des processus en temps réel, lire la mémoire et les configurations système
**Définition :** Système de fichiers virtuel (procfs) généré dynamiquement en mémoire par le noyau Linux sous le répertoire `/proc`.
**Syntaxe :** `cat /proc/cpuinfo / cat /proc/meminfo / cat /proc/sys/vm/swappiness`
**Cas réguliers :**
- `cat /proc/cpuinfo` — Lire les informations matérielles détaillées des cœurs du processeur
- `cat /proc/sys/net/ipv4/ip_forward` — Vérifier si le routage IP est activé dans le noyau
- `ls -l /proc/<PID>/fd` — Examiner tous les descripteurs de fichiers ouverts par un processus
**Origine :** Conçu à l'origine sous Bell Labs Unix par Tom Killian pour l'inspection des processus, étendu par Linux pour les métriques noyau.
**Subtilités/confusions :**
- Les fichiers dans `/proc` ont une taille apparente de 0 octet sur disque car ils n'existent qu'en RAM générés à la volée par le noyau.
- La modification de certains fichiers sous `/proc/sys/` altère instantanément la configuration du noyau en cours d'exécution.
**Urgences/dangers :** —
**Précautions :** Préférer l'utilisation de `sysctl` pour modifier de manière permanente les paramètres du noyau plutôt que l'écriture directe dans `/proc/sys/`.
**Équivalents :** /sys (sysfs), sysctl
**Voir aussi :** sysctl, ps, lsof, top, CPU, RAM

## `Protobuf` — Protocol Buffers [Data / Développement]
**Catégorie :** Data | **Niveau :** avance | **Popularité :** 88
**Signification :** Protocol Buffers (Google Serialisation)
**Contextes :** communication inter-microservices ultra-rapide avec gRPC, sérialisation binaire compacte, API internes
**Définition :** Mécanisme neutre vis-à-vis des langages et des plateformes conçu par Google pour sérialiser des données structurées de manière binaire et compacte.
**Syntaxe :** `protoc --go_out=. service.proto`
**Cas réguliers :**
- `message User { string name = 1; int32 id = 2; }` — Définition de la structure de données dans un fichier `.proto`
- `Compilation avec protoc` — Génération automatique des classes de données typées en Go, Java, Python ou C++
**Origine :** Développé en interne chez Google au début des années 2000, publié en open-source en 2008.
**Subtilités/confusions :**
- Protobuf est un format binaire non lisible à l'œil nu (contrairement à JSON ou XML), ce qui le rend beaucoup plus compact et rapide à parser.
- Les numéros de champs (`= 1`, `= 2`) identifient les données dans le binaire : ne jamais modifier les numéros de champs existants pour conserver la compatibilité ascendante.
**Urgences/dangers :** —
**Précautions :** Utiliser le compilateur officiel `protoc` et maintenir des fichiers `.proto` versionnés pour la compatibilité de vos APIs.
**Équivalents :** JSON (lisible), MessagePack, Avro, CBOR
**Voir aussi :** gRPC, JSON, API, Microservices

## `Entra ID` — Microsoft Entra ID [Sécurité / Cloud]
**Catégorie :** Sécurité | **Niveau :** intermediaire | **Popularité :** 90
**Signification :** Microsoft Entra ID (anciennement Azure Active Directory)
**Contextes :** gestion des identités cloud, Single Sign-On (SSO), contrôle d'accès conditionnel, sécurité entreprise Microsoft 365
**Rôle :** Service de gestion des identités et des accès basé sur le cloud de Microsoft assurant le SSO, l'authentification MFA et la gestion des comptes d'entreprise.
**Syntaxe :** (Console Azure / PowerShell `Connect-MgGraph`)
**Cas réguliers :**
- `Authentification SSO Microsoft 365` — Connexion unifiée à toutes les applications SaaS via SAML/OIDC
- `Accès Conditionnel` — Restriction de connexion basée sur l'état de l'appareil et la géolocalisation
**Origine :** Lancé par Microsoft sous le nom d'Azure Active Directory en 2010, renommé Microsoft Entra ID en 2023.
**Subtilités/confusions :**
- Ne repose pas sur les mêmes protocoles que l'Active Directory traditionnel sur site (pas de Kerberos/LDAP direct, mais OAuth2/OIDC/SAML).
- Entra ID Connect permet de synchroniser les comptes de l'AD local vers Entra ID Cloud.
**Urgences/dangers :** —
**Précautions :** Exiger le MFA pour tous les comptes utilisateurs et administrateurs d'un tenant Entra ID.
**Équivalents :** Okta, Ping Identity, Keycloak
**Voir aussi :** SSO, SAML, OAuth2, MFA, Cloud
