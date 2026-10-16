# Humanizer Bahasa Indonesia

Skill yang menghapus tanda-tanda tulisan buatan AI dari teks Bahasa Indonesia — artikel, laporan bisnis, caption medsos, dan **tugas akademik siswa/mahasiswa** (diskusi, praktikum, makalah, skripsi, proposal, jurnal, KKN, tugas sekolah).

Adaptasi Bahasa Indonesia dari [blader/humanizer](https://github.com/blader/humanizer), diperluas dengan [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) + pola khas AI berbahasa Indonesia hasil observasi.

---

## Isi Skill

| File | Isi |
|------|-----|
| `SKILL.md` | Aturan inti: 23 pola universal + 7 pola Indonesia (ID-1 s/d ID-7), gaya jawaban tugas, 4 Kaidah Emas struktur akademik |
| `references/template-jawaban.md` | **12 template** format tugas (T1–T12): diskusi, latihan bernomor, praktikum, esai, resume, kode, makalah, skripsi, proposal, jurnal IMRAD, magang/KKN, tugas sekolah SMP/SMA |
| `references/aturan-teknis.md` | PUEBI, margin, nomor halaman, sitasi, kesalahan struktur yang paling sering dinilai dosen |
| `references/placeholder.md` | Tanda bagian yang hanya bisa diisi user (logo, tanda tangan, data pribadi) — tidak dikarang |

---

## Cara Pasang

### Claude.ai (web)

1. Download `humanizer-id.skill` dari [Releases](../../releases)
2. **Settings → Skills → Upload** file `.skill`

### Claude Code

```bash
git clone https://github.com/adamhasani/humanizer-bahasa-indonesia.git ~/.claude/skills/humanizer-id
```

### Pasang Manual

```bash
mkdir -p ~/.claude/skills/humanizer-id
cp -r SKILL.md references ~/.claude/skills/humanizer-id/
```

### Cara pakai

```
/humanizer-id [tempel teks kamu]
```

atau langsung minta:

```
Tolong humanize teks ini: [teks]
```
```
Kerjakan tugas ini dengan gaya mahasiswa: [soal/tugas]
```

---

## Pola yang Dideteksi

### Universal (adaptasi dari pola bahasa Inggris, 23 pola)

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Significance inflation** | "menandai tonggak penting dalam evolusi..." | "didirikan pada 1989 untuk mengumpulkan statistik regional" |
| 2 | **Notability name-dropping** | "dikutip oleh Kompas, BBC, Financial Times" | "Dalam wawancara Kompas 2024, ia berpendapat..." |
| 3 | **Superficial -ing analyses** | "melambangkan... mencerminkan... menampilkan..." | Hapus atau ganti dengan sumber spesifik |
| 4 | **Promotional language** | "tersembunyi di kawasan Danau Toba yang menakjubkan" | "adalah desa di tepi Danau Toba" |
| 5 | **Vague attributions** | "Para ahli percaya sungai ini memainkan peran krusial" | "menurut survei 2019 oleh LIPI" |
| 6 | **Formulaic challenges section** | "Terlepas dari tantangan... terus berkembang" | Fakta spesifik tentang tantangan nyata |
| 7 | **AI vocabulary words** | "holistik, transformatif, krusial, lanskap, semarak" | Kata biasa yang lebih spesifik |
| 8 | **Copula avoidance** | "berfungsi sebagai... berperan sebagai... berdiri sebagai" | "adalah / merupakan" |
| 9 | **Negative parallelisms** | "Ini bukan hanya tentang X, ini tentang Y" | Langsung ke intinya |
| 10 | **Rule of three** | "inovasi, inspirasi, dan wawasan industri" | Jumlah item yang natural |
| 11 | **Synonym cycling** | "tokoh utama... protagonis... figur sentral... sang pahlawan" | Ulangi kata yang paling jelas |
| 12 | **False ranges** | "dari Big Bang hingga materi gelap" | Daftar topik langsung |
| 13 | **Em dash overuse** | "lembaga pemerintah—bukan masyarakat—namun terus berlanjut—" | Gunakan koma atau titik |
| 14 | **Boldface overuse** | "**OKR**, **KPI**, **BMC**" | "OKR, KPI, BMC" |
| 15 | **Inline-header lists** | "**Performa:** Performa meningkat..." | Ubah ke prosa |
| 16 | **Title Case headings** | "Negosiasi Strategis Dan Kemitraan Global" | "Negosiasi strategis dan kemitraan global" |
| 17 | **Emojis** | "🚀 Fase Peluncuran: 💡 Wawasan Kunci:" | Hapus emoji |
| 18 | **Chatbot artifacts** | "Pertanyaan bagus! Semoga membantu! Beritahu saya jika..." | Hapus seluruhnya |
| 19 | **Knowledge-cutoff disclaimers** | "Meskipun detail spesifisnya terbatas..." | Cari sumber atau hapus |
| 20 | **Sycophantic tone** | "Pertanyaan yang sangat bagus! Kamu benar sekali!" | Langsung ke substansi |
| 21 | **Filler phrases** | "Dalam rangka mencapai...", "Penting untuk dicatat bahwa" | "Untuk...", langsung ke klaimnya |
| 22 | **Excessive hedging** | "bisa jadi mungkin dapat diargumentasikan bahwa... mungkin" | "kemungkinan berdampak pada" |
| 23 | **Generic positive conclusions** | "Masa depan terlihat cerah. Waktu menggembirakan menanti..." | Rencana atau fakta spesifik |

### Khas Bahasa Indonesia (7 pola)

| # | Pattern | Before | After |
|---|---------|--------|-------|
| ID-1 | **Frasa birokratis** | "dalam rangka meningkatkan... guna memastikan... terkait dengan hal tersebut" | "untuk meningkatkan..." |
| ID-2 | **AI vocabulary Indonesia** | "holistik, komprehensif, transformatif, tak terbantahkan, berkelanjutan (abstrak)" | Kata konkret lebih spesifik |
| ID-3 | **"Tidak hanya... tetapi juga..."** | "Ini tidak hanya X, tetapi juga Y. Bukan sekadar A, melainkan B." | Satu kalimat langsung |
| ID-4 | **Konjungsi transisi rutin** | "Selain itu,... Lebih lanjut,... Di sisi lain,..." di setiap awal paragraf | Sambung lewat isi kalimat |
| ID-5 | **Redundansi pasif formal** | "dapat dilakukan dengan cara..., perlu diperhatikan bahwa..., patut dicatat bahwa..." | Kalimat aktif langsung |
| ID-6 | **Penutup moralistik/slogan** | "Oleh karena itu, penting bagi kita semua untuk senantiasa..." | Implikasi konkret, bukan seruan |
| ID-7 | **Judul slogan simetris** | "X: Fondasi Menuju Y" | Judul deskriptif spesifik |

---

## Lapisan Tugas Akademik

Untuk tugas siswa/mahasiswa, skill menambahkan 3 lapisan di atas humanizer dasar:

1. **Template per jenis tugas (T1–T12)** — dosen mengenali jawaban yang "formatnya salah". Setiap template punya struktur, aturan header, dan batasan apa yang tidak boleh ada (misal: laporan praktikum TANPA BAB I/II).
2. **4 Kaidah Emas struktur akademik** — sejajaran rumusan masalah ↔ tujuan ↔ kesimpulan; piramida latar belakang (fakta → masalah → gap → solusi); matriks penelitian terdahulu; pemisahan tegas hasil vs pembahasan.
3. **Aturan teknis PUEBI + pedoman kampus** — "di" dipisah vs "di-" disambung, istilah asing miring, nomor halaman romawi/Arab, kutipan panjang, abstrak ≤250 kata.

---

## CLI Scanner: Deteksi Pola AI Otomatis

Tersedia script Python mandiri tanpa dependensi untuk memeriksa naskah kamu sebelum diserahkan:

```bash
python3 scripts/scan_ai_slop.py path/ke/naskah_kamu.md
```

Fitur scanner:
* Menghitung total kata, jumlah temuan pola AI, dan skor kepadatan AI (*AI Slop Density Score*).
* Menampilkan nomor baris dan kutipan kalimat yang terindikasi kaku.
* Memberikan rekomendasi perbaikan sesuai aturan ID-1 s.d. ID-7.
* Contoh perbandingan sebelum dan sesudah humanisasi tugas skripsi dapat dilihat di [`examples/skripsi-bab1-before-after.md`](examples/skripsi-bab1-before-after.md).

---

## Contoh

**Before (terasa AI):**

> Pertanyaan bagus! Pengkodean berbantuan AI merupakan bukti abadi dari potensi transformatif large language model, menandai momen penting dalam evolusi pengembangan perangkat lunak. Dalam lanskap teknologi yang terus berkembang pesat saat ini, alat-alat revolusioner ini sedang membentuk ulang cara insinyur berideasi, menggarisbawahi peran vitalnya dalam alur kerja modern. Masa depan terlihat cerah!

**After (humanized):**

> Asisten koding AI bisa bikin kamu lebih cepat di bagian-bagian yang membosankan. Bukan semuanya. Apalagi untuk arsitektur sistem.
>
> Bagusnya untuk boilerplate: file konfigurasi, scaffolding tes, refactor berulang. Jeleknya, mereka juga jago terdengar benar padahal salah. Saya pernah asal terima saran yang dikompilasi, lolos lint, tapi tetap salah karena saya tidak lagi memperhatikan.
>
> Metrik produktivitasnya licin. Kalau tidak ada tes, kamu pada dasarnya nebak.

---

## Referensi

- [blader/humanizer](https://github.com/blader/humanizer) — skill humanizer bahasa Inggris asli
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — sumber utama pola universal
- Pedoman penulisan resmi: FPsi UI, UIN Raden Fatah, UIN-SU, FT UB, UNIKOM, UGM DTSL, PUEBI (Permendikbud 50/2015)

## Lisensi

MIT
