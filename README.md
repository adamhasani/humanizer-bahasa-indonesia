# Humanizer Bahasa Indonesia

<p align="center">
  <a href="https://github.com/adamhasani/humanizer-bahasa-indonesia/releases">
    <img src="https://img.shields.io/github/v/release/adamhasani/humanizer-bahasa-indonesia?color=blue&label=Release" alt="Release">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
  <a href="#cli-scanner-deteksi-pola-ai-otomatis">
    <img src="https://img.shields.io/badge/Python-3.8+-yellow.svg" alt="Python 3.8+">
  </a>
  <a href="#cara-pasang">
    <img src="https://img.shields.io/badge/Claude-Skill%20Ready-purple.svg" alt="Claude Skill">
  </a>
  <a href="https://github.com/adamhasani/humanizer-bahasa-indonesia/stargazers">
    <img src="https://img.shields.io/github/stars/adamhasani/humanizer-bahasa-indonesia?style=social" alt="Stars">
  </a>
</p>

<p align="center">
  <b>Hapus jejak tulisan buatan AI dari teks Bahasa Indonesia agar terdengar alami, berbobot, dan lolos standar karya tulis akademik.</b><br>
  Dirancang khusus untuk artikel, konten profesional, serta <b>tugas sekolah & perkuliahan</b> (forum diskusi, praktikum, makalah, skripsi, proposal, jurnal SINTA, hingga magang/KKN).
</p>

---

## Daftar Isi

