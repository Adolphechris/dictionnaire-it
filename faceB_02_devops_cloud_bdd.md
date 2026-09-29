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





