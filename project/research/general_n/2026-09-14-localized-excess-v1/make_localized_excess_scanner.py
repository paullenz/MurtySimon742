#!/usr/bin/env python3
"""Instrument a COPY of a relational scanner; never modify the canonical input.

IMPORTANT: paircap_fail/pass now include the additional localized-excess test.
A run must complete, cover its declared input and pass a separate audit before
any whole-state promotion. This generator alone certifies no exclusions.
"""
import argparse
from pathlib import Path
INSERT=r'''
// Candidate localized-excess cap. C_h=E+sum_{s<=h}s-sum_{rho<=h}q.
// For rho[u]>h: C_h >= k+(q[u]-k)*(p[u]-rho[u]+1) if p[u]>=rho[u].
static bool localize_excess_caps(const State&st,const vector<int>&q,
                                 const vector<int>&rho,int E,OD&o){
    vector<int>hs={0};hs.insert(hs.end(),rho.begin(),rho.end());
    sort(hs.begin(),hs.end());hs.erase(unique(hs.begin(),hs.end()),hs.end());
    for(int h:hs){
        int m=0,C=E;
        for(int s:st.s)if(s<=h){++m;C+=s;}
        for(int u=0;u<(int)q.size();++u)if(rho[u]<=h)C-=q[u];
        if(C<0)return false;
        for(int u=0;u<(int)q.size();++u)if(rho[u]>h&&q[u]>0){
            int k=min({m,q[u],C});
            if(k<q[u])o.P[u]=min(o.P[u],rho[u]-1+(C-k)/(q[u]-k));
        }
    }
    int sumP=0;
    for(int p:o.P){if(p<0)return false;sumP+=p;}
    return sumP>=accumulate(q.begin(),q.end(),0);
}
'''
def transform(text):
    point='static int pair_flow(const vector<int>&q,const OD&o){'
    target='if(!o.pass){++res.paircap_fail;return;}++res.paircap_pass;'
    if text.count(point)!=1 or text.count(target)!=1:
        raise ValueError('Scanner anchors changed; inspect rather than patching blindly.')
    text=text.replace(point,INSERT+'\n'+point)
    text=text.replace(target,'if(!o.pass || !localize_excess_caps(st,q,rho,E,o)){++res.paircap_fail;return;}++res.paircap_pass;')
    return '// EXPERIMENTAL LOCALIZED-EXCESS COPY. NOT A PROMOTED LEDGER.\n'+text
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);args=p.parse_args()
    if args.source.resolve()==args.output.resolve():p.error('Refusing to overwrite canonical source')
    args.output.write_text(transform(args.source.read_text()))
