---
id: 20261007-1926-kr-002-zamanli-kosular
ad: kr-002-zamanli-kosular
tur: kural
kat: 3
surum: 0.1
durum: onerildi
amac: Bu kural, zamanli ve gozetimsiz kosularin yalniz hazirla adimi yapmasini zorunlu kilmak icin var; amaci sahibinin onayi olmadan yayin, mesaj ya da bagli dis sisteme yazim riskini onlemektir.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-043
dayandigi: [10-insan/kaynaklar/yz-teknoloji-taramasi-2026-10-07.md]
besledigi: [30-devlet/kapilar/KP-004-kr-002-yayimi.md]
ust: 30-devlet/MOC-devlet.md
kapi: tek-yonlu
karar_veren: kaan
yururluk: belirlenmedi
yuruten: orkestrator
sunset: 2027-01-05
yerine_gecti:
yerine_gecen:
saklama: S
etiketler: [kural/guvenlik, arac/claude-code]
---

# Kural KR-002: Zamanlı koşular yalnız hazırlar

## Amaç
Bu kural, zamanlı ve gözetimsiz koşuların yalnız "hazırla" adımı yapmasını zorunlu kılmak için var; amacı sahibinin onayı olmadan yayın, mesaj ya da bağlı dış sisteme yazım riskini önlemektir.

## İçerik
### Madde 1 — Kapsam
4k-claude adına sahibi başında olmadan çalışan her koşu: Claude Code Routines (`/schedule`, bulut rutinleri), `00-sistem/scripts/calistir.sh` gözetimsiz koşuları, CronCreate/RemoteTrigger ile kurulan zamanlamalar ve bunların açtığı alt ajanlar. KP-003 otomatik git push birimi (sahibinin imzasıyla kurulu) kapsam dışıdır.

### Madde 2 — Hüküm
1. Zamanlı koşu yalnız okur, hesaplar ve taslak üretir; çıktısını depo içine (`01-gelen/` ya da `00-sistem/.kosu/`) yazar. İş "hazırla (gözetimsiz) → onayla (sahibi) → uygula (sonraki, gözetimli oturum)" diye bölünür.
2. Zamanlı koşuya bağlayıcı (MCP sunucusu, konektör, OAuth'lu dış hesap) bağlanmaz.
3. Yayın içeren rutin kurulmaz: artifact/web yayını, e-posta, mesaj, pazar yeri ilanı, ödeme ve her türlü dış API yazımı (IMZA-MATRISI A6, A9).
4. Her rutin kurulumu ve değişikliği GUNLUK'e `[ayar]` satırıyla düşer; yeni rutin A10 (yeni araç) sayılır.

### Madde 3 — İstisnalar
Sahibinin ayrı bir kapı kaydıyla (`sonuc: go`) adıyla imzaladığı rutin; kapı kaydı rutinin tam kapsamını yazar.

### Madde 4 — Yürürlük ve yürütme
Bu kural sahibinin imzasıyla (KP-004) KARARLAR.md'ye yazılarak yürürlüğe girer; orkestratör uygular; 2027-01-05'te gözden geçirilir, uzatılmazsa yürürlükten kalkar.

### DEA-lite (düzenleyici etki analizi)
| Soru | Cevap |
| --- | --- |
| İhtiyaç: hangi sorun, hangi kanıt | Tarama: "Routines onaysız artifact yayımlıyor, konektörler izinsiz" (UNCONFIRMED, raporda URL yok). Kanıttan bağımsız risk: gözetimsiz koşuda onay sorusu sorulamaz (rules/10-insan); yayın ve dış yazım geri alınamaz (A6). |
| Alternatifler (kural çıkarmama dahil) | 0) Kural yok: rules/10-insan'daki "hazırla → onayla → uygula" ilkesi metin olarak kalır, bağlayıcı/yayın yasağı yazılı değil. A) Bu kural. B) Routines'i tümden yasaklamak: hazırlık işlerini de keser. |
| Etkilenen roller / sayfalar | Orkestratör; calistir.sh; /uyku ve /inbox-triage'ın zamanlı koşuları; ileride /haftalik. Rol yok (K-001). |
| Maliyet (zaman, token, bağlam) | Yok denecek kadar az; rutin kurulumunda bir kapı adımı. |
| Risk ve azaltma | Rutin bir bağlayıcıyı sessizce kullanabilir → Madde 2.2 + kurulumun GUNLUK kaydı; denetim: haftalık gözden geçirmede rutin listesi. |
| Nasıl ölçülür (uygunluk) | Haftalık: kurulu rutinlerin listesi ↔ GUNLUK `[ayar]` satırları; bağlayıcı ya da yayın adımı içeren rutin sayısı = 0. |

### Write-round
| Rol | Görüş | Tarih |
| --- | --- | --- |
| (rol yok, K-001) | — | 2026-10-07 |

### Danışman görüşü (≤ 3 cümle)
Kural mevcut ilkeyi (rules/10-insan: gözetimsiz koşuda onay sorulamaz) araç ve yayın düzeyinde yazılı hâle getiriyor; dar ve geri alınabilir. Asıl risk kuralın metinde kalması: rutin kurulumu bir hook ile GUNLUK'e bağlanmazsa uygunluk ancak haftalık bakışla ölçülür.

### Denetim uygunluk notu
Anayasaya uygunluk: evet; Madde 6 (yetki) ve IMZA-MATRISI A6/A9 ile uyumlu, onları daraltmıyor, uygulamasını tarif ediyor. (Orkestratör ön notu; bağımsız Denetim rolü yok, K-001.)

### Değişiklik geçmişi (çerçeve taslak)
- 2026-10-07: Kural önerildi (T-043).

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — bu kuralın yetki kaynağı
- [[10-insan/kaynaklar/yz-teknoloji-taramasi-2026-10-07]] — Routines riskini bildiren tarama (iddia UNCONFIRMED)
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kurallar listesi
- ← [[30-devlet/kapilar/KP-004-kr-002-yayimi]] — imza kapısı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-043 | Oluşturuldu (onerildi) |
