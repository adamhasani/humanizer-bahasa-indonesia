# Pola Visual AI (design slop)

Tanda-tanda desain buatan AI dan cara mengatasinya. Berlaku saat membuat
landing page, poster, slide, atau UI apapun.

## Pola yang harus dihindari

| Pola AI | Kenapa terdeteksi | Ganti dengan |
|---|---|---|
| Tailwind `blue-500` (#3B82F6) sebagai warna utama | Model dilatih dari jutaan situs Tailwind default; biru = probabilitas tertinggi | Palet custom dengan minimum 2 warna non-biru; tanya konteks brand dulu |
| Gradient ungu-biru / indigo (`from-indigo-500 to-purple-600`) | Signature background hero "AI-made" | Warna solid, atau gradient yang dipilih dari brand |
| Emoji sebagai ikon section (🚀💡✅) | AI dekorasi mekanis | Icon library (lucide, heroicons) atau tanpa ikon |
| Semua card sudut membulat sama + shadow lembut | Layout cookie-cutter | Variasi komposisi; asimetri bila konteksnya cocok |
| Hero: heading besar + subteks abu-abu + tombol biru | Template bawaan generik | Layout yang menyangkut konten spesifik pengguna |
| Bold mekanis di frasa acak | Pengulangan pola chatbot | Tebal hanya untuk kata yang benar-benar perlu |
| 3 kartu fitur seragam berjajar (rule of three visual) | Formula AI | Sesuaikan jumlah & bentuk dengan konten nyata |

## Prosedur saat diminta bikin visual

1. Tanya/derive palet dari brand, bukan dari default framework.
2. Blacklist mental: biru default Tailwind, gradient ungu-biru, emoji-ikon.
3. Kalau user tidak memberi arah warna, pilih palet netral (hitam/putih + 1
   aksen berani non-biru) — lebih aman daripada biru generik.
4. Final pass: "kalau screenshot ini diselipkan di antara 5 situs AI-made lain,
   apa yang membuatnya bisa dibedakan?" Kalau jawabannya "tidak ada", revisi.
