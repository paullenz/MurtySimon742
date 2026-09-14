#!/usr/bin/env python3
"""Instrument the frozen q-crossing pilot with exact high-q-tail Hall statistics.

Run after the existing q-crossing scanner generator.  Canonical relational
screening decisions are unchanged.  On each exact target-Hall failure, this
adds the margins of source tails S_t={u:q_u>=t} and compares the best tail
with the exact Hall minimum f-Q.

Reconnaissance only: a miss is recorded, not converted into a workflow
failure or a promoted theorem.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_q_crossing_stats.cpp'
OUT=HERE/'scan_q_tail_stats.cpp'
s=SRC.read_text()

needle='struct Result {\n'
block=r'''static tuple<int,int,int> q_tail_stats(const vector<int>&q,const OD&o){
    int n=q.size(),maxq=0;
    for(int x:q)maxq=max(maxq,x);
    int best_margin=0,best_t=0,first_negative=0;
    for(int t=1;t<=maxq;++t){
        int demand=0;
        vector<unsigned char> selected(n,0);
        for(int u=0;u<n;++u)if(q[u]>=t){selected[u]=1;demand+=q[u];}
        if(demand==0)continue;
        int receiving=0;
        for(int w=0;w<n;++w){
            int incoming=0;
            for(int u=0;u<n;++u)if(selected[u]&&o.D[u][w])++incoming;
            receiving+=min(o.P[w],incoming);
        }
        int margin=receiving-demand;
        if(margin<0&&first_negative==0)first_negative=t;
        if(margin<best_margin){best_margin=margin;best_t=t;}
    }
    return {best_margin,best_t,first_negative};
}

'''
if s.count(needle)!=1:
    raise SystemExit('Result insertion point not unique')
s=s.replace(needle,block+needle,1)

old='''    long long qlayer_fail=0,qlayer_pass=0,qcross_zero=0,qcross_positive=0,qcross_sum=0; array<long long,10> qcross_hist{}; int qcross_max=0;\n'''
new=old+'''    long long qtail_detected=0,qtail_missed=0,qtail_exact=0,qtail_nonexact=0,qtail_gap_sum=0; int qtail_gap_max=0; array<long long,16> qtail_first_hist{},qtail_best_hist{};\n'''
if s.count(old)!=1:
    raise SystemExit('Result q-crossing counter point not unique')
s=s.replace(old,new,1)

old='''            ++res.targethall_fail;\n            auto [qflow,gcount]=canonical_antichain_stats(q,o,Q);\n'''
new='''            ++res.targethall_fail;\n            int exact_margin=f-Q;\n            auto [tail_margin,tail_best_t,tail_first_t]=q_tail_stats(q,o);\n            if(tail_margin<0)++res.qtail_detected;else ++res.qtail_missed;\n            if(tail_margin==exact_margin)++res.qtail_exact;else ++res.qtail_nonexact;\n            int tail_gap=tail_margin-exact_margin;\n            if(tail_gap<0){\n                cerr<<"QTAIL_BELOW_EXACT_MIN state="<<st.id<<" E="<<E\n                    <<" exact="<<exact_margin<<" tail="<<tail_margin<<"\\n";\n                exit(83);\n            }\n            res.qtail_gap_sum+=tail_gap;\n            res.qtail_gap_max=max(res.qtail_gap_max,tail_gap);\n            if(0<=tail_first_t&&tail_first_t<16)++res.qtail_first_hist[tail_first_t];\n            if(0<=tail_best_t&&tail_best_t<16)++res.qtail_best_hist[tail_best_t];\n            auto [qflow,gcount]=canonical_antichain_stats(q,o,Q);\n'''
if s.count(old)!=1:
    raise SystemExit('target-Hall failure insertion point not unique')
s=s.replace(old,new,1)

old='qcross_8\\tqcross_9plus\\tcost_fail'
new=('qcross_8\\tqcross_9plus\\tqtail_detected\\tqtail_missed\\tqtail_exact\\tqtail_nonexact'
     '\\tqtail_gap_sum\\tqtail_gap_max'
     +''.join(f'\\tqtail_first_t{i}' for i in range(1,16))
     +''.join(f'\\tqtail_best_t{i}' for i in range(1,16))
     +'\\tcost_fail')
if s.count(old)!=1:
    raise SystemExit('TSV header point not unique')
s=s.replace(old,new,1)

old="<<r.qcross_hist[9]<<'\\t'<<r.cost_fail<<'\\t'\n"
first=''.join(f"<<r.qtail_first_hist[{i}]<<'\\t'" for i in range(1,16))
best=''.join(f"<<r.qtail_best_hist[{i}]<<'\\t'" for i in range(1,16))
new=("<<r.qcross_hist[9]<<'\\t'<<r.qtail_detected<<'\\t'<<r.qtail_missed<<'\\t'"
     "<<r.qtail_exact<<'\\t'<<r.qtail_nonexact<<'\\t'<<r.qtail_gap_sum<<'\\t'<<r.qtail_gap_max<<'\\t'\n           "
     +first+"\n           "+best+"<<r.cost_fail<<'\\t'\n")
if s.count(old)!=1:
    raise SystemExit('TSV row point not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED q-tail statistics scanner; canonical decisions unchanged. */\n'+s)
print(OUT)
