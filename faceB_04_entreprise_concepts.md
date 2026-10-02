## `ERP` — Enterprise Resource Planning [Entreprise/Système]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** PGI (Progiciel de Gestion Intégré)
**Contextes :** centraliser la gestion opérationnelle de l'entreprise (comptabilité, achats, stocks, ressources humaines, ventes) dans une base de données unique
**Rôle :** Système d'information unifié qui automatise et intègre l'ensemble des processus métier d'une organisation au sein d'une architecture modulaire commune.
**Syntaxe :** (Systèmes ERP d'entreprise : SAP S/4HANA, Oracle ERP Cloud, Odoo, Microsoft Dynamics 365)
**Cas réguliers :**
- `ERP Modulaire` — Déploiement par modules métier (Finance, RH, Supply Chain, Ventes)
- `Base de Données Unique` — Élimination des silos de données et des saisies multiples entre départements
**Origine :** Évolution des systèmes MRP (Material Requirements Planning) des années 1970 / Gartner (1990).
**Subtilités/confusions :**
- L'implémentation d'un ERP exige souvent une conduite du changement majeure car elle impose d'aligner les processus internes sur les meilleures pratiques de l'éditeur.
**Urgences/dangers :** —
**Précautions :** Éviter les développements spécifiques trop lourds (*customizations*) pour préserver la capacité de mise à jour de l'ERP.
**Équivalents :** PGI, SAP, Odoo, NetSuite
**Voir aussi :** CRM, BI, BDD, SAP

## `CRM` — Customer Relationship Management [Entreprise/Web]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** GRC (Gestion de la Relation Client)
**Contextes :** suivre les prospects, gérer les pipelines de vente, automatiser les campagnes marketing et centraliser le support client
**Rôle :** Stratégie et outil logiciel de gestion des interactions d'une entreprise avec ses clients actuels et potentiels.
**Syntaxe :** (Plateformes CRM : Salesforce, HubSpot, Zoho CRM, Microsoft Dynamics CRM)
**Cas réguliers :**
- `Gestion des Leads / Opportunités` — Suivi du cycle de vie commercial du premier contact jusqu'à la signature de la vente
- `Support & Ticketing` — Suivi de la satisfaction et des réclamations clients (Service Cloud)
**Origine :** Robert et Kate Kestnbaum / Pat Sullivan (ACT!, 1986) / Salesforce (1999).
**Subtilités/confusions :**
- Le CRM se concentre sur les relations **extérieures** (clients/prospects), alors que l'ERP gère les processus **interne** (achats/comptabilité/stocks).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Intégrer le CRM avec l'ERP de l'entreprise via des APIs pour synchroniser les commandes et factures.
**Équivalents :** Salesforce, HubSpot, Zoho
**Voir aussi :** ERP, BI, API
## `MDM` — Master Data Management [Entreprise/Data]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** Gestion des Données de Référence
**Contextes :** garantir la cohérence, l'exactitude et la déduplication des données de référence (clients, produits, fournisseurs) partagées entre l'ERP, le CRM et le e-commerce
**Rôle :** Ensemble de disciplines, d'outils et de gouvernance visant à créer une source de vérité unique et consolidée (*Golden Record*) pour les données stratégiques de l'entreprise.
**Syntaxe :** (Solutions MDM : Informatica, Semarchy, Riversand, SAP Master Data Governance)
**Cas réguliers :**
- `Golden Record` — Fiche unique consolidée et nettoyée représentant un client unique issu du croisement du CRM et de l'ERP
- `Gouvernance des Données` — Définition de règles de validation et de responsabilités des données (*Data Stewardship*)
**Origine :** Évolution de l'EAI et des Data Warehouses au début des années 2000.
**Subtilités/confusions :**
- Le MDM ne remplace pas les bases de données applicatives, mais agit comme l'arbitre central de la qualité et des référentiels.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Définir des règles d'arbitrage claires en cas de conflit d'information entre deux systèmes hôtes.
**Équivalents :** Data Governance, PIM (Product Information Management)
**Voir aussi :** ERP, CRM, ETL, BDD
## `ESB` — Enterprise Service Bus [Entreprise/Architecture]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Bus d'Intégration d'Entreprise
**Contextes :** faire communiquer des dizaines d'applications hétérogènes (ERP, CRM, bases historiques) de manière découplée sans créer de liens point-à-point spaghetti
**Rôle :** Modèle d'architecture logicielle middleware qui assure le routage, la transformation, la médiation et la sécurité des messages échangés entre applications.
**Syntaxe :** (Plateformes ESB : MuleSoft Anypoint, Apache Camel, WSO2, Red Hat Fuse)
**Cas réguliers :**
- `Transformation de Formats` — Convertir automatiquement un message XML SOAP en payload JSON REST
- `Routage Dynamique` — Aiguiller les messages vers les bons destinataires en fonction du contenu
**Origine :** Dave Chappell (2002) / concept popularisé dans les architectures SOA.
**Subtilités/confusions :**
- L'ESB centralisait toute la logique d'intégration ; dans les microservices modernes, on préfère des bus d'événements distribués comme Kafka et des API Gateways.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Éviter de coder de la logique métier complexe à l'intérieur de l'ESB (« bus intelligent, composants simples »).
**Précautions :** Privilégier les architectures d'API légères pour les nouveaux projets.
**Équivalents :** API Gateway, Kafka, Message Broker
**Voir aussi :** SOA, API, Kafka, SOAP
## `SOA` — Service-Oriented Architecture [Entreprise/Architecture]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Architecture Orientée Services
**Contextes :** concevoir les systèmes d'information d'entreprise sous forme d'un ensemble de services logiciels réutilisables, découplés et interopérables
**Rôle :** Style d'architecture logicielle dans lequel les fonctionnalités applicatives sont découpées en services autonomes exposant des interfaces contractuelles bien définies (SOAP, REST).
**Syntaxe :** (Modèle d'architecture d'intégration d'entreprise)
**Cas réguliers :**
- `Réutilisabilité des Services` — Un service "Paiement" est partagé par l'application mobile, le site e-commerce et le logiciel de caisse
- `Contrat de Service` — Définition stricte des entrées/sorties (WSDL, OpenAPI)
**Origine :** Gartner / Roy Schulte (1996) / Évolution des architectures distribuées (CORBA, DCOM).
**Subtilités/confusions :**
- **SOA** s'adresse à l'intégration à l'échelle de **toute l'entreprise** (souvent avec un ESB central) ; les **microservices** découpent **une application** en petits processus indépendants.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Veiller à ce que les contrats d'interface restent stables pour ne pas casser les applications clientes dépendantes.
**Équivalents :** Microservices, EDA (Event-Driven Architecture)
**Voir aussi :** ESB, SOAP, REST, Microservices
## `BPM` — Business Process Management [Entreprise/Management]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** GPE (Gestion des Processus Métier)
**Contextes :** modéliser, automatiser, exécuter, mesurer et optimiser les processus d'affaires de l'entreprise (ex: processus d'octroi de crédit, validation de congés, onboarding client)
**Rôle :** Discipline de gestion et suite logicielle permettant de cartographier les flux de travail (*workflows*) humains et informatiques pour les exécuter de manière fluide.
**Syntaxe :** (Moteurs BPM : Camunda, Bonita, IBM BAW, Appian)
**Cas réguliers :**
- `Modélisation BPMN` — Dessiner le processus sous forme de diagramme normalisé
- `Moteur d'Exécution` — Orchestrer l'attribution des tâches aux utilisateurs et les appels aux API informatiques
**Origine :** Howard Smith et Peter Fingar (2003).
**Subtilités/confusions :**
- Le BPM s'intéresse à l'optimisation continue du processus complet, alors que la RPA (Robotic Process Automation) s'intéresse à l'imitation de clics sur des tâches répétitives.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Impliquer les acteurs métier (*Business Analysts*) dans la modélisation pour refléter la réalité du terrain.
**Équivalents :** Workflow Engine, RPA
**Voir aussi :** BPMN, ERP, RPA
## `BPMN` — Business Process Model and Notation [Entreprise/Management]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** BPMN 2.0
**Contextes :** représenter visuellement les processus métier de manière standardisée et compréhensible à la fois par les équipes métier et les développeurs informatiques
**Rôle :** Norme graphique universelle (ISO/IEC 19510) pour la modélisation de diagrammes de flux de processus d'affaires (*workflows*).
**Syntaxe :** Standard de notation graphique (Événements ⭕, Activités ▢, Décisions ◊)
**Cas réguliers :**
- `Événement de Début / Fin` — Cercles fins (début) ou épais (fin) indiquant le déclenchement et l'aboutissement du processus
- `Passerelle (Gateway)` — Losange représentant des embranchements de décision (ex: Ou exclusif `XOR`, Et parallèle `AND`)
- `Couloirs (Pools & Lanes)` — Lignes de séparation identifiant quel rôle ou système exécute chaque tâche
**Origine :** BPMI (2004) / Géré par l'Object Management Group (OMG) (BPMN 2.0 en 2011).
**Subtilités/confusions :**
- BPMN 2.0 est un format XML exécutable directement par les moteurs de workflow comme Camunda sans réécriture de code !
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser des outils d'édition conformes (Camunda Modeler, Signavio, Draw.io) pour préserver la validité de la syntaxe XML.
**Équivalents :** UML Activity Diagram, EPC (Event-driven Process Chain)
**Voir aussi :** BPM, UML, Camunda
## `ITIL` — Information Technology Infrastructure Library [ITSM]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** ITIL v4
**Contextes :** structurer la gestion des services informatiques d'une entreprise (gestion des incidents, des changements, des problèmes et des niveaux de service SLA)
**Rôle :** Référentiel de bonnes pratiques d'origine britannique le plus largement adopté au monde pour la gestion des services IT (*IT Service Management*).
**Syntaxe :** (Référentiel méthodologique et cadre d'organisation IT)
**Cas réguliers :**
- `Gestion des Incidents` — Rétablir le fonctionnement normal du service le plus rapidement possible
- `Gestion des Changements (Change Management)` — Évaluer et approuver les mises en production pour éviter les interruptions
- `Service Desk (Centre de Services)` — Point de contact unique entre les utilisateurs et la DSI
**Origine :** CCTA / OGC britannique (années 1980 / ITIL 4 publié par AXELOS en 2019).
**Subtilités/confusions :**
- ITIL 4 a fait évoluer le cadre historique orienté « processus » vers un système de valeur des services (*Service Value System*) adapté à l'Agile et au DevOps.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Adapter ITIL au contexte de votre entreprise (« *Adopt and Adapt* ») au lieu de l'appliquer de façon bureaucratique et rigide.
**Équivalents :** ISO/IEC 20000, COBIT, FitSM
**Voir aussi :** ITSM, CMDB, SLA, DevOps
## `COBIT` — Control Objectives for Information and Related Technology [Gouvernance]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** COBIT 2019
**Contextes :** aligner la stratégie du système d'information sur les objectifs business de l'entreprise, évaluer les risques et auditer la gouvernance globale de la DSI
**Rôle :** Cadre de référence mondial de gouvernance et de management des systèmes d'information publié par l'ISACA.
**Syntaxe :** (Référentiel de gouvernance et de contrôle IT)
**Cas réguliers :**
- `Alignement Stratégique` — S'assurer que les investissements informatiques créent de la valeur mesurable pour les métiers
- `Gestion des Risques & Conformité` — Fournir des indicateurs de contrôle et de maturité pour les auditeurs et la direction générale
**Origine :** ISACA (Information Systems Audit and Control Association, 1996 / COBIT 2019).
**Subtilités/confusions :**
- **ITIL** se concentre sur le **management des services informatiques au quotidien** ; **COBIT** se situe au niveau de la **gouvernance stratégique** par le conseil d'administration et la DSI.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser COBIT lors de la préparation d'audits de conformité réglementaire majeurs (SOX, ISO 27001).
**Équivalents :** TOGAF, ISO/IEC 38500
**Voir aussi :** ITIL, TOGAF, CISO, CIO
## `TOGAF` — The Open Group Architecture Framework [Architecture]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** TOGAF Standard 10th Edition
**Contextes :** concevoir, planifier et piloter la transformation de l'architecture d'entreprise (Business, Data, Application, Technology) sur le long terme
**Rôle :** Méthodologie et cadre de référence d'Architecture d'Entreprise le plus utilisé au monde, fournissant une démarche étape par étape (méthode **ADM**).
**Syntaxe :** (Cadre de modélisation d'architecture d'entreprise)
**Cas réguliers :**
- `ADM (Architecture Development Method)` — Cycle itératif en 8 phases (de la vision d'architecture jusqu'à la gestion des changements)
- `4 Domaines d'Architecture` — Métier (Business), Données (Data), Applications (Application), Technique (Technology)
**Origine :** The Open Group (1995 / basé sur le cadre TAFIM du ministère de la défense américain).
**Subtilités/confusions :**
- Offre un langage et un cadre structuré aux architectes d'entreprise pour faire le pont entre les enjeux stratégiques généraux et les choix d'implémentation technique.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Adapter la méthode ADM pour qu'elle fonctionne de façon itérative avec les méthodologies Agiles à l'échelle (SAFe).
**Équivalents :** Zachman Framework, FEAF
**Voir aussi :** COBIT, SOA, Archimate
## `CMDB` — Configuration Management Database [ITSM]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Base de Données de Gestion des Configurations
**Contextes :** maintenir un inventaire à jour de tous les éléments du SI (serveurs, VMs, bases de données, applications, routeurs) et de leurs relations de dépendance
**Rôle :** Base de données centrale de l'ITIL qui répertorie l'ensemble des Éléments de Configuration (CI / Configuration Items) et cartographie leurs liaisons.
**Syntaxe :** (Base de données ITSM : ServiceNow CMDB, Device42, iTop, Jira Service Management)
**Cas réguliers :**
- `Élément de Configuration (CI)` — Tout composant devant être géré pour fournir un service IT (serveur physique, cluster K8s, licence, application)
- `Analyse d'Impact` — Identifier instantanément toutes les applications impactées si un commutateur réseau ou un serveur de BDD tombe en panne !
**Origine :** Concept fondateur de la méthodologie ITIL (années 1990).
**Subtilités/confusions :**
- Une CMDB ne contient pas seulement la liste des équipements, mais surtout la **carte de leurs dépendances croisées**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Une CMDB mise à jour manuellement devient obsolète et inutile en moins de 6 mois.
**Précautions :** Automatiser l'alimentation et la mise à jour de la CMDB grâce à des outils de découverte réseau dynamique (*Auto-Discovery*).
**Équivalents :** Asset Management Database, Asset Inventory
**Voir aussi :** ITIL, ITSM, CIO
## `ITSM` — IT Service Management [ITSM]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Gestion des Services Informatiques
**Contextes :** organiser la fourniture, la gestion et le support des services informatiques aux utilisateurs et aux clients avec un niveau de qualité garanti
**Rôle :** Ensemble des capacités organisationnelles orientées vers la conception, la livraison, le soutien et l'amélioration continue des services IT.
**Syntaxe :** (Discipline opérationnelle IT : ServiceNow, BMC Helix, Freshservice, Jira Service Management)
**Cas réguliers :**
- `Portail en Libre-Service` — Permettre aux employés de commander du matériel, demander des accès ou déclarer un problème en autonomie
- `Gestion des Demandes (Request Fulfillment)` — Traitement des demandes d'accès ou d'équipements standardisées
**Origine :** Émergence de l'approche orientée service dans les années 1990 (fondée sur ITIL).
**Subtilités/confusions :**
- Fait évoluer le rôle de l'IT : d'un simple gestionnaire d'équipements de secours (*gérer des serveurs*), l'IT devient un **fournisseur de services métier** (*fournir un espace de travail numérique*).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Mesurer la satisfaction des utilisateurs (*CSAT*) en plus du respect des délais de résolution de tickets (*SLA*).
**Équivalents :** ESM (Enterprise Service Management)
**Voir aussi :** ITIL, CMDB, SLA, CIO
## `CIO` — Chief Information Officer [Management/DSI]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** DSI (Directeur des Systèmes d'Information)
**Contextes :** désigner le dirigeant exécutif responsable de la stratégie, du budget, des infrastructures et des opérations informatiques d'une entreprise
**Rôle :** Membre du comité de direction chargé d'aligner les technologies de l'information sur les objectifs stratégiques de l'entreprise.
**Syntaxe :** (Poste de direction exécutive / C-Level)
**Cas réguliers :**
- `Transformation Numérique` — Piloter la modernisation des systèmes historiques vers le Cloud
- `Gestion Budgétaire IT` — Arbitrer les dépenses d'investissement (CapEx) et d'exploitation (OpEx) de la DSI
**Origine :** William R. Synnott et William H. Gruber (1981).
**Subtilités/confusions :**
- Le **CIO / DSI** se concentre sur les systèmes informatiques et opérations **interne** de l'entreprise ; le **CTO** se concentre sur les technologies et produits informatiques **vendus aux clients**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Travailler en synergie étroite avec le CISO / RSSI pour garantir que la sécurité est intégrée à chaque projet de la DSI.
**Équivalents :** DSI, VP of IT
**Voir aussi :** CTO, CISO, ITSM, COBIT
## `CTO` — Chief Technology Officer [Management/Tech]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Directeur Technique
**Contextes :** désigner le responsable exécutif des choix technologiques, de la R&D, de l'architecture logicielle et du développement des produits technologiques d'une entreprise
**Rôle :** Dirigeant technique chargé d'orienter les choix d'architecture, de piloter les équipes d'ingénierie logicielle et d'anticiper les ruptures technologiques.
**Syntaxe :** (Poste de direction exécutive / C-Level)
**Cas réguliers :**
- `Feuille de Route Produit (Tech Roadmap)` — Définir les choix d'architecture applicative et la stratégie d'ingénierie
- `Veille & R&D` — Évaluer l'impact des nouvelles technologies (IA, Cloud, Serverless) sur l'offre de l'entreprise
**Origine :** Entreprises de haute technologie américaines (années 1980).
**Subtilités/confusions :**
- Dans une startup tech, le CTO est souvent le premier développeur et l'architecte fondateur ; dans une grande entreprise, il pilote la vision et l'innovation technologique globale.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Maintenir un équilibre permanent entre l'innovation technologique et la réduction de la dette technique.
**Équivalents :** VP of Engineering, Directeur Technique
**Voir aussi :** CIO, CISO, Architecte
## `CISO` — Chief Information Security Officer [Sécurité/Management]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** RSSI (Responsables de la Sécurité des Systèmes d'Information)
**Contextes :** désigner le dirigeant exécutif responsable de la stratégie de cybersécurité, de la conformité, de la protection des données et de la gestion des risques informatiques
**Rôle :** Dirigeant chargé de définir et d'appliquer la Politique de Sécurité des Systèmes d'Information (PSSI) de l'organisation.
**Syntaxe :** (Poste de direction exécutive / C-Level)
**Cas réguliers :**
- `Gestion des Incidents de Sécurité` — Piloter la réponse aux cyberattaques, fuites de données ou ransomwares
- `Conformité Réglementaire` — S'assurer de la conformité avec le RGPD, NIS 2, DORA ou la norme ISO 27001
**Origine :** Citigroup (1995 / après les premières grandes vagues de piratage bancaire).
**Subtilités/confusions :**
- Pour éviter les conflits d'intérêts, le CISO / RSSI doit idéalement rapporter directement au Comité de Direction ou au Risk Management plutôt qu'au CIO / DSI.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Sensibiliser régulièrement l'ensemble des collaborateurs aux risques de phishing et d'ingénierie sociale.
**Équivalents :** RSSI, VP of Cybersecurity
**Voir aussi :** CIO, CTO, SIEM, EDR
## `OLA` — Operational Level Agreement [ITSM]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** Accord de Niveau Opérationnel
**Contextes :** définir les engagements de service internes entre les différents départements informatiques d'une même entreprise (ex: délai d'intervention de l'équipe réseau pour l'équipe système)
**Rôle :** Accord interne à la DSI décrivant les responsabilités et les délais d'exécution réciproques des équipes internes nécessaires au respect des contrats SLA signés avec le client.
**Syntaxe :** (Accord opérationnel interne ITIL)
**Cas réguliers :**
- `OLA Réseau vs DBA` — L'équipe réseau s'engage auprès de l'équipe base de données à ouvrir les flux de pare-feu sous 2h ouvrées
- `SLA vs OLA` — Le SLA engage la DSI vis-à-vis du **client externe** ; l'OLA engage les **équipes internes** entre elles
**Origine :** Référentiel ITIL (années 1990).
**Subtilités/confusions :**
- Sans des accords OLA internes stricts entre équipes, il est impossible de garantir le respect du contrat SLA global vis-à-vis du client.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Réviser régulièrement les OLA lors de l'introduction de nouveaux outils d'automatisation.
**Équivalents :** SLA, UC (Underpinning Contract)
**Voir aussi :** SLA, SLO, ITIL, ITSM
## `SLO` — Service Level Objective [DevOps/SRE]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Objectif de Niveau de Service
**Contextes :** définir la cible interne mesurable de disponibilité ou de performance d'un service (ex: 99.9% de requêtes HTTP réussies sur 30 jours)
**Rôle :** Objectif chiffré et précis défini par les équipes d'ingénierie (SRE/DevOps) sur la base d'un ou plusieurs indicateurs SLI.
**Syntaxe :** `SLO = 99.9% de disponibilité mensuelle`
**Cas réguliers :**
- `Budget d'Erreur (Error Budget)` — Marge d'erreur tolérée calculée à partir du SLO (ex: 99.9% d'uptime autorise 43 minutes d'indisponibilité par mois)
- `Arbitrage DevOps` — Si le budget d'erreur est consommé, les déploiements de nouvelles fonctionnalités sont gelés au profit de la stabilisation de l'infrastructure
**Origine :** Google Site Reliability Engineering (SRE, 2016).
**Subtilités/confusions :**
- Le **SLO** est l'objectif interne que visent les équipes SRE ; le **SLA** est le contrat commercial liant l'entreprise avec pénalités financières. Le SLO est toujours plus strict que le SLA !
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Fixer des SLOs réalistes : viser "100% d'uptime" est une illusion d'ingénierie financièrement ruineuse.
**Équivalents :** SLA, SLI
**Voir aussi :** SLA, SLI, SRE, Prometheus
## `SLI` — Service Level Indicator [DevOps/SRE]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Indicateur de Niveau de Service
**Contextes :** mesurer empiriquement et en temps réel la qualité d'un service informatique (taux d'erreur, latence du 99e percentile, débit)
**Rôle :** Mesure quantitative directe et factuelle d'un aspect de la performance d'un service informatique en fonctionnement.
**Syntaxe :** Ex: `SLI = (requêtes HTTP 200 en < 200ms) / (total des requêtes)`
**Cas réguliers :**
- `SLI de Latence` — Pourcentage de requêtes traitées sous la barre des 100 ms
- `SLI de Disponibilité` — Pourcentage d'appels d'API retournant un statut `200 OK` sans erreur `5xx`
**Origine :** Google Site Reliability Engineering (SRE, 2016).
**Subtilités/confusions :**
- Le **SLI** est la **mesure réelle** enregistrée par les outils de monitoring (ex: Prometheus) ; le **SLO** est la **cible** que l'on souhaite atteindre avec cette mesure.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Mesurer les SLI au plus près de l'utilisateur final (côté client ou au niveau de l'API Gateway).
**Équivalents :** KPI technique, Métrique de monitoring
**Voir aussi :** SLO, SLA, SRE, Prometheus
## `RPO` — Recovery Point Objective [ITSM/Dispositifs]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** PDMA (Perte Maximale de Données Admissible)
**Contextes :** définir la quantité maximale de données qu'une entreprise accepte de perdre lors d'un incident majeur ou d'un crash de base de données (ex: 5 minutes de transactions)
**Rôle :** Indicateur clé des plans de continuité d'activité (PCA/PRA) fixant la fréquence minimale requise des sauvegardes et de la réplication de données.
**Syntaxe :** Durée temporelle : `RPO = 15 minutes` ou `RPO = 0` (réplication synchrone)
**Cas réguliers :**
- `RPO = 0` — Aucune perte de données tolérée (exige une réplication synchrone de base de données multi-datacenter)
- `RPO = 24h` — Perte d'une journée de travail tolérée (sauvegardes nocturnes quotidiennes basiques)
**Origine :** Standards de gestion de sinistres informatiques (Disaster Recovery Institute, 1990s).
**Subtilités/confusions :**
- Le **RPO** concerne la **DONNÉE** (combien de minutes de données perdues ?) ; le **RTO** concerne le **TEMPS** (combien de temps pour rouvrir le service ?).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Diminuer le RPO vers zéro augmente de façon exponentielle les coûts d'infrastructure réseau et de stockage.
**Précautions :** Tester régulièrement la restauration des sauvegardes pour garantir la tenue réelle du RPO promis.
**Équivalents :** PDMA
**Voir aussi :** RTO, PRA, PCA, BDD
## `RTO` — Recovery Time Objective [ITSM/Dispositifs]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** DMIA (Durée Maximale d'Indisponibilité Admissible)
**Contextes :** fixer la durée maximale tolérée d'interruption complète d'un service informatique après un incident grave avant que l'entreprise ne subisse des dommages inacceptables
**Rôle :** Objectif de temps fixé dans le Plan de Reprise d'Activité (PRA) pour restaurer les infrastructures et remettre les applications à disposition des utilisateurs.
**Syntaxe :** Durée temporelle : `RTO = 2 heures`
**Cas réguliers :**
- `RTO quasi-nul (< 1 min)` — Basculement automatique (*Failover*) vers un site secondaire chaud (*Hot Site*)
- `RTO de 4h` — Redémarrage manuel des VMs et restauration des bases à partir d'un site tiède (*Warm Site*)
**Origine :** Standards de continuité d'activité (DRI / ISO 22301).
**Subtilités/confusions :**
- Le RTO inclut le temps d'alerte, le temps de diagnostic, la décision de basculement, le redémarrage et la vérification des données.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Automatiser les procédures de basculement réseau (DNS, Load Balancer) pour réduire le RTO.
**Équivalents :** DMIA
**Voir aussi :** RPO, PRA, PCA, SLA
## `PCA` — Plan de Continuité d'Activité [Management/ITSM]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** BCP (Business Continuity Plan)
**Contextes :** garantir que les activités essentielles d'une entreprise puissent se poursuivre sans interruption majeure même en cas de sinistre (incendie, cyberattaque, pandémie, panne de datacenter)
**Rôle :** Stratégie globale et ensemble de procédures documentées permettant à une organisation de maintenir ou reprendre ses fonctions critiques lors d'une crise.
**Syntaxe :** (Plan d'organisation stratégique et opérationnel)
**Cas réguliers :**
- `Analyse d'Impact (BIA - Business Impact Analysis)` — Identification des processus critiques et des tolérances de panne de l'entreprise
- `Infrastructures Redondantes` — Datacenters distants, télétravail généralisé, secours électrique (HQ)
**Origine :** Norme ISO 22301 / Management des risques d'entreprise.
**Subtilités/confusions :**
- Le **PCA** englobe l'ensemble de l'**entreprise** (métiers, locaux, RH, informatique) ; le **PRA** est le volet spécifiquement **informatique** du PCA.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Organiser des simulations de crise réelles au moins une fois par an pour mettre à jour le PCA.
**Équivalents :** BCP (Business Continuity Plan)
**Voir aussi :** PRA, RPO, RTO, ISO27001
## `PRA` — Plan de Reprise d'Activité [ITSM/Infrastructure]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** DRP (Disaster Recovery Plan)
**Contextes :** reconstruire et remettre en service l'infrastructure informatique et les applications de l'entreprise suite à un sinistre grave (attaque de ransomware, destruction d'un datacenter)
**Rôle :** Volet technique et opérationnel du PCA décrivant la séquence exacte des étapes de restauration du système d'information.
**Syntaxe :** (Plan d'action technique d'urgence DSI)
**Cas réguliers :**
- `Site de Secours Chaud (Hot Site)` — Datacenter miroir synchrone prêt à reprendre la charge en quelques secondes
- `Basculement (Failover)` — Inversion des flux réseau vers le site de secours
- `Retour à la normale (Failback)` — Ré-inversion vers le site principal après réparation
**Origine :** Norme ISO 22301 / DRP.
**Subtilités/confusions :**
- Un bon PRA doit être documenté sur du **papier physique ou un support hors-ligne**, car en cas de sinistre majeur, le Wiki interne ou le serveur documentaire peut être inaccessible !
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne jamais valider un PRA qui n'a jamais été testé en conditions réelles (*Disaster Recovery Drill*).
**Précautions :** Réaliser des exercices de basculement réels chaque année.
**Équivalents :** DRP (Disaster Recovery Plan)
**Voir aussi :** PCA, RPO, RTO, Backup
## `EAI` — Enterprise Application Integration [Entreprise/Architecture]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** Intégration des Applications d'Entreprise
**Contextes :** interconnecter des applications métier hétérogènes existantes (ERP, CRM, gestion de paie) pour échanger des données sans modifier le code source interne de chaque outil
**Rôle :** Architecture logicielle et catégorie de middleware assurant le transfert de données, la transformation de formats et la synchronisation entre applications d'un même SI.
**Syntaxe :** (Middleware d'intégration : Tibco, webMethods, IBM App Connect)
**Cas réguliers :**
- `Hub-and-Spoke` — Architecture centralisée autour d'un serveur d'intégration central
- `Connecteurs Applicatifs` — Adaptateurs capables de lire/écrire nativement dans SAP, Salesforce ou des fichiers plats
**Origine :** Années 1990 / Précurseur direct des architectures ESB.
**Subtilités/confusions :**
- L'EAI historique était souvent orienté par lots (*batch*) ou fichiers ; les ESB et bus d'événements modernes travaillent en temps réel.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Favoriser les échanges basés sur des contrats d'API clairs et des formats pivot (JSON, XML).
**Équivalents :** ESB, ETL, iPaaS
**Voir aussi :** ESB, ERP, CRM, ETL
## `RPA` — Robotic Process Automation [Entreprise/Automation]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Automatisation Botanique / Robots Logiciels
**Contextes :** automatiser des tâches manuelles répétitives effectuées par des humains sur des interfaces graphiques d'anciens logiciels sans API (ex: copier-coller de données entre 3 écrans)
**Rôle :** Technologie d'automatisation basée sur des robots logiciels (*bots*) qui imitent les actions d'un utilisateur humain sur l'interface graphique (clics, saisie au clavier, lecture d'écran).
**Syntaxe :** (Plateformes RPA : UiPath, Automation Anywhere, Blue Prism, Power Automate)
**Cas réguliers :**
- `Attended Bot` — Robot d'assistance exécuté à la demande de l'utilisateur sur son poste de travail
- `Unattended Bot` — Robot autonome exécuté sur un serveur d'arrière-plan selon un calendrier
**Origine :** Émergence au début des années 2010 (UiPath, Blue Prism).
**Subtilités/confusions :**
- La RPA est une solution rapide d'automatisation de surface ("pansement") ; elle ne remplace pas une vraie intégration par API (ESB/EAI) plus pérenne.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Un changement d'interface graphique (UI) dans le logiciel ciblé peut casser le fonctionnement du robot RPA.
**Précautions :** Privilégier les API natives chaque fois qu'elles existent avant de recourir à la RPA.
**Équivalents :** Screen Scraping, Macro, BPM
**Voir aussi :** BPM, ESB, UI
## `PoC` — Proof of Concept [Management/Dev]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Preuve de Concept
**Contextes :** valider la faisabilité technique ou l'intérêt pratique d'une idée, d'une nouvelle technologie ou d'un outil avant d'investir du budget et du temps
**Rôle :** Réalisation expérimentale à petite échelle destinée à vérifier qu'un concept ou une hypothèse technique est réalisable dans la pratique.
**Syntaxe :** (Phase de projet / Prototype de faisabilité)
**Cas réguliers :**
- `PoC Technique` — Tester par exemple si une base de données NoSQL peut absorber 50 000 écritures/seconde sur un prototype réduit
- `Throwaway Code` — Le code d'un PoC est généralement écrit rapidement sans chercher la perfection d'architecture et a vocation à être réécrit proprement
**Origine :** Industrie d'ingénierie et recherche / adopté dans le logiciel.
**Subtilités/confusions :**
- Un **PoC** valide la **faisabilité technique** (Est-ce que ça marche ?) ; un **MVP** est une **première version fonctionnelle du produit** mise entre les mains de vrais utilisateurs.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne jamais déployer le code brut d'un PoC directement en production sans refactorisation préalable.
**Précautions :** Définir des critères de succès mesurables et précis avant de démarrer un PoC.
**Équivalents :** Prototype, Spike (Agile)
**Voir aussi :** MVP, Agile
## `MVP` — Minimum Viable Product [Management/Produit]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Produit Minimum Viable
**Contextes :** lancer rapidement la première version d'un produit logiciel contenant uniquement les fonctionnalités essentielles pour recueillir le retour d'utilisateurs réels
**Rôle :** Concept central de la méthodologie Lean Startup désignant la version la plus épurée d'un produit qui permet de valider des hypothèses métier avec un minimum d'effort.
**Syntaxe :** (Concept de développement produit Lean/Agile)
**Cas réguliers :**
- `Feedback Loop (Build-Measure-Learn)` — Livrer le MVP -> Mesurer l'usage -> Apprendre et ajuster la feuille de route
- `Focus Fonctionnel` — Ne développer QUE les fonctionnalités indispensables qui résolvent le problème principal de l'utilisateur
**Origine :** Frank Robinson (2001) / Popularisé par Eric Ries (*The Lean Startup*, 2011).
**Subtilités/confusions :**
- Le MVP doit être **VIABLE** : il ne s'agit pas d'un produit buggué ou incomplet, mais d'un produit simple, fonctionnel et utilisable apportant une vraie valeur.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Rister la tentation du "feature creep" (ajouter sans cesse des fonctionnalités avant le lancement).
**Équivalents :** MMP (Minimum Marketable Product), PoC
**Voir aussi :** PoC, Agile, Scrum
## `KPI` — Key Performance Indicator [Management]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** ICP (Indicateur Clé de Performance)
**Contextes :** mesurer l'efficacité, la performance et l'atteinte des objectifs stratégiques ou opérationnels d'une entreprise ou d'un projet IT
**Rôle :** Valeur mesurable utilisée pour évaluer le succès d'une organisation ou d'un projet par rapport à des objectifs définis.
**Syntaxe :** (Métriques de pilotage business et IT)
**Cas réguliers :**
- `KPI Business` — Taux de conversion, chiffre d'affaires mensuel (MRR), coût d'acquisition client (CAC)
- `KPI IT / DSI` — Temps moyen de rétablissement (MTTR), taux de disponibilité des applications, nombre de tickets ouverts
**Origine :** Sciences de gestion / Tableaux de bord de pilotage (années 1990).
**Subtilités/confusions :**
- Un bon KPI doit respecter le principe SMART (Spécifique, Mesurable, Atteignable, Réaliste, Temporellement défini).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Limiter le nombre de KPI sur un tableau de bord (5 à 10 max) pour ne pas noyer les décideurs dans la masse de données.
**Équivalents :** OKR, Métriques
**Voir aussi :** OKR, SLA, ROI
## `OKR` — Objectives and Key Results [Management]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Objectifs et Résultats Clés
**Contextes :** aligner l'ensemble des équipes (engineering, produit, marketing) autour d'objectifs ambitieux et mesurer leur progression grâce à des résultats clés chiffrés
**Rôle :** Méthodologie de cadrage des objectifs popularisée par Intel et Google : un **Objectif** qualitatif et 3 à 5 **Résultats Clés** quantitatifs et mesurables.
**Syntaxe :** *Objectif : Devenir le leader du stockage cloud.* -> *KR1 : Atteindre 99.99% d'uptime. KR2 : Réduire le temps de latence de 30%.*
**Cas réguliers :**
- `Stretch Goals` — Les OKR sont conçus pour être très ambitieux (atteindre 70% d'un OKR est généralement considéré comme un succès !)
- `Cadence Trimestrielle` — Révision et définition de nouveaux OKR tous les 3 mois
**Origine :** Andy Grove (Intel, 1970s) / Introduit chez Google par John Doerr (1999).
**Subtilités/confusions :**
- Les OKR ne doivent pas être directement liés aux évaluations individuelles de rémunération ou primes pour encourager la prise de risque et l'ambition.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Assurer la transparence complète des OKR dans toute l'entreprise.
**Équivalents :** KPI, MBO (Management by Objectives)
**Voir aussi :** KPI, Agile, Scrum
## `ROI` — Return on Investment [Finance/Management]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Retour sur Investissement
**Contextes :** évaluer la rentabilité financière d'un projet informatique (ex: migration cloud, achat d'un nouvel ERP, automatisation RPA)
**Rôle :** Ratio financier comparant les gains nets générés par un investissement par rapport aux coûts initiaux engagés.
**Syntaxe :** `ROI (%) = ((Gains de l'investissement - Coût de l'investissement) / Coût de l'investissement) * 100`
**Cas réguliers :**
- `ROI Positif` — L'investissement a rapporté plus d'argent ou d'économies qu'il n'en a coûté
- `Délai de Récupération (Payback Period)` — Temps nécessaire pour que les économies générées remboursent l'investissement initial
**Origine :** Donaldson Brown / DuPont (1914).
**Subtilités/confusions :**
- En informatique, le ROI intègre non seulement les nouveaux revenus, mais surtout les **économies d'échelle** et la **réduction des coûts d'exploitation (OpEx)**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Inclure l'intégralité du coût global de possession (**TCO**) dans le calcul du coût de l'investissement.
**Équivalents :** TCO, TRI (Taux de Rentabilité Interne)
**Voir aussi :** TCO, CIO, ERP
## `TCO` — Total Cost of Ownership [Finance/IT]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Coût Global de Possession
**Contextes :** calculer le coût réel et complet d'un équipement ou projet informatique sur tout son cycle de vie (achat, maintenance, formation, énergie, support, fin de vie)
**Rôle :** Analyse financière évaluant les coûts directs (achats, licences) et indirects (formation, pannes, consommation électrique, support) d'un actif informatique.
**Syntaxe :** `TCO = Coûts d'Acquisition (CapEx) + Coûts de Fonctionnement (OpEx) sur N ans`
**Cas réguliers :**
- `Comparatif On-Premise vs Cloud` — Comparer le TCO d'un serveur physique (achat + électricité + climatisation + admin) avec l'abonnement cloud mensuel
- `Coûts Cachés` — Intégrer les coûts de formation du personnel et la dette technique
**Origine :** Gartner Group (1987).
**Subtilités/confusions :**
- Se fier uniquement au prix d'achat initial (*CapEx*) est l'erreur classique : les coûts d'exploitation et de maintenance représentent souvent 70% à 80% du TCO total !
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Effectuer une analyse TCO sur une durée de 3 à 5 ans pour faire des choix d'infrastructure éclairés.
**Équivalents :** LCC (Life Cycle Costing), ROI
**Voir aussi :** ROI, CIO, Cloud, IaaS
## `CapEx` — Capital Expenditures [Finance/IT]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Dépenses d'Investissement
**Contextes :** désigner les dépenses financières d'investissement à long terme inscrites à l'actif du bilan (ex: achat de serveurs informatiques physiques, acquisition de locaux, achat de licences logicielles perpétuelles)
**Rôle :** Catégorie comptable représentant les investissements matériels ou immatériels amortis sur plusieurs années.
**Syntaxe :** (Modalité de gestion financière et comptable)
**Cas réguliers :**
- `Achat de Matériel` — Achat de baies de stockage ou serveurs en propre pour un datacenter privé
- `Amortissement` — Déduction fiscale étalée sur la durée de vie estimée de l'actif (ex: 3 à 5 ans)
**Origine :** Comptabilité financière et analytique d'entreprise.
**Subtilités/confusions :**
- L'ère du Cloud a marqué le passage massif d'un modèle **CapEx** (achat d'infrastructures) vers un modèle **OpEx** (location mensuelle à l'usage).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Évaluer l'impact sur la trésorerie immédiate avant d'engager des dépenses CapEx importantes.
**Équivalents :** OpEx, Investissement
**Voir aussi :** OpEx, TCO, ROI, CIO
## `OpEx` — Operational Expenditures [Finance/IT]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Dépenses d'Exploitation
**Contextes :** désigner les dépenses courantes et récurrentes de fonctionnement consommées immédiatement pour faire tourner l'entreprise au quotidien (factures Cloud, abonnements SaaS, salaires, maintenance)
**Rôle :** Catégorie comptable regroupant les charges d'exploitation déductibles directement du résultat de l'exercice comptable en cours.
**Syntaxe :** (Modalité de gestion financière et comptable)
**Cas réguliers :**
- `Facturation Cloud Pay-as-you-go` — Paiement à la consommation réelle des ressources AWS/GCP/Azure
- `Abonnements SaaS` — Licences mensuelles/annuelles par utilisateur (Microsoft 365, Salesforce)
**Origine :** Comptabilité financière et analytique d'entreprise.
**Subtilités/confusions :**
- Les dépenses OpEx offrent une grande souplesse car elles peuvent être ajustées rapidement à la hausse ou à la baisse selon la conjoncture.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Sans contrôle rigoureux des ressources cloud (FinOps), la facture OpEx mensuelle peut rapidement s'envoler de façon incontrôlée.
**Précautions :** Mettre en place des alertes de budget et des politiques FinOps strictes sur vos comptes cloud.
**Équivalents :** CapEx, Charge d'exploitation
**Voir aussi :** CapEx, FinOps, TCO, Cloud
## `FinOps` — Cloud Financial Management [Cloud/Finance]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Gestion Financière Cloud
**Contextes :** optimiser et maîtriser les coûts de consommation des infrastructures cloud (AWS, GCP, Azure) en impliquant conjointement les équipes Dev, Ops et Finance
**Rôle :** Discipline et pratique culturelle visant à maximiser la valeur métier du Cloud grâce à une responsabilisation financière et une optimisation continue des dépenses.
**Syntaxe :** (Pratique organisationnelle et outillage de coût cloud)
**Cas réguliers :**
- `Tagging des Ressources` — Taguer chaque ressource cloud par projet, environnement et équipe pour attribuer les coûts avec précision
- `Instances Réservées / Savings Plans` — S'engager sur 1 à 3 ans de consommation pour bénéficier de réductions de 30% à 70% sur les instances
- `Droits de Dimensionnement (Right-Sizing)` — Réduire la taille des VMs sous-utilisées
**Origine :** FinOps Foundation / J.R. Storment et Mike Fuller (2019).
**Subtilités/confusions :**
- Le FinOps ne vise pas à "dépenser le moins possible", mais à **optimiser le retour sur investissement de chaque dollar dépensé dans le cloud**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Activer la suppression automatique des volumes disques orphelins et des IP publiques non rattachées.
**Équivalents :** Cloud Cost Optimization
**Voir aussi :** OpEx, Cloud, AWS, Kubernetes
## `ChatOps` — Chat-Driven Operations [DevOps]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** exécuter des tâches d'exploitation et de déploiement (mise en prod, redémarrage de services, requêtes d'état) directement via des commandes saisies dans un salon de tchat d'équipe (Slack, Microsoft Teams)
**Rôle :** Pratique opérationnelle DevOps qui intègre des bots d'automatisation au sein des outils de messagerie d'équipe pour rendre les actions d'infrastructure visibles et collaboratives.
**Syntaxe :** `bot deploy app-v2 to production` (dans Slack/Teams)
**Cas réguliers :**
- `Transparence d'Équipe` — Toute l'équipe voit qui a déclenché un déploiement et quel en a été le résultat
- `Hubot / Lita / Errbot` — Moteurs de bots d'automatisation connectés aux APIs de CI/CD et d'infrastructure
**Origine :** Jesse Newland / GitHub (2013).
**Subtilités/confusions :**
- Transforme le canal de discussion d'équipe en véritable console de contrôle en direct de l'infrastructure.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Restreindre strictement les permissions d'exécution des commandes sensibles du bot (authentification forte obligatoire).
**Précautions :** Ne pas permettre l'exécution de commandes système destructrices sans confirmation explicite d'un second administrateur.
**Équivalents :** GitOps, CLI Automation
**Voir aussi :** DevOps, Slack, GitHub, Pipeline
## `Shift Left` — Déplacement précoce des tests et de la sécurité [DevOps/Qualité]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Tester au plus tôt
**Contextes :** intégrer les tests de qualité, de performance et de sécurité dès les premières étapes du développement logiciel plutôt que juste avant la livraison
**Rôle :** Principe fondamental des démarches Agile et DevOps préconisant d'effectuer les validations au plus tôt dans le cycle de vie applicatif pour corriger les bugs à moindre coût.
**Syntaxe :** (Principe d'ingénierie et d'architecture de test)
**Cas réguliers :**
- `Shift Left Security` — Exécuter des linter SAST et des scans de dépendances directement sur le poste du développeur et lors de chaque commit
- `Réduction des Coûts` — Un bug détecté pendant le développement coûte 10 à 100 fois moins cher à corriger qu'un bug découvert en production !
**Origine :** Larry Smith (2001).
**Subtilités/confusions :**
- L'expression fait référence à la représentation chronologique du cycle de projet (de gauche à droite) : "déplacer vers la gauche" signifie agir plus tôt.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Équiper les IDE des développeurs avec des plugins de vérification automatique en temps réel.
**Équivalents :** TDD, Continuous Testing
**Voir aussi :** SAST, DevSecOps, TDD, CI
## `Agile` — Méthodologie itérative de gestion de projet [Management/Dev]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Agile Software Development
**Contextes :** piloter des projets logiciels en cycles courts (itérations) en favorisant la collaboration, l'adaptation au changement et la livraison fréquente de valeur aux utilisateurs
**Rôle :** Approche de gestion de projet basée sur les 4 valeurs et 12 principes du *Manifeste Agile*, s'opposant aux modèles rigides en cascade (V/Waterfall).
**Syntaxe :** (Philosophie et cadre de gestion de projet)
**Cas réguliers :**
- `4 Valeurs fondamentales` — Les individus et leurs interactions > les processus ; des logiciels opérationnels > une documentation exhaustive ; la collaboration > la négociation ; l'adaptation > le suivi d'un plan
- `Livraison Incrémentale` — Fournir des versions fonctionnelles toutes les 2 à 4 semaines
**Origine :** 17 signataires (Kent Beck, Martin Fowler, Jeff Sutherland...) Snowbird, Utah (2001).
**Subtilités/confusions :**
- L'Agilité est une **philosophie/état d'esprit**, alors que **Scrum** et **Kanban** sont des **frameworks concrets** qui mettent en œuvre cette philosophie.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Éviter l'Agile de façade ("Dark Agile") qui applique la cérémonie sans adopter la culture de confiance et d'autonomie.
**Précautions :** Accepter que le périmètre fonctionnel puisse évoluer en fonction des retours d'usage réels.
**Équivalents :** Scrum, Kanban, XP (Extreme Programming)
**Voir aussi :** Scrum, Kanban, SAFe, MVP
## `Scrum` — Framework de gestion de projet Agile par Sprints [Management/Dev]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Cadre Scrum
**Contextes :** organiser le travail d'une équipe de développement autonome (3 à 9 personnes) en itérations de durée fixe (*Sprints*) avec des rôles et cérémonies définis
**Rôle :** Framework léger d'organisation Agile le plus populaire au monde pour résoudre des problèmes complexes tout en livrant des produits de haute valeur.
**Syntaxe :** (Framework méthodologique et cérémonies d'équipe)
**Cas réguliers :**
- `3 Rôles` — Product Owner (vision produit), Scrum Master (coach/facilitateur), Équipe de Développeurs (exécution)
- `4 Cérémonies` — Sprint Planning, Daily Scrum (15 min debout), Sprint Review (démonstration), Sprint Retrospective (amélioration continue)
- `Sprint` — Période de temps fixe (*Timebox*) de 1 à 4 semaines
**Origine :** Hirotaka Takeuchi et Ikujiro Nonaka (1986) / Ken Schwaber et Jeff Sutherland (1995).
**Subtilités/confusions :**
- Le Scrum Master n'est pas un chef de projet traditionnel : c'est un "Leader au service de l'équipe" (*Servant Leader*) qui lève les obstacles.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Ne pas modifier l'objectif du Sprint (*Sprint Goal*) en cours de route sauf urgence majeure.
**Équivalents :** Kanban, Extreme Programming (XP)
**Voir aussi :** Agile, Kanban, SAFe, MVP
## `Kanban` — Système visuel de gestion du flux de travail [Management/Dev]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Méthode Kanban
**Contextes :** visualiser l'avancement des tâches, limiter le travail en cours (*WIP*) et optimiser le flux d'exécution continu d'une équipe (support, maintenance, dev)
**Rôle :** Méthode de gestion visuelle du travail issue du système de production Toyota, matérialisée par un tableau à colonnes (À faire, En cours, Validé, Terminé).
**Syntaxe :** (Outils visuels : Jira Board, Trello, GitHub Projects)
**Cas réguliers :**
- `Limitation du WIP (Work in Progress)` — Fixer un nombre maximal de tâches autorisées simultanément dans une colonne (ex: max 3 tâches "En cours") pour éviter le surmenage et identifier les goulets d'étranglement
- `Système à Flux Tiré (Pull System)` — On ne "pousse" pas du travail à l'équipe : une nouvelle tâche n'est démarrée que lorsqu'une place se libère
**Origine :** Taiichi Ohno / Toyota (1940s) / Adapté au logiciel par David J. Anderson (2007).
**Subtilités/confusions :**
- Contrairement à Scrum qui fonctionne par Sprints de durée fixe, Kanban est un **flux continu** sans itérations imposées.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Mesurer le temps de traversée (*Lead Time*) et le temps de traitement (*Cycle Time*) pour améliorer la fluidité du flux.
**Équivalents :** Scrum, Scrumban
**Voir aussi :** Scrum, Agile, TODO_TRACKER
## `SAFe` — Scaled Agile Framework [Management/Entreprise]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Agilité à l'Échelle
**Contextes :** synchroniser et aligner le travail de dizaines ou centaines d'équipes de développement (plus de 50 à 1000 personnes) au niveau d'une grande entreprise ou DSI
**Rôle :** Cadre méthodologique d'entreprise fournissant des guides, rôles et processus pour déployer l'Agilité, Scrum et Lean à très grande échelle.
**Syntaxe :** (Framework d'organisation d'entreprise à grande échelle)
**Cas réguliers :**
- `ART (Agile Release Train)` — Équipe d'équipes (50 à 125 personnes) synchronisées sur le même rythme de livraison
- `PI Planning (Program Increment Planning)` — Événement de planification géant de 2 jours où toutes les équipes préparent le trimestre à venir
**Origine :** Dean Leffingwell (2011).
**Subtilités/confusions :**
- Souvent critiqué pour sa lourdeur et sa bureaucratie perçue par rapport à l'Agilité pure, mais apprécié des grands groupes pour sa capacité de cadrage.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Ne déployer SAFe que lorsque la taille de l'organisation et la complexité des dépendances entre équipes le réclament impérativement.
**Équivalents :** LeSS (Large-Scale Scrum), Spotify Model, Nexus
**Voir aussi :** Agile, Scrum, Kanban
## `Lean` — Philosophie d'élimination du gaspillage et valeur [Management/Dev]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Lean Software Development
**Contextes :** maximiser la valeur délivrée au client tout en éliminant systématiquement toutes les formes de gaspillage (*Waste / Muda*) dans le processus de développement
**Rôle :** Philosophie de gestion issue du système de production Toyota adaptée au développement logiciel par Mary et Tom Poppendieck.
**Syntaxe :** (7 Principes : Éliminer les gaspillages, Amplifier l'apprentissage, Décider le plus tard possible, Livrer le plus vite possible, Doter l'équipe de pouvoirs, Intégrer la qualité dès l'origine, Optimiser le tout)
**Cas réguliers :**
- `Élimination du Gaspillage (Muda)` — Supprimer le code inutile, la bureaucratie excessive, les attentes, le multitâche excessif et les défauts
- `Kaizen` — Philosophie d'amélioration continue permanente par petits pas
**Origine :** Taiichi Ohno et Shigeo Shingo (Toyota, 1950s) / Mary et Tom Poppendieck (2003).
**Subtilités/confusions :**
- Le Lean est la fondation théorique directe de l'Agilité, du DevOps et du mouvement Lean Startup.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Cartographier la chaîne de valeur (*Value Stream Mapping*) pour repérer où les tâches perdent du temps.
**Équivalents :** Kaizen, Six Sigma, Agile
**Voir aussi :** Agile, Kanban, MVP
## `Trunk-Based Development` — Développement axé sur le trunk principal [DevOps/Git]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** TBD
**Contextes :** éviter l'enfer des fusions de branches Git (*Merge Hell*) et permettre l'intégration continue réelle en faisant intégrer très fréquemment le code de tous les développeurs sur la branche principale (`main`/`master`)
**Rôle :** Pratique de gestion de code source où tous les développeurs fusionnent leurs modifications très régulièrement (plusieurs fois par jour) sur une branche principale unique.
**Syntaxe :** (Stratégie de branching Git)
**Cas réguliers :**
- `Branches Courtes` — Les branches de fonctionnalités (*Feature branches*) durent moins de 24h avant d'être merged
- `Feature Flags` — Masquer les fonctionnalités incomplètes dans le code en prod sans bloquer la fusion sur la branche principale
**Origine :** Pratique pionnière d'Extreme Programming (XP) et Google/Meta / Formalisé par Paul Hammant (2013).
**Subtilités/confusions :**
- S'oppose au modèle **GitFlow** (qui conserve de longues branches isolées pendant des semaines).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Exige une suite de tests automatisés (CI) extrêmement rapide et fiable pour éviter de casser la branche principale.
**Précautions :** Utiliser conjointement des Feature Flags pour désactiver les fonctionnalités non prêtes en production.
**Équivalents :** Continuous Integration, GitFlow (alternative)
**Voir aussi :** Git, CI, Feature Flag
## `Refactoring` — Reconfiguration interne du code sans altérer son comportement [Développement]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Réusinage de code
**Contextes :** nettoyer, restructurer et simplifier un code source existant pour améliorer sa lisibilité et sa maintenabilité sans modifier son comportement fonctionnel externe
**Rôle :** Discipline d'ingénierie logicielle consistant à modifier la structure interne d'un programme pour réduire la dette technique.
**Syntaxe :** (Pratique de développement et nettoyage de code)
**Cas réguliers :**
- `Extraction de Méthode` — Isoler un bloc de code complexe dans une fonction autonome bien nommée
- `Rename / Move` — Renommer des variables ou déplacer des classes pour rendre le code auto-documenté
**Origine :** William Opdyke (1990) / Martin Fowler (*Refactoring: Improving the Design of Existing Code*, 1999).
**Subtilités/confusions :**
- Le refactoring ne doit **JAMAIS** ajouter de nouvelles fonctionnalités ni corriger de bugs fonctionnels en même temps : son unique but est l'amélioration de la qualité du code.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne JAMAIS entreprendre un refactoring d'envergure sans disposer au préalable d'une suite complète de tests unitaires automatisés pour vérifier l'absence de régression.
**Précautions :** Appliquer la règle du boy-scout : « Toujours laisser le code dans un état plus propre que celui dans lequel vous l'avez trouvé ».
**Équivalents :** Code Cleanup, Modernisation de code
**Voir aussi :** Technical Debt, TDD, Clean Code
## `Design System` — Système de design et composants UI réutilisables [UI/UX]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Système de Conception
**Contextes :** maintenir la cohérence visuelle et l'ergonomie sur l'ensemble des produits numériques d'une entreprise (web, mobile, desktop) en partageant des composants et des règles de style uniques
**Rôle :** Référentiel centralisé combinant une bibliothèque de composants UI codés, des principes de design, des règles d'accessibilité et une identité visuelle.
**Syntaxe :** (Bibliothèques : Material UI, Tailwind UI, Carbon Design System, Shadcn UI)
**Cas réguliers :**
- `Design Tokens` — Variables atomiques décrivant les couleurs, typographies, espaces et ombres (`color-primary`, `spacing-md`)
- `Bibliothèque de Composants` — Boutons, Modales, Inputs pré-codés et testés pour l'accessibilité
**Origine :** Brad Frost (*Atomic Design*, 2013) / Salesforce Lightning Design System (2015).
**Subtilités/confusions :**
- Un Design System n'est pas un simple fichier Figma ou un kit UI : c'est un produit vivant partagé et maintenu conjointement par les designers et les développeurs.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Documenter les composants avec des bacs à sable interactifs comme **Storybook**.
**Équivalents :** Style Guide, UI Kit, Component Library
**Voir aussi :** UI, UX, A11Y, CSS
## `Micro-frontend` — Découpage modulaire de l'architecture frontend [Web/Architecture]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** Micro-frontends
**Contextes :** découper une grande application web complexe (ex: site e-commerce) en plusieurs micro-applications autonomes développées et déployées indépendamment par des équipes distinctes
**Rôle :** Modèle d'architecture applicative transposant le concept des microservices à l'interface utilisateur web.
**Syntaxe :** (Technologies : Module Federation / Webpack 5, Single-SPA, iFrames, Web Components)
**Cas réguliers :**
- `Module Federation` — Fonctionnalité de Webpack 5 permettant de charger à la volée des composants JS distants sans les inclure au build principal
- `Équipes Autonomes` — L'équipe "Panier" gère son micro-frontend indépendamment de l'équipe "Catalogue produits"
**Origine :** ThoughtWorks Technology Radar (2016) / Cam Jackson.
**Subtilités/confusions :**
- Introduit de la complexité (surcoût de téléchargement JS, gestion de l'isolation CSS et du state global) : à réserver aux très grands projets d'entreprise.
- Un suivi des métriques en production permet de prévenir la saturation des ressources.
**Urgences/dangers :** ⚠️ Éviter de charger plusieurs versions de React/Vue en même temps sur la même page pour préserver les performances.
**Précautions :** Harmoniser les styles visuels via un **Design System** partagé.
**Équivalents :** Web Components, Microservices
**Voir aussi :** Microservices, SPA, Webpack, Design System
## `Headless` — Architecture découplée sans interface intégrée [Web/Architecture]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Architecture Headless / Headless CMS
**Contextes :** séparer la gestion du contenu ou de la logique métier (back-end) de sa restitution visuelle (front-end) pour pouvoir alimenter simultanément un site web, une app mobile et des objets connectés
**Rôle :** Paradigme d'architecture logicielle dans lequel le système arrière (*back-end*) fournit uniquement des APIs (REST/GraphQL) et n'a aucune connaissance de l'interface graphique utilisateur (*head*).
**Syntaxe :** (CMS Headless : Strapi, Contentful, Sanity, Commerce Layer)
**Cas réguliers :**
- `Headless CMS` — Système de gestion de contenu qui saisit les articles et les expose via API JSON sans générer de HTML
- `Headless Commerce` — Moteur e-commerce (Shopify Headless, Commerce Layer) gérant uniquement le panier et le paiement via des endpoints d'API
**Origine :** Émergence du Web découplé et de la montée en puissance des SPA/Jamstack (années 2010).
**Subtilités/confusions :**
- Offre une liberté totale aux développeurs frontend d'utiliser n'importe quel framework (Next.js, Astro, Flutter) sans être bridés par le système de templates du CMS.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Mettre en place un cache CDN d'API performant pour supporter les requêtes de rendu.
**Équivalents :** Decoupled Architecture, API-first
**Voir aussi :** CMS, REST, GraphQL, SSG
## `Jamstack` — JavaScript, APIs, and Markup [Web/Architecture]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** JAMstack
**Contextes :** concevoir des sites web ultra-rapides, sécurisés et économiques en dissociant la génération du HTML (Markup pré-généré) et la dynamique (JavaScript et APIs)
**Rôle :** Architecture web moderne basée sur le pré-rendu statique, l'utilisation d'APIs réutilisables et le déploiement direct sur des réseaux CDN mondiaux.
**Syntaxe :** (Architecture : Static Site Generator + Headless CMS + CDN)
**Cas réguliers :**
- `JavaScript` — Gère les comportements dynamiques et l'interactivité côté client dans le navigateur
- `APIs` — Toutes les fonctionnalités back-end (base de données, recherche, paiement) sont déléguées à des services d'API tiers ou Serverless
- `Markup` — Le HTML de chaque page est pré-généré lors du build (SSG) et servi instantanément via un CDN
**Origine :** Mathias Biilmann / Netlify (2015).
**Subtilités/confusions :**
- Supprime le besoin d'un serveur web traditionnel (Apache/Nginx/Node) exécutant du code à chaque requête de page.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser des fonctions Serverless (Edge Functions) pour traiter les comportements dynamiques personnalisés.
**Équivalents :** Headless, SSG, Serverless
**Voir aussi :** SSG, Headless, CDN, Next.js
## `Edge Computing` — Calcul informatique en périphérie de réseau [Cloud/Infrastructure]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** Traitement en Périphérie
**Contextes :** exécuter du code applicatif ou des traitements d'IA au plus près de l'utilisateur final ou des capteurs IoT (sur les nœuds CDN ou les passerelles locales) pour annuler la latence
**Rôle :** Architecture informatique distribuée qui déporte le traitement des données et l'exécution du code de l'ordinateur central (Cloud) vers les nœuds de bordure de réseau (*Edge*).
**Syntaxe :** (Services : Cloudflare Workers, Vercel Edge Functions, AWS Greengrass)
**Cas réguliers :**
- `Edge Functions` — Petites fonctions Serverless s'exécutant dans le PoP (Point of Presence) CDN le plus proche de l'utilisateur (< 10 ms)
- `IoT Edge` — Traitement des données de capteurs industriels sur une passerelle locale sans envoyer tout le flux vidéo brut dans le Cloud
**Origine :** Akamai (fin des années 1990) / Généralisé par la 5G et les Edge Workers (2018).
**Subtilités/confusions :**
- Réduit la latence de manière spectaculaire et préserve la bande passante globale vers le Cloud central.
- Un suivi des métriques en production permet de prévenir la saturation des ressources.
**Urgences/dangers :** —
**Précautions :** Prendre en compte les contraintes de mémoire et de temps d'exécution généralement plus restreintes sur les environnements Edge.
**Équivalents :** Fog Computing, On-Premise
**Voir aussi :** CDN, Serverless, Cloud, IoT
## `Cloud Native` — Applications conçues pour l'environnement Cloud [DevOps/Cloud]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Architecture Cloud Native
**Contextes :** concevoir et exécuter des applications capables d'exploiter pleinement la flexibilité, le passage à l'échelle automatique et la résilience des clouds modernes
**Rôle :** Approche de conception logicielle basée sur les conteneurs (Docker), l'orchestration (Kubernetes), les microservices, les API déclaratives et le DevOps (CNCF).
**Syntaxe :** (Philosophie et écosystème de technologies CNCF)
**Cas réguliers :**
- `CNCF (Cloud Native Computing Foundation)` — Organisation hébergeant les projets open source majeurs (Kubernetes, Prometheus, Envoy, Helm)
- `Résilience & Auto-scaling` — Applications capables de résister aux pannes de serveurs et de s'adapter automatiquement aux pics de charge
**Origine :** CNCF (Cloud Native Computing Foundation, 2015).
**Subtilités/confusions :**
- Une application "Cloud Native" est conçue dès l'origine pour le cloud ; une application "Lift and Shift" est un vieux système déplacé sur une VM cloud sans réarchitecture.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Respecter les principes de la *Twelve-Factor App* pour garantir la portabilité entre fournisseurs cloud.
**Équivalents :** Microservices, Serverless
**Voir aussi :** Kubernetes, Docker, Microservices, DevOps
## `Twelve-Factor App` — 12 principes pour les applications SaaS [DevOps/Architecture]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Les 12 Facteurs
**Contextes :** concevoir des applications web/SaaS modernes, portables, automatisables et faciles à déployer dans des conteneurs ou sur des plateformes cloud (PaaS/IaaS)
**Rôle :** Méthodologie et manifeste de 12 bonnes pratiques d'ingénierie rédigé par les ingénieurs de Heroku pour la création d'applications applicatives résilientes.
**Syntaxe :** (12 Principes d'architecture logicielle)
**Cas réguliers :**
- `I. Codebase` — Une seule base de code suivie sous contrôle de version, déployée sur plusieurs environnements
- `III. Config` — Stocker la configuration exclusivement dans les **variables d'environnement** (jamais dans le code !)
- `VI. Processes` — Exécuter l'application sous forme de processus **sans état (stateless)** et sans partage de mémoire
- `XI. Logs` — Traiter les logs comme des **flux d'événements** envoyés sur `stdout`
**Origine :** Adam Wiggins / Heroku (2011).
**Subtilités/confusions :**
- Standard incontournable pour la conteneurisation Docker et le déploiement sur Kubernetes.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Vérifier que votre application respecte l'isolation des dépendances (Facteur II) et la parité dev/prod (Facteur X).
**Équivalents :** Cloud Native Architecture
**Voir aussi :** Cloud Native, Docker, Kubernetes, env
## `DRY` — Don't Repeat Yourself [Développement]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Ne vous répétez pas
**Contextes :** concevoir du code propre et maintenable en évitant la duplication de logique métier ou de structures de données à plusieurs endroits du projet
**Rôle :** Principe de conception logicielle stipulant que chaque pièce de connaissance ou de logique doit avoir une représentation unique, non ambiguë et autoritaire dans le système.
**Syntaxe :** (Principe de refactoring et d'architecture)
**Cas réguliers :**
- `Factorisation` — Extraire un bloc de code dupliqué dans 3 fonctions vers une fonction utilitaire unique
- `Source de Vérité Unique` — Définir un schéma de données à un seul endroit et générer les types dépendants
**Origine :** Andy Hunt et Dave Thomas (*The Pragmatic Programmer*, 1999).
**Subtilités/confusions :**
- S'oppose au code **WET** (*Write Everything Twice* / *We Enjoy Typing*).
- Attention au "sur-DRY" : dupliquer 3 lignes de code simples vaut mieux que créer une mauvaise abstraction prématurée trop complexe !
**Urgences/dangers :** —
**Précautions :** Appliquer le principe DRY avec discernement : la duplication est préférable à la mauvaise abstraction.
**Équivalents :** Single Source of Truth
**Voir aussi :** KISS, YAGNI, Refactoring
## `KISS` — Keep It Simple, Stupid [Développement/Architecture]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Garde ça simple
**Contextes :** privilégier la simplicité de conception et de code par rapport à des architectures inutilement complexes et sur-dimensionnées
**Rôle :** Principe de conception préconisant que la plupart des systèmes fonctionnent mieux s'ils restent simples plutôt que rendus compliqués.
**Syntaxe :** (Principe de philosophie d'ingénierie)
**Cas réguliers :**
- `Éviter la Sur-Ingénierie (Over-engineering)` — Ne pas créer une architecture microservices distribuée à 10 serveurs pour un projet qui nécessite juste un simple script Python et une base SQLite
- `Lisibilité du Code` — Écrire du code simple et lisible par n'importe quel développeur junior plutôt qu'un code "intelligent" et obscur
**Origine :** Kelly Johnson / Skunk Works Lockheed (1960).
**Subtilités/confusions :**
- « La simplicité est la sophistication ultime » (Léonard de Vinci). Écrire un code simple est souvent beaucoup plus difficile que d'écrire un code complexe.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Préférer toujours la solution la plus simple qui résout correctement le problème actuel.
**Équivalents :** Simplicité, Occam's Razor
**Voir aussi :** DRY, YAGNI, Clean Code
## `YAGNI` — You Aren't Gonna Need It [Développement/Agile]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Vous n'en aurez pas besoin
**Contextes :** éviter de coder des fonctionnalités ou des abstractions prématurées "au cas où on en aurait besoin plus tard"
**Rôle :** Principe de la méthodologie Extreme Programming (XP) stipulant qu'un développeur ne doit pas ajouter une fonctionnalité tant qu'elle n'est pas immédiatement nécessaire.
**Syntaxe :** (Principe de développement logiciel Agile)
**Cas réguliers :**
- `Anti-Anticipation Excessive` — Ne pas coder de moteur de plugins complexe si l'application n'a qu'un seul cas d'usage aujourd'hui
- `Gain de Temps` — Économiser du temps de développement, de test et de maintenance sur des fonctions imaginaires qui ne seront finalement jamais utilisées
**Origine :** Kent Beck / Extreme Programming (XP, 1990s).
**Subtilités/confusions :**
- Complète les principes DRY et KISS en éliminant le code mort ou spéculatif.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Concevoir le code pour qu'il soit **facile à faire évoluer plus tard**, sans pour autant coder la fonctionnalité future aujourd'hui.
**Équivalents :** Minimalisme, Continuous Refactoring
**Voir aussi :** DRY, KISS, Agile, Refactoring
## `SOLID` — 5 principes de conception orientée objet [Développement/Architecture]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** Principes SOLID
**Contextes :** concevoir du code orienté objet maintenable, évolutif, testable et réutilisable dans la durée
**Rôle :** Acronyme regroupant 5 principes fondamentaux de conception logicielle définis par Robert C. Martin ("Uncle Bob").
**Syntaxe :** (5 Principes de conception objet)
**Cas réguliers :**
- `S - Single Responsibility` — Une classe ne doit avoir qu'une seule et unique responsabilité (une seule raison de changer)
- `O - Open/Closed` — Une entité doit être ouverte à l'extension, mais fermée à la modification
- `L - Liskov Substitution` — Une sous-classe doit pouvoir remplacer sa classe mère sans altérer le comportement du programme
- `I - Interface Segregation` — Préférer plusieurs interfaces spécifiques légères à une interface générale lourde
- `D - Dependency Inversion` — Dépendre des abstractions (interfaces), non des implémentations concrètes
**Origine :** Robert C. Martin « Uncle Bob » (2000 / acronyme par Michael Feathers).
**Subtilités/confusions :**
- Les principes SOLID constituent la base de la conception Clean Architecture et des Design Patterns.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser l'injection de dépendances pour mettre en œuvre facilement le principe D (Dependency Inversion).
**Équivalents :** Clean Architecture, GRASP
**Voir aussi :** Clean Code, Design Pattern, DRY
## `Clean Code` — Code lisible, maintenable et élégant [Développement]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Code Propre
**Contextes :** écrire un code informatique d'une clarté exemplaire, facile à lire, à comprendre et à faire évoluer par n'importe quel autre développeur
**Rôle :** Ensemble de pratiques d'ingénierie et d'artisanat logiciel (*Software Craftsmanship*) privilégiant la lisibilité et l'élégance du code source.
**Syntaxe :** (Philosophie et règles de style de programmation)
**Cas réguliers :**
- `Noms Révélateurs d'Intention` — Nommer les variables et fonctions de façon explicite (ex: `elapsedTimeInDays` plutôt que `d`)
- `Fonctions Courtes` — Une fonction doit être courte et ne faire qu'une seule chose
- `Commentaires Utiles` — Le bon code s'auto-documente ; les commentaires doivent expliquer le **POURQUOI**, pas le **COMMENT**
**Origine :** Robert C. Martin « Uncle Bob » (*Clean Code: A Handbook of Agile Software Craftsmanship*, 2008).
**Subtilités/confusions :**
- Le ratio temps passé à **lire** du code par rapport au temps passé à en **écrire** est supérieur à 10 pour 1 : rendre le code facile à lire fait gagner un temps précieux à l'équipe.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser des linters et des formateurs automatiques (Prettier, Ruff, ESLint) pour automatiser la conformité de style.
**Équivalents :** Software Craftsmanship, Readable Code
**Voir aussi :** SOLID, DRY, KISS, Refactoring
## `Design Pattern` — Patron de conception logicielle [Développement/Architecture]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** Patrons de Conception
**Contextes :** résoudre des problèmes récurrents d'architecture logicielle en utilisant des solutions éprouvées et un vocabulaire commun partagé entre développeurs
**Rôle :** Solution standardisée et réutilisable à un problème de conception applicative récurrent dans un contexte donné.
**Syntaxe :** (Catégories : Création, Structure, Comportement)
**Cas réguliers :**
- `Singleton` — Garantir qu'une classe n'a qu'une seule instance globale (ex: gestionnaire de connexion BDD)
- `Factory (Fabrique)` — Créer des objets sans spécifier la classe exacte de l'objet à créer
- `Observer (Observateur)` — Définir une relation un-à-plusieurs pour notifier automatiquement des objets lors d'un changement d'état (événement)
**Origine :** Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four" / GoF, 1994).
**Subtilités/confusions :**
- Les Design Patterns ne sont pas des morceaux de code à copier-coller, mais des **schémas conceptuels** à adapter à votre langage et contexte.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne pas appliquer de Design Patterns de manière forcie là où une simple fonction suffit.
**Précautions :** Apprendre les patrons de conception pour enrichir son vocabulaire d'architecture.
**Équivalents :** Architectural Pattern
**Voir aussi :** SOLID, MVC, Clean Code
## `MVC` — Model-View-Controller [Développement/Architecture]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Modèle-Vue-Contrôleur
**Contextes :** séparer la logique de données (Model), l'interface utilisateur (View) et la logique de contrôle (Controller) dans les applications web ou desktop
**Rôle :** Patron d'architecture logicielle fondamental découpant une application en trois composants interconnectés.
**Syntaxe :** (Frameworks MVC : Django, Ruby on Rails, Laravel, Spring MVC, ASP.NET Core)
**Cas réguliers :**
- `Modèle (Model)` — Gère les données, les règles métier et les interactions avec la base de données
- `Vue (View)` — Affiche l'interface graphique et le HTML à l'utilisateur
- `Contrôleur (Controller)` — Intercepte les requêtes utilisateur, interroge le Modèle et sélectionne la Vue à afficher
**Origine :** Trygve Reenskaug (Xerox PARC, 1979 / Smalltalk-80).
**Subtilités/confusions :**
- Modèle d'architecture historique qui a structuré le développement web des années 2000 (Rails, Django, Laravel).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Éviter les "Fat Controllers" en déportant la logique métier dans des services dédiés (*Service Layer*).
**Équivalents :** MVVM, MVP (Model-View-Presenter)
**Voir aussi :** MVVM, Design Pattern, DOM
## `MVVM` — Model-View-ViewModel [Développement/UI]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Modèle-Vue-VueModèle
**Contextes :** lier automatiquement l'interface utilisateur (Vue) aux données métier (Modèle) via du Data-Binding bidirectionnel dans les applications réactives (Vue.js, Flutter, WPF, Angular)
**Rôle :** Patron d'architecture d'interface utilisateur facilitant la séparation entre le développement de l'interface graphique et la logique métier grâce au Data-Binding.
**Syntaxe :** (Frameworks : Vue.js, Angular, WPF, SwiftUI, Knockout.js)
**Cas réguliers :**
- `ViewModel` — Convertit les données du Modèle en état réactif directement consommable par la Vue et intercepte les événements utilisateur
- `Data Binding` — Toute modification de l'état dans le ViewModel met à jour instantanément la Vue à l'écran sans manipulation manuelle du DOM !
**Origine :** Ken Cooper et Ted Peters / Microsoft (2005 / conçu pour WPF).
**Subtilités/confusions :**
- Élimine le besoin d'écrire du code de manipulation manuelle du DOM (comme en jQuery) au profit d'un état réactif déclaratif.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Conserver le ViewModel indépendant de tout code spécifique à la plateforme UI pour faciliter les tests unitaires.
**Équivalents :** MVC, MVP (Model-View-Presenter)
**Voir aussi :** MVC, DOM, SPA, Flutter
## `DDD` — Domain-Driven Design [Développement/Architecture]
**Niveau :** avance | **Popularité :** 93 | **Aliases :** Conception Pilotée par le Domaine
**Contextes :** concevoir des logiciels métiers complexes (banque, logistique, assurance) en modélisant le code au plus près du langage et des réalités des experts métier
**Rôle :** Approche de conception logicielle centrée sur la modélisation du domaine métier et l'utilisation d'un langage omniprésent (*Ubiquitous Language*) partagé entre dévs et experts métier.
**Syntaxe :** (Concepts : Bounded Context, Aggregate, Entity, Value Object, Repository)
**Cas réguliers :**
- `Ubiquitous Language` — Vocabulaire strict et unique utilisé dans les réunions, la documentation ET dans le nom des classes du code source !
- `Bounded Context (Contexte Délimité)` — Frontière explicite dans laquelle un modèle de données particulier s'applique (ex: la notion de "Client" n'a pas la même définition dans le contexte "Ventes" et dans le contexte "Support")
**Origine :** Eric Evans (*Domain-Driven Design: Tackling Complexity in the Heart of Software*, 2003).
**Subtilités/confusions :**
- Le DDD est la base d'architecture idéale pour découper un monolithe en **microservices** pertinents aux bonnes frontières métier.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne pas appliquer le DDD sur des projets CRUD simples (sur-ingénierie inutile).
**Précautions :** Organiser des ateliers d'**Event Storming** avec les experts métier pour faire émerger les contextes délimités.
**Équivalents :** Clean Architecture, Hexagonal Architecture
**Voir aussi :** CQRS, Event Sourcing, Microservices, SOLID
## `CQRS` — Command Query Responsibility Segregation [Développement/Architecture]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** Séparation Commandes / Requêtes
**Contextes :** optimiser séparément les opérations de lecture (très fréquentes) et les opérations d'écriture/modification (complexes) dans des systèmes à très haute charge
**Rôle :** Patron d'architecture logicielle séparant physiquement ou logiquement les opérations qui modifient l'état (*Commands*) des opérations qui lisent l'état (*Queries*).
**Syntaxe :** (Modèle d'architecture distribuée)
**Cas réguliers :**
- `Côté Commandes (Write)` — Reçoit les actions (`CreateUser`, `UpdateOrder`), valide les règles métier et enregistre les événements
- `Côté Requêtes (Read)` — Interroge une base de données de lecture dénormalisée ultra-rapide (ex: Elasticsearch/Redis)
**Origine :** Bertrand Meyer (principe CQS, 1988) / Greg Young (CQRS, 2010).
**Subtilités/confusions :**
- Entraîne une **cohérence éventuelle** (*Eventual Consistency*) : il peut y avoir un léger délai de quelques millisecondes avant que l'écriture ne soit répercutée sur la vue de lecture.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Combiner très souvent avec l'**Event Sourcing** pour alimenter les modèles de lecture à partir du journal d'événements.
**Équivalents :** CQS (Command Query Separation)
**Voir aussi :** Event Sourcing, DDD, Elasticsearch, Redis
## `Event Sourcing` — Persistence par journal d'événements [Développement/Data]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** Sourcing d'Événements
**Contextes :** conserver l'historique complet et inaltérable de tous les changements d'état d'un système (banque, comptabilité, suivi de colis, audit juridique)
**Rôle :** Patron de persistance où l'état d'une application n'est pas modifié sur place (*UPDATE*) mais reconstruit depuis une séquence immuable d'événements (*Event Log*).
**Syntaxe :** Ex: `[AccountOpened, MoneyDeposited(100), MoneyWithdrawn(30)]` -> Solde actuel calculé = 70
**Cas réguliers :**
- `Journal Immuable (Append-only Log)` — Les événements ne sont JAMAIS supprimés ni modifiés (`INSERT` uniquement)
- `Voyage dans le Temps (Time Travel)` — Capacité de reconstruire l'état exact du système à n'importe quel instant du passé en rejouant le journal jusqu'à cette date !
**Origine :** Martin Fowler (2005) / Greg Young.
**Subtilités/confusions :**
- S'oppose au modèle CRUD traditionnel qui écrase l'ancien état lors d'un `UPDATE` en faisant perdre l'historique de ce qui s'est passé.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser des instantanés (*Snapshots*) périodiques pour éviter d'avoir à rejouer des millions d'événements au démarrage.
**Équivalents :** Change Data Capture (CDC), Audit Log
**Voir aussi :** CQRS, Kafka, DDD
## `Monolith` — Architecture applicative monolithique [Architecture]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Monolithe Logiciel
**Contextes :** regrouper l'ensemble des modules d'une application (interface, logique métier, accès base) au sein d'une seule base de code déployée sous forme d'un exécutable unique
**Rôle :** Modèle d'architecture applicative traditionnel dans lequel tous les composants logiciels sont étroitement couplés et s'exécutent au sein d'un même processus.
**Syntaxe :** (Architecture applicative unifiée : application Django, Rails ou Spring Boot unique)
**Cas réguliers :**
- `Modular Monolith (Monolithe Modulaire)` — Monolithe structuré en modules internes strictement isolés (idéal avant toute séparation en microservices)
- `Simplicité de Déploiement` — Facilité de déploiement et de débogage (un seul binaire/archive à tester et déployer)
**Origine :** Modèle d'architecture logiciel d'origine.
**Subtilités/confusions :**
- Un monolithe n'est pas "mauvais" par nature : c'est l'architecture la plus efficace et la plus rapide à développer pour 90% des projets et des startups !
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Garder une séparation stricte des modules internes pour éviter que le monolithe ne se transforme en "Big Ball of Mud" (sac de nœuds inmaintenable).
**Équivalents :** Modular Monolith, Microservices (alternative)
**Voir aussi :** Microservices, SOA, Clean Architecture
## `EDA` — Event-Driven Architecture [Architecture]
**Niveau :** avance | **Popularité :** 95 | **Aliases :** Architecture Orientée Événements
**Contextes :** concevoir des systèmes réactifs et hautement scalables où les composants communiquent en publiant et s'abonnant à des événements en temps réel (ex: Kafka, RabbitMQ)
**Rôle :** Paradigme d'architecture logicielle basé sur la production, la détection, la consommation et la réaction à des événements système (*Events*).
**Syntaxe :** (Architecture réactive : Producteurs -> Bus d'événements -> Consommateurs)
**Cas réguliers :**
- `Découplage Temporel & Spacial` — L'émetteur d'un événement ne sait pas qui le consomme ni quand il sera traité
- `Pub/Sub (Publish/Subscribe)` — Diffusion d'un événement vers plusieurs services abonnés simultanément
**Origine :** K. Mani Chandy / Gartner (2003).
**Subtilités/confusions :**
- Permet une montée en charge exceptionnelle et une résilience face aux pannes (si un consommateur tombe, les événements s'accumulent dans la file sans être perdus).
- Un suivi des métriques en production permet de prévenir la saturation des ressources.
**Urgences/dangers :** —
**Précautions :** Gérer l'idempotence des consommateurs pour supporter les re-livraisons d'événements en cas de panne réseau.
**Équivalents :** Pub/Sub, Messaging Architecture
**Voir aussi :** Kafka, RabbitMQ, CQRS, Event Sourcing
## `Service Registry` — Annuaire dynamique de découverte de services [Architecture/Cloud]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** Service Discovery
**Contextes :** permettre aux microservices de se localiser dynamiquement entre eux (adresses IP et ports) sans hardcoder de configurations réseau fixes
**Rôle :** Base de données centrale dynamique dans laquelle chaque instance de microservice s'enregistre au démarrage et signale sa présence via des tests de santé (*Health Checks*).
**Syntaxe :** (Solutions : HashiCorp Consul, Netflix Eureka, ETCD, CoreDNS)
**Cas réguliers :**
- `Enregistrement Automatique` — Une nouvelle VM ou pod Kubernetes s'inscrit dans l'annuaire dès son lancement
- `Health Check` — Suppression automatique de l'annuaire si le service ne répond plus aux requêtes de santé
**Origine :** Netflix OSS (Eureka, 2012) / HashiCorp (Consul).
**Subtilités/confusions :**
- Dans Kubernetes, la découverte de services est gérée de manière transparente via le DNS interne (`Kube-DNS` / `CoreDNS`).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Coupler avec un Load Balancer ou une API Gateway pour répartir la charge sur les instances actives.
**Équivalents :** Consul, Eureka, ETCD, DNS
**Voir aussi :** Microservices, Kubernetes, Consul
## `Reverse Proxy` — Serveur mandataire inverse [Réseau/Infrastructure]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** Proxy Inverse
**Contextes :** s'interposer devant des serveurs web pour gérer la terminaison TLS, la répartition de charge, le cache de contenu et la sécurité
**Rôle :** Serveur intermédiaire qui intercepte les requêtes des clients Internet et les achemine vers les serveurs applicatifs internes appropriés.
**Syntaxe :** (Logiciels : Nginx, HAProxy, Traefik, Caddy, Envoy)
**Cas réguliers :**
- `Terminaison TLS` — Déchiffrer le HTTPS au niveau du proxy pour transmettre du HTTP simple et rapide au réseau interne
- `Masquage d'Infrastructure` — Masquer les adresses IP réelles et la topologie des serveurs applicatifs internes
**Origine :** Netscape / CERN (1990s).
**Subtilités/confusions :**
- Un **Forward Proxy** protège et masque les **clients** (sortant) ; un **Reverse Proxy** protège et masque les **serveurs** (entrant).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Transmettre l'adresse IP réelle du client aux serveurs d'arrière-plan via les en-têtes `X-Forwarded-For` et `X-Real-IP`.
**Équivalents :** API Gateway, Load Balancer
**Voir aussi :** Nginx, HAProxy, TLS, WAF
## `Fault Tolerance` — Tolérance aux pannes matérielles et logicielles [Infrastructure]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Tolérance aux Pannes
**Contextes :** concevoir des systèmes capables de continuer à fonctionner sans interruption de service même en cas de défaillance matérielle ou logicielle de l'un de leurs composants
**Rôle :** Propriété d'une architecture informatique garantissant la continuité de fonctionnement malgré la survenance de pannes d'éléments physiques ou logiciels.
**Syntaxe :** (Principe de conception d'infrastructure résiliente)
**Cas réguliers :**
- `Redondance N+1` — Doubler les composants critiques (alimentations électriques, cartes réseau, disques RAID, serveurs)
- `Graceful Degradation` — Dégrader légèrement certaines fonctions secondaires d'un site sans bloquer les fonctionnalités vitales
**Origine :** Informatique spatiale et aéronautique (NASA / Boeing, 1970s).
**Subtilités/confusions :**
- Diffère de la simple Haute Disponibilité (HA) : la tolérance aux pannes garantit souvent **zéro coupure et zéro perte d'état**, alors que la HA accepte une brève bascule de quelques secondes.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Éliminer tous les points uniques de défaillance (*SPOF - Single Point of Failure*).
**Équivalents :** HA (High Availability), Resilience
**Voir aussi :** HA, Circuit Breaker, RAID, PCA
## `Multi-Tenancy` — Architecture multi-locataire [Cloud/Architecture]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Multi-occupant / Multi-tenant
**Contextes :** faire tourner une seule instance d'une application SaaS (ex: Slack, Salesforce, Notion) qui sert des milliers de clients (entreprises) différents en garantissant le cloisonnement étanche de leurs données
**Rôle :** Architecture logicielle dans laquelle une instance unique d'une application sert plusieurs clients distincts (*tenants*).
**Syntaxe :** (Modèle d'isolation de données SaaS)
**Cas réguliers :**
- `Isolation par Schéma / Base` — Une base de données ou un schéma SQL séparé par client
- `Isolation par Colonne (Tenant ID)` — Une seule table partagée contenant une colonne `tenant_id` filtrée systématiquement dans chaque requête SQL
**Origine :** Modèle économique et technique du SaaS cloud (années 2000).
**Subtilités/confusions :**
- Beaucoup plus économique à héberger et à maintenir qu'une architecture mono-tenant (où l'on déploie une VM et une BDD séparée pour chaque client).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Faille critique si un bug de filtrage SQL permet au client A de consulter les données du client B (*Cross-tenant data leak*).
**Précautions :** Activer la sécurité au niveau des lignes (*Row-Level Security / RLS*) directement dans la base de données (ex: PostgreSQL RLS).
**Équivalents :** Single-Tenancy (alternative)
**Voir aussi :** SaaS, Cloud, PostgreSQL, BDD
## `Stateless` — Architecture sans conservation d'état [Cloud/Architecture]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Sans état
**Contextes :** concevoir des serveurs web applicatifs qui ne stockent aucune donnée de session en mémoire locale, permettant de passer à l'échelle à l'infini en ajoutant des serveurs derrière un Load Balancer
**Rôle :** Propriété d'un service ou protocole où chaque requête est traitée de façon autonome sans dépendre d'informations de session conservées sur le serveur entre les requêtes.
**Syntaxe :** (Principe d'architecture Cloud Native / REST)
**Cas réguliers :**
- `Stockage de Session Déporté` — Sauvegarder les sessions utilisateur dans un cache mémoire externe partagé (Redis/Memcached) plutôt que dans la RAM du serveur web
- `Auto-scaling Instantané` — Possibilité d'éteindre ou d'allumer 50 instances de serveurs web à tout moment sans déconnecter les utilisateurs
**Origine :** Conception du protocole HTTP / Roy Fielding (2000).
**Subtilités/confusions :**
- S'oppose aux architectures **Stateful** (avec état) qui nécessitent de rediriger toujours le même utilisateur vers le même serveur (*Sticky Sessions*).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Rendre tous les serveurs web applicatifs 100% Stateless pour tirer pleinement parti de Kubernetes et des Auto-scaling Groups cloud.
**Équivalents :** State-free, Shared-nothing
**Voir aussi :** Stateful, REST, Redis, Twelve-Factor App
## `Stateful` — Architecture avec conservation d'état [Cloud/Architecture]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** Avec état
**Contextes :** désigner les applications et bases de données qui doivent impérativement conserver leur état et leurs données en mémoire ou sur disque entre chaque transaction (ex: PostgreSQL, Redis, Kafka)
**Rôle :** Propriété d'un système qui se souvient des interactions passées et maintient des informations d'état persistantes sur son stockage local.
**Syntaxe :** (Applications avec état : Databases, Caches, Message Brokers)
**Cas réguliers :**
- `StatefulSet Kubernetes` — Objet Kubernetes dédié au déploiement d'applications avec état nécessitant des identifiants réseau stables et des volumes disques persistants
- `Persistance Disque` — Écriture des transactions sur des volumes physiques (SSD/NVMe)
**Origine :** Architecture système traditionnelle.
**Subtilités/confusions :**
- La gestion des applications Stateful est beaucoup plus complexe dans le cloud que celle des applications Stateless (gestion des sauvegardes, réplication, basculement de disques).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Séparer clairement la couche applicative Stateless (facile à scaler) de la couche de stockage Stateful (hautement sécurisée).
**Équivalents :** State-bearing
**Voir aussi :** Stateless, Kubernetes, BDD, Redis
## `Circuit Breaker` — Patron de disjoncteur réseau [DevOps/Architecture]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Disjoncteur Logiciel
**Contextes :** empêcher qu'une panne sur un microservice secondaire (ex: service de recommandation) ne fasse s'effondrer par cascade l'ensemble du site web (ex: blocage du panier d'achat)
**Rôle :** Patron de résilience qui coupe temporairement les appels vers un service distant (*Open*) au-delà d'un seuil d'erreur et renvoie un mode dégradé (*Fallback*).
**Syntaxe :** (États : Fermé / Normal, Ouvert / Coupé, Semi-Ouvert / Test)
**Cas réguliers :**
- `Fermé (Closed)` — Le trafic circule normalement, les erreurs sont comptabilisées
- `Ouvert (Open)` — Le service distant est en panne : les appels sont bloqués immédiatement sans attente de timeout, renvoyant la réponse de secours
- `Semi-Ouvert (Half-Open)` — Quelques requêtes de test sont autorisées pour vérifier si le service distant est rétabli
**Origine :** Michael Nygard (*Release It!*, 2007) / Netflix Hystrix (2012).
**Subtilités/confusions :**
- Évite que des centaines de requêtes ne restent bloquées en attente de timeout, ce qui épuiserait tous les threads du serveur appelant.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Toujours prévoir une réponse de secours (*Fallback*) pertinente (ex: renvoyer une liste de produits par défaut au lieu d'une erreur 500).
**Équivalents :** Resilience4j, Hystrix, Istio Fault Injection
**Voir aussi :** Microservices, Rate Limiting, Fault Tolerance
## `Rate Limiting` — Limitation du débit de requêtes applicatives [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Limiteur de Débit
**Contextes :** protéger une API web contre la surconsommation, les attaques par force brute, le scraping abusif et les déni de service (DDoS)
**Rôle :** Mécanisme de contrôle de trafic qui limite le nombre de requêtes qu'un client (IP, clé d'API, utilisateur) peut effectuer dans une fenêtre de temps donnée.
**Syntaxe :** En-tête HTTP de réponse : `HTTP 429 Too Many Requests`
**Cas réguliers :**
- `Algorithme Token Bucket / Leaky Bucket` — Moteurs algorithmiques classiques de limitation de débit
- `En-têtes standards` — `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
- `Limitation par IP ou par Token` — Ex: max 100 requêtes/minute par adresse IP
**Origine :** Ingénierie réseau / Protocole Leaky Bucket (1986).
**Subtilités/confusions :**
- En cas de dépassement de quota, le serveur doit renvoyer le code de statut HTTP `429 Too Many Requests`.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser un cache Redis centralisé pour partager le compteur de rate-limiting entre tous les serveurs de votre infrastructure.
**Équivalents :** Throttling, Quota Management
**Voir aussi :** WAF, Redis, HTTP, API Gateway
## `Service Mesh` — Maillage de services d'infrastructure [Cloud/Architecture]
**Niveau :** avance | **Popularité :** 93 | **Aliases :** Maillage de Services
**Contextes :** gérer de manière transparente la sécurité (mTLS), le routage, la observabilité et la résilience des communications entre milliers de microservices sans modifier leur code source
**Rôle :** Couche d'infrastructure dédiée à la gestion sécurisée et observable des communications de service à service (*East-West traffic*) dans un cluster Kubernetes.
**Syntaxe :** (Projets : Istio, Linkerd, Consul Service Mesh, Cilium)
**Cas réguliers :**
- `Sidecar Proxy (Envoy)` — Un petit proxy léger est injecté à côté de chaque conteneur applicatif pour intercepter et sécuriser tout son trafic entrant/sortant
- `mTLS Automatique` — Chiffrement et authentification mutuelle automatique de tous les échanges entre microservices
**Origine :** William Morgan / Linkerd / Buoyant (2016) / Istio (Google & IBM, 2017).
**Subtilités/confusions :**
- Déporte la gestion de la sécurité réseau, du retry et des métriques hors du code des développeurs vers la couche d'infrastructure.
- Les implémentations doivent suivre les recommandations de sécurité et les mises à jour régulières.
**Urgences/dangers :** ⚠️ Un Service Mesh ajoute une légère latence réseau (< 2 ms) et consomme des ressources mémoire CPU pour chaque proxy sidecar.
**Précautions :** Évaluer Cilium (basé sur eBPF) pour des architectures Service Mesh sans sidecar plus légères.
**Équivalents :** Istio, Linkerd, Cilium
**Voir aussi :** Kubernetes, Microservices, TLS
## `Telemetry` — Collecte automatique de métriques, logs et traces [DevOps]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Télémétrie
**Contextes :** mesurer et collecter en continu les données d'état d'un système informatique en fonctionnement (métriques CPU/RAM, journaux d'erreurs, traces de requêtes)
**Rôle :** Processus automatique de mesure et de transmission de données depuis des sources distantes vers un système de traitement et de visualisation centralisé.
**Syntaxe :** (Standard d'industrie : OpenTelemetry / OTel)
**Cas réguliers :**
- `Les 3 Piliers de l'Observabilité` — Metrics (chiffres/compteurs), Logs (événements textuels), Traces (parcours d'une requête)
- `OpenTelemetry (OTel)` — Standard mondial de la CNCF fournissant des SDKs d'instrumentation universels
**Origine :** Ingénierie aérospatiale / Télémesure (19e siècle) / Dérivé en IT avec le monitoring.
**Subtilités/confusions :**
- La télémétrie est l'étape de **collecte et d'émission** des données ; l'**Observabilité** est la capacité de comprendre l'état interne du système grâce à ces données.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Échantillonner (*Sampling*) la collecte de traces en haute charge pour éviter de consommer un espace disque colossal.
**Équivalents :** OpenTelemetry, Monitoring
**Voir aussi :** Distributed Tracing, Prometheus, SIEM, ELK
## `Distributed Tracing` — Traçage distribué de requêtes [DevOps/Cloud]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Traçage Distribué
**Contextes :** suivre le parcours exact d'une requête utilisateur à travers des dizaines de microservices distincts pour identifier instantanément quel service cause un ralentissement
**Rôle :** Technique d'observabilité qui attribue un identifiant unique (*Trace ID*) à chaque requête entrante et le propage dans les en-têtes HTTP/gRPC d'un service à l'autre.
**Syntaxe :** En-tête de propagation W3C : `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`
**Cas réguliers :**
- `Trace ID` — Identifiant unique global représentant l'ensemble du voyage de la requête
- `Span ID` — Identifiant représentant le temps passé dans une opération ou un microservice individuel
**Origine :** Google Dapper (2010) / OpenZipkin, Jaeger, OpenTelemetry.
**Subtilités/confusions :**
- Permet de visualiser sous forme de diagramme de Gantt (cascade) le temps exact consommé par chaque appel d'API et requête base de données.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser OpenTelemetry pour instrumenter votre code de manière indépendante de l'outil de stockage final (Jaeger, Datadog, Tempo).
**Équivalents :** Jaeger, Zipkin, AWS X-Ray, Grafana Tempo
**Voir aussi :** Telemetry, Microservices, Prometheus
## `Idempotency` — Idempotence des opérations applicatives et réseau [Développement/API]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Idempotence
**Contextes :** concevoir des APIs et des processeurs de paiements ou de messages de manière à ce qu'exécuter la même requête plusieurs fois produise exactement le même résultat qu'une exécution unique
**Rôle :** Propriété d'une opération mathématique ou informatique qui produit le même effet qu'elle soit exécutée une seule fois ou plusieurs fois de suite avec les mêmes paramètres.
**Syntaxe :** En-tête HTTP : `Idempotency-Key: 7b9b2447-0929-4560-b286-90e6659f13d8`
**Cas réguliers :**
- `Verbes HTTP Idempotents` — `GET`, `PUT`, `DELETE` sont idempotents par nature (`DELETE /user/42` exécuté 10 fois laisse l'utilisateur supprimé sans effet de bord supplémentaire)
- `Clé d'Idempotence (Idempotency Key)` — Jeton unique envoyé lors d'un `POST` de paiement Stripe : si la connexion coupe et que le client réessaie, Stripe ne débite pas le client une deuxième fois !
**Origine :** Mathématiques (algèbre) / Spécification HTTP RFC 7231.
**Subtilités/confusions :**
- `POST` n'est pas idempotent par défaut (exécuter `POST /orders` 3 fois crée 3 commandes distinctes) ; d'où la nécessité d'utiliser une clé d'idempotence.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Indispensable dans les architectures distribuées où les coupures réseau entraînent des tentatives de re-livraison automatiques (*Retries*).
**Précautions :** Conserver les clés d'idempotence traitées dans un cache Redis pendant 24h.
**Équivalents :** Repeatability
**Voir aussi :** HTTP, REST, Redis, Kafka
## `DLQ` — Dead Letter Queue [DevOps/Architecture]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** File de Lettres Mortes
**Contextes :** isoler automatiquement les messages d'une file d'attente (RabbitMQ, SQS, Kafka) qui n'ont pas pu être traités après plusieurs tentatives en raison d'erreurs ou de données corrompues
**Rôle :** File d'attente secondaire dans laquelle un middleware de messagerie déplace les messages en échec répétitif pour éviter de bloquer le traitement des autres messages.
**Syntaxe :** (Configuration de file d'attente RabbitMQ / AWS SQS)
**Cas réguliers :**
- `Poison Pill Message` — Message malformé qui fait planter systématiquement le consommateur à chaque tentative
- `Analyse Post-Mortem` — Inspection manuelle ou re-traitement différé des messages isolés dans la DLQ
**Origine :** Systèmes de messagerie d'entreprise (Enterprise Messaging, 1990s).
**Subtilités/confusions :**
- Empêche l'effet de boucle infinie où un consommateur essaie en continu de lire un message cassé sans jamais pouvoir dépiler les suivants.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Configurer des alertes de monitoring sur la taille de la DLQ pour être averti dès qu'un message y est transféré.
**Précautions :** Prévoir des scripts de re-jeu (*Replay*) pour ré-injecter les messages de la DLQ dans la file principale après correction du bug.
**Équivalents :** Poison Queue, Retry Queue
**Voir aussi :** RabbitMQ, Kafka, EDA
## `CRUD` — Create, Read, Update, Delete [Développement/BDD]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Opérations CRUD
**Contextes :** désigner les 4 opérations fondamentales de manipulation de données persévérées dans une base de données ou exposées par une API
**Rôle :** Acronyme décrivant les quatre actions de base sur la donnée : Création, Lecture, Mise à jour et Suppression.
**Syntaxe :** (Correspondance SQL & HTTP)
**Cas réguliers :**
- `C - Create` — SQL `INSERT` / HTTP `POST`
- `R - Read` — SQL `SELECT` / HTTP `GET`
- `U - Update` — SQL `UPDATE` / HTTP `PUT` ou `PATCH`
- `D - Delete` — SQL `DELETE` / HTTP `DELETE`
**Origine :** James Martin (1983 / *Managing the Data-Base Environment*).
**Subtilités/confusions :**
- Une application "pur CRUD" se contente de faire de la saisie et de l'affichage de formulaires sans logique métier complexe.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Réfléchir à l'utilisation de la suppression logique (*Soft Delete*) à la place du `DELETE` physique pour pouvoir restaurer des données effacées par erreur.
**Équivalents :** BREAD (Browse, Read, Edit, Add, Delete)
**Voir aussi :** SQL, REST, BDD
## `ACID` — Atomicity, Consistency, Isolation, Durability [BDD]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** Propriétés ACID
**Contextes :** garantir la fiabilité et l'intégrité absolue des transactions financières ou critiques dans les bases de données relationnelles (PostgreSQL, MySQL)
**Rôle :** Ensemble de 4 garanties de sécurité appliquées aux transactions de bases de données relationnelles.
**Syntaxe :** (Propriétés de transactions SQL)
**Cas réguliers :**
- `A - Atomicité` — La transaction s'exécute entièrement ou pas du tout ("Tout ou Rien")
- `C - Cohérence` — La transaction fait passer la base d'un état valide à un autre état valide en respectant toutes les contraintes
- `I - Isolation` — Plusieurs transactions concurrentes ne s'interfèrent pas (niveaux d'isolement : Read Committed, Repeatable Read, Serializable)
- `D - Durabilité` — Une fois la transaction validée (*COMMIT*), ses effets sont définitivement enregistrés sur disque même en cas de panne de courant immédiate
**Origine :** Jim Gray (1970s) / Acronyme par Andreas Reuter et Theo Härder (1983).
**Subtilités/confusions :**
- S'oppose au modèle **BASE** des bases de données NoSQL distribuées qui privilégient la haute disponibilité au détriment de la cohérence immédiate.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Choisir le niveau d'isolement des transactions SQL adapté aux exigences de votre application (attention aux verrous et deadlocks en mode `Serializable`).
**Équivalents :** BASE (alternative NoSQL)
**Voir aussi :** BASE, PostgreSQL, MySQL, BDD
## `BASE` — Basically Available, Soft state, Eventual consistency [BDD/Cloud]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** Modèle BASE
**Contextes :** concevoir des bases de données NoSQL distribuées à très grande échelle (Cassandra, DynamoDB, MongoDB) capables de fonctionner sans interruption sur des milliers de serveurs
**Rôle :** Modèle d'architecture de persistance distribuée assouplissant les contraintes strictes d'ACID au profit de la haute disponibilité et de la cohérence éventuelle.
**Syntaxe :** (Modèle de persistance NoSQL distribuée)
**Cas réguliers :**
- `Basically Available` — Le système garantit la disponibilité des données en répondant toujours, même en cas de pannes partielles de nœuds
- `Soft State` — L'état du système peut évoluer au fil du temps sans intervention utilisateur en raison de la réplication d'arrière-plan
- `Eventual Consistency` — Les données deviendront cohérentes sur l'ensemble des nœuds au bout d'un certain délai (quelques millisecondes)
**Origine :** Dan Pritchett / eBay (2008).
**Subtilités/confusions :**
- Acronyme choisi comme un jeu de mots opposé à **ACID** (Base vs Acide en chimie).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Ne pas utiliser une base de données au modèle BASE pour de la tenue de compte bancaire où chaque centime doit être exact en temps réel.
**Équivalents :** Eventual Consistency, ACID (alternative)
**Voir aussi :** ACID, CAP Theorem, NoSQL, Cassandra
## `CAP Theorem` — Théorème CAP de Brewer [BDD/Architecture]
**Niveau :** avance | **Popularité :** 97 | **Aliases :** Théorème de Brewer
**Contextes :** faire des choix d'architecture fondamentaux lors de la sélection d'une base de données distribuée ou d'un système réseau
**Rôle :** Théorème : un système distribué ne peut garantir simultanément que deux des trois propriétés — Cohérence (**C**), Disponibilité (**A**), Tolérance au morcellement (**P**).
**Syntaxe :** (Choix d'architecture : CP vs AP vs CA)
**Cas réguliers :**
- `C - Cohérence (Consistency)` — Tous les nœuds voient exactement les mêmes données au même moment
- `A - Disponibilité (Availability)` — Chaque requête reçue par un nœud non défaillant reçoit une réponse
- `P - Tolérance au morcellement (Partition Tolerance)` — Le système continue de fonctionner malgré la perte de messages réseau entre nœuds
**Origine :** Eric Brewer (2000 / Preuve formelle par Seth Gilbert et Nancy Lynch, 2002).
**Subtilités/confusions :**
- Dans un réseau réel, les coupures réseau (P) sont inévitables : le vrai choix imposé par CAP est donc entre **CP** (bloquer la réponse pour garantir la cohérence) et **AP** (répondre immédiatement avec des données potentiellement périmées).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Consulter l'extension **PACELC** pour une modélisation plus fine des choix d'architecture en fonctionnement normal.
**Équivalents :** PACELC Theorem
**Voir aussi :** PACELC, ACID, BASE, NoSQL
## `PACELC` — Extension du Théorème CAP [BDD/Architecture]
**Niveau :** avance | **Popularité :** 86 | **Aliases :** Théorème PACELC
**Contextes :** affiner les critères d'évaluation des bases de données distribuées en prenant en compte leur comportement en fonctionnement normal (hors panne réseau)
**Rôle :** Extension du CAP par Daniel Abadi : en cas de morcellement (**P**), choisir Disponibilité (**A**) ou Cohérence (**C**) ; sinon, choisir Latence (**L**) ou Cohérence (**C**).
**Syntaxe :** Format : `PA/EL` (ex: DynamoDB est PA/EL, MongoDB est PC/EC)
**Cas réguliers :**
- `MongoDB (PC/EC)` — Privilégie la cohérence en cas de panne et la cohérence en fonctionnement normal
- `DynamoDB / Cassandra (PA/EL)` — Privilégie la disponibilité en cas de panne et la faible latence en fonctionnement normal
**Origine :** Daniel Abadi (2012 / Yale University).
**Subtilités/confusions :**
- Résout la lacune du théorème CAP qui n'expliquait pas les compromis d'architecture lorsque le réseau fonctionne parfaitement sans panne.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Choisir la base de données dont le profil PACELC correspond exactement aux tolérances de votre métier.
**Équivalents :** CAP Theorem
**Voir aussi :** CAP Theorem, BASE, NoSQL
## `iPaaS` — Integration Platform as a Service [Cloud/Enterprise]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** Plateforme d'Intégration Cloud
**Contextes :** connecter des applications SaaS cloud (Salesforce, Zendesk, ServiceNow) avec des systèmes On-Premise sans développer de middleware sur-mesure
**Rôle :** Service cloud permettant de développer, d'exécuter et de gérer des flux d'intégration de données et d'APIs entre applications disparates.
**Syntaxe :** (Services : Workato, Make, Zapier, Boomi, MuleSoft CloudHub)
**Cas réguliers :**
- `Connecteurs Pré-intégrés` — Glisser-déposer des blocs d'intégration prêts à l'emploi (ex: synchroniser automatiquement un lead HubSpot vers PostgreSQL)
- `Automation No-Code / Low-Code` — Permettre aux équipes métiers et intégrateurs d'automatiser des flux sans coder d'infrastructures
**Origine :** Gartner (2011).
**Subtilités/confusions :**
- L'iPaaS est la modernisation cloud en mode SaaS des anciens middlewares **EAI** et **ESB**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Surveiller les coûts d'exécution au volume de requêtes transmis par les fournisseurs iPaaS.
**Équivalents :** EAI, ESB, Zapier, Make
**Voir aussi :** ESB, EAI, SaaS, Cloud
## `SECaaS` — Security as a Service [Cloud/Sécurité]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** Sécurité en tant que Service
**Contextes :** externaliser des fonctions de cybersécurité (antivirus, filtrage web, SIEM, protection DDoS, WAF) auprès d'un fournisseur cloud spécialisé
**Rôle :** Modèle de fourniture de services de sécurité informatique hébergés dans le cloud et facturés sous forme d'abonnement.
**Syntaxe :** (Services : Cloudflare, Zscaler, CrowdStrike, Okta)
**Cas réguliers :**
- `Protection DDoS & WAF Cloud` — Filtrage du trafic malveillant avant qu'il n'atteigne le datacenter de l'entreprise
- `Gestion des Identités (IDaaS)` — Authentification centralisée hébergée (Okta, Auth0)
**Origine :** Cloud Security Alliance (CSA, 2011).
**Subtilités/confusions :**
- Permet aux PME de bénéficier de technologies de sécurité de niveau militaire sans investir dans des équipements matériels coûteux.
- Ne pas confondre avec le SaaS standard : le SECaaS se concentre exclusivement sur les fonctions de cybersécurité et d'audit.
**Urgences/dangers :** —
**Précautions :** Vérifier les certifications de sécurité du prestataire SECaaS (ISO 27001, SOC 2 Type II).
**Équivalents :** Managed Security Service Provider (MSSP)
**Voir aussi :** WAF, SIEM, EDR, SaaS
## `B2B` — Business to Business [Entreprise]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Commerce Interentreprises
**Contextes :** désigner les activités commerciales, logiciels et services d'une entreprise s'adressant spécifiquement à d'autres entreprises (et non au grand public)
**Rôle :** Modèle économique et commercial régissant les échanges commerciaux entre professionnels.
**Syntaxe :** (Modèle économique d'entreprise)
**Cas réguliers :**
- `Logiciels B2B` — Progiciels d'entreprise (ERP, CRM, Slack, Snowflake, Datadog)
- `Cycles de Vente Longs` — Processus de décision impliquant de multiples validateurs (Achats, DSI, Juridique) et des contrats annuels
**Origine :** Vocabulaire économique et commercial traditionnel.
**Subtilités/confusions :**
- S'oppose à **B2C** (Business to Consumer).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Intégrer les exigences de sécurité et de conformité d'entreprise (SAML SSO, SOC 2, DPA) dès la conception de produits B2B.
**Équivalents :** B2C (alternative), B2B2C
**Voir aussi :** B2C, ERP, CRM, SaaS
## `B2C` — Business to Consumer [Entreprise]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Vente aux Particuliers
**Contextes :** désigner les produits, services et applications web/mobiles s'adressant directement aux consommateurs individuels (ex: Netflix, Amazon, Spotify, Uber)
**Rôle :** Modèle économique et commercial orienté vers le grand public.
**Syntaxe :** (Modèle économique grand public)
**Cas réguliers :**
- `Volume & Scalabilité` — Nécessite de supporter de très grands volumes d'utilisateurs simultanés avec une UX d'une simplicité absolue
- `Marketing de Masse` — Stratégies d'acquisition basées sur le référencement, les réseaux sociaux et la recommandation
**Origine :** Vocabulaire commercial et e-commerce.
**Subtilités/confusions :**
- Les exigences UX et de vitesse de premier chargement (LCP) sont encore plus critiques en B2C qu'en B2B.
- Un suivi des métriques en production permet de prévenir la saturation des ressources.
**Urgences/dangers :** —
**Précautions :** Optimiser l'infrastructure pour supporter des pics de trafic soudains (ventes flash, campagnes TV).
**Équivalents :** B2B (alternative)
**Voir aussi :** B2B, UX, PWA, CDN
## `SDN` — Software-Defined Networking [Réseau]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** Réseau Piloté par Logiciel
**Contextes :** automatiser la configuration et la gestion des équipements réseau (routeurs, commutateurs) en séparant le plan de contrôle (logiciel) du plan de données (matériel)
**Rôle :** Architecture réseau qui centralise le contrôle du trafic au niveau d'un contrôleur logiciel programmable sans intervenir physiquement sur chaque switch.
**Syntaxe :** (Technologies : OpenFlow, VMware NSX, OpenDaylight, Cisco ACI)
**Cas réguliers :**
- `Séparation Contrôle / Données` — Le plan de contrôle (décision) est centralisé ; le plan de données (paquets) reste sur les équipements physiques
- `Réseau Virtuel Programmable` — Créer des réseaux virtuels (VLANs/VXLANs) à la volée via des requêtes d'API
**Origine :** Université de Stanford / UC Berkeley (projet OpenFlow, 2008).
**Subtilités/confusions :**
- La brique fondamentale qui a permis la création du **Cloud Computing** moderne (AWS VPC, GCP VPC).
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Protéger le contrôleur SDN central avec une haute disponibilité maximale pour éviter d'isoler tout le réseau.
**Équivalents :** SD-WAN, NFV (Network Functions Virtualization)
**Voir aussi :** SD-WAN, Cloud, Réseau, VPC
## `SD-WAN` — Software-Defined Wide Area Network [Réseau]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** WAN Piloté par Logiciel
**Contextes :** interconnecter les différents sites d'une entreprise (siège, usines, magasins) en optimisant dynamiquement l'utilisation de liens Internet standards (Fibre, 4G/5G) et MPLS
**Rôle :** Application des principes du SDN aux réseaux étendus (WAN) pour gérer et sécuriser automatiquement le trafic entre sites distants.
**Syntaxe :** (Solutions : Cisco Meraki, Fortinet SD-WAN, VMware Velocloud)
**Cas réguliers :**
- `Routage Dynamique` — Aiguiller le trafic critique (VoIP) sur le lien MPLS et le trafic web classique sur une fibre grand public bon marché
- `Réduction des Coûts` — Remplacer de coûteuses liaisons MPLS dédiées par des liaisons Internet sécurisées par chiffrement IPsec
**Origine :** Évolutions des technologies SDN au milieu des années 2010.
**Subtilités/confusions :**
- Permet de diviser les coûts de connectivité inter-sites par 3 à 5 tout en augmentant la bande passante globale.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Intégrer des briques de sécurité (SASE / Firewall cloud) directement sur les équipements SD-WAN d'agences.
**Équivalents :** MPLS (alternative traditionnelle), SASE
**Voir aussi :** SDN, IPsec, VPN, Réseau
## `BaaS` — Backend as a Service [Cloud/Web]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** Backend en tant que Service
**Contextes :** accélérer le développement d'applications web et mobiles en sous-traitant l'intégralité du back-end (base de données, auth, stockage, notifications) à une plateforme cloud (Firebase, Supabase)
**Rôle :** Modèle de service cloud fournissant aux développeurs une infrastructure back-end prête à l'emploi accessible directement via des SDKs client.
**Syntaxe :** `await supabase.from('users').select('*')`
**Cas réguliers :**
- `Services Inclus` — Base de données temps réel, authentification (OAuth/Email), stockage de fichiers (S3-like), Fonctions Serverless
- `Projets phares` — Firebase (Google), Supabase (Alternative open source PostgreSQL), PocketBase, Appwrite
**Origine :** Parse (2011) / Google Firebase.
**Subtilités/confusions :**
- Permet à un développeur frontend ou mobile de créer une application complète en autonomie sans écrire une seule ligne de code serveur traditionnel.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** ⚠️ Ne jamais oublier de configurer les règles de sécurité de la base de données (Firestore Security Rules / PostgreSQL RLS) sous peine de laisser la base ouverte en lecture/écriture à tout Internet !
**Précautions :** Utiliser des alternatives open source comme Supabase pour éviter le verrouillage propriétaire (*Vendor Lock-in*).
**Équivalents :** Firebase, Supabase, Serverless
**Voir aussi :** Firebase, Supabase, Serverless, Firestore
## `FaaS` — Function as a Service [Cloud/Serverless]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Fonctions Serverless
**Contextes :** exécuter des morceaux de code événementiels (fonctions) dans le cloud sans provisionner ni administrer de serveurs (ex: AWS Lambda, Google Cloud Functions)
**Rôle :** Cœur de l'architecture Serverless permettant de déployer de simples fonctions exécutées à la demande et facturées à la milliseconde près.
**Syntaxe :** `exports.handler = async (event) => { return { statusCode: 200, body: "Hello" }; };`
**Cas réguliers :**
- `Paiement à l'Exécution` — Facturation uniquement lorsque la fonction s'exécute (0€ si personne ne l'appelle !)
- `Cold Start (Démarrage à froid)` — Léger délai d'attente (quelques centaines de ms) lors de la toute première exécution d'une fonction inactive
**Origine :** AWS Lambda (Amazon Web Services, 2014).
**Subtilités/confusions :**
- Les fonctions FaaS sont **Stateless** et éphémères : elles sont détruites après exécution et ne doivent rien stocker sur leur disque local.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Optimiser la taille du paquet de déploiement et des dépendances pour minimiser l'impact du *Cold Start*.
**Équivalents :** AWS Lambda, Cloud Functions, Azure Functions
**Voir aussi :** Serverless, Cloud, AWS, Stateless
## `DBA` — Database Administrator [Management/BDD]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** Administrateur de Bases de Données
**Contextes :** désigner l'expert responsable de l'installation, de la configuration, des performances, des sauvegardes et de la sécurité des bases de données de l'entreprise
**Rôle :** Rôle technique spécialisé garantissant la disponibilité, l'intégrité, la vitesse et la sauvegarde des systèmes de gestion de bases de données (SGBD).
**Syntaxe :** (Métier / Rôle d'ingénierie BDD)
**Cas réguliers :**
- `Tuning de Recommandations & Index` — Optimiser les requêtes SQL lentes et créer des index appropriés
- `Sauvegardes & Restauration (PRA)` — S'assurer que les sauvegardes sont valides et tester les procédures de restauration
**Origine :** Origines des grands SGBD d'entreprise (IBM, Oracle, 1970s).
**Subtilités/confusions :**
- Avec l'avènement des bases cloud managées (AWS RDS) et du DevOps, le rôle évolue vers celui d'**Ingénieur Data Infrastructure**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Automatiser les tâches de maintenance récurrentes (analyse des tables, réindexation, vérification d'espace disque).
**Équivalents :** Data Infrastructure Engineer, Database Reliability Engineer (DBRE)
**Voir aussi :** BDD, SQL, PostgreSQL, Oracle
## `Platform Engineering` — Ingénierie de plateforme interne [DevOps/Cloud]
**Niveau :** avance | **Popularité :** 94 | **Aliases :** IDP (Internal Developer Platform)
**Contextes :** créer une plateforme interne en libre-service (*Internal Developer Platform / IDP*) pour offrir aux développeurs des environnements de dev, de test et de prod sans qu'ils aient à maîtriser la complexité de Kubernetes ou de Terraform
**Rôle :** Discipline d'ingénierie concevant et maintenant des outils et plateformes internes en libre-service pour améliorer l'expérience développeur (*Developer Experience / DX*).
**Syntaxe :** (Discipline organisationnelle et outillage IDP : Backstage, Humanitec, Port)
**Cas réguliers :**
- `IDP (Internal Developer Platform)` — Portail web interne permettant à un dev de provisionner une base de données ou un environnement de test en 1 clic
- `Réduction de la Charge Mentale` — Masquer la complexité des manifestes YAML Kubernetes et des règles cloud derrière des abstractions simples
**Origine :** Évolutions du DevOps à l'échelle / Manuel Pais et Matthew Skelton (*Team Topologies*, 2019).
**Subtilités/confusions :**
- Le Platform Engineering traite la plateforme interne comme un **produit** dont les **développeurs internes sont les clients**.
- Les choix d architecture doivent évaluer l impact sur la maintenance et la complexité opérationnelle.
**Urgences/dangers :** —
**Précautions :** Utiliser des portails open source comme **Backstage** (Spotify) pour cataloguer les services et APIs de l'entreprise.
**Équivalents :** Developer Experience (DX), Internal Cloud
**Voir aussi :** DevOps, Kubernetes, Terraform, Backstage