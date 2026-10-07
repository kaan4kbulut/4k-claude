---
id: 20261007-1010-freyatts-turkce-deneme
ad: freyatts-turkce-deneme
tur: arastirma-notu
kat: 4
surum: 0.1
durum: aktif
amac: Bu arastirma notu, arastirma 10'un "yerel Turkce TTS kalitesi olculmeden bagimliliga cevrilmez" sartina FreyaTTS icin celisiyor cevabini (islemcide gercek zamanli degil; yabanci terimlerde zayif) olcumle verir.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-016
dayandigi: [00-sistem/arastirma/10-yenilikci-teknolojiler.md]
besledigi: []
ust: 40-ic-ses/MOC-ic-ses.md
kaynaklar: ["https://github.com/freyavoiceai/FreyaTTS", ".araclar/tts/ornek_uret.py", ".araclar/tts/anlasilirlik.py"]
alindi: 2026-10-07
guven: orta
sonuc: celisiyor
etiketler: [arac/tts, ses-hatti]
---

# Araştırma notu: FreyaTTS İç Ses için yerel Türkçe ses olur mu?

## Amaç
Bu araştırma notu, araştırma 10'un "yerel Türkçe TTS kalitesi ölçülmeden bağımlılığa çevrilmez" şartına FreyaTTS için çelişiyor cevabını (işlemcide gerçek zamanlı değil; yabancı terimlerde zayıf) ölçümle verir.

## İçerik
### Soru
Araştırma 10 öncelik 8 (İç Ses ses hattı) FreyaTTS'i "Türkçe öncelikli, dizüstü CPU'da gerçek zamanlı (RTF 0.70), Apache-2.0, 183M" diye İZLE etiketiyle önermişti. Bu makinede gerçek zamanlı ve anlaşılır mı?

### Sonuç
sonuc: celisiyor · güven: orta · **Günlük Türkçe anlaşılır (WER %7), ama işlemcide gerçek zamanlı değil (RTF 2.5–12) ve İngilizce terimlerde bozuluyor (WER %60).** Bağımlılık yapılmadı; ses kalitesi yargısı sahibinin kulağında.

### Kanıt
Kurulum: FreyaTTS commit `146d36c` (2026-08-03), PyTorch 2.11.0+cpu, torchaudio 2.11.0+cpu, voxcpm 2.0.3; izole ortam `.araclar/tts` (git dışı). Ağ: yalnız HuggingFace model indirme (`HF_HUB_DISABLE_TELEMETRY=1`); paketlerde başka ağ ya da telemetri çağrısı bulunmadı (grep). İşlemci, 32 iş parçacığı.

| Örnek | Ses (sn) | Üretim (sn) | RTF | WER (Whisper large-v3-turbo ile geri yazım) |
| --- | --- | --- | --- | --- |
| 1 günlük cümle | 7.1 | 86.9 (ilk, ısınma dahil) | 12.21 | %7 — "Kaan" → "Kaan'ın" |
| 2 Türkçe harfler (ğ ş ı ç ü â) | 4.6 | 25.2 | 5.52 | %25 — "şıkırdayarak" → "şükürdeyerek" (â farkı ölçüm yapaylığı) |
| 3 sayılar | 7.8 | 45.3 | 5.78 | %53 — çoğu Whisper'ın rakam yazmasından ("otuz üç" → "33"); gerçek hata "betiği" → "beti" |
| 4 İngilizce terimler | 5.4 | 13.6 | 2.52 | %60 — "Sandbox" → "Sunbols", "Graphify" → "küreç", "qmd" → "kifi" |

Model yükleme: 109.7 sn. Örnek dosyalar: `00-sistem/.kosu/tts-ornek/*.wav` (48 kHz).

### Ölçüm sınırları
- WER, TTS ile Whisper'ın hatalarını birlikte ölçer; anlaşılırlığın yaklaşığıdır, ses doğallığını ölçmez.
- Dört cümle küçük bir örnektir. GPU ölçülmedi (üreticinin iddiası RTX 4090'da RTF 0.10); bu makinede RTX 5070 Ti var.
- Ses doğallığı ve "Leyla" sesinin beğenisi ölçülemez: sahibi dinlemeli.

### Çelişen kaynaklar
- Araştırma 10 ve FreyaTTS README: "dizüstü CPU'da gerçek zamanlı (RTF 0.70 fp32, Apple M3)". Bu makinenin işlemcisinde 2.5–12 ölçüldü.

### Fikre etkisi (delta)
- İç Ses sesli sohbeti için işlemci yolu kullanılamaz (5 sn ses ≈ 14–87 sn üretim).
- İngilizce terim yoğun sistem metni (araç adları) yanlış okunuyor; seslendirmeden önce terimleri Türkçe okunuşa çeviren bir sözlük gerekir.
- Sıradaki ölçüm (sahibin kararıyla): aynı dört cümle CUDA'lı PyTorch ile GPU'da (RTF hedefi < 1). Ek disk ~3 GB.
- Merdiven önerisi: değişmez (bu not bir araç ölçümüdür).

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/10-yenilikci-teknolojiler]] — öncelik 8 ses hattı ve "Türkçe kalite ölçülmeli" şartı
### Beslediği
### Gelen
- ← [[40-ic-ses/MOC-ic-ses]] — araştırma notları listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-016 | Oluşturuldu (4 örnek, RTF ve WER ölçümü) |
