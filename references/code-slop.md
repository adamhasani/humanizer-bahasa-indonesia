# Code Slop: pola kode buatan AI

Tanda-tanda kode buatan AI dan cara mengatasinya.

| Pola AI | Kenapa terdeteksi | Ganti dengan |
|---|---|---|
| Nama generik ala tutorial (`userData`, `itemList`, `data2`) | AI meniru tutorial; nama tak mengandung makna | Nama sesuai domain: `siswa`, `tagihanTerbayar` |
| Abstraksi percuma: factory/interface untuk 1 implementasi | AI over-engineering untuk "kelihatan profesional" | Tulis fungsi biasa; abstraksi saat implementasi kedua benar-benar muncul |
| `try/catch` kosong atau `catch (e) { return null }` | Menekan error tanpa menangani | Biarkan error naik, atau tangani dengan jelas (log + tindakan) |
| Komentar narratif (`// Increment counter by 1`) | Meniru contoh belajar | Komentar hanya untuk "kenapa", bukan "apa" |
| Config untuk nilai yang tidak pernah berubah | AI "siap-siap untuk masa depan" | Hardcode; config saat butuh nyata |
| Selalu bikin file/folder baru, jarang edit yang ada | AI tidak melihat kodebase secara menyeluruh | Grep dulu, reuse helper yang sudah ada |
| Solution "untuk skala ribuan user" di skrip 50 baris | Over-engineering ala AI | Ponytail: tulis paling sederhana yang bekerja, beri komentar batasnya |
| Boilerplate "for later" (skeleton kosong, TODO stub) | AI berhenti di kerangka, bukan hasil jadi | Kerjakan sampai bisa dieksekusi & diverifikasi |

## Aturan eksekusi nyata (paling penting)

AI sering "menyelesaikan" tugas dengan mengarang output: hasil eksekusi,
angka statistik, isi file yang tidak pernah dibuat. Aturan keras:

1. Kode yang dihasilkan HARUS dijalankan sebelum diklaim jadi.
2. Angka/divergifikasi dari output nyata, bukan perkiraan.
3. Kalau tool gagal, laporkan gagal + coba alternatif. JANGAN karang hasil.
4. Satu self-check kecil (assert/test sederhana) untuk logika non-trivial.
