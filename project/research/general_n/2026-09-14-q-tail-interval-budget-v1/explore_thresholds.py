import json, collections, pathlib, math
ROOT=pathlib.Path(__file__).parent
states={}
for line in (ROOT/'project/research/general_n/2026-09-13-alternative-attacks-v1/Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt').read_text().splitlines()[1:]:
    z=list(map(int,line.split())); layer,id,a,b,t,ns=z[:6]; s=z[6:6+ns]; nr=z[6+ns]; rho=z[7+ns:]; assert len(rho)==nr
    states[id]=dict(layer=layer,id=id,a=a,b=b,t=t,s=s,rho=rho)
profiles=[]
for idx,line in enumerate((ROOT/'LAYER_EXCEPTION_DIAGNOSTIC.tsv').read_text().splitlines()):
    f=dict(part.split('=',1) for part in line.split('\t')[1:]); types=[list(map(int,row.split(','))) for row in f['types'].split(';')]; qrP=[]
    for q,c,p,n,*etc in types: qrP += [(q,c-q,p)]*n
    st=states[int(f['state'])]; q=[v[0] for v in qrP]; rho=[v[1] for v in qrP]; P=[v[2] for v in qrP]; c=[x+y for x,y in zip(q,rho)]; n=len(q); Q=sum(q); r=sum(rho); E=int(f['E']); D0=sum(st['s'])-r-2*st['t']; B=Q-r; G=n*(n-st['a']-1)-B
    assert Q==int(f['Q']) and Q==r+2*st['t']+D0+E and D0>=0 and G>=0
    rows=[]
    for tau in range(1,max(q)+2):
        S=[u for u in range(n) if q[u]>=tau]; D=sum(q[u] for u in S)
        yy=[sum(u!=w and q[u]<=c[w]+1 and q[w]<=c[u] for u in S) for w in range(n)]
        yy1=[sum(u!=w and q[u]<=c[w]+1 for u in S) for w in range(n)]
        yy0=[(len(S)-(w in S)) if c[w]+1>=tau else 0 for w in range(n)]
        cap=sum(min(P[w],yy[w]) for w in range(n)); cap1=sum(min(P[w],yy1[w]) for w in range(n)); cap0=sum(min(P[w],yy0[w]) for w in range(n)); capdead=sum(P[w] for w in range(n) if c[w]+1>=tau)
        rows.append(dict(tau=tau,D=D,exact=D-cap,interval=D-cap1,dead_count=D-cap0,dead=D-capdead))
    profiles.append(dict(index=idx,state=st['id'],a=st['a'],b=n,t=st['t'],s=st['s'],q=q,rho=rho,P=P,Esel=E,D0=D0,Q=Q,r=r,G=G,rows=rows))
if __name__=='__main__':
    print('profiles',len(profiles))
    for kind in ['exact','interval','dead_count','dead']:
        good=[p for p in profiles if max(r[kind] for r in p['rows'])>0]
        print(kind,len(good),'first',collections.Counter(next(r['tau'] for r in p['rows'] if r[kind]>0) for p in good),'max_threshold',collections.Counter(max(p['rows'],key=lambda r:r[kind])['tau'] for p in good))
    for rule in ['1','2','3','4','delta','delta+1','minposrho','minposrho+1']:
        get=lambda p: int(rule) if rule.isdigit() else p['b']-p['a']+(rule=='delta+1') if rule.startswith('delta') else min(r for r,q in zip(p['rho'],p['q']) if q)+(rule=='minposrho+1')
        print(rule,collections.Counter(next((r['exact']>0 for r in p['rows'] if r['tau']==get(p)),False) for p in profiles))
    (ROOT/'profiles812.json').write_text(json.dumps(profiles))
