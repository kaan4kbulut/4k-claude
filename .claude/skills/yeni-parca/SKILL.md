---
name: yeni-parca
description: 4k-claude'a yeni bir sayfa (gözlem, fikir, karar, görev, kural, kaynak vb.) eklerken kullan. Bir parçanın doğuşunun altı adımını sırayla yürütür ve kontrol.py ile kapatır. Sahibi "not al", "kaydet", "yeni görev aç", "karar yaz" gibi bir şey istediğinde proaktif olarak kullan.
argument-hint: [tur] [kat] [baslik]
---

# /yeni-parca — bir parçanın doğuşu

Sistemin en küçük birimi. Altı adım, sıra değişmez, hiçbiri atlanmaz. Her adımda hangi adımda olduğunu tek satırla söyle: `ADIM 3/6 · YER + AD`.

Argümanlar: `$0` tür (gozlem|fikir|yansima|kavram|karar|kural|yonerge|kapi|gorev|rol|sop|alan-paketi|cikti|kaynak|referans|moc|bulgu), `$1` kat (0-4), `$2` başlık. Eksikse sor; kat belirsizse dosya açma.

Güncel durum:
!`python3 00-sistem/scripts/kontrol.py --kisa 2>&1 | tail -5`

## ADIM 1/6 · KAYIT
1. `00-sistem/TALIMATLAR.md` son numarayı bul, bir sonrakini ver (T-xxx).
2. `00-sistem/sablonlar/talimat.md` bloğunu doldur: tarih, niyet (ne, neden), başarı ölçütü (nasıl bittiği anlaşılır), sınırlar (yapılmayacaklar), kat, kapı türü (tek-yonlu | cift-yonlu), durum `acik`.
3. Belirsizlik varsa en çok üç soru sor; cevap gelmeden 2. adıma geçme. Soru bir kapı gerektiriyorsa `/kapi`.
4. Sahibinin isteği zaten açık bir talimata aitse yeni numara verme; o talimatı kullan.

## ADIM 2/6 · AMAÇ + KAT
1. Amaç tek cümle: "Bu sayfa … için var." Sayfanın `amac` alanı bu cümledir.
2. Kat: 4 zihin (gözlem/fikir/yansıma/kavram/araştırma-notu), 3 irade (karar/kural/yönerge/kapı/bulgu), 2 örgütleme (görev/rol/SOP/alan paketi), 1 eller (çıktı/kaynak/referans), 0 sistem (şema/şablon/betik/kaynak rapor).
3. Tür ile kat uyuşmuyorsa (ör. görev kat 4) dur, sor. Kat belirsizse dosya açma.
4. Bu sayfanın ait olacağı MOC'u belirle (`ust`): `40-ic-ses/MOC-ic-ses`, `30-devlet/MOC-devlet`, `20-sirket/MOC-sirket`, `10-insan/MOC-insan`; kat 0 için `ust` boş kalabilir.

## ADIM 3/6 · YER + AD
1. Klasör = kat klasörü + tür alt klasörü (ör. `40-ic-ses/fikirler/`, `30-devlet/kararlar/`, `20-sirket/gorevler/`, `10-insan/kaynaklar/`).
2. Ad = numara (varsa) + ASCII kebab-case başlık: `F-0003-yazici-isi-fikri.md`. Türkçe karakterleri dönüştür.
3. `00-sistem/HARITA.md`'de aynı ad ya da aynı amaçta sayfa var mı bak (grep). Varsa yeni sayfa açma; `/degistir` ile o sayfayı güncelle ve sahibine söyle.
4. Kimlik: `id` = `YYYYMMDD-HHMM-<kisa-slug>`; bir daha değişmez.

## ADIM 4/6 · ŞABLON
1. `00-sistem/sablonlar/<tur>.md` dosyasını kopyala (parca.md genel iskelettir; tür şablonu onu genişletir).
2. Frontmatter'ın her alanını doldur. Boş alan bırakma; bilinmeyen için `belirlenmedi`. `dayandigi`/`besledigi` boş liste olabilir ama alan var olmalı.
3. `talimat: T-xxx`, `olusturma: YYYY-MM-DD`, `yazar: claude` (sahibi yazdırıyorsa `kaan`), `surum: 0.1`, `durum: taslak` (karar/kural için `onerildi`).
4. Gövde: Amaç (frontmatter ile aynı cümle), İçerik, Bağlar (dayandığı / beslediği / gelen), Günlük tablosu (ilk satır: 0.1 · tarih · T-xxx · Oluşturuldu).
5. Web'den gelen her olgu: URL + `alindi` tarihi + güven etiketi. Emin olmadığın şey UNCONFIRMED.

## ADIM 5/6 · BAĞLAR
1. Bu sayfanın dayandığı sayfaları `dayandigi` listesine yaz; gövdede her birini `[[yol]] — neden` biçiminde gerekçele.
2. Her dayanılan sayfanın `besledigi` listesine bu sayfayı ekle ve o sayfanın "Bağlar / gelen" bölümüne `← [[bu-sayfa]] — aynı neden` satırı düş; o sayfanın `guncelleme` alanını bugüne çek (sürüm artmaz; bağ eklemek içerik değişikliği sayılmaz).
3. `ust` MOC'un ilgili bölümüne bu sayfayı tek satırla ekle.
4. Tek yönlü bağ bırakma; kontrol.py "tek yönlü bağ" hatasıyla yakalar.

## ADIM 6/6 · KAPANIŞ
1. `00-sistem/HARITA.md`'ye satır: `- [[yol]] — amaç · tur · kat N · YYYY-MM-DD`. 200 satırı aşıyorsa harita.py MOC bölme önerir; öneriyi sahibine ilet, yine de satırı ekle.
2. `00-sistem/GUNLUK.md`'ye satır: `YYYY-MM-DD HH:MM [yeni] yol — tek satır not`.
3. TALIMATLAR.md'de T-xxx: `Doğurduğu dosyalar` ve `Kapanış notu` doldur, `Durum: kapali`. Talimat birden çok sayfa doğuruyorsa son sayfadan sonra kapat.
4. `python3 00-sistem/scripts/kontrol.py --kisa` çalıştır. Hata varsa talimat kapanmaz; düzelt, tekrar çalıştır. İki denemede çözülmezse GUNLUK'e `[durdu]` yaz ve sahibine sor.
5. Çıktıyı `## Kanıt` bloğunda ver: oluşturulan dosya yolu, kontrol.py komutu ve çıkış kodu, HARITA satırı.

## Değişiklik için
Var olan sayfayı değiştirmek bu skill'in işi değildir; `/degistir` kullan (sürüm artar, iki günlüğe satır).
