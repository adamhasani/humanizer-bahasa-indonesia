#!/usr/bin/env python3
"""
Scanner Pola Tulisan AI Bahasa Indonesia (AI Slop & Burstiness Detector CLI)
Tool mandiri zero-dependency untuk mendeteksi penanda tulisan buatan AI,
klise sintaksis, serta mengukur variasi ritme panjang kalimat (Burstiness).
"""

import sys, os, re, math, argparse

# Katalog Pola AI Bahasa Indonesia & Universal
PATTERNS = {
    "ID-1 (Frasa Birokratis)": [
        (r"\bdalam rangka\b", "Ganti dengan 'untuk' atau langsung ke kata kerja tindakan"),
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
        (r"\bpermadani\b", "Hindari metafora klise terjemahan mesin (tapestry)"),
        (r"\bmenyelami\b", "Ganti dengan 'mengkaji', 'meneliti', atau 'membahas' (delve)"),
        (r"\bmerajut\b", "Hindari metafora puitis klise pada konteks formal/akademik"),
        (r"\bjalinan\b", "Ganti dengan 'hubungan' atau 'keterkaitan'"),
        (r"\btak terelakkan\b", "Ganti dengan uraian konsekuensi logis/data konkret"),
        (r"\bkatalis(?:ator)?\b", "Ganti dengan 'pendorong' atau sebutkan faktor penyebabnya"),
        (r"\bgarda terdepan\b", "Hindari slogan klise; sebutkan peran operasionalnya"),
        (r"\bkomitmen teguh\b", "Ganti dengan program kerja atau target terukur"),
    ],
    "ID-3 (Formula 'Tidak hanya... tetapi juga...')": [
        (r"\b(?:tidak hanya|bukan hanya)[^.\n]+(?:tetapi juga|melainkan juga)\b", "Variasikan menjadi kalimat deklaratif biasa tanpa antitesis klise"),
    ],
    "ID-4 (Konjungsi Awal Paragraf & Klise Pembuka)": [
        (r"(?:^|\n\n)(?:Selain itu|Lebih lanjut|Di sisi lain|Kendati demikian|Di samping itu|Dengan demikian),", "Awali paragraf dengan kalimat topik substantif, bukan kata transisi"),
        (r"(?:^|\n\n)(?:Di era (?:globalisasi|digitalisasi|modern)(?: yang kian pesat)?|Pada zaman sekarang ini),?", "Hindari pembuka klise; langsung buka dengan data empiris atau fenomena lapangan"),
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
    "Format (Raw Markdown Headers / Em Dash / Emojis)": [
        (r"^#{1,6}\s+.*$", "Hapus tag markdown (#, ##, ###); gunakan penomoran baku akademik (BAB I, 1.1)"),
        (r"—", "Ganti em dash (—) dengan koma, titik, atau restrukturisasi kalimat"),
        (r"[\U00010000-\U0010ffff]", "Hapus emoji dekoratif dari naskah akademik/formal"),
    ],
}

def analyze_burstiness(text):
    """
    Menghitung dinamika variasi panjang kalimat (Burstiness).
    Manusia memiliki variasi tinggi (CV >= 0.45).
    AI cenderung menghasilkan panjang kalimat seragam (CV < 0.35).
    """
    # Bersihkan markdown formatting untuk estimasi kata yang adil
    clean = re.sub(r'#+|\*+|_+|`+', '', text)
    sentences = re.split(r'(?<=[.!?])\s+', clean)
    
    lengths = []
    for s in sentences:
        words = re.findall(r'\b\w+\b', s)
        if len(words) >= 2: # Abaikan kalimat semu < 2 kata
            lengths.append(len(words))
            
    if len(lengths) < 3:
        return 0, 0, 0, "Sampel kalimat terlalu sedikit untuk analisis ritme."

    mean_len = sum(lengths) / len(lengths)
    variance = sum((x - mean_len) ** 2 for x in lengths) / len(lengths)
    std_dev = math.sqrt(variance)
    cv = std_dev / (mean_len if mean_len > 0 else 1) # Coefficient of Variation

    if cv >= 0.50:
        desc = "[SANGAT DINAMIS] Ritme kalimat bervariasi alami (karakter tulisan manusia)."
    elif cv >= 0.35:
        desc = "[CUKUP VARIATIF] Variasi panjang kalimat dalam rentang wajar."
    else:
        desc = "[MONOTON / FLAT] Panjang kalimat cenderung seragam (indikator kuat AI slop)."

    return mean_len, std_dev, cv, desc

def scan_text(text):
    results = []
    total_matches = 0

    for category, regex_list in PATTERNS.items():
        cat_matches = []
        for pattern_re, advice in regex_list:
            matches = list(re.finditer(pattern_re, text, re.IGNORECASE | re.MULTILINE))
            for m in matches:
                total_matches += 1
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

    words = len(re.findall(r"\b\w+\b", text))
    density = (total_matches / max(words, 1)) * 100
    mean_len, std_dev, cv, burst_desc = analyze_burstiness(text)

    return results, total_matches, words, density, (mean_len, std_dev, cv, burst_desc)

def main():
    parser = argparse.ArgumentParser(description="Pindai pola tulisan AI Bahasa Indonesia dan ukur ritme Burstiness.")
    parser.add_argument("file", help="Path file teks atau markdown yang ingin diperiksa")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' tidak ditemukan.")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    results, total_matches, words, density, (mean_len, std_dev, cv, burst_desc) = scan_text(content)

    print("=" * 68)
    print(f" HASIL PEMERIKSAAN POLA AI & BURSTINESS: {os.path.basename(args.file)}")
    print("=" * 68)
    print(f"Total Kata                 : {words}")
    print(f"Temuan Pola Klise AI       : {total_matches}")
    print(f"Kepadatan Pola AI (Density): {density:.2f} temuan / 100 kata")
    print(f"Rata-rata Panjang Kalimat  : {mean_len:.1f} kata (Std Dev: {std_dev:.1f})")
    print(f"Skor Burstiness (CV)       : {cv:.2f} -> {burst_desc}")
    print("-" * 68)

    if total_matches == 0 and cv >= 0.35:
        print("Status Akhir               : [BERSIH & ALAMI] Naskah lolos indikator manusiawi.")
        print("=" * 68)
        return

    if density > 2.0 or cv < 0.30:
        status = "[TERINDIKASI KUAT AI] Banyak klise dan ritme kalimat terkesan mekanis."
    elif density > 0.8 or cv < 0.38:
        status = "[PERLU PERBAIKAN] Terdapat beberapa frasa kaku atau ritme perlu divariasikan."
    else:
        status = "[CENDERUNG NATURAL] Ditemukan sedikit penanda minor."

    print(f"Status Akhir               : {status}")
    print("-" * 68)

    for category, items in results:
        print(f"\n* {category} ({len(items)} temuan):")
        for item in items[:5]:
            print(f"  - Baris {item['line']}: \"{item['matched']}\"")
            print(f"    Saran: {item['advice']}")
        if len(items) > 5:
            print(f"    ... dan {len(items) - 5} temuan lainnya.")

    print("\n" + "=" * 68)
    print("Tips: Terapkan rumus ritme 1-3-1 dan alur 2-tahap (Reflective Pass) di SKILL.md")
    print("=" * 68)

if __name__ == "__main__":
    main()
