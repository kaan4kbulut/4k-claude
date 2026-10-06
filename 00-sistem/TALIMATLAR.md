# Talimatlar — istek defteri

Her istek numaralı bir talimattır. Biçim `00-sistem/sablonlar/talimat.md`. Durumlar: `acik`, `bekliyor` (ASK.md var), `kapali`. En yeni en altta. Numara boşluk bırakmadan artar, yeniden kullanılmaz.

---

## T-000 — Yeni Sistem klasörünün ilk kurulumu
- Tarih: 2026-10-06
- Niyet: Şema v2'ye göre tüm sistem dosyalarını (CLAUDE.md, .claude katmanı, 00-sistem omurgası, şablonlar, betikler, kat dosyaları, araştırma raporları) tam içerikle oluşturmak; işleyiş Claude Code'da denenebilir olsun.
- Başarı ölçütü: `python3 00-sistem/scripts/kontrol.py` sıfır hata; HARITA'da tüm frontmatter'lı sayfalar; her sayfa SEMA'ya uygun.
- Sınırlar: Rol (kadro) dosyası yazılmaz; gerçek proje işi yapılmaz; sandbox açılmaz.
- Kat: 0
- Kapı: cift-yonlu (dosyalar geri alınabilir; git ile)
- Durum: kapali
- Doğurduğu dosyalar: tüm klasör (HARITA.md listeler)
- Kapanış notu: Kurulum tamamlandı; kontrol.py sıfır hata. Danışman ve kadro kararları açık (K-002).

## T-001 — Yazıcı işi fikrini kat 4'e not olarak kaydet
- Tarih: 2026-10-06
- Niyet: Deneme 1/4. Sahibinin "yazıcı alıp bir işe başlamak istiyorum" fikrini zihin katına fikir sayfası olarak kaydetmek; altı adımın tamamını işletmek.
- Başarı ölçütü: `40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md` var; merdiven 1; Cynefin tipi atanmış; HARITA ve GUNLUK satırı; kontrol.py sıfır hata.
- Sınırlar: Fikir değerlendirilmez (ZORLA modu çalıştırılmaz); yalnız kayıt.
- Kat: 4
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md
- Kapanış notu: F-0001 merdiven 1, cynefin kompleks (Claude ataması, sahibi onayı bekliyor) olarak kaydedildi; HARITA, MOC, GUNLUK satırları düştü; kontrol.py 0. Açık: yazıcı türü sorusu; şablon/şema uyumsuzluğu (kapi, son_dokunus) için kök neden talimatı önerildi.

## T-002 — "Önce pazar araştırması yapılacak" kararını kat 3'e kaydet
- Tarih: 2026-10-06
- Niyet: Deneme 2/4. F-0001'e dayanan bir karar kaydı (K-003) açmak; MADR-mini alanları dolu; F-0001 ile iki yönlü bağ.
- Başarı ölçütü: `30-devlet/kararlar/K-003-yazici-pazar-arastirmasi.md` var; durum onerildi; KARARLAR.md satırı; F-0001.besledigi içinde K-003; kontrol.py sıfır hata.
- Sınırlar: Karar sahibi onaylamadan `kabul` olmaz.
- Kat: 3
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:

## T-003 — Pazar araştırması görev kartını kat 2'ye aç
- Tarih: 2026-10-06
- Niyet: Deneme 3/4. K-003'e dayanan görev kartı (G-001); 12 alan dolu; insan noktaları beyan edilmiş; kanıt boş olduğu için kanban `bekliyor`.
- Başarı ölçütü: `20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md` var; K-003.besledigi içinde G-001; kontrol.py sıfır hata; kanıtsız `tamam` denemesi kontrol.py tarafından reddedilir (bunu bilerek dene ve raporla).
- Sınırlar: Araştırma yapılmaz; yalnız kart.
- Kat: 2
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:

## T-004 — F-0001'e bir cümle ekle (değiştirme kuralı denemesi)
- Tarih: 2026-10-06
- Niyet: Deneme 4/4. `/degistir` ile F-0001'e bir cümle eklemek; sürüm 0.2; sayfa günlüğünde ve GUNLUK'te satır.
- Başarı ölçütü: F-0001 `surum: 0.2`; günlük tablosunda ikinci satır; GUNLUK `[degisti]`; kontrol.py sıfır hata.
- Sınırlar: Başka alan değişmez.
- Kat: 4
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:
