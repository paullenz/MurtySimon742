#!/usr/bin/env python3
"""PDF geometry/text preflight; visual page inspection remains separate."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import platform
import re
import subprocess
import pdfplumber

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OUT=ROOT/'releases/n30-reviewer-v3'


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    files=[]
    for path in sorted(OUT.glob('*.pdf')):
        with pdfplumber.open(path) as pdf:
            pages=[];fulltext=[]
            for i,p in enumerate(pdf.pages,1):
                chars=[c for c in p.chars if c['text'].strip()]
                assert chars,(path.name,i,'blank page')
                outside=[c for c in chars if c['x0']<15 or c['x1']>p.width-15 or c['top']<15 or c['bottom']>p.height-15]
                assert not outside,(path.name,i,'outside safe page area',outside[:1])
                assert not any(c['text']=='\ufffd' for c in chars),(path.name,i,'replacement glyph')
                pages.append({'page':i,'width':round(p.width,2),'height':round(p.height,2),'characters':len(chars)})
                fulltext.append(p.extract_text() or '')
            text='\n'.join(fulltext)
            if 'Manuscript' in path.name:
                assert all(f'Appendix {letter}.' in text for letter in 'ABCDEFGH')
                assert len(re.findall(r'^(?:B1|B2|B3|C1)\s',text,re.M))==211
                actual=re.findall(r'^(B1|B2|B3|C1)\s+(\([^)]*\))\s+(\([^)]*\))',text,re.M)
                original=ROOT/'project/research/n30/2026-09-11-m225-resource-envelope-v1/EXACT_APPENDIX.md'
                expected=[]
                for line in original.read_text().splitlines():
                    if re.match(r'^\| (B1|B2|B3|C1) \|',line):
                        fields=[v.strip() for v in line.strip('|').split('|')]
                        expected.append(tuple(fields[:3]))
                compact=lambda rows:[tuple(re.sub(r'\s+','',s) for s in row) for row in rows]
                assert compact(actual)==compact(expected),'PDF histogram typography changed the 211 rows'
            files.append({'path':path.relative_to(ROOT).as_posix(),'sha256':sha256(path.read_bytes()).hexdigest(),'pages':pages})
    result={'schema':'n30-reviewer-v3-pdf-preflight-v1','geometry_and_text_status':'PASS','files':files,
        'python':platform.python_version(),
        'pandoc':subprocess.check_output(['pandoc','--version'],text=True).splitlines()[0],
        'xelatex':subprocess.check_output(['xelatex','--version'],text=True).splitlines()[0],
        'visual_inspection_required':True}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','pages':{Path(f['path']).name:len(f['pages']) for f in files}}))


if __name__=='__main__':
    main()
