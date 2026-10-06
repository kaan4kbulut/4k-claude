# Değişiklikler — sistemin kendi sürüm günlüğü

Biçim: Keep a Changelog 1.1.0; sürümleme SemVer. Şema ya da kural değişikliği MINOR, şablon/betik düzeltmesi PATCH, kat yapısı değişikliği MAJOR. Bu dosya sistemin kendisini anlatır; içerik sayfalarının değişiklikleri GUNLUK.md'dedir.

## [Unreleased]

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
- Git deposu (temel commit e39a086).

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
