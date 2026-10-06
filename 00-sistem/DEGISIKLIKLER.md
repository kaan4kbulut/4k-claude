# Değişiklikler — sistemin kendi sürüm günlüğü

Biçim: Keep a Changelog 1.1.0; sürümleme SemVer. Şema ya da kural değişikliği MINOR, şablon/betik düzeltmesi PATCH, kat yapısı değişikliği MAJOR. Bu dosya sistemin kendisini anlatır; içerik sayfalarının değişiklikleri GUNLUK.md'dedir.

## [Unreleased]

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
