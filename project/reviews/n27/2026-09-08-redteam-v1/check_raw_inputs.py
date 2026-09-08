#!/usr/bin/env python3
"""Reject malformed/signed/floating C++ input tokens before frozen n27 replay.
Covers every original C++ outer ledger, frontier, subset cut and survivor row.
The frozen C++ reader extracts digits; this guard parses real JSON and checks
record shapes. Manifest hashing and mathematical replay remain separate checks.
"""
import argparse,gzip,hashlib,json
from pathlib import Path

def require(ok,detail):
    if not ok:raise ValueError(detail)

def ints(x):
    if type(x) is list:
        for y in x:ints(y)
    else:require(type(x) is int and 0<=x<=2147483647,'bounded nonnegative integer required')

def check(p):
    digest=hashlib.sha256();count=0
    name=p.name
    with gzip.open(p,'rt',encoding='utf-8') as f:
        for line in f:
            row=json.loads(line);require(type(row) is list,'array required');ints(row)
            if name.endswith('_ledger.jsonl.gz'):
                require(len(row)==6,'ledger shape');k,r,d,rho,kind,w=row
                require(len(d)==11 and len(rho)==15 and 0<=kind<=4,'ledger dimensions')
            elif name.endswith('_frontier.jsonl.gz'):
                require(len(row)==5,'frontier shape');k,r,d,rho,lo=row
                require(len(d)==len(lo)==11 and len(rho)==15,'frontier dimensions')
            elif name.endswith('_cuts.jsonl.gz'):
                require(len(row)==4,'cut shape');state,R,c,mask=row
                require(len(R)==11 and len(c)==15 and mask<2048,'cut dimensions')
            elif name.endswith('_survivors.jsonl.gz'):
                require(len(row)==7,'survivor shape');state,k,r,d,rho,R,c=row
                require(len(d)==len(R)==11 and len(rho)==len(c)==15,'survivor dimensions')
            else:raise ValueError('unexpected path')
            digest.update(line.encode());count+=1
    return {'path':name,'rows':count,'decompressed_sha256':digest.hexdigest()}

def run(root):
    files=[]
    for e in (182,183):
        for s in ('ledger','frontier','cuts','survivors','pair_survivors'):
            p=root/f'd15_{e}_{s}.jsonl.gz';require(p.is_file(),str(p));files.append(p)
    for s in ('frontier','cuts','survivors'):
        p=root/f'validation_{s}.jsonl.gz';require(p.is_file(),str(p));files.append(p)
    records=[check(p) for p in files]
    return {'status':'PASS','files':records,'total_rows':sum(x['rows'] for x in records),'scope':'Strict JSON/token/shape validation; not a replacement for the graph lemmas or arithmetic inequalities.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=run(a.root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print('Strict C++ input guard: PASS',r['total_rows'],'rows')
