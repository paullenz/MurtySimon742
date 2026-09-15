#!/usr/bin/env python3
from __future__ import annotations
import csv, json, sys
from pathlib import Path

SOURCE_RESULTS_SHA256='2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970'
EXPECTED_SURVIVORS=952
EXPECTED_N34=949
EXPECTED_N35=3
EXPECTED_WITNESS_KILLED=306
EXPECTED_WITNESS_RETAINED=646

def canonical_partition(caps,h,m,loss=None):
    if h<=0 or m<=0:return True,0
    caps=[min(int(c),m) for c in caps if c>0]
    if sum(caps)<h*m:return False,None
    if loss is None: loss=[0]*len(caps)
    d={tuple([0]*h):0}
    for cap,w in zip(caps,loss):
        nd=dict(d)
        for st,cost in d.items():
            seen=set()
            for j,x in enumerate(st):
                if x in seen:continue
                seen.add(x)
                a=list(st);a[j]=min(m,x+cap);a.sort();ns=tuple(a);nc=cost+w
                if nc<nd.get(ns,10**18):nd[ns]=nc
        d=nd
    t=tuple([m]*h)
    return t in d,d.get(t)

def witness_rejected(st,q):
    s,rho,a,b=st['s'],st['rho'],st['a'],st['b']
    for r in sorted(set(rho)):
        h=sum(x<=r for x in s)
        if not h:continue
        U=[u for u,(qq,rr) in enumerate(zip(q,rho)) if rr==r and qq==h]
        if not U:continue
        m=len(U); us=set(U); cand=[]
        for v,(qq,rr) in enumerate(zip(q,rho)):
            c=rr+b-a-1
            if v not in us and qq<=h+r-1 and qq+rr>=h-1 and c>0:cand.append((v,c))
        caps=[c for _,c in cand]
        ok,_=canonical_partition(caps,h,m)
        if not ok:return True,'CAPACITY_PARTITION',r
        for tau in sorted({x for x in s if x>r}):
            raw=sum(qq for qq,rr in zip(q,rho) if rr>=tau)
            demand=sum(x for x in s if x>=tau)
            losses=[max(0,q[v]-r) if rho[v]>=tau else 0 for v,_ in cand]
            ok,minloss=canonical_partition(caps,h,m,losses)
            assert ok
            if raw-minloss<demand:return True,f'HIGH_SQUEEZE_TAU_{tau}',r
    return False,'',-1

def parse_states(path):
    lines=[x.strip() for x in path.read_text().splitlines() if x.strip()]
    n=int(lines[0]);body=lines[1:]
    if len(body)!=n:raise SystemExit('EXPECTED_ACTIVE count mismatch')
    out={}
    for line in body:
        z=list(map(int,line.split()));layer,sid,a,b,t=z[:5];ns=z[5];s=z[6:6+ns];j=6+ns;nr=z[j];rho=z[j+1:j+1+nr]
        if j+1+nr!=len(z):raise SystemExit('state parse length mismatch')
        out[(layer,sid)]={'line':line,'layer':layer,'state_id':sid,'a':a,'b':b,'t':t,'s':s,'rho':rho}
    return out

def main():
    if len(sys.argv)!=3:raise SystemExit('usage: prepare_scan.py DISCOVERY_DIR OUTDIR')
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    import hashlib
    rp=root/'POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv'
    if hashlib.sha256(rp.read_bytes()).hexdigest()!=SOURCE_RESULTS_SHA256:raise SystemExit('pinned source results hash mismatch')
    states=parse_states(root/'plan'/'EXPECTED_ACTIVE.txt')
    with rp.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    surv=[r for r in rows if r['status']=='SURVIVES_RELATIONAL']
    if len(surv)!=EXPECTED_SURVIVORS:raise SystemExit('survivor count mismatch')
    if sum(r['layer']=='0' for r in surv)!=EXPECTED_N34 or sum(r['layer']=='1' for r in surv)!=EXPECTED_N35:raise SystemExit('survivor layer mismatch')
    killed=[];retained=[];screen=[]
    for r in surv:
        key=(int(r['layer']),int(r['state_id']));st=states[key];q=[int(x) for x in r['witness_q'].split(',')]
        if len(q)!=len(st['rho']):raise SystemExit(f'witness q length mismatch {key}')
        bad,why,rr=witness_rejected(st,q)
        rec={'layer':key[0],'state_id':key[1],'stored_witness_rejected':bad,'reason':why,'r':rr}
        screen.append(rec)
        (killed if bad else retained).append(key)
    if len(killed)!=EXPECTED_WITNESS_KILLED or len(retained)!=EXPECTED_WITNESS_RETAINED:raise SystemExit(f'witness split changed killed={len(killed)} retained={len(retained)}')
    target_lines=[states[k]['line'] for k in killed]
    (out/'TARGET_INPUT.txt').write_text(str(len(target_lines))+'\n'+'\n'.join(target_lines)+'\n')
    with (out/'STORED_WITNESS_SCREEN.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['layer','state_id','stored_witness_rejected','reason','r'],delimiter='\t');w.writeheader();w.writerows(screen)
    (out/'PRESERVED_WITNESS_SURVIVORS.tsv').write_text('layer\tstate_id\n'+''.join(f'{a}\t{b}\n' for a,b in retained))
    summary={'schema':'canonical-forced-core-scan-plan-v1','source_results_sha256':SOURCE_RESULTS_SHA256,'canonical_survivors':len(surv),'n34':EXPECTED_N34,'n35':EXPECTED_N35,'stored_witness_rejected':len(killed),'stored_witness_retained':len(retained),'target_keys':[list(x) for x in killed]}
    (out/'PLAN.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'target_count':len(killed),'retained_count':len(retained)}))
if __name__=='__main__':main()
