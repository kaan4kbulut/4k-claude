# Değişmez kurallar (kapsamsız; her oturumda yüklenir, sıkıştırmadan sağ çıkar)

## Kanıt tanımı
Kanıt, çalıştırılmış bir dış kontrolün izidir: komut, çıkış kodu, çıktının ilgili özeti (en çok 20 satır). Şunlar kanıt değildir: "kontrol ettim", "tekrar okudum", "doğru görünüyor", bir alt ajanın "tamam" demesi. Dosya üretildiyse kanıt `ls -l` + ilk satırlar; betik yazıldıysa çalıştırma çıktısı; sayfa eklendiyse `kontrol.py --kisa` çıktısıdır.

## Talimat numaralama
- Biçim `T-001`, `T-002`… üç haneli, sıfır dolgulu; 999'dan sonra dört hane.
- Karar `K-001`, kapı `KP-001`, görev `G-001`, fikir `F-0001` (dört hane), bulgu `B-001`, kural `KR-001`, yönerge `Y-001`.
- Numara TALIMATLAR.md / KARARLAR.md / HARITA.md'deki son numaradan bir sonrakidir; boşluk bırakılmaz, yeniden kullanılmaz.

## Bağlantı kuralı
- Yalnız wikilink: `[[00-sistem/SEMA]]` (uzantısız yol). Harici kaynak için düz URL.
- Gövdedeki her bağ nedenlidir: `[[hedef]] — <neden>`. Nedensiz bağ eksiktir.
- `dayandigi` ve `besledigi` iki yönlü tutulur: A.dayandigi ⊇ {B} ⇔ B.besledigi ⊇ {A}. Ters satır hedef sayfanın "Bağlar / gelen" bölümüne de yazılır.
- Kat sayfasının `ust` alanı o katın MOC'udur (örn. `40-ic-ses/MOC-ic-ses`).

## Adlandırma
- Dosya adları ASCII kebab-case: `yazici-isi-fikri.md`. Türkçe karakterler dönüştürülür (ş→s, ı→i, ğ→g, ü→u, ö→o, ç→c).
- Kimlikli sayfalar numara ile başlar: `F-0001-yazici-isi-fikri.md`, `K-001-...`, `G-001-...`.
- Üst düzey sistem dosyaları BÜYÜK HARF: SISTEM, SEMA, HARITA, GUNLUK, ILERLEME, TALIMATLAR, KARARLAR, DEGISIKLIKLER, ASK, MALIYET.

## Günlük satır biçimi
`YYYY-MM-DD HH:MM [tur] yol — not`. Türler: yeni, degisti, arsiv, karar, kapi, hata, durdu, ayar, oturum, uyku. Satır tek satırdır; ayrıştırılabilir kalır. Satırı `python3 00-sistem/scripts/gunluk.py <tur> <yol> "<not>"` yazar: model saati bilmez, elle yazılan damga uydurmadır ve kontrol.py sıra dışı damgayı uyarır.

## Sürüm kuralı
- Sayfa sürümü `surum`: 0.1 ile doğar; her değişiklikte +0.1; durum `kabul` olunca 1.0; kabulden sonra yalnız `yerine_gecen` değişir.
- Sistem sürümü DEGISIKLIKLER.md'de semver: şema ya da kural değişikliği MINOR, şablon düzeltmesi PATCH, kat yapısı değişikliği MAJOR.

## Silme yasağı
Hiçbir sayfa silinmez. `durum: arsiv` ve `yerine_gecen` ile geçersiz kılınır, 90-arsiv'e taşınır, HARITA'dan düşer, GUNLUK'te kalır. Fiziksel silme yalnız sahibinin imzasıyla ve imha komisyonu kaydıyla (30-devlet/kararlar).

## Model ve bütçe
Alt ajan açmadan önce `30-devlet/normlar/MODEL-POLITIKASI.md`'ye bak: hangi iş hangi modele, tur ve bütçe tavanı nedir. Tek ajanla yapılabilen iş için alt ajan açma.
