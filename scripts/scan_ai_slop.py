#!/usr/bin/env python3
"""
Scanner Pola Tulisan AI Bahasa Indonesia (AI Slop Detector CLI)
Tool mandiri tanpa dependensi untuk mendeteksi penanda tulisan buatan AI pada naskah Bahasa Indonesia.
"""

import sys, os, re, argparse

# Katalog Pola AI Bahasa Indonesia & Universal
PATTERNS = {
    "ID-1 (Frasa Birokratis)": [
        (r"\bdalam rangka\b", "Ganti dengan 'untuk' atau langsung ke kata kerja"),
        (r"\bguna (?:memastikan|meningkatkan|mencapai)\b", "Ganti dengan 'agar' atau 'untuk'"),
        (r"\bsehubungan dengan (?:hal )?tersebut\b", "Hapus, lanjutkan langsung ke fakta"),
        (r"\bterkait dengan hal tersebut\b", "Hapus atau ganti dengan subjek spesifik"),
        (r"\bdemi tercapainya\b", "Ganti dengan 'agar'"),
    ],
    "ID-2 (Kosakata AI Khas)": [
        (r"\bkrusial\b", "Ganti dengan 'penting' atau sebutkan dampak riilnya"),
        (r"\blanskap\b", "Ganti dengan 'kondisi', 'situasi', atau 'lingkungan'"),
        (r"\bparadigma\b", "Ganti dengan 'sudut pandang' atau 'kerangka acuan'"),
        (r"\bholistik\b", "Ganti dengan 'menyeluruh' atau jelaskan komponennya"),
        (r"\btransformatif\b", "Ganti dengan 'membawa perubahan nyata'"),
        (r"\bsinergi\b", "Ganti dengan 'kerja sama' atau 'kolaborasi'"),
        (r"\bkomprehensif\b", "Ganti dengan 'lengkap' atau 'mendalam'"),
        (r"\bmenandai tonggak\b", "Ganti dengan tahun/fakta sejarah konkret"),
        (r"\bbukti abadi\b", "Ganti dengan 'contoh nyata' atau 'data'"),
        (r"\bpermadani\b", "Hindari metafora klise terjemahan mesin"),
    ],
    "ID-3 (Formula 'Tidak hanya... tetapi juga...')": [
        (r"\b(?:tidak hanya|bukan hanya)[^.\n]+(?:tetapi juga|melainkan juga)\b", "Variasikan menjadi kalimat deklaratif biasa tanpa antitesis klise"),
    ],
    "ID-4 (Konjungsi Awal Paragraf)": [
        (r"(?:^|\n\n)(?:Selain itu|Lebih lanjut|Di sisi lain|Kendati demikian|Di samping itu|Dengan demikian),", "Awali paragraf dengan kalimat topik substantif, bukan kata transisi"),
    ],
    "ID-5 (Redundansi Pasif Formal)": [
        (r"\bdapat dilakukan dengan cara\b", "Ganti dengan 'dapat...' atau kalimat aktif"),
        (r"\bperlu diperhatikan bahwa\b", "Hapus, langsung sebutkan peraturannya"),
        (r"\bpatut dicatat bahwa\b", "Hapus, langsung sampaikan datanya"),
        (r"\btidak dapat dipungkiri bahwa\b", "Hapus, langsung sampaikan argumennya"),
        (r"\bsebagaimana diketahui bahwa\b", "Hapus pembuka basa-basi"),
    ],
    "ID-6 (Slogan Moralistik / Masa Depan)": [
        (r"\bpenting bagi kita semua untuk\b", "Ganti dengan rekomendasi teknis konkret"),
        (r"\bsenantiasa\b", "Ganti dengan kata 'selalu' atau hilangkan bila redundan"),
        (r"\bbersinergi demi mewujudkan\b", "Ganti dengan rencana aksi operasional"),
        (r"\bmenuju masa depan yang lebih (?:cerah|baik)\b", "Tutup dengan implikasi empiris, bukan slogan utopis"),
    ],
    "Format (Em Dash / Emojis)": [
        (r"—", "Ganti em dash (—) dengan koma, titik, atau restrukturisasi kalimat"),
        (r"[\U00010000-\U0010ffff]", "Hapus emoji dekoratif dari naskah akademik/formal"),
    ],
}

def scan_text(text):
    results = []
    lines = text.split("\n")
    total_matches = 0

    for category, regex_list in PATTERNS.items():
        cat_matches = []
        for pattern_re, advice in regex_list:
            matches = list(re.finditer(pattern_re, text, re.IGNORECASE | re.MULTILINE))
            for m in matches:
                total_matches += 1
                # Find line number
                start_pos = m.start()
                line_no = text[:start_pos].count("\n") + 1
                matched_str = m.group(0).strip().replace("\n", " ")
                cat_matches.append({
                    "line": line_no,
                    "matched": matched_str,
                    "advice": advice
                })
        if cat_matches:
            results.append((category, cat_matches))

    word_count = len(re.findall(r"\w+", text))
    # Hitung density: match per 100 kata
    density = (total_matches / max(word_count, 1)) * 100

    return results, total_matches, word_count, density

def main():
    parser = argparse.ArgumentParser(description="Pindai pola tulisan AI Bahasa Indonesia pada file teks/markdown.")
    parser.add_argument("file", help="Path file teks atau markdown yang ingin diperiksa")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' tidak ditemukan.")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    results, total_matches, words, density = scan_text(content)

    print("=" * 65)
    print(f" HASIL PEMERIKSAAN POLA AI: {os.path.basename(args.file)}")
    print("=" * 65)
    print(f"Total Kata           : {words}")
    print(f"Temuan Pola AI       : {total_matches}")
    print(f"Kepadatan Pola AI    : {density:.2f} temuan / 100 kata")
    
    if total_matches == 0:
        print("Status               : [BERSIH] Naskah terdengar alami dan bebas pola klise AI.")
        print("=" * 65)
        return

    if density > 2.0:
        status = "[TERINDIKASI KUAT AI] Banyak klise dan frasa khas AI terdeteksi."
    elif density > 0.8:
        status = "[PERLU PERBAIKAN] Terdapat beberapa frasa kaku yang perlu di-humanize."
    else:
        status = "[CENDERUNG NATURAL] Ditemukan sedikit penanda minor."

    print(f"Status               : {status}")
    print("-" * 65)

    for category, items in results:
        print(f"\n* {category} ({len(items)} temuan):")
        for item in items[:5]: # Batasi 5 contoh teratas per kategori
            print(f"  - Baris {item['line']}: \"{item['matched']}\"")
            print(f"    Saran: {item['advice']}")
        if len(items) > 5:
            print(f"    ... dan {len(items) - 5} temuan lainnya.")

    print("\n" + "=" * 65)
    print("Gunakan skill humanizer-id untuk memperbaiki bagian-bagian di atas.")
    print("=" * 65)

if __name__ == "__main__":
    main()
