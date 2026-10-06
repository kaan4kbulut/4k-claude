---
id: 20261006-2203-hakem-kurallari
ad: hakem-kurallari
tur: referans
kat: 3
surum: 0.1
durum: aktif
amac: Bir modelin baska bir modelin ciktisini yargiladigi her yerde (denetci, kapi yargisi, eval) onyargilari azaltan kurallari koyar.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: kaan
talimat: T-000
dayandigi: [30-devlet/normlar/ANAYASA.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md]
besledigi: []
kaynaklar: ["https://arxiv.org/abs/2410.02736", "https://arxiv.org/abs/2310.01798", "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"]
alindi: 2026-10-06
saklama: S
etiketler: [norm/denetim]
---

# Hakem kuralları

LLM-hakem onyargıları (konum, uzunluk, kendini beğenme, otorite, duygu, "iyileştirildi" etiketi…) ve "dış geri bildirimsiz öz-düzeltme güvenilir değildir" bulgusuna dayanır. Anayasa Madde 4 (kanıt) ve Madde 8 (denetim) uygulamasıdır.

## Amaç
Bir modelin başka bir modelin çıktısını yargıladığı her yerde (denetci, kapı yargısı, eval) önyargıları azaltan kuralları koyar.

## İçerik
1. **Dış kontrol önce.** Çalıştırılabilir bir kontrol varsa (test, kontrol.py, derleme, diff) hakem ondan sonra gelir; hakem dış kontrolün yerini tutmaz.
2. **Temiz bağlam.** Hakem, üreticinin akıl yürütmesini görmez; yalnız çıktıyı ve ölçütü görür (denetci: diff + kart).
3. **Farklı model ya da en azından farklı örnek.** Hakem, üreticiyle aynı modelse farklı bir örnek ve temiz bağlamla; mümkünse farklı model ailesi.
4. **Kısa çıktıda ikili yargı.** PASS / FAIL / BİLİNMİYOR; uzun artefaktları regex, dosya varlığı, komut çıkışı ile puanla, hakemle değil.
5. **"Bilinmiyor" geçerli cevap.** Zorlama karar istenmez; bilinmiyor → sahibine soru (ASK).
6. **Sıra karıştır.** İki çıktı karşılaştırılıyorsa sıra rastgele; konum önyargısı.
7. **Uzunluk ödül değil.** Daha uzun cevap daha iyi sayılmaz; ölçüt karşılanıyor mu.
8. **Etiket verme.** Çıktının "iyileştirilmiş", "uzman tarafından yazılmış" gibi etiketleri hakeme gösterilmez.
9. **Üç oy.** Kapı yargısı gibi yüksek riskli kararlarda 3 bağımsız Haiku oyu; oybirliği yoksa karar hakemde değil sahibinde (ASK).
10. **Boşluk avcılığı yok.** Hakem yalnız doğruluk ve gereksinim boşluğu raporlar; stil tercihi "öneri" sınıfıdır ve kapanışı durdurmaz.
11. **Kalibrasyon.** Hakem kararları ile sahibinin sonradan verdiği kararlar aylık karşılaştırılır (uyku aylık); sapma sistematikse kurallar güncellenir.
12. **Rubrik yazılı.** Hakem ölçütü kartta ya da kapı kaydında önceden yazılıdır; sonradan uydurulmaz.

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 4 ve 8
- [[00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri]] — hakem onyargıları, öz-düzeltme sınırı, eval tasarımı
### Beslediği
### Gelen
- ← [[30-devlet/normlar/ANAYASA]] — Madde 8 ve 4'ün uygulaması

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
