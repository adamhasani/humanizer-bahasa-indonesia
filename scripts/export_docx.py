#!/usr/bin/env python3
"""
Generator Dokumen Word (.docx) Standar Akademik Indonesia
Mengonversi naskah Markdown/Teks menjadi file Microsoft Word (.docx) yang sudah
terformat rapi sesuai pedoman kampus (Margin 4-4-3-3 cm, Times New Roman 12pt,
spasi 1.5, inden paragraf 1.25 cm, tabel 3 garis, dan kutipan baku).

Zero dependencies: 100% Python Standard Library (zipfile & xml).
"""

import os, sys, re, argparse, zipfile
from xml.sax.saxutils import escape

# Template Dasar OpenXML
CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="24"/>
        <w:szCs w:val="24"/>
        <w:lang w:val="id-ID"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:line="360" w:lineRule="auto" w:before="0" w:after="120"/>
        <w:jc w:val="both"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
</w:styles>"""

def parse_inline_runs(text):
    """Mengubah format inline markdown (**tebal**, *miring*, `kode`) menjadi elemen <w:r>."""
    # Tokenizer sederhana untuk markdown inline
    tokens = re.split(r"(\*\*.*?\*\*|\*.*?\*|`.*?`)", text)
    runs_xml = []
    
    for token in tokens:
        if not token:
            continue
        bold = False
        italic = False
        font_family = "Times New Roman"
        font_size = "24" # 12 pt
        
        if token.startswith("**") and token.endswith("**") and len(token) >= 4:
            bold = True
            token_text = token[2:-2]
        elif token.startswith("*") and token.endswith("*") and len(token) >= 2:
            italic = True
            token_text = token[1:-1]
        elif token.startswith("`") and token.endswith("`") and len(token) >= 2:
            font_family = "Courier New"
            font_size = "21" # 10.5 pt
            token_text = token[1:-1]
        else:
            token_text = token
            
        rpr_parts = [f'<w:rFonts w:ascii="{font_family}" w:hAnsi="{font_family}"/>', f'<w:sz w:val="{font_size}"/>']
        if bold:
            rpr_parts.append('<w:b/>')
        if italic:
            rpr_parts.append('<w:i/>')
            
        rpr_xml = f'<w:rPr>{"".join(rpr_parts)}</w:rPr>'
        # Tangani spasi awal/akhir agar tidak dipangkas Word
        space_attr = ' xml:space="preserve"' if (token_text.startswith(" ") or token_text.endswith(" ")) else ""
        escaped_text = escape(token_text)
        runs_xml.append(f'<w:r>{rpr_xml}<w:t{space_attr}>{escaped_text}</w:t></w:r>')
        
    return "".join(runs_xml)

def make_table_xml(table_lines):
    """Membuat tabel format formal 3 garis akademik (tanpa garis vertikal)."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line or not line.startswith("|"):
            continue
        # Pisahkan sel
        cells = [c.strip() for c in line.strip("|").split("|")]
        # Lewati garis pemisah markdown |---|---|
        if all(re.match(r"^:?-+:?$", c) for c in cells if c):
            continue
        rows.append(cells)
        
    if not rows:
        return ""
        
    table_xml = ['<w:tbl>',
                 '<w:tblPr>',
                 '  <w:tblW w:w="0" w:type="auto"/>',
                 '  <w:jc w:val="center"/>',
                 '  <w:tblBorders>',
                 '    <w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>',
                 '    <w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>',
                 '    <w:left w:val="none"/>',
                 '    <w:right w:val="none"/>',
                 '    <w:insideH w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>',
                 '    <w:insideV w:val="none"/>',
                 '  </w:tblBorders>',
                 '  <w:tblCellMar>',
                 '    <w:top w:w="120" w:type="dxa"/>',
                 '    <w:bottom w:w="120" w:type="dxa"/>',
                 '    <w:left w:w="180" w:type="dxa"/>',
                 '    <w:right w:w="180" w:type="dxa"/>',
                 '  </w:tblCellMar>',
                 '</w:tblPr>']
                 
    for i, row in enumerate(rows):
        is_header = (i == 0)
        table_xml.append('<w:tr>')
        if is_header:
            table_xml.append('<w:trPr><w:tblHeader/></w:trPr>')
            
        for cell in row:
            runs = parse_inline_runs(cell)
            bold_flag = '<w:b/>' if is_header else ''
            align_val = 'center' if is_header else 'left'
            border_bottom = '<w:tcBorders><w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/></w:tcBorders>' if is_header else ''
            
            tc = [
                '<w:tc>',
                f'<w:tcPr>{border_bottom}<w:vAlign w:val="center"/></w:tcPr>',
                '<w:p>',
                f'<w:pPr><w:spacing w:line="240" w:lineRule="auto" w:before="60" w:after="60"/><w:jc w:val="{align_val}"/></w:pPr>',
                f'<w:r><w:rPr>{bold_flag}<w:sz w:val="22"/></w:rPr></w:r>',
                runs,
                '</w:p>',
                '</w:tc>'
            ]
            table_xml.append("".join(tc))
        table_xml.append('</w:tr>')
        
    table_xml.append('</w:tbl>')
    table_xml.append('<w:p><w:pPr><w:spacing w:after="180"/></w:pPr></w:p>') # Spasi setelah tabel
    return "".join(table_xml)

