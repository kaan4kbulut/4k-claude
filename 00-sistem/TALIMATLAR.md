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
- Niyet: Deneme 2/4. F-0001'e dayanan bir karar kaydı (K-004) açmak; MADR-mini alanları dolu; F-0001 ile iki yönlü bağ.
- Başarı ölçütü: `30-devlet/kararlar/K-004-yazici-pazar-arastirmasi.md` var; durum onerildi; KARARLAR.md satırı; F-0001.besledigi içinde K-004; kontrol.py sıfır hata.
- Sınırlar: Karar sahibi onaylamadan `kabul` olmaz.
- Kat: 3
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kararlar/K-004-yazici-pazar-arastirmasi.md; değişen: F-0001 (besledigi, sürüm değişmez — bağ eklemek içerik değişikliği değil), KARARLAR, MOC-devlet
- Kapanış notu: K-004 önerildi; MADR-mini alanları dolu, F-0001 ile iki yönlü bağ. Sahibi onaylamadan kabul olmaz. Sapma: talimat kurulumda K-003 numarasını öngörüyordu; K-003 ad değişikliğine verildi, bu karar K-004.

## T-003 — Pazar araştırması görev kartını kat 2'ye aç
- Tarih: 2026-10-06
- Niyet: Deneme 3/4. K-004'e dayanan görev kartı (G-001); 12 alan dolu; insan noktaları beyan edilmiş; kanıt boş olduğu için kanban `bekliyor`.
- Başarı ölçütü: `20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md` var; K-004.besledigi içinde G-001; kontrol.py sıfır hata; kanıtsız `tamam` denemesi kontrol.py tarafından reddedilir (bunu bilerek dene ve raporla).
- Sınırlar: Araştırma yapılmaz; yalnız kart.
- Kat: 2
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md; değişen: K-004 (besledigi, sürüm değişmez), MOC-sirket, HARITA
- Kapanış notu: G-001 12 alanla açıldı, kanban bekliyor; insan noktaları HP-001 (K-004 onayı) ve HP-002 (yazıcı türü). Kanıtsız tamam denemesi kontrol.py tarafından reddedildi (karalama kopyasında kanban: tamam → "kanıtsız tamam: kanban tamam ama kanit boş", çıkış 1). Sapma: talimat K-003 öngörüyordu, karar K-004.

## T-004 — F-0001'e bir cümle ekle (değiştirme kuralı denemesi)
- Tarih: 2026-10-06
- Niyet: Deneme 4/4. `/degistir` ile F-0001'e bir cümle eklemek; sürüm 0.2; sayfa günlüğünde ve GUNLUK'te satır.
- Başarı ölçütü: F-0001 `surum: 0.2`; günlük tablosunda ikinci satır; GUNLUK `[degisti]`; kontrol.py sıfır hata.
- Sınırlar: Başka alan değişmez.
- Kat: 4
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: değişen: 40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md (0.1 → 0.2), HARITA
- Kapanış notu: /degistir ile tek cümle eklendi; sürüm 0.2, sayfa günlüğünde ikinci satır, GUNLUK [degisti]; başka alan değişmedi (git diff ile doğrulandı). Not: T-002/T-003 bağ eklemeleri sürümü artırmadı (yeni-parca ADIM 5.2), bu yüzden ölçütteki 0.2 tuttu.

## T-005 — Analizde bulunan eksiklerin kök neden düzeltmesi
- Tarih: 2026-10-06
- Niyet: 2026-10-06 analizinde bulunan eksikleri kapatmak: calistir.sh'ta hook'ları kapatan --bare; git deposu yok; durus-kapisi'nin metne dayalı (sahte kanıtla geçilebilen) kontrolü ve İç Ses sohbetiyle çatışması; yikici-koruma'nın yanlış pozitifleri ve açıkları; MALIYET.csv'nin hep 0 yazması; şablon/şema uyumsuzluğu (belirlenmedi enum dışı, tarih alanları); GUNLUK'te elle yazılan zaman damgaları.
- Başarı ölçütü: her düzeltme için çalıştırılmış test (komut + çıkış kodu); kontrol.py sıfır hata; hook'lar örnek girdilerle beklenen kararı veriyor; git'te temel commit (20bc76d) ve düzeltme commit'i.
- Sınırlar: Anayasa, imza matrisi ve "altı adım" kuralı değiştirilmez (sahibinin kararı; öneri olarak sunulur). F-0001 içeriğine dokunulmaz (T-004 denemesi için korunur). T-002..T-004 açık kalır.
- Kat: 0
- Kapı: cift-yonlu (git ile geri alınabilir)
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/gunluk.py (yeni); değişen: calistir.sh, durus-kapisi.py, oturum-basi.py, yikici-koruma.py, kapanis-kaydi.py, settings.json, yscommon.py, kontrol.py, sayfa.schema.json, SEMA.md, MALIYET.csv, CLAUDE.md, rules/00-sistem.md, DEGISIKLIKLER.md
- Kapanış notu: Yedi eksik kök nedenden düzeltildi ve testlerle doğrulandı. Açık kalanlar: hafif yol önerisi (sahibinin kararı); sandbox hâlâ kapalı (bubblewrap + socat kurulumu sahibinde); omitClaudeMd alanı belgelerde doğrulanamadı.

