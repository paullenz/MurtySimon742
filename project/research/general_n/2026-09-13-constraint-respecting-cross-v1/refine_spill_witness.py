#!/usr/bin/env python3
"""Deepen the positive-witness search only on pass-1 unresolved states.

The goal remains constructive: find a directly checkable exact-demand selected
pattern, q vector and p vector satisfying the transport and spill conditions.
Failure to find one is explicitly *not* an exclusion.
"""
from collections import Counter
from pathlib import Path
import json
import math
import random
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

sys.path.insert(0, str(HERE))
from full_domain_spill_witness import greedy_p, spill_details, check_witness  # noqa: E402


def survivors_by_key():
    rows = json.loads(read_bytes("survivors.json"))
    return {(r["layer"], r["state_id"]): r for r in rows if r["combined_survives"]}


def parameter_selected(rec, rng):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    S = [set() for _ in range(b)]
    alpha = rng.choice([-3.0, -1.5, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0])
    beta = rng.choice([-4.0, -2.0, 0.0, 1.0, 2.0, 4.0])
    gamma = rng.choice([-0.6, -0.25, 0.0, 0.25, 0.6])
    noise = rng.choice([0.25, 0.75, 1.5, 3.0, 6.0])
    order = sorted(range(a), key=lambda i: (-s[i], rng.random()))
    for i in order:
        eligible = [u for u in range(b) if rho[u] >= s[i] and len(S[u]) < a - rho[u]]
        if len(eligible) < s[i]:
            return None
        scored = []
        for u in eligible:
            q = len(S[u]); cap = a - rho[u]
            score = alpha*q + beta*(q/max(1, cap)) + gamma*rho[u] + noise*rng.random()
            scored.append((score, rng.random(), u))
        for _, _, u in sorted(scored)[:s[i]]:
            S[u].add(i)
    return S


def p_penalty(rec, q):
    a, b, rho = rec["a"], rec["b"], rec["rho"]
    Q = sum(q)
    cap = [min(rho[u] + b - a - 1, b - 1 - q[u]) for u in range(b)]
    if min(cap, default=0) < 0:
        return 1000 + sum(-min(0, x) for x in cap)
    if sum(cap) < Q:
        return 100 + Q - sum(cap)
    p = [0]*b; left = Q
    for u in sorted(range(b), key=lambda u: (-(rho[u]+q[u]), -cap[u], u)):
        take = min(cap[u], left); p[u]=take; left-=take
    assert left == 0
    deficit = 0
    for k in range(a+2):
        lhs = sum(q[u] for u in range(b) if q[u] > k)
        rhs = sum(p[u] for u in range(b) if rho[u]+q[u] >= k)
        deficit += max(0, lhs-rhs)
    return deficit


def spill_penalty(rec, q):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    Q=sum(q); S_total=sum(s)
    elig=[sum(rho[v]>=s[i] for v in range(b)) for i in range(a)]
    ps=[0]; pe=[0]
    for x in sorted(s,reverse=True): ps.append(ps[-1]+x)
    for x in sorted(elig,reverse=True): pe.append(pe[-1]+x)
    penalty=0
    for u in range(b):
        nu=q[u]+rho[u]
        if not 0<=nu<=a: return 1000+abs(nu-a)
        cand=[v for v in range(b) if v!=u and q[v]+rho[v]>=q[u]-1 and q[v]<=nu and rho[v]+b-a-1>=1]
        penalty += max(0,q[u]-len(cand))*5
        if len(cand)>=q[u]:
            h=a-nu
            G=sum(min(q[v],h) for v in range(b) if v!=u)-sum(sorted(min(q[v],h) for v in cand)[:q[u]])
            lam=max(0,S_total-ps[nu],Q-pe[nu])
            penalty += max(0,lam-G)
    return penalty


def score(rec,S):
    q=[len(z) for z in S]
    pp=p_penalty(rec,q); sp=spill_penalty(rec,q)
    return (pp+sp, sp, pp, max(q)-min(q)), q


