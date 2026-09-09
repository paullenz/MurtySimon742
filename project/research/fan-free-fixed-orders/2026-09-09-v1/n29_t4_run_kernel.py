#!/usr/bin/env python3
"""Exact-certificate runner for n29 Delta16 t=4 Fan-free closure.

Same model/certificate functions as the frozen n29 minimal trusted kernel; this
wrapper removes only the historical argparse choices=[2,3] restriction.
"""
import argparse,gzip,hashlib,json,multiprocessing as mp,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
D=ROOT/'project/reviews/n29/2026-09-08-redteam-restart-v1'
sys.path.insert(0,str(D))
from independent_threshold_model_v2 import build,exact_certificate,verify_certificate
DEMANDS=None;ROWS=None

def init_worker(demands,rows):
    global DEMANDS,ROWS;DEMANDS=demands;ROWS=rows

def work(pos):
    row=ROWS[pos];s=DEMANDS[row[0]]['s'];rho=row[2:];m=build(s,rho,4);res=m.solve()
    if res.status!=2:return {'position':pos,'status':int(res.status),'certificate':None}
    c=exact_certificate(m)
    if c is None:return {'position':pos,'status':2,'certificate':None}
    verify_certificate(m,c);return {'position':pos,'status':2,'certificate':c}

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--workers',type=int,default=4);a=p.parse_args()
    demands=json.loads((a.root/'demands.json').read_text());rows=[list(map(int,x.split())) for x in (a.root/'row_survivors.txt').read_text().splitlines() if x.strip()]
    start=time.time();out=[];ctx=mp.get_context('fork')
    with ctx.Pool(a.workers,initializer=init_worker,initargs=(demands,rows)) as pool:
        for rec in pool.imap_unordered(work,range(len(rows)),chunksize=1):out.append(rec)
    out.sort(key=lambda x:x['position']);assert [x['position'] for x in out]==list(range(len(rows)))
    bad=[x for x in out if x['certificate'] is None];assert not bad,bad[:3]
    rhs=[x['certificate']['rhs'] for x in out];raw=(json.dumps(out,separators=(',',':'))+'\n').encode();gz=gzip.compress(raw,mtime=0)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(gz)
    rep={'schema':'fan-free-n29-t4-kernel-v1','n':29,'Delta':16,'m':212,'t':4,'input_rows':len(out),'exact_rejections':len(out),'final_survivors':0,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest(),'seconds':time.time()-start,'frozen_model_source':'project/reviews/n29/2026-09-08-redteam-restart-v1/independent_threshold_model_v2.py'}
    (a.output.with_suffix(a.output.suffix+'.report.json')).write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps(rep))
if __name__=='__main__':main()
