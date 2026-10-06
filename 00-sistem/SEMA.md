---
id: 20261006-2101-sema
ad: sema
tur: referans
kat: 0
surum: 0.3
durum: aktif
amac: Her sayfanin frontmatter alanlarini, turlerini, durum degerlerini, bag turlerini, adlandirma ve saklama kurallarini tek yerde tam olarak tanimlar; kontrol.py bu dosyaya gore denetler.
olusturma: 2026-10-06
guncelleme: 2026-10-07
yazar: claude
talimat: T-000
dayandigi: [00-sistem/SISTEM.md, 00-sistem/arastirma/02-hafiza-ve-wiki-duzenleri.md, 00-sistem/arastirma/01-claude-code-mekanikleri.md]
besledigi: [00-sistem/sema/sayfa.schema.json, 00-sistem/scripts/kontrol.py, 00-sistem/sablonlar/parca.md]
saklama: S
---

# Şema — alanlar, türler, durumlar, bağlar, adlandırma, saklama

Bu dosya CLAUDE.md tarafından `@00-sistem/SEMA.md` ile içe alınır. Kural: sayfa "SEMA'ya uymuyorsa" kontrol.py hata verir ve talimat kapanmaz. Makine okur biçimi `sema/sayfa.schema.json`'dadır; iki dosya birbirinden sapamaz (kontrol.py karşılaştırır).

## 1. Frontmatter alanları

Her Markdown sayfası `---` ile açılan YAML frontmatter taşır. Alan adları ASCII, küçük harf, alt çizgi.

### 1.1 Her sayfada zorunlu
| Alan | Tip | Değer | Açıklama |
| --- | --- | --- | --- |
| `id` | string | `YYYYMMDD-HHMM-<slug>` | Değişmez kimlik. Dosya adı değişebilir, id değişmez. Zettelkasten zaman damgası. |
| `ad` | string | ASCII slug | Dosya adının uzantısız hali (numara öneki hariç olabilir). |
| `tur` | enum | bkz. §2 | Sayfanın türü. Klasörle uyuşmalı (§4). |
| `kat` | int | 0, 1, 2, 3, 4, 9 | 0 sistem/gelen, 1 insan, 2 şirket, 3 devlet, 4 iç ses, 9 arşiv. Klasörle uyuşmalı. |
| `surum` | string | `0.1`, `0.2`, … `1.0` | 0.1 ile doğar; her değişiklikte +0.1; `kabul`te 1.0. |
| `durum` | enum | bkz. §3 | Yaşam döngüsü durumu. |
| `amac` | string | tek cümle | "Bu sayfa … için var." Gövdedeki Amaç başlığı ile aynı. |
| `olusturma` | date | `YYYY-MM-DD` | ISO 8601. |
| `yazar` | enum | `claude`, `kaan`, `<rol-adi>`, `hook` | Kimin yazdığı. |
| `talimat` | string | `T-xxx` | Sayfayı doğuran talimat. TALIMATLAR.md'de bulunmalı. |
| `dayandigi` | list[path] | `[yol.md, …]` | Bu sayfanın dayandığı sayfalar (yol, uzantılı). Boş liste olabilir. |
| `besledigi` | list[path] | `[yol.md, …]` | Bu sayfaya dayanan sayfalar. Boş liste olabilir. İki yönlülük §5. |

