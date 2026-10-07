#!/usr/bin/env bash
# push.sh — commit sonrası otomatik push (KP-003, T-026).
# ~/.config/systemd/user/4k-claude-push.path .git/logs/HEAD değişince bunu sandbox dışından çalıştırır
# (4k-claude oturumunda sandbox ağı ve ~/.config/gh okumasını kapatır; içeriden push olmaz).
# Yalnız hızlı ileri push; force yok. Sonuç 00-sistem/.kosu/push.log'a, hata ayrıca GUNLUK'e.
set -u
cd "$(dirname "$0")/../.."
LOG=00-sistem/.kosu/push.log
mkdir -p 00-sistem/.kosu
sleep 3  # commit ve ardışık commit'ler bitsin
DAL=$(git symbolic-ref --short HEAD 2>/dev/null) || exit 0
[ "$DAL" = master ] || exit 0
if CIKTI=$(git -c credential.helper= -c credential.helper='!gh auth git-credential' push --porcelain origin master 2>&1); then
  echo "$(date '+%F %T') ok $(git rev-parse --short HEAD)" >> "$LOG"
else
  SON=$(echo "$CIKTI" | tail -1)
  echo "$(date '+%F %T') HATA $SON" >> "$LOG"
  python3 00-sistem/scripts/gunluk.py hata 00-sistem/scripts/push.sh "otomatik push başarısız: $SON" >/dev/null
  exit 1
fi
