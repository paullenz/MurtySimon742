#!/usr/bin/env python3
"""Exact row-threshold + corrected threshold/source-flow closure for n30 Delta16 m227..230.

Reuses the audited n30 threshold model. Floating infeasibility is proposal-only;
every accepted rejection has an exact integer Farkas certificate verified by the
model's exact checker.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_threshold_model.py'
sp=spec_from_file_location('model',p);model=module_from_spec(sp);sp.loader.exec_module(model)
A=13

def load_demands(path):
    with open(path) as f:
        N=int(f.readline());out=[]
        for _ in range(N):out.append(list(map(int,f.readline().split()))[:A])
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,choices=[227,228,229,230],required=True);ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    D=load_demands(z.demands);t=z.m-224;rows=[list(map(int,line.split())) for line in z.rows.read_text().splitlines() if line.strip()]
    cnt={'rows':len(rows),'source_count':0,'threshold':0,'model_exact_rejected':0,'model_noninfeasible':0,'model_exact_missing':0};survivors=[];certs=[]
    for pos,row in enumerate(rows):
        did=row[0];rho=row[2:];s=D[did];bad=None
        for h in range(2,A):
            high=[x for x in s if x>=h]
            if not high:continue
            zh=sum(x>=h for x in rho)
            if max(high)>zh:bad='source_count';break
            W=sum(high)
            if 2*W>zh*zh-zh+h*(h+1):bad='threshold';break
        if bad:cnt[bad]+=1;continue
        m=model.build(s,rho,t);sol=m.solve()
        if sol.status!=2:
            cnt['model_noninfeasible']+=1;survivors.append({'position':pos,'demand_id':did,'total':row[1],'rho':rho,'solver_status':int(sol.status)});continue
        c=model.exact_certificate(m)
        if c is None:
            cnt['model_exact_missing']+=1;survivors.append({'position':pos,'demand_id':did,'total':row[1],'rho':rho,'reason':'no_exact_certificate'});continue
        model.verify_certificate(m,c);cnt['model_exact_rejected']+=1;certs.append({'position':pos,'demand_id':did,'total':row[1],'rho':rho,'certificate':c})
    rep={'schema':'fan-free-n30-d16-upper-close-v1','scope':{'n':30,'Delta':16,'m':z.m,'a':13,'b':16,'t':t,'dmax':11},'counts':cnt,'final_survivors':len(survivors),'survivors':survivors,'parameterized_model_source':str(p.relative_to(ROOT)),'all_model_rejections_exact_integer_farkas_verified':True,'floating_infeasibility_alone_accepted':False}
    raw=(json.dumps({'report':rep,'certificates':certs},separators=(',',':'))+'\n').encode();gz=gzip.compress(raw,mtime=0);z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_bytes(gz)
    rr={k:v for k,v in rep.items() if k!='survivors'};rr['json_sha256']=hashlib.sha256(raw).hexdigest();rr['gzip_sha256']=hashlib.sha256(gz).hexdigest();print(json.dumps(rr,sort_keys=True));assert not survivors,rep
if __name__=='__main__':main()