## T-006 — Sistemin adını "Yeni Sistem"den "4k-claude"a değiştir
- Tarih: 2026-10-06
- Niyet: Sahibinin isteğiyle sistemin adı 4k-claude olur. Canlı dosyalardaki ad (kurallar, hook iletileri, şema, README, SISTEM, ANAYASA) ve klasör adı değişir; tarihî kayıtlar (GUNLUK satırları, 00-sistem/arastirma raporları, kapanmış talimat başlıkları) olduğu gibi kalır.
- Başarı ölçütü: canlı dosyalarda "Yeni Sistem" geçmiyor (grep); ANAYASA 1.1 ve sayfa günlüğünde çerçeve ifade; K-003 karar kaydı ve KARARLAR satırı; kontrol.py sıfır hata; klasör ~/Downloads/4k-claude.
- Sınırlar: Anlam değişmez, yalnız ad. Arşiv niteliğindeki metin yeniden yazılmaz. T-002/T-003'ün planladığı karar numarası K-003'ten K-004'e kayar (numara sırası kuralı).
- Kat: 0
- Kapı: cift-yonlu (git ile geri alınabilir)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kararlar/K-003-ad-degisikligi-4k-claude.md (yeni); değişen: ANAYASA (1.1), SISTEM (0.2), KARARLAR, MOC-devlet, HARITA, README, CLAUDE.md, AGENTS.md, hook iletileri, şemalar, ajanlar, skill açıklamaları; klasör ~/Downloads/yeni-sistem → ~/Downloads/4k-claude
- Kapanış notu: Ad değişti; canlı dosyalarda eski ad yok, tarihî kayıtlar korundu. Açık: eski Claude Code oturum geçmişi eski yola bağlı; ~/Downloads/yeni-sistem.zip ve "Yeni Sistem Şeması.md" klasör dışı, dokunulmadı.

## T-007 — Yenilikçi YZ araç ve teknoloji araştırmasını kaynak sayfası olarak kaydet
- Tarih: 2026-10-06
- Niyet: Sahibinin "Graphify gibi yapay zeka çözümlerini ve yenilikçi teknolojileri araştır, dahil edebileceklerimizi bul" isteği. Araştırma alt ajanının raporu 00-sistem/arastirma/10 olarak, 09-github-taramasi kararlarını tekrar etmeden, BENİMSE/ÖDÜNÇ AL/İZLE/UNCONFIRMED etiketleriyle sisteme girer.
- Başarı ölçütü: sayfa var, SEMA'ya uygun; dayandığı raporlar ve ARAC-KAYDI ile iki yönlü bağ; HARITA ve GUNLUK satırı; kontrol.py sıfır hata.
- Sınırlar: Hiçbir araç kurulmaz, ayar değiştirilmez; öneriler sahibinin seçimiyle ayrı talimatlara döner (sandbox açmak imza ister).
- Kat: 0
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/arastirma/10-yenilikci-teknolojiler.md (yeni); değişen: arastirma 02/04/05/08/09 (besledigi, 1.1), ARAC-KAYDI (0.2), HARITA
- Kapanış notu: 10 öncelikli öneri kayıtlı; hiçbiri kurulmadı. Sahibinin seçimi bekleniyor (öncelik 1 sandbox imza ister). Ara hata: backlink betiği 5 raporu boşalttı, git HEAD'den geri yüklenip yeniden uygulandı.

## T-008 — Bash sandbox'ını aç (öncelik 1)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 1: Claude Code Bash sandbox'ı (bubblewrap + socat) proje ayarında açılır; sandbox kurulamazsa oturum açılmaz, sandbox dışına kaçış kapalıdır, kimlik bilgisi klasörleri okunamaz.
- Başarı ölçütü: settings.json'da sandbox bloğu; gerçek bir Claude Code oturumunda (claude -p) beş yoklama beklenen sonucu verir: ev dizinine yazma reddedilir, proxy dışı ağ çözülemez, ~/.ssh okunamaz, .claude/hooks'a yazma reddedilir, kontrol.py çalışır; kontrol.py sıfır hata.
- Sınırlar: Ağ izin listesi boş başlar (alan adı eklemek ayrı karar). Kullanıcı ayarına (~/.claude/settings.json) dokunulmaz; yalnız bu proje.
- Kat: 0
- Kapı: cift-yonlu (ayar geri alınabilir) · imza: sahibi (KP-001)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kapilar/KP-001-sandbox-acilisi.md (yeni); değişen: .claude/settings.json, SISTEM (0.3), MOC-devlet, arastirma/10 (1.1), HARITA, DEGISIKLIKLER
- Kapanış notu: Sandbox açık ve gerçek oturumda doğrulandı (ev dizinine yazma, proxy dışı ağ, .claude/hooks yazma reddedildi; ~/.config/gh ve keyrings boş göründü; kontrol.py çalıştı). Açık: klasör yeni adıyla güvenilir değil (sahibi bir kez etkileşimli claude açıp onaylamalı); maliyet tahmini gerçek faturadan ~%30 düşük (1 saatlik önbellek yazımı 2× fiyatlanıyor) → ccusage mutabakatı (öncelik 7).

