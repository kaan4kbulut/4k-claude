---
name: degistir
description: Var olan bir 4k-claude sayfasını değiştirirken kullan (içerik düzeltme, alan güncelleme, bağ ekleme/çıkarma, durum değişikliği, supersede). Sürümü artırır, iki günlüğe satır düşer, bağları iki yönlü tutar. Sahibi "şunu güncelle", "düzelt", "şu kararı geçersiz kıl" dediğinde kullan.
argument-hint: [yol] [ne-degisecek]
---

# /degistir — var olan sayfayı değiştirme

Değiştirmek de talimatla başlar. Hiçbir sayfa sessizce değişmez; eski metin sayfanın günlük tablosunda iz bırakır.

Hedef: `$0` (yol). Değişiklik: `$1`.

## 1. KAYIT
- Açık bir talimata bağlıysa onu kullan; değilse `TALIMATLAR.md`'ye yeni T-xxx (niyet: "X sayfasında Y değişecek, çünkü Z").
- Değişiklik bir kapı gerektiriyor mu? Şu durumlarda **evet, önce `/kapi`**: kabul edilmiş karar/kural/yönerge metni (yalnız supersede ile değişir), anayasa (hiç; yalnız sahibi), imza matrisi, model politikası, görev kartının kabul ölçütleri (uygulama başladıysa), alan paketinin mevzuat/maliyet bölümleri.

## 2. OKU ve SINIFLA
- Sayfayı tam oku. Frontmatter'daki `durum` ve `surum`'a bak.
- Sınıf: (a) içerik düzeltmesi, (b) alan güncellemesi, (c) bağ ekleme/çıkarma, (d) durum değişikliği (taslak→aktif, aktif→arsiv), (e) supersede (yeni sayfa eskisinin yerine geçer).
- `durum: kabul` olan karar/kural için yalnız (e) geçerlidir: eski sayfa düzenlenmez; yeni sayfa açılır (`/yeni-parca`), eskiye `yerine_gecen`, yeniye `yerine_gecti`, eski `durum: yerine-gecildi`.

## 3. DEĞİŞTİR
- İçeriği düzenle. Frontmatter: `surum` += 0.1; `guncelleme: bugün`; durum değişiyorsa `durum`; bağ değişiyorsa `dayandigi`/`besledigi`.
- Bağ eklendiyse hedef sayfaya ters satır (`← [[bu]] — neden`) ve `besledigi` girişi; bağ çıkarıldıysa iki taraftan da kaldır.
- Sayfanın günlük tablosuna satır: `surum · tarih · T-xxx · ne değişti (kısa, eski değer parantez içinde)`.
- Arşive gidiyorsa: `durum: arsiv`, dosyayı `90-arsiv/<eski-yol>` altına taşı (git mv), HARITA satırını sil, GUNLUK'e `[arsiv]`.

## 4. KAPANIŞ
- `GUNLUK.md`: `YYYY-MM-DD HH:MM [degisti] yol — ne değişti`.
- HARITA satırındaki tarih ve amaç (değiştiyse) güncelle.
- Sistem dosyası (SEMA, şablon, betik, kural, CLAUDE.md) değiştiyse `DEGISIKLIKLER.md` Unreleased altına madde (Eklendi/Değişti/Kaldırıldı/Düzeltildi).
- `python3 00-sistem/scripts/kontrol.py --kisa`; sıfır hata olmadan talimat kapanmaz.
- `## Kanıt`: diff özeti (`git diff --stat`), kontrol.py çıkışı.

## Yasaklar
- Kabul edilmiş kararın gövdesini düzenlemek (supersede et).
- Sürüm artırmadan değiştirmek.
- Eski değeri iz bırakmadan silmek.
- Başka birinin (başka rolün) sahip olduğu dosyayı kartta izin yokken değiştirmek.
