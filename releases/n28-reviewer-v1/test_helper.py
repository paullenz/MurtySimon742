#!/usr/bin/env python3
"""Fail-closed input regressions and complete valid-domain comparison."""
from pathlib import Path
import argparse,json,subprocess,hashlib

def main():
    p=argparse.ArgumentParser();p.add_argument('--original-v8',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    root=Path(__file__).resolve().parent;out=a.output.resolve()
    if out.exists():raise ValueError('Output must be new')
    out.mkdir(parents=True);exe=out/'check_rows'
    subprocess.run(['g++','-O3','-std=c++17',str(root/'check_rows_hardened.cpp'),'-o',str(exe)],check=True)
    def invoke(name,text):
        i=out/(name+'.txt');o=out/(name+'.rows');b=out/(name+'.bands');i.write_text(text)
        r=subprocess.run([str(exe),str(i),str(o),str(b)],capture_output=True,text=True)
        (out/(name+'.stderr')).write_text(r.stderr)
        return r,o,b
    row='0 0 0 0 3 4 4 4 4 4 4 4'
    tests={'interval_64':'1\n'+row+' 64 64\n','interval_below15':'1\n'+row+' 14 15\n','inverted_interval':'1\n'+row+' 28 27\n',
       'negative_count':'-1\n','zero_count':'0\n','huge_count':'999999999999999999999999\n','too_many_records':'1230\n','truncated':'1\n'+row+' 27\n',
       'negative_demand':'1\n-1 '+'0 '*11+'15 15\n','oversized_demand':'1\n'+'0 '*11+'12 15 15\n','unsorted':'1\n1 '+'0 '*11+'15 15\n',
       'duplicate':'2\n'+row+' 27 27\n'+row+' 27 27\n','trailing':'1\n'+row+' 27 27\nEXTRA\n'}
    results={}
    for n,text in tests.items():
        r,o,b=invoke(n,text)
        if r.returncode==0 or o.exists() or b.exists():raise ValueError('Malformed input accepted or output opened: '+n)
        results[n]={'exit_code':r.returncode,'rejected_before_output_creation':True}
    ev=a.original_v8/'evidence';r,o,b=invoke('complete_valid_scope',(ev/'demands.txt').read_text())
    if r.returncode:raise ValueError('Valid scope failed')
    report=json.loads(r.stdout);expected=json.loads((ev/'ROWS_CHECK_REPORT.json').read_text())
    if report!=expected or o.read_bytes()!=(ev/'check_row_survivors.txt').read_bytes() or b.read_bytes()!=(ev/'check_row_bands.txt').read_bytes():raise ValueError('Valid output changed')
    result={'all_pass':True,'malformed_inputs':results,'valid_scope':report,'survivor_bytes_identical':True,'band_bytes_identical':True,'hardened_sha256':hashlib.sha256((root/'check_rows_hardened.cpp').read_bytes()).hexdigest(),'original_archives_modified':False}
    (out/'HELPER_TEST_REPORT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