## T-009 — graf.py: Graphify'ı LLM'siz kütüphane olarak bağla (öncelik 2)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 2: frontmatter bağlarından (dayandigi, ust) ve gövde wikilink'lerinden sayfa grafı kurmak; Graphify ile topluluk, merkez düğüm, sınır aşan bağ ve HTML görünümü üretmek; kopuk küme ve yetim sayfayı raporlamak.
- Başarı ölçütü: graf.py çalışır (çıkış 0), graphify yokken çıkış 2; çıktılar 00-sistem/.kosu/graf/ (git dışı); kurulu paket incelenen 0.9.77 ile birebir (sha256); ARAC-KAYDI satırı; kontrol.py sıfır hata.
- Sınırlar: graphify install, git hook'ları, --mode deep yok; LLM çağrısı yok. Bulunan yapısal sorunlar düzeltilmez, raporlanır.
- Kat: 0
- Kapı: cift-yonlu · araç kaydı A10 değil (dış erişim vermez; B7, sahibinin sıra onayı 2026-10-06)
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/graf.py (yeni), .venv/ (git dışı); değişen: yscommon.py, sikistirma-oncesi.py, settings.json, CLAUDE.md, uyku SKILL.md, ARAC-KAYDI (0.3), .gitignore, DEGISIKLIKLER
- Kapanış notu: graf.py çalışıyor (doğrudan ve sandbox içinde çıkış 0; graphify yokken 2). İlk bulgu: 40-ic-ses katı (MOC-ic-ses, F-0001, nerede-kaldik) sistemin geri kalanından kopuk; düzeltme sahibinin içerik kararı (öneri: MOC-ic-ses dayandigi += arastirma/08, ya da SISTEM besledigi += MOC-ic-ses).

## T-010 — qmd: yerel anlamsal arama (öncelik 3)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 3: wiki için yerel hibrit arama (BM25 + vektör + yeniden sıralama). Proje içine sabit sürümle kurulur (`.araclar/`, git dışı); dizin ve modeller proje içinde tutulur ki sandbox içinden güncellenebilsin. Türkçe isabet ölçülür.
- Başarı ölçütü: `ara.py` sarmalayıcısı çalışır; 20 Türkçe sorguda isabet@3 ölçülür ve BM25 ile karşılaştırılır; sonuç 40-ic-ses/arastirma-notlari'na yazılır; 01-gelen dizine girmez; kontrol.py sıfır hata.
- Sınırlar: Global kurulum yok. MCP sunucusu (.mcp.json) yalnız ölçüm tatmin ediciyse eklenir. Modeller yalnız ilk kurulumda HuggingFace'ten iner (sonra ağ yok).
- Kat: 0
- Kapı: cift-yonlu · yerel araç, dış erişim vermez (B7); sahibinin sıra onayı 2026-10-06
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/ara.py, 00-sistem/scripts/ara-olcum.py, 40-ic-ses/arastirma-notlari/qmd-turkce-isabet.md (yeni), .araclar/ (git dışı); değişen: şema + SEMA (0.3) + kontrol.py (sonuc türleri), ARAC-KAYDI (0.4), MOC-ic-ses (0.2), arastirma/10 (1.2), settings.json, CLAUDE.md, HARITA, DEGISIKLIKLER
- Kapanış notu: Vektör arama Türkçe çalışıyor (%75@1, %90@3, 4.5 sn); kelime araması Türkçe cümlede %0; hibrit daha kötü. MCP eklenmedi (30 sayfada gereksiz; 100 sayfada yeniden ölç). Yan etki: not araştırma 10'a dayandığı için 40-ic-ses kopuk kümesi bağlandı (graf: 1 bileşen). T-005 kalıntısı sonuc şema uyumsuzluğu düzeltildi.

## T-011 — Ayar denetimi hook'u (öncelik 4)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 4: `.claude` ayarlarının kendisine "kural ile engel ayrıdır" ilkesini uygulamak. Güvenlik değişmezlerini (sandbox, deny kuralları, koruma hook'ları, izin kipi) bozan ayar değişikliği oturum içinde engellenir; oturum açılışında diskteki ihlal uyarılır; her geçerli değişiklik anahtar düzeyinde GUNLUK'e yazılır; auto kipte izin reddi kaydedilir.
- Başarı ölçütü: değişmez listesi tek yerde; örnek girdilerle (geçerli, ihlal, imzalı istisna, geçersiz JSON, skills, izin reddi, açılış uyarısı) beklenen karar; gerçek oturumda dışarıdan yapılan sandbox kapatma girişimi engellenir ve kaydedilir; kontrol.py sıfır hata.
- Sınırlar: Değişen dosya geri alınmaz (yalnız oturuma yüklenmesi engellenir, sahibine bildirilir). policy_settings engellenemez (belge). Kullanıcı ayarına yazılmaz.
- Kat: 0
- Kapı: cift-yonlu · sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: .claude/hooks/ayar-denetimi.py (yeni); değişen: settings.json (ConfigChange, PermissionDenied, SessionStart), kapanis-kaydi.py, SISTEM (0.4), CLAUDE.md, DEGISIKLIKLER
- Kapanış notu: 17 durumluk izole test doğru; gerçek oturumda dışarıdan diske yazılan sandbox kapatma ayarı yüklenmedi, ev dizinine yazma reddedildi, engelleme GUNLUK'te. İlk gerçek testte sandbox'ın 0 baytlık yer tutucusu "geçersiz JSON" diye engellenip 2 gürültü satırı yazdı (GUNLUK 00:48); boş dosya artık "ayar yok" sayılıyor, farksız değişiklik yazılmıyor. Açık: IMZA-MATRISI'ne imzalı istisna satırı eklemek sahibinin işi (norm).

