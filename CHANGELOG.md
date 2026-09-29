# Changelog

## 2026-09-29 10h40 — Lot 1 contenu (par Muse Spark)
- FaceA_05_reseau.md : 15 cmds (ping, curl, wget, ssh, scp, sftp, ip, dig, nslookup, ss, netstat...)
- FaceB_01_abreviations.md vague 1/4 : 54 sigles (matériel, réseau, web, prog, sécu, concept)
- Fix validate.py : split ignore | dans backticks + clés Face:nom (IP/SSH existent en A et B légitimement)
- md_to_json.py : support Face B (sigle→nom, signification→alias, catégorie, description→role_fr)
- CONVENTIONS.md : schéma Face B 6 colonnes + catégories fermées
- Résultat : 85 → 154 entrées (30.8% MVP), validate ✅ 0 erreur

## 2026-09-29 — Phase 0 (par Muse Spark)
- git init + .gitignore + dossiers data/tools/web_preview/.logs
- Corrections : tail -f.log→-f app.log, head/tail OS Linux/macOS, mv typo, hostname -I→Linux seul, free→Linux seul + alternatives macOS
- Ajout vision v2, architecture Flutter+Firebase, data model, plan 10 phases, todo tracker, conventions
- Outils : validate.py, md_to_json.py, stats.py + web_preview/index.html + firebase.json/rules/indexes

## Session 3 — 29/09/2026 : contenu riche v3 en marche (208 entités, 20.8% du MVP)
- MVP officiellement porté à **1000** (600 A + 400 B) dans TODO_TRACKER
- `parse_rich.py` validé : 29 fiches riches v3 conformes (10 rubriques Face A / 8 Face B) + fusion automatique riche→legacy (SQL, VM élévés)
- `stats.py` MVP1000, app web : contextes, cas réguliers, subtilités dépliables, origine
- FaceA_06 : 32/40 (gestionnaires multi-OS + builds : tar…zypper)
- FaceB_02 : 26/90 (DevOps/Cloud/BDD : CI…BI)
- TOTAL : 208 entités / 1000 (20.8%) — 57 fiches riches conformes — validate 0 erreur
