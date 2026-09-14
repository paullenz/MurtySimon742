#!/usr/bin/env python3
"""Exact source-priced charge envelope and targeted boundary-profile reconnaissance.

The price inequality is algebraic: exact row sums are restored after subtracting
a source price from every selected incidence. The finite price search is only a
certificate finder; failure to find a price is retained as a non-rejection.
"""
from __future__ import annotations
import argparse, importlib.util, json
from itertools import product
from pathlib import Path

ORIGINAL_ROWS=[108,160,338,347,471,586]
FRESH_ROWS=[20,91,391,490,528,562,677]

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def normalize_prices(prices):
    if not prices:return ()
    m=min(prices)
    return tuple(int(x-m) for x in prices)

def priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,prices):
    """Safe integer upper bound. Returns (value,row_usage_witness) or None."""
    assert len(q)==len(rho)==len(P)==len(alpha)==len(prices)
    assert min(alpha,default=0)>=0 and charge_eta>=0
    ss=sorted(s);E=sum(q)-sum(ss);n_low=sum(d<=eta for d in ss)
    if E<0 or not 0<=e_low<=E:return None
    if n_low==0 and e_low!=0:return None
    if n_low==len(ss) and e_low!=E:return None
    limits=[sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in ss]
    if min(limits,default=0)<0:return None
    floors={}
    for t in set(ss):
        n=sum(d<=t for d in ss)
        spill=sum(max(0,qq-sum(t<d<=r for d in ss)) for qq,r in zip(q,rho))
        floors[n]=max(0,spill-sum(d for d in ss if d<=t))
    ceilings=[max(0,pp-r+1) for pp,r in zip(P,rho)]
    b=len(q);zero=(0,)*b
    best={0:(0,zero)}
    for i,(d,h) in enumerate(zip(ss,limits),1):
        opts=[]
        for e in range(min(h,E)+1):
            vals=[]
            for u,(qq,r,al,D,lam) in enumerate(zip(q,rho,alpha,ceilings,prices)):
                if qq<=0 or r<d:continue
                w=al*min(e,D) if d>charge_eta else 0
                vals.append((w-lam,u))
            vals.sort(key=lambda z:(z[0],-z[1]),reverse=True)
            k=d+e
            if k>len(vals):continue
            chosen=tuple(u for _,u in vals[:k])
            score=sum(v for v,_ in vals[:k])
            use=[0]*b
            for u in chosen:use[u]=1
            opts.append((e,score,tuple(use)))
        nxt={}
        for used,(value,usage) in best.items():
            for e,score,use in opts:
                total=used+e
                if total>E or total<floors.get(i,0):continue
                if i<n_low and total>e_low:continue
                if i==n_low and total!=e_low:continue
                usage2=tuple(x+y for x,y in zip(usage,use))
                value2=value+score
                old=nxt.get(total)
                key=(value2,sum((usage2[u]-q[u])**2 for u in range(b)),usage2)
                if old is None:
                    nxt[total]=(value2,usage2)
                else:
                    oldkey=(old[0],sum((old[1][u]-q[u])**2 for u in range(b)),old[1])
                    if key>oldkey:nxt[total]=(value2,usage2)
        best=nxt
    if E not in best:return None
    adjusted,usage=best[E]
    return sum(lam*qq for lam,qq in zip(prices,q))+adjusted,usage

def search_prices(s,q,rho,P,eta,e_low,charge_eta,alpha,max_rounds=6):
    D=[max(0,pp-r+1) for pp,r in zip(P,rho)]
    seeds=[(0,)*len(q),normalize_prices(D),normalize_prices([al*d for al,d in zip(alpha,D)])]
    cache={}
    def ev(p):
        p=normalize_prices(p)
        if p not in cache:cache[p]=priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,p)
        return cache[p]
    best=None
    for seed in seeds:
        p=normalize_prices(seed)
        for step,rounds in ((4,2),(2,3),(1,max_rounds)):
            if best is not None and step==1:p=tuple(best['prices'])
            seen=set()
            for _ in range(rounds):
                if p in seen:break
                seen.add(p)
                got=ev(p)
                if got is None:return dict(upper=None,prices=list(p),usage=None,evaluations=len(cache),empty=True)
                val,usage=got
                rec=dict(upper=val,prices=list(p),usage=list(usage),evaluations=len(cache),empty=False)
                if best is None or (val,sum(p),p)<(best['upper'],sum(best['prices']),tuple(best['prices'])):best=rec
                delta=[usage[u]-q[u] for u in range(len(q))]
                if not any(delta):break
                p=normalize_prices([p[u]+step*delta[u] for u in range(len(q))])
    assert best is not None
    p=tuple(best['prices']);usage=best['usage']
    order=sorted(range(len(q)),key=lambda u:abs(usage[u]-q[u]),reverse=True)[:4]
    for u in order:
        for direction in (-1,1):
            cand=list(p);cand[u]+=direction;cand=normalize_prices(cand)
            got=ev(cand)
            if got is None:continue
            val,use=got
            if val<best['upper']:
                best=dict(upper=val,prices=list(cand),usage=list(use),evaluations=len(cache),empty=False);p=tuple(cand)
    best['evaluations']=len(cache)
    return best