## T-012 — Gelen kutusu besleme: belge ve web → 01-gelen (öncelik 5)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 5: PDF/DOCX/PPTX/XLSX/HTML ve URL'yi yerelde markdown'a çevirip şablona uygun ham not olarak 01-gelen'e koyan `al.py`; Obsidian Web Clipper şablonu. Dönüştürücü kanıtla seçilir (önce hafif markitdown; Türkçe PDF'te yetmezse docling).
- Başarı ölçütü: gerçek bir Türkçe PDF ve bir DOCX/HTML örneği dönüşür, Türkçe karakter ve tablo korunur (örnek satırlar kanıt); üretilen not kontrol.py'den geçer; kötü niyetli meta veri (başlıkta YAML kırıcı karakter) frontmatter'ı bozmaz; içerik ara.py dizinine girmez.
- Sınırlar: Dönüşen içerik okunmaz/özetlenmez (okuyucu işi). Web Clipper kurulumu ve telefon eşlemesi (Syncthing) sahibinin insan noktası; yalnız şablon ve talimat hazırlanır. URL alma ağ ister: sandbox içinde alan adı onayı gerekir.
- Kat: 0
- Kapı: cift-yonlu · yerel araç (B7); sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/al.py, 00-sistem/sablonlar/web-clipper-gelen.json (yeni); değişen: kontrol.py, graf.py, settings.json (env + allow), ARAC-KAYDI (0.5), SISTEM (0.5), CLAUDE.md, DEGISIKLIKLER
- Kapanış notu: markitdown Türkçe PDF'te kayıpsız (73 bin karakter, 0 bozuk, tablolar korunur); kötü niyetli başlık ve dosya adı frontmatter'ı bozmadı; sahte wikilink kontrolü kırmadı; sandbox içinde çalışıyor. docling kurulmadı (kanıtla). Beklenmeyen bulgu: onnxruntime 1.30 Microsoft telemetrisi (cihaz kimliği + 24 olaylık kuyruk ~/.cache/Microsoft/DeveloperTools/.onnxruntime/, sandbox'ta proje köküne ":memory:.ses"); ORT_DISABLE_TELEMETRY=1 ile durduruldu, resmi disable_telemetry_events() etkisiz. Kayıt betiği tırnak hatasıyla çalışmadan commit atıldı (bd868ba); kayıtlar ayrı commit'le tamamlandı. Açık: kuyruğun silinmesi sahibinin kararı (proje dışı); Web Clipper şablonu gerçek eklentide sınanmadı.

## T-013 — Bağlantı canlılığı (lychee) ve maliyet mutabakatı (ccusage) (öncelik 6)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 6'nın yerel parçaları: kaynak sayfalarındaki URL'lerin canlılığını denetleyen `canli.py` (lychee) ve MALIYET.csv tahminini Claude Code oturum kayıtlarıyla karşılaştıran `maliyet.py` (ccusage). agent-scan bu talimatta YOK: içerik Snyk API'sine gider ve hesap ister (araştırma 10'daki "yerel" bilgisi yanlıştı); sahibinin kararı bekleniyor.
- Başarı ölçütü: iki betik çalışır (çıkış kodu anlamlı); ilk canlılık raporu ve ilk mutabakat sonucu kanıt olarak; 01-gelen URL'leri denetlenmez (güvenilmeyen); kontrol.py sıfır hata.
- Sınırlar: Ölü bağlantı otomatik düzeltilmez (rapor; düzeltme /degistir ile). MALIYET.csv satırları yeniden yazılmaz. Sürüm sabit, proje içine kurulum (.araclar).
- Kat: 0
- Kapı: cift-yonlu · yerel araçlar (B7); sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/canli.py, 00-sistem/scripts/maliyet.py (yeni), .araclar/lychee, .araclar/ccusage (git dışı); değişen: kapanis-kaydi.py, settings.json, CLAUDE.md, haftalik SKILL.md, ARAC-KAYDI (0.6), arastirma/10 (1.3), DEGISIKLIKLER
- Kapanış notu: canli.py ilk rapor: 414 bağlantı, 401 canlı, 3 kesin ölü (404: arastirma/03 ADP 6-0 PDF; arastirma/07 enerji.gov.tr imza yönergesi ve anayasa.gov.tr norm kararı PDF'leri), 6 belirsiz. maliyet.py: T-013 öncesi 9 satır ccusage'in %27-34 altında (kök neden: önbellek yazımı tek tip 1.25×); kapanis-kaydi TTL ayrımıyla düzeltildi, yeni satır %0.0 fark. Sandbox içinde maliyet.py çalışıyor; canli.py ağ istediği için sahibi çalıştırır. agent-scan kurulmadı (veri Snyk'e gider). Ara hata: geçici sunucuları kapatan pkill kendi kabuğunu da öldürdü; kayıt ikinci denemede yazıldı. Açık: 3 ölü bağlantının sayfaları (kaynak) /degistir ile güncellenmeli ya da UNCONFIRMED işaretlenmeli — sahibinin onayıyla.

## T-014 — Ölü kaynak bağlantılarının düzeltilmesi
- Tarih: 2026-10-07
- Niyet: canli.py'nin T-013'te bulduğu 3 kesin ölü (404) bağlantıyı (arastirma/03: ADP 6-0 PDF; arastirma/07: ETKB imza yetkileri yönergesi, AYM norm kararı 2024/51) resmi güncel adresleriyle değiştirmek; bulunamazsa UNCONFIRMED işaretlemek.
- Başarı ölçütü: her bağlantı için ya doğrulanmış yeni adres (canlı + belge kimliği eşleşiyor) ya da UNCONFIRMED notu; eski adres sayfa günlüğünde; canli.py'de bu üçü ölü listesinde yok; kontrol.py sıfır hata.
- Sınırlar: Raporların içeriği (iddialar) değiştirilmez; yalnız kaynak adresi ve gerekirse doğrulanamayan iddiaya UNCONFIRMED etiketi.
- Kat: 0
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: değişen: 00-sistem/arastirma/03-cok-ajanli-isleyis-ve-yonetisim.md (1.1), 00-sistem/arastirma/07-devlet-yapilari.md (1.1); ikisine sayfa günlüğü eklendi
- Kapanış notu: ETKB yönergesi düzeltildi (sorun Türkçe karakterlerin ASCII'ye çevrilmesiydi; belge kimliği doğrulandı). AYM 2024/51 resmi bağlantısı kaldırılmış; Lexpera Resmî Gazete metniyle değiştirildi (başlık doğrulandı). ADP 6-0 resmi PDF'i kaldırılmış, yeni baskının adresi bulunamadı; FAS kopyası bot koruması yüzünden doğrulanamadı → UNCONFIRMED. canli.py iki sayfada 0 ölü. Eski adresler sayfa günlüklerinde kod olarak duruyor (canlılık denetimine girmesin diye).

## T-015 — İç Ses ses hattı, 1. kısım: /voice Türkçe (öncelik 7)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 7'nin sahibin katılımını gerektirmeyen kısmı: Claude Code dikte dilini Türkçe yapmak (`language` ayarı; aynı ayar yanıt dilini de belirler). Etkinleştirme (/voice, mikrofon denetimi) ve yerel TTS denemesi sahibinin katılımıyla ayrı talimatta.
- Başarı ölçütü: proje ayarında `language: turkish`; ayar-denetimi değişmezleri bozulmuyor; ARAC-KAYDI'nda "ses Anthropic'e gider" notu; kontrol.py sıfır hata.
- Sınırlar: /voice burada açılmaz; kullanıcı ayarına ve tuş atamalarına dokunulmaz; TTS kurulmaz.
- Kat: 0
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: değişen: .claude/settings.json (language), 10-insan/araclar/ARAC-KAYDI.md (0.7)
- Kapanış notu: Dikte dili Türkçe (belge: Türkçe `tr` destekli; language yanıt dilini de belirler). Ayar denetimi değişmezleri tamam. Sıradaki (sahibin katılımıyla): /voice ile mikrofon denetimi ve deneme dikte; yerel TTS (FreyaTTS hafif / Chatterbox GPU) ses örnekleri.

## T-016 — İç Ses ses hattı, 2. kısım: yerel Türkçe TTS denemesi (öncelik 7)
- Tarih: 2026-10-07
- Niyet: Araştırma 10'un "Türkçe kalitesi ölçülmeden bağımlılığa çevrilmez" şartıyla, yerel Türkçe TTS adayını (FreyaTTS, Apache-2.0, 183M) proje dışı izole ortamda (.araclar/tts, git dışı) kurup Türkçe örnek ses dosyaları üretmek ve hızını (RTF) ölçmek. Kalite yargısı sahibinin kulağına bırakılır.
- Başarı ölçütü: sabit commit'li kurulum; Türkçe karakter, sayı ve İngilizce terim içeren örnek cümlelerden WAV dosyaları; RTF ölçümü; ağ erişimi yalnız model indirmede; sonuç 40-ic-ses/arastirma-notlari'na; kontrol.py sıfır hata.
- Sınırlar: Bağımlılık yapılmaz (hook/skill entegrasyonu yok); ses klonlama yok; Chatterbox (GPU, birkaç GB) bu talimatta yok.
- Kat: 0
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 40-ic-ses/arastirma-notlari/freyatts-turkce-deneme.md (yeni), .araclar/tts (git dışı), 00-sistem/.kosu/tts-ornek/*.wav (git dışı); değişen: arastirma/10 (besledigi), MOC-ic-ses, ARAC-KAYDI (0.8)
- Kapanış notu: FreyaTTS CPU'da kuruldu (torchaudio CUDA/CPU uyumsuzluğu 2.11 CPU sürümleriyle çözüldü), 4 Türkçe örnek üretildi (00-sistem/.kosu/tts-ornek). RTF 2.5–12 (iddia 0.70); Whisper ile anlaşılırlık: günlük %7, Türkçe harf %25, sayı %53 (çoğu rakam yazımı), İngilizce terim %60. Sonuç notu: 40-ic-ses/arastirma-notlari/freyatts-turkce-deneme (celisiyor). Bağımlılık yapılmadı. Açık: sahibi örnekleri dinler; GPU denemesi (~3 GB) sahibinin kararı.

## T-017 — Sahibinin 2026-10-07 kararlarının işlenmesi
- Tarih: 2026-10-07
- Niyet: Sahibinin sohbette verdiği dört kararı kayda geçirmek: K-004 kabul; F-0001 yazıcı türü "henüz bilmiyorum"; agent-scan kurulmayacak; onnxruntime telemetri kuyruğu silinsin.
- Başarı ölçütü: K-004 durum kabul (1.0) ve KARARLAR/MOC; F-0001 0.3 cevaplı; G-001 HP-001 ve HP-002 kapalı (kanban bekliyor); ARAC-KAYDI agent-scan kararı; ~/.cache/Microsoft/DeveloperTools/.onnxruntime yok; kontrol.py sıfır hata.
- Sınırlar: G-001 bu talimatta başlatılmaz (ayrı talimat). K-002 ve hafif yol kararlarına dokunulmaz.
- Kat: 0
- Kapı: cift-yonlu · imza: sahibi (sohbet, 2026-10-07)
- Durum: kapali
- Doğurduğu dosyalar: değişen: K-004 (1.0 kabul), KARARLAR, MOC-devlet, F-0001 (0.3), G-001 (0.2), MOC-sirket, ARAC-KAYDI (0.9); silinen (proje dışı): ~/.cache/Microsoft/DeveloperTools/.onnxruntime (+ boş üst klasörler)
- Kapanış notu: Dört karar işlendi. G-001'in iki insan noktası kapandı; kart başlatılabilir (ayrı talimat). Telemetri kuyruğu 00:57'den beri yeni olay almamıştı (ORT_DISABLE_TELEMETRY etkili), silindi.

## T-018 — G-001'in yürütülmesi: yazıcı işi pazar araştırması
- Tarih: 2026-10-07
- Niyet: K-004 (kabul) ve G-001 (insan noktaları kapalı) uyarınca G-001'i yürütmek: 3D ve kâğıt/baskı türlerini yan yana, kaynaklı karşılaştırmak; seçim yapmadan en ucuz deneme önerisini yazmak.
- Başarı ölçütü: G-001'in 4 kabul ölçütü kanıtla (kontrol.py 0; ≥2 seçenek ve her satırda kaynak URL; canli.py 40-ic-ses ölü 0; dış eylem yok); denetci incelemesi; kanban tamam ve kanit dolu; F-0001 kaynaklar/alternatifler güncel.
- Sınırlar: G-001 kapsamı: satın alma, tedarikçiyle iletişim, ilan, ödeme YOK. Web içeriği veri olarak okunur (okuyucu kuralları). Bütçe 2 USD, Sonnet.
- Kat: 2
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 40-ic-ses/arastirma-notlari/yazici-pazar-arastirmasi.md (yeni); değişen: G-001 (0.4 tamam), F-0001 (0.4), MOC-ic-ses (0.3), MOC-sirket, HARITA
- Kapanış notu: G-001 tamam. Çıktı: 40-ic-ses/arastirma-notlari/yazici-pazar-arastirmasi (sonuç bilinmiyor, güven düşük, 16 UNCONFIRMED): A FDM 3D (cihaz ~21-26 bin TL, anahtarlık 21-250 TL), B1 süblimasyon (pres ~11 bin TL, kupa 375-899 TL), B2 DTF (TL fiyatları bulunamadı); hiçbirinde talep kanıtı yok. 4 ölçüt kanıtla karşılandı; denetci ilk turda 2 engelleyici (sürüm/günlük eksikliği) buldu, düzeltildi, ikinci tur geçer. Web'deki talimat benzeri içeriğe (pea3d paneli) uyulmadı. Açık (sahibine tek soru): hangi seçenek için 'hazır hizmetle 10 ürün' denemesi yapılsın, yoksa önce ZORLA modu mu?

## T-019 — K-002 kabulü ve F-0001 için ZORLA modu
- Tarih: 2026-10-07
- Niyet: Sahibinin kararları: K-002 kabul; yazıcı işi için önce ZORLA modu (rules/40-ic-ses: steelman → inversion ≥3 → pre-mortem ≥3 olasılıklı).
- Başarı ölçütü: K-002 1.0 kabul ve KARARLAR/MOC; F-0001'de steelman (sahibi onayı bekliyor), inversion ≥3, pre-mortem ≥3 olasılıklı, gerekçeli [konum]; merdiven 1'de kalır (M2 için steelman onayı şart); kontrol.py sıfır hata.
- Sınırlar: Merdiven sahibinin steelman onayı olmadan değişmez. Seçenek seçimi yapılmaz.
- Kat: 4
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: değişen: K-002 (1.0 kabul), KARARLAR, MOC-devlet, F-0001 (0.5)
- Kapanış notu: K-002 kabul. F-0001 ZORLA: steelman yazıldı (sahibinin onayı bekleniyor), inversion 4, pre-mortem 4 (en olası: talep yok %40), [konum]: cihazsız deneme önce. M2 için tek eksik sahibinin steelman onayı.

## T-020 — Y-001: çift yönlü kararlarda yetki devri
- Tarih: 2026-10-07
- Niyet: Sahibinin talimatı ("bu tarz seçimleri neden bana yaptırıyorsun … bunu benim için ayarlayamaz mısın"): çift yönlü kararlar orkestratörde; sahibine yalnız imza matrisi (A1–A11), dışarıya veri gönderen araçlar, proje dışı silme ve fiziksel eylemler sorulur.
- Başarı ölçütü: Y-001 yönergesi yayımlandı (KARARLAR satırı, MOC-devlet), IMZA-MATRISI ile iki yönlü bağ, CLAUDE.md'de tek satır; kontrol.py sıfır hata.
- Sınırlar: Anayasa ve imza matrisinin içeriği değişmez (Madde 6: sahibine ayrılanlar yönergeyle daraltılamaz).
- Kat: 3
- Kapı: cift-yonlu · imza: orkestratör (Başkan a.), sahibinin yazılı talimatıyla
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/normlar/yonergeler/Y-001-cift-yonlu-karar-yetki-devri.md (yeni); değişen: IMZA-MATRISI (bağ), MOC-devlet, KARARLAR, CLAUDE.md, HARITA; ayrıca Claude hafızası (karar-yetkisi-cift-yonlu)
- Kapanış notu: Y-001 yürürlükte. Kendi hatam: K-002, K-004, deneme sırası ve ZORLA gibi çift yönlü seçimleri sahibine sordum; anayasa Madde 9 ve rules/30-devlet bunları orkestratöre bırakıyordu. Bundan sonra yalnız imza matrisi ve fiziksel eylemler sorulur.

## T-021 — KR-001 hafif yol kural taslağı ve not.py
- Tarih: 2026-10-07
- Niyet: Sahibinin "kural taslağı hazırla" kararı: İç Ses gözlem ve M0 fikir için altı adımı tek komutla yapan hafif yol (KR-001, önerildi) ve uygulayıcısı not.py (kural kabul edilmeden kilitli). Fikir şablonundaki merdiven/cynefin çelişkisi de düzeltilir.
- Başarı ölçütü: KR-001 şablona uygun (amaç, sunset, DEA-lite); not.py kural önerildiyken çıkış 3; karalama kopyasında kural kabul varsayılarak gözlem ve fikir eklenir ve kontrol.py 0; fikir şablonu kontrol.py ile çelişmez; kontrol.py sıfır hata.
- Sınırlar: Kural yayımı sahibinin imzasıdır (A4); bu talimat yayımlamaz. CLAUDE.md'nin altı adım kuralı değişmez.
- Kat: 3
- Kapı: tek-yonlu (yayım) · taslak çift yönlü
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/normlar/kurallar/KR-001-hafif-yol.md, 00-sistem/scripts/not.py (yeni); değişen: MOC-devlet, sablonlar/fikir.md, CLAUDE.md, DEGISIKLIKLER, HARITA
- Kapanış notu: KR-001 önerildi; not.py kural kabul edilmeden çıkış 3 (doğrulandı). Karalama kopyasında kural kabul varsayılarak 1 gözlem + 2 M0 fikir eklendi; sayfalar, MOC M0 satırı, gözlem listesi, talimat aç/kapa doğru. Yayım sahibinin imzası (A4).

## T-022 — KR-001 yayımı ve F-0001 steelman onayı (sahibinin imzaları)
- Tarih: 2026-10-07
- Niyet: Sahibinin iki imzasını işlemek: KR-001 kabul ve yürürlük (A4, kapı KP-002); F-0001 steelman onayı → merdiven 2.
- Başarı ölçütü: KR-001 1.0 kabul, KARARLAR satırı, KP-002 go; not.py kilidi açık; F-0001 merdiven 2 ve MOC-ic-ses tablosu; kontrol.py sıfır hata.
- Sınırlar: Yalnız imzalanan iki kalem.
- Kat: 3
- Kapı: tek-yonlu (kural yayımı) · imza: sahibi (sohbet, 2026-10-07)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kapilar/KP-002-kr-001-yayimi.md (yeni); değişen: KR-001 (1.0 kabul), KARARLAR, MOC-devlet, F-0001 (0.6, merdiven 2), MOC-ic-ses, HARITA
- Kapanış notu: KR-001 yürürlükte (KP-002 go); not.py kilidi açık (boş girdi çıkış 2 = kilit geçildi). F-0001 M2 (sınanmış). Bir sonraki fikir adımı (M3: açık soru ≤2, canlı kaynaklar) ve deneme seçimi Y-001 uyarınca orkestratörde, sahibinin ilgisine bağlı tür seçimi sahibinde.

## T-023 — ARAŞTIR: esnaf muafiyeti çelişkisi (F-0001 → M3 koşulu)
- Tarih: 2026-10-07
- Niyet: F-0001'in M3 (araştırılmış) koşulu "çelişki cevaplanmış". G-001 notundaki esnaf muafiyeti çelişkisini (limit 396.360 / 1.900.000 / 1.983.000 TL; makineyle üretim ve al-sat kapsamı) resmi kaynaklarla (GVK md. 9/6, GİB, Resmî Gazete) çözmek. Y-001 Madde 2.1 (ARAŞTIR modu orkestratörde).
- Başarı ölçütü: resmi kaynaklı araştırma notu (sonuc: dogruluyor/celisiyor/bilinmiyor); her iddia URL + tarih; canli.py 40-ic-ses ölü 0; F-0001 çelişki bölümü güncel; M3 koşulları değerlendirilmiş; kontrol.py sıfır hata.
- Sınırlar: Hukuki/vergi görüşü değildir; mali müşavire sorulacak sorular listelenir. Dış eylem yok.
- Kat: 4
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 40-ic-ses/arastirma-notlari/esnaf-muafiyeti-yazici.md (yeni); değişen: F-0001 (0.7, merdiven 3), yazici-pazar-arastirmasi (bağ), MOC-ic-ses, HARITA
- Kapanış notu: Çelişki kanun metniyle çözüldü: 9/6 (motorsuz, sayılı ev ürünleri) yazıcı işine uygulanmaz; 9/10 (evde, seri üretim makinesi olmadan, internet satışı, banka %4 kesinti, hasılat sınırı metinde 1.900.000 TL) cihazın makine yorumuna bağlı → açık soru (mali müşavir/özelge). F-0001 M3 (Y-001). canli.py 0 ölü.

## T-024 — Obsidian kasası: .obsidian/ için dar istisna (kural 7) ve git dışı
- Tarih: 2026-10-07
- Niyet: Sahibinin "evet, .obsidian için talimatı aç" talimatı. Klasör Obsidian kasası olarak açılınca kök dizinde doğacak `.obsidian/` ayar klasörünün kural 7'yi (kat dışına yazma yok) ve git durumunu bozmaması: karar kaydı (K-005), `.gitignore` satırı, Obsidian'ın yeni not ve ekleri köke değil `01-gelen/`'e koyması için ön ayar (`.obsidian/app.json`).
- Başarı ölçütü: K-005 kabul ve KARARLAR satırı; `git check-ignore .obsidian/app.json` çıkış 0; app.json geçerli JSON; tarama betikleri `.obsidian`'ı görmüyor; kontrol.py sıfır hata.
- Sınırlar: CLAUDE.md kural metni değişmez (istisna K-005'te). Obsidian'ı açmak, eklentiyi kurmak sahibinin fiziksel adımı. Proje dışına (~/.config/obsidian) yazılmaz.
- Kat: 3
- Kapı: cift-yonlu · onay: sahibi (sohbet, 2026-10-07)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kararlar/K-005-obsidian-kasa-istisnasi.md (yeni); değişen: .gitignore, KARARLAR, MOC-devlet, ARAC-KAYDI, HARITA; git dışı: .obsidian/app.json
- Kapanış notu: `.obsidian/` kural 7'ye dar istisna (K-005) ve git dışı; yeni not ve ekler 01-gelen'e. Açık: kasayı Obsidian'da açmak ve Web Clipper kurulumu sahibinin fiziksel adımı.

## T-025 — Kapanış kayıtlarını kontrol.py ile zorunlu kıl (eksik analizi #2)
- Tarih: 2026-10-07
- Niyet: Sahibinin "eksikleri tamamlayalım" talimatı. 2026-10-07 analizi: nerede-kaldik.md T-000'dan beri güncellenmemiş, ILERLEME.md "Son kanıt" 26 sayfada kalmış; /kapat'ın 3. adımı elle kapanışlarda atlanıyor ve hiçbir denetim yakalamıyor. Kural metinde var, engel yok (Anayasa ilke 6).
- Başarı ölçütü: kontrol.py 16. denetim: son kapanan talimatın GUNLUK [oturum] satırı, ILERLEME.md ve nerede-kaldik.md'de izi yoksa hata; birden çok açık talimat hata; ILERLEME aktif_talimat kapalı bir talimatı gösteriyorsa hata. Denetim eski hâl üzerinde hata verir (negatif kanıt), düzeltilmiş hâlde kontrol.py sıfır hata.
- Sınırlar: Eski talimatların kayıtları geriye dönük yeniden yazılmaz; yalnız son kapanış denetlenir. "Oturumda tek talimat" kuralının metni değişmez.
- Kat: 0
- Kapı: cift-yonlu · onay: sahibi (sohbet, 2026-10-07)
- Durum: kapali
- Doğurduğu dosyalar: değişen: 00-sistem/scripts/kontrol.py (16. denetim), 00-sistem/ILERLEME.md (yeniden düzen), 40-ic-ses/nerede-kaldik.md (0.2), 00-sistem/SEMA.md (0.4), .claude/skills/kapat/SKILL.md, DEGISIKLIKLER
- Kapanış notu: Kapanış kaydı artık engelle sağlanıyor: kontrol.py 16. denetim eski hâlde 2 hata verdi (nerede-kaldik T-024 yok, aktif_talimat yanlış), düzeltmeden sonra 0.

## T-026 — GitHub açık depo, gizli e-posta ve otomatik push (eksik analizi #5)
- Tarih: 2026-10-07
- Niyet: Sahibinin "4k claude neden github'da yok?" sorusu ve "Açık depo" + "Gizli adrese çevir" seçimleri. Eksik analizi #5 (yedek yok): depo yalnız ~/Downloads'ta, uzak kopya yok.
- Başarı ölçütü: KP-003 go (A6, A9 sahibi); geçmişte gmail adresi kalmaz (`git log --format=%ae` yalnız noreply); github.com/kaan4kbulut/4k-claude açık ve `git status -sb` uzakla eşit; commit sonrası otomatik push (systemd path birimi) bir deneme commit'iyle kanıtlı; kayıtlarda geçen eski commit kimlikleri yenilendi; kontrol.py sıfır hata.
- Sınırlar: .araclar ve .venv yayımlanmaz (git dışı kalır). Sandbox ve izin ayarları değişmez (push sandbox dışından, systemd ile). Force push yok.
- Kat: 3
- Kapı: tek-yonlu (A6 dış API yazımı, A9 kamuya açık çıktı) · imza: sahibi (sohbet, 2026-10-07)
- Durum: acik
