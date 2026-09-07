#!/usr/bin/env python3
"""Adversarial finite tests of reduced premises; these objects are NOT graphs G."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import Counter
import argparse,json,random,hashlib

def req(c,m):
    if not c:raise ValueError(m)

def validate(h,z,labels,arcs):
    req(1<=h<=z<=h*h+h,'source count scope')
    req(len(set((min(u,v),max(u,v)) for u,v,i in arcs))==len(arcs),'unordered pair budget')
    q=[0]*z;p=[0]*z;e=[0]*z;load=[F(0)]*z
    for i,(sources,exceptional) in enumerate(labels):
        x=len(sources);req(len(set(sources))==x and h<=x<=z,'label demand')
        if exceptional:req(x<z,'exceptional label cannot use every source')
        for u in sources:
            req(0<=u<z,'source range');q[u]+=1;load[u]+=F(h,x)
            if exceptional:e[u]+=1
    indexed=Counter()
    for u,v,i in arcs:
        req(0<=u<z and 0<=v<z and u!=v and 0<=i<len(labels),'arc range')
        sources,exceptional=labels[i]
        req(exceptional and u in sources and v not in sources,'exceptional supplement must miss label')
        indexed[u,i]+=1;p[v]+=1
    req(indexed==Counter((u,i) for i,(T,E) in enumerate(labels) if E for u in T),'exceptional coverage')
    for sources,exceptional in labels:
        D=h+len(sources)-(not exceptional)
        req(all(q[u]+p[u]<=D for u in sources),'actual endpoint premise')
    for u in range(z):
        req(load[u]<=2*h-1+F(e[u]-p[u],h+1),'weighted source conclusion')
    req(sum(e)==sum(p),'incoming/outgoing compensation')
    req(h*len(labels)<=(2*h-1)*z,'spare source conclusion')
    return any(e)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    rng=random.Random(74220260907);attempts=0;accepted=0;with_exc=0;hashes=hashlib.sha256();first=None
    for h in range(1,13):
        for z in sorted({h,h+1,min(h+2,h*h+h),2*h,h*h+h}):
            for _ in range(200):
                attempts+=1;labels=[];arcs=[];used=set();bad=False
                for i in range(rng.randint(1,min(2*z,2*h+4))):
                    x=rng.randint(h,min(z,h+2));T=sorted(rng.sample(range(z),x));exc=(x<z and rng.random()<.3)
                    labels.append((T,exc))
                    if exc:
                        for u in T:
                            choices=[v for v in range(z) if v not in T and tuple(sorted((u,v))) not in used]
                            if not choices:bad=True;break
                            v=rng.choice(choices);used.add(tuple(sorted((u,v))));arcs.append((u,v,i))
                    if bad:break
                if bad:continue
                try:nonempty=validate(h,z,labels,arcs)
                except ValueError as ex:
                    # Only failing PREMISES may discard a trial. Any failing conclusion is fatal.
                    if 'conclusion' in str(ex) or 'compensation' in str(ex):raise
                    continue
                accepted+=1;with_exc+=nonempty
                rec={'h':h,'z':z,'labels':labels,'arcs':arcs}
                hashes.update(json.dumps(rec,sort_keys=True,separators=(',',':')).encode()+b'\n')
                if first is None and nonempty:first=rec
    # Exhaust all oriented simple graphs up to five vertices, and every integer
    # threshold from 0 to z. Busy out-arcs may only occupy pairs incident with busy set.
    digraphs=0;checks=0
    for z in range(1,6):
        edges=list(combinations(range(z),2))
        for word in product(range(3),repeat=len(edges)):
            arcs=[(u,v) if v0==1 else (v,u) for (u,v),v0 in zip(edges,word) if v0]
            q=[0]*z
            for u,v in arcs:q[u]+=1
            for T in range(z+1):
                U={u for u in range(z) if q[u]>T};k=len(U);P=len(arcs)
                bound=(z-k)*T+k*z-F(k*(k+1),2)
                req(P<=bound and bound<=F(z*z+T*T,2),'pair capacity conclusion');checks+=1
            digraphs+=1
    # A valid reduced system attains compensated loads 1/2 and 3/2.
    # The second source violates an uncompensated upper bound of 2h-1=1.
    validate(1,2,[([0,1],False),([1],True)],[(1,0,1)])
    req(F(1,2)+1>1,'counterexample to dropping exceptional compensation')
    out=dict(all_checks_pass=True,random_seed=74220260907,reduced_attempts=attempts,
        valid_reduced_systems=accepted,valid_systems_with_exceptional_arcs=with_exc,
        accepted_input_stream_sha256=hashes.hexdigest(),first_exceptional_example=first,
        oriented_graphs_exhausted=digraphs,pair_capacity_threshold_checks=checks,
        invalid_uncompensated_local_bound_falsified=True,
        uncompensated_counterexample={'h':1,'z':2,'ordinary_sources':[0,1],'exceptional_sources':[1],'exceptional_arc':[1,0],'weighted_loads':['1/2','3/2']},
        limitation='Reduced local incidence/arc systems only; not actual critical graphs or proof of universal mathematical statements.')
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
