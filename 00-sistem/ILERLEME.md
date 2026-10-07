# İlerleme

Bu dosya "kesintiyi varsay" ilkesinin karşılığıdır. Her oturum SessionStart hook'u ile bunu okur; /kapat ve PreCompact hook'u bunu yazar. Son kapanan talimat burada adıyla geçmezse kontrol.py hata verir (16. denetim, T-025).

aktif_talimat: T-026 — GitHub açık depo, gizli e-posta, otomatik push
kapi: KP-003 go (A6, A9; sahibi sohbette onayladı)
acik_soru: yok
siradaki: T-026 GitHub açık depo + otomatik push (sahibi A6/A9 onayladı); ardından hook testleri, bütçe uyarısı, scorecard, F-0001 soruları, klasör dışı açılış engeli

## Son kapanış
- T-025 (2026-10-07): Kapanış kaydı artık engelle sağlanıyor: kontrol.py 16. denetim eski hâlde 2 hata verdi (nerede-kaldik T-024 yok, aktif_talimat yanlış), düzeltmeden sonra 0. Kanıt: kontrol.py --kisa önce → 1 (2 hata), sonra → 0.
- T-024 (2026-10-07): .obsidian dar istisna (K-005), git dışı. Kanıt: `git check-ignore .obsidian/app.json` → 0; `kontrol.py --kisa` → 0 (40 sayfa, 47 bağ). Commit ede2e0a.
- T-017..T-023 kayıtları: TALIMATLAR.md kapanış notları ve GUNLUK [oturum] satırları (bu dosyaya o dönemde yazılmadı; 2026-10-07 eksik analizi).

## Eski kayıtlar
### T-005 (2026-10-06)
- [x] calistir.sh --bare · durus-kapisi dosya izi · yikici-koruma 35 test · MALIYET transcript · şema belirlenmedi · gunluk.py · git
- Değişen: bkz. DEGISIKLIKLER 0.2.0; commit e39a086 sonrası

### T-001 (2026-10-06)
- [x] KAYIT (T-001 zaten açıktı) · AMAÇ+KAT (4) · YER+AD (40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md) · ŞABLON · BAĞLAR (MOC M1 + park) · KAPANIŞ (HARITA, GUNLUK, TALIMATLAR)
- Değişen: F-0001 (yeni), MOC-ic-ses, HARITA, GUNLUK, TALIMATLAR, ILERLEME

### Kurulum partileri (T-000)

- [x] Parti 1: CLAUDE.md, .claude/settings.json, .claude/hooks (5), .claude/rules (5)
- [x] Parti 2: .claude/skills (10), .claude/agents (2)
- [x] Parti 3: 00-sistem kök dosyaları (SISTEM, SEMA, sema/*.json, HARITA, GUNLUK, DEGISIKLIKLER, TALIMATLAR, KARARLAR, MALIYET, ASK yok)
- [x] Parti 4: 00-sistem/sablonlar (23: parca, gozlem, fikir, yansima, kavram, karar, kural, yonerge, kapi, gorev, rol, sop, alan-paketi, talimat, brifing, brif, bulgu, moc, kaynak, cikti, arastirma-notu, eylem-plani, ham)
- [x] Parti 5: 00-sistem/scripts (kontrol.py, bayat.py, harita.py, calistir.sh)
- [x] Parti 6: 40-ic-ses, 30-devlet (ANAYASA, IMZA-MATRISI, MODEL-POLITIKASI, HAKEM-KURALLARI, K-001..), 20-sirket (SCORECARD, RITIM, alan-paketleri/3d-uretim), 10-insan (ARAC-KAYDI), MOC'lar, README, .gitignore
- [x] Parti 7: araştırma raporlarının frontmatter tamamlaması (id, yazar, kaynaklar), HARITA ve GUNLUK dolumu
- [x] Parti 8: kontrol.py testi, düzeltmeler, zip, teslim

### Değişen dosyalar (bu oturum)
- 00-sistem/arastirma/01..09 (frontmatter tamamlandı)
- 00-sistem/HARITA.md (harita.py --uret ile üretildi)
- 00-sistem/GUNLUK.md (26 [yeni] + 2 [karar] satırı)
- 00-sistem/scripts/kontrol.py (wikilink atlama kuralı)
- 30-devlet/kararlar/K-001 (besledigi += K-002)
- 00-sistem/ILERLEME.md (bu dosya)

### Son kanıt
`python3 00-sistem/scripts/kontrol.py` → çıkış 0 · "Bütünlük tam: 26 sayfa, 27 bağ, 26 harita satırı. Uyarı: 0."
