#!/usr/bin/env python3
"""Graph-based falsification tests. Finite successes are not universal proofs."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as F
from collections import Counter
import gzip,json,random,math,sys,argparse,copy
sys.path.insert(0,str(Path(__file__).resolve().parent))
from exact_checks import Q2,require

def le2(g):
    n=len(g)
    return all((g[u]>>v)&1 or g[u]&g[v] for u in range(n) for v in range(u+1,n))

def crit(g):
    n=len(g)
    if n<3 or not le2(g) or all(x.bit_count()==n-1 for x in g):return False
    g=list(g)
    for u,v in combinations(range(n),2):
        if g[u]>>v&1:
            g[u]^=1<<v;g[v]^=1<<u;ok=le2(g);g[u]^=1<<v;g[v]^=1<<u
            if ok:return False
    return True

def masks(nxg):
    return [sum(1<<int(v) for v in nxg.neighbors(u)) for u in range(len(nxg))]

def selection_cases(g,v,rng,cap=512):
    n=len(g);allm=(1<<n)-1;H=[allm^(1<<i)^g[i] for i in range(n)]
    A=[i for i in range(n) if H[v]>>i&1];B=[i for i in range(n) if i!=v and not(H[v]>>i&1)]
    opts=[]
    for u,w in combinations(range(len(B)),2):
        if H[B[u]]>>B[w]&1:continue
        oo=[]
        for f,to in [(u,w),(w,u)]:
            for i in range(len(A)):
                if H[B[f]]>>A[i]&1 and H[B[f]]|H[A[i]]==allm^(1<<B[to]):oo.append([f,i,to])
        require(oo,'critical graph has no cross quasi-edge')
        opts.append(oo)
    count=math.prod(map(len,opts)); sampled=count>cap
    selections=([rng.choice(o) for o in opts] for _ in range(16)) if sampled else product(*opts)
    return selections,count,sampled

def inspect(g,v,triples):
    n=len(g);allm=(1<<n)-1
    require(all(0<=g[u]<=allm and not(g[u]>>u&1) for u in range(n)),'simple masks')
    require(all(bool(g[u]>>v&1)==bool(g[v]>>u&1) for u,v in combinations(range(n),2)),'symmetry')
    b=max(x.bit_count() for x in g);require(g[v].bit_count()==b,'root is not maximum-degree')
    H=[allm^(1<<i)^g[i] for i in range(n)]
    A=[i for i in range(n) if H[v]>>i&1];B=[i for i in range(n) if i!=v and not(H[v]>>i&1)]
    a=len(A);selected=set();pairset=set();q=[0]*b;p=[0]*b
    for u,i,w in triples:
        require(0<=u<b and 0<=w<b and 0<=i<a and u!=w,'invalid triple')
        require(H[B[u]]>>A[i]&1,'selected cross-edge missing')
        require(H[B[u]]|H[A[i]]==allm^(1<<B[w]),'incorrect unique exception')
        key=tuple(sorted((u,w)));require(key not in pairset,'duplicate unordered pair')
        require((u,i) not in selected,'duplicate selected incidence')
        selected.add((u,i));pairset.add(key);q[u]+=1;p[w]+=1
    missing={(u,w) for u,w in combinations(range(b),2) if not(H[B[u]]>>B[w]&1)}
    require(pairset==missing,'missing B-pair coverage')
    res={(u,i) for u in range(b) for i in range(a) if H[B[u]]>>A[i]&1 and (u,i) not in selected}
    rho=[sum(x==u for x,i in res) for u in range(b)];R=[sum(j==i for u,j in res) for i in range(a)]
    d=[sum(g[x]>>y&1 for y in A) for x in A];x=[sum(j==i for u,j in selected) for i in range(a)]
    s=[max(0,di-ri) for di,ri in zip(d,R)];r=len(res);t=sum(z.bit_count() for z in g)//2-b*(n-b)
    require(sum(d)==2*(r+t),'ledger');require(sum(s)>=r+2*t,'demand ledger')
    require(all(xi>=si for xi,si in zip(x,s)),'demand supply')
    for u,i,w in triples:
        require(d[i]<=rho[u]+R[i],'column injection')
        require(d[i]<=rho[u]+rho[w],'pair injection')
        require(d[i]<=rho[u]+q[u]-1,'source adjacency')
        require(rho[w]+q[w]>=q[u]-1,'supplement adjacency')
        require(R[i]+x[i]>=q[u]+p[u],'actual endpoint bound')
    out={'systems':1,'positive_surplus':int(t>0),'nonempty_selected_systems':int(bool(triples)),
         'nonempty_demands':int(any(s)),'a_at_least_25':int(a>=25),'pair_capacity_thresholds':0,
         'nonempty_spare_classes':0,'nonempty_two_spare_classes':0}
    if a:
        require(max(s,default=0)<a,'demand denominator')
        charge=sum(F(si*si,a-si) for si in s)
        require(charge<=r,'charging inequality')
        c=Q2(F(3,2),-1);lam=Q2(1,F(-1,2));loss=sum((si-lam*a)**2/(a-si) for si in s)
        led=F(sum(s)-r-2*t,2);ch=F(r-charge,2)
        require(c*a*a-t==loss+led+ch and led>=0 and ch>=0,'exact deficit decomposition')
        if a>=25:require(t<(c-F(1,5000))*a*a,'improved surplus theorem')
        for h in range(1,max(s,default=0)+1):
            I={i for i in range(a) if s[i]>=h};Z={u for u in range(b) if rho[u]>=h};z=len(Z)
            T=h+(a-len(I))+1;busy={u for u in Z if q[u]>T};k=len(busy)
            require(all(w in Z for u,i,w in triples if u in busy),'busy supplement confinement')
            P=sum(x[i] for i in I)
            require(P<=(z-k)*T+k*z-F(k*(k+1),2),'joint pair capacity')
            require(P<=F(z*z+T*T,2),'pair square bound');out['pair_capacity_thresholds']+=1
        h=max(rho,default=0);z=sum(ru==h for ru in rho);I=[i for i in range(a) if s[i]==h]
        if h>=1 and h<=z<=h*h+h:
            require(h*len(I)<=(2*h-1)*z,'general spare theorem')
            out['nonempty_spare_classes']=int(bool(I));out['nonempty_two_spare_classes']=int(bool(I) and z==h+2)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--generate',action='store_true');args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; rng=random.Random(20260907)
    inherited=json.loads((root/'tests/inherited_actual_graph_instances.json').read_text())
    totals=Counter();graphs=set();checks=0;all_records=[]
    for e in inherited:
        g=e['g'];key=tuple(g)
        if key not in graphs:require(crit(g),'inherited graph fails criticality');graphs.add(key)
        totals.update(inspect(g,e['root'],e['triples']));all_records.append({'g':g,'root':e['root'],'triples':e['triples']})
    inherited_n=len(inherited);generated=[];details={}
    target=root/'tests/generated_graph_systems.json'
    if args.generate:
        import networkx as nx
        atlas=list(nx.graph_atlas_g());critical_atlas=[]
        for G in atlas:
            if len(G)<3:continue
            g=masks(G)
            ok=crit(g)
            # Different distance implementation for every atlas verdict.
            nx_ok=nx.is_connected(G) and nx.diameter(G)==2
            if nx_ok:
                for u,v in list(G.edges()):
                    C=G.copy();C.remove_edge(u,v)
                    if nx.is_connected(C) and nx.diameter(C)<=2:nx_ok=False;break
            require(ok==nx_ok,'bitset/networkx criticality disagreement')
            if ok:critical_atlas.append(g)
        extra=[]
        for n in [8,9,10,12,16,20]:
            for trial in range(20):
                g=[((1<<n)-1)^(1<<i) for i in range(n)];edges=list(combinations(range(n),2));rng.shuffle(edges)
                for u,v in edges:
                    g[u]^=1<<v;g[v]^=1<<u
                    if not le2(g):g[u]^=1<<v;g[v]^=1<<u
                require(crit(g),'greedy graph not critical');extra.append(g)
        # Large exact families exercise a>=25, but not near-saturation premises.
        for sizes in [[8,8,8,8,8],[12,9,8,10,11],[1,20,20,1,1],[15,15,15,15,15]]:
            groups=[];k=0
            for size in sizes:groups.append(list(range(k,k+size)));k+=size
            g=[0]*k
            for c in range(5):
                for u in groups[c]:
                    for v in groups[(c+1)%5]:g[u]|=1<<v;g[v]|=1<<u
            require(crit(g),'C5 blow-up criticality');extra.append(g)
        roots=0;sampled_roots=0;full_roots=0;largest=0
        for g in critical_atlas+extra:
            b=max(x.bit_count() for x in g)
            roots_here=[i for i,x in enumerate(g) if x.bit_count()==b]
            if len(g)>7:roots_here=roots_here[:2]
            for v in roots_here:
                cases,count,sampled=selection_cases(g,v,rng);roots+=1
                sampled_roots+=sampled;full_roots+=not sampled;largest=max(largest,count)
                for tr in cases:generated.append(dict(g=g,root=v,triples=list(tr)))
        details=dict(atlas_graphs=len(atlas),critical_atlas_graphs=len(critical_atlas),
                     extra_graphs=len(extra),roots=roots,exhaustive_selection_roots=full_roots,
                     sampled_selection_roots=sampled_roots,largest_selection_product=largest,networkx_version=nx.__version__)
        target.write_text(json.dumps({'generation':details,'systems':generated},separators=(',',':')))
    else:
        data=json.loads(target.read_text());details=data['generation'];generated=data['systems']
    for e in generated:
        key=tuple(e['g'])
        if key not in graphs:require(crit(e['g']),'saved graph fails criticality');graphs.add(key)
        totals.update(inspect(e['g'],e['root'],e['triples']));all_records.append(e)
    # Corrupt actual valid samples: no malformed sample may be accepted as proof input.
    e=next(copy.deepcopy(e) for e in all_records if e['triples']);bad=[]
    a=copy.deepcopy(e);a['triples'].pop();bad.append(('omitted_pair',a))
    a=copy.deepcopy(e);a['triples'].append(a['triples'][0]);bad.append(('duplicate_pair',a))
    a=copy.deepcopy(e);a['triples'][0][2]=a['triples'][0][0];bad.append(('self_supplement',a))
    rejected=[]
    for name,e in bad:
        try:inspect(e['g'],e['root'],e['triples'])
        except ValueError:rejected.append(name)
        else:raise ValueError('negative control accepted: '+name)
    report=dict(all_checks_pass=True,inherited_systems=inherited_n,generated_systems=len(generated),
      distinct_labelled_graphs=len(graphs),counts=dict(totals),generation=details,
      negative_controls_rejected=rejected,positive_surplus_actual_graphs_tested=totals['positive_surplus'],
      near_saturation_actual_graphs_present=False,
      limitation='Finite regressions only. No positive-surplus example, no empirical universal proof; larger selections may be sampled.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
