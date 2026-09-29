# Data Model — Entité Universelle v2 (pour 10k-50k entrées)

Toute entité, quelle que soit sa Face, utilise ce schéma JSON. C'est ce qui permet la recherche "dans tous les sens" + l'export multi-plateforme.

## Fiche Riche v3 — schéma complet (obligatoire pour tout nouveau contenu, 29/09)
```json
{
  "id": "A-00101", "face": "A", "type": "commande", "nom": "tar",
  "aliases": [], "os": ["linux", "macos"], "os_raw": "Linux/macOS",
  "categories": ["archives"], "tags": ["compresser", "sauvegarde"],
  "niveau": "intermediaire", "popularite": 90,
  "role_fr": "Archiver et compresser des fichiers",
  "syntaxe": "tar [options] <archive> <fichiers>",
  "contextes": ["sauvegarde serveur", "distribution logicielle"],
  "cas_reguliers": [{"cmd": "tar -czf b.tar.gz d/", "explication": "Sauvegarde", "contexte": "backup quotidien"}],
  "origine": "Tape ARchive, Unix V7 1979",
  "subtilites": ["Sans -z pas de compression"],
  "urgences_dangers": "⚠️ ...", "precautions": "...",
  "equivalents": [{"os": "windows", "cmd": "Compress-Archive"}],
  "voir_aussi": ["gzip"], "source": "faceA_06_archives.md", "version": 1, "updated_at": "2026-09-29"
}
```
Face B : mêmes champs, `signification` dans aliases[0], `role_fr`=définition, `syntaxe`="". 10 rubriques A / 8 rubriques B obligatoires. Format source : fiches Markdown `##` (voir CONVENTIONS), parsées par tools/parse_rich.py.

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

## Volumes cibles (MVP porté à 1000 le 29/09 — demande Adolphe)
- MVP 1000 = 600 commandes A + 400 sigles B, en fiches RICHES v3 ("la totale" : contextes, cas réguliers, origines, subtilités/confusions, urgences)
- Phase 2 (5000) : A complète + B + C
- Phase 3 (30000+) : import auto Wiktionary, man pages, docs MS, contributions communauté avec modération
