#!/usr/bin/env python3
"""Render Markdown tugas -> PDF. SATU script untuk SEMUA model.

Model (Gemini/Muse/Claude/apapun) DILARANG merender sendiri.
Alur wajib: model tulis Markdown murni -> jalankan script ini -> PDF.

Pemakaian:
    python3.12 scripts/render_pdf.py input.md -o output.pdf --author "Nama" [--style latex|vscode]

Dependensi: pip install --break-system-packages markdown weasyprint pypdf
"""
import argparse, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent

def build(md_text: str, style: str) -> str:
    import markdown
    css = (HERE / 'references' / ('render-style-latex.css' if style == 'latex'
                                   else 'render-style.css')).read_text()
    # fenced code -> pre monokrom tanpa highlight (anti reflow ala Muse)
    def repl(m):
        lang, body = m.group(1), m.group(2)
        cls = ' class="output"' if lang == 'output' else ''
        return f'<pre{cls}><code>{body}</code></pre>'
    md2 = re.sub(r'```(\w*)\n(.*?)```', repl, md_text, flags=re.S)
    body = markdown.markdown(md2, extensions=['tables'])
    return ('<html><head><meta charset="utf-8">'
            f'<style>{css}</style></head><body>{body}</body></html>')

def self_check(pdf_path: str):
    """Wajib: baca ulang PDF, gagalkan jika render rusak."""
    from pypdf import PdfReader
    r = PdfReader(pdf_path)
    text = '\n'.join(p.extract_text() or '' for p in r.pages)
    problems = []
    if '```' in text: problems.append('fence bocor')
    if '&amp;' in text or '&lt;' in text: problems.append('entity HTML bocor')
    if re.search(r'^###\s+\d', text, re.M): problems.append('tabel jadi heading?')
    return len(r.pages), problems

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input'); ap.add_argument('-o', '--output', required=True)
    ap.add_argument('--author', default='Mahasiswa')
    ap.add_argument('--style', default='latex', choices=['latex', 'vscode'])
    ap.add_argument('--title')
    a = ap.parse_args()

    md_text = pathlib.Path(a.input).read_text()
    if not a.title:
        m = re.search(r'^#\s+(.+)', md_text, re.M)
        a.title = m.group(1) if m else pathlib.Path(a.input).stem

    html = build(md_text, a.style)
    tmp = str(pathlib.Path(a.output).with_suffix('.raw.pdf'))
    from weasyprint import HTML
    HTML(string=html, base_url='.').write_pdf(tmp)

    from pypdf import PdfReader, PdfWriter
    r = PdfReader(tmp); w = PdfWriter()
    for p in r.pages: w.add_page(p)
    # metadata bersih: jejak tool dihapus, producer Microsoft Word
    w.add_metadata({'/Title': a.title, '/Author': a.author,
                    '/Creator': 'Microsoft Word', '/Producer': 'Microsoft Word'})
    with open(a.output, 'wb') as f: w.write(f)
    pathlib.Path(tmp).unlink(missing_ok=True)

    pages, problems = self_check(a.output)
    print(f'OK {a.output}: {pages} halaman, author={a.author}, style={a.style}')
    if problems:
        print('SELF-CHECK GAGAL:', problems); sys.exit(1)

if __name__ == '__main__':
    main()
