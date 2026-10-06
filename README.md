# Yeni Sistem

Fikirden gerçek dünyaya giden her işi aynı yoldan geçiren, Claude Code ile işletilen bir çalışma düzeni. Dört kat (İç Ses, Devlet, Şirket, İnsan) ve bir omurga; her sayfa aynı şemayla doğar, haritada ve günlükte görünür; hiçbir iş sessizce yarım kalmaz.

## Başlangıç
```bash
cd yeni-sistem
python3 00-sistem/scripts/kontrol.py      # bütünlük tam olmalı
git init && git add -A && git commit -m "T-000: kurulum"
claude                                     # Claude Code'u bu klasörde aç
```
İlk talimat: `00-sistem/TALIMATLAR.md` içindeki T-001 (dört talimatlık deneme).

## Nerede ne var
- `CLAUDE.md` çekirdek kurallar · `.claude/` izinler, hook'lar, kurallar, skill'ler, ajanlar
- `00-sistem/` SISTEM (kök harita), SEMA (alanlar), HARITA (dizin), GUNLUK, ILERLEME, TALIMATLAR, KARARLAR, şablonlar, betikler, araştırma
- `40-ic-ses/` zihin · `30-devlet/` irade · `20-sirket/` örgütleme · `10-insan/` eller · `01-gelen/` gelen kutusu · `90-arsiv/`

Ayrıntı: `00-sistem/SISTEM.md`. Mimari belgesi: Yeni Sistem Mimarisi v2.0 (Claude Docs).

## Gereksinimler
python3 (hook'lar ve betikler standart kütüphaneyle çalışır; PyYAML varsa kullanılır), git, Claude Code. Sandbox için (isteğe bağlı) bubblewrap + socat.
