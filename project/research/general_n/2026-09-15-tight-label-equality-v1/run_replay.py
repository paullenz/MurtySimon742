#!/usr/bin/env python3
import argparse,csv,json,subprocess,tempfile
from pathlib import Path
from scan_equality import run,read_inputs

root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--base',type=Path,default=root.parent/'2026-09-15-tight-label-block-v1');a=ap.parse_args()
got=run(a.base);expected=json.loads((root/'RESULTS.json').read_text());assert got==expected
ps,_=read_inputs(a.base);checked={(p['layer'],p['state_id']):p for p in got['rows']}
with tempfile.TemporaryDirectory() as td:
    exe=Path(td)/'verify'
    subprocess.run(['g++','-std=c++17','-O2',str(root/'verify_equality.cpp'),'-o',str(exe)],check=True)
    result=subprocess.run([str(exe),str(a.base/'INDEPENDENT_INPUT.txt')],check=True,capture_output=True,text=True).stdout
    assert result==(root/'INDEPENDENT_RESULTS.tsv').read_text()
    rows=list(csv.DictReader(result.splitlines(),delimiter='\t'))
    assert len(rows)==len(ps)==4588
    for row,p in zip(rows,ps):
        key=(p['layer'],p['state_id']);assert (row['layer'],int(row['state_id']))==key
        assert bool(int(row['applicable']))==(key in checked)
        assert bool(int(row['rejected']))==(key in checked and checked[key]['rejected'])
print('PASS: 4,588 Python/C++ decisions, 164 applicable/rejected states, 25 active whole-state certificates; not promoted.')