def markdown_to_docx_body(md_text):
    """Mengonversi sintaks Markdown menjadi elemen body OpenXML."""
    lines = md_text.split("\n")
    body_parts = []
    in_code_block = False
    code_lines = []
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 1. Penanganan Code Block (``` ... ```)
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                in_code_block = False
                # Cetak blok kode ke format kotak terpisah dengan font monospace
                for cl in code_lines:
                    esc_code = escape(cl)
                    body_parts.append(
                        f'<w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto" w:before="0" w:after="40"/>'
                        f'<w:ind w:left="720"/><w:jc w:val="left"/></w:pPr>'
                        f'<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="20"/><w:color w:val="333333"/></w:rPr>'
                        f'<w:t xml:space="preserve">{esc_code}</w:t></w:r></w:p>'
                    )
                body_parts.append('<w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>')
            i += 1
            continue
            
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue
            
        # 2. Penanganan Tabel Markdown
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            table_lines.append(stripped)
            i += 1
            continue
        else:
            if in_table:
                body_parts.append(make_table_xml(table_lines))
                table_lines = []
                in_table = False
                
        # 3. Baris Kosong
        if not stripped:
            i += 1
            continue
            
        # 4. Heading 1 (# Judul / BAB)
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            runs = parse_inline_runs(title)
            body_parts.append(
                f'<w:p><w:pPr><w:spacing w:before="360" w:after="240"/><w:jc w:val="center"/></w:pPr>'
                f'<w:r><w:rPr><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:r>'
                f'{runs}</w:p>'
            )
            i += 1
            continue
            
        # 5. Heading 2 (## Sub-bab)
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            runs = parse_inline_runs(title)
            body_parts.append(
                f'<w:p><w:pPr><w:spacing w:before="280" w:after="160"/><w:jc w:val="left"/></w:pPr>'
                f'<w:r><w:rPr><w:b/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:r>'
                f'{runs}</w:p>'
            )
            i += 1
            continue
            
        # 6. Heading 3 (### Sub-sub-bab)
        if stripped.startswith("### "):
            title = stripped[4:].strip()
            runs = parse_inline_runs(title)
            body_parts.append(
                f'<w:p><w:pPr><w:spacing w:before="200" w:after="120"/><w:jc w:val="left"/></w:pPr>'
                f'<w:r><w:rPr><w:b/><w:i/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:r>'
                f'{runs}</w:p>'
            )
            i += 1
            continue
            
        # 7. Blockquote / Kutipan (> ...)
        if stripped.startswith("> "):
            quote_text = stripped[2:].strip()
            runs = parse_inline_runs(quote_text)
            body_parts.append(
                f'<w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto" w:before="100" w:after="100"/>'
                f'<w:ind w:left="709" w:right="709"/><w:jc w:val="both"/></w:pPr>'
                f'<w:r><w:rPr><w:i/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:r>'
                f'{runs}</w:p>'
            )
            i += 1
            continue
            
        # 8. List Item berbutir (- atau * atau 1. )
        list_match = re.match(r"^(\*|-|\d+\.)\s+(.+)$", stripped)
        if list_match:
            bullet_sym = list_match.group(1)
            item_text = list_match.group(2)
            runs = parse_inline_runs(item_text)
            
            prefix_run = f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{bullet_sym} </w:t></w:r>'
            body_parts.append(
                f'<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto" w:before="0" w:after="60"/>'
                f'<w:ind w:left="709" w:hanging="400"/><w:jc w:val="both"/></w:pPr>'
                f'{prefix_run}{runs}</w:p>'
            )
            i += 1
            continue
            
        # 9. Garis Horizontal Pembatas (---)
        if stripped in ("---", "***", "___"):
            body_parts.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="CCCCCC"/></w:pBdr>'
                              '<w:spacing w:before="120" w:after="120"/></w:pPr></w:p>')
            i += 1
            continue
            
        # 10. Paragraf Biasa Akademik (Spasi 1.5, Inden 1.25 cm, Justified)
        runs = parse_inline_runs(stripped)
        body_parts.append(
            f'<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto" w:before="0" w:after="120"/>'
            f'<w:ind w:firstLine="709"/><w:jc w:val="both"/></w:pPr>'
            f'{runs}</w:p>'
        )
        i += 1
        
    if in_table:
        body_parts.append(make_table_xml(table_lines))
        
    return "".join(body_parts)