def try_witness(rec,S):
    if S is None:return None
    q=[len(z) for z in S]
    p=greedy_p(rec,q)
    if p is None:return None
    ok,_=spill_details(rec,q)
    if not ok:return None
    w={"selected":[sorted(z) for z in S],"q":q,"p":p}
    w["check"]=check_witness(rec,w)
    return w


def local_improve(rec,S,rng,steps=400):
    current=[set(x) for x in S]
    best_score,bq=score(rec,current)
    if best_score[0]==0:return current,best_score
    a,b,s,rho=rec["a"],rec["b"],rec["s"],rec["rho"]
    for step in range(steps):
        moves=[]
        # random subset of feasible one-label moves; each preserves x=s exactly.
        for _ in range(100):
            u=rng.randrange(b)
            if not current[u]:continue
            i=rng.choice(tuple(current[u]))
            v=rng.randrange(b)
            if v==u or i in current[v] or rho[v]<s[i] or len(current[v])>=a-rho[v]:continue
            moves.append((i,u,v))
        if not moves:continue
        rng.shuffle(moves)
        accepted=False
        for i,u,v in moves[:40]:
            current[u].remove(i); current[v].add(i)
            sc,_=score(rec,current)
            if sc < best_score or (step%50==49 and sc[0] <= best_score[0]+1 and rng.random()<0.1):
                best_score=sc; accepted=True; break
            current[v].remove(i); current[u].add(i)
        if not accepted:
            continue
        if best_score[0]==0:return current,best_score
    return current,best_score


def main():
    pass1=json.loads((HERE/"FULL_DOMAIN_SPILL_WITNESSES.json").read_text())
    unresolved=[(x["layer"],x["state_id"]) for x in pass1["unresolved"]]
    assert len(unresolved)==pass1["summary"]["unresolved"]
    bykey=survivors_by_key()
    new=[]; still=[]; diagnostics=[]
    for idx,key in enumerate(unresolved):
        rec=bykey[key]
        seed=913000000+idx*100003+rec["state_id"]
        rng=random.Random(seed)
        best=None; best_tuple=None; found=None; attempts=0
        for attempt in range(20000):
            S=parameter_selected(rec,rng); attempts+=1
            if S is None:continue
            sc,_=score(rec,S)
            if best_tuple is None or sc<best_tuple:
                best_tuple=sc; best=[set(x) for x in S]
            w=try_witness(rec,S)
            if w is not None:
                found=w; break
            if attempt in (499,1999,7999) and best is not None:
                improved,isc=local_improve(rec,best,rng,steps=600)
                if isc < best_tuple:
                    best_tuple=isc; best=improved
                w=try_witness(rec,best)
                if w is not None:
                    found=w; break
        if found is None and best is not None:
            improved,isc=local_improve(rec,best,rng,steps=3000)
            if isc < best_tuple:
                best_tuple=isc; best=improved
            found=try_witness(rec,best)
        if found is not None:
            new.append({"layer":key[0],"state_id":key[1],"seed":seed,"attempts":attempts,**found})
        else:
            still.append({"layer":key[0],"state_id":key[1]})
            diagnostics.append({"layer":key[0],"state_id":key[1],"seed":seed,"attempts":attempts,"best_score":list(best_tuple) if best_tuple else None,
                "s":rec["s"],"rho":rec["rho"],"best_q":[len(x) for x in best] if best else None})
        print(f"{idx+1}/{len(unresolved)} {key} {'FOUND' if found else 'OPEN'} best={best_tuple} remaining={len(still)}",flush=True)
    out={
      "schema":"full-domain-spill-refinement-v1","date":"2026-09-13",
      "pass1_unresolved":len(unresolved),"new_witnesses":len(new),"still_unresolved":len(still),
      "interpretation":"Positive witnesses are directly checked. Still-unresolved states are OPEN, not excluded; random/local search is not exhaustive.",
      "new":new,"unresolved":still,"diagnostics":diagnostics}
    (HERE/"SPILL_WITNESS_REFINEMENT.json").write_text(json.dumps(out,separators=(",",":"))+"\n")
    print(json.dumps({"status":"PASS" if not still else "PARTIAL","new_witnesses":len(new),"still_unresolved":len(still)},indent=2))

if __name__=="__main__":main()
