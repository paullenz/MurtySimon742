#!/usr/bin/env python3
"""Mutation audit of frozen n27 verifiers; originals are copied, never edited."""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path

def need(x,msg):
    if not x:raise ValueError(msg)

def writegz(p,obj,lines=False):
    with gzip.open(p,'wt') as f:
        if lines:
            for row in obj:f.write(json.dumps(row,separators=(',',':'))+'\n')
        else:json.dump(obj,f,separators=(',',':'))

def strict_nonnegative(obj):
    if type(obj) is list:
        for x in obj:strict_nonnegative(x)
    elif type(obj) is not int or obj<0 or obj>2**31-1:
        raise ValueError('Expected a bounded nonnegative JSON integer')

def run(root,out):
    need(not out.exists(),'new output required');out.mkdir(parents=True)
    work=out/'scratch';work.mkdir()
    for p in root.glob('d15_*'):
        if p.is_file() and ('pair_' in p.name or 'supplement_' in p.name or p.name.endswith('_survivors.jsonl.gz')):
            shutil.copyfile(p,work/p.name)
    shutil.copyfile(root/'check_final.py',work/'check_final.py')
    def final():return subprocess.run([sys.executable,'-I','-B','check_final.py'],cwd=work,text=True,capture_output=True)
    baseline=final();need(baseline.returncode==0,baseline.stderr)
    records=[]
    p=work/'d15_183_pair_certificates.json.gz';baseline_bytes=p.read_bytes()
    data=json.load(gzip.open(p,'rt'))
    for name,changed in [('missing_pair_certificate',data[:-1]),('duplicate_pair_certificate',data+[data[0]])]:
        writegz(p,changed);r=final();need(r.returncode!=0,name+' accepted')
        records.append({'test':name,'exit_code':r.returncode,'result':'REJECTED'})
        (out/(name+'.stderr.txt')).write_text(r.stderr)
    changed=copy.deepcopy(data);changed[0]['witness']['required']=changed[0]['witness']['available_pairs']
    writegz(p,changed);r=final();need(r.returncode!=0,'non-strict certificate accepted')
    records.append({'test':'non_strict_pair_certificate','exit_code':r.returncode,'result':'REJECTED'})
    (out/'non_strict_pair_certificate.stderr.txt').write_text(r.stderr);p.write_bytes(baseline_bytes)
    p=work/'d15_182_supplement_certificates.json';original=p.read_bytes();s=json.loads(original)
    s['certificates']=s['certificates'][:-1];p.write_text(json.dumps(s));r=final();need(r.returncode!=0,'missing supplement accepted')
    records.append({'test':'missing_supplement_certificate','exit_code':r.returncode,'result':'REJECTED'})
    (out/'missing_supplement_certificate.stderr.txt').write_text(r.stderr);p.write_bytes(original)
    # Only small cross-language fixture is used for executable parser tests.
    build=subprocess.run(['g++','-O2','-std=c++17',str(root/'columns.cpp'),'-lz','-lcrypto','-o',str(work/'columns')],capture_output=True,text=True)
    need(build.returncode==0,build.stderr)
    frontier=work/'validation_frontier.jsonl.gz';shutil.copyfile(root/frontier.name,frontier)
    cs=[json.loads(s) for s in gzip.open(root/'validation_cuts.jsonl.gz','rt')]
    cases={
      'original':copy.deepcopy(cs),
      'negative_source_cap':copy.deepcopy(cs),
      'false_subset_mask':copy.deepcopy(cs),
      'missing_subset_certificate':[],
      'duplicate_subset_certificate':cs+cs}
    cases['negative_source_cap'][0][2][0]*=-1
    cases['false_subset_mask'][0][-1]=1
    for name,rows in cases.items():
        prefix=work/name;writegz(Path(str(prefix)+'_cuts.jsonl.gz'),rows,lines=True)
        r=subprocess.run([str(work/'columns'),'check','27','15','0',str(frontier),str(prefix),str(work/('checked_'+name))],capture_output=True,text=True)
        (out/(name+'.stdout.txt')).write_text(r.stdout);(out/(name+'.stderr.txt')).write_text(r.stderr)
        if name=='original':need(r.returncode==0,r.stderr)
        elif name=='negative_source_cap':
            need(r.returncode==0,'reproduction of digit-parser issue changed')
            try:strict_nonnegative(rows)
            except ValueError:guard='REJECTED'
            else:guard='ACCEPTED'
            need(guard=='REJECTED','strict guard failure')
            records.append({'test':name,'exit_code':r.returncode,'result':'ACCEPTED_BY_FROZEN_DIGIT_SCANNER','strict_json_guard':guard,'frozen_manifest_would_reject_changed_bytes':True})
        else:
            need(r.returncode!=0,name+' accepted');records.append({'test':name,'exit_code':r.returncode,'result':'REJECTED'})
    result={'status':'COMPLETED_WITH_PARSER_HARDENING_FINDING','tests':records,'no_frozen_input_modified':True,'scope':'Malformed raw inputs, not a counterexample to the graph theorem. The published manifest pins the intended bytes.'}
    (out/'MUTATION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    shutil.rmtree(work)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.root.resolve(),a.output.resolve())