### 1.2 Koşullu zorunlu (türe göre)
| Alan | Tip | Zorunlu olduğu türler | Açıklama |
| --- | --- | --- | --- |
| `guncelleme` | date | durum ≠ taslak olan her sayfa | Son içerik değişikliği. |
| `ust` | path | kat 1-4'teki her sayfa (MOC hariç) | Tek üst MOC: `40-ic-ses/MOC-ic-ses.md` vb. |
| `kaynaklar` | list[string] | gozlem, kaynak, yansima, arastirma-notu, alan-paketi | URL ya da dosya yolu; web kaynağı için `alindi` de zorunlu. |
| `alindi` | date | `kaynaklar` içinde http(s) URL olan her sayfa | Web'den alınma tarihi; 90 günden eskisi TAZELIK uyarısı. |
| `guven` | enum | fikir, kaynak, yansima, arastirma-notu, alan-paketi | `dusuk`, `orta`, `yuksek`. |
| `onem` | int 1-10 | gozlem, yansima | Generative Agents önem puanı; yansıma eşiği hesabında kullanılır. |
| `merdiven` | int 0-5 | fikir | Olgunluk basamağı. |
| `cynefin` | enum | fikir (merdiven ≥ 1) | `acik`, `karmasik`, `kompleks`, `kaotik`, `karisik`, `belirlenmedi`. |
| `kapi` | enum | karar, kural, kapi, gorev | `tek-yonlu`, `cift-yonlu`, `belirlenmedi`. `belirlenmedi` yalnız `taslak` sayfada ve M4 öncesi fikirde geçerlidir (kontrol.py). |
| `karar_veren` | string | karar, kural, kapi | Tek kişi/rol (DACI tek Approver). |
| `sunset` | date | kural, yonerge | Gözden geçirme/son geçerlilik tarihi (varsayılan +90 gün). |
| `dayanak` | path | yonerge | Dayandığı kural. |
| `sahip` | string | gorev, rol, sop | Tek sahip (RACI tek A). |
| `inceleyici` | string | gorev | Sahipten farklı. |
| `kanit` | list[object] | gorev | `{komut, cikis, ozet}`; `durum: tamam` için boş olamaz. |
| `insan_noktalari` | list[object] | gorev, sop, alan-paketi | `{id, tur, kosul, kanit, bekleyen_adim}`. |
| `bekci` | string | kapi | Tek bekçi. |
| `sonuc` | enum | kapi, arastirma-notu | kapı: `bekliyor`, `go`, `kill`, `hold`, `recycle`; araştırma notu: `dogruluyor`, `celisiyor`, `bilinmiyor`; ikisinde de `belirlenmedi`. Kapı kaydında karar çıkana kadar `bekliyor` kullanılır. |
| `saklama` | enum | kat 3 sayfaları, kaynak, cikti | `S` sürekli, `K` kurum (plan dönemi + denetim), `B` birim (görev + 1 çevrim), `I` imha adayı. |

### 1.3 İsteğe bağlı
| Alan | Tip | Açıklama |
| --- | --- | --- |
| `son_gozden_gecirme` | date | Bayatlık ölçümü için; 60 günü aşınca uyarı. |
| `yerine_gecti` | path | Bu sayfa hangi sayfanın yerine geçti (supersede). |
| `yerine_gecen` | path | Bu sayfanın yerine hangi sayfa geçti; `durum: yerine-gecildi` ile birlikte. Simetrik olmalı. |
| `gecerli_baslangic`, `gecerli_bitis` | date | Çift zamanlı geçerlilik (Zep). Çelişkide eskiye `gecerli_bitis` yazılır, silinmez. |
| `etiketler` | list[string] | Kesen boyutlar: `proje/x`, `alan/3d`, `oncelik/yuksek`. Tür ve kat için etiket kullanma (alanlar var). |
| `takma_adlar` | list[string] | Aynı sayfanın diğer adları (Obsidian aliases). |
| `oldurme_tarihi`, `oldurme_nedeni` | date, string | Öldürülen fikir için. |
| `dokunus_sayisi`, `son_dokunus` | int, date | Fikir için; yaşa değil referansa göre tutma. |
| `islendi`, `islenme_tarihi`, `sonuc_yol` | bool, date, path | 01-gelen notları için. |

