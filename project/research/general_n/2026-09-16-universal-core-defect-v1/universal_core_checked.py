#!/usr/bin/env python3
"""Check the universal-core local lemma and incidence relaxation, not canonical graphs.

Python uses bitset reachability for graphs. The C++ replay enumerates individual
intermediate vertices. Both implementations are by the same assistant.
Run with --generate-only, --replay-only, or no option for generation and replay.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools as it, json, random, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SEED=202609162

def add(a:list[int],u:int,v:int)->None:
    assert u!=v
    a[u]|=1<<v; a[v]|=1<<u

def reach(a:list[int],u:int)->int:
    r=(1<<u)|a[u]; ns=a[u]
    while ns:
        b=ns&-ns; ns-=b; r|=a[b.bit_length()-1]
    return r

def gd(a:list[int],d:int,k:int)->list[int]:
    n=len(a); full=(1<<d)-1
    universal=all((a[t]&full)==(full^(1<<t)) for t in (0,1))
    common=bool(k>=d and a[k]&1 and a[k]&2)
    singles=[x for x in range(d,n) if a[x]&full in (1,2)]
    covered=all(a[k]>>x&1 for x in singles)
    eligible=bool(d>=3 and a[0]&2 and universal and common and covered)
    mu=d*(d-1)//2-sum((a[t]&full).bit_count() for t in range(d))//2
    pre=[reach(a,i) for i in range(n)]
    aa=a.copy(); aa[0]&=~2; aa[1]&=~1
    post=[reach(aa,i) for i in range(n)]
    lost=sum(bool(pre[i]>>j&1) and not(post[i]>>j&1) for i in range(n) for j in range(i+1,n))
    diameter_two=int(all(r==((1<<n)-1) for r in pre))
    return [int(eligible),mu,len(singles),diameter_two,lost]

def idata(d:int,q:list[int],p:list[int],beta:list[int],cols:list[tuple[int,int]])->list[int]:
    ts=set(range(d)); qm=[{j for j in ts if q[t]>>j&1} for t in ts]
    universe={t for t in ts if len(qm[t])==d-1}
    supports=[{j for j in ts if mask>>j&1} for mask,_ in cols]
    marks=set().union(*(s for s in supports if len(s)==1)) if supports else set()
    U=universe-marks
    row=[sum(t in s for s in supports) for t in range(d)]
    m=sum(p); mu=d*(d-1)//2-sum(map(len,qm))//2
    L=sum(w-len(s) for s,(_,w) in zip(supports,cols)); b=sum(beta)
    valid=(d>=3 and all(x>=1 for x in p) and all(x>=0 for x in beta)
      and all(s and w in (d,d-1) and len(s)<=w for s,(_,w) in zip(supports,cols))
      and all(row[t]==1+m-p[t]+beta[t]+d-1-len(qm[t]) for t in range(d)))
    cover=all(len(s&U)<=1 for s in supports)
    D=L+b+2*mu; bound=2*mu+(d-2)*max(0,len(universe)-1)
    return [int(valid and cover),len(universe),len(U),mu,L,b,D,bound,int(D>=bound)]

def digest(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def generate()->None:
    counters={"exhaustive_graphs_inspected":0,"exhaustive_graph_records":0,
      "sampled_graph_records":0,"negative_controls":0,"incidence_multisets_inspected":0,
      "incidence_records":0,"incidence_eligible":0,"incidence_eligible_incomplete":0,
      "incidence_eligible_u_ge_2":0,"graph_eligible":0,"graph_eligible_incomplete":0,
      "graph_eligible_singleton_replacements":0,"graph_eligible_incomplete_with_singletons":0,
      "graph_diameter_two":0,"covering_failure_controls":0}
    rnd=random.Random(SEED); idx=0; graph_records=[]; neg={}; equality_rows=[]
    with (ROOT/'INPUT.txt').open('w') as fi,(ROOT/'PYTHON_DECISIONS.tsv').open('w') as fo:
        def put_g(a,d,k,kind):
            nonlocal idx
            out=gd(a,d,k)
            assert not out[0] or out[-1]==0
            fi.write('G '+str(len(a))+' '+str(d)+' '+str(k)+' '+' '.join(map(str,a))+'\n')
            fo.write(str(idx)+' G '+' '.join(map(str,out))+'\n')
            if out[0]:
                counters['graph_eligible']+=1
                counters['graph_eligible_incomplete']+=out[1]>0
                counters['graph_eligible_singleton_replacements']+=out[2]>0
                counters['graph_eligible_incomplete_with_singletons']+=out[1]>0 and out[2]>0
            counters['graph_diameter_two']+=out[3]
            if kind=='negative':
                assert out[3] and out[4]>0 and not out[0]
            graph_records.append(dict(index=idx,kind=kind,n=len(a),d=d,k=k,adjacency=a,decision=out))
            idx+=1
        def put_i(d,q,p,beta,cols,kind):
            nonlocal idx
            out=idata(d,q,p,beta,cols)
            assert not out[0] or out[-1]
            fi.write('I '+str(d)+' '+str(len(cols))+' '+' '.join(map(str,q+p+beta))+' '+
                     ' '.join(f'{s} {w}' for s,w in cols)+'\n')
            fo.write(str(idx)+' I '+' '.join(map(str,out))+'\n')
            counters['incidence_records']+=1
            if out[0]:
                counters['incidence_eligible']+=1
                counters['incidence_eligible_incomplete']+=out[3]>0
                counters['incidence_eligible_u_ge_2']+=out[2]>=2
            if kind=='covering-control':
                assert not out[0] and not out[-1]
                counters['covering_failure_controls']+=1
            if out[0] and out[6]==out[7] and len(equality_rows)<30:
                equality_rows.append(dict(index=idx,d=d,q=q,p=p,beta=beta,cols=cols,decision=out))
            idx+=1
        # Exhaust labelled graphs with fixed distinguished roles. Including every
        # labelled adjacency mask covers all assignments to these fixed roles.
        for n in range(4,7):
            pairs=list(it.combinations(range(n),2))
            for mask in range(1<<len(pairs)):
                a=[0]*n
                for j,(x,y) in enumerate(pairs):
                    if mask>>j&1:add(a,x,y)
                counters['exhaustive_graphs_inspected']+=1
                if not(a[0]&2):continue
                for d in range(3,n):
                    k=d; out=gd(a,d,k)
                    if out[0]:
                        put_g(a,d,k,'exhaustive');counters['exhaustive_graph_records']+=1
                    # Find all necessary negative controls from actual diameter-two graphs.
                    if out[3] and out[4]>0:
                        T=(1<<d)-1
                        universals=[(a[t]&T)==(T^(1<<t)) for t in (0,1)]
                        common=bool(a[k]&1 and a[k]&2)
                        singles=[x for x in range(d,n) if a[x]&T in (1,2)]
                        covered=all(a[k]>>x&1 for x in singles)
                        if common and covered and not universals[0] and universals[1] and 'endpoint-0' not in neg:
                            neg['endpoint-0']=(a.copy(),d,k)
                        if common and covered and universals[0] and not universals[1] and 'endpoint-1' not in neg:
                            neg['endpoint-1']=(a.copy(),d,k)
                        if all(universals) and common and not covered and 'singleton-pool-protection' not in neg:
                            neg['singleton-pool-protection']=(a.copy(),d,k)
        for name,(a,d,k) in sorted(neg.items()):
            put_g(a,d,k,'negative');counters['negative_controls']+=1
        assert set(neg)=={'endpoint-0','endpoint-1','singleton-pool-protection'},set(neg)
        # Larger positive models: arbitrary holes away from the tested endpoints.
        for d in range(4,13):
            for rep in range(30):
                n=d+4+(rep%4); k=d; a=[0]*n
                for t,s in it.combinations(range(d),2):
                    if t<2 or rnd.random()<0.55:add(a,t,s)
                add(a,0,k);add(a,1,k)
                for t in range(2,d):
                    if rnd.random()<0.5:add(a,t,k)
                # An actual singleton support at each tested endpoint.
                add(a,0,d+1);add(a,1,d+2)
                for x in range(d+3,n):
                    for t in range(d):
                        if rnd.random()<0.42:add(a,t,x)
                for x,y in it.combinations(range(d,n),2):
                    if rnd.random()<0.5:add(a,x,y)
                for x in range(d,n):
                    if a[x]&((1<<d)-1) in (1,2):add(a,k,x)
                put_g(a,d,k,'sampled');counters['sampled_graph_records']+=1
        # d=3: exhaust all support/weight multisets of size <=6, all tight
        # graphs, and beta_t in {0,1}. Derive integer pool sizes from exact rows.
        d=3;types=[(m,w) for m in range(1,1<<d) for w in (d-1,d) if m.bit_count()<=w]
        qpairs=list(it.combinations(range(d),2)); control_saved=False
        for length in range(3,7):
            for choices in it.combinations_with_replacement(range(len(types)),length):
                counters['incidence_multisets_inspected']+=1
                cols=[types[j] for j in choices];row=[sum(m>>t&1 for m,_ in cols) for t in range(d)]
                for qbits in range(1<<len(qpairs)):
                    q=[0]*d
                    for j,(t,s) in enumerate(qpairs):
                        if qbits>>j&1:add(q,t,s)
                    nu=[d-1-q[t].bit_count() for t in range(d)]
                    for beta in it.product(range(2),repeat=d):
                        numerator=sum(row)-d-sum(beta)-sum(nu)
                        if numerator%(d-1):continue
                        m=numerator//(d-1)
                        if m<d:continue
                        p=[1+m+beta[t]+nu[t]-row[t] for t in range(d)]
                        if min(p)<1:continue
                        out=idata(d,q,p,list(beta),cols)
                        if out[0]:put_i(d,q,p,list(beta),cols,'exhaustive-incidence')
                        elif not out[-1] and not control_saved:
                            put_i(d,q,p,list(beta),cols,'covering-control');control_saved=True
        assert control_saved
        # Force genuinely nontrivial U cases and arbitrary incomplete Q.
        for d in range(3,16):
            for rep in range(60):
                q=[0]*d
                desired_g=rep%(d+1)
                for t,s in it.combinations(range(d),2):
                    if t<desired_g or s<desired_g or rnd.random()<0.5:add(q,t,s)
                C=[t for t in range(d) if q[t].bit_count()==d-1]
                u=min(rep%4,len(C),d-1);U=set(C[:u]); outside=[t for t in range(d) if t not in U]
                p=[1+rnd.randrange(3) for _ in range(d)];m=sum(p)
                target=[1+m-p[t]+d-1-q[t].bit_count() for t in range(d)]
                cols=[];row=[0]*d
                for t in U:
                    for _ in range(target[t]):
                        s=rnd.choice(outside);mask=(1<<t)|(1<<s)
                        cols.append((mask,d-rnd.randrange(2)));row[t]+=1;row[s]+=1
                for t in outside:
                    # Force all universal vertices outside U to be marked.
                    howmany=max(1 if t in C else 0,target[t]-row[t])
                    for _ in range(howmany):cols.append((1<<t,d-rnd.randrange(2)));row[t]+=1
                beta=[row[t]-target[t] for t in range(d)]
                assert min(beta)>=0
                assert idata(d,q,p,beta,cols)[0]
                put_i(d,q,p,beta,cols,'seeded-incidence')
        # Exact envelope and auxiliary bound as fully reproducible arithmetic.
        envelopes=[]
        for d in range(3,100):
            values=[2*mu+(d-2)*max(0,d-2*mu-1) for mu in range(d*(d-1)//2+1)]
            assert min(values)==2*(d//2)
            for g in range(2,d+1):assert g*(2*d-g)-2*d>=2*(d-2)
            envelopes.append(dict(d=d,minimum=min(values),minimizing_mu=[j for j,v in enumerate(values) if v==min(values)]))
    (ROOT/'GRAPH_RECORDS.json').write_text(json.dumps(graph_records,separators=(',',':'))+'\n')
    (ROOT/'CONTROLS.json').write_text(json.dumps({'negative_graph_controls':{k:{'a':a,'d':d,'k':kk} for k,(a,d,kk) in neg.items()},'incidence_equality_samples':equality_rows},indent=2)+'\n')
    (ROOT/'ENVELOPES.json').write_text(json.dumps(envelopes,indent=2)+'\n')
    summary={'status':'PYTHON_GENERATED_CPP_REPLAY_PENDING','seed':SEED,'records':idx,**counters,
      'input_sha256':digest(ROOT/'INPUT.txt'),'decision_sha256':digest(ROOT/'PYTHON_DECISIONS.tsv'),
      'scope':'Local graph lemma and incidence relaxation only; no canonical graph census, catalogue application or independent expert acceptance.'}
    (ROOT/'CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

def replay()->None:
    exe=ROOT/'check_universal_core_cpp'
    subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(ROOT/'check_universal_core.cpp'),'-o',str(exe)],check=True)
    with (ROOT/'INPUT.txt').open('rb') as fi,(ROOT/'CPP_DECISIONS.tsv').open('wb') as fo:
        subprocess.run([str(exe)],stdin=fi,stdout=fo,check=True)
    assert (ROOT/'PYTHON_DECISIONS.tsv').read_bytes()==(ROOT/'CPP_DECISIONS.tsv').read_bytes(),'Python/C++ mismatch'
    summary=json.loads((ROOT/'CHECK_SUMMARY.json').read_text())
    summary.update(status='PASS_LOCAL_AND_INCIDENCE_CHECKS',cpp_decision_sha256=digest(ROOT/'CPP_DECISIONS.tsv'),replay_agreement_records=summary['records'])
    (ROOT/'CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    for name in ['INPUT.txt','PYTHON_DECISIONS.tsv','CPP_DECISIONS.tsv','GRAPH_RECORDS.json']:
        with (ROOT/name).open('rb') as src,(ROOT/(name+'.gz')).open('wb') as raw:
            with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as dst:
                for chunk in iter(lambda:src.read(1<<20),b''):dst.write(chunk)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--generate-only',action='store_true');ap.add_argument('--replay-only',action='store_true');args=ap.parse_args()
    if args.generate_only and args.replay_only:ap.error('choose at most one mode')
    if args.replay_only:
        for name in ['INPUT.txt','PYTHON_DECISIONS.tsv']:
            if not (ROOT/name).exists():
                with gzip.open(ROOT/(name+'.gz'),'rb') as f:(ROOT/name).write_bytes(f.read())
    else:generate()
    if not args.generate_only:replay()
