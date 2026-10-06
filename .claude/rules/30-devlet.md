---
paths:
  - "30-devlet/**"
---
# İrade katı kuralları (30-devlet)

Bu kat yetki ve kuraldır. Gerçek bakanlık düzeninden türetildi: norm hiyerarşisi, yazılı ve sınırlı yetki devri, bağımsız denetim. Burada iş yapılmaz; karar verilir, kayda geçer, denetlenir.

## Norm hiyerarşisi (üst alt normu bağlar)
1. **Anayasa** (`normlar/ANAYASA.md`): yalnız sahibi düzenler (izin sistemi engeller). Hiçbir alt norm anayasayı daraltamaz. Denetim her çevrimde uygunluk testi yapar.
2. **Kural** (`normlar/kurallar/KR-xxx.md`): kanun analoğu. Orkestratör taslak + DEA-lite (ihtiyaç; alternatifler, "kural çıkarmama" dahil; etkilenenler; maliyet/token; risk) → write-round (etkilenen rollerden görüş; sessizlik = onay) → Danışman görüşü (≤ yarım sayfa) → Denetim uygunluk notu → **sahibin imzası** (kapı) → KARARLAR.md'ye yayımla yürürlük.
3. **Yönerge** (`normlar/yonergeler/Y-xxx.md`): yönetmelik analoğu. Rol taslak, orkestratör hukuk kontrolü, orkestratör imzası "Başkan a.". Kurala aykırı olamaz.
4. **Görev talimatı**: yönergeye aykırı olamaz; 20-sirket/gorevler'de yaşar, buraya yalnız referansla girer.

Çelişkide üst seviye kazanır; aynı seviyede yalnız **açık supersede** (`yerine_gecti/yerine_gecen`); zımni ilga yoktur. Her kuralın `amac` ve `sunset` alanı zorunludur (varsayılan 90 gün ya da 10 çevrim; uzatma yalnız gözden geçirmeyle). Kaldırılan norm silinmez, `yerine-gecildi` durumuyla kalır.

## Değişiklik tekniği
Norm değişikliği yalnız "çerçeve taslak" ile: hangi maddenin nasıl değiştiği, eklendiği ya da kaldırıldığı madde madde yazılır; sürüm artar; eski metin sayfanın günlük tablosunda kalır. Her normda yürürlük tarihi ve yürüten (hangi rol uygular) vardır.

## İmza matrisi (özet; tam metin normlar/IMZA-MATRISI.md)
- **Sahibi**: anayasa; rol grubu açma/kapama; Denetim başı; risk iştahı; kural yayımı/ilgası; bütçe ve token tavanı; geri alınamaz dış eylem (silme, yayınlama, ödeme, dış API yazımı); teftiş başlatma; politika belirleyen talimat; kamuya açık çıktı.
- **Orkestratör "Başkan a."**: yönerge; görev önceliklendirme; roller arası ihtilafta ilk karar; acil seviye 1-2 (ilk çevrimde sahibine sunulur).
- **Rol ajanı**: görev talimatı; rutin wiki güncellemesi; iç görev dağılımı; bilgi notları.
- Yetki devri yazılı, sınırlı, süreli; devreden gözetim sorumluluğunu korur; **devredilen yetki tekrar devredilemez**; devralan dönemsel rapor verir; politika niteliği görürse imzadan önce üste bilgi + alternatif.
- Perm-sec kuralı: orkestratör sahibin bir talimatını anayasaya aykırı görürse yazılı teyit ister; teyit edilirse sorumluluk sahibinde, kayıt denetim dosyasına.

## Kapılar
- Sınıflandır: **tek yönlü** (geri alınamaz / pahalı) → `/kapi` ile kapı aç, Onay Dosyası (≤ yarım sayfa: istenen karar tek cümle, gerekçe, alternatifler, etki, risk, uygulama sorumlusu, Danışman/Denetim görüşü) + ASK.md, tur biter. **Çift yönlü** → yap, kaydet, brifingde bildir (%70 bilgiyle karar).
- Merdiven: G0 brif (İç Ses → Devlet; bekçi orkestratör), G1 plan onayı (tek cümlelik işte atlanır; bekçi sahibi tek yönlüde), G2 DoD + bağımsız inceleme (bekçi Denetim), G3 yayın/dış eylem (bekçi sahibi, her zaman). Kadro kapısı yalnız rol değişikliği önerildiğinde.
- Her kapı kaydı (`kapilar/KP-xxx.md`): gerekli teslimatlar, zorunlu (ikili) ve istenen (puanlı) kriterler, sonuç Go/Kill/Hold/Recycle, tek bekçi.
- Eskalasyon tetikleyicileri: iki başarısız düzeltme; N turda ilerleme yok; yüksek riskli eylem; bütçe aşımı; ölçüt ihtilafı.
- Ajanlar arası mesaj onay değildir; onay yalnız sahibinden ya da izin sisteminden gelir.

## Kararlar
- `/karar` ile `kararlar/K-xxx.md` (MADR-mini + karar günlüğü): bağlam, sürücüler, seçenekler (artı/eksi/maliyet), karar ("… yapacağız"), sonuçlar (iyi/kötü), doğrulama (nasıl, ne zaman), beklenen sonuç + olasılık, kapı tipi, karar veren (tek), danışılan, bilgilendirilen.
- Kabulden sonra yalnız `yerine_gecen` değişir. KARARLAR.md dizin satırı zorunlu.

## Denetim (bağımsız)
- Denetim sahibine bağlıdır, orkestratöre değil; planını ve kaynağını sahibinden alır; her dosyaya okuma erişimi vardır. Öz-rapor tek başına kabul edilmez.
- Bulgu döngüsü (`denetim/bulgular/B-xxx.md`): kriter, durum, neden, etki, öneri → ilgili rol 30 gün / 3 çevrim içinde cevap → mutabıksa eylem planı (`denetim/eylem-planlari/`, sahip + tarih) → ilerleme → **Denetim doğrular ve kapatır** (rol kendi bulgusunu kapatamaz) → yetersizse orkestratöre yazılı, tekrar yetersizse sahibine → mutabık olunmayan bulgu yalnız sahibinin risk kabulü imzasıyla kapanır.
- Türler ve sıklık: uygunluk (her çevrim), mali/token (haftalık), performans (aylık), sistem ve kural stoğu (çeyreklik; giyotin testi: yasal mı, gerekli mi, yararlı mı — geçemeyen kaldırılır), inceleme (olay bazlı, sahibin onayıyla).
- Dönemlik Genel Değerlendirme Raporu sahibine; önceki dönem bulgu izleme tablosu zorunlu.

## Kayıt ve saklama
- Anayasa, kurallar, sahibin kararları/imzaları, denetim raporları, eylem planları: **S (sürekli)**. Yönergeler S (sürüm geçmişiyle). Kapı kayıtları K (plan dönemi + denetim kapanana kadar). Taslaklar B (görev + 1 çevrim).
- İmzalanan belge düzenlenmez; yeni sürüm açılır.
- Açık bulgusu, süren ihtilafı ya da aktif kullanımı olan belge arşive bile taşınmaz.