def coordinate_refine(s,q,rho,P,eta,e_low,charge_eta,alpha,start,limit_sweeps=8):
    p=normalize_prices(start);got=priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,p)
    if got is None:return dict(upper=None,prices=list(p),usage=None,evaluations=1,empty=True)
    bestv,bestuse=got;evals=1
    for _ in range(limit_sweeps):
        move=None
        for u in range(len(q)):
            for direction in (-1,1):
                cand=list(p);cand[u]+=direction;cand=normalize_prices(cand)
                g=priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,cand);evals+=1
                if g is None:continue
                val,use=g
                if val<bestv and (move is None or (val,sum(cand),cand)<(move[0],sum(move[1]),move[1])):move=(val,list(cand),use)
        if move is None:break
        bestv,p,bestuse=move[0],tuple(move[1]),move[2]
    return dict(upper=bestv,prices=list(p),usage=list(bestuse),evaluations=evals,empty=False)

def base_caps(p,prior):
    s,q,rho=p['s'],p['q'],p['rho'];old=prior.old_caps(p['a'],s,q,rho);assert old==p['P']
    return prior.spill_caps(s,q,rho,prior.prior_localized(s,q,rho,old))

def classify_inherited(p,eta,e_low,P,cond,block,shared):
    s,q,rho=p['s'],p['q'],p['rho'];pc=cond.conditional_caps(s,q,rho,P,eta,e_low)
    if pc is None:return True,'infeasible_split',None
    if sum(pc)<sum(q):return True,'total_capacity',pc
    for ce in sorted({0,eta}):
        for weighted,alpha in [(False,[1]*len(q)),(True,[1 if qq<=2 else 3 for qq in q])]:
            upper=cond.conditional_upper(s,q,rho,pc,eta,e_low,ce,alpha)
            if upper is None:return True,'empty_conditioned_projection',pc
            low=block.best_lower(q,rho,s,pc,ce,alpha)
            if low['lower']>upper:return True,'conditioned_price',pc
    data=shared.block_options(s,q,rho,pc,{i for i,d in enumerate(s) if d<=eta},e_low)
    if data is None:return True,'shared_infeasible_block',pc
    cert=shared.best_shared(q,rho,pc,*data)
    if cert['kind']!='shared_slack' or cert.get('gap',0)>0:return True,'shared_slack',pc
    return False,'unrejected',pc

def best_source_certificate(p,eta,e_low,pc,block,cond):
    s,q,rho=p['s'],p['q'],p['rho'];candidates=[]
    for ce in sorted({0,eta}):
        for weighted,alpha in [(False,[1]*len(q)),(True,[1 if qq<=2 else 3 for qq in q])]:
            low=block.best_lower(q,rho,s,pc,ce,alpha);old=cond.conditional_upper(s,q,rho,pc,eta,e_low,ce,alpha);assert old is not None
            candidates.append((low['lower']-old,ce,weighted,alpha,low,old))
    candidates.sort(key=lambda x:x[0],reverse=True);best=None
    for oldgap,ce,weighted,alpha,low,old in candidates[:2]:
        search=search_prices(s,q,rho,pc,eta,e_low,ce,alpha);upper=search['upper'];gap=(10**18 if upper is None else low['lower']-upper)
        if upper is not None and low['lower']>0 and gap>=-5:
            refined=coordinate_refine(s,q,rho,pc,eta,e_low,ce,alpha,search['prices'])
            if refined['upper'] is None or refined['upper']<upper:
                refined['initial_evaluations']=search['evaluations'];search=refined;upper=search['upper'];gap=(10**18 if upper is None else low['lower']-upper)
        rec=dict(e_low=e_low,charge_eta=ce,weighted=weighted,zero_price_upper=old,zero_price_gap=oldgap,lower=low['lower'],tau=low['tau'],theta=low['theta'],gap=gap,search=search)
        if best is None or gap>best['gap']:best=rec
    return best

def scan_profile(p,prior,cond,block,shared):
    s,q,rho=p['s'],p['q'],p['rho'];E=p['Esel'];P=base_caps(p,prior);candidates=[]
    for eta in sorted(set(s))[:-1]:
        M=sum(max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho));SL=sum(d for d in s if d<=eta);lo=max(0,M-SL)
        branches=[];survivors=[]
        for e_low in range(lo,E+1):
            rejected,reason,pc=classify_inherited(p,eta,e_low,P,cond,block,shared);branches.append(dict(e_low=e_low,rejected=rejected,reason=reason))
            if not rejected:survivors.append((e_low,pc))
        candidates.append((len(survivors),eta,lo,branches,survivors))
    count,eta,lo,branches,survivors=min(candidates,key=lambda x:(x[0],x[1]));assert survivors,('profile was already closed before source pricing',p['row'],eta)
    certs=[];remaining=[]
    for e_low,pc in survivors:
        cert=best_source_certificate(p,eta,e_low,pc,block,cond);certs.append(cert)
        if cert['gap']<=0:remaining.append(e_low)
    return dict(row=p['row'],target_eta=eta,admissible_range=[lo,E],inherited_rejected=len(branches)-len(survivors),inherited_reasons={r['reason']:sum(x['reason']==r['reason'] for x in branches) for r in branches},source_price_tested=len(survivors),source_price_rejected=sum(c['gap']>0 for c in certs),remaining=remaining,excluded=not remaining,certificates=certs,scope='target eta chosen by fewest inherited non-rejections; finite integer price search, not exhaustive over all prices/etas')

