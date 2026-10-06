---
name: haftalik
description: Sahibiyle ~45 dakikalık sesli haftalık gözden geçirme: gelen kutusunu temizle, fikirleri ilerlet/bekle/öldür, haftanın üç sorusunu yansıt, karar günlüğünü kalibre et, yaratıcı tur, metrikler. Sahibi "haftalık", "gözden geçirelim", "hafta nasıl geçti" dediğinde kullan.
argument-hint: [tarih]
---

# /haftalik — haftalık gözden geçirme (sesli, ~45 dk)

GTD haftalık gözden geçirme (temizle → güncelle → yaratıcı) + Generative Agents yansıması + karar günlüğü kalibrasyonu. Sahibi konuşur, sen yönetir ve kaydedersin. DİNLE/SOR kuralları geçerli; tur başına tek soru.

Hazırlık (sen önceden çıkar, sahibine okuma):
!`python3 00-sistem/scripts/bayat.py 2>&1 | head -30`
!`ls 01-gelen/*.md 2>/dev/null | wc -l`

## 1. Temizle (5 dk)
- 01-gelen sıfırlanır: her not için `/inbox-triage` sonucu sahibine tek cümleyle sun: gözlem mi, fikir mi, görev adayı mı, çöp mü. Sahibi onaylar; 48 saati aşanlar arşiv.
- Açık ASK.md varsa ilk o.

## 2. Güncelle (15 dk)
- M1-M3'teki her fikri tek cümleyle oku (tek-cumle alanı). Sahibi üçten birini söyler: **ilerlet** (hangi basamağa; kriter karşılanıyor mu kontrol et), **bekle** (tarih), **öldür** (neden zorunlu; `oldurme_nedeni`, arşiv).
- Açık görev kartları: durum, is_yasi, SLE aşımı. Sahibinin fiziksel saat kısıtına göre bu haftanın "insan noktaları" listesi.
- Açık kapılar ve bulgular: bekleyen karar var mı.

## 3. Yansıt (10 dk)
- Haftanın gözlem ve notlarından **üç en belirgin üst düzey soru** çıkar (önem toplamına göre); sırayla sor; sahibinin sesli cevabı yansıma sayfası olur (`yansimalar/`, kanıt = gözlem yolları).
- Çelişki taraması: haftanın notlarında birbiriyle çelişen iki iddia varsa göster; sahibi karar verir.

## 4. Karar günlüğü (5 dk)
- `gozden_gecir` tarihi gelen kararlar: beklenen sonuç + olasılık vs ne oldu. Kalibrasyon notu (fazla iyimser / kötümser / isabetli). Kararın `dogrulama` bölümüne yaz.

## 5. Yaratıcı (5 dk)
- Someday listesi (MOC-ic-ses "Someday"); arşivden rastgele iki öldürülmüş fikir oku (yeniden karşılaşma; aralıklı tekrar değil). Sahibi isterse biri geri alınır (`durum: taslak`, günlük notu).

## 6. Metrikler (5 dk, sen yazarsın, sahibi okur)
- Yakalanan not sayısı; 48 saatte işlenen %; basamak başına terfi; öldürülen; medyan fikir→brif gün; açık görev ve ortalama is_yasi; MALIYET.csv haftalık toplam; **flip sayacı**: senin `[konum]` değişikliklerin ve kaçının gerekçeli olduğu.
- MOC-ic-ses "Haftalık" bölümüne tablo satırı.
- Maliyet doğruluğu: `python3 00-sistem/scripts/maliyet.py --gunluk` (çıkış 1 = tahmin ile ccusage farkı > %5; nedenini bul). Bağlantı canlılığı: sahibine `! python3 00-sistem/scripts/canli.py` çalıştırmasını öner (ağ ister); ölü bağlantılı kaynak sayfası /degistir ile güncellenir ya da olgu UNCONFIRMED işaretlenir.

## 7. Kapanış
- `/uyku tam` çalıştır (ya da zamanlı göreve bırak).
- `nerede-kaldik.md`, ILERLEME, GUNLUK `[oturum] haftalık gözden geçirme`.
- BLUF (INFO/ACTION): bu hafta sahibinden beklenen üç şey.

## Kurallar
- Sahibinin "beğendim" ya da "beğenmedim" demesi senin davranışını değiştirmez; yalnız 6. adımdaki kalibrasyon protokolü değiştirir.
- Öldürme utanç değildir; PR/FAQ'ların çoğu asla yayımlanmaz. Öldürülen fikir silinmez.
