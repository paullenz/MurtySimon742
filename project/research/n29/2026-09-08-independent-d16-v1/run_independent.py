#!/usr/bin/env python3
"""End-to-end independent late-stage N29 Delta16 replay from prepared finite inputs."""
import argparse,json,gzip,time,hashlib
from pathlib import Path
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from multiprocessing import get_context
from fresh_joint import propagate
from fresh_endpoint import build,certificate,verify

def charging_count(t):
    need=16+2*t;count=0
    def rec(pos,lo,total):
        nonlocal count
        if pos==12:
            if total>=need:count+=1
            return
        for s in range(lo,11):
            rec(pos+1,s,total+Fraction(s*(13-2*s),12-s))
    rec(0,0,Fraction(0));return count

def profile_counts():
    @lru_cache(None)
    def f(left,lo,total):
        if left==0:return int(total==0)
        if total<lo*left or total>12*left:return 0
        return sum(f(left-1,v,total-v) for v in range(lo,13))
    return {r:f(16,1,r) for r in range(16,67)}

def projected(s,rho,r,t):
    slack=sum(s)-r-2*t
    if slack and 0 not in s:return False
    D=2*r+2*t
    for j in range(2,11):
        pairs=sum(rho[u]+rho[v]>=j for u in range(16) for v in range(u+1,16))
        forced=[x for x in s if x>=j];optional=sorted(x for x in s if x<j);bounds=[]
        for h in range(len(forced),13):
            if 10*h+(12-h)*(j-1)<D or j*h>D:continue
            q=sum(forced)+sum(optional[:h-len(forced)])
            high=max(h*j,D-(12-h)*(j-1))
            q=max(q,high-sum(min(x,h) for x in rho));bounds.append(q)
        if not bounds or min(bounds)>pairs:return False
    return True

def worker(arg):
    t,rec=arg;m=build(rec['s'],rec['row'][2:],rec['state'],t);res=m.solve()
    if res.status!=2:return {'position':rec['position'],'error':'endpoint LP not infeasible','status':int(res.status)}
    c=certificate(m)
    if c is None:return {'position':rec['position'],'error':'no exact Farkas certificate'}
    verify(m,c)
    return {'position':rec['position'],'rhs':c['rhs'],'variables':len(m.names),'inequalities':len(m.ub),'equalities':len(m.eq),'certificate':c}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prepared',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--jobs',type=int,default=4);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    expected={3:{'domain':4867,'raw':1848957,'projected':118,'joint':{'survivor':36,'source_matching':38,'source_hall':2,'joint_total_source':42}},2:{'domain':9251,'raw':5765218,'projected':1225,'joint':{'survivor':593,'source_matching':311,'source_hall':29,'label_domain':6,'total_source':58,'joint_total_source':222,'pair_hall':6}}}
    pc=profile_counts();allstates={};allcerts={};summary={}
    for t in (3,2):
        P=a.prepared/f't{t}';D=json.loads((P/'demands.json').read_text());rows=[]
        assert charging_count(t)==expected[t]['domain']
        raw=sum(sum(pc[r] for r in range(x['rmin'],x['rmax']+1)) for x in D);assert raw==expected[t]['raw']
        for line in (P/'row_survivors.txt').read_text().splitlines():
            row=list(map(int,line.split()));s=D[row[0]]['s']
            if projected(s,row[2:],row[1],t):rows.append(row)
        saved=json.loads((P/'projected_survivors.json').read_text());assert rows==saved and len(rows)==expected[t]['projected']
        counts=Counter();surv=[];start=time.time()
        for pos,row in enumerate(rows):
            s=D[row[0]]['s'];st=propagate(s,row[2:],t);counts[st['kind']]+=1
            if st['kind']=='survivor':surv.append({'position':pos,'row':row,'s':s,'state':st})
        assert dict(counts)==expected[t]['joint'],(t,counts)
        allstates[str(208+t)]=surv
        with get_context('fork').Pool(a.jobs) as pool:cert=pool.map(worker,[(t,x) for x in surv])
        bad=[x for x in cert if 'error' in x];assert not bad,bad
        allcerts[str(208+t)]=cert
        summary[str(208+t)]={'charging_domain':expected[t]['domain'],'raw_residual_profiles':raw,'projected_rows':len(rows),'joint_counts':dict(counts),'exact_endpoint_certificates':len(cert),'rhs_min':min(x['rhs'] for x in cert),'rhs_max':max(x['rhs'] for x in cert),'seconds':time.time()-start}
        print(t,summary[str(208+t)],flush=True)
    def dump(name,obj):
        raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();gz=gzip.compress(raw,mtime=0);p=a.output/name;p.write_bytes(gz);return {'file':name,'bytes':len(gz),'sha256':hashlib.sha256(gz).hexdigest(),'json_bytes':len(raw),'json_sha256':hashlib.sha256(raw).hexdigest()}
    states=dump('N29_INDEPENDENT_D16_STATES.json.gz',{'schema':'n29-independent-d16-joint-states-v1',**allstates});certs=dump('N29_INDEPENDENT_D16_CERTIFICATES.json.gz',{'schema':'n29-independent-d16-certificates-v1',**allcerts})
    here=Path(__file__).resolve().parent;src={x:hashlib.sha256((here/x).read_bytes()).hexdigest() for x in ['fresh_joint.py','fresh_endpoint.py','run_independent.py']}
    manifest={'schema':'n29-independent-d16-manifest-v1','date':'2026-09-08','scope':'n=29 Delta=16 at m=211 and m=210','summary':summary,'source_sha256':src,'evidence':{'states':states,'certificates':certs},'independence':'Fresh source imports no inherited verifier/model modules. Prepared input generation remains an explicit upstream dependency; charging-domain count, raw residual-profile count and projected survivor set are independently recomputed here. Joint propagation and endpoint LP/certificate checking are independently implemented.','status':'PASS; same-assistant independent implementation, not independent researcher reproduction or formal verification'}
    (a.output/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
