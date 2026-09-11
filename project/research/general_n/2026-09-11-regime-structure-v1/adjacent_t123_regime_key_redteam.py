#!/usr/bin/env python3
"""Exact red-team of low-threshold regime compression on adjacent t=1,2,3 labs.

This script deliberately asks whether J=2*z2-D1 carries genuine order information
or is mainly a finite encoding of simpler statistics.  It consumes only the
already-preserved exact canonical template assignments and regenerated audited
frontiers; no floating point or optimizer is used here.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
from pathlib import Path
import importlib.util
import json


def load_t1(exact_script: Path):
    spec=importlib.util.spec_from_file_location("t1exact",exact_script)
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    out=[]
    for pf in mod.PROFILES:
        i=pf["hard_position"]
        out.append({
            "index":i,"demand_id":pf["demand_id"],
            "s":list(pf["s"]),"rho":list(pf["rho"]),
            "a":int(mod.A),"b":len(pf["rho"]),"label":mod.ASSIGN[i],
        })
    return out


def load_n29(demands_json: Path, rows: Path, t: int):
    D=json.loads(demands_json.read_text())
    out=[]
    for line in rows.read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split()))
        did=z[0]; rho=z[2:]; s=D[did]["s"]
        if min(s)>0 and sum(s)==sum(rho)+2*t:
            out.append({
                "index":len(out),"demand_id":did,
                "s":s,"rho":rho,"a":12,"b":len(rho),
            })
    return out


def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k: h=k
        else: break
    return h


def D1(p): return p["s"].count(1)
def rho1(p): return p["rho"].count(1)
def z2(p): return sum(x>=2 for x in p["rho"])
def J(p): return 2*z2(p)-D1(p)
def G(p): return 2*rho1(p)+D1(p)


def label_t1(p): return p["label"]

def label_t2(p):
    d=D1(p)
    if d==2: return "T0"
    if d==1: return "T1"
    if d==0: return "T2"
    raise ValueError((p["index"],d))

def label_t3(p):
    r1=rho1(p); s5=p["s"].count(5); d1=D1(p)
    if r1<=8:
        return "A530" if s5==0 else "A38"
    return "A1" if d1==0 else "A0"


def census(P,label_fn,key_fn):
    d=defaultdict(Counter)
    for p in P: d[key_fn(p)][label_fn(p)]+=1
    rows=[]
    for k in sorted(d,key=lambda x:repr(x)):
        labs=dict(sorted(d[k].items()))
        rows.append({
            "key":list(k) if isinstance(k,tuple) else k,
            "profiles":sum(labs.values()),"labels":labs,"mixed":len(labs)>1,
        })
    return rows


def summary(rows):
    m=[r for r in rows if r["mixed"]]
    return {"occupied_cells":len(rows),"mixed_cells":len(m),"mixed_profiles":sum(r["profiles"] for r in m)}


def forbidden_slopes(P,label_fn):
    """Positive a/b for which (h, a*rho1+b*D1) collides across labels."""
    vals=defaultdict(list)
    for p in P: vals[h_res(p["rho"])].append(p)
    out=set()
    for group in vals.values():
        for i,p in enumerate(group):
            for q in group[i+1:]:
                if label_fn(p)==label_fn(q): continue
                dr=rho1(p)-rho1(q); dd=D1(p)-D1(q)
                if dr and dd and dr*dd<0:
                    x=Fraction(-dd,dr)
                    if x>0: out.add(x)
    return sorted(out)


def main():
    ap=ArgumentParser()
    ap.add_argument("--t1-exact-script",type=Path,required=True)
    ap.add_argument("--t2-demands-json",type=Path,required=True)
    ap.add_argument("--t2-rows",type=Path,required=True)
    ap.add_argument("--t3-demands-json",type=Path,required=True)
    ap.add_argument("--t3-rows",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    z=ap.parse_args()

    P1=load_t1(z.t1_exact_script)
    P2=load_n29(z.t2_demands_json,z.t2_rows,2)
    P3=load_n29(z.t3_demands_json,z.t3_rows,3)
    assert (len(P1),len(P2),len(P3))==(7,902,94)
    labs=[("t1",P1,label_t1),("t2",P2,label_t2),("t3",P3,label_t3)]

    natural={}
    keys={
        "D1":lambda p:(D1(p),),
        "D1_h":lambda p:(D1(p),h_res(p["rho"])),
        "D1_h_rho1":lambda p:(D1(p),h_res(p["rho"]),rho1(p)),
        "D1_h_half_z2":lambda p:(D1(p),h_res(p["rho"]),int(2*z2(p)>=p["b"])),
        "h_J":lambda p:(h_res(p["rho"]),J(p)),
    }
    for keyname,kf in keys.items():
        natural[keyname]={}
        for name,P,lf in labs:
            rows=census(P,lf,kf)
            natural[keyname][name]={"summary":summary(rows),"cells":rows}

    coeff_scan=[]
    success=[]
    for a in range(0,13):
        for b in range(0,13):
            if a==0 and b==0: continue
            if gcd(a,b)!=1: continue
            rec={"a":a,"b":b,"max_coeff":max(a,b)}
            good=True
            for name,P,lf in labs:
                rows=census(P,lf,lambda p,a=a,b=b:(h_res(p["rho"]),a*rho1(p)+b*D1(p)))
                s=summary(rows); rec[name]=s
                good &= s["mixed_cells"]==0
            rec["all_labs_pure"]=good
            coeff_scan.append(rec)
            if good: success.append((max(a,b),a+b,a,b))
    success.sort()

    forbidden={}
    for name,P,lf in labs:
        forbidden[name]=[f"{x.numerator}/{x.denominator}" for x in forbidden_slopes(P,lf)]

    # Find all integer half-source thresholds k making (D1,h,1[z2>=k]) pure.
    threshold_scan=[]
    for k in range(0,18):
        rec={"k":k}; good=True
        for name,P,lf in labs:
            rows=census(P,lf,lambda p,k=k:(D1(p),h_res(p["rho"]),int(z2(p)>=k)))
            s=summary(rows); rec[name]=s; good &= s["mixed_cells"]==0
        rec["all_labs_pure"]=good
        threshold_scan.append(rec)

    # Compact canonical leaf census for the particularly natural balanced split 2*z2>=b.
    leaves={}
    for name,P,lf in labs:
        rows=census(P,lf,keys["D1_h_half_z2"])
        leaves[name]=[r for r in rows]

    ok=(
        natural["D1"]["t1"]["summary"]["mixed_cells"]==0 and
        natural["D1"]["t2"]["summary"]["mixed_cells"]==0 and
        natural["D1"]["t3"]["summary"]["mixed_cells"]>0 and
        natural["D1_h"]["t3"]["summary"]["mixed_cells"]>0 and
        all(natural["D1_h_half_z2"][name]["summary"]["mixed_cells"]==0 for name in ("t1","t2","t3")) and
        success and success[0][2:]==(2,1)
    )

    out={
        "schema":"adjacent-t123-regime-key-redteam-v1",
        "status":"PASS" if ok else "FAIL",
        "scope":{"t1":len(P1),"t2":len(P2),"t3":len(P3)},
        "definitions":{
            "D1":"#{i:s_i=1}","rho1":"#{u:rho_u=1}","z2":"#{u:rho_u>=2}=b-rho1",
            "J":"2*z2-D1","balanced_source_bit":"1[2*z2>=b]",
        },
        "natural_key_census":natural,
        "balanced_tree_leaves":leaves,
        "primitive_coefficient_scan_0_to_12":coeff_scan,
        "successful_primitive_pairs_sorted": [{"a":a,"b":b,"max_coeff":m,"sum_coeff":s} for m,s,a,b in success],
        "positive_forbidden_slopes_a_over_b":forbidden,
        "z2_threshold_scan":threshold_scan,
        "interpretation":(
            "D1 alone determines the preserved canonical assignment at t=1 and t=2. "
            "At t=3, D1 and h_res still leave a collision, but the balanced source-tail bit 1[2*z2>=b] resolves it. "
            "The linear key J=2*z2-D1 is therefore partly an arithmetic encoding (notably parity of D1), and its coefficient 2 should not be promoted as a combinatorial law without further evidence. "
            "A more interpretable finite key on these labs is the decision tree (D1,h_res,1[2*z2>=b])."
        ),
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":out["status"],"successful_pairs":out["successful_primitive_pairs_sorted"][:12],"forbidden":forbidden,"thresholds":[r["k"] for r in threshold_scan if r["all_labs_pure"]]},indent=2))
    if not ok: raise SystemExit(1)

if __name__=="__main__": main()
