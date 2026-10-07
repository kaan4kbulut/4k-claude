#!/usr/bin/env bash
# pano — 4k-claude panosunu üretir ve tarayıcıda açar (T-034). Salt okur; yalnız 00-sistem/.kosu/pano'ya yazar.
# Kurulum (sahibi, bir kez): ln -s <kasa>/00-sistem/scripts/pano.sh ~/.local/bin/4k-pano
set -e
kok="$(dirname "$(readlink -f "$0")")/../.."
python3 "$kok/00-sistem/scripts/pano.py"
[ "${1:-}" = "--acma" ] || xdg-open "$kok/00-sistem/.kosu/pano/pano.html" >/dev/null 2>&1 &
