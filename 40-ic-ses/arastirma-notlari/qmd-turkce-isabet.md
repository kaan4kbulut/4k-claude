---
id: 20261007-0041-qmd-turkce-isabet
ad: qmd-turkce-isabet
tur: arastirma-notu
kat: 4
surum: 0.1
durum: aktif
amac: Bu arastirma notu, arastirma 10'un "qmd yerel aramanin Turkce isabeti olculmeli" sorusuna dogruluyor cevabini 20 sorguluk olcumle verir.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-010
dayandigi: [00-sistem/arastirma/10-yenilikci-teknolojiler.md]
besledigi: []
ust: 40-ic-ses/MOC-ic-ses.md
kaynaklar: ["https://github.com/tobi/qmd", "00-sistem/scripts/ara-olcum.py", "00-sistem/scripts/ara.py"]
alindi: 2026-10-07
guven: orta
sonuc: dogruluyor
etiketler: [arac/qmd, arama]
---

# Araştırma notu: qmd Türkçe wikide işe yarıyor mu?

## Amaç
Bu araştırma notu, araştırma 10'un "qmd yerel aramanın Türkçe isabeti ölçülmeli" sorusuna doğruluyor cevabını 20 sorguluk ölçümle verir.

## İçerik
### Soru
Araştırma 10 öncelik 3: qmd (yerel BM25 + vektör + yeniden sıralama) bu wikide Türkçe sorgularla doğru sayfayı buluyor mu? Hangi kip ve hangi gömme modeli?

### Sonuç
sonuc: dogruluyor · güven: orta · **Anlamsal (vektör) arama Türkçe çalışıyor (isabet@3 %90); kelime araması Türkçe cümlede hiç çalışmıyor; Qwen3'ün varsayılan modele üstünlüğü bu küçük kümede ölçülemedi.**

### Kanıt
Ölçüm: `python3 00-sistem/scripts/ara-olcum.py` → çıkış 0. 20 sorgu; sorgular sayfa başlığını kopyalamaz, çekimli günlük Türkçeyle sorulur. 36 sayfalık dizin (`ara.py --yenile`), qmd 2.8.3, RTX 5070 Ti.

| Kurulum | Kip | isabet@1 | isabet@3 | sn/sorgu |
| --- | --- | --- | --- | --- |
| embeddinggemma-300M, günlükler dizinde | vektör | %70 | %85 | (ilk çalıştırma, ölçülmedi) |
| embeddinggemma-300M, günlükler dizinde | hibrit | %60 | %85 | (model indirme dahil) |
| Qwen3-Embedding-0.6B, günlükler dizinde | vektör | %65 | %85 | 5.3 |
| **Qwen3-Embedding-0.6B, günlüksüz** | **vektör** | **%75** | **%90** | **4.5** |
| Qwen3-Embedding-0.6B, günlüksüz | hibrit | %50 | %90 | 7.5 |
| her ikisi | kelime (BM25) | %0 | %0 (20/20 boş) | 0.1 |

Sandbox içinde gerçek oturumda: `ara.py 'imza yetkisini kim devredebilir' -n 2 --files` → çıkış 0, ilk sonuç IMZA-MATRISI (oturum 9 sn, 0.046 USD).

### Bulgular
1. **Kelime araması (BM25) Türkçe eklerde çöker.** "fiyat" bulunur, "fiyatları" bulunmaz; cümle sorgularının tamamı boş. Yalnız tek terim ya da özel ad için (`--kelime`).
2. **Günlük dosyaları sonuçları kirletir.** TALIMATLAR, GUNLUK, DEGISIKLIKLER her şeyden bahsettiği için ilk sırayı kapıyordu; dizinden çıkarılınca isabet@3 %85 → %90, isabet@1 %65 → %75.
3. **Hibrit kip bu wikide kötü.** Sorgu genişletme modeli Türkçe sorguyu İngilizce "hyde" cümlelerine çeviriyor; ilk sıra isabeti %50'ye düşüyor ve süre 1.7 kat. Varsayılan kip vektör yapıldı.
4. **Qwen3 vs embeddinggemma: fark gürültü düzeyinde** (20 sorguda ±1). Araştırma 10'un "Türkçe için Qwen3 gerekir" önerisi bu ölçümle ne doğrulandı ne çürütüldü; Qwen3 tutuldu (günlüksüz ölçümde en iyi sonuç ve daha uzun bağlam).
5. **Kalan iki kaçırma terim farkı:** "kancalar/beceriler" (belgede hook/skill), "kabuk komutları … kısıtlama" (belgede Bash sandbox). Türkçe-İngilizce karışık terimli wikide beklenen sınır.

### Çelişen kaynaklar
- Araştırma 10: qmd'nin "BM25 + vektör + reranker" hibrit yolunu öne çıkarıyor; bu wikide hibrit, vektörden kötü çıktı.

### Fikre etkisi (delta)
- Karar: `ara.py` varsayılanı vektör; `--hibrit` ve `--kelime` seçenek. MCP sunucusu (.mcp.json) **eklenmedi**: 30 sayfada HARITA-önce yeterli, CLI 4.5 sn kabul edilebilir; MCP `query` aracının hangi kipi kullandığı doğrulanmadı (UNCONFIRMED).
- Yeniden ölçüm: HARITA 100 sayfayı geçince ya da sorgu kümesi 50'ye çıkınca; o zaman MCP yeniden değerlendirilir.
- Merdiven önerisi: değişmez (bu not bir araç ölçümüdür, fikir değil).

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/10-yenilikci-teknolojiler]] — öncelik 3 (qmd) ve "Türkçe isabet UNCONFIRMED, ölçülmeli" notu
### Beslediği
### Gelen
- ← [[40-ic-ses/MOC-ic-ses]] — araştırma notları listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-010 | Oluşturuldu (20 sorgu, 6 ölçüm) |
