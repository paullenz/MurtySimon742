#!/usr/bin/env python3
"""Shardable numerical/exact scan of n=30 Delta16 row survivors.

Numerical infeasibility is reconnaissance only.  In --exact mode a row is
counted rejected only if n30_threshold_model.exact_certificate returns a
certificate that verify_certificate checks exactly.
"""
import argparse,gzip,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from n30_threshold_model import build,exact_certificate,verify_certificate

def load_demands(path):
    with open(path) as f:
        N=int(f.readline());out=[]
        for _ in range(N):
            z=list(map(int,f.readline().split()));out.append(z[:13])
    return out

def load_rows(path):
    out=[]
    with open(path) as f:
        for pos,line in enumerate(f):
            z=list(map(int,line.split()))
            out.append((pos,z[0],z[1],z[2:]))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--m',type=int,choices=[225,226],required=True);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=1)
    ap.add_argument('--exact',action='store_true');ap.add_argument('--output',type=Path)
    z=ap.parse_args();assert 0<=z.shard<z.shards
    D=load_demands(z.demands);R=load_rows(z.rows);t=z.m-224
    counts={'rows_total':len(R),'rows_in_shard':0,'numerical_infeasible':0,'numerical_other':0,'exact_rejected':0,'exact_missing':0}
    survivors=[];certs=[]
    for pos,did,total,rho in R:
        if pos%z.shards!=z.shard:continue
        counts['rows_in_shard']+=1;m=build(D[did],rho,t);sol=m.solve()
        if sol.status==2:
            counts['numerical_infeasible']+=1
            if z.exact:
                c=exact_certificate(m)
                if c is None:counts['exact_missing']+=1;survivors.append({'position':pos,'demand_id':did,'total':total,'rho':rho,'reason':'no_exact_certificate'})
                else:
                    verify_certificate(m,c);counts['exact_rejected']+=1;certs.append({'position':pos,'demand_id':did,'total':total,'rho':rho,'certificate':c})
        else:
            counts['numerical_other']+=1;survivors.append({'position':pos,'demand_id':did,'total':total,'rho':rho,'solver_status':int(sol.status)})
    rep={'schema':'n30-d16-threshold-scan-v1','status':'PASS','scope':{'n':30,'Delta':16,'m':z.m,'t':t},'shard':z.shard,'shards':z.shards,'exact_mode':z.exact,'counts':counts,'survivors':survivors}
    print(json.dumps(rep,separators=(',',':')))
    if z.output:
        z.output.parent.mkdir(parents=True,exist_ok=True)
        if z.output.suffix=='.gz':
            with gzip.open(z.output,'wt') as f:json.dump({'report':rep,'certificates':certs},f,separators=(',',':'))
        else:z.output.write_text(json.dumps({'report':rep,'certificates':certs},separators=(',',':'))+'\n')
if __name__=='__main__':main()
