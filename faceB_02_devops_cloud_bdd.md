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
