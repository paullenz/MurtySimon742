#!/usr/bin/env python3
"""Exact finite collision diagnostic for the adjacent t=1,2,3 RX-Hall regime labs.

t=1 is read from the preserved n=30 exact two-template replay.
t=2,3 are read from the regenerated n=29 audited frontiers.

The script does not re-prove the template gaps. It consumes deterministic regime
assignments already established by exact rational template replays and tests
whether coarse profile statistics separate those labels.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter, defaultdict
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
            "index":i,
            "demand_id":pf["demand_id"],
            "s":list(pf["s"]),
            "rho":list(pf["rho"]),
            "a":int(mod.A),
            "label":mod.ASSIGN[i],
        })
    return out


def load_n29(demands_json: Path, rows: Path, t: int):
    D=json.loads(demands_json.read_text())
    out=[]
    for line in rows.read_text().splitlines():
        if not line.strip():
            continue
        z=list(map(int,line.split()))
        did=z[0]; rho=z[2:]; s=D[did]["s"]
        if min(s)>0 and sum(s)==sum(rho)+2*t:
            out.append({
                "index":len(out),"demand_id":did,
                "s":s,"rho":rho,"a":12,
            })
    return out


def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k: h=k
        else: break
    return h


def initial_caps(s,rho,a):
    return [min(a-r,sum(x<=r for x in s)) for r in rho]


def cutoff_L(p):
    C=initial_caps(p["s"],p["rho"],p["a"])
    Z=[r+c for r,c in zip(p["rho"],C)]
    L=0
    for k in range(1,max(C,default=0)+1):
        if sum(z>=k-1 for z in Z)>=k+1:
            L=k
        else:
            break
    return L


def nu1(p): return p["s"].count(1)
def rho1(p): return p["rho"].count(1)
def G(p): return 2*rho1(p)+nu1(p)


def label_t1(p):
    return p["label"]


def label_t2(p):
    n=nu1(p)
    if n==2: return "T0"
    if n==1: return "T1"
    if n==0: return "T2"
    raise ValueError(f"unexpected t=2 nu1={n} at profile {p['index']}")


def label_t3(p):
    r1=rho1(p); s5=p["s"].count(5); s1=nu1(p)
    if r1<=8:
        return "A530" if s5==0 else "A38"
    return "A1" if s1==0 else "A0"


def key_hL(p):
    return (h_res(p["rho"]),cutoff_L(p))


def census(P,label_fn,key_fn):
    d=defaultdict(Counter)
    examples=defaultdict(list)
    for p in P:
        k=key_fn(p); lab=label_fn(p)
        d[k][lab]+=1
        if len(examples[k])<8: examples[k].append(p["index"])
    rows=[]
    for k in sorted(d):
        rows.append({
            "key":list(k) if isinstance(k,tuple) else k,
            "profiles":sum(d[k].values()),
            "labels":dict(sorted(d[k].items())),
            "mixed":len(d[k])>1,
            "example_indices":examples[k],
        })
    return rows


def mixed_summary(rows):
    m=[r for r in rows if r["mixed"]]
    return {"cells":len(m),"profiles":sum(r["profiles"] for r in m)}


def linear_test(P,label_fn,a,b):
    rows=census(P,label_fn,lambda p:key_hL(p)+(a*rho1(p)+b*nu1(p),))
    return mixed_summary(rows)


def first_by_label(P,label_fn,target_hL):
    ans={}
    for p in P:
        if key_hL(p)!=target_hL: continue
        lab=label_fn(p)
        if lab not in ans:
            ans[lab]={
                "index":p["index"],"demand_id":p["demand_id"],
                "rho1":rho1(p),"nu1":nu1(p),"G":G(p),
                "s":p["s"],"rho":p["rho"],
            }
    return ans


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
    if len(P1)!=7: raise SystemExit(f"expected 7 t=1 hard profiles, got {len(P1)}")
    if len(P2)!=902: raise SystemExit(f"expected 902 t=2 profiles, got {len(P2)}")
    if len(P3)!=94: raise SystemExit(f"expected 94 t=3 profiles, got {len(P3)}")

    labs=[("t1",P1,label_t1),("t2",P2,label_t2),("t3",P3,label_t3)]
    hL={}; hLG={}
    for name,P,lf in labs:
        a=census(P,lf,key_hL)
        b=census(P,lf,lambda p:key_hL(p)+(G(p),))
        hL[name]={"summary":mixed_summary(a),"cells":a}
        hLG[name]={"summary":mixed_summary(b),"cells":b}

    small_linear={}
    for a,b in [(1,0),(0,1),(1,1),(1,2),(2,1)]:
        rec={"statistic":f"{a}*rho1+{b}*nu1"}
        for name,P,lf in labs:
            rec[name]=linear_test(P,lf,a,b)
        small_linear[f"{a},{b}"]=rec

    triangle=[]
    for i in [0,3,77]:
        p=P2[i]
        triangle.append({
            "index":i,"label":label_t2(p),"demand_id":p["demand_id"],
            "h_res":h_res(p["rho"]),"L":cutoff_L(p),
            "rho1":rho1(p),"nu1":nu1(p),"G":G(p),
        })

    t1_profiles=[]
    for p in P1:
        t1_profiles.append({
            "index":p["index"],"label":label_t1(p),"demand_id":p["demand_id"],
            "h_res":h_res(p["rho"]),"L":cutoff_L(p),
            "rho1":rho1(p),"nu1":nu1(p),"G":G(p),
        })

    ok=(
        all(hL[name]["summary"]["cells"]>0 for name in ("t1","t2","t3")) and
        all(hLG[name]["summary"]["cells"]==0 for name in ("t1","t2","t3")) and
        all((x["h_res"],x["L"])==(4,6) for x in triangle) and
        all(small_linear["2,1"][name]["cells"]==0 for name in ("t1","t2","t3"))
    )
    out={
        "schema":"adjacent-t123-hL-compression-falsification-v2",
        "status":"PASS" if ok else "FAIL",
        "scope":{
            "t1":{"n":30,"a":13,"b":16,"profiles":len(P1)},
            "t2":{"n":29,"Delta":16,"a":12,"b":16,"profiles":len(P2)},
            "t3":{"n":29,"Delta":16,"a":12,"b":16,"profiles":len(P3)},
        },
        "definitions":{
            "h_res":"max{k: #{u:rho_u>=k}>=k}",
            "C_u":"min(a-rho_u,#{i:s_i<=rho_u})",
            "L":"max{k>=1: #{u:rho_u+C_u>=k-1}>=k+1}",
            "G":"2*#{u:rho_u=1}+#{i:s_i=1}",
        },
        "hL":hL,
        "hLG":hLG,
        "t1_exact_profiles":t1_profiles,
        "t2_lower_bound_triangle":triangle,
        "first_mixed_cell_profile_by_label":{
            "t1":first_by_label(P1,label_t1,(3,7)),
            "t2":first_by_label(P2,label_t2,(4,6)),
            "t3":first_by_label(P3,label_t3,(4,6)),
        },
        "small_nonnegative_primitive_linear_comparison":small_linear,
        "interpretation":"(h_res,L) is exactly falsified as a regime key in all three adjacent exact finite laboratories; adding G=2*rho1+nu1 makes every occupied cell regime-pure in t=1,2,3. This is a finite structural diagnostic, not a general-N theorem.",
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(1)


if __name__=="__main__":
    main()
