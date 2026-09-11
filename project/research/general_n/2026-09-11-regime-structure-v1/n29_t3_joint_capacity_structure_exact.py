#!/usr/bin/env python3
"""Exact joint (s,rho) capacity compression scan for the n=29,t=3 mask geometry.

The interaction statistic is the graph-derived HC3 source cap

  qcap(rho) = min(a-rho, #{i:s_i<=rho}).

For each regenerated profile we recompute all four exact rational template gaps,
then test whether increasingly informative summaries of qcap determine the full
validity mask.  No chosen assignment labels are used.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter,defaultdict
from pathlib import Path
import importlib.util,json


def load_module(path):
    spec=importlib.util.spec_from_file_location('cover',path)
    m=importlib.util.module_from_spec(spec);assert spec.loader is not None
    spec.loader.exec_module(m);return m

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def hist_tuple(xs):return tuple(sorted(Counter(xs).items()))
def pair_hist_tuple(xs):return tuple(sorted(Counter(xs).items()))

def record(i,p,names,gaps):
    s=p['s'];rho=p['rho'];a=len(s)
    nle={r:sum(x<=r for x in s) for r in set(rho)}
    qcaps=[min(a-r,nle[r]) for r in rho]
    raw=[nle[r] for r in rho]
    rq=[(r,min(a-r,nle[r])) for r in rho]
    mask=tuple(n for n in names if gaps[n][i]>0)
    z2=sum(r>=2 for r in rho);D1=s.count(1)
    return {
      'index':i,'mask':'+'.join(mask),'s_hist':hist_tuple(s),'rho_hist':hist_tuple(rho),
      'qcap_hist':hist_tuple(qcaps),'rho_qcap_hist':pair_hist_tuple(rq),
      'qsum':sum(qcaps),'raw_compat_sum':sum(raw),'h':h_res(rho),'J':2*z2-D1,
    }

def census(R,keyfn):
    d=defaultdict(Counter)
    for r in R:d[keyfn(r)][r['mask']]+=1
    mixed=[]
    for k,c in d.items():
        if len(c)>1:mixed.append((k,c))
    return {'occupied_cells':len(d),'mixed_cells':len(mixed),'profiles_in_mixed_cells':sum(sum(c.values()) for _,c in mixed)}

def first_collision(R,keyfn):
    d=defaultdict(list)
    for r in R:d[keyfn(r)].append(r)
    cand=[]
    for k,rs in d.items():
      rs=sorted(rs,key=lambda x:x['index'])
      for i in range(len(rs)):
       for j in range(i+1,len(rs)):
        if rs[i]['mask']!=rs[j]['mask']:
         cand.append((rs[i]['index'],rs[j]['index'],k,rs[i],rs[j]))
    if not cand:return None
    x=min(cand,key=lambda z:(z[1],z[0]))
    def enc(v):
      if isinstance(v,tuple):return [enc(z) for z in v]
      return v
    return {'key':enc(x[2]),'indices':[x[0],x[1]],'masks':[x[3]['mask'],x[4]['mask']]}

def main():
    ap=ArgumentParser();ap.add_argument('--cover-script',type=Path,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    m=load_module(z.cover_script);P=m.load(z.demands_json,z.rows)
    if len(P)!=94:raise SystemExit(f'expected 94, got {len(P)}')
    names=sorted(m.TEMPLATES);gaps={n:m.gaps_for(P,m.TEMPLATES[n]) for n in names}
    R=[record(i,p,names,gaps) for i,p in enumerate(P)]
    keys={
      'qsum':lambda r:(r['qsum'],),
      'raw_compat_sum':lambda r:(r['raw_compat_sum'],),
      'h_J_qsum':lambda r:(r['h'],r['J'],r['qsum']),
      'qcap_hist':lambda r:r['qcap_hist'],
      'rho_qcap_hist':lambda r:r['rho_qcap_hist'],
      's_hist_plus_qsum':lambda r:(r['s_hist'],r['qsum']),
      'rho_hist_plus_qsum':lambda r:(r['rho_hist'],r['qsum']),
      'h_J_plus_qcap_hist':lambda r:(r['h'],r['J'],r['qcap_hist']),
      's_hist_plus_qcap_hist':lambda r:(r['s_hist'],r['qcap_hist']),
      'rho_hist_plus_qcap_hist':lambda r:(r['rho_hist'],r['qcap_hist']),
      's_hist_plus_rho_qcap_hist':lambda r:(r['s_hist'],r['rho_qcap_hist']),
    }
    tests={}
    for name,kf in keys.items():tests[name]={'summary':census(R,kf),'first_collision':first_collision(R,kf)}
    # By direct inspection of the exact gap formula, the final key must be pure:
    # label envelopes depend only on s_hist; source envelopes only on (rho,qmax);
    # lambda*r is determined by rho_qcap_hist.
    assert tests['s_hist_plus_rho_qcap_hist']['summary']['mixed_cells']==0
    out={'schema':'n29-t3-joint-hc3-capacity-structure-exact-v1','status':'PASS','profiles':94,
         'definition':'qcap(rho)=min(a-rho,#{i:s_i<=rho}) (HC3 / exact checker qmax)',
         'tests':tests,
         'exact_sufficient_state':'(s_hist, multiset(rho,qcap(rho)))',
         'sufficiency_reason':'For each fixed scalar template, every label-envelope term is a function of s, every source-envelope term is a function of (rho,qmax), and the -lambda*sum(rho) term is determined by the same source-type multiset.',
         'records':[{'index':r['index'],'mask':r['mask'],'qsum':r['qsum'],'raw_compat_sum':r['raw_compat_sum'],'h':r['h'],'J':r['J'],'s_hist':[list(x) for x in r['s_hist']],'rho_hist':[list(x) for x in r['rho_hist']],'qcap_hist':[list(x) for x in r['qcap_hist']],'rho_qcap_hist':[[list(a),n] for a,n in r['rho_qcap_hist']]} for r in R]}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','tests':{k:v['summary'] for k,v in tests.items()},'first_collisions':{k:v['first_collision'] for k,v in tests.items()}},indent=2,sort_keys=True))
if __name__=='__main__':main()
