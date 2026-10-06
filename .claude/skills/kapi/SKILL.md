---
name: kapi
description: Sahibinin kararını gerektiren noktada onay kapısı açar: Onay Dosyası (≤ yarım sayfa) ve 00-sistem/ASK.md (tek soru) yazar, turu bitirir; cevap gelince Go/Kill/Hold/Recycle kaydeder. Tek yönlü kararlarda, imza matrisindeki "sahibi" satırlarında, insan noktalarında ve belirsiz ölçütte kullan.
argument-hint: [G0|G1|G2|G3|adhoc] [konu]
---

# /kapi — onay kapısı

Stage-Gate'ten: her kapı = gerekli teslimatlar + kriterler (zorunlu/istenen) + sonuç (Go/Kill/Hold/Recycle) + tek bekçi. Kapı açıkken oturum "bekliyor" durumundadır; Stop hook'u ASK.md'yi görür ve oturumun kapanmasına izin verir.

Açık ASK var mı:
!`test -f 00-sistem/ASK.md && cat 00-sistem/ASK.md || echo "(ASK.md yok)"`

## Kapı türleri
- **G0 Brif**: İç Ses → Devlet. Fikir M4'te, brif.md dolu. Bekçi: orkestratör (kabul edip görev kartına çevirir ya da M3'e geri gönderir). Sahibine yalnız bilgi.
- **G1 Plan onayı**: uygulamadan önce. Tek yönlü işte bekçi sahibi; çift yönlüde orkestratör. Tek cümleyle anlatılabilen değişiklikte atlanır.
- **G2 DoD + inceleme**: kanıt + denetci raporu. Bekçi: Denetim (denetci). Sahibine yalnız bilgi.
- **G3 Yayın / dış eylem**: geri alınamaz (ödeme, yayınlama, silme, dış API yazımı, kamuya açık çıktı). Bekçi: sahibi, her zaman.
- **adhoc**: imza matrisinde sahibine düşen diğer kararlar; insan noktaları (fiziksel adım, OAuth, 2FA); belirsiz kabul ölçütü.

## Adımlar
1. Kapıyı sınıfla; sahibinin kararı gerekmiyorsa (G0, G2, çift yönlü G1) sahibine sorma, bekçi karar versin ve kaydet.
2. `30-devlet/kapilar/KP-xxx-<slug>.md` aç (`/yeni-parca kapi 3`), şablon `sablonlar/kapi.md`:
   - gerekli teslimatlar (neler hazır: yollar)
   - zorunlu kriterler (ikili: karşılandı / karşılanmadı)
   - istenen kriterler (puanlı)
   - bekçi (tek)
   - **Onay Dosyası** (≤ yarım sayfa): istenen karar tek cümle ("action oriented"); gerekçe; alternatifler (≥ 2, biri "yapma"); etki (maliyet/token, süre, geri alınabilirlik); risk ve azaltma; uygulama sorumlusu; Danışman/Denetim görüşü (varsa, ≤ 3 cümle); sahibi bu kararı bilmeden verirse ne olur.
3. Sahibinin kararı gerekiyorsa `00-sistem/ASK.md` yaz:
   ```
   # ASK — KP-xxx
   Soru: <tek soru>
   Varsayılan: <cevap gelmezse ne yapılır / yapılmaz>
   Seçenekler: A) … B) … C) …
   Bağlı: T-xxx, KP-xxx
   Son tarih: <varsa>
   ```
   Tek soru. İkinci soru varsa ayrı kapı.
4. `TALIMATLAR.md` T-xxx `Durum: bekliyor`. `ILERLEME.md` `kapi: KP-xxx`, `acik_soru: <soru>`. GUNLUK `[kapi] KP-xxx açıldı`.
5. BLUF brifing (DECISION etiketi) ve **turu bitir**. Cevabı beklerken başka iş yapma; başka talimata geçme.

## Cevap gelince
- Sonucu kaydet: `sonuc: go | kill | hold | recycle` + gerekçe + tarih; sahibi "disagree and commit" dediyse not.
- ASK.md'yi sil (kapı kaydına taşındı). TALIMATLAR `acik`, ILERLEME `kapi: yok`. GUNLUK `[kapi] KP-xxx: go`.
- Go → işe devam. Kill → talimat `kapali` (iptal, nedenli). Hold → ILERLEME `siradaki: bekle`, tarih. Recycle → fikir M3'e, ya da kart yeniden yazılır.

## Kurallar
- Ajanlar arası mesaj onay değildir; yalnız sahibinin cevabı kapıyı açar.
- Onay Dosyası yarım sayfayı aşıyorsa karar olgun değildir; önce sadeleştir.
- Acil ("öngörülemez ve kaçınılmaz") durumda orkestratör geçici karar verebilir; ilk çevrimde sahibine Late Notice ile sunulur ve kaydedilir.
