# Data Model — Entité Universelle v2 (pour 10k-50k entrées)

Toute entité, quelle que soit sa Face, utilise ce schéma JSON. C'est ce qui permet la recherche "dans tous les sens" + l'export multi-plateforme.

```json
{
  "id": "A-01234",
  "face": "A",
  "type": "commande",
  "nom": "cp",
  "aliases": ["copy", "Copy-Item"],
  "os": ["linux", "macos"],
  "categories": ["fichiers", "copie"],
  "tags": ["copier", "dupliquer", "backup"],
  "niveau": "debutant",
  "role_fr": "Copier un fichier ou dossier",
  "role_en": "Copy files and directories",
  "syntaxe": "cp [options] <source> <cible>",
  "exemples": [{"cmd": "cp -r src/ dest/", "explication": "Copie récursive"}],
  "precautions": "Écrase sans confirmation",
  "equivalents": [{"os": "windows-powershell", "cmd": "Copy-Item"}],
  "voir_aussi": ["A-00012", "B-00231"],
  "popularite": 95,
  "version": 1,
  "updated_at": "2026-09-29"
}
```

## Règles
- `id` stable, jamais réutilisé. A=Commandes, B=Sigles, C=Concepts, D=Erreurs, E=Dev, F=Outils.
- `os` vocab fermé : linux, windows-cmd, windows-powershell, macos, bash, zsh, git, docker, k8s, aws, az, gcloud, cross.
- `niveau` : debutant | intermediaire | avance | expert.
- `face` B exemple : nom=API, aliases=[Application Programming Interface], role_fr=...
- `face` D exemple : nom="Permission denied", syntaxe="", exemples=[{cmd:"chmod +x..."}]

## Migration depuis Markdown actuel
Tableau actuel 7 colonnes → mapping auto :
`commande→nom, OS→os (normalisé), rôle→role_fr, syntaxe→syntaxe, exemples→exemples (split ·), précautions→precautions, équivalents→equivalents`
Script `tools/import.py` fera ça + rapport d'erreurs (ex: `tail -f.log`, `hostname -I` sur macOS à corriger).

## Volumes cibles
- Phase 1 (MVP 500 entrées propres) : finir A + démarrer B
- Phase 2 (5000) : A complète + B + C
- Phase 3 (30000+) : import auto Wiktionary, man pages, docs MS, contributions communauté avec modération
