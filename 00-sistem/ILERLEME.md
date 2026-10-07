# İlerleme

Bu dosya "kesintiyi varsay" ilkesinin karşılığıdır. Her oturum SessionStart hook'u ile bunu okur; /kapat ve PreCompact hook'u bunu yazar. Son kapanan talimat burada adıyla geçmezse kontrol.py hata verir (16. denetim, T-025).

aktif_talimat: yok — T-037 kapandı; sıradaki: liste T-b (mod koruması kararı)
kapi: yok
acik_soru: yok
siradaki: talimat listesi ~/Work/isler/2026-10-07-yz-teknoloji-taramasi/4k-claude-talimatlari.md T-b … T-m sırayla (kaynak: 10-insan/kaynaklar/yz-teknoloji-taramasi-2026-10-07). Sahibi: test kopyasını kur, panoyu gözle kontrol; /tmp/claude-1000/4k-test-* (40 klasör) kararı; mali müşavire metni gönder

## Son kapanış
- T-037 (2026-10-07): YZ tarama raporu gelen kutusundan kaynak sayfasına işlendi; iddialar URL'siz, UNCONFIRMED. Kanıt: al.py → 0; harita.py --dogrula → 0 (43); kontrol.py --kisa → 0.
- T-036 (2026-10-07): Hatalar: test kopyalama (sızıntı + sandbox yer tutucuları), kasa-disi-koruma yanlış pozitifleri (realpath hedefli), eski yol, ara.py yeni yol, not.py metni, çok satırlı GUNLUK kök nedeni. Kanıt: kontrol.py --test gerçek depoda → 0; yeni testler eski hook'larda FAIL (14 + 1); eski/yeni karşılaştırma 116 komut → gerçek daralma 0; ara.py --yenile → 0; kontrol.py --kisa → 0; denetci 2 tur, engelleyiciler düzeltildi.
- T-035 (2026-10-07): Ayrı test kopyası: test-kurulum.py guncelle/geri/pano/durum; doğrulamayı geçmeyen kopya geçmez, uzak depo bağı kalırsa geçmez. Açık: ilk kurulum ve bağ sahibine. Kanıt: kontrol.py --test temiz kopyada → 0; uçtan uca guncelle (tam doğrulama) → 0; uzak bağ denetimi kapatılınca test FAIL; kontrol.py --kisa → 0; denetci: engelleyici (remote) düzeltildi.
- T-034 (2026-10-07): pano.py ilk aşaması: Pano ve Sağlık ekranları 00-sistem/.kosu/pano'da; başlatıcı pano.sh. Açık: görsel kontrol ve ~/.local/bin bağı sahibine. Kanıt: pano.py → 0; grep script/style/http → 0; kontrol.py --test temiz kopyada → 0 (62), bozuk kopyada 6 FAIL; kontrol.py --kisa → 0; denetci: engelleyici yok.
- T-033 (2026-10-07): Pano paketinin iki notu işlendi → 10-insan/kaynaklar/pano-tasarim-paketi (kapsam, §6, §9). Talimat benzeri içerik (izin satırı önerisi) uyulmadan kaydedildi. Kanıt: harita.py --dogrula → 0 (42); kontrol.py --kisa → 0 (44 sayfa).
- T-032 (2026-10-07): Pano tasarım paketi 01-gelen/ham'de, içerik aynı; ham dosyalar kontrol.py taramasından hariç. Açık: ~/Downloads zip'ini arşive taşımak (proje dışı, sahibi). Kanıt: sha256sum -c → 35/35 OK; zip içeriği 35/35 OK; kontrol.py --test gerçek depoda → 1 (40 hata: sandbox /dev/null yer tutucuları copytree'yi bozuyor), git ls-files kopyasında → 0 (53); kontrol.py --kisa → 0.
- T-031 (2026-10-07): Klasör dışında açılan oturum artık 4k-claude'a yazamaz (okuma serbest); oturumlar 4k-claude ile açılır. Kurulum bu commit'ten sonra yapıldı; canlı doğrulama brifingde. Kanıt: kontrol.py --test → 0 (53); kontrol.py --kisa → 0.
- T-030 (2026-10-07): Mali müşavire 3 soruluk metin hazır; F-0001'de sıradaki insan noktaları yazılı. Sahibi deneme türünü henüz bilmiyor, önce müşavir cevabını görmek istiyor. Açık: metni göndermek (sahibi). Kanıt: kontrol.py --kisa → 0; sahibine tek soru soruldu (cevap: henüz bilmiyor).
- T-029 (2026-10-07): Scorecard artık ölçülüyor; ilk kayıt 2026-W41: S1 %97 (T-001 kaydı eksik), S5 67,85 USD (bir oturum tavanı 13× aştı). S7 flip sayacı ölçülmüyor ([konum] satır türü yok). Kanıt: kontrol.py --test → 0 (46); scorecard.py --yaz T-029 → SCORECARD 0.2; kontrol.py --kisa → 0.
- T-028 (2026-10-07): Oturum tavanı artık oturum sürerken ölçülüyor (uyarı + GUNLUK, engel yok). Gerçek ölçüm: 5fd94f32 ≈65,80 USD = tavanın 13 katı. Tavan ya da model politikası değişikliği sahibinin kararı (A5). Kanıt: kontrol.py --test → 0 (41 test); gerçek 7,2 MB transcript'te 0,18 s, 65,80 USD (ccusage 64,54, +%2); kontrol.py --kisa → 0.
- T-027 (2026-10-07): 35 regresyon testi; kontrol.py --test → 0. Negatif kanıt: kopyada sudo kuralı, kanıt denetimi ve zorunlu deny bozulunca 6 test düştü. Hook davranışında hata bulunmadı. Kanıt: kontrol.py --test → 0 (35 test); bozuk kopyada → FAILED (6); kontrol.py --kisa → 0.
- T-026 (2026-10-07): 4k-claude GitHub'da açık (kaan4kbulut/4k-claude); geçmişte gmail 0, GitHub'da 58/58 noreply; her commit'ten sonra systemd birimi push eder. Yedek: ön-yeniden-yazım bundle'ı oturum scratchpad'inde, refs/original yerelde. Kanıt: git log %ae → yalnız noreply; gh api commits → 58 noreply; gh repo view → PUBLIC; kapanış commit'i otomatik push ile gitti (push.log).
- T-025 (2026-10-07): Kapanış kaydı artık engelle sağlanıyor: kontrol.py 16. denetim eski hâlde 2 hata verdi (nerede-kaldik T-024 yok, aktif_talimat yanlış), düzeltmeden sonra 0. Kanıt: kontrol.py --kisa önce → 1 (2 hata), sonra → 0.
- T-024 (2026-10-07): .obsidian dar istisna (K-005), git dışı. Kanıt: `git check-ignore .obsidian/app.json` → 0; `kontrol.py --kisa` → 0 (40 sayfa, 47 bağ). Commit 8451ee2.
- T-017..T-023 kayıtları: TALIMATLAR.md kapanış notları ve GUNLUK [oturum] satırları (bu dosyaya o dönemde yazılmadı; 2026-10-07 eksik analizi).

## Eski kayıtlar
### T-005 (2026-10-06)
- [x] calistir.sh --bare · durus-kapisi dosya izi · yikici-koruma 35 test · MALIYET transcript · şema belirlenmedi · gunluk.py · git
- Değişen: bkz. DEGISIKLIKLER 0.2.0; commit 20bc76d sonrası

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
