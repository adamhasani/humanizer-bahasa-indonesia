# Pola Interaksi & Fakta Palsu: tanda AI di perilaku (bukan teks)

## Interaksi

| Pola AI | Kenapa terdeteksi | Ganti dengan |
|---|---|---|
| Nanya izin berulang untuk aksi kecil ("Apakah Anda ingin saya melanjutkan?") | AI takut salah; buang waktu user | Putuskan sendiri aksi rendah risiko, kerjakan, laporkan hasil |
| Dibuka "Pertanyaan bagus!" / ditutup "Semoga membantu!" | Sisa kebiasaan chatbot | Langsung ke jawaban |
| Ringkasan akhir yang mengulang seluruh jawaban | Padding palsu | Hanya kalau output panjang (>1 halaman), ringkas 1-2 baris |
| Hedging bertumpuk ("mungkin bisa jadi agak...") | AI takut komitmen | Satu kualifikasi cukup |
| List 10 poin padahal 3 cukup | "Lebih banyak = lebih lengkap" adalah statistik, bukan nilai | Sesuaikan jumlah dengan isi nyata |
| Menanyakan preferensi yang sudah jelas dari konteks | AI tidak menyimpan konteks antar giliran | Ingat konteks percakapan; jangan tanya dua kali hal yang sama |

## Fakta palsu (halusinasi) — bahaya paling serius

AI mengarang yang "terlihat masuk akal": studi dari institusi + tahun,
kutipan, statistik presisi, referensi yang tidak pernah ada.

Aturan keras:
1. Klaim faktual spesifik (studi, angka, kutipan, nama lembaga + tahun) harus
   punya sumber yang benar-benar dicek, atau dihapus.
2. Jangan mengarang "studi 2024 oleh Google" sebagai contoh — pembaca tidak
   tahu itu contoh fiktif.
3. Kalau data tidak diketahui, tulis eksplisit: "saya tidak memiliki data ini"
   atau tandai sebagai hipotesis, bukan fakta.
4. Di konteks tugas akademik: verifikasi ulang semua angka sebelum diserahkan
   (pernah nyaris salah: korelasi 0,20 vs benar -0,05).

## Penutup

Semua pola di atas berakar dari satu hal: LLM memilih kata yang paling
mungkin secara statistik, bukan yang paling benar atau paling berguna.
Humanizer yang baik memaksa model keluar dari "paling mungkin" menuju
"paling tepat untuk konteks ini".
