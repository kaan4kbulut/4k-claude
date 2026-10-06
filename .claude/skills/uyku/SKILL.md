---
name: uyku
description: Oturum sonu / haftalık / aylık konsolidasyon. Tekrarları birleştirir, bayat sayfaları işaretler, süresi dolanları arşive taşır, gözlemleri fikre ve fikirleri kavrama terfi ettirir, yansıma tetikler, HARITA ve GUNLUK'ü günceller. Sahibi "toparla", "uyku", "konsolide et" dediğinde ya da zamanlı görevde kullan.
argument-hint: [hafif|tam|aylik]
---

# /uyku — konsolidasyon

Letta'nın uyku-zamanı ajanı ve Generative Agents yansıma eşiğinden. Üç derinlik: `hafif` (oturum sonu, ~5 dk), `tam` (haftalık), `aylik` (hiyerarşik özet). Varsayılan `hafif`.

Bayat liste:
!`python3 00-sistem/scripts/bayat.py 2>&1 | head -40`

## İlkeler
- **Silme yok.** Geçersiz kıl (`gecerli_bitis`, `yerine_gecen`), arşive taşı, günlükte bırak.
- **Önce ara, sonra yaz.** Yeni bir olgu için var olan sayfalarda ara; karar: ADD (yeni sayfa) / UPDATE (var olanı değiştir, sürüm artar) / INVALIDATE (çelişen eski sayfayı geçersiz kıl) / NOOP.
- **Aşırı konsolidasyon yasak.** Orijinaller kalır; özet üstüne eklenir. Yaşa değil referans sayısına göre tut.
- **Koddan türetilebileni kaydetme.** Git'ten ve dosyadan okunabilen şey wiki'ye yazılmaz.

## hafif (oturum sonu)
1. Bu oturumda açılan gözlem/ucucu notlarda tekrar var mı? Aynı olguyu anlatan iki gözlem → biri diğerine `yerine_gecen`, içerik birleştirilir.
2. 01-gelen'de 48 saati aşan işlenmemiş not → `/inbox-triage` çağır ya da `durum: arsiv` ile 90-arsiv/01-gelen/ altına taşı (GUNLUK `[arsiv]`).
3. `nerede-kaldik.md` güncel mi? Değilse yaz.
4. HARITA satır sayısı; 180'i geçtiyse sahibine "MOC bölme zamanı" notu.
5. GUNLUK `[uyku] hafif — N birleştirme, M arşiv`.

## tam (haftalık)
1. hafif adımları.
2. **Bayatlar** (bayat.py): gözlem 30 gün ve atıf < 3 → arşiv; görev 90 gün → sahibine "ilerlet/bekle/iptal" sorusu listesi; `son_gozden_gecirme` > 60 gün → sayfayı yeniden oku, kaynakları canlı kontrol et, ya `son_gozden_gecirme` güncelle ya `guven` düşür.
3. **Terfi**: aynı konuda ≥ 2 bağımsız gözlem → fikir taslağı öner (`merdiven: 1`); `guven: yuksek` ve ≥ 2 sayfadan atıf alan fikir → kavram önerisi. Terfi öneri olarak sahibine sunulur; sahibi onaylarsa `/yeni-parca`.
4. **Yansıma**: yansıtılmamış gözlemlerin `onem` toplamı > 30 ise (1-10 ölçeği) en belirgin üç soruyu çıkar; her soruya kanıt atıflı tek yansıma sayfası (`yansimalar/`), kanıt = gözlem yolları.
5. **Çelişki taraması**: aynı varlık hakkında çelişen iki iddia → raporla (LLM yargısı, otomatik düzeltme yok); sahibi karar verir.
6. MOC'ları güncelle (merdiven özeti, açık sorular, park listesi).
7. `python3 00-sistem/scripts/harita.py --dogrula`; `kontrol.py --kisa`.
7a. **Graf** (`python3 00-sistem/scripts/graf.py`): kopuk küme ve yetim sayfa → bağ önerisi (hangi MOC ya da dayanak eksik); "sınır aşan bağ" → yansıma adayı; merkez sayfalar → değişirse etkisi geniş, BLUF'ta belirt. Öneri sunulur, bağ sahibinin onayıyla `/degistir` ile eklenir.
8. GUNLUK `[uyku] tam — …`. Sahibine BLUF: ne birleşti, ne arşivlendi, hangi terfiler onay bekliyor.

## aylik
1. tam adımları.
2. Ayın gözlem ve yansımalarından bir "ay özeti" yansıması (tema ağacı); orijinaller kalır.
3. Karar günlüğü: `gozden_gecir` tarihi gelen kararlarda tahmin vs gerçek; kalibrasyon notu sahibine.
4. Arşiv süpürmesi: `durum: arsiv` olup hâlâ kat klasöründe duran dosyaları 90-arsiv'e taşı.
5. Kural stoğu için Denetim'e not: giyotin testi zamanı (yasal mı, gerekli mi, yararlı mı).

## Çıktı
`## Kanıt`: bayat.py ve kontrol.py çıkışları, taşınan/birleştirilen dosya listesi, GUNLUK satırı.
