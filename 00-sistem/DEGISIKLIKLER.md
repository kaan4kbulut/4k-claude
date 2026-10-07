# Değişiklikler — sistemin kendi sürüm günlüğü

Biçim: Keep a Changelog 1.1.0; sürümleme SemVer. Şema ya da kural değişikliği MINOR, şablon/betik düzeltmesi PATCH, kat yapısı değişikliği MAJOR. Bu dosya sistemin kendisini anlatır; içerik sayfalarının değişiklikleri GUNLUK.md'dedir.

## [Unreleased]
### Eklendi
- `pano.py` ilk aşama (T-034): salt okur HTML pano, kabuk + Pano + Sağlık ekranları, çıktı `00-sistem/.kosu/pano/`; yalnız stdlib, ağ yok, betik/stil/http yok. Tasarım CSS'i `scripts/pano-tasarim/css/` (01-gelen/ham paketinden, değiştirilmeden). Başlatıcı `pano.sh` (üretir + `xdg-open`). Testler `test_pano.py` (7).
### Değişti
- `yscommon.py` HARIC_KLASOR += `01-gelen/ham` (T-032): gelen kutusunun özgün dış dosyaları (HTML, CSS, PNG, frontmatter'sız .md) taranmaz; okunacak hâlleri `al.py` notu olarak `01-gelen/*.md`'de durur.
### Düzeltildi
- GUNLUK.md: 2026-10-07 17:04-17:06 kota hatası satırları (kapanis-kaydi hook'u çok satırlı hata özeti yazmıştı) tek satır kuralına getirildi (T-032).

## [0.10.0] — 2026-10-07 (T-024..T-031, eksik analizi)
### Eklendi
- `kontrol.py` 16. denetim (T-025): son kapanan talimatın GUNLUK [oturum] satırı, ILERLEME ve nerede-kaldik izi; en çok bir açık talimat; aktif_talimat tutarlılığı. /kapat 3. adımı artık engelle sağlanır.
- GitHub açık depo `kaan4kbulut/4k-claude` (T-026, KP-003): commit e-postası gizli adres, geçmiş yeniden yazıldı; `push.sh` + systemd kullanıcı path birimi her commit'ten sonra sandbox dışından push eder (sonuç `00-sistem/.kosu/push.log`).
- `00-sistem/testler/` (T-027): 35 regresyon testi — yikici-koruma (red/sor/izin, yanlış pozitif), durus-kapisi, ayar-denetimi, kontrol.py bozma senaryoları, gunluk.py. Depo kopyasında koşar. `kontrol.py --test` hepsini çalıştırır.
- `butce-bekcisi.py` (T-028, UserPromptSubmit): oturum maliyetini her istemde transcript'ten tahmin eder (kapanis-kaydi hesabı), tavanı MODEL-POLITIKASI'ndan okur; %80 ve tavanın katlarında bir kez uyarı, tavanda GUNLUK [hata]. Engellemez. 6 test.
- `scorecard.py` (T-029): SCORECARD S1–S8 dosyalardan (son 7 gün); `--yaz T-xxx` haftalık satır + Issues; ölçülemeyen gösterge "ölçülmüyor" ve neden. /haftalik 6. adım bunu çağırır. 5 test. İlk kayıt 2026-W41.
- `kasa-disi-koruma.py` (T-031, kullanıcı düzeyi PreToolUse, ~/.claude/settings.json): oturum klasör dışında açıldıysa 4k-claude'a yazımı reddeder, okumalar serbest; başka projelere dokunmaz. `4k-claude.sh` başlatıcısı (~/.local/bin/4k-claude). 7 test.
### Düzeltildi
- `calistir.sh` GUNLUK'e `echo` ile yazıyordu; satırları artık `gunluk.py` yazar (kural 3).
- MALIYET.csv: klasör dışından açılan 5fd94f32 oturumu geriye dönük eklendi (≈65,80 USD; ccusage 64,54).

## [0.9.0] — 2026-10-07 (T-019..T-021)
### Eklendi
- Y-001 yönergesi: çift yönlü kararlar orkestratörde; sahibine yalnız imza matrisi ve fiziksel eylemler.
- KR-001 hafif yol kural taslağı (önerildi) ve `not.py` (kural kabul edilmeden çıkış 3).
### Düzeltildi
- Fikir şablonu varsayılanı `merdiven: 0` (eski `merdiven: 1` + `cynefin: belirlenmedi` kontrol.py 14. denetimiyle çelişiyordu).

## [0.8.0] — 2026-10-07 (T-013)
### Eklendi
- `canli.py` (lychee 0.24.2): web bağlantı canlılığı; ilk rapor 414 bağlantı, 401 canlı, 3 ölü (404), 6 belirsiz.
- `maliyet.py` (ccusage 20.0.26): MALIYET.csv ↔ oturum kayıtları mutabakatı; eşik %5.
- `/haftalik` metrikler: maliyet mutabakatı ve bağlantı canlılığı adımı.
### Düzeltildi
- `kapanis-kaydi.py`: önbellek yazımı TTL'ye göre fiyatlanır (5 dk 1.25×, 1 saat 2×). Eski tek tip 1.25× tahmin ~%30 düşüktü; yeni yöntem 9 oturumda ccusage ile ±%0.1.

## [0.7.0] — 2026-10-07 (T-012)
### Eklendi
- `al.py`: PDF/DOCX/PPTX/XLSX/HTML/URL → 01-gelen ham not (markitdown, yerel, LLM yok). Meta veri JSON dizgisiyle yazılır (YAML kırılamaz); taranmış PDF uyarısı.
- `00-sistem/sablonlar/web-clipper-gelen.json`: Obsidian Web Clipper şablonu (ham not alanları).
- `settings.json` env: `ORT_DISABLE_TELEMETRY=1` (onnxruntime 1DS telemetrisi).
### Değişti
- `kontrol.py`: ham notlarda gövde wikilink denetimi yok; boş bağ alanı [] sayılır. `graf.py`: ham notlar grafa girmez.

## [0.6.0] — 2026-10-07 (T-011)
### Eklendi
- `ayar-denetimi.py` (ConfigChange, SessionStart, PermissionDenied): güvenlik değişmezlerini bozan ayar değişikliği oturuma yüklenmez; açılışta diskteki ihlal uyarılır; geçerli değişiklik anahtar düzeyinde GUNLUK'e; auto kipte izin reddi kaydı. İmzalı istisna: KP (go) + `.claude/ayar-imzasi.json`.
### Değişti
- `kapanis-kaydi.py`: ConfigChange kaydı ayar-denetimi'ne taşındı (çift kayıt yok).

## [0.5.0] — 2026-10-07 (T-010)
### Eklendi
- `ara.py`: qmd 2.8.3 ile yerel anlamsal arama (varsayılan vektör; `--hibrit`, `--kelime`, `--yenile`, `--mcp`). Dizin ve modeller proje içinde (`.araclar/`, git dışı) ki sandbox içinden güncellenebilsin. 01-gelen, şablonlar ve günlükler dizin dışı.
- `ara-olcum.py`: 20 Türkçe sorguluk isabet ölçümü. Sonuç: 40-ic-ses/arastirma-notlari/qmd-turkce-isabet.
### Düzeltildi
- Şema: `sonuc` enum'u araştırma notu değerlerini (dogruluyor, celisiyor, bilinmiyor) kabul eder; kontrol.py tür karışmasını (kapıda araştırma değeri ve tersi) hata sayar. T-005'ten kalan şablon/şema uyumsuzluğu.

## [0.4.0] — 2026-10-06 (T-009)
### Eklendi
- `graf.py`: frontmatter ve wikilink'lerden sayfa grafı; Graphify 0.9.77 (kütüphane, LLM'siz) ile topluluk, merkez, sınır aşan bağ, HTML. Çıktı `00-sistem/.kosu/graf/`. Proje `.venv/` (git dışı).
- `/uyku tam` adım 7a: graf bulguları bağ ve yansıma önerisine döner.
- İzin: `graf.py` allow; `graphify install`, `graphify hook`, `--mode deep` deny.
### Değişti
- `yscommon` ve `sikistirma-oncesi`: `00-sistem/.kosu` (üretilmiş dosyalar) taramadan çıkarıldı.

## [0.3.0] — 2026-10-06 (T-008)
### Değişti
- Bash sandbox açıldı (`.claude/settings.json` → `sandbox`): `enabled`, `failIfUnavailable`, `allowUnsandboxedCommands: false`, `autoAllowBashIfSandboxed`, kimlik bilgisi klasörleri `denyRead`, boş ağ izin listesi. Onay: KP-001.

## [0.2.0] — 2026-10-06 (T-005)
### Düzeltildi
- `calistir.sh`: `--bare` kaldırıldı; gözetimsiz koşuda hook'lar ve CLAUDE.md yükleniyor.
- `durus-kapisi`: metin araması yerine dosya izi; sohbet turu serbest, yalnız wiki değişikliği kontrol.py ile geçer, diğer değişiklik gerçek kanıt (`komut` + çıkış kodu), ASK.md ya da bu oturumda yazılmış [durdu] satırı ister; ikinci denemede kanıtsız durma GUNLUK'e [hata] olarak yazılır.
- `yikici-koruma`: commit mesajı/heredoc/grep deseni yanlış pozitifleri giderildi; find -delete, rmtree, +refspec push, kabukla ANAYASA/normlar yazımı, göreli proje dışı yönlendirme, sembolik bağ ve NotebookEdit açıkları kapatıldı; tek dosya rm sahibine sorulur.
- `kapanis-kaydi`: MALIYET.csv token ve maliyeti transcript'ten okur (message.id tekilleştirme, alt ajanlar dahil); fiyatlar MODEL-POLITIKASI'ndan. CSV'ye cache_okuma, cache_yazma, model sütunları eklendi.
- `yscommon`: PyYAML'ın döndürdüğü tüm tarih nesneleri metne çevrilir (sabit alan listesi kaldırıldı).
- `settings.json`: belgelenmemiş `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` kaldırıldı; PreToolUse eşleyicisine NotebookEdit eklendi.
### Değişti
- Şema: `kapi` ve `sonuc` enum'larına `belirlenmedi`; kontrol.py 14. denetim: belirlenmedi yalnız taslakta / M4 öncesi fikirde.
### Eklendi
- `gunluk.py`: GUNLUK satırını sistem saatiyle yazar. kontrol.py 15. denetim: GUNLUK zaman sırası (uyarı).
- Git deposu (temel commit 20bc76d).

## [0.1.0] — 2026-10-06
### Eklendi
- Dört katlı klasör düzeni (00-sistem, 01-gelen, 10-insan, 20-sirket, 30-devlet, 40-ic-ses, 90-arsiv).
- CLAUDE.md (çekirdek kurallar, 10 sert kural, oturum protokolü, Compact instructions).
- `.claude/settings.json`: izinler (deny/ask/allow), hook kayıtları, alt ajan modeli.
- Hook'lar: oturum-basi (SessionStart), durus-kapisi (Stop), yikici-koruma (PreToolUse), sikistirma-oncesi (PreCompact), kapanis-kaydi (SessionEnd/StopFailure/PostToolUseFailure/ConfigChange).
- Kurallar: 00-sistem (kapsamsız), 40-ic-ses, 30-devlet, 20-sirket, 10-insan (yol kapsamlı).
- Skill'ler: yeni-parca, degistir, kapat, brifing, uyku, karar, kapi, alan-paketi, haftalik, inbox-triage.
- Alt ajanlar: okuyucu (karantinalı), denetci (bağımsız inceleyici).
- 00-sistem: SISTEM, SEMA, sema/sayfa.schema.json, sema/kapi-raporu.schema.json, HARITA, GUNLUK, ILERLEME, TALIMATLAR, KARARLAR, DEGISIKLIKLER, MALIYET.csv.
- Şablonlar (18): parca, gozlem, fikir, yansima, kavram, karar, kural, yonerge, kapi, gorev, rol, sop, alan-paketi, talimat, brifing, brif, bulgu, moc.
- Betikler: kontrol.py (13 denetim), bayat.py, harita.py, calistir.sh.
- Kat dosyaları: ANAYASA, IMZA-MATRISI, MODEL-POLITIKASI, HAKEM-KURALLARI, K-001, K-002, MOC'lar, nerede-kaldik, SCORECARD, RITIM, alan-paketleri/3d-uretim, ARAC-KAYDI.
- Araştırma raporları (9) `00-sistem/arastirma/`.
