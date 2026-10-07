#!/usr/bin/env bash
# masaustu-kur — 4k-claude komutlarını ve menü girdilerini bilgisayara kurar (T-050). Tekrar çalıştırmak güvenlidir.
# Kurar: ~/.local/bin/{4k-claude,4k-pano,4k-claude-test} bağları; ~/.local/share/applications/4k-claude*.desktop;
# test kopyası yoksa ilk kurulumunu yapar (~/.local/share/4k-claude-test). Silme yapmaz.
# Kullanım (sahibi, bir kez): ~/Work/4k-claude/00-sistem/scripts/masaustu-kur.sh
set -euo pipefail
betik="$(dirname "$(readlink -f "$0")")"
bin="$HOME/.local/bin"; app="$HOME/.local/share/applications"
mkdir -p "$bin" "$app"
ln -sfn "$betik/4k-claude.sh" "$bin/4k-claude"
ln -sfn "$betik/pano.sh" "$bin/4k-pano"
ln -sfn "$betik/test-kurulum.py" "$bin/4k-claude-test"
for d in "$betik"/masaustu/*.desktop; do sed "s|@BIN@|$bin|g" "$d" > "$app/$(basename "$d")"; chmod 644 "$app/$(basename "$d")"; done
command -v update-desktop-database >/dev/null && update-desktop-database "$app" >/dev/null 2>&1 || true
echo "Komutlar: 4k-claude, 4k-pano, 4k-claude-test · Menü: 4K Claude, 4K Claude Pano, 4K Claude Test, 4K Claude Test Pano"
if [ ! -d "$HOME/.local/share/4k-claude-test/kasa" ]; then
  echo "Test kopyası kuruluyor (doğrulama ~1 dk)…"
  "$bin/4k-claude-test" guncelle
fi
"$bin/4k-pano"
