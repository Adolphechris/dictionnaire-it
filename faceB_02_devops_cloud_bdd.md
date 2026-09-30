# Face B — DEVOPS, CLOUD, BASES DE DONNÉES (fiches riches v3 — 90 visées, lot 1 : 8)

## `CI` — Continuous Integration [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 88
**Signification :** Continuous Integration (Intégration Continue)
**Définition :** Pratique qui fusionne et teste automatiquement le code à chaque commit pour détecter les bugs tôt.
**Contextes :** équipe de développement, pipeline GitHub Actions ou GitLab CI, qualité logicielle, revue de code
**Cas réguliers :**
- `Pipeline CI : lint + tests à chaque push` — Bloquer la fusion si les tests échouent (le plus courant)
- `Badge CI vert sur README` — Preuve visible que la branche principale est saine
- `CI qui publie un rapport de couverture` — Suivre que 80% du code est testé
**Origine :** Grady Booch (1991), popularisée par Extreme Programming de Kent Beck (1999), explosée avec Jenkins (2011) puis GitHub Actions (2019).
**Subtilités/confusions :**
- CI vs CD : CI = tester et intégrer, CD = livrer et déployer. Faire de la CI sans CD = tests sans mise en prod automatique.
- Committer souvent sans pipeline n'est PAS de la CI, c'est juste du versionnement.
- Faux vert : une pipeline qui ne teste rien donne une fausse confiance pire que pas de CI.
**Exemple :** `.github/workflows/ci.yml qui lance pytest à chaque pull request`
**Voir aussi :** CD, DevOps, TDD, Jenkins

## `SaaS` — Software as a Service [Cloud]
**Catégorie :** Cloud | **Niveau :** debutant | **Popularité :** 90
**Signification :** Software as a Service (Logiciel en tant que Service)
**Définition :** Logiciel utilisé via le navigateur sans installation, facturé par abonnement et hébergé par l'éditeur.
**Contextes :** bureautique d'entreprise, CRM, paie, choix d'outil sans serveur à gérer
**Cas réguliers :**
- `Gmail ou Microsoft 365` — Messagerie et bureautique sans serveur mail à administrer (le plus courant)
- `Salesforce pour le commercial` — CRM accessible partout sans installation
- `Notion pour la documentation d'équipe` — Collaboration temps réel facturée par utilisateur
**Origine :** Années 2000 (Salesforce 1999 pionnier) ; démocratisé par le cloud AWS (2006) et le haut débit.
**Subtilités/confusions :**
- SaaS vs PaaS vs IaaS : SaaS = logiciel clé en main, PaaS = plateforme pour coder, IaaS = serveurs nus à gérer.
- SaaS = dépendance : sans internet ou si l'éditeur augmente ses prix, pas d'alternative locale.
- Données chez l'éditeur : vérifier RGPD et lieu d'hébergement avant de mettre des données sensibles.
**Exemple :** `Abonnement 12€/utilisateur/mois à un CRM en ligne`
**Voir aussi :** PaaS, IaaS, Cloud, CRM

## `NoSQL` — Bases de données non relationnelles [Bases de données]
**Catégorie :** Bases de données | **Niveau :** intermediaire | **Popularité :** 75
**Signification :** Not Only SQL (Pas Seulement SQL)
**Définition :** Famille de bases sans schéma SQL rigide : documents, clé-valeur, colonnes ou graphes, pensées pour le scale horizontal.
**Contextes :** application web à fort trafic, données semi-structurées, prototypage rapide, temps réel
**Cas réguliers :**
- `MongoDB pour un catalogue produit` — Chaque produit a des champs différents sans migration de schéma (le plus courant)
- `Redis pour le cache de session` — Clé-valeur ultra-rapide en mémoire
- `Elasticsearch pour la recherche plein texte` — Moteur de recherche du dictionnaire IT lui-même
**Origine :** Terme de Carlo Strozzi (1998), renaissance 2009 (Big Data, web 2.0) : MongoDB, Cassandra, Redis contre la rigidité du relationnel.
**Subtilités/confusions :**
- NoSQL = Not Only SQL, pas No SQL : beaucoup supportent un langage proche de SQL.
- NoSQL vs SQL : NoSQL = flexibilité et scale, SQL = cohérence et jointures. Choisir selon le besoin, beaucoup de projets mixent les deux.
- Sans schéma ne veut pas dire sans structure : valider les données côté application sinon c'est le chaos.
**Exemple :** `db.users.insertOne({nom: "Ada", tags: ["dev", "linux"]})`
**Voir aussi :** SQL, SGBD, MongoDB, Redis

## `CD` — Continuous Delivery / Deployment [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 85
**Signification :** Continuous Delivery / Continuous Deployment (Livraison / Déploiement Continus)
**Définition :** Delivery : le code prêt à partir en prod à tout moment avec validation humaine. Deployment : la prod se fait SANS validation humaine, automatiquement.
**Contextes :** mises à jour fréquentes, équipe produit agile, sortie de version quotidienne
**Cas réguliers :**
- `Merge sur main → déploiement auto en staging` — Teste à chaque fusion (delivery, le plus courant)
- `Tag v1.4 → release GitHub → prod auto` — Deployment sans clic humain
- `Rollback en 1 clic sur une version stable` — Sécurité quand tout part tout seul
**Origine :** Livraison continue popularisée par Jez Humble et David Farley (2010, "Continuous Delivery"), prolongement logique de la CI.
**Subtilités/confusions :**
- Delivery vs Deployment : Delivery = TOUT EST PRÊT (validation humaine ok), Deployment = DÉPLOYÉ AUTO (aucune).
- CD ≠ CI : la CI teste, la CD livre ; un projet CI sans CD s'arrête aux tests.
- Deployment automatique sans tests solides = débâcle ; la CI est un prérequis, pas une option.
**Exemple :** `Git push → tests → staging auto → prod après approbation Slack`
**Voir aussi :** CI, DevOps, GitOps

## `DevOps` — Culture développement + exploitation [DevOps]
**Catégorie :** DevOps | **Niveau :** debutant | **Popularité :** 88
**Signification :** Development + Operations (Développement et Exploitation)
**Définition :** Culture et pratiques qui réunissent dev et sysadmin autour d'outils communs pour livrer plus vite sans casser la prod.
**Contextes :** pipelines, infra as code, astreintes, équipes produit autonomes
**Cas réguliers :**
- `Dev enregistre l'infra dans du code (Terraform)` — Reproduire un environnement en 10 min (le plus courant)
- `Astreinte partagée dev/prod` — Ceux qui écrivent le code en assument l'exploitation
- `Monitoring commun (Grafana)` — Dev voit ce que voit l'ops en production
**Origine :** Terme forgé par Patrick Debois et Andrew Shafer au DevOpsDays d'Anvers (2009), inspiré par "The Agile Administrator" (2008).
**Subtilités/confusions :**
- DevOps ≠ un outil (Jenkins/Docker ne font pas DevOps) — c'est une CULTURE d'équipe.
- DevOps vs SRE : SRE est une façon précise (Google) de faire du DevOps avec objectifs chiffrés de fiabilité.
- "On a mis Docker donc on est DevOps" : outillage sans collaboration = DevOps de façade.
**Exemple :** `Équipe de 6 : chacun code, teste, déploie et monitor`
**Voir aussi :** CI, CD, SRE, IaC, Agile

