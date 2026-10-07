#!/usr/bin/env bash
# 4k-claude — Claude Code oturumunu kasada açar (T-031).
# Proje ayarı (sandbox, koruma hook'ları, maliyet kaydı) yalnız oturum bu klasörde açılınca yüklenir.
# Kurulum: ln -s <kasa>/00-sistem/scripts/4k-claude.sh ~/.local/bin/4k-claude
cd "$(dirname "$(readlink -f "$0")")/../.." && exec claude "$@"