- [Mengapa Humanizer Ini Berbeda?](#mengapa-humanizer-ini-berbeda)
- [Isi Repositori](#isi-repositori)
- [Cara Pasang & Penggunaan](#cara-pasang--penggunaan)
  - [1. Claude.ai (Web UI)](#1-claudeai-web-ui)
  - [2. Claude Code (CLI)](#2-claude-code-cli)
  - [3. Instalasi Manual](#3-instalasi-manual)
  - [4. ChatGPT / Gemini / AI Lainnya](#4-chatgpt--gemini--ai-lainnya)
- [12 Template Format Tugas (T1–T12)](#12-template-format-tugas-t1t12)
- [4 Kaidah Emas Struktur Akademik](#4-kaidah-emas-struktur-akademik)
- [Katalog Pola yang Dideteksi](#katalog-pola-yang-dideteksi)
  - [Pola Khas AI Bahasa Indonesia (ID-1 s/d ID-7)](#pola-khas-ai-bahasa-indonesia-id-1-sd-id-7)
  - [Pola Universal (23 Pola)](#pola-universal-23-pola)
- [Generator Word (.docx) Siap Cetak](#generator-word-docx-siap-cetak)
- [CLI Scanner: Deteksi Pola AI Otomatis](#cli-scanner-deteksi-pola-ai-otomatis)
- [Contoh Before vs After](#contoh-before-vs-after)
- [Pertanyaan yang Sering Diajukan (FAQ)](#pertanyaan-yang-sering-diajukan-faq)
- [Lisensi & Kontribusi](#lisensi--kontribusi)

---

## Mengapa Humanizer Ini Berbeda?

Sebagian besar "AI humanizer" online hanya bekerja seperti *article spinner* biasa: menukar kata dengan sinonim acak yang sering kali membuat kalimat menjadi rancu, atau hanya efektif untuk teks berbahasa Inggris.

Detektor AI modern (Turnitin AI, GPTZero) dan dosen penguji tidak hanya melihat kata per kata, melainkan **pola keteraturan sintaksis (*burstiness & perplexity*)**, ketiadaan data empiris, dan struktur jawaban yang salah format. 

**Humanizer Bahasa Indonesia** menyelesaikan ini melalui pendekatan tiga lapis:
1. **Pembersihan Diksi & Sintaksis**: Membasmi kosakata klise AI (*"krusial"*, *"lanskap"*, *"transformatif"*), kalimat pasif birokratis berulang, dan konjungsi ritual di awal paragraf.
2. **Standardisasi Format Dokumen**: Dosen langsung curiga jika laporan praktikum memakai bab skripsi. Repositori ini menyediakan 12 template baku yang memisahkan format diskusi singkat, esai, hingga skripsi 5 BAB.
3. **Penegakan Kaidah Akademik Valid**: Menerapkan struktur piramida terbalik latar belakang, kesejajaran rumusan masalah dengan kesimpulan, matriks telaah pustaka terdahulu, dan panduan ejaan EYD V / PUEBI.

---

## Isi Repositori

```text
.
├── SKILL.md                              # Modul aturan utama Claude Skill (23 pola universal + 7 pola ID + 4 kaidah)
├── README.md                             # Panduan lengkap dokumentasi proyek
├── LICENSE                               # Lisensi open-source MIT
├── references/
│   ├── template-jawaban.md               # Spesifikasi lengkap 12 template tugas (T1–T12)
│   ├── aturan-teknis.md                  # Panduan EYD V, margin 4-4-3-3, format tabel 3 garis, dan sitasi
│   └── placeholder.md                    # Sistem visual penanda bagian wajib isi manual (logo, data mentah)
├── scripts/
│   ├── export_docx.py                    # Generator Word .docx standar kampus (margin 4-4-3-3, zero-dependencies)
│   └── scan_ai_slop.py                   # Script CLI mandiri untuk scan naskah (zero-dependencies)
└── examples/
    └── skripsi-bab1-before-after.md      # Contoh bedah kasus draf latar belakang skripsi sebelum vs sesudah
```

---

## Cara Pasang & Penggunaan

### 1. Claude.ai (Web UI)
1. Unduh file paket **`humanizer-id.skill`** dari halaman [GitHub Releases](https://github.com/adamhasani/humanizer-bahasa-indonesia/releases).
2. Buka **Claude.ai** $\rightarrow$ klik profil di kiri bawah $\rightarrow$ pilih **Settings** $\rightarrow$ **Skills**.
3. Klik **Upload Skill** dan pilih file `humanizer-id.skill`.

### 2. Claude Code (CLI)
Kloning langsung repositori ini ke folder skills Claude Code kamu:
```bash
git clone https://github.com/adamhasani/humanizer-bahasa-indonesia.git ~/.claude/skills/humanizer-id
```

### 3. Instalasi Manual
Jika ingin memasang manual pada tool agentic lainnya (misal: Hermes Agent, OpenCode):
```bash
mkdir -p ~/.claude/skills/humanizer-id
cp -r SKILL.md references ~/.claude/skills/humanizer-id/
```

### 4. ChatGPT / Gemini / AI Lainnya
Kamu juga bisa menggunakannya di ChatGPT atau Gemini tanpa fitur skill:
* Salin seluruh teks di [`SKILL.md`](SKILL.md) ke dalam **Custom Instructions** (ChatGPT) atau jadikan sebagai awalan *system prompt*.

### Cara Pakai dalam Obrolan:
* **Humanisasi tulisan yang sudah ada:**
  ```text
  Tolong humanize teks ini agar terdengar natural dan bebas dari gaya AI:
  [tempel naskahmu di sini]
  ```
* **Mengerjakan tugas baru sesuai jenisnya:**
  ```text
  Kerjakan tugas ini dengan gaya mahasiswa menggunakan template T3 (Laporan Praktikum):
  [tempel soal / modul praktikum di sini]
  ```

---

## 12 Template Format Tugas (T1–T12)

Dosen sangat sensitif terhadap format. Jangan pernah mengirim esai dengan format skripsi atau sebaliknya.

| Kode | Jenis Dokumen | Karakteristik Utama | Pantangan Keras |
|:---:|:---|:---|:---|
| **T1** | **Diskusi LMS / Tanya-Jawab** | 2–5 kalimat padat, to-the-point, jawaban langsung ke inti pertanyaan. | Tanpa kata pengantar, tanpa kesimpulan retoris. |
| **T2** | **Latihan Soal Bernomor** | Format berbutir, rumus sejajar tanda `=`, tabel jika diminta. | Jangan menyalin ulang soal panjang-panjang. |
| **T3** | **Laporan Praktikum / Lab** | Landasan teori, alat/bahan, langkah kerja, data & analisis, grafik. | **Dilarang memakai pembagian BAB I / BAB II**. |
| **T4** | **Esai / Makalah Pendek** | 2–5 halaman mengalir, pembuka konteks, argumen, penutup posisi. | Jangan diberi nomor bab formal. |
| **T5** | **Resume / Ringkasan Kuliah** | Poin per sub-bab tematik, maksimal 1–2 halaman. | Hindari narasi bertele-tele tanpa substansi materi. |
| **T6** | **Tugas Kode / Pemrograman** | Kode modular, hasil terminal nyata, analisis kompleksitas ($O(n)$). | Kode dilarang berupa stub kosong atau halusinasi output. |
| **T7** | **Makalah Akademik Resmi** | Sampul resmi, Kata Pengantar, BAB I Pendahuluan, BAB II Pembahasan, BAB III Penutup. | Margin wajib 4-4-3-3 cm, tabel formal 3 garis. |
| **T8** | **Skripsi / Tugas Akhir S1** | BAB I s.d. BAB V lengkap, landasan teori empiris, analisis hasil teruji. | Rumusan masalah wajib dijawab 1:1 di BAB V. |
| **T9** | **Proposal Penelitian / Hibah** | BAB I–III, metodologi terperinci, jadwal pelaksanaan (Gantt Chart), estimasi anggaran. | Jangan mengarang data hasil sebelum penelitian. |
| **T10** | **Artikel Jurnal IMRAD** | Abstrak dwibahasa ($\le$250 kata), Introduction, Methods, Results, Discussion, Daftar Pustaka APA/IEEE. | Pembahasan bukan sekadar membaca ulang tabel. |
| **T11** | **Laporan Magang / PKL / KKN** | Profil mitra instansi, deskripsi tupoksi, logbook kegiatan mingguan, kendala & solusi. | Tanpa keluhan personal; fokus pada refleksi profesional. |
| **T12** | **Tugas Sekolah (SMP/SMA)** | Identitas siswa & guru pembimbing, format lugas, makalah sekolah wajib kata pengantar. | Hindari jargon perguruan tinggi yang belum diajarkan di sekolah. |

*Rincian struktur dan contoh setiap template tersedia di [`references/template-jawaban.md`](references/template-jawaban.md).*

---

## 4 Kaidah Emas Struktur Akademik

Dosen pembimbing yang berpengalaman dapat mendeteksi naskah buatan AI hanya dalam beberapa detik dengan memeriksa 4 poin struktural ini:

1. **Segitiga Emas Kesejajaran (1:1)**:
   Jumlah rumusan masalah di BAB I wajib selaras sempurna dengan tujuan penelitian (BAB I) dan butir kesimpulan (BAB V). Kesimpulan bukan refleksi filosofis, melainkan jawaban berbasis angka konkret terhadap rumusan masalah.
2. **Piramida Terbalik Latar Belakang**:
   Alur penulisan dimulai dari fenomena empiris/regulasi makro $\rightarrow$ persoalan spesifik di lapangan $\rightarrow$ kesenjangan riset terdahulu (*research gap*) $\rightarrow$ urgensi solusi yang diajukan. Bebas dari pembuka klise (*"Di era globalisasi yang semakin pesat saat ini..."*).
3. **Matriks Penelitian Terdahulu**:
   Kajian pustaka wajib merangkum riset-riset sebelumnya ke dalam tabel matriks komparasi (*Peneliti & Tahun, Metode, Hasil Utama, dan Perbedaan dengan Riset Ini*), diikuti sintesis kebaruan (*novelty*).
4. **Pemisahan Tegas Hasil vs Pembahasan**:
   Sub-bab **Hasil** hanya menyajikan data objektif (angka, tabel, kurva). Sub-bab **Pembahasan** mengulas kritis *mengapa* hasilnya demikian dengan membandingkannya terhadap teori di BAB II dan temuan peneliti lain.

---

## Katalog Pola yang Dideteksi

### Pola Khas AI Bahasa Indonesia (ID-1 s/d ID-7)

| # | Pola | Contoh Gaya AI (Dihindari) | Rekomendasi Perbaikan |
|:---:|:---|:---|:---|
| **ID-1** | **Frasa Birokratis Berlebih** | *"dalam rangka meningkatkan... guna memastikan terlaksananya... sehubungan dengan hal tersebut..."* | Gunakan *"untuk..."*, *"agar..."*, atau langsung ke kata kerja tindakan. |
| **ID-2** | **Kosakata Klise AI Indonesia** | *"krusial, lanskap, paradigma, holistik, komprehensif, transformatif, sinergi, selaras, bukti abadi"* | Gunakan padanan lugas: *"penting, kondisi, sudut pandang, menyeluruh, kerja sama"*. |
| **ID-3** | **Formula "Tidak Hanya... Tetapi Juga..."** | *"Sistem ini tidak hanya menghemat waktu, tetapi juga meningkatkan akurasi. Tidak hanya itu, ia juga..."* | Susun dalam kalimat deklaratif proporsional tanpa antitesis mekanis. |
| **ID-4** | **Konjungsi Transisi di Setiap Awal Paragraf** | Setiap paragraf dibuka: *"Selain itu,", "Lebih lanjut,", "Di sisi lain,", "Kendati demikian,"* | Sambung antargagasan melalui kalimat topik (*topic sentence*) substantif. |
| **ID-5** | **Redundansi Pasif Formal** | *"dapat dilakukan dengan cara...", "perlu dicatat bahwa...", "patut dipahami bahwa..."* | Langsung nyatakan premis atau data: *"Data menunjukkan bahwa..."*. |
| **ID-6** | **Penutup Khotbah Moral & Slogan** | *"Oleh karena itu, marilah kita senantiasa bersinergi demi mewujudkan masa depan yang gemilang..."* | Tutup dengan ringkasan temuan terukur, keterbatasan metode, dan saran teknis. |
| **ID-7** | **Judul Berpola Slogan Simetris Titik Dua** | *"Transformasi Digital: Menjembatani Kesenjangan antara Teori dan Praktik Industri"* | Buat judul deskriptif: *"Penerapan Sistem ERP pada PT X: Analisis Efisiensi Distribusi"*. |

### Pola Universal (23 Pola)
Adaptasi dari panduan resmi [*Wikipedia: Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing):
1. **Significance inflation**: Membesar-besarkan warisan sejarah atau dampak karya.
2. **Notability name-dropping**: Menyebut daftar media/organisasi ternama tanpa konteks kutipan.
3. **Superficial -ing analyses**: Memaksakan akhiran beruntun (*"mencerminkan... melambangkan..."*).
4. **Promotional language**: Nada brosur wisata atau pujian hiperbolis.
5. **Vague attributions**: Atribusi anonim (*"Banyak pakar meyakini..."*).
6. **Formulaic challenges section**: Kalimat pembelaan tantangan generik di akhir sub-bab.
7. **AI vocabulary words**: Penggunaan kata frekuensi tinggi bot (*delve, tapestry, multifaceted*).
8. **Copula avoidance**: Menghindari kata "adalah/merupakan" dengan menggantinya jadi *"berfungsi sebagai..."*.
9. **Negative parallelisms**: Menjejali kalimat dengan struktur *"Bukan tentang A, melainkan B"*.
10. **Rule of three**: Memaksakan 3 kata berima atau 3 kata sifat berderet di setiap kalimat.
11. **Synonym cycling**: Menggonta-ganti sebutan subjek demi menghindari repetisi yang wajar.
12. **False ranges**: Menulis rentang palsu (*"dari skala mikro hingga makro, dari hulu ke hilir"*).
13. **Em dash overuse**: Menggunakan tanda pisah em dash (—) secara beruntun.
14. **Boldface overuse**: Menghitamkan terlalu banyak kata di tengah paragraf biasa.
15. **Inline-header lists**: Daftar berbutir dengan judul tebal inline yang seragam.
16. **Title Case headings**: Menulis judul dengan huruf kapital di setiap kata ala Bahasa Inggris.
17. **Emojis**: Menyisipkan ikon emoji dekoratif pada teks akademik atau formal.
18. **Chatbot artifacts**: Sisa percakapan bot (*"Semoga membantu!", "Beri tahu saya jika..."*).
19. **Knowledge-cutoff disclaimers**: Catatan basi keterbatasan data pelatihan model.
20. **Sycophantic tone**: Nada menjilat dan memuji pertanyaan pengguna secara berlebihan.
21. **Filler phrases**: Basa-basi pengantar sebelum masuk ke jawaban inti.
22. **Excessive hedging**: Keraguan berlebihan (*"bisa jadi mungkin dapat diindikasikan bahwa..."*).
23. **Generic positive conclusions**: Kalimat penutup generik bertema harapan masa depan cerah.

---

---

## Generator Word (.docx) Siap Cetak

Mahasiswa tidak mengumpulkan tugas ke dosen dalam format Markdown (`.md`), melainkan file **Microsoft Word (`.docx`)** yang rapi. 

Repositori ini menyertakan script konverter mandiri (100% Python Standard Library, tanpa perlu `pip install`) yang otomatis memformat naskah sesuai standar pedoman akademik kampus:

```bash
# Konversi naskah markdown ke file Word .docx
python3 scripts/export_docx.py tugas_kamu.md

# Atau tentukan nama file output & custom margin (opsional)
python3 scripts/export_docx.py tugas_kamu.md -o Makalah_Lengkap.docx --margin 4-4-3-3
```

### Standar Tipografi Otomatis:
* **Ukuran Kertas & Margin**: A4 dengan margin baku **4-4-3-3 cm** (Kiri 4 cm, Atas 4 cm, Kanan 3 cm, Bawah 3 cm).
* **Huruf & Spasi**: Times New Roman 12 pt, spasi 1.5 baris, perataan teks kanan-kiri (*Justified*).
* **Alinea Baru**: Inden baris pertama otomatis 1.25 cm.
* **Tabel Formal 3 Garis**: Tabel akademis standar tanpa garis vertikal penjara.
* **Blok Kutipan Langsung**: Kutipan panjang (>4 baris) otomatis font 11 pt, spasi tunggal 1.0, dan inden masuk 1.25 cm.

## CLI Scanner: Deteksi Pola AI Otomatis

Repositori ini menyertakan script Python mandiri tanpa dependensi tambahan (*pure standard library*) untuk memindai dokumen kamu secara lokal sebelum dikumpulkan ke dosen atau dipublikasikan:

```bash
# Jalankan pemindaian naskah
python3 scripts/scan_ai_slop.py path/ke/dokumen_kamu.md
```

### Tampilan Output Scanner:
```text
=================================================================
 HASIL PEMERIKSAAN POLA AI: skripsi_bab1.md
=================================================================
Total Kata           : 482
Temuan Pola AI       : 14
Kepadatan Pola AI    : 2.90 temuan / 100 kata
Status               : [TERINDIKASI KUAT AI] Banyak klise dan frasa khas AI terdeteksi.
-----------------------------------------------------------------

* ID-2 (Kosakata AI Khas) (5 temuan):
  - Baris 3: "krusial"
    Saran: Ganti dengan 'penting' atau sebutkan dampak riilnya
  - Baris 4: "lanskap"
    Saran: Ganti dengan 'kondisi', 'situasi', atau 'lingkungan'

* ID-4 (Konjungsi Awal Paragraf) (2 temuan):
  - Baris 9: "Selain itu,"
    Saran: Awali paragraf dengan kalimat topik substantif, bukan kata transisi
=================================================================
```

---

## Contoh Before vs After

### 1. Kasus Konten / Opini Umum
* **Before (Gaya AI):**
  > Pertanyaan bagus! Pengkodean berbantuan AI merupakan bukti abadi dari potensi transformatif teknologi modern dalam lanskap industri saat ini. Dalam rangka meningkatkan produktivitas, alat-alat canggih ini memegang peranan krusial bagi para pengembang software. Masa depan terlihat sangat cerah!
* **After (Humanized):**
  > Asisten koding AI praktis untuk mengerjakan bagian-bagian repetitif seperti konfigurasi boilerplate atau pembuatan skrip pengujian awal. Namun untuk perancangan arsitektur sistem inti, ketergantungan penuh pada AI justru berisiko meloloskan bug yang sulit dilacak jika tidak ditinjau manual secara cermat.

### 2. Kasus Akademik Mahasiswa
Bedah naskah lengkap perbandingan draf **BAB I Latar Belakang Skripsi** dari versi ChatGPT yang penuh bunga kata hingga menjadi naskah berbasis piramida terbalik dan data BPS dapat dilihat langsung di:
👉 **[`examples/skripsi-bab1-before-after.md`](examples/skripsi-bab1-before-after.md)**

---

## Pertanyaan yang Sering Diajukan (FAQ)

<details>
<summary><b>1. Apakah naskah yang diproses skill ini dijamin lolos Turnitin AI detection?</b></summary>
Turnitin AI mengukur dua variabel linguistik utama: <i>Perplexity</i> (keragaman pilihan kata yang tak terduga) dan <i>Burstiness</i> (variasi dinamika panjang-pendek kalimat). Humanizer ini sengaja memecah ritme monoton AI, menyisipkan data numerik, dan menghapus pola sintaksis standar yang dihafal mesin detektor sehingga skor probabilitas AI turun drastis.
</details>

<details>
<summary><b>2. Bisakah digunakan untuk tugas non-kuliah (kantor/konten medsos)?</b></summary>
Bisa. Kamu cukup menggunakan perintah umum tanpa menyebutkan kode template akademik. Skill akan mengaktifkan aturan pembersihan diksi umum (ID-1 s.d. ID-7 dan 23 pola universal) untuk menghasilkan artikel atau laporan bisnis yang profesional dan luwes.
</details>

<details>
<summary><b>3. Mengapa laporan praktikum dilarang memakai format BAB I/II?</b></summary>
Berdasarkan telaah pedoman akademik berbagai laboratorium sains dan teknik di Indonesia, laporan praktikum mingguan menggunakan struktur modul langsung (Tujuan, Alat/Bahan, Prosedur, Data Pengamatan, Pembahasan, Kesimpulan). Penggunaan format BAB I/II adalah salah satu penanda utama tugas hasil generate AI sembarangan.
</details>

<details>
<summary><b>4. Apakah script scanner membutuhkan instalasi library (pip)?</b></summary>
Tidak. Script <code>scripts/scan_ai_slop.py</code> dibuat menggunakan modul bawaan Python (<code>re</code>, <code>sys</code>, <code>argparse</code>) sehingga bisa langsung dijalankan di sistem operasi mana pun tanpa perlu <code>pip install</code>.
</details>

---

## Referensi & Pedoman

* [blader/humanizer](https://github.com/blader/humanizer) — Proyek asli humanizer bahasa Inggris.
* [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — Dokumentasi pola sintaksis model bahasa besar.
* **Pedoman Penulisan Karya Ilmiah Kampus**: FPsi UI, UIN Raden Fatah, UIN-SU, FT Universitas Brawijaya, UNIKOM, DTSL UGM.
* **Badan Pengembangan dan Pembinaan Bahasa**: Pedoman Umum Ejaan Bahasa Indonesia (PUEBI / EYD Edisi V).

---

## Lisensi

Didistribusikan di bawah lisensi terbuka [MIT License](LICENSE). Bebas digunakan, dimodifikasi, dan dibagikan untuk keperluan akademik maupun komersial.