## `IaaS` — Infrastructure as a Service [Cloud]
**Catégorie :** Cloud | **Niveau :** debutant | **Popularité :** 80
**Signification :** Infrastructure as a Service (Infrastructure en tant que Service)
**Définition :** Louer des serveurs, réseaux et stockage virtualisés à la demande, on gère le dessus (OS, apps), le fournisseur le dessous.
**Contextes :** migration serveur vers le cloud, environnements de test éphémères, besoin de scale rapide
**Cas réguliers :**
- `Lancer un VM Debian sur Scaleway/AWS` — Serveur prêt en 2 min (le plus courant)
- `Serveur de test qui vit 3 heures` — Payer à l'usage réel sans investissement
- `Scale auto de 2 à 10 VMs à Black Friday` — Suivre la charge sans acheter du fer
**Origine :** Modèle popularisé par Amazon EC2 (2006), formalisé par NIST (2011) avec PaaS et SaaS comme couches.
**Subtilités/confusions :**
- IaaS vs PaaS vs SaaS : IaaS = serveur nu (tu gères l'OS), PaaS = plateforme (tu gères le code), SaaS = logiciel fini.
- "Cloud" ≠ IaaS : un SaaS comme Gmail est cloud mais PAS de l'IaaS.
- Coût à l'usage : une VM oubliée allumée 24/7 coûte plus cher qu'un serveur physique à l'ancienne — surveiller les coûts (FinOps).
**Exemple :** `aws ec2 run-instances --image-id ami-0abc --instance-type t3.micro`
**Voir aussi :** SaaS, PaaS, Cloud, VM

## `PaaS` — Platform as a Service [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 75
**Signification :** Platform as a Service (Plateforme en tant que Service)
**Définition :** Une plateforme hébergée où on dépose son code sans gérer ni serveurs ni système : runtime, base, déploiement inclus.
**Contextes :** startups sans ops, apps web rapidement déployées, serverless
**Cas réguliers :**
- `Déployer une API sur Heroku/Render` — Git push et l'app est en ligne (le plus courant)
- `Base managée : Cloud SQL, Supabase` — SGBD sans patchs ni sauvegardes à gérer
- `Fonction serverless sur Cloud Functions` — Du code qui tourne sans serveur visible
**Origine :** Concept formalisé par NIST (2011) après l'explosion d'Heroku (2007) et Google App Engine (2008).
**Subtilités/confusions :**
- PaaS vs IaaS : sur PaaS tu ne choisis même pas l'OS — plus simple mais moins de contrôle.
- PaaS vs SaaS : PaaS sert à CONSTRUIRE un logiciel, SaaS à l'UTILISER.
- Vendor lock-in fort : partir d'Heroku vers autre chose = réécrire la config de déploiement.
**Exemple :** `git push heroku main` qui build et déploie automatiquement
**Voir aussi :** IaaS, SaaS, Serverless, Cloud

## `SQL` — Structured Query Language [Bases de données]
**Catégorie :** Bases de données | **Niveau :** intermediaire | **Popularité :** 92
**Signification :** Structured Query Language (Langage de Requête Structuré)
**Définition :** Langage standard pour interroger, modifier et gérer les bases de données relationnelles.
**Contextes :** applications web, reporting, data analysis, back-office, dictionnaire IT
**Cas réguliers :**
- `SELECT nom FROM users WHERE actif = 1` — Lire des données filtrées (le plus courant de loin)
- `INSERT INTO logs(message) VALUES ('erreur 500')` — Enregistrer un événement
- `UPDATE users SET ville='Paris' WHERE id=42` — Corriger une donnée
- `JOIN users ON orders.user_id = users.id` — Croiser deux tables (le vrai pouvoir du relationnel)
**Origine :** Recherche IBM System R (1974, Chamberlin & Boyce), standardisé SQL-86 après commercialisation d'Oracle (1979) ; le "relationnel" vient d'Edgar Codd (1970).
**Subtilités/confusions :**
- SQL ≠ MySQL : SQL = langage, MySQL = logiciel (SGBD) qui l'implémente.
- SELECT * en prod = lent et fragile — lister explicitement les colonnes.
- Injection SQL : concaténer l'entrée utilisateur dans la requête permet de tout voler — utiliser des requêtes préparées.
**Exemple :** `SELECT o.id, u.nom FROM orders o JOIN users u ON u.id = o.user_id WHERE o.total > 100`
**Voir aussi :** SGBD, NoSQL, ORM, MySQL

## `AWS` — Amazon Web Services [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 90
**Signification :** Amazon Web Services
**Définition :** Suite cloud n°1 mondiale d'Amazon : compute (EC2), stockage (S3), bases (RDS), serverless (Lambda)...
**Contextes :** startups scale-ups, sites à fort trafic, data engineering, migration d'infra
**Cas réguliers :**
- `Déployer un site sur S3 + CloudFront` — Site statique rapide et pas cher (le plus courant)
- `EC2 pour un serveur d'application` — Machine virtuelle classique à l'usage
- `Lambda pour des fonctions sans serveur` — Code déclenché par événement, facturé à l'exécution
- `S3 pour les backups` — Stockage objet quasi inépuisable et peu onéreux
**Origine :** Amazon, 2006 (S3 puis EC2) — pionnier du cloud moderne, né de l'excédent d'infrastructure de la boutique en ligne.
**Subtilités/confusions :**
- Facturation à l'usage : un bucket S3 ouvert publiquement ou une VM oubliée = facture qui explose — activer les alertes de coût.
- AWS ≠ "le cloud" : Azure (Microsoft) et GCP (Google) sont les concurrents directs.
- Region ≠ AZ : une région (Paris) contient plusieurs zones de disponibilité — pour la haute dispo, répartir sur 2+ AZ.
**Exemple :** `aws s3 sync ./site s3://mon-site --delete`
**Voir aussi :** Azure, GCP, SaaS, IaaS

## `Kubernetes` — Orchestration de conteneurs [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 85
**Signification :** Kubernetes (Gouverneur en grec), abrégé K8s (K + 8 lettres + s)
**Définition :** Système open source qui déploie, monte en charge et maintient des conteneurs Docker en production.
**Contextes :** microservices, multi-conteneurs, haute disponibilité, équipe plateforme
**Cas réguliers :**
- `kubectl apply -f app.yaml` — Déployer/déployer une mise à jour de l'app (le plus courant)
- `kubectl get pods` — Voir l'état des conteneurs
- `kubectl logs -f pod-xyz` — Suivre les logs d'un conteneur
- `kubectl scale deployment web --replicas=4` — Passer de 2 à 4 instances (scale auto avec HPA)
**Origine :** Né chez Google (2014) de leurs 15 ans d'expérience avec Borg, confié à la CNCF ; standard de facto du cloud depuis 2016.
**Subtilités/confusions :**
- Docker vs Kubernetes : Docker CRÉE les conteneurs, K8s les ORCHESTRE (déploie, redémarre, scale).
- K8s en interne (on-prem) = lourd à opérer (certains, réseau, stockage) — souvent préférer un managé (EKS, GKE).
- Ne pas confondre `kubectl apply` (déclaratif, idempotent) et `kubectl run` (impératif, pour tests).
**Exemple :** `kubectl get all -n production`
**Voir aussi :** Docker, DevOps, CI, Docker Compose

## `IaC` — Infrastructure as Code [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 75
**Signification :** Infrastructure as Code (Infrastructure en tant que Code)
**Définition :** Décrire les serveurs, réseaux et bases dans des fichiers texte versionnés, pour les recréer à l'identique à volonté.
**Contextes :** environnements reproductibles, multi-cloud, reprise après sinistre, revue de code sur l'infra
**Cas réguliers :**
- `terraform apply` — Créer l'infra décrite dans main.tf (le plus courant)
- `Stack CloudFormation déployé via CI` — Reproduire dev/prod à l'identique
- `Changement d'infra en pull request` — Revue par les pairs avant application
**Origine :** Concept formalisé par la communauté DevOps vers 2011-2013, incarné par Terraform (HashiCorp, 2014) et CloudFormation (AWS, 2011).
**Subtilités/confusions :**
- IaC vs script Bash : un script IMPÉRATIF (fait), l'IaC est DÉCLARATIF (état voulu) → idempotent.
- IaC ≠ configuration managée : Ansible gère l'état des machines, Terraform crée les machines elles-mêmes (chevauchement réel mais rôles distincts).
- État partagé : Terraform stocke un state (souvent distant) — le perdre = ne plus savoir ce qui tourne.
**Exemple :** `terraform plan` pour voir le diff avant `terraform apply`
**Voir aussi :** DevOps, Terraform, Ansible, GitOps

## `Serverless` — Exécution sans serveur géré [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 78
**Signification :** Serverless (sans serveur — mais il y en a un, c'est le cloud provider qui le gère)
**Définition :** Déployer du code en fonctions déclenchées par des événements : le fournisseur alloue les ressources à la demande, facture à l'exécution.
**Contextes :** APIs légères, traitements d'images/files, backends de sites statiques, coûts à l'usage
**Cas réguliers :**
- `Lambda déclenché par upload S3` — Traitement automatique d'un fichier déposé (le plus courant)
- `API Gateway → fonction → réponse HTTP` — API sans serveur à surveiller
- `Cron toutes les heures → fonction` — Tâches périodiques sans machine dédiée
**Origine :** AWS Lambda (2014) — popularisé par des startups voulant ZeroDevOps ; le terme est antérieur (Backends 2006).
**Subtilités/confusions :**
- Serverless ≠ sans machine : un serveur tourne chez le fournisseur, tu ne le gères juste pas.
- Cold start : première exécution = quelques centimètres de latence — à prévoir pour l'API temps réel.
- Facturation par exécution : une boucle infinie ou un trigger en boucle = facture qui grimpe vite.
**Exemple :** `aws lambda invoke --function-name resize out.json`
**Voir aussi :** PaaS, AWS, Lambda, Cloud

## `VM` — Machine Virtuelle [Virtualisation]
**Catégorie :** Virtualisation | **Niveau :** debutant | **Popularité :** 82
**Signification :** Virtual Machine (Machine Virtuelle)
**Définition :** Ordinateur logique complet (OS + applications) émulé sur un hyperviseur partageant le matériel physique.
**Contextes :** hébergement serveurs, tests multi-OS, isolation d'environnements, legacy
**Cas réguliers :**
- `VM VirtualBox avec Ubuntu pour tester` — Tester une distro sans toucher au poste (le plus courant)
- `VM sur VMware ESXi en datacenter` — Découper un serveur physique en 10 serveurs logiques
- `VM Windows dans un Mac` — Utiliser un logiciel Windows-only
**Origine :** IBM CP-40 (1967), théorisée par Gerald Popek ; VMware (1998) démocratise le x86, KVM (2007) l'intègre au noyau Linux.
**Subtilités/confusions :**
- VM vs conteneur : VM = OS complet isolé (lourd, minutes), conteneur = processus partageant le noyau (léger, secondes).
- Hyperviseur type 1 (ESXi, bare metal) vs type 2 (VirtualBox, sur un OS) : le 1 est proche du matériel, plus performant.
- Snapshot ≠ backup : un snapshot fige l'état mais vit sur le même stockage — crash du disque = tout perdu.
**Exemple :** `qemu-system-x86_64 -m 2048 -cdro ubuntu.iso`
**Voir aussi :** Docker, IaaS, hyperviseur, cloud

## `S3` — Stockage objet cloud [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 80
**Signification :** Simple Storage Service (Service de stockage simple)
**Définition :** Service de stockage objet d'AWS : fichiers ("objets") dans des buckets accessibles par HTTP, à l'échelle quasi illimitée.
**Contextes :** backups, images médias, sites statiques, data lake, artefacts de build
**Cas réguliers :**
- `aws s3 cp rapport.pdf s3://mon-bucket/` — Uploader un fichier (le plus courant)
- `aws s3 sync ./dist s3://site-web` — Déployer un site statique complet
- `Bucket en privé + politique d'accès` — Règle de sécurité n°1 (les scandales de buckets ouverts)
**Origine :** Amazon, 4 mars 2006 — premier service AWS public (avant EC2), qui a lancé l'ère du cloud moderne.
**Subtilités/confusions :**
- S3 ≠ EBS : S3 = objet (HTTP, non montable), EBS = disque dur virtuel (montable, pour VM).
- "Rendre un bucket public" est la faute de sécurité cloud la plus médiatisée (voir les fuites de données).
- Versioning activé = protection contre suppressions accidentelles (sinon pas de corbeille sur S3).
**Exemple :** `aws s3 presign s3://mon-bucket/facture.pdf --expires-in 3600`
**Voir aussi :** AWS, CDN, cloud, backup

## `IAM` — Gestion des identités et accès [Sécurité/Cloud]
**Catégorie :** Cloud | **Niveau :** avance | **Popularité :** 75
**Signification :** Identity and Access Management (Gestion des identités et des accès)
**Définition :** Système qui décide QUI a le droit de faire QUOI : comptes, rôles, politiques de permissions.
**Contextes :** cloud multi-projets, rotation des accès, conformité, principe du moindre privilège
**Cas réguliers :**
- `Policy JSON : Allow s3:GetObject sur mon-bucket` — Donner un accès précis (le plus courant)
- `Rôle assumé par un service (EC2 → S3)` — Pas de clé statique pour les machines
- `Accès revu trimestriellement` — Audit des utilisateurs internes
**Origine :** Concept issu de la gestion des droits d'accès (années 1970 DAC/MAC), incarné par AWS IAM (2011), Okta, Keycloak ; aujourd'hui standard Zero Trust.
**Subtilités/confusions :**
- Permission ≠ authentification : IAM = droits (après la connexion), AuthN (login) = identité (qui tu es).
- Moindre privilège : donner UNIQUEMENT l'accès nécessaire — "FullAccess" pour tout = faille garantie.
- Clés d'accès longue durée = risque n°1 volées en public (GitHub) → raccourcir, faire tourner les clés, utiliser des rôles.
**Exemple :** `aws iam list-users --query "Users[*].UserName"`
**Voir aussi :** sécurité, Zero Trust, OAuth, cloud

## `ORM` — Couche objet-relationnelle [Bases de données]
**Catégorie :** Bases de données | **Niveau :** intermediaire | **Popularité :** 70
**Signification :** Object-Relational Mapping (Mapping Objet-Relationnel)
**Définition :** Traduire automatiquement entre le code applicatif (objets) et les tables SQL — requêtes écrites en langage de prog, exécutées en SQL.
**Contextes :** backends web, frameworks (Django, Rails, TypeORM), productivité d'équipe
**Cas réguliers :**
- `User.objects.filter(actif=True)` — SELECT en Python au lieu de SQL brut (le plus courant)
- `user.save()` — INSERT/UPDATE automatique selon la présence de l'id
- `Migration générée depuis le modèle` — Évolution du schéma versionnée
**Origine :** Hibernate (Java, 2001) a démocratisé le pattern ; les ORM sont nés du "impedance mismatch" (1990s) entre objets et relations.
**Subtilités/confusions :**
- ORM ≠ magie : les requêtes complexes deviennent lentes (N+1) — il faut parfois SQL brut.
- ORM vs query builder : l'ORM mappe des objets, le builder (Knex, Doctrine Query Builder) construit du SQL manuellement.
- Les migrations générées peuvent être détruites sur dev (rollback) — jamais en prod.
**Exemple :** `SELECT u.nom, COUNT(o.id) FROM users u JOIN orders o ... -- équivalent du ORM`
**Voir aussi :** SQL, SGBD, API REST, NoSQL

## `CDN` — Réseau de diffusion de contenu [Réseau/Web]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 72
**Signification :** Content Delivery Network (Réseau de Diffusion de Contenu)
**Définition :** Réserve de serveurs répartis dans le monde qui servent les fichiers statiques depuis le point le plus proche de l'utilisateur.
**Contextes :** sites à trafic mondial, images/vidéos, cache de fichiers statiques, réduction de latence
**Cas réguliers :**
- `CloudFront devant un site S3` — Le plus courant : site statique rapide partout
- `Cache-Control: max-age=86400` — Dire au CDN de garder le fichier 24h
- `Invalider le cache après un déploiement` — Sinon les utilisateurs voient l'ancienne version
**Origine :** Akamai (1998, né d'une recherche MIT sur le congestement Internet) ; Cloudflare et CloudFront ont démocratisé l'usage.
**Subtilités/confusions :**
- CDN ≠ hébergeur : le CDN CACHE, l'hébergeur STOCKE la source originale.
- Cache périmé = bug n°1 de déploiement : pensez à purger/invalider après chaque release.
- CDN = couche 7 (HTTP) vs LB (load balancer) = répartition de charge des serveurs d'app — complémentaires.
**Exemple :** `Cache-Control: public, max-age=31536000, immutable`
**Voir aussi :** S3, cache, HTTP, cloud

## `ETL` — Extraction-Transformation-Chargement [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 65
**Signification :** Extract, Transform, Load (Extraire, Transformer, Charger)
**Définition :** Processus qui copie des données de plusieurs sources vers un entrepôt en les nettoyant et les reformattant.
**Contextes :** reporting d'entreprise, data warehouse, migration de base, synchronisation d'outils
**Cas réguliers :**
- `Extraction CRM + facturation → entrepôt analytics` — Rapport consolidé (le plus courant)
- `Nettoyage : normaliser emails, dédupliquer` — Transformer avant chargement
- `Chargement nocturne dans le data warehouse` — Batch planifié
**Origine :** Terme des data warehouses (années 1990, Bill Inmon/Ralph Kimball) ; les ETL traditionnels (Informatica, 1993) ont évolué vers ELT (charger puis transformer dans la base).
**Subtilités/confusions :**
- ETL vs ELT : ETL = transformer AVANT (flux contrôlé), ELT = charger PUIS transformer (puissance de la base).
- ETL vs API sync : ETL = batch (nuit), API sync = temps réel ; souvent complémentaires.
- Data quality : une entrée pourrie en amont = décision fausse en aval ("garbage in, garbage out").
**Exemple :** `dbt run --models stg_clients` — chargement puis transformation versionnée en SQL
**Voir aussi :** data warehouse, BI, SQL, SGBD

## `VPS` — Serveur virtuel loué [Cloud]
**Catégorie :** Cloud | **Niveau :** debutant | **Popularité :** 75
**Signification :** Virtual Private Server (Serveur Privé Virtuel)
**Définition :** Une part d'un serveur physique virtualisée, louée avec ses ressources garanties (CPU, RAM, disque) et un accès root.
**Contextes :** hébergement de sites, bots, petits services, apprentissage sysadmin, tunneling
**Cas réguliers :**
- `Louer un VPS Ubuntu 4 Go pour 5€/mois` — Héberger un site ou un service (le plus courant)
- `VPS pour un reverse proxy Caddy/nginx` — Centraliser plusieurs services derrière HTTPS
- `VPS en Alsace/Paris pour la RGPD` — Localisation des données en France
**Origine :** Concept popularisé par les hébergeurs (Virtuozzo/OpenVZ dès 2001, puis KVM) — entre le shared hosting (partagé) et le serveur dédié.
**Subtilités/confusions :**
- VPS vs hébergement mutualisé : VPS = tu es seul sur ta part (root, isolé), mutualisé = partagé sans root.
- VPS vs cloud (IaaS) : VPS = forfait mensuel fixe, cloud = à l'usage ; pour un petit service le VPS est 3-10x moins cher.
- "VPS illimité" n'existe pas : les ressources sont partagées avec les voisins (overcommit).
**Exemple :** `ssh root@mon-vps -p 22`
**Voir aussi :** IaaS, cloud, VM, hébergement

## `MongoDB` — Base documentaire JSON [Bases de données]
**Catégorie :** Bases de données | **Niveau :** intermediaire | **Popularité :** 76
**Signification :** MongoDB (de "humongous" — énorme)
**Définition :** Base NoSQL documentaire : chaque enregistrement est un JSON (BSON) flexible, stocké dans des collections.
**Contextes :** catalogues produits, contenu éditorial, APIs JSON, prototypage sans schéma figé
**Cas réguliers :**
- `db.produits.insertOne({nom: "Clavier", prix: 49})` — Ajouter un document (le plus courant)
- `db.produits.find({prix: {$lt: 50}})` — Requête filtrée
- `db.produits.createIndex({nom: 1})` — Index pour accélérer la recherche (essentiel en prod)
- `mongodump --db boutique` — Sauvegarder la base
**Origine :** 10gen (devenu MongoDB Inc.), 2009, par le fondateur Dwight Merriman — réponse aux bases relationnelles face au Big Data web 2.0.
**Subtilités/confusions :**
- MongoDB ≠ sans schéma : les validations de schéma existent (JSON Schema) — les ignorer = données incohérentes.
- Le champ _id est obligatoire et auto-généré (ObjectId) — pas un entier auto-incrémenté comme en SQL.
- Requêtes sans index = COLLSCAN (scan de toute la collection) — surveiller avec explain().
**Exemple :** `db.produits.find({cat: "informatique"}).sort({prix: -1}).limit(10)`
**Voir aussi :** NoSQL, SQL, SGBD, ORM

## `Redis` — Cache et clé-valeur en mémoire [Bases de données]
**Catégorie :** Bases de données | **Niveau :** avance | **Popularité :** 74
**Signification :** Remote Dictionary Server
**Définition :** Base clé-valeur ultra rapide en mémoire, utilisée pour cache, sessions, files d'attente et compteurs.
**Contextes :** cache de requêtes, sessions web, rate limiting, queues (Celery, Bull)
**Cas réguliers :**
- `SET session:abc {user} EX 3600` — Cache avec expiration 1h (le plus courant)
- `GET maclé` — Lire une valeur
- `SCAN 0 MATCH cache:* COUNT 100` — Parcourir les clés SANS bloquer (prod)
- `INCR rate:ip:1.2.3.4` — Compteur pour rate limiting
**Origine :** Salvatore Sanfilippo (antirez), 2009 — né du besoin de sortir la session des bases relationnelles ; 100k+ op/s par instance.
**Subtilités/confusions :**
- Redis est en MÉMOIRE : sans réplique + AOF, un redémarrage = perte des données — ne pas y mettre la source de vérité.
- KEYS bloque TOUT le serveur en prod (parcourt toute la base) → utiliser SCAN — cause classique d'incident.
- Redis vs memcached : Redis = multi-structures (listes, sets, TTL) et persistence ; memcached = simple cache volatil.
**Exemple :** `redis-cli SET session:abc {user} EX 60`
**Voir aussi :** NoSQL, cache, memcached, PostgreSQL

## `PostgreSQL` — SGBD relationnel avancé [Bases de données]
**Catégorie :** Bases de données | **Niveau :** intermediaire | **Popularité :** 82
**Signification :** PostgreSQL (Postgres — « Post-Ingres », suite du projet Ingres)
**Définition :** SGBD relationnel open source réputé pour sa rigueur (ACID), ses types riches et sa conformité SQL.
**Contextes :** applications métier, données géospatiales, JSONB, startups jusqu'au scale
**Cas réguliers :**
- `CREATE TABLE users (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, email TEXT UNIQUE)` — Créer une table (le plus courant)
- `SELECT * WHERE data->>'ville' = 'Paris'` — Requête sur du JSON stocké (JSONB)
- `pg_dump boutique > backup.sql` — Sauvegarder en SQL
- `psql -U postgres -d boutique` — Se connecter en CLI
**Origine :** UC Berkeley (Michael Stonebraker, POSTGRES 1986), sorti en 1996 — fidèle au modèle relationnel d'origine ; aujourd'hui souvent préféré à MySQL.
**Subtilités/confusions :**
- PostgreSQL vs MySQL : Postgres = standards, types riches, JSONB, géo ; MySQL = plus simple et hébergé partout.
- SERIAL (auto-incrément) vs IDENTITY (standard SQL) : préférer IDENTITY sur les projets neufs.
- Autocommit : chaque requête seule est commitée — transaction OBLIGATOIRE pour plusieurs opérations liées (BEGIN/COMMIT).
**Exemple :** `SELECT u.nom, count(o.id) FROM users u LEFT JOIN orders o ON o.user_id=u.id GROUP BY u.nom`
**Voir aussi :** SQL, SGBD, MySQL, ORM

## `MySQL` — SGBD relationnel le plus déployé [Bases de données]
**Catégorie :** Bases de données | **Niveau :** debutant | **Popularité :** 84
**Signification :** MySQL (« My » d'après la fille de Monty Widenius, co-fondateur)
**Définition :** SGBD relationnel open source le plus répandu, moteur des LAMP, de WordPress et de nombreux hébergeurs.
**Contextes :** sites web, blogs WordPress, applications PHP, bases d'entraînement
**Cas réguliers :**
- `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) UNIQUE)` — Créer une table (le plus courant)
- `mysqldump boutique > backup.sql` — Sauvegarder en SQL
- `mysql -u root -p boutique` — Se connecter en CLI
- `SHOW TABLES;` — Lister les tables
**Origine :** MySQL AB, 1995 — racheté par Sun (2008) puis Oracle (2010) ; la communauté a forké en MariaDB (2009) par le fondateur originel.
**Subtilités/confusions :**
- MySQL vs MariaDB : forks frères, compatibles mais dérivés (fonctions, moteurs) — les confondre casse des requêtes subtiles.
- MySQL vs PostgreSQL : MySQL = vitesse et simplicité (web classique), Postgres = rigueur standards et fonctionnalités riches.
- utf8 de MySQL est en réalité utf8mb3 (3 octets) → les emojis cassent : utiliser utf8mb4.
**Exemple :** `SELECT * FROM users WHERE email = ?` — toujours avec requête préparée (anti-injection)
**Voir aussi :** SQL, PostgreSQL, SGBD, MariaDB

## `SQLite` — Base embarquée en 1 fichier [Bases de données]
**Catégorie :** Bases de données | **Niveau :** debutant | **Popularité :** 80
**Signification :** SQLite (SQL en version litote : « lite » = sans serveur)
**Définition :** Moteur SQL complet embarqué dans l'application, stocké dans UN SEUL fichier, sans processus serveur.
**Contextes :** apps mobiles (Android/iOS), navigateurs, dictionnaire IT offline, prototypage, CLI
**Cas réguliers :**
- `sqlite3 dictionnaire.db "SELECT * FROM entrees"` — Interroger en 1 ligne (le plus courant)
- `.tables` puis `.schema entrees` — Explorer la base dans l'CLI
- `sqlite3 dico.db < migration.sql` — Appliquer un script SQL
- `PRAGMA journal_mode=WAL;` — Mode écriture concurrente (requis pour apps multi-lecteurs)
**Origine :** D. Richard Hipp, 2000 — pour le dragon embossé de l'hôtel de RDF qui réclamait un SGBD sans admin ; la DB la plus déployée au monde (milliards d'instances : téléphones, navigateurs, systèmes d'exploitation).
**Subtilités/confusions :**
- SQLite n'a PAS de serveur : pas d'accès réseau, pas d'utilisateur — un seul processus écrit à la fois (concurrence limitée).
- SQLite vs MySQL/Postgres : SQLite = embarqué/local ; les autres = serveur réseau — SQLite n'est pas fait pour des milliers d'utilisateurs simultanés.
- Un fichier = toute la base : le sauvegarder suffit (cp dictionnaire.db backup.db).
**Exemple :** `sqlite3 dico.db "SELECT COUNT(*) FROM entrees WHERE face='A'"`
**Voir aussi :** SQL, SGBD, PostgreSQL, FTS5

## `FTS5` — Recherche plein texte SQLite [Bases de données]
**Catégorie :** Bases de données | **Niveau :** avance | **Popularité :** 60
**Signification :** Full-Text Search version 5 (module de SQLite)
**Définition :** Extension SQLite indexant du texte pour des recherches mot-clé RAPIDES avec rangs de pertinence — le cœur de la recherche du Dictionnaire IT.
**Contextes :** recherche offline, applications mobiles, dictionnaires, logs, sans serveur Elasticsearch
**Cas réguliers :**
- `CREATE VIRTUAL TABLE fts USING fts5(nom, role, contenu)` — Créer l'index plein texte (le plus courant)
- `SELECT * FROM fts WHERE fts MATCH 'reseau OR tcp'` — Recherche plein texte avec opérateurs
- `SELECT *, rank FROM fts WHERE fts MATCH 'grep' ORDER BY rank` — Résultats triés par pertinence
- `INSERT INTO fts(nom, role) VALUES (...)` — Alimenter (ou via trigger sur la table source)
**Origine :** Module intégré à SQLite 3.9 (2015) par D. Richard Hipp — remplace FTS3/FTS4 plus anciens et moins performants.
**Subtilités/confusions :**
- FTS5 vs LIKE '%mot%' : LIKE parcourt TOUTE la table (lent), FTS5 utilise un index inversé (rapide même sur des millions de lignes).
- MATCH n'aime pas les accents/casse mal configurés : prévoir tokenizer (unicode61 remove_diacritics 1) pour un dico FR.
- FTS5 est une table VIRTUELLE : le contenu vit dans l'index — préférer triggers pour rester synchronisé avec la table principale.
**Exemple :** `CREATE VIRTUAL TABLE fts USING fts5(nom, role_fr, content='entrees', content_rowid='id')`
**Voir aussi :** SQLite, SQL, recherche, tokenisation

## `BI` — Intelligence d'affaires [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 68
**Signification :** Business Intelligence (Intelligence d'Affaires)
**Définition :** Collecte et visualisation des données de l'entreprise pour éclairer les décisions (tableaux de bord, rapports).
**Contextes :** reporting direction, KPIs commerciaux, data warehouse, aide à la décision
**Cas réguliers :**
- `Tableau de bord Power BI avec CA par région` — Suivi mensuel (le plus courant)
- `Fichier Excel consolidé (exports SQL)` — La "BI" de 90% des PME
- `Grafana sur metrics serveurs` — BI d'infrastructure (temps réel)
**Origine :** Terme popularisé par les analystes IBM (années 1960 « Business Intelligence » relu par Hans Peter Luhn, 1958) ; outils modernes : Tableau (2003), Power BI (2015).
**Subtilités/confusions :**
- BI ≠ data science : BI = DÉCRIRE le passé/présent (tableaux), data science = PRÉDIRE le futur (modèles).
- Une BI sur données sales = décisions fausses — la qualité de l'amont (ETL) prime sur le joli dashboard.
- BI en temps réel vs batch : choisir selon le besoin (Grafana temps réel, reporting mensuel = suffisant).
**Exemple :** `SELECT mois, SUM(total) FROM commandes GROUP BY mois`
**Voir aussi :** ETL, data warehouse, dashboard, KPI

## `Docker` — Conteneurs d'application [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 90
**Signification :** Docker (la « baleine » qui porte les conteneurs — logo de la baleine)
**Définition :** Plateforme qui empaquette une application avec TOUTES ses dépendances dans un conteneur léger, reproduisible partout.
**Contextes :** environnements identiques dev/prod, microservices, déploiements reproductibles, isolation
**Cas réguliers :**
- `docker build -t monapp .` — Créer une image depuis un Dockerfile (le plus courant)
- `docker run -p 8080:80 monapp` — Lancer un conteneur (port hôte:conteneur)
- `docker ps` — Voir les conteneurs en cours (ajouter -a pour tous)
- `docker compose up -d` — Monter l'ensemble (app + base + cache) en arrière-plan
**Origine :** Solomon Hykes, présentation Lightning Talk à PyCon chez dotCloud, 2013 — a rendu accessibles les conteneurs Linux (namespaces/cgroups existaient depuis 2002-2008).
**Subtilités/confusions :**
- Docker ≠ VM : conteneur partage le noyau de l'hôte (léger) vs VM avec son propre OS (lourd).
- Le .dockerignore est aussi important que .gitignore : sans lui, node_modules part dans l'image (gigaoctets).
- `docker rmi` supprime une IMAGE, `docker rm` un CONTENEUR — confusion de raccourcis très fréquente.
**Exemple :** `docker logs -f <conteneur>` — suivre les logs (réflexe debug n°1)
**Voir aussi :** Kubernetes, Docker Compose, container, image

## `Terraform` — Infrastructure as Code déclaratif [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 76
**Signification :** Terraform (« former la terre » — l'infra façonnée comme un paysage)
**Définition :** Outil open source qui crée et modifie l'infrastructure (VM, réseaux, bases) à partir de fichiers de configuration déclaratifs.
**Contextes :** cloud multi-fournisseur, environnements reproductibles, revue de code sur l'infra
**Cas réguliers :**
- `terraform init` — Initialiser le projet (télécharge les providers — le plus courant)
- `terraform plan` — Aperçu du changement SANS l'appliquer (toujours avant apply)
- `terraform apply` — Créer/modifier l'infra décrite dans main.tf
- `terraform destroy` — Tout supprimer (⚠️ vérifier le plan avant !)
**Origine :** HashiCorp (Mitchell Hashimoto et Armon Dadgar), 2014 — premier outil majeur multi-cloud de l'IaC ; le state devient le miroir de l'infra réelle.
**Subtilités/confusions :**
- Terraform vs Ansible : Terraform CRÉE les ressources (déclaratif, state) ; Ansible configure ce qui tourne (impératif, sans state).
- Le state (terraform.tfstate) = sacré : le perdre ou le dupliquer en équipe = drift → toujours un backend distant partagé.
- `apply` sans `plan` en prod = mauvaise pratique — le plan est la revue de sécurité.
**Exemple :** `terraform state list` — savoir ce que Terraform gère
**Voir aussi :** IaC, Ansible, DevOps, GitOps

## `Ansible` — Configuration automatisée sans agent [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 72
**Signification :** Ansible (le « messager interstellaire » d'Asimov — orchestration sans agent)
**Définition :** Outil qui configure et déploie sur des serveurs en SSH avec des playbooks YAML, sans agent à installer.
**Contextes :** configuration de flotte de serveurs, déploiements d'apps, tâches répétitives multi-hôtes
**Cas réguliers :**
- `ansible-playbook -i inventaire site.yml` — Exécuter un playbook (le plus courant)
- `ansible all -m ping -i inventaire` — Tester la connexion SSH de tous les hôtes
- `ansible-playbook --check site.yml` — Mode simulation (rien n'est modifié)
**Origine :** Michael DeHaan (aussi co-créateur de Puppet), 2012 — le nom vient d'Asimov ; racheté par Red Hat (2015).
**Subtilités/confusions :**
- Ansible vs Terraform : Ansible CONFIGURE (OS, services, fichiers), Terraform CRÉE les ressources cloud.
- Sans agent = SSH requis sur chaque cible — pas d'agent à maintenir, mais la connexion doit exister.
- Un playbook doit être idempotent (état voulu) — toujours `--check` avant l'exécution en prod.
**Exemple :** `ansible-playbook site.yml --limit web1` — n'agir que sur un hôte
**Voir aussi :** IaC, Terraform, DevOps, YAML

## `Azure` — Cloud Microsoft [Cloud]
**Catégorie :** Cloud | **Niveau :** debutant | **Popularité :** 85
**Signification :** Azure (« horizon bleu » — autrefois Windows Azure, 2010)
**Définition :** Suite cloud de Microsoft : VMs, Azure AD, SQL Database, App Service, intégration native à Windows et Microsoft 365.
**Contextes :** entreprises Microsoft (Active Directory, .NET), environnements hybrides Windows/Linux, données en France
**Cas réguliers :**
- `Azure AD Connect avec le domaine local` — SSO entre annuaire local et cloud (le plus courant en entreprise)
- `App Service pour héberger une webapp .NET` — PaaS Microsoft
- `Blob Storage pour les backups` — Équivalent S3 d'Azure
- `az group create` — Gérer en CLI (az = équivalent aws)
**Origine :** Microsoft, 2010 (Windows Azure), renommé Microsoft Azure en 2014 — 2e part mondiale derrière AWS, 1er auprès des entreprises déjà installées Microsoft.
**Subtilités/confusions :**
- Azure AD (identités) ≠ Azure (infra) : deux produits au même endroit — aujourd'hui renommé Microsoft Entra ID.
- Azure vs AWS : même gamme de services, noms différents (Blob vs S3, VM vs EC2) — les concepts transitent.
- Régions France Central / France South disponibles pour la RGPD — vérifier la région des ressources sensibles.
**Exemple :** `az vm list-ip-addresses --output table`
**Voir aussi :** AWS, GCP, cloud, Entra ID

## `GCP` — Google Cloud Platform [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 75
**Signification :** Google Cloud Platform (Google Cloud)
**Définition :** Suite cloud de Google : Compute Engine, BigQuery, Cloud Run, Kubernetes managé (GKE) — réputée pour la data.
**Contextes :** data engineering, machine learning, startups, analytics, Google Workspace
**Cas réguliers :**
- `BigQuery pour analyser des milliards de lignes` — SQL sur lac de données (le plus courant)
- `Cloud Run pour déployer un conteneur sans cluster` — Serverless conteneurisé
- `GKE pour Kubernetes managé` — Le K8s d'origine, géré par ses créateurs
- `gcloud auth login` — S'authentifier en CLI
**Origine :** Google, 2008 (App Engine) — le réseau mondial de Google (le même que Search) en ossature ; a créé Kubernetes puis l'a confié à la CNCF.
**Subtilités/confusions :**
- GCP vs Google Workspace : GCP = cloud IT (serveurs, data), Workspace = bureautique (Gmail, Docs) — abonnements distincts.
- BigQuery vs SQL classique : même syntaxe mais facturé au téraoctet analysé — un SELECT * mal écrit coûte cher.
- BigQuery ≠ base OLTP : c'est de l'analytique, pas des écritures transactionnelles.
**Exemple :** `bq query --use_legacy_sql=false 'SELECT count(*) FROM dataset.table'`
**Voir aussi :** AWS, Azure, BigQuery, cloud

## `GitOps` — L'infra pilotée par Git [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 65
**Signification :** Git Operations (Opérations par Git)
**Définition :** Git = source de vérité UNIQUE de l'infrastructure : une modification = un commit, un agent applique automatiquement la différence.
**Contextes :** déploiements Kubernetes, infra reviewable en pull request, reproductibilité totale
**Cas réguliers :**
- `Pull request sur le repo d'infra → ArgoCD applique` — Changement validé puis appliqué (le plus courant)
- `Drift détecté : l'agent resynchronise` — La prod revient à l'état de Git (auto-réparation)
- `Rollback = git revert` — Retour arrière tracé et daté
**Origine :** Concept formalisé par Alexis Richardson (Weaveworks), popularisé par ArgoCD (2018) ; s'appuie sur les pratiques CI/CD.
**Subtilités/confusions :**
- GitOps ≠ CI/CD : la CI/CD POUSSED les changements, le GitOps fait PULLE depuis Git (l'agent réconcilie).
- Un commit dans le repo d'infra = une modification RÉELLE en prod : branch rules du repo = critique.
- Le drift (prod modifiée à la main) est détecté et écrasé — toute modification manuelle en prod est perdue.
**Exemple :** `argocd app diff monapp` — voir l'écart entre Git et la prod
**Voir aussi :** CI, ArgoCD, DevOps, IaC

## `SRE` — Site Reliability Engineering [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 70
**Signification :** Site Reliability Engineering (Ingénierie de Fiabilité des Sites)
**Définition :** Discipline née chez Google : appliquer le génie logiciel à l'exploitation, avec des objectifs de fiabilité CHIFFRÉS (SLO) et un budget d'erreur.
**Contextes :** services à haute dispo, astreintes structurées, gros trafic, réduction des incidents
**Cas réguliers :**
- `SLO : 99,9% de requêtes < 300ms` — Objectif mesuré en continu (le plus courant)
- `Budget d'erreur consommé → gèle des features` — La fiabilité devient un budget d'équipe
- `Post-mortem sans blâme après incident` — On blame le système, pas la personne
**Origine :** Google, livre "Site Reliability Engineering" (2016, libre) — écrit par l'équipe qui opère Search ; premier ingénieur "Site Reliability" : Ben Treynor (2003).
**Subtilités/confusions :**
- SRE vs DevOps : SRE = une IMPLÉMENTATION précise du DevOps avec métriques ; DevOps = la culture globale.
- SLA vs SLO vs SLI : SLI = mesure brute (latence), SLO = cible interne (99,9%), SLA = engagement CONTRACTUEL client (pénalités).
- L'astreinte ne peut pas prendre 100% du temps dev : la règle 50/50 ops/dev de Google sert de base.
**Exemple :** `erreur_budget = SLO - disponibilité réelle sur 30j`
**Voir aussi :** DevOps, SLA, monitoring, post-mortem

## `Jenkins` — Serveur d'intégration continue [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 68
**Signification :** Jenkins (majordome — logo du majordome)
**Définition :** Serveur open source qui exécute automatiquement les builds/tests/déploiements à chaque commit (CI/CD).
**Contextes :** pipelines d'entreprise, projets hérités, déploiements Jenkinsfile versionnés
**Cas réguliers :**
- `Pipeline Jenkinsfile dans le repo` — Le pipeline est du code versionné (le plus courant)
- `Build déclenché à chaque push` — Feedback en quelques minutes
- `Paramètres de build (branche, env)` — Exécution manuelle paramétrée
- `Credential store pour les secrets` — Clés stockées chiffrées, pas dans le Jenkinsfile
**Origine :** Kohsuke Kawaguchi chez Sun, 2004 (Hudson) — scission en Jenkins en 2011 après conflit avec Oracle ; leader historique du CI, concurrencé par GitHub Actions/GitLab CI.
**Subtilités/confusions :**
- Jenkins vs GitLab CI/GitHub Actions : Jenkins = serveur auto-hébergé très extensible (plugins), les autres = intégrés au forfait git.
- Les 1800+ plugins sont sa force ET sa faiblesse (cassures après upgrade).
- "Jenkins passe mais prod casse" : le pipeline ne remplace pas les tests ni la revue.
**Exemple :** `pipeline { stages { stage('Test') { steps { sh 'pytest' } } } }`
**Voir aussi :** CI, CD, GitLab, GitHub Actions

## `Lambda` — Fonctions serverless AWS [Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 77
**Signification :** AWS Lambda (λ — la fonction mathématique)
**Définition :** Exécuter du code réactionnel sans serveur : la fonction tourne à la demande, facturée à la milliseconde d'exécution.
**Contextes :** traitements d'événements, APIs légères, automatismes sans maintenance, coûts à l'usage
**Cas réguliers :**
- `Lambda déclenché par un upload S3` — Traitement automatique de fichier (le plus courant)
- `Lambda derrière API Gateway` — API payée à l'usage réel
- `Cron EventBridge toutes les heures` — Tâche planifiée sans serveur
- `Lambda@Edge` — Fonction exécutée au point de présence CDN le plus proche
**Origine :** AWS, 2014 — premier grand service serverless public ; a créé toute une génération d'architectures événementielles.
**Subtilités/confusions :**
- Cold start : première exécution = latence (100ms-1s) — à compenser si l'API est temps réel.
- 15 minutes MAX par exécution : un traitement plus long doit être découpé (ou utiliser ECS/Batch).
- Le code doit démarrer vite et sans état (stateless) — sinon la fonction est mal adaptée.
**Exemple :** `aws lambda invoke --function-name resize --payload '{"key":"img.png"}' out.json`
**Voir aussi :** Serverless, AWS, API Gateway, PaaS

## `Helm` — Gestionnaire de paquets Kubernetes [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 66
**Signification :** Helm (le gouvernail — K8s = bateau, Helm = gouvernail)
**Définition :** « apt de Kubernetes » : des charts (templates paramétrés) pour installer des applications K8s en 1 commande.
**Contextes :** déploiements K8s réutilisables, environnements dev/stag/prod, apps tierces sur cluster
**Cas réguliers :**
- `helm install monapp ./chart -f prod.yaml` — Déployer avec valeurs d'env (le plus courant)
- `helm upgrade --install monapp bitnami/postgresql` — Mettre à jour sans downtime
- `helm list` — Voir les releases du cluster
- `helm rollback monapp 2` — Revenir à la version précédente en 1 ligne
**Origine :** Deis puis CNCF/Google, 2015 — a introduit le packaging pour K8s quand les YAML bruts devenaient ingérables.
**Subtilités/confusions :**
- Helm ≠ Kubernetes : Helm GÉRE des déploiements K8s, il ne remplace pas le moteur.
- `--install` rend la commande idempotente : créer OU mettre à jour selon l'existant — réflexe moderne.
- Un chart tiers = YAML exécuté sur ton cluster : auditer (bitnami officiel vs repo perso).
**Exemple :** `helm template monapp ./chart | kubectl apply -f -` — prévisualiser sans installer
**Voir aussi :** Kubernetes, kubectl, DevOps, YAML

## `SLA` — Engagements de service contractuels [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 74
**Signification :** Service Level Agreement (Accord de Niveau de Service)
**Définition :** Contrat qui engage un fournisseur sur des mesures de service (disponibilité, latence) avec des sanctions en cas de manquement.
**Contextes :** contrats hébergeur/cloud, SaaS d'entreprise, engagements clients, pénalités financières
**Cas réguliers :**
- `SLA 99,9% de dispo = 8h47 d'arrêt max/an` — Le plus courant (3 nines)
- `Crédit de remboursement si manquement` — La sanction classique du cloud
- `Mesures définies en SLI puis cibles en SLO` — La chaîne complète SLI→SLO→SLA
**Origine :** Contrats de télécom des années 1980 (AT&T), généralisés par le cloud (AWS ECP, 2009) ; formalisés avec les SLO par le SRE de Google.
**Subtilités/confusions :**
- SLA vs SLO vs SLI : SLI = ce qu'on mesure, SLO = la cible interne, SLA = le contrat client (souvent MOINS strict que le SLO pour laisser de la marge).
- Un SLA à 99,9% = ~4 min/semaine d'arrêt acceptable — personne ne promet 100%.
- Les pénalités sont généralement des CRÉDITS (remboursement partiels), pas des indemnités — lire la clause.
**Exemple :** `99,95% sur 30j = 21 min 54 s d'arrêt maximum`
**Voir aussi :** SRE, monitoring, uptime, cloud

## `Webhook` — Notification par appel automatique [Web/DevOps]
**Catégorie :** DevOps | **Niveau :** debutant | **Popularité :** 72
**Signification :** Web Hook (« crochet web »)
**Définition :** Quand un événement arrive, un système APPELE automatiquement ton URL avec les données — push inversé d'une API.
**Contextes :** notifications GitHub/Slack, paiement Stripe, sync entre outils, CI déclenchée
**Cas réguliers :**
- `GitHub → POST sur ton URL à chaque push` — Déclencher une CI ou un bot (le plus courant)
- `Stripe notifie ta plateforme d'un paiement` — Événement critique temps réel
- `Slack Incoming Webhook pour une alerte` — Pousser un message dans un canal
**Origine :** Terme popularisé par les API publiques (PayPal, eBay, GitHub) vers 2009-2012 — résout le polling inutile ("et si on t'appelait ?").
**Subtilités/confusions :**
- Webhook vs API : l'API c'est TOI qui demandes (pull), le webhook c'est EUX qui notifient (push).
- Le webhook doit répondre 200 vite sinon le sender RETENTE (potentiellement en boucle) — idempotence requise.
- URL de callback = secret : la divulguer permet d'injecter de faux événements → signer les payloads.
**Exemple :** `Content-Type: application/json + header X-Signature: sha256=...`
**Voir aussi :** API REST, CI, polling, event-driven

## `Microservices` — Architecture en services découpés [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 76
**Signification :** Microservices (Petits Services)
**Définition :** Découper une application en petits services indépendants (équipes, déploiements, bases séparés) communiquant par API.
**Contextes :** équipes multiples, scaling ciblé, Codebase gigantesque, projets à longue vie
**Cas réguliers :**
- `Service panier déployé sans toucher au catalogue` — Déploiements indépendants (le plus courant)
- `Chaque service = sa base de données` — Isolation forte (mais plus de JOIN inter-services)
- `Communication par API REST/gRPC ou messages` — Frontière de service = contrat d'API
**Origine :** Terme forgé par les architectes de ThoughtWorks (Fred George, 2008-2011) et popularisé par Netflix (2012) en remplacement du monolithe.
**Subtilités/confusions :**
- Microservices ≠ SOA redécoupée : la SOA avait un bus central (ESB), les microservices parlent directement.
- Pas de "petits services" par défaut : chaque découpe ajoute réseau, latence, défaillance — le monolithe bien fait bat des 50 microservices mal gérés.
- Base de données par service = cohérence finale (sagas) au lieu de transactions ACID globales.
**Exemple :** `Temps de réponse total = somme des services appelés → limiter la profondeur de chaîne`
**Voir aussi :** Docker, Kubernetes, API REST, DevOps

## `Prometheus` — Métriques et alertes de monitoring [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 68
**Signification :** Prometheus (le Titan qui vola le feu aux dieux — le dieu de la surveillance)
**Définition :** Système open source qui collecte des métriques (pull), les stocke en séries temporelles et déclenche des alertes (PromQL).
**Contextes :** monitoring infra/apps, alerting d'astreinte, dashboards Grafana, Kubernetes
**Cas réguliers :**
- `alerte : taux d'erreur HTTP > 5% pendant 5 min` — Règle d'alerting (le plus courant)
- `rate(http_requests_total[5m])` — Requête PromQL classique
- `Scrape /metrics toutes les 15s` — Chaque service expose ses métriques
**Origine :** SoundCloud, 2012 — inspiré par le monitoring de Borg chez Google ; gradué CNCF (2016), standard de facto du monitoring cloud-native.
**Subtilités/confusions :**
- Prometheus PULL (il va chercher les /metrics) vs agents push (StatsD) — le modèle pull domine en K8s.
- Les métriques avec cardinalité énorme (user_id en label) explosent la mémoire — labels à cardinalité contrôlée.
- Prometheus = données & alertes, Grafana = VISUALISATION : ils vont ensemble mais sont distincts.
**Exemple :** `histogram_quantile(0.95, rate(latency_bucket[5m]))` — latence P95
**Voir aussi :** Grafana, monitoring, alerting, SRE

## `Grafana` — Dashboards de visualisation [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 73
**Signification :** Grafana (l'astronome graphique — visuels et étoiles)
**Définition :** Plateforme open source qui transforme des données (Prometheus, SQL, logs) en dashboards et alertes partagés.
**Contextes :** supervision infra, tableaux de bord métier, alertes visuelles, revues d'équipe
**Cas réguliers :**
- `Dashboard : CPU, RAM, requêtes/s en direct` — Vue unifiée multi-sources (le plus courant)
- `Panneau annotations à chaque déploiement` — Corréler incidents et releases
- `Alerte Grafana envoyée sur Slack/Teams` — Notification quand un seuil tombe
**Origine :** Torkel Ödegaard (Released), 2014 — fork de Kibana d'abord, devenu l'IHM de supervision standard ; racheté par la société Grafana Labs (2019).
**Subtilités/confusions :**
- Grafana ≠ Prometheus : Grafana AFFICHE, Prometheus COLLECTE — même écosystème, rôles distincts.
- Grafana est multi-sources : un même dashboard peut mélanger Postgres + Prometheus + CloudWatch.
- Variables de dashboard (par région, par service) = éviter 50 dashboards quasi identiques.
**Exemple :** `Grafana → Add data source → Prometheus (http://prom:9090)`
**Voir aussi :** Prometheus, monitoring, dashboard, SRE

## `Kafka` — Flux d'événements distribués [Data/DevOps]
**Catégorie :** Data | **Niveau :** avance | **Popularité :** 72
**Signification :** Apache Kafka (du nom de Franz Kafka — flux et messages comme prédestination)
**Définition :** Plateforme de flux d'événements distribués : publier/consommer des messages durables à très haut débit, ordonnés par partition.
**Contextes :** pipelines de données temps réel, microservices événementiels, ingestion de logs, event sourcing
**Cas réguliers :**
- `Producer publie dans un topic, consumers en groupes` — Découplage à haut débit (le plus courant)
- `Event stream → entrepôt analytics` — Alimentation data platform
- `Rejeu des messages après incident` — Les offsets autorisent la relecture
**Origine :** Né chez LinkedIn (Jay Kreps, Neha Narkhede, Jun Rao), 2011, open-sourcé en 2012 sous Apache — devenu l'épine dorsale d'un très grand nombre de plateformes data.
**Subtilités/confusions :**
- Kafka ≠ file d'attente type RabbitMQ : Kafka conserve les messages (durée configurable) et permet le rejeu — RabbitMQ supprime après consommation.
- Un consommateur PULL des batchs : la progression est stockée en offsets (d'où le rejeu possible).
- Cardinalité des topics : créer un topic par utilisateur = explosion (préférer partition/clé).
**Exemple :** `kafka-console-producer --topic commandes --bootstrap-server localhost:9092`
**Voir aussi :** RabbitMQ, event-driven, microservices, data streaming

## `Data Warehouse` — Entrepôt analytique [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 66
**Signification :** Data Warehouse (Entrepôt de Données)
**Définition :** Base centralisée OPTIMISÉE pour l'analyse : données historisées de multiples sources, structurées en étoile pour le reporting.
**Contextes :** reporting d'entreprise, historisation longue, BI, analyse croisée
**Cas réguliers :**
- `Fait_vente liée à Dimensions (temps, produit, région)` — Schéma en étoile (le plus courant)
- `Chargement nocturne depuis les sources opérationnelles` — Séparation OLTP/OLAP
- `Historisation type 2 (valid_from/valid_to)` — Garder toutes les versions d'un produit
**Origine :** Bill Inmon (« père du data warehouse », 1990) et Ralph Kimball (dimensionnel, 1996) — leurs deux approches structurent encore tous les projets data.
**Subtilités/confusions :**
- Data warehouse vs data lake : entrepôt = données STRUCTURÉES et nettoyées (SQL), lac = brut de tout format (cheap, mais à gouverner).
- OLTP (production, écritures) ≠ OLAP (analyse, lectures) : ne pas greffer le reporting sur la base de prod.
- Le schéma en étoile dénormalisé est VOLONTAIRE : plus rapide pour les jointures de rapports.
**Exemple :** `SELECT r.region, SUM(f.montant) FROM fait_vente f JOIN dim_region r ...`
**Voir aussi :** ETL, BI, data lake, OLAP

## `RabbitMQ` — File de messages légère [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 70
**Signification :** RabbitMQ (« lapin messager » — protocole AMQP)
**Définition :** Broker de messages open source : producteurs publient dans des files/échanges, consommateurs récupèrent — messages supprimés après traitement.
**Contextes :** découplage de services, tâches asynchrones (facturation, emails), files de travaux
**Cas réguliers :**
- `File de tâches : worker traite les emails un par un` — Asynchrone (le plus courant)
- `Exchange fanout → plusieurs services notifiés` — Diffusion à N abonnés
- `Message rejeté → re-queue avec TTL` — Gestion d'échecs sans perte
**Origine :** Rabbit Technologies, 2007 — implémentation open source du protocole AMQP (2003, financé par JP Morgan) ; aujourd'hui VMware/Broadcom.
**Subtilités/confusions :**
- RabbitMQ vs Kafka : RabbitMQ = file classique (supprime après lecture, point-à-point), Kafka = journal durable (relecture possible).
- Un message non acké remet en file si le worker MEURT — prévoir idempotence côté consommateur.
- Management UI sur le port 15672 : indispensable pour voir les files bloquées.
**Exemple :** `rabbitmqctl list_queues name messages` — voir la profondeur des files
**Voir aussi :** Kafka, microservices, event-driven, queue

## `API Gateway` — Point d'entrée unique des APIs [Web/Cloud]
**Catégorie :** Cloud | **Niveau :** intermediaire | **Popularité :** 74
**Signification :** API Gateway (Passerelle d'API)
**Définition :** Service unique qui reçoit toutes les requêtes API puis les route vers les bons services, avec auth, rate limit et cache.
**Contextes :** microservices, APIs multi-clients, agrégation, sécurité centralisée
**Cas réguliers :**
- `Client → Gateway → service panier / service users` — Routage (le plus courant)
- `Clé API validée à la frontière` — Auth centralisée, services internes non exposés
- `100 req/min par clé` — Rate limiting sans le coder dans chaque service
- `Agrégation : 1 appel externe = 3 appels services internes` — BFF pour mobile
**Origine :** Concept des EAI (années 1990) renouvelé par le cloud : API Gateway d'AWS (2015), Kong (2015 sur NGINX), Apigee (Google, 2016).
**Subtilités/confusions :**
- API Gateway vs reverse proxy (nginx) : le proxy streame du HTTP, le gateway COMPREND l'API (auth, quotas).
- Ne PAS mettre de logique métier dans le gateway — il devient le monolithe qu'on fuyait.
- Point de défaillance unique → le déployer en HA derrière un load balancer.
**Exemple :** `Host: api.exemple.fr → routes /v1/users → service-users:8080`
**Voir aussi :** microservices, Load Balancer, API REST, cloud

## `GraphQL` — Langage d'interrogation d'API flexible [Web]
**Catégorie :** Web | **Niveau :** intermediaire | **Popularité :** 75
**Signification :** Graph Query Language (Langage de Requête Graphique)
**Définition :** Alternative à REST : le client DEMANDE exactement les champs voulus, le serveur répond en un seul point d'entrée.
**Contextes :** apps mobiles à données hétérogènes, BFF, APIs multi-clients, évolution sans breaking change
**Cas réguliers :**
- `query { user(id:1) { nom, posts { titre } } }` — Exactement les champs nécessaires (le plus courant)
- `mutation { createUser(nom:"Ada") { id } }` — Écritures
- `Champ déprécié annoncé dans le schéma` — Évolution en douceur des clients
**Origine :** Facebook (Lee Byron et Petter Skoldberg), créé en 2012, open-sourcé en 2015 — pour le flux mobile à bandwidth limité ; aujourd'hui à la CNCF.
**Subtilités/confusions :**
- GraphQL ≠ base de données : c'est un LANGAGE d'API qui se branche sur tes sources existantes.
- REST = multiples endpoints (/users, /users/1/posts), GraphQL = UN endpoint avec requêtes structurées.
- Requêtes coûteuses (imbriquages profonds) → limiter la profondeur et la complexité côté serveur.
**Exemple :** `curl -X POST /graphql -d '{"query":"{ users { id nom } }"}'`
**Voir aussi :** API REST, API Gateway, gRPC, web

## `Data Lake` — Lac de données brut [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 64
**Signification :** Data Lake (Lac de Données)
**Définition :** Stockage massif de données BRUTES dans leur format d'origine (JSON, logs, images, CSV) — on structure à la lecture, pas à l'écriture.
**Contextes :** données hétérogènes, machine learning, logs massifs, explorations futures inconnues
**Cas réguliers :**
- `Raw zone : dumps JSON + logs + CSV au même endroit` — Tout atterrir d'abord (le plus courant)
- `Schema-on-read : structurer quand on consomme` — Contrairement au warehouse
- `Zones : raw / curated / mart` — Empêcher le "swamp"
**Origine :** Terme popularisé par la communauté Big Data (2010-2011, articles James Dixon/Pentaho) — réponse à la rigidité des entrepôts face aux données non prévues.
**Subtilités/confusions :**
- Data lake vs data warehouse : lake = brut et cheap (exploration), warehouse = structuré et fiable (reporting).
- Sans gouvernance, le lake devient un SWAMP : données inutilisables, personne ne sait ce qu'elles valent.
- JAMAIS de données confidentielles non classifiées — un lake ouvert = fuite massive.
**Exemple :** `s3://datalake/raw/2026/09/logs/... → spark job → curated/events.parquet`
**Voir aussi :** data warehouse, ETL, BI, S3

## `OLAP` — Analyse multidimensionnelle [Data]
**Catégorie :** Data | **Niveau :** avance | **Popularité :** 60
**Signification :** Online Analytical Processing (Traitements Analytiques En Ligne)
**Définition :** Techniques de requêtes sur données agrégées en hypercubes (ventes × temps × région) pour le reporting instantané.
**Contextes :** rapports croisés, analyse de tendances, BI, cube de décision
**Cas réguliers :**
- `CA par région ET par mois ET par produit` — Découpage en tous sens (le plus courant)
- `Roll-up : remonter du jour au trimestre` — Agrégation hiérarchique
- `Drill-down : zoomer de la région au client` — Descendre dans la granularité
**Origine :** Concept formalisé par Edgar Codd (1993 — le même qui a inventé le relationnel), puis incarné par les OLAP servers (Essbase 1993, Microsoft SSAS) ; cousin de l'OLTP.
**Subtilités/confusions :**
- OLAP vs OLTP : OLTP = transactionnel (écrire vite, une ligne), OLAP = analytique (lire des millions de lignes agrégées).
- L'hypercube est pré-agrégé : répond en ms mais ne se met pas à jour en temps réel (rafraîchi par batch).
- Snowflake vs étoile : deux modèles dimensionnels — l'étoile est le plus répandu.
**Exemple :** `SELECT region, annee, SUM(ca) ... GROUP BY ROLLUP(region, annee)`
**Voir aussi :** data warehouse, BI, ETL, SQL

## `gRPC` — RPC haute performance [Web]
**Catégorie :** Web | **Niveau :** avance | **Popularité :** 62
**Signification :** gRPC (Google Remote Procedure Call)
**Définition :** Framework d'appels RPC binaires : appeler une fonction comme si elle était locale, sur le réseau, avec Protobuf et HTTP/2.
**Contextes :** communication inter-services à haut débit, microservices, streams binaires
**Cas réguliers :**
- `Service A appelle ServiceB.getUser()` — RPC typé (le plus courant)
- `Multiplexing HTTP/2 : 100 appels sur 1 connexion` — Beaucoup plus rapide que REST/JSON
- `Bidirectional streaming : les deux côtés envoient en continu` — Temps réel
**Origine :** Google (à partir de RPC/Stubby interne), open-sourcé en 2015, gradué CNCF — le Protobuf (2001) en est le format de sérialisation.
**Subtilités/confusions :**
- gRPC vs REST : gRPC = binaire + HTTP/2 (rapide, inter-services), REST = texte JSON (lisible, public, navigateur).
- Le navigateur ne gère pas nativement le gRPC : à la frontière client, REST/GraphQL reste nécessaire (ou grpc-web).
- Protobuf = contrat .proto versionné — c'est LUI qui génère les clients (codegen), pas la main.
**Exemple :** `service Greeter { rpc SayHello (HelloRequest) returns (HelloReply); }`
**Voir aussi :** API REST, GraphQL, microservices, protobuf

## `ELT` — Charger puis transformer [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 63
**Signification :** Extract, Load, Transform (Extraire, Charger, Transformer)
**Définition :** Variante moderne de l'ETL : charger les données BRUTES dans la base cible PUIS les transformer avec la puissance de cette base.
**Contextes :** pipelines cloud, Lakehouse, transformations versionnées en SQL (dbt), données brutes conservées
**Cas réguliers :**
- `Raw → warehouse → dbt transform en SQL versionné` — La chaîne ELT moderne (le plus courant)
- `Toutes les colonnes chargées d'abord` — Conserver le brut permet de re-transformer
- `Tests de données après transformation` — Qualité vérifiée dans la base
**Origine :** Popularisé avec les entrepôts cloud puissants et bon marché (Snowflake 2015, dbt 2016) — le T déplacé dans la base coûte moins cher qu'un ETL dédié.
**Subtilités/confusions :**
- ELT vs ETL : ETL = transformer AVANT (flux contrôlé), ELT = charger PUIS transformer (brut conservé).
- ELT exige une base cible PUISSANTE : sur un petit moteur, l'ETL dédié est plus rapide.
- Le brut doit rester reproductible : si la transformation rate, on repart du brut sans re-extraire.
**Exemple :** `dbt run --models stg_clients` — transformations versionnées dans la base
**Voir aussi :** ETL, data warehouse, dbt, BI

## `ArgoCD` — Déploiements GitOps pour Kubernetes [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 64
**Signification :** ArgoCD (Argo = le navire des Argonautes, Continuous Delivery)
**Définition :** Déployeur GitOps pour K8s : surveille un dépôt Git et applique automatiquement les changements au cluster.
**Contextes :** clusters K8s, équipes plateforme, déploiements reproductibles, audit des changements
**Cas réguliers :**
- `argocd app sync monapp` — Synchroniser Git → cluster (le plus courant)
- `Sync automatique + self-heal` — Le drift est corrigé tout seul
- `UI : comparaison live vs Git` — Voir exactement ce qui diffère
- `argocd app rollback` — Retour à une révision Git précédente
**Origine :** Intuit puis gradué CNCF (Argoproj), 2018 — a défini le pattern GitOps applicatif tel qu'on le connaît aujourd'hui.
**Subtilités/confusions :**
- ArgoCD ne BUILD pas : c'est un déploiement (le build reste dans la CI) — CD au sens strict.
- Sync waves : plusieurs applications (base puis app) se déploient dans un ORDRE — sinon crashloop.
- Self-heal : la valeur du repo Git prime TOUJOURS sur une modif manuelle kubectl.
**Exemple :** `argocd app set monapp --sync-policy auto` — auto-synchronisation
**Voir aussi :** GitOps, Kubernetes, Helm, CD

## `DevSecOps` — Sécurité intégrée à la chaîne DevOps [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 71
**Signification :** Development + Security + Operations
**Définition :** Intégrer la sécurité À CHAQUE étape du cycle (build, test, déploiement) au lieu de la réserver à une fin de projet.
**Contextes :** audits sécurité, conformité, gestion des vulnérabilités, shift left
**Cas réguliers :**
- `Scan d'image Docker à chaque build (Trivy)` — Blocage si CVE critique (le plus courant)
- `SAST sur chaque pull request` — Analyse du code source pendant la revue
- `Secrets scannés dans le repo (gitleaks)` — Empêcher les clés commitées
- `SBOM de chaque livraison` — Liste des composants logiciels livrés
**Origine :** Réponse au DevOps sans sécurité (années 2010, Zero Trust, « Shift Left ») ; encadré aujourd'hui par les frameworks SLSA et NIST SSDF.
**Subtilités/confusions :**
- DevSecOps ≠ "auditeur en fin de projet" : la sécurité devient un pipeline, pas une étape finale.
- Le shift left fait GAGNER de l'argent : corriger une faille en prod coûte ~30x plus cher qu'en build.
- Trop de scans = alert fatigue → blocker sur le critique, signaler le reste.
**Exemple :** `trivy image monapp:latest` — avant push au registre
**Voir aussi :** CI, sécurité, SAST, supply chain

## `Load Balancer` — Répartition de charge entre serveurs [Réseau]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 78
**Signification :** Load Balancer (Équilibreur de Charge)
**Définition :** Point d'entrée qui distribue les requêtes entre plusieurs serveurs selon une stratégie (round-robin, charge, session).
**Contextes :** HA multi-serveurs, scale horizontal, maintenance sans interruption, terminaison TLS
**Cas réguliers :**
- `Requêtes réparties sur 4 serveurs app` — Le plus courant (round-robin)
- `least-connections, IP hash` — Autres stratégies classiques
- `Health checks : serveur mort = retiré automatiquement` — Auto-réparation
- `TLS terminaison sur le LB` — HTTPS déchiffré une fois, pas sur chaque serveur
**Origine :** Équilibreurs matériels des réseques (années 1990, F5, Cisco) ; délogés par le logiciel : NGINX (2004), HAProxy (2006), puis les LB managés cloud (ALB, Cloud Load Balancing).
**Subtilités/confusions :**
- LB L7 (HTTP, comprend l'URL) vs L4 (TCP brut, plus rapide) : choisir selon le besoin.
- Round-robin aveugle vs least-connections : le premier peut écraser un serveur déjà en charge.
- Le LB devient SPOF s'il n'est pas lui-même en HA — les LB cloud sont managés multi-AZ.
**Exemple :** `upstream backend { server app1; server app2; }` (nginx)
**Voir aussi :** reverse proxy, HA, nginx, cloud

## `HA` — Haute Disponibilité [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 76
**Signification :** High Availability (Haute Disponibilité)
**Définition :** Concevoir un système pour qu'il reste accessible même en cas de panne d'un composant (redondance + bascule automatique).
**Contextes :** services critiques, e-commerce, infra cloud, contrats SLA exigeants
**Cas réguliers :**
- `2 serveurs + load balancer au lieu d'1` — Éliminer le point unique de défaillance (le plus courant)
- `Multi-AZ : répartir sur 2 zones de données` — Survivre à la panne d'une zone
- `Bascule automatique si health check échoue` — Failover sans intervention humaine
- `Base primaire + réplique en lecture` — Continuer à servir les lectures
**Origine :** Terminologie télécom des « cinq nines » (99,999%, ~5 min/an) ; systèmes redondés dès les mainframes IBM (années 1960), systématisés par le cloud (AZs, régions).
**Subtilités/confusions :**
- HA ≠ backup : HA garde le service EN COURS, le backup sauvegarde les DONNÉES — les deux sont nécessaires.
- HA ≠ scale : la HA survit aux pannes, le scale suit la charge — 2 serveurs ne suffisent pas pour 10x trafic.
- Un SPOF caché (DNS, LB unique, base unique) annule toute la redondance — cartographier les dépendances.
**Exemple :** `99,9% = 8h47/an | 99,99% = 52min/an | 99,999% = 5min/an`
**Voir aussi :** Load Balancer, SLA, cloud, SPOF

## `Registry` — Dépôt d'images conteneur [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 67
**Signification :** Container Registry (Registre de Conteneurs)
**Définition :** Service qui stocke et distribue les images Docker (versionnées par tag), avec scan de sécurité et politique d'accès.
**Contextes :** partage d'images CI → prod, images privées, scan de vulnérabilités, pull en prod
**Cas réguliers :**
- `docker push monapp:1.4` — Publier une image (le plus courant)
- `docker pull monapp:1.4` — Récupérer sur un serveur de prod
- `GHCR / Docker Hub / ECR / ACR` — Registres publics et privés majeurs
- `Tags : latest vs 1.4.2 vs git-sha` — Identifier une build de façon fiable
**Origine :** Docker Hub (2013, initialement index.docker.io) a créé le pattern ; ensuite les registres privés : Harbor (2016, CNCF), ECR (AWS), ACR (Azure), GHCR (GitHub).
**Subtilités/confusions :**
- `latest` n'est PAS figé : c'est un alias mou — en prod, tagger par VERSION ou SHA de commit.
- Image ≠ conteneur : l'image est le gabarit immuable, le conteneur est l'exécution en cours.
- Un registre privé ne rend pas une image sûre : scanner quand même (Trivy) avant le pull prod.
**Exemple :** `docker tag monapp:dev ghcr.io/equipe/monapp:1.4.2 && docker push ghcr.io/equipe/monapp:1.4.2`
**Voir aussi :** Docker, image, DevSecOps, CI

## `Observability` — Comprendre l'état d'un système [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 70
**Signification :** Observability (Observabilité)
**Définition :** Capacité à déduire l'état INTERNE d'un système à partir de ses sorties (métriques, logs, traces) — sans deviner à l'avance.
**Contextes :** debug en production, microservices complexes, SRE, réduction du MTTR
**Cas réguliers :**
- `3 piliers : metrics + logs + traces corrélés` — Le modèle complet (le plus courant)
- `Trace distribuée : 1 requête traverse 6 services` — Retrouver le coupable (Jaeger, Tempo)
- `Alerte sur symptôme utilisateur (taux d'erreur), pas sur CPU` — Alertes utiles vs bruit
**Origine :** Concept d'ingénierie des systèmes (années 1960, théorie du contrôle), remis au goût du jour par Twitter (Finagle, Zipkin 2012) face aux microservices.
**Subtilités/confusions :**
- Monitoring vs observabilité : monitoring = ce qu'on SAIT déjà vouloir voir (dashboards prédéfinis), observabilité = explorer l'inconnu.
- 3 piliers sans corrélation (même trace_id partout) = 3 silos qui ne s'expliquent pas.
- Un dashboard ne prouve rien sans contexte (déploiement récent, changement de config).
**Exemple :** `trace_id=abc123 → logs des 6 services de la requête en 1 recherche`
**Voir aussi :** Prometheus, Grafana, SRE, monitoring

## `Blue/Green` — Déploiement par deux environnements [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 65
**Signification :** Blue/Green (Bleu/Vert — les deux couleurs d'environnement)
**Définition :** Maintenir DEUX environnements identiques : on déploie la nouvelle version sur l'inactif, on bascule le trafic d'un coup, rollback = re-basculer.
**Contextes :** mises à jour critiques sans interruption, infra non containerisée, validation avant switch
**Cas réguliers :**
- `Blue = prod actuelle, Green = version 2 testée` — Puis bascule du load balancer (le plus courant)
- `Rollback en 1 clic : re-basculer sur Blue` — Revenir à l'ancienne instantanément
- `Tester Green avec un % de trafic avant` — Variante progressive
**Origine :** Pratique décrite par Martin Fowler et Paul Hammant (2010) dans le contexte CI/CD — popularisée par les PaaS pouvant dupliquer les environnements.
**Subtilités/confusions :**
- Blue/Green vs Canary : Blue/Green = bascule TOUTE OU RIEN ; Canary = migration PROGRESSIVE par pourcentage.
- Les DEUX environnements doivent tourner (coût x2 temporaire) — c'est le prix du rollback rapide.
- Une base de données partagée casse le pattern : prévoir des migrations rétro-compatibles (expand/contract).
**Exemple :** `Switch LB : 100% → blue | rollback : 100% → green`
**Voir aussi :** canary, CD, déploiement, rollback

## `Canary` — Déploiement progressif par cohortes [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 66
**Signification :** Canary Release (« Release canari » — les canaris dans les mines, alerte précoce)
**Définition :** Exposer la nouvelle version à un PETIT pourcentage d'utilisateurs d'abord, élargir si les métriques restent saines.
**Contextes :** APIs à fort trafic, réduction du risque de release, features à impact incertain
**Cas réguliers :**
- `1% → 10% → 50% → 100% du trafic` — Progression conditionnée aux métriques (le plus courant)
- `Alertes canari : taux d'erreur de la version neuve` — Critère d'arrêt automatique
- `Comparaison des deux versions en parallèle` — Mesure d'impact réelle
**Origine :** Métaphore des mines de charbon (canaris sentinelles) appliquée au déploiement par les pratiques Agile (2000s), systématisée par Google (2010s) et les feature flags.
**Subtilités/confusions :**
- Canary vs Blue/Green : canary = progressif sur vrais users, blue/green = bascule nette entre deux environnements.
- Sans métriques fiables, un canary est aveugle : il faut pouvoir DÉTECTER la régression pour l'arrêter.
- Router par user/session, sinon un user alterne entre versions (bugs de cohérence).
**Exemple :** `1% du trafic → critère : taux d'erreur < 0,1% sur 15 min → passage à 10%`
**Voir aussi :** blue/green, CD, feature flag, SRE

## `Docker Compose` — Multi-conteneurs en 1 fichier [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 80
**Signification :** Docker Compose (Composition d'images Docker)
**Définition :** Décrire une application complète (app + base + cache...) dans un fichier YAML puis la démarrer d'un seul geste.
**Contextes :** environnement local de dev, empilement multi-services, démos, tests d'intégration
**Cas réguliers :**
- `docker compose up -d` — Monter tout l'empilement en arrière-plan (le plus courant)
- `docker compose down` — Tout arrêter et supprimer les réseaux
- `docker compose logs -f api` — Suivre les logs d'un service
- `docker compose ps` — État des services du fichier
**Origine :** Fig (2013) racheté par Docker (2014) — intégré à Docker Engine en 2017 (v2 : plugin `docker compose`, l'ancien `docker-compose` binaire est obsolète).
**Subtilités/confusions :**
- `docker compose` (nouveau, plugin) vs `docker-compose` (v1, trait d'union) : mêmes commandes, binaire différent.
- Le YAML décrit l'EMPILEMENT (réseaux partagés, volumes, ordre avec depends_on) — pas le rôle d'un Dockerfile.
- `down -v` supprime AUSSI les volumes (données de la base !) — relire avant.
**Exemple :** `services: { web: {build: ., ports: ["8080:80"]}, db: {image: postgres} }`
**Voir aussi :** Docker, Kubernetes, YAML, image

## `Feature Flag` — Activer des features sans redéployer [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 69
**Signification :** Feature Flag (Drapeau de Fonctionnalité)
**Définition :** Interrupteur dans le code qui active/désactive une feature à l'exécution, par utilisateur ou par pourcentage, sans redéployer.
**Contextes :** déploiements continus, tests A/B, activation progressive, kill switch d'incident
**Cas réguliers :**
- `if flag("new-checkout") : ...` — Code déployé, feature cachée (le plus courant)
- `Activation à 5% des users → 100%` — Déploiement par paliers
- `Kill switch : couper une feature qui casse` — Retour instantané sans rollback du build
**Origine :** Pratique née du trunk-based development chez Facebook, Google et Flickr (années 2000-2010) ; outillée par LaunchDarkly (2014), Unleash, Flagsmith.
**Subtilités/confusions :**
- Un flag est TEMPORAIRE : garder les flags morts = dette technique (date de suppression dans le ticket).
- Flag ≠ déploiement : le code est en prod dans les DEUX cas — le flag décide de la visibilité.
- Trop de flags simultanés = matrice ingérable à tester (limiter le nombre actif).
**Exemple :** `env "checkout-v2" : pourcentage=10, targeting=beta-users`
**Voir aussi :** canary, CI/CD, A/B testing, rollback

## `Chaos Engineering` — Test volontaire de résilience [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 55
**Signification :** Chaos Engineering (Ingénierie du Chaos)
**Définition :** Injecter des pannes VOLONTAIRES en production contrôlée pour découvrir les faiblesses AVANT qu'elles n'arrivent naturellement.
**Contextes :** systèmes à haute disponibilité, maturité ops, réduction des incidents, game day
**Cas réguliers :**
- `Couper un serveur en plein trafic` — Vérifier le failover (le plus courant)
- `Latence artificielle +300ms sur un service` — Tester la tolérance aux ralentissements
- `Game Day : exercice d'incident en équipe` — Préparer l'astreinte sans urgence réelle
**Origine :** Netflix Chaos Monkey (2011, dans la Simian Army) — pour survivre aux pannes AWS ; principes formalisés par Casey Rosenthal et Nora Jones (livre O'Reilly, 2020).
**Subtilités/confusions :**
- Chaos ≠ sabotage : hypothèse d'abord, périmètre limité, rollback immédiat — sinon c'est du vandalisme.
- Règle d'or : sans observation pendant l'expérience, on n'apprend RIEN.
- Commencer en DEV/staging, puis production à faible blast radius — maturité requise.
**Exemple :** `kubectl delete pod --grace-period=0 sur 1 replica` — panne simulée ciblée
**Voir aussi :** SRE, HA, game day, résilience

## `Elasticsearch` — Moteur de recherche et analyse [Data]
**Catégorie :** Data | **Niveau :** avance | **Popularité :** 78
**Signification :** Elasticsearch (Lucene distribué par Elastic)
**Définition :** Moteur de recherche plein texte distribué sur index JSON — recherche instantanée, analytics de logs, moteur derrière Kibana.
**Contextes :** moteur de recherche de site, centralisation de logs, analytics temps réel
**Cas réguliers :**
- `GET /logs/_search {"query": {"match": {"message": "erreur 500"}}}` — Recherche plein texte (le plus courant)
- `Indexation en quasi temps réel (~1s)` — Logs visibles presque immédiatement
- `Agrégations : count par niveau, top des IPs` — Analytics sans SQL
**Origine :** Shay Banon, 2010 (sur Lucene, 1999) — ossature de la stack ELK (Elasticsearch, Logstash, Kibana) ; le changement de licence (Apache → SSPL/Elastic License, 2021) a fait naître le fork OpenSearch d'AWS.
**Subtilités/confusions :**
- Elasticsearch ≠ base transactionnelle : pas de JOIN, pas d'ACID — c'est un INDEX, la source de vérité reste ailleurs.
- Le mapping est un schéma IMPLICITE : un champ mal deviné au premier doc (text vs keyword) casse les agrégations.
- Cluster mal dimensionné en RAM = OOM (circuit breaker) — un index par logique, pas par jour "au cas où".
**Exemple :** `GET /logs-2026.09/_count` — éléments de l'index du mois
**Voir aussi :** Kibana, FTS5, logstash, NoSQL

## `MariaDB` — Fork communautaire de MySQL [Bases de données]
**Catégorie :** Bases de données | **Niveau :** debutant | **Popularité :** 62
**Signification :** MariaDB (prénom de la fille de Monty Widenius, co-créateur de MySQL)
**Définition :** SGBD relationnel forké de MySQL par son créateur après le rachat par Oracle — compatible MySQL dans l'essentiel.
**Contextes :** Debian/Ubuntu (remplace MySQL par défaut), hébergeurs, migration de WordPress
**Cas réguliers :**
- `mariadb-dump boutique > backup.sql` — Sauvegarder (syntaxe mysqldump)
- `mariadb -u root -p boutique` — Se connecter en CLI
- `SELECT VERSION();` — Savoir exactement ce qui tourne
**Origine :** Michael "Monty" Widenius, 2009, après le rachat de Sun/MySQL par Oracle (2008) — assurer la continuité open source ; distribué par défaut sur Debian et la plupart des distros.
**Subtilités/confusions :**
- MariaDB vs MySQL : compatibles mais DIVERGENT (moteurs, réplication, SQL étendu) — les dumps ne circulent pas toujours dans les deux sens.
- `mysql` en commande peut appeler MariaDB sur Debian — vérifier avec `SELECT VERSION();`.
- MySQL 8 vs MariaDB 11 = deux feuilles de route distinctes malgré l'origine commune.
**Exemple :** `SELECT VERSION();` → "11.4.2-MariaDB" par exemple
**Voir aussi :** MySQL, SQL, SGBD, PostgreSQL

## `Istio` — Maillage de services (service mesh) [DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 60
**Signification :** Istio (grec : « voile » — le navire avance au voile)
**Définition :** Couche réseau qui ajoute sécurité (mTLS), observabilité et routage ENTRE les conteneurs, sans changer le code applicatif.
**Contextes :** microservices K8s multiples, mTLS obligatoire, canary au niveau trafic, circuit breaking
**Cas réguliers :**
- `mTLS activé entre tous les services` — Chiffrement interne automatique (le plus courant)
- `Routage : 10% du trafic vers v2` — Canary géré par le mesh, pas dans le code
- `Retry/timeout/circuit breaker par défaut` — Résilience imposée au service
**Origine :** Lyft (2017) puis Google et IBM — le service mesh naît du besoin d'observabilité inter-services quand toutes les équipes ne peuvent pas instrumenter leur code.
**Subtilités/confusions :**
- Istio vs Kubernetes : K8s ORCHESTRE les pods, Istio gère le TRAFIC entre pods — complémentaires, surcharge ~1-2% de latence.
- Sidecar (envoy par pod) = cœur du mesh : plus de pods = plus d'envoys à gérer (coût mémoire).
- Complexité majeure : souvent surdimensionné pour une petite équipe — à activer progressivement.
**Exemple :** `istioctl proxy-status` — état des sidecars du mesh
**Voir aussi :** Kubernetes, microservices, mTLS, observability

## `Vault` — Gestion centralisée des secrets [Sécurité/DevOps]
**Catégorie :** DevOps | **Niveau :** avance | **Popularité :** 66
**Signification :** Vault (Coffre-fort — HashiCorp Vault)
**Définition :** Stocker, délivrer et faire tourner les secrets (mots de passe, clés API, certificats) — plus jamais de clé en dur dans le code.
**Contextes :** rotation de secrets, CI qui récupère ses clés au build, chiffrement applicatif, conformité
**Cas réguliers :**
- `vault kv get secret/prod/db` — Récupérer un secret à la volée (le plus courant)
- `Rotation automatique du mot de passe base` — Secret jamais statique
- `Clés AWS dynamiques (90 min puis expirées)` — Credentials éphémères
- `Transit engine : chiffrer les données applicatives` — Clé maître centralisée
**Origine :** HashiCorp (Mitchell Hashimoto et Armon Dadgar), 2015 — réponse au "secret dans le .env commité par erreur" ; standard de facto de la gestion de secrets.
**Subtilités/confusions :**
- Vault ≠ coffre-fort simple : il DÉLIVRE des secrets temporaires (dynamiques) plutôt que de stocker du statique.
- Secret en dur dans le repo = compromis définitif (git le garde même après suppress) → révoquer TOUT de suite.
- Mode HA obligatoire en prod : si Vault est down, les services qui renouvellent leur lease ne démarrent pas.
**Exemple :** `vault kv put secret/ci/deploy token=...` — puis lecture par la CI, jamais dans les logs
**Voir aussi :** IAM, sécurité, secrets, DevSecOps

## `Kibana` — Exploration de logs et dashboards [Data]
**Catégorie :** Data | **Niveau :** intermediaire | **Popularité :** 70
**Signification :** Kibana (nom inventé par l'équipe — la « K » de la stack ELK)
**Définition :** Interface web d'Elasticsearch : explorer les logs, construire des dashboards et alertes de la Elastic Stack.
**Contextes :** centralisation de logs, investigation d'incident, dashboards d'usage, audit
**Cas réguliers :**
- `Discover : chercher "error 500" sur 7 jours` — Investigation en 1 clic (le plus courant)
- `Dashboard : count par service, top des routes` — Vue d'ensemble des logs
- `Index pattern : logs-* par date` — Gestion des index de logs
- `Alerte sur champ` — Notification quand un motif apparaît
**Origine :** Rashid Khan, 2013 — la « K » de ELK (Elasticsearch, Logstash, Kibana) ; aujourd'hui Elastic Stack.
**Subtilités/confusions :**
- Kibana n'analyse PAS : elle AFFICHE — toute la recherche est exécutée par Elasticsearch en dessous.
- Un champ non-indexé (mapping) donne 0 résultat trompeur → vérifier le mapping avant de conclure "pas de logs".
- Kibana sans auth = tous les logs lisibles (souvent des clés dedans) — toujours protéger.
**Exemple :** `@timestamp >= "now-1h" AND status >= 500`
**Voir aussi :** Elasticsearch, logstash, logging, observability

## `MTTR` — Temps moyen de rétablissement [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 72
**Signification :** Mean Time To Repair (Temps Moyen de Réparation)
**Définition :** Durée moyenne entre le début d'un incident et le retour du service à la normale — la métrique reine de la réactivité d'astreinte.
**Contextes :** post-mortems, revues d'astreinte, tableaux de bord SRE, objectifs d'amélioration
**Cas réguliers :**
- `MTTR de 45 min sur 10 incidents ce mois` — Mesure mensuelle (le plus courant)
- `Objectif : réduire le MTTR de 30% ce trimestre` — KPI d'équipe
- `MTTD + MTTA + MTTR décomposés` — Distinguer détection, prise en charge, réparation
**Origine :** Maintenance industrielle (années 1960, fiabilité des systèmes) ; remis au premier plan par le SRE de Google et les métriques DORA (2013).
**Subtilités/confusions :**
- MTTR = 3 homonymes : REPAIR (réparer), RESTORE (restaurer backup), RESPOND (réagir) — préciser lequel on cite.
- MTBF vs MTTR : MTBF = temps MOYEN ENTRE pannes (fiabilité), MTTR = temps pour réparer (réactivité).
- Réduire le MTTR d'abord : prévenir toutes les pannes est long, un rollback rapide protège déjà les users.
**Exemple :** `MTTR = Σ(durées d'incident) / nombre d'incidents`
**Voir aussi :** SRE, MTBF, post-mortem, SLA

## `DORA` — Métriques de performance de livraison [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 64
**Signification :** DevOps Research and Assessment (métriques DORA)
**Définition :** Les 4 métriques qui mesurent la performance d'une équipe logicielle : fréquence de déploiement, délai de livraison, taux de changement, taux d'échec.
**Contextes :** auto-évaluation d'équipe, comparaison annuelle (State of DevOps), maturité CI/CD
**Cas réguliers :**
- `Déploiements par jour + délai commit→prod` — Les 2 métriques de VITESSE (le plus courant)
- `Taux d'échec de changement + MTTR` — Les 2 métriques de STABILITÉ
- `Niveaux : Elite / High / Medium / Low` — Le benchmark annuel
**Origine :** Étude annuelle Puppet (2013), reprise et renommée DORA chez Google (2018, livre Accelerate par Forsgren, Humble, Kim) — la référence empirique du DevOps.
**Subtilités/confusions :**
- VITESSE ET STABILITÉ ensemble : déploiements fréquents MAIS cassés = niveau LOW, pas ELITE.
- Mesurer l'ÉQUIPE, pas l'individu : objectifs personnels sur ces métriques = tricheries (bugs séparés des features...).
- DORA ≠ outillage : des pipelines parfaits avec une culture toxique baissent les scores.
**Exemple :** `Elite : déploiements multiples par jour, MTTR < 1h, taux d'échec < 15%`
**Voir aussi :** CI/CD, SRE, MTTR, Accelerate

## `Post-mortem` — Analyse d'incident sans blâme [DevOps]
**Catégorie :** DevOps | **Niveau :** intermediaire | **Popularité :** 71
**Signification :** Post-mortem (« après la mort » — analyse rétrospective d'incident)
**Définition :** Compte rendu structuré d'un incident : chronologie, cause racine, actions correctives — centré sur le SYSTÈME, pas sur la personne.
**Contextes :** incident en prod, amélioration continue, partage d'expérience, réduction du MTTR
**Cas réguliers :**
- `Timeline : 14h02 alerte, 14h12 cause identifiée...` — Chronologie factuelle (le plus courant)
- `5 Whys : pourquoi ? → pourquoi ? → cause racine` — Remonter au fond du problème
- `Actions avec owner et deadline` — Pas de "on fera attention"
- `Publié et lu par toute l'équipe` — Le savoir doit circuler
**Origine :** Aviation (rapports d'accident sans poursuite, Culture Safety, années 1990) et SRE de Google (2016) ; adoption étendue après chaque gros incident (Cloudflare, GitHub...).
**Subtilités/confusions :**
- Sans blame culture, les gens CACHENT les incidents → les vraies causes n'émergent jamais.
- "Cause humaine" n'est JAMAIS une cause racine : l'erreur humaine est le symptôme d'un système qui la permet.
- Post-mortem ≠ sanction : c'est un document d'apprentissage ; en cas de récidive, c'est le PROCESSUS qui a échoué.
**Exemple :** `Action : ajouter un health check sur le cache — owner: Alice — 12/10`
**Voir aussi :** SRE, MTTR, incident, retro

## `Runbook` — Procédure opérationnelle d'astreinte [DevOps]
**Catégorie :** DevOps | **Niveau :** debutant | **Popularité :** 67
**Signification :** Runbook (« carnet de bord » — procédures d'exploitation)
**Définition :** Document pas-à-pas décrivant comment diagnostiquer et traiter une situation donnée, exécutable par n'importe qui d'astreinte.
**Contextes :** astreinte, escalade, reprise après sinistre, onboarding ops
**Cas réguliers :**
- `Alerte "disk > 90%" → commande de nettoyage` — Procédure d'astreinte (le plus courant)
- `Reprise après panne base : étapes 1-5` — DRP exécutable
- `Escalade : niveau 1 → niveau 2 → équipe périmètre` — Qui appeler quand
**Origine :** Opérations télécom/mainframe (« run books » des salles machine, années 1970-80) ; systématisés par le SRE (Google) et l'ITIL.
**Subtilités/confusions :**
- Un runbook OBSOLÈTE est plus dangereux que pas de runbook : versionner et tester (game day).
- Runbook ≠ monitoring : l'alerte TE DIT le problème, le runbook TE DIT quoi FAIRE.
- Idéal : runbook = code (scripts exécutables dans l'alerte), pas un wiki périmé.
**Exemple :** `Alerte disk-full → runbook: journalctl --vacuum-size=500M, vérifier /var/log/kern.log`
**Voir aussi :** on-call, post-mortem, monitoring, astreinte

## `TDD` — Test-Driven Development [Développement]
**Catégorie :** Développement | **Niveau :** avance | **Popularité :** 68
**Signification :** Test-Driven Development (Développement Piloté par les Tests)
**Définition :** Écrire le test AVANT le code : rouge (il échoue), vert (le code le fait passer), refactor (nettoyer) — en boucle courte.
**Contextes :** code robuste, refactoring sécurisé, conception par les exigences, revues de code
**Cas réguliers :**
- `Écrire test_sum → échoue (rouge) → coder → passe (vert)` — La boucle classique (le plus courant)
- `100% des chemins critiques testés` — Couverture ciblée
- `Refactor en confiance` — Les tests protègent les modifications
**Origine :** Kent Beck, années 1990 avec les méthodes XP (Extreme Programming), formalisé dans "Test Driven Development: By Example" (2003) ; adopté par tous les frameworks modernes (JUnit, pytest...).
**Subtilités/confusions :**
- TDD ≠ écrire les tests après : l'ordre compte — écrire le test d'abord clarifie l'API et évite le sur-conception.
- TDD ≠ 100% de couverture : une couverture de 100% avec des tests inutiles rassure sans protéger.
- RED-GREEN-REFACTOR : sauter le refactor = code sale qui s'accumule derrière les tests verts.
**Exemple :** `def test_add(): assert add(2,3) == 5  # écrit AVANT la fonction add`
**Voir aussi :** unit test, refactoring, CI, clean code

## `Technical Debt` — Dette technique cumulée [Développement]
**Catégorie :** Développement | **Niveau :** intermediaire | **Popularité :** 73
**Signification :** Technical Debt (Dette Technique)
**Définition :** Le coût reporté des raccourcis pris aujourd'hui : chaque "on corrigera plus tard" pénalise les développements futurs, avec intérêts.
**Contextes :** code legacy, raccourcis de deadline, refactoring, arbitrages produit/dev
**Cas réguliers :**
- `Copier-coller au lieu d'une abstraction partagée` — Dette à intérêts (le plus courant)
- `Bibliothèques jamais mises à jour` — Dette de sécurité qui grossit
- `Sprint "technique" trimestriel pour rembourser` — Remboursement planifié
**Origine :** Métaphore financière de Ward Cunningham (créateur de Wiki, 1992) : la dette est OK si on a l'intention de la rembourser — elle devient toxique quand on l'oublie.
**Subtilités/confusions :**
- Dette ≠ code imparfait : c'est une dette VOLONTAIRE et CONSCIENTE — l'inventorier est la moindre des choses.
- Intérêts = temps perdu à chaque feature touchant ce code — plus on attend, plus on paie.
- "On n'a pas le temps de tests" = emprunt à taux très élevé : la prochaine modification coûtera le double.
**Exemple :** `Inventaire : ticket "dette: refactor auth" — coût estimé 3j — criticité haute`
**Voir aussi :** refactoring, clean code, code legacy, sprint technique























