#!/usr/bin/env python3
"""Exact replay of the supplement-cap fixed point via threshold recursion.

For each regenerated n=29,t=2 frontier row, let c_u be the initial source cap

    c_u = min(12-rho_u, #{i:s_i <= rho_u}).

The audited refinement iterates the monotone map

    F_u(q) = max { k <= c_u : #{w != u : rho_w+q_w >= k-1} >= k }.

At a fixed point q, define H_j = #{w : rho_w+q_w >= j}.  Because rho_u>=1,
for every k>=1 one has the exact threshold equivalence

    q_u >= k  <=>  c_u >= k and H_{k-1} >= k+1.

Moreover H_{k-1} only depends on threshold predicates q_w>=h with h<=k-2,
so the fixed point can be reconstructed in ascending k without iteration.

This script verifies the ascending reconstruction against the original iterative
map for all 902 regenerated frontier profiles and records finite structural
statistics by nu1=#{i:s_i=1}.  The equivalence itself is elementary and does
not depend on n=29; the exhaustive replay is a regression check, not its proof.
"""
from pathlib import Path
from collections import Counter,defaultdict
import argparse,json


def load(demands_json:Path,rows:Path):
    D=json.loads(demands_json.read_text());out=[]
    for line in rows.read_text().splitlines():
        if not line.strip():continue
        z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+4:
            out.append({'demand_id':did,'s':s,'rho':rho})
    return out


def initial_caps(s,rho):
    return [min(12-r,sum(x<=r for x in s)) for r in rho]


def refine_iterative(rho,init):
    cap=list(init)
    while True:
        nxt=[]
        for u in range(len(rho)):
            best=0
            for k in range(1,cap[u]+1):
                supporters=sum(w!=u and rho[w]+cap[w]>=k-1 for w in range(len(rho)))
                if supporters>=k:best=k
            nxt.append(best)
        if nxt==cap:return cap
        cap=nxt


def refine_threshold(rho,init):
    # ge[k][u] means final q_u >= k. ge[0] is identically true.
    K=max(init,default=0)
    ge=[[True]*len(rho)]
    H=[];gate=[]
    for k in range(1,K+1):
        hk=0
        for u,r in enumerate(rho):
            need=k-1-r
            if need<=0 or ge[need][u]:hk+=1
        H.append(hk)
        g=(hk>=k+1);gate.append(g)
        ge.append([init[u]>=k and g for u in range(len(rho))])
    q=[]
    for u in range(len(rho)):
        q.append(max((k for k in range(1,K+1) if ge[k][u]),default=0))
    return q,H,gate


def hall_margins(s,rho,cap):
    ans=[]
    for k in range(1,13):
        top=s[12-k:]
        need=sum(top);supply=0
        for u,r in enumerate(rho):
            elig=sum(x<=r for x in top)
            supply+=min(cap[u],elig)
        ans.append(supply-need)
    return ans


def threshold_stats(rho,q):
    H={str(j):sum(r+qq>=j for r,qq in zip(rho,q)) for j in range(0,13)}
    Q={str(k):sum(qq>=k for qq in q) for k in range(1,12)}
    return H,Q


def range_summary(vals,witness):
    lo=min(vals);hi=max(vals)
    return {'min':lo,'max':hi,'witness':witness,'witness_is_min':witness==lo,'witness_is_max':witness==hi}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=load(z.demands_json,z.rows)
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    true_min={0:136,1:39,2:0}
    records=[];bad=[]
    for i,p in enumerate(P):
        init=initial_caps(p['s'],p['rho'])
        qi=refine_iterative(p['rho'],init)
        qr,Hrec,gates=refine_threshold(p['rho'],init)
        if qi!=qr:bad.append({'index':i,'kind':'fixed_point_mismatch','iterative':qi,'threshold':qr})
        H,Q=threshold_stats(p['rho'],qi)
        hm=hall_margins(p['s'],p['rho'],qi)
        records.append({'index':i,'nu1':p['s'].count(1),'init':init,'q':qi,'H':H,'Q':Q,'gates':gates,'hall_margins':hm})
    groups={}
    for nu1 in (0,1,2):
        ids=[r for r in records if r['nu1']==nu1];w=records[true_min[nu1]]
        sig=Counter(tuple(r['gates']) for r in ids)
        groups[str(nu1)]={
          'profiles':len(ids),
          'gate_signature_count':len(sig),
          'gate_signature_census':[{'signature':[int(x) for x in k],'count':v} for k,v in sorted(sig.items(),key=lambda kv:(-kv[1],kv[0]))],
          'minimum_gap_witness_index':w['index'],
          'minimum_gap_witness':{
             'initial_cap_histogram':dict(sorted(Counter(w['init']).items())),
             'refined_cap_histogram':dict(sorted(Counter(w['q']).items())),
             'H':w['H'],'Q':w['Q'],'gate_signature':[int(x) for x in w['gates']],
             'hall_margins':w['hall_margins'],
          },
          'H_ranges':{str(j):range_summary([r['H'][str(j)] for r in ids],w['H'][str(j)]) for j in range(13)},
          'Q_ranges':{str(k):range_summary([r['Q'][str(k)] for r in ids],w['Q'][str(k)]) for k in range(1,12)},
          'hall_margin_ranges':{str(k):range_summary([r['hall_margins'][k-1] for r in ids],w['hall_margins'][k-1]) for k in range(1,13)},
        }
    out={
      'schema':'n29-t2-supplement-threshold-replay-v1',
      'status':'PASS' if not bad else 'FAIL','profiles':len(P),'mismatches':bad,
      'fixed_point_identity':'q_u>=k iff initial_cap_u>=k and H_{k-1}>=k+1, H_j=#{w:rho_w+q_w>=j}',
      'ascending_reason':'rho_w>=1 implies H_{k-1} only asks q_w>=k-1-rho_w <= k-2, so lower threshold levels suffice.',
      'groups':groups,
      'interpretation':'The audited supplement-cap fixed point is reproduced exactly by the ascending threshold recursion on every regenerated n29,t2 frontier profile. Group statistics are finite diagnostics only.',
    }
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if bad:raise SystemExit(1)

if __name__=='__main__':main()