## 2. Türler (`tur`)
| Tür | Kat | Klasör | Ne |
| --- | --- | --- | --- |
| `gozlem` | 4 | 40-ic-ses/gozlemler | Epizodik, tarihli ham olgu |
| `fikir` | 4 | 40-ic-ses/fikirler | Olgunlaşan fikir (merdiven 0-5) |
| `yansima` | 4 | 40-ic-ses/yansimalar | ≥ 2 sayfaya kanıt atıflı sentez |
| `kavram` | 4 | 40-ic-ses/kavramlar | Evergreen kavram notu |
| `arastirma-notu` | 4 | 40-ic-ses/arastirma-notlari | Park listesinden çıkan sonuç |
| `karar` | 3 | 30-devlet/kararlar | MADR-mini karar kaydı |
| `kural` | 3 | 30-devlet/normlar/kurallar | Kanun/CBK analoğu |
| `yonerge` | 3 | 30-devlet/normlar/yonergeler | Yönetmelik analoğu |
| `kapi` | 3 | 30-devlet/kapilar | Onay kapısı kaydı |
| `bulgu` | 3 | 30-devlet/denetim/bulgular | Denetim bulgusu |
| `eylem-plani` | 3 | 30-devlet/denetim/eylem-planlari | Bulguya eylem planı |
| `gorev` | 2 | 20-sirket/gorevler | Görev kartı |
| `rol` | 2 | 20-sirket/roller | Rol kartı |
| `sop` | 2 | 20-sirket/sop | Standart iş prosedürü |
| `alan-paketi` | 2 | 20-sirket/alan-paketleri | Bir alanın tüm bilgisi |
| `cikti` | 1 | 10-insan/ciktilar | Yapılan işin sayfası |
| `kaynak` | 1 veya 0 | 10-insan/kaynaklar, 00-sistem/arastirma | Değişmez kaynak / araştırma raporu |
| `referans` | 0, 1, 2, 3 | kök dosyalar (SISTEM, SEMA, IMZA-MATRISI, MODEL-POLITIKASI, HAKEM-KURALLARI, ARAC-KAYDI, SCORECARD, RITIM) | Dışarıya ya da içeriye işaretçi/başvuru sayfası |
| `anayasa` | 3 | 30-devlet/normlar | Tek dosya |
| `moc` | 1-4 | her kat kökü | İçerik haritası |
| `ham` | 0 | 01-gelen | Gelen kutusu notu |

## 3. Durumlar (`durum`)
`taslak` → `aktif` (ya da karar/kural için `onerildi` → `kabul`) → `yerine-gecildi` | `reddedildi` | `arsiv`. Görev kartı ayrıca Kanban durumunu `kanban` alanında tutar: `bekliyor`, `basladi`, `fiziksel-adim-bekliyor`, `kontrol`, `tamam`, `iptal`. Talimat durumu TALIMATLAR.md'de: `acik`, `bekliyor`, `kapali`.

## 4. Kat ↔ klasör uyumu
Klasör öneki katı belirler: `00-`, `01-` → 0; `10-` → 1; `20-` → 2; `30-` → 3; `40-` → 4; `90-` → 9. Uyumsuzluk hata. Tür §2'deki klasöre uymalı; `kaynak` iki yerde olabilir; `referans` kök dosyalarda.

## 5. Bağlar
- Yalnız wikilink: `[[00-sistem/SEMA]]` (uzantısız yol, kökten). Dış kaynak düz URL.
- Gövdede her bağ nedenlidir: `[[hedef]] — neden`. Bağlar bölümü üç alt başlık: Dayandığı, Beslediği, Gelen.
- İki yönlülük: A.dayandigi ∋ B ⇔ B.besledigi ∋ A. Tek yönlü bağ hatadır (kontrol.py "tek yönlü bağ").
- Frontmatter'da yol uzantılı yazılır (`yol/dosya.md`), gövdede wikilink uzantısız.
- Frontmatter'sız sistem dosyalarına (CLAUDE.md, .claude/*, *.json, *.py, *.sh, *.csv) `besledigi` ile işaret edilebilir; onlar için karşılıklılık aranmaz, yalnız varlık.
- `ust`: kat 1-4 sayfalarında tek MOC. MOC, altındaki her sayfayı en az bir satırla listeler.

## 6. Adlandırma
- ASCII kebab-case; Türkçe karakter dönüşümü: ş→s, ı→i, ğ→g, ü→u, ö→o, ç→c, İ→i.
- Numaralı türler: `F-0001-slug.md` (fikir), `K-001-slug.md` (karar), `KR-001-slug.md` (kural), `Y-001-slug.md` (yönerge), `KP-001-slug.md` (kapı), `G-001-slug.md` (görev), `B-001-slug.md` (bulgu), `SOP-001-slug.md`, `R-slug.md` (rol).
- Üst düzey sistem dosyaları BÜYÜK HARF: SISTEM, SEMA, HARITA, GUNLUK, ILERLEME, TALIMATLAR, KARARLAR, DEGISIKLIKLER, ASK, MALIYET, ANAYASA, IMZA-MATRISI, MODEL-POLITIKASI, HAKEM-KURALLARI, ARAC-KAYDI, SCORECARD, RITIM.
- MOC dosyaları `MOC-<kat>.md`.

