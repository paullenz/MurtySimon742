from pathlib import Path
import hashlib
p=Path(__file__).parent
src=p/'project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/scan_q_crossing_stats.cpp'
s=src.read_text()
expected='7b07649c355028818ba2153dedf461eb001b92541a5d994a83967cf366757906'
actual=hashlib.sha256(src.read_bytes()).hexdigest()
if actual != expected: raise SystemExit(f'Frozen source hash mismatch: {actual}')
print('source sha256',actual)
insert=r'''
static ofstream interval_diag;
static void interval_probe(const State& st,const vector<int>& q,const vector<int>& rho,const OD& o,int E,bool hall_failure){
    int n=q.size(),maxq=*max_element(q.begin(),q.end());
    int Q=accumulate(q.begin(),q.end(),0),r=accumulate(rho.begin(),rho.end(),0);
    int D0=accumulate(st.s.begin(),st.s.end(),0)-r-2*st.t;
    if(D0<0||Q!=r+2*st.t+D0+E){cerr<<"INTERVAL_LEDGER_FAILURE\n";exit(90);}
    int G=n*(n-st.a-1)-(2*st.t+D0+E);
    if(G<0){cerr<<"INTERVAL_GLOBAL_BUDGET_FAILURE\n";exit(91);}
    int first=-1,best=-999,firstupper=-1,bestupper=-999,mismatches=0,uniform=0;
    for(int tau=1;tau<=maxq+1;++tau){
        int demand=0,H=0,U=0,N=0,low=0,loss=0;
        for(int u=0;u<n;++u)if(q[u]>=tau){demand+=q[u];++N;}else low+=q[u];
        for(int w=0;w<n;++w){
            int y=0,J=0;
            for(int u=0;u<n;++u)if(q[u]>=tau){
                if(o.D[u][w])++y;
                if(u!=w&&q[u]<=o.c[w]+1)++J;
            }
            H+=min(o.P[w],y);U+=min(o.P[w],J);
            loss+=rho[w]+n-st.a-1-min(o.P[w],J);
        }
        int exact=demand-H,lower=demand-U;
        if(lower!=loss-low-G||lower>exact){cerr<<"INTERVAL_IDENTITY_FAILURE\n";exit(92);}
        if(exact>0&&first<0)first=tau;
        if(lower>0&&firstupper<0)firstupper=tau;
        best=max(best,exact);bestupper=max(bestupper,lower);
        uniform+=exact;mismatches+=H!=U;
    }
    interval_diag<<st.layer<<'\t'<<st.id<<'\t'<<E<<'\t'<<D0<<'\t'<<st.t<<'\t'<<Q<<'\t'<<r<<'\t'<<G<<'\t'<<hall_failure<<'\t'<<first<<'\t'<<best<<'\t'<<firstupper<<'\t'<<bestupper<<'\t'<<mismatches<<'\t'<<uniform;
    for(auto* v:{&q,&rho,&o.P}){interval_diag<<'\t';for(int i=0;i<n;++i){if(i)interval_diag<<',';interval_diag<<(*v)[i];}}
    interval_diag<<'\n';
}
'''
anchor='struct Scanner {'
assert s.count(anchor)==1
s=s.replace(anchor,insert+'\n'+anchor)
anchor='        if(f<Q){\n            ++res.targethall_fail;'
assert s.count(anchor)==1
s=s.replace(anchor,'        interval_probe(st,q,rho,o,E,f<Q);\n'+anchor)
anchor='    ifstream in(argv[1]);ofstream out(argv[2]);'
assert s.count(anchor)==1
s=s.replace(anchor,'    if(argc<4)return 2; interval_diag.open(argv[3]); if(!interval_diag)return 2;\n    interval_diag<<"layer\\tstate\\tEsel\\tD0\\tt\\tQ\\tr\\tG\\thall_failure\\tfirst_exact\\tbest_exact\\tfirst_interval\\tbest_interval\\tthreshold_mismatches\\tuniform\\tq\\trho\\tP\\n";\n'+anchor)
(p/'scan_interval_probe.cpp').write_text(s)
