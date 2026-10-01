# Face A - Fixture de test unitaire

## `testfmt` - Formater une fixture [Linux/macOS]
**Niveau :** debutant | **Popularite :** 42 | **Aliases :** tf
**Contexte :** fabriquer des exemples de test
**Role :** Commande de test du parseur (ne pas importer en production).
**Syntaxe :** `testfmt [options] <cible>`
**Cas reguliers :**
- `testfmt -a` - premier cas
- `testfmt -b` - deuxieme cas
- `testfmt -c` - troisieme cas
**Origine :** fixture locale (2026)
**Subtilites/confusions :**
- La rubrique suivante ne doit pas etre avalee comme une puce.
**Urgences/dangers :** -
**Precautions :** -
**Equivalents :** testfmt2
**Voir aussi :** cd

## `testnl` - Fixture avec ligne vide avant la rubrique suivante [Cross]
**Niveau :** intermediaire | **Popularite :** 11
**Contexte :** tester la fin de liste sur ligne vide
**Role :** Deuxieme fixture du parseur pour verifier l'arret de liste.
**Syntaxe :** `testnl --go`
**Cas reguliers :**
- `testnl un` - cas un
- `testnl deux` - cas deux

**Origine :** fixture locale (2026)
**Subtilites/confusions :**
- Une ligne vide termine bien la liste des cas.
**Urgences/dangers :** -
**Precautions :** -
**Equivalents :** -
**Voir aussi :** testfmt

## `alpha` / `beta` - Fixture de titre compose [Cross]
**Niveau :** debutant | **Popularite :** 3
**Contexte :** verifier les alias automatiques
**Role :** Troisieme fixture : le titre compose doit creer un alias.
**Syntaxe :** `alpha beta`
**Cas reguliers :**
- `alpha` - invoque le binaire alpha
- `beta` - invoque le binaire beta
**Origine :** fixture locale (2026)
**Subtilites/confusions :**
- La barre oblique separe deux noms, pas un chemin.
**Urgences/dangers :** -
**Precautions :** -
**Equivalents :** -
**Voir aussi :** testfmt
