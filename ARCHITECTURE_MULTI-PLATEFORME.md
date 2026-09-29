# Architecture Multi-Plateforme — Dictionnaire IT

## Choix cible : Flutter + Firebase + SQLite FTS5

```
[ Contributeurs MD/JSON ] → [ tools/import.py → Firestore + SQLite ] 
                                ↓
[ Firebase: Firestore + Auth + Hosting + Functions + Storage ]
                                ↓
[ Flutter App unique → Android | iOS | Web PWA | Windows | macOS | Linux ]
+ Cache local SQLite FTS5 pour offline + recherche instantanée <50ms
```

### Pourquoi Flutter ?
- 1 langage (Dart), 6 compilations natives. Idéal solo.
- PWA Web installable + Stores (Play/App Store via même build) + .exe/.dmg/.deb via même build.
- Perf suffisante pour 50k entrées en local.

### Pourquoi Firebase (tu as déjà commencé) ?
- Firestore = base entités + favoris + historique user.
- Auth = Google/Email (ton log montre déjà `adolphechristopher@gmail.com` connecté).
- Hosting = héberge PWA gratuitement.
- Functions = API recherche floue + suggestions IA plus tard.
- Storage = images/schémas.

### Recherche "dans tous les sens"
- V1 locale : SQLite FTS5 (full-text FR tokenisé) + filtres OS/catégorie. 100% offline.
- V2 cloud : Meilisearch ou Algolia (typo-tolérant, synonymes `copier=cp=Copy-Item`) OU Typesense auto-hébergé si coût.
- V3 IA : embeddings + `cherche.py` sémantique ("comment libérer de l'espace disque ?" → `df, du, apt clean`).

### Structure repo cible
```
/data/faceA/*.md + *.json (source)
/data/faceB/*.md ...
/app_flutter/ (1 codebase)
/tools/validate.py, import.py, export.py, stats.py
/web_preview/index.html (démo rapide avant Flutter)
/firestore.rules, firebase.json
TODO_TRACKER.md, CHANGELOG.md
```

### Offline-first obligatoire
Afrique/Europe mobilité : l'app doit marcher sans internet. Sync Firestore → SQLite au premier lancement, puis delta.

### Coûts
- Dev : 0€ (Flutter+Firebase free tier : 50k lectures/jour suffisantes pour V1).
- Scale 10k users : ~25€/mois → migrer recherche vers Meilisearch VPS 6€.
