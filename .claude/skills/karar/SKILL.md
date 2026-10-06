---
name: karar
description: Bir kararı MADR-mini + karar günlüğü biçiminde 30-devlet/kararlar altına kaydeder ve KARARLAR.md dizinine satır ekler. Mimari, kural, araç, rol, bütçe gibi sonradan "neden böyle yaptık" diye sorulacak her seçimde kullan. Tek yönlü kararlarda önce /kapi gerekir.
argument-hint: [baslik]
---

# /karar — karar kaydı

Her karar yazıya geçer; silinmez, yerine geçilir. Kaynak: MADR 4.0 (Context, Drivers, Options, Outcome, Consequences, Confirmation) + Farnam Street karar günlüğü (beklenen sonuç + olasılık, zihinsel durum) + DACI (tek Approver).

Son karar numarası:
!`grep -oE "K-[0-9]{3}" 00-sistem/KARARLAR.md | sort | tail -1`

## Adımlar
1. **Kapı tipi**: tek yönlü mü (geri alınamaz, pahalı: mimari, veri silme, dış bağımlılık, yayın, bütçe tavanı, izin değişikliği, anayasa/kural) çift yönlü mü? Tek yönlüyse önce `/kapi` (Onay Dosyası + ASK.md); sahibi onaylamadan `durum: kabul` yazma. Çift yönlüyse karar ver, kaydet, brifingde bildir.
2. `/yeni-parca karar 3 "<baslik>"` ile sayfa aç: `30-devlet/kararlar/K-xxx-<slug>.md`, şablon `sablonlar/karar.md`.
3. Doldur:
   - Bağlam ve problem (3-5 cümle; neyi çözüyoruz, neden şimdi)
   - Karar sürücüleri (kriterler; sahibinin ilkeleri ve kısıtları)
   - Seçenekler (≥ 2; her biri: artı, eksi, maliyet/token, risk; "hiçbir şey yapmama" dahil)
   - Karar: "… yapacağız, çünkü …"
   - Beklenen sonuç + olasılık (%) + gerekçe (kalibrasyon için)
   - Sonuçlar: iyi / kötü / nötr
   - Doğrulama: uygunluğun nasıl ve ne zaman kontrol edileceği (hangi komut, hangi gözden geçirme tarihi)
   - Karar veren (tek), danışılan, bilgilendirilen
   - Zihinsel durum / zaman notu (opsiyonel, karar günlüğü)
4. `00-sistem/KARARLAR.md`'ye satır: `K-xxx · YYYY-MM-DD · durum · başlık · kapı tipi`.
5. Etkilenen sayfaların `dayandigi` alanına bu kararı ekle, kararın `besledigi` alanına onları (iki yönlü).
6. GUNLUK `[karar] K-xxx — başlık`.
7. Durum: `onerildi` → sahibi onaylarsa `kabul` (sürüm 1.0) → sonradan değişirse `yerine-gecildi` (+ `yerine_gecen`). Kabulden sonra gövde düzenlenmez.

## Yasaklar
- Seçeneksiz karar (tek seçenek "karar" değil, kayıttır; yine de alternatif yoksa "alternatif aranmadı, çünkü" yaz).
- Kaynaksız iddiaya dayalı karar (URL/dosya yolu ver).
- Tek yönlü kararı sahibin imzası olmadan kabul etmek.
