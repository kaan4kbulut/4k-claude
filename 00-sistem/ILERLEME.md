# İlerleme

Bu dosya "kesintiyi varsay" ilkesinin karşılığıdır. Her oturum SessionStart hook'u ile bunu okur; /kapat ve PreCompact hook'u bunu yazar.

aktif_talimat: T-013 (kapandı) — sıradaki T-014 İç Ses ses hattı (öncelik 7)
kapi: yok
acik_soru: agent-scan (veri Snyk'e gider) · telemetri kuyruğu silinsin mi · 3 ölü kaynak bağlantısı nasıl işaretlensin · F-0001 yazıcı türü · hafif yol
siradaki: T-014 öncelik 7 (ses: /voice Türkçe + yerel TTS denemesi); sahibi: güven onayı, Web Clipper; T-002..T-004 açık

## T-005 (2026-10-06)
- [x] calistir.sh --bare · durus-kapisi dosya izi · yikici-koruma 35 test · MALIYET transcript · şema belirlenmedi · gunluk.py · git
- Değişen: bkz. DEGISIKLIKLER 0.2.0; commit e39a086 sonrası

## T-001 (2026-10-06)
- [x] KAYIT (T-001 zaten açıktı) · AMAÇ+KAT (4) · YER+AD (40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md) · ŞABLON · BAĞLAR (MOC M1 + park) · KAPANIŞ (HARITA, GUNLUK, TALIMATLAR)
- Değişen: F-0001 (yeni), MOC-ic-ses, HARITA, GUNLUK, TALIMATLAR, ILERLEME

## Kurulum partileri (T-000)

- [x] Parti 1: CLAUDE.md, .claude/settings.json, .claude/hooks (5), .claude/rules (5)
- [x] Parti 2: .claude/skills (10), .claude/agents (2)
- [x] Parti 3: 00-sistem kök dosyaları (SISTEM, SEMA, sema/*.json, HARITA, GUNLUK, DEGISIKLIKLER, TALIMATLAR, KARARLAR, MALIYET, ASK yok)
- [x] Parti 4: 00-sistem/sablonlar (23: parca, gozlem, fikir, yansima, kavram, karar, kural, yonerge, kapi, gorev, rol, sop, alan-paketi, talimat, brifing, brif, bulgu, moc, kaynak, cikti, arastirma-notu, eylem-plani, ham)
- [x] Parti 5: 00-sistem/scripts (kontrol.py, bayat.py, harita.py, calistir.sh)
- [x] Parti 6: 40-ic-ses, 30-devlet (ANAYASA, IMZA-MATRISI, MODEL-POLITIKASI, HAKEM-KURALLARI, K-001..), 20-sirket (SCORECARD, RITIM, alan-paketleri/3d-uretim), 10-insan (ARAC-KAYDI), MOC'lar, README, .gitignore
- [x] Parti 7: araştırma raporlarının frontmatter tamamlaması (id, yazar, kaynaklar), HARITA ve GUNLUK dolumu
- [x] Parti 8: kontrol.py testi, düzeltmeler, zip, teslim

## Değişen dosyalar (bu oturum)
- 00-sistem/arastirma/01..09 (frontmatter tamamlandı)
- 00-sistem/HARITA.md (harita.py --uret ile üretildi)
- 00-sistem/GUNLUK.md (26 [yeni] + 2 [karar] satırı)
- 00-sistem/scripts/kontrol.py (wikilink atlama kuralı)
- 30-devlet/kararlar/K-001 (besledigi += K-002)
- 00-sistem/ILERLEME.md (bu dosya)

## Son kanıt
`python3 00-sistem/scripts/kontrol.py` → çıkış 0 · "Bütünlük tam: 26 sayfa, 27 bağ, 26 harita satırı. Uyarı: 0."