def build_docx(md_content, output_path, margin="4-4-3-3"):
    """Mengemas XML ke dalam file ZIP .docx dengan margin yang ditentukan."""
    # Parsing margin (Kiri-Atas-Kanan-Bawah dalam cm)
    # 1 cm = 567 twips (dxa)
    try:
        parts = [float(x) for x in margin.split("-")]
        if len(parts) == 4:
            left_cm, top_cm, right_cm, bottom_cm = parts
        else:
            left_cm, top_cm, right_cm, bottom_cm = 4.0, 4.0, 3.0, 3.0
    except Exception:
        left_cm, top_cm, right_cm, bottom_cm = 4.0, 4.0, 3.0, 3.0
        
    top_dxa = int(top_cm * 567)
    bottom_dxa = int(bottom_cm * 567)
    left_dxa = int(left_cm * 567)
    right_dxa = int(right_cm * 567)
    
    # Halaman A4: lebar 21 cm (11906 dxa), tinggi 29.7 cm (16838 dxa)
    sect_pr = (
        f'<w:sectPr>'
        f'<w:pgSz w:w="11906" w:h="16838"/>'
        f'<w:pgMar w:top="{top_dxa}" w:bottom="{bottom_dxa}" w:left="{left_dxa}" w:right="{right_dxa}" '
        f'w:header="708" w:footer="708" w:gutter="0"/>'
        f'</w:sectPr>'
    )
    
    body_xml = markdown_to_docx_body(md_content)
    document_xml = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">\n'
        f'<w:body>\n'
        f'{body_xml}\n'
        f'{sect_pr}\n'
        f'</w:body>\n'
        f'</w:document>'
    )
    
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES_XML)
        docx.writestr("_rels/.rels", RELS_XML)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS_XML)
        docx.writestr("word/styles.xml", STYLES_XML)
        docx.writestr("word/document.xml", document_xml)

def main():
    parser = argparse.ArgumentParser(description="Konversi naskah Markdown ke Microsoft Word (.docx) siap cetak format kampus.")
    parser.add_argument("input", help="File naskah input (.md atau .txt)")
    parser.add_argument("-o", "--output", help="Nama file hasil output .docx (default: sama dengan input)")
    parser.add_argument("--margin", default="4-4-3-3", help="Margin halaman Kiri-Atas-Kanan-Bawah dalam cm (default: 4-4-3-3)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File input '{args.input}' tidak ditemukan.")
        sys.exit(1)

    output_file = args.output
    if not output_file:
        base_name = os.path.splitext(args.input)[0]
        output_file = f"{base_name}.docx"

    with open(args.input, "r", encoding="utf-8", errors="ignore") as f:
        md_text = f.read()

    print("=" * 65)
    print(" GENERATOR DOKUMEN WORD (.DOCX) - STANDAR AKADEMIK INDONESIA")
    print("=" * 65)
    print(f"Input File      : {args.input}")
    print(f"Output File     : {output_file}")
    print(f"Format Standar  : A4, Margin {args.margin} cm, Times New Roman 12pt, Spasi 1.5")
    
    build_docx(md_text, output_file, margin=args.margin)
    
    print("-" * 65)
    print(f"[SUKSES] Dokumen Word siap cetak berhasil dibuat:")
    print(f"👉 {output_file} ({os.path.getsize(output_file):,} bytes)")
    print("=" * 65)

if __name__ == "__main__":
    main()