def strict_fixture(cond):
    s=[1,1];q=[1,1,1,1];rho=[1,1,1,1];P=[0,0,0,1];eta=e_low=charge_eta=0;alpha=[1,1,1,1]
    zero=priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,[0,0,0,0]);priced=priced_upper(s,q,rho,P,eta,e_low,charge_eta,alpha,[0,0,0,1]);old=cond.conditional_upper(s,q,rho,P,eta,e_low,charge_eta,alpha)
    assert zero[0]==old==2 and priced[0]==1
    return dict(zero_price=zero[0],source_price=priced[0],prices=[0,0,0,1],explanation='zero-price relaxation can reuse source 3 on both high-charge labels; its exact row sum is one')

def incidence_audit(cond):
    configs=checks=strict=0
    for a in range(1,4):
        for b in range(1,4):
            for masks in product(range(1<<a),repeat=b):
                X=[[(mask>>i)&1 for i in range(a)] for mask in masks];q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
                for s0 in product(*(range(xx+1) for xx in x)):
                    s=list(s0);ranges=[range(max([1]+[s[i] for i in range(a) if X[u][i]]),a-q[u]+1) for u in range(b)]
                    for rr in product(*ranges):
                        rho=list(rr);configs+=1;ev=[xx-d for xx,d in zip(x,s)];D=[(2*u+sum(s)+q[u])%5 for u in range(b)];P=[r-1+d for r,d in zip(rho,D)];prices=normalize_prices([(3*u+sum(q)+sum(s))%7 for u in range(b)]);alpha=[1+u%3 for u in range(b)]
                        for eta in sorted({0,*s}):
                            e_low=sum(e for e,d in zip(ev,s) if d<=eta)
                            for ce in sorted({0,eta}):
                                got=priced_upper(s,q,rho,P,eta,e_low,ce,alpha,prices);zero=priced_upper(s,q,rho,P,eta,e_low,ce,alpha,[0]*b);old=cond.conditional_upper(s,q,rho,P,eta,e_low,ce,alpha)
                                assert got is not None and zero is not None and zero[0]==old
                                actual=sum(alpha[u]*min(ev[i],D[u]) for i,d in enumerate(s) if d>ce for u in range(b) if X[u][i]);assert actual<=got[0],(s,q,rho,eta,ce,prices,actual,got)
                                strict+=got[0]<zero[0];checks+=1
    return dict(configurations=configs,priced_inequalities=checks,strict_vs_zero_price=strict)

def main():
    if not __debug__:raise SystemExit('Assertions disabled: do not run with -O')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path);args=ap.parse_args();base=Path(__file__).resolve().parents[1]
    prior=load_module(base/'2026-09-14-capped-spill-v1/verify_capped_spill.py','source_price_prior');block=load_module(base/'2026-09-14-block-pressure-v1/verify_block_pressure.py','source_price_block');cond=load_module(base/'2026-09-14-conditioned-excess-v1/verify_conditioned_excess.py','source_price_cond');shared=load_module(base/'2026-09-14-joint-blocks-v1/verify_shared_slack.py','source_price_shared')
    original=json.loads((base/'2026-09-14-block-pressure-v1/REMAINDER_12.json').read_text())['rows'];fresh=json.loads((base/'2026-09-14-joint-blocks-v1/FRESH_RECHECK_FULL.json').read_text())['unrejected'];orig=[p for p in original if p['row'] in ORIGINAL_ROWS];freshp=[p for p in fresh if p['row'] in FRESH_ROWS]
    assert [p['row'] for p in orig]==ORIGINAL_ROWS and [p['row'] for p in freshp]==FRESH_ROWS
    audit=incidence_audit(cond);fixture=strict_fixture(cond);original_reports=[scan_profile(p,prior,cond,block,shared) for p in orig];fresh_reports=[scan_profile(p,prior,cond,block,shared) for p in freshp]
    result=dict(schema='source-priced-row-budget-v1',external_review='OPEN',theorem_scope='exact row sums restored by arbitrary integer source prices; finite price search only finds certificates',audit=audit,strict_fixture=fixture,original=original_reports,fresh=fresh_reports,newly_excluded_original=[r['row'] for r in original_reports if r['excluded']],newly_excluded_fresh=[r['row'] for r in fresh_reports if r['excluded']],canonical_frontier_changed=False,relational_candidates_promoted=False)
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:args.out.write_text(text)
    summary={k:result[k] for k in ('schema','newly_excluded_original','newly_excluded_fresh','canonical_frontier_changed','relational_candidates_promoted')};summary['audit']=audit;summary['strict_fixture']=fixture;print(json.dumps(summary,sort_keys=True,indent=2))
if __name__=='__main__':main()
