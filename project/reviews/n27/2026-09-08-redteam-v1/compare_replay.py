#!/usr/bin/env python3
"""Compare original and regenerated n27 evidence; normalize one proved gzip link.
No arbitrary hash fields are ignored. Both raw links and decompressed equality
must verify before the sole known compression-dependent field is normalized.
"""
import argparse,copy,gzip,hashlib,json
from pathlib import Path

def sha(p,decompress=False):
    h=hashlib.sha256();op=gzip.open if decompress else open
    with op(p,'rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()

def run(old,new):
    records=[];mismatches=[]
    for p in sorted(new.rglob('*')):
        if not p.is_file():continue
        name=p.relative_to(new).as_posix();q=old/name
        if not q.is_file() or p.suffix in ('.log','') or '__pycache__' in p.parts:continue
        mode='decompressed SHA256' if p.suffix=='.gz' else 'SHA256'
        xsha,ysha=sha(p,p.suffix=='.gz'),sha(q,q.suffix=='.gz')
        eq=xsha==ysha;link=None
        if name=='d15_182_supplement_certificates.json':
            x=json.loads(p.read_text());y=json.loads(q.read_text())
            target='d15_182_pair_survivors.jsonl.gz'
            links=(x['input_sha256']==sha(new/target) and y['input_sha256']==sha(old/target))
            data_equal=sha(new/target,True)==sha(old/target,True)
            link={'target':target,'new_raw_sha256':sha(new/target),'original_raw_sha256':sha(old/target),'both_raw_links_valid':links,'decompressed_equal':data_equal}
            x.pop('input_sha256');y.pop('input_sha256')
            eq=links and data_equal and x==y;mode='JSON after verified gzip-link normalization'
        records.append({'path':name,'comparison':mode,'equal':eq,'new_content_sha256':xsha,'original_content_sha256':ysha,**({'link':link} if link else {})})
        if not eq:mismatches.append(name)
    required={f'd16_{e}/{f}' for e in (182,183) for f in ('primary_summary.json','independent_summary.json','primary_column_cases.json','primary_ledger.jsonl.gz')}
    required|={f'd15_{e}_{s}' for e in (182,183) for s in ('ledger.jsonl.gz','frontier.jsonl.gz','columns.jsonl','check_columns.jsonl','cuts.jsonl.gz','survivors.jsonl.gz','pair_certificates.json.gz','pair_survivors.jsonl.gz','column_summary.json','check_column_summary.json','outer_check.json','summary.jsonl','pair_summary.json')}
    required|={'d15_182_supplement_certificates.json','FINAL_CHECK.json','COLUMN_SAMPLE_CHECK.json','PREFLIGHT_CHECK.json','structural_results.json','tested_graphs.json'}
    missing=sorted(required-{r['path'] for r in records})
    return {'status':'PASS' if not missing and not mismatches else 'FAIL','comparisons':records,'missing_required':missing,'mismatches':mismatches,'scope':'Complete regenerated data plus available copied source files; logs are preserved separately.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('original',type=Path);p.add_argument('replay',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=run(a.original,a.replay);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(r['status'],len(r['comparisons']),'comparisons')
    if r['status']!='PASS':raise SystemExit(1)