## 7. Gövde yapısı (her sayfa)
```
# Başlık
## Amaç          (frontmatter amac ile aynı cümle)
## İçerik        (türe göre alt başlıklar; şablon belirler)
## Bağlar        (Dayandığı / Beslediği / Gelen; her satır "[[yol]] — neden")
## Günlük        (| Sürüm | Tarih | Talimat | Değişiklik |)
```

## 8. Günlük biçimleri
- Sayfa günlüğü: tablo satırı `sürüm · tarih · T-xxx · ne değişti (eski değer parantezde)`.
- GUNLUK.md: `YYYY-MM-DD HH:MM [tur] yol — not`; türler: yeni, degisti, arsiv, karar, kapi, hata, durdu, ayar, oturum, uyku.
- HARITA.md: `- [[yol]] — amaç · tur · kat N · YYYY-MM-DD`.
- DEGISIKLIKLER.md: keep-a-changelog; Eklendi / Değişti / Kaldırıldı / Düzeltildi; semver.

## 9. Saklama kodları (`saklama`)
Devlet Arşivleri ve ISO 15489'dan uyarlandı: `S` sürekli (anayasa, kurallar, kararlar, kapı sonuçları, denetim raporları, eylem planları, yönergeler); `K` kurum (görev kartları ve talimatlar: plan dönemi + denetim kapanana kadar); `B` birim (taslaklar, gözlemler: görev + 1 çevrim, sonra arşiv); `I` imha adayı (geçici loglar; fiziksel silme yalnız sahibinin imzasıyla). Hiçbir sayfa silinmez; arşive düşer.

## 10. Boyut sınırları (kontrol.py denetler)
CLAUDE.md ≤ 200 satır; her SKILL.md ≤ 500 satır; HARITA.md ≤ 200 sayfa satırı (aşınca MOC bölme); ajan→orkestratör rapor ≤ 2.000 token (kural, ölçülmez); Onay Dosyası ≤ yarım sayfa (~250 kelime).

## 11. Kontrol listesi (kontrol.py'nin 13 denetimi)
1 frontmatter var/ayrıştırılır, zorunlu alanlar türe göre tam, enum geçerli, tarih ISO · 2 id tekil · 3 kat ↔ klasör, tür ↔ klasör · 4 HARITA'da tek satır (arşiv ve şablon hariç) · 5 kırık bağ (dayandigi/besledigi/ust hedefi yok) · 6 tek yönlü bağ · 7 `ust` var ve MOC · 8 GUNLUK kaydı var · 9 `talimat` TALIMATLAR'da var; durum ≠ taslak ise talimat kapalı ya da bekliyor · 10 ADR simetrisi (yerine_gecti/yerine_gecen) · 11 bayat (son_gozden_gecirme > 60, alindi > 90, gecerli_bitis geçmiş ama durum aktif) · 12 boyutlar (§10) · 13 kanıtsız tamam (gorev kanban=tamam ve kanit boş).

## Bağlar
- Dayandığı: [[00-sistem/SISTEM]] — klasör ve kat yapısı buradan; [[00-sistem/arastirma/02-hafiza-ve-wiki-duzenleri]] — frontmatter, tür taksonomisi, lint listesi; [[00-sistem/arastirma/01-claude-code-mekanikleri]] — CLAUDE.md ve SKILL.md boyut sınırları
- Beslediği: [[00-sistem/sema/sayfa.schema.json]] — makine okur karşılığı; [[00-sistem/scripts/kontrol.py]] — denetimler bu tanıma göre; [[00-sistem/sablonlar/parca]] — genel şablon bu alanları taşır

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
| 0.2 | 2026-10-06 | T-005 | kapi ve sonuc enum'larına `belirlenmedi` eklendi (eski: yalnız karar değerleri); cynefin satırı şemayla eşitlendi; belirlenmedi'nin taslak sınırı yazıldı |
| 0.3 | 2026-10-07 | T-010 | sonuc enum'una araştırma notu değerleri (dogruluyor, celisiyor, bilinmiyor) eklendi; şablon bunları öneriyordu, şema reddediyordu |
