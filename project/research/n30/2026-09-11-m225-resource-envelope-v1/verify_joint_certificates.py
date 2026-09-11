#!/usr/bin/env python3
"""Standalone exact envelope acceptance, with no solver or discovery imports.

The 100-profile completeness theorem remains an external input. The checker
reconstructs its tail rows, evaluates every template on every tight row, and
compares two independently structured local-envelope calculations.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import argparse,json

HERE=Path(__file__).resolve().parent
PROFILE=HERE.parent/'2026-09-11-threshold-tail-v1/N30_M225_QGE18_PROFILES.txt'
A=13;B=16

def validate(T):
    assert set(T)=={'name','lambda','c','mu','tau','potential'}
    for x in (T['lambda'],T['c'],T['mu'],*T['tau'].values(),*T['potential'].values()):
        assert type(x) is int and x>=0
    assert all(1<=int(k)<=12 for k in T['tau'])
    assert T['potential']
    for f in T['potential']:
        if f in {'sv','sh2'}:continue
        if f.startswith('diag_'):
            assert 0<=int(f[5:])<=3
        else:
            _,D,V=f.split('_');assert f.startswith('bc_') and 1<=int(D)<=12 and 0<=int(V)<=16

def phi(T,s,d,v):
    assert s>=0 and d>=0 and v>=0
    z=0
    for f,w in T['potential'].items():
        if f=='sv':value=s*v
        elif f=='sh2':value=int(s>=2)
        elif f.startswith('diag_'):value=int(d+v>=B-int(f[5:]))
        else:
            _,D,V=f.split('_');value=int(d>=int(D) and v>=int(V))
        z+=w*value
    return z

def lval(T,s,R,x):
    return T['lambda']*R+T['c']*x+x*phi(T,s,R+s,B-R-x)

def sval(T,r,q,p):
    val=T['mu']*(q-p)-T['c']*q-q*phi(T,r,r+q-1,B-q-p)
    for j,w in T['tau'].items():
        j=int(j);val+=w*((q if q>=j+1 else 0)-(p if r+q>=j else 0))
    return val

def label_envelope(T,s,H):
    # Literal complete integer domain, R first.
    direct=[]
    for R in range(A-s):
        for x in range(s,min(B-R,H)+1):direct.append((lval(T,s,R,x),R,x))
    assert direct
    # For fixed x the function is linear in R between rectangle breakpoints.
    endpoints=[]
    for x in range(s,H+1):
        top=min(A-1-s,B-x)
        if top<0:continue
        candidates={0,top}
        for f in T['potential']:
            if f.startswith('bc_'):
                _,D,V=f.split('_');low=int(D)-s;high=B-int(V)-x
                candidates.update([low-1,low,high,high+1])
        for R in candidates:
            if 0<=R<=top:endpoints.append((lval(T,s,R,x),R,x))
    ell=min(v for v,R,x in direct)
    assert ell==min(v for v,R,x in endpoints)
    return ell,len(direct),len(endpoints)

def source_envelope(T,r,Q):
    direct=[(sval(T,r,q,p),q,p) for q in range(Q+1) for p in range(r+3)]
    endpoints=[]
    # For fixed q, the source expression is linear between these p jumps.
    for q in range(Q+1):
        candidates={0,r+2}
        for f in T['potential']:
            if f.startswith('diag_'):
                boundary=r+int(f[5:])-1;candidates.update([boundary,boundary+1])
            elif f.startswith('bc_'):
                _,D,V=f.split('_')
                if r+q-1>=int(D):
                    boundary=B-q-int(V);candidates.update([boundary,boundary+1])
        for p in candidates:
            if 0<=p<=r+2:endpoints.append((sval(T,r,q,p),q,p))
    sig=min(v for v,q,p in direct)
    assert sig==min(v for v,q,p in endpoints)
    return sig,len(direct),len(endpoints)

def reconstruct(path):
    profiles=[]
    for line in path.read_text().splitlines():
        if not line or line.startswith('#'):continue
        lhs,rhs=line.split('|');s=tuple(map(int,lhs.split()))
        assert len(s)==13 and s==tuple(sorted(s)) and 0<=min(s)<=max(s)<=12
        g=[]
        for h in range(2,14):
            W=sum(si for si in s if si>=h)
            if W==0:g.append(0);continue
            g.append(next(z for z in range(h,B+1) if 2*W<=z*(z-1)+h*(h+1)))
        Q=sum(s)-sum(g);assert Q==int(rhs.split('=')[1]) and 18<=Q<=21
        profiles.append((s,Q,tuple(g)))
    assert len(profiles)==100 and len({s for s,Q,g in profiles})==100
    rows=[]
    for s,Q,g in profiles:
        # Stars-and-bars reconstruction over twelve tail increments and lambda.
        def distribute(h,remaining,tail):
            if h==12:
                counts=[16-tail[0]]+[tail[i]-tail[i+1] for i in range(11)]+[tail[-1]]
                rho=tuple(r for r,n in enumerate(counts,1) for _ in range(n))
                assert len(rho)==16 and sum(s)==sum(rho)+2+remaining
                rows.append((s,rho,remaining));return
            for extra in range(remaining+1):
                z=g[h]+extra
                if z<=(tail[-1] if tail else 16):distribute(h+1,remaining-extra,tail+(z,))
        distribute(0,Q-18,())
    assert len(rows)==272 and len(set(rows))==272
    assert sum(lam>0 for s,rho,lam in rows)==61
    assert all(min(s)>0 for s,rho,lam in rows if lam>0)
    tight=sorted((s,rho) for s,rho,lam in rows if lam==0)
    assert len(tight)==211 and sum(min(s)>0 for s,rho in tight)==207
    return tight

def short(v):return ','.join(str(k) if n==1 else f'{k}^{n}' for k,n in sorted(Counter(v).items()))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--certificates',type=Path,default=HERE/'JOINT_CERTIFICATES.json');ap.add_argument('--profiles',type=Path,default=PROFILE);ap.add_argument('--output',type=Path);ap.add_argument('--appendix',type=Path);ap.add_argument('--allow-partial',action='store_true');args=ap.parse_args()
    data=json.loads(args.certificates.read_text());assert (data['a'],data['b'],data['t'],data['dmax'])==(13,16,1,12)
    Ts=data['templates'];assert Ts and len({T['name'] for T in Ts})==len(Ts)
    for T in Ts:validate(T)
    rows=reconstruct(args.profiles);labels={};sources={};direct_count=0;endpoint_count=0
    records=[];assigned=Counter();coverage=Counter();uncovered=[]
    appendix=['# Exact joint-envelope appendix','',
      'Each positive gap is sum(n_s * ell_s) + sum(n_rho * sigma_rho) - lambda*r. Every template is evaluated on every tight row before the first successful one is assigned.','',
      '| Template | Demand s | Residual rho | Label minima ell_s | Source minima sigma_rho | Positive gap |',
      '|---|---|---|---|---|---:|']
    for s,rho in rows:
        results=[]
        for T in Ts:
            ell={};sig={}
            for si in sorted(set(s)):
                H=sum(r>=si for r in rho);key=(T['name'],si,H)
                if key not in labels:
                    value,n1,n2=label_envelope(T,si,H);labels[key]=value;direct_count+=n1;endpoint_count+=n2
                ell[si]=labels[key]
            for r in sorted(set(rho)):
                Q=min(A-r,sum(si<=r for si in s));key=(T['name'],r,Q)
                if key not in sources:
                    value,n1,n2=source_envelope(T,r,Q);sources[key]=value;direct_count+=n1;endpoint_count+=n2
                sig[r]=sources[key]
            gap=sum(n*ell[si] for si,n in Counter(s).items())+sum(n*sig[r] for r,n in Counter(rho).items())-T['lambda']*sum(rho)
            results.append({'template':T['name'],'gap':gap,'ell':ell,'sigma':sig})
            if gap>0:coverage[T['name']]+=1
        good=[x for x in results if x['gap']>0]
        if good:
            chosen=good[0];assigned[chosen['template']]+=1
            appendix.append(f"| {chosen['template']} | ({short(s)}) | ({short(rho)}) | {chosen['ell']} | {chosen['sigma']} | {chosen['gap']} |")
        else:chosen=None;uncovered.append({'s':s,'rho':rho})
        records.append({'s':s,'rho':rho,'assigned':None if chosen is None else chosen['template'],'template_gaps':{x['template']:x['gap'] for x in results},'chosen_envelopes':chosen})
    # Independently check product-order monotonicity across the entire state box.
    monotone=0
    for T in Ts:
        for s in range(14):
            for d in range(13):
                for v in range(17):
                    base=phi(T,s,d,v)
                    for ss,dd,vv in [(s+1,d,v),(s,d+1,v),(s,d,v+1)]:
                        assert phi(T,ss,dd,vv)>=base;monotone+=1
    out={'schema':'n30-joint-envelope-audit-v1','status':'PASS' if not uncovered else 'PARTIAL',
         'solver_used':False,'floating_point_used':False,'discovery_imported':False,
         'profile_completeness_is_input':True,'dmax':12,'isolated_C_degree_bound_used':False,
         'profile_sha256':sha256(args.profiles.read_bytes()).hexdigest(),'certificate_sha256':sha256(args.certificates.read_bytes()).hexdigest(),
         'tight_rows':211,'template_count':len(Ts),'covered':len(rows)-len(uncovered),'uncovered':uncovered,
         'assigned_counts':dict(assigned),'full_frontier_template_coverage':dict(coverage),
         'minimum_assigned_gap':min(r['chosen_envelopes']['gap'] for r in records if r['assigned']),
         'direct_integer_state_checks':direct_count,'endpoint_integer_state_checks':endpoint_count,
         'product_order_checks':monotone,'rows':records}
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    if args.appendix:args.appendix.write_text('\n'.join(appendix)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'rows','uncovered'}},indent=2))
    if uncovered:
        print('uncovered',json.dumps(uncovered))
        if not args.allow_partial:raise SystemExit('Incomplete envelope cover; no full endpoint acceptance')

if __name__=='__main__':main()
