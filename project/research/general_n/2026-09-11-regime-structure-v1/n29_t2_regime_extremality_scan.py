#!/usr/bin/env python3
"""Test whether the exact n=29,t=2 minimum-gap regime witnesses are order-extremal.

For each unit-demand regime nu1=0,1,2, recompute the exact assigned-template
certificate gaps and select the true minimum-gap profile(s) in that regime.
Then compare every profile in the regime against the first minimum-gap witness
under several transparent partial orders:

  * componentwise order on sorted s and rho vectors;
  * ascending/descending prefix-sum majorization;
  * threshold tail-count and tail-excess coordinates.

The pairwise-incompatibility witnesses are reported separately; they are not
silently substituted for the minimum-gap witnesses.

This is an exploratory structural diagnostic. Any universal order reported is
checked exhaustively over the 902 regenerated finite frontier profiles; it is
not a general-N theorem.
"""
from pathlib import Path
import argparse, importlib.util, json

ASSIGNMENT={0:'T2',1:'T1',2:'T0'}
INCOMPATIBILITY_WITNESS={0:77,1:3,2:0}

def loadmod(path:Path):
    sp=importlib.util.spec_from_file_location('t2exact',path)
    m=importlib.util.module_from_spec(sp); assert sp.loader is not None
    sp.loader.exec_module(m); return m

def cmpvec(a,b):
    return {
      'all_le':all(x<=y for x,y in zip(a,b)),
      'all_ge':all(x>=y for x,y in zip(a,b)),
      'equal':a==b,
    }

def prefix(v):
    z=[];s=0
    for x in v:s+=x;z.append(s)
    return z

def rat(x):return [x.numerator,x.denominator]

def sig(pf):
    s=sorted(pf['s']);r=sorted(pf['rho'])
    sd=sorted(s,reverse=True);rd=sorted(r,reverse=True)
    out={'s_asc':s,'rho_asc':r,'s_desc':sd,'rho_desc':rd,
         's_asc_prefix':prefix(s),'rho_asc_prefix':prefix(r),
         's_desc_prefix':prefix(sd),'rho_desc_prefix':prefix(rd)}
    for k in range(1,11):
        out[f's_ge_{k}']=sum(x>=k for x in s)
        out[f'r_ge_{k}']=sum(x>=k for x in r)
        out[f's_excess_{k}']=sum(max(x-k,0) for x in s)
        out[f'r_excess_{k}']=sum(max(x-k,0) for x in r)
    return out

def compare_regime(P,ids,wid):
    w=sig(P[wid])
    vec_keys=['s_asc','rho_asc','s_desc','rho_desc','s_asc_prefix','rho_asc_prefix','s_desc_prefix','rho_desc_prefix']
    vec_summary={}
    for key in vec_keys:
        all_le=[];all_ge=[];bad_le=[];bad_ge=[]
        for i in ids:
            c=cmpvec(sig(P[i])[key],w[key]);all_le.append(c['all_le']);all_ge.append(c['all_ge'])
            if not c['all_le'] and len(bad_le)<5:bad_le.append(i)
            if not c['all_ge'] and len(bad_ge)<5:bad_ge.append(i)
        vec_summary[key]={'profile_le_witness_all':all(all_le),'profile_ge_witness_all':all(all_ge),
                          'counterexamples_to_le':bad_le,'counterexamples_to_ge':bad_ge}
    scalar_summary={}
    for key in [k for k in w if k.startswith(('s_ge_','r_ge_','s_excess_','r_excess_'))]:
        vs=[sig(P[i])[key] for i in ids];wv=w[key]
        scalar_summary[key]={'witness':wv,'min':min(vs),'max':max(vs),
                             'witness_is_min':wv==min(vs),'witness_is_max':wv==max(vs)}
    extremal=[{'coordinate':k,**v} for k,v in scalar_summary.items() if v['witness_is_min'] or v['witness_is_max']]
    return {'witness_index':wid,'witness_demand_id':P[wid]['demand_id'],
            'witness_s':P[wid]['s'],'witness_rho':P[wid]['rho'],
            'vector_orders':vec_summary,'extremal_scalar_coordinates':extremal}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--exact-script',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args(); ex=loadmod(z.exact_script);P=ex.load(z.demands_json,z.rows)
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    gaps={name:ex.gaps(P,th) for name,th in ex.TEMPLATES.items()}
    results={}
    for nu1,tname in ASSIGNMENT.items():
        ids=[i for i,p in enumerate(P) if p['s'].count(1)==nu1]
        mg=min(gaps[tname][i] for i in ids)
        mids=[i for i in ids if gaps[tname][i]==mg]
        wid=mids[0]
        inc=INCOMPATIBILITY_WITNESS[nu1]
        if inc not in ids:raise SystemExit(f'incompatibility witness {inc} not in nu1={nu1}')
        results[str(nu1)]={
          'profiles':len(ids),'assigned_template':tname,
          'minimum_assigned_gap':rat(mg),'minimum_gap_indices':mids,
          'minimum_gap_extremality':compare_regime(P,ids,wid),
          'incompatibility_witness':{
             'index':inc,'demand_id':P[inc]['demand_id'],'gap_under_assigned_template':rat(gaps[tname][inc]),
             's':P[inc]['s'],'rho':P[inc]['rho']
          }
        }
    out={'schema':'n29-t2-regime-extremality-scan-v2','status':'PASS','profiles':len(P),'regimes':results,
         'interpretation':'Finite structural diagnostic. Minimum-gap witnesses are recomputed exactly from the assigned rational templates; incompatibility witnesses are reported separately. Universal order relations are exhaustive only over the regenerated 902-profile frontier.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
