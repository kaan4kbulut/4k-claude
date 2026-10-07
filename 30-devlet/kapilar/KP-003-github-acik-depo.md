---
id: 20261007-1200-kp-003-github-acik-depo
ad: kp-003-github-acik-depo
tur: kapi
kat: 3
surum: 1.0
durum: aktif
amac: Bu kapi kaydi, 4k-claude deposunun GitHub'da herkese acik yayimlanmasi ve her commit'ten sonra otomatik push karari icin sahibinin imzasini, kriterleri ve sonucu tutmak icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-026
dayandigi: []
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi_turu: adhoc
kapi: tek-yonlu
karar_veren: kaan
bekci: kaan
sonuc: go
saklama: S
etiketler: [kapi/yayin, kapi/dis-yazim]
---

# Kapı KP-003: GitHub açık depo ve otomatik push

## Amaç
Bu kapı kaydı, 4k-claude deposunun GitHub'da herkese açık yayımlanması ve her commit'ten sonra otomatik push kararı için sahibinin imzasını, kriterleri ve sonucu tutmak için var.

## İçerik
### Bağlam
Eksik analizi (2026-10-07) #5: depo yalnız `~/Downloads/4k-claude`'da, uzak kopya yok. Sahibi "4k claude neden github'da yok?" diye sordu. Push dış API yazımıdır (IMZA-MATRISI A6); açık depo kamuya açık çıktıdır (A9).

### Seçenekler ve uyarılar (sahibine sunuldu)
- Özel depo (önerilen) · açık depo · şimdilik yok (yerel bare repo). Açık depoda iş fikri (F-0001), vergi notları ve maliyet kayıtları herkese görünür; bu sahibine yazılı olarak söylendi.
- Commit'lerdeki kişisel e-posta: GitHub gizli adresine (52260768+kaan4kbulut@users.noreply.github.com) çevrildi; geçmiş push'tan önce yeniden yazıldı.

### Kriterler
- Zorunlu: izlenen dosyalarda parola, anahtar, telefon, IBAN yok (git grep taraması, 2026-10-07: 0 eşleşme).
- Zorunlu: `.araclar/`, `.venv/`, `00-sistem/.kosu/`, `.obsidian/`, `.env*` git dışı (.gitignore).
- Zorunlu: force push yok; otomatik push yalnız hızlı ileri (fast-forward) push dener, reddedilirse günlüğe yazar.

### İmza
Sahibinin imzası (IMZA-MATRISI A6, A9), 2026-10-07 sohbet: "Açık depo" ve "Gizli adrese çevir (Önerilen)" seçimleri.

### Sonuç
go — bekçi: kaan. Depo: https://github.com/kaan4kbulut/4k-claude (açık).

## Bağlar
### Dayandığı
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kapılar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-07 | T-026 | Sahibinin imzasıyla go |
