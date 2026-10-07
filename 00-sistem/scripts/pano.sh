#!/usr/bin/env bash
# pano — 4k-claude panosunu üretir ve uygulama penceresinde açar (T-034, T-050). Salt okur; yalnız 00-sistem/.kosu/pano'ya yazar.
# Kurulum: 00-sistem/scripts/masaustu-kur.sh (komut 4k-pano + menü girdisi "4K Claude Pano").
set -e
kok="$(dirname "$(readlink -f "$0")")/../.."
kok="$(cd "$kok" && pwd)"
python3 "$kok/00-sistem/scripts/pano.py"
[ "${1:-}" = "--acma" ] && exit 0
adres="file://$kok/00-sistem/.kosu/pano/pano.html"
if command -v omarchy-launch-webapp >/dev/null; then
  omarchy-launch-webapp "$adres" >/dev/null 2>&1 &
else
  xdg-open "$adres" >/dev/null 2>&1 &
fi
