#!/usr/bin/env bash
# check.sh - rituel de verification du corpus, a lancer avant chaque commit de lot.
# Usage: ./tools/check.sh
set -uo pipefail
cd "$(dirname "$0")/.."
code=0

run() {
  echo ""
  echo "== $1 =="
  shift
  "$@" || { code=1; echo ">>> ECHEC"; }
}

run "1/5 tests unitaires du parseur" python3 tools/test_parse.py
run "2/5 validation du corpus (schema + regles)" python3 tools/validate.py
run "3/5 analyse parseur (check, sans ecriture)" python3 tools/parse_rich.py --check --quiet
run "4/5 derive du JSON committe" python3 tools/parse_rich.py --compare --quiet
run "5/5 statistiques" python3 tools/stats.py
run "5/5 audit qualite" python3 tools/audit.py --summary

echo ""
if [ "$code" -eq 0 ]; then
  echo "OK: pipeline vert"
else
  echo "ECHEC: voir les etapes ci-dessus"
fi
exit "$code"
