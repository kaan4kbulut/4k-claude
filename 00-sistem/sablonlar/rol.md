---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: rol
kat: 2
surum: 0.1
durum: taslak
amac: Bu rol karti, ... rolunun neye sahip oldugunu, tek basina neye karar verebildigini ve neyi eskale ettigini tanimlamak icin var.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: ["30-devlet/normlar/IMZA-MATRISI.md"]
besledigi: []
ust: 20-sirket/MOC-sirket.md
sahip: kaan
model: sonnet
yazabildigi_yerler: []
etiketler: []
---

<!--
ROL KARTI — Agent Skills / alt ajan tanımıyla uyumlu; bu dosyadan .claude/agents/<rol>.md üretilir (kadro kapısı sonrası).
- Rol açma/kapama sahibinin kadro kapısıyla. Pilotta rol yok (K-001).
- Birim 4 görevden küçükse birleştir; bir rol 5-7'den fazla "koltuk" tutuyorsa böl.
- Yazabildiği yerler = yetki devri tablosu; başka yere yazamaz (hook ile sınırlanabilir).
-->

# Rol: <ad>

## Amaç
Bu rol kartı, … rolünün neye sahip olduğunu, tek başına neye karar verebildiğini ve neyi eskale ettiğini tanımlamak için var.

## İçerik
### Sahip olduğu (koltuklar, ≤ 5-7)
- …

### Girdiler
- (hangi sayfalar/kartlar/olaylar bu rolü tetikler)

### Çıktılar
- (hangi sayfaları, kartları, raporları üretir)

### Tek başına karar verebildikleri
- …

### Eskale ettikleri (asla tek başına karar vermez)
- (rules/20-sirket.md'deki 9 alandan ilgili olanlar + role özel)

### Yazabildiği yerler (yetki devri)
| Klasör / dosya | Yetki | Dayanak |
| --- | --- | --- |
| … | yaz / oku | Y-xxx |

### Model ve bütçe
model: sonnet · çaba: medium · maxTurns: 20 · haftalık token tavanı: … (MODEL-POLITIKASI)

### Alt ajan tanımı taslağı (.claude/agents/<rol>.md)
```yaml
name: <rol>
description: <ne zaman devredilir; "use proactively" gerekiyorsa>
tools: Read, Grep, Glob, Edit, Write, Bash
model: sonnet
maxTurns: 20
memory: project
```
Gövde: bu kartın "Sahip olduğu", "Eskale ettikleri" ve "Yazabildiği yerler" bölümleri.

### Performans (karne)
| Dönem | Kapanan kart | Kanıtlı kapanış % | Eskalasyon | Not |
| --- | --- | --- | --- | --- |

## Bağlar
### Dayandığı
- [[30-devlet/normlar/IMZA-MATRISI]] — yetki sınırları buradan
### Beslediği
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu |
