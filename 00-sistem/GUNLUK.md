# Günlük — salt ekleme işlem kaydı

Biçim: `YYYY-MM-DD HH:MM [tur] yol — not`. Türler: yeni, degisti, arsiv, karar, kapi, hata, durdu, ayar, oturum, uyku. Satırlar değiştirilmez, silinmez; yalnız sonuna eklenir. Hook'lar da buraya yazar. SessionStart son 30 satırı okur.

2026-10-06 21:00 [oturum] T-000 — kurulum başladı (şema v2)
2026-10-06 21:30 [yeni] 00-sistem/SEMA.md — Her sayfanin frontmatter alanlarini, turlerini, durum degerlerini, bag turlerini
2026-10-06 21:30 [yeni] 00-sistem/SISTEM.md — Yeni Sistem'in kok haritasi; ne oldugunu, katlari, klasorleri ve nasil gezileceg
2026-10-06 21:30 [yeni] 00-sistem/arastirma/01-claude-code-mekanikleri.md — Claude Code'un CLAUDE.md, hafiza, alt ajan, hook, skill, izin ve oturum mekanikl
2026-10-06 21:30 [yeni] 00-sistem/arastirma/02-hafiza-ve-wiki-duzenleri.md — Yapay zeka ajan hafiza sistemlerinin ve kisisel bilgi/wiki yontemlerinin, duz Ma
2026-10-06 21:30 [yeni] 00-sistem/arastirma/03-cok-ajanli-isleyis-ve-yonetisim.md — Cok ajanli mimari desenlerini, insan-dongude yonetisim araclarini (kapilar, kara
2026-10-06 21:30 [yeni] 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md — Bir LLM/ajan sistemini daha iyi ve daha guvenilir yapan teknikleri (baglam muhen
2026-10-06 21:30 [yeni] 00-sistem/arastirma/05-eller-ve-alan-paketi-3d.md — Bir ajanin dunyaya dijital olarak dokunma yollarini (eller yetenek matrisi) ve b
2026-10-06 21:30 [yeni] 00-sistem/arastirma/06-sirket-operasyonlari.md — Gercek sirket operasyon bilgisini (SOP, surec haritalari, roller, kalite, tedari
2026-10-06 21:30 [yeni] 00-sistem/arastirma/07-devlet-yapilari.md — Gercek devlet teskilatlarinin (bakanlik anatomisi, norm hiyerarsisi, imza/onay, 
2026-10-06 21:30 [yeni] 00-sistem/arastirma/08-ic-ses-yontemleri.md — Sesli dusunme, fikir yakalama ve olgunlastirma, ses-boru-hatti, arastirma-eslikc
2026-10-06 21:30 [yeni] 00-sistem/arastirma/09-github-taramasi.md — Ekim 2026 itibariyla Markdown-wiki tabanli bir Claude Code isletim sistemiyle il
2026-10-06 21:30 [yeni] 10-insan/MOC-insan.md — Bu icerik haritasi, eller katindaki ciktilari, degismez kaynaklari ve arac kaydi
2026-10-06 21:30 [yeni] 10-insan/araclar/ARAC-KAYDI.md — Sistemin dunyaya dijital dokunma yollarini (yetenek, arac/API, olgunluk, insan n
2026-10-06 21:30 [yeni] 20-sirket/MOC-sirket.md — Bu icerik haritasi, orgutleme katindaki rolleri, acik gorev kartlarini (Kanban),
2026-10-06 21:30 [yeni] 20-sirket/RITIM.md — Gunluk, haftalik, aylik, ceyreklik ve yillik operasyon ritmini; her toplantinin 
2026-10-06 21:30 [yeni] 20-sirket/SCORECARD.md — Haftalik 5-15 KPI'yi sahipli ve hedefli tutar; off-track olan gosterge Issues li
2026-10-06 21:30 [yeni] 20-sirket/alan-paketleri/3d-uretim.md — Bu alan paketi, 3D baski mikro-uretim alaninda sistemin dijital tarafi ucten uca
2026-10-06 21:30 [yeni] 30-devlet/MOC-devlet.md — Bu icerik haritasi, irade katindaki normlari, kararlari, kapilari ve denetim kay
2026-10-06 21:30 [yeni] 30-devlet/kararlar/K-001-pilotta-kadro-yok.md — Bu karar kaydi, pilot asamasinda rol (bakanlik) ajanlari acilmamasini, yalniz ok
2026-10-06 21:30 [yeni] 30-devlet/kararlar/K-002-danisman-zihin-islevi.md — Bu karar kaydi, Danisman rolunun ayri bir ajan olarak degil zihin katinin bir is
2026-10-06 21:30 [yeni] 30-devlet/normlar/ANAYASA.md — Yeni Sistem'in degistirilemez cekirdegini kurar; katlari, ilkeleri, yetkinin kay
2026-10-06 21:30 [yeni] 30-devlet/normlar/HAKEM-KURALLARI.md — Bir modelin baska bir modelin ciktisini yargiladigi her yerde (denetci, kapi yar
2026-10-06 21:30 [yeni] 30-devlet/normlar/IMZA-MATRISI.md — Hangi kararin kimin imzasini istedigini, yetki devrinin kurallarini ve kayitlari
2026-10-06 21:30 [yeni] 30-devlet/normlar/MODEL-POLITIKASI.md — Hangi isin hangi modele ve cabaya gidecegini, tur ve butce tavanlarini, onbellek
2026-10-06 21:30 [yeni] 40-ic-ses/MOC-ic-ses.md — Bu icerik haritasi, zihin katindaki fikirlerin merdiven durumunu, gozlemleri, ya
2026-10-06 21:30 [yeni] 40-ic-ses/nerede-kaldik.md — Son oturumun uc maddesini (konusulan, acik, sonraki) tutar; SessionStart okur, /
2026-10-06 21:40 [karar] 30-devlet/kararlar/K-001-pilotta-kadro-yok.md — kabul: pilotta kadro yok
2026-10-06 21:41 [karar] 30-devlet/kararlar/K-002-danisman-zihin-islevi.md — önerildi: Danışman zihin işlevi
2026-10-06 22:50 [degisti] 00-sistem/HARITA.md — harita.py --uret: 26 satır
2026-10-06 22:52 [ayar] 00-sistem/scripts/kontrol.py — wikilink atlama: '/' içermeyen hedef (ör. [[hedef]] yer tutucu) denetlenmez
2026-10-06 22:55 [oturum] T-000 — kurulum kapandı; kontrol.py çıkış 0 (26 sayfa, 27 bağ, uyarı 0)
2026-10-06 21:44 [yeni] 40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md — Kaan'in yazici alip is kurma fikri; merdiven 1, cynefin kompleks (Claude atamasi, onay bekliyor)
2026-10-06 21:46 [durdu] T-001 — sablon/sema uyumsuzlugu: fikir.md 'kapi: belirlenmedi' enum'da yok; son_dokunus PyYAML ile date okunuyor (yscommon tarih listesinde yok). Sayfada gecici cozum: kapi alani cikarildi, son_dokunus tirnakli. Kok neden icin yeni talimat onerildi.
2026-10-06 21:51 [oturum] d061ab4c-b1f — kapandı (other); tur= in=0 out=0
2026-10-06 21:52 [hata] oturum 9630e132-c06 — durma hatası: rate_limit
2026-10-06 21:53 [oturum] 9630e132-c06 — kapandı (other); tur= in=0 out=0
2026-10-06 23:41 [degisti] T-005 — talimat açıldı: analiz eksiklerinin kök neden düzeltmesi
2026-10-06 23:46 [ayar] 00-sistem/GUNLUK.md — sira-onaylandi: T-000 satırlarındaki 22:50-22:55 damgaları elle yazılmış (yeni-sistem.zip 21:40'ta oluştu, gerçek saat daha erken); satırlar değiştirilmedi, bu satırdan sonrası sıra denetimine girer (T-005)
2026-10-06 23:46 [degisti] 00-sistem/scripts/calistir.sh — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/hooks/durus-kapisi.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/hooks/oturum-basi.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/hooks/yikici-koruma.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/hooks/kapanis-kaydi.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/settings.json — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/scripts/yscommon.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/scripts/kontrol.py — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/sema/sayfa.schema.json — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/SEMA.md — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/MALIYET.csv — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] CLAUDE.md — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] .claude/rules/00-sistem.md — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [degisti] 00-sistem/DEGISIKLIKLER.md — T-005 kök neden düzeltmesi (ayrıntı DEGISIKLIKLER 0.2.0)
2026-10-06 23:46 [yeni] 00-sistem/scripts/gunluk.py — T-005: GUNLUK satırını sistem saatiyle yazan yardımcı
2026-10-06 23:46 [oturum] T-005 — kapandı — 7 eksik düzeltildi; kontrol.py 0
