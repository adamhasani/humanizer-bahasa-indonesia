#!/usr/bin/env python3
"""Bersihkan metadata dokumen (PDF) dari jejak AI/tool sebelum dikumpulkan.
Usage: python3 clean_metadata.py file.pdf [--author "Nama"]"""
import sys, argparse
from pypdf import PdfReader, PdfWriter

def clean(path, author):
    r = PdfReader(path)
    w = PdfWriter()
    for p in r.pages:
        w.add_page(p)
    w.add_metadata({
        '/Title': (r.metadata or {}).get('/Title') or path.rsplit('/',1)[-1].rsplit('.',1)[0],
        '/Author': author,
        '/Creator': 'Microsoft Word',
        '/Producer': 'Microsoft Word',
    })
    out = path.rsplit('.',1)[0] + '_clean.pdf'
    with open(out, 'wb') as f:
        w.write(f)
    print(out)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--author', default='Mahasiswa')
    a = ap.parse_args()
    clean(a.file, a.author)
