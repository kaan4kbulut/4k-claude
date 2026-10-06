---
name: brifing
description: Sahibine BLUF (bottom line up front) biçiminde rapor yazarken kullan: ACTION/DECISION/INFO etiketi, tek cümle sonuç, kanıt, değerlendirme, öneri, açık sorular. Kötü haber ilk satırda. Her talimat kapanışında ve her kapı açılışında kullan.
argument-hint: [konu]
---

# /brifing — BLUF rapor

Askeri BLUF ve SBAR'dan: ana nokta önce, ayrıntı sonra, istek açık. Ajan→orkestratör raporu ≤ 2.000 token; orkestratör→sahibi raporu ≤ 1 sayfa. Ayrıntı bağlantılı dosyalarda durur, raporda değil.

## Şablon

```
# [ACTION | DECISION | INFO] <konu> — T-xxx

**BLUF.** <Sonuç tek cümle.> <Sahibinden istenen tek cümle; INFO ise "istenen yok".>

**Durum.** Ne istendi (T-xxx niyeti), ne yapıldı, nerede duruyor.

**Kanıt.**
- `komut` → çıkış kodu · çıktı özeti
- değişen dosyalar: …
- test/kontrol: …

**Değerlendirme.**
- Risk: …
- Sapma (brif/talimattan): …
- Örtülü aldığım kararlar: … (çift yönlü; itiraz edersen geri alınır)

**Öneri / istek.** <Karar gerekiyorsa seçenekler, varsayılan seçenek işaretli, son tarih.>

**Açık sorular.** ≤ 3.

**Sıradaki.** Tek adım.
```

## Kurallar
- Etiket: ACTION (sahibi bir şey yapacak: imza, fiziksel adım, ödeme), DECISION (bir karar bekliyor; ASK.md var), INFO (bilgi; istenen yok).
- Kötü haber, başarısızlık, aşılan bütçe, atlanan adım: ilk satırda, yumuşatmadan.
- "Yaptım" değil kanıt: komut ve çıkış kodu olmadan "test ettim" yazma.
- Övgü ve dolgu yok. Her cümle bir bilgi taşır.
- Sahibi sesli dinleyecekse: BLUF'u yüksek sesle okunabilir tek cümle yaz; listeyi kısa tut.
- Örtülü kararlar bölümü zorunludur: ajanlar eylem yaparken karar verir; bunlar görünür olmalı (Cognition: "actions carry implicit decisions").
