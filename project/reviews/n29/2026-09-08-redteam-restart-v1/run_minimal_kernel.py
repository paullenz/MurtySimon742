#!/usr/bin/env python3
"""Exact-certificate runner for the minimal n=29 Delta=16 kernel.
Reads minimal_prepare demands plus minimal_rows residual survivors directly.
"""
import argparse,gzip,hashlib,json,multiprocessing as mp,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from independent_threshold_model_v2 import build,exact_certificate,verify_certificate
D=None;ROWS=None;T=None

def init_worker(demands,rows,t):
    global D,ROWS,T;D=demands;ROWS=rows;T=t

def work(pos):
    row=ROWS[pos];s=D[row[0]]['s'];rho=row[2:];m=build(s,rho,T);res=m.solve()
    if res.status!=2:return {'position':pos,'status':int(res.status),'certificate':None}
    c=exact_certificate(m)
    if c is None:return {'position':pos,'status':2,'certificate':None}
    verify_certificate(m,c);return {'position':pos,'status':2,'certificate':c}

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--t',type=int,choices=[2,3],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--workers',type=int,default=4);p.add_argument('--shard',type=int,default=0);p.add_argument('--shards',type=int,default=1);a=p.parse_args()
    demands=json.loads((a.root/'demands.json').read_text())
    rows=[list(map(int,x.split())) for x in (a.root/'row_survivors.txt').read_text().splitlines() if x.strip()]
    positions=[i for i in range(len(rows)) if i%a.shards==a.shard];start=time.time();out=[]
    ctx=mp.get_context('fork')
    with ctx.Pool(a.workers,initializer=init_worker,initargs=(demands,rows,a.t)) as pool:
        for rec in pool.imap_unordered(work,positions,chunksize=1):out.append(rec)
    out.sort(key=lambda x:x['position']);assert [x['position'] for x in out]==positions
    assert all(x['certificate'] is not None for x in out)
    rhs=[x['certificate']['rhs'] for x in out];raw=(json.dumps(out,separators=(',',':'))+'\n').encode();gz=gzip.compress(raw,mtime=0)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(gz)
    rep={'schema':'n29-minimal-kernel-shard-v1','t':a.t,'m':208+a.t,'shard':a.shard,'shards':a.shards,'positions':positions,'input_rows':len(out),'exact_rejections':len(out),'final_survivors':0,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest(),'seconds':time.time()-start}
    (a.output.with_suffix(a.output.suffix+'.report.json')).write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps({k:v for k,v in rep.items() if k!='positions'}))
if __name__=='__main__':main()
