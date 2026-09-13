#!/usr/bin/env python3
"""Generate a low-demand scanner with an exact p-allocation class-packing fallback.

The audited incidence-capacity scanner remains the cheap first pass.  Only a
profile whose existing bound is still nonpositive is sent to the new fallback.
The fallback enumerates incoming p allocations subject to the same pointwise
caps and applies ENDPOINT_CLASS_PACKING.md to the zero-excess demand-two and
demand-three classes, together with the exact total endpoint budget.
"""
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_incidence_capacity_family.cpp"
OUT = HERE / "scan_class_packing.generated.cpp"
EXTRA = [
    (283, 3, 12, 5, 4, 9, 42, 40),
    (153, 5, 10, 7, 2, 9, 40, 38),
    (231, 4, 11, 5, 5, 8, 41, 39),
    (154, 5, 10, 6, 4, 8, 40, 38),
    (122, 6, 9, 7, 3, 8, 39, 37),
    (77, 7, 8, 7, 4, 7, 38, 36),
    (60, 8, 7, 7, 5, 6, 37, 35),
]

HELPER = r'''
struct PackSrc{int q,rho,cap;};

static long long endpoint_class_lb(const vector<PackSrc>&src,const vector<int>&p,int d,int z){
 if(z==0)return 0;
 vector<pair<int,int>> a;
 for(int i=0;i<(int)src.size();++i){
  if(src[i].q<=0||src[i].rho<d||p[i]>src[i].rho-1)continue;
  a.push_back({src[i].q+p[i],src[i].q});
 }
 long long tot=0;for(auto [w,q]:a)tot+=min(q,z);
 if(tot<1LL*d*z)return INF;
 long long lb=1LL*d*z;int mx=d;for(auto [w,q]:a)mx=max(mx,w);
 for(int lam=d+1;lam<=mx+1;++lam){
  int kmax=0;
  for(int k=1;k<=z;++k){long long c=0;for(auto [w,q]:a)if(w<lam)c+=min(q,k);if(1LL*d*k<=c)kmax=k;}
  lb+=z-kmax;
 }
 return lb;
}

static long long packed_source_objective(const State&st,const vector<int>&q2,const vector<int>&q3,
                                         const vector<int>&e2,const vector<int>&e3,int Q){
 vector<int>d2=e2,all=e2;all.insert(all.end(),e3.begin(),e3.end());
 sort(d2.begin(),d2.end(),greater<int>());sort(all.begin(),all.end(),greater<int>());
 vector<PackSrc> src;int freecap=0;bool bad=false;
 auto add=[&](int q,int rho){
  int cap=min(rho+2,17-q);
  if(q>0){const auto&v=(rho==2?d2:all);if(q>(int)v.size()){bad=true;return;}cap=min(cap,rho-1+v[q-1]);}
  cap=max(0,cap);if(q==0)freecap+=cap;else src.push_back({q,rho,cap});
 };
 for(int i=0;i<st.r1;++i)add(0,1);for(int q:q2)add(q,2);for(int q:q3)add(q,3);if(bad)return INF;
 int target=max(0,Q-freecap),U=0;for(auto s:src)U+=s.cap;if(target>U)return INF;
 int z2=0,z3=0;long long other=0;for(int e:e2){if(e==0)++z2;else other+=2+e;}for(int e:e3){if(e==0)++z3;else other+=3+e;}
 long long totalC=st.r+Q,best=INF;vector<int>p(src.size(),0),suf(src.size()+1,0);for(int i=(int)src.size()-1;i>=0;--i)suf[i]=suf[i+1]+src[i].cap;
 function<void(int,int,long long)> dfs=[&](int at,int rem,long long qp){
  if(qp>=best)return;if(rem<0||rem>suf[at])return;
  if(at==(int)src.size()){
   if(rem)return;long long l2=endpoint_class_lb(src,p,2,z2);if(l2==INF)return;long long l3=endpoint_class_lb(src,p,3,z3);if(l3==INF)return;
   if(l2+l3+other>totalC)return;best=min(best,qp+l2);return;
  }
  int hi=min(src[at].cap,rem);for(int x=0;x<=hi;++x){p[at]=x;dfs(at+1,rem-x,qp+1LL*src[at].q*x);}p[at]=0;
 };
 dfs(0,target,0);return best;
}

'''


def main():
    raw = SRC.read_text(); s = raw
    inc="#include <vector>\n"
    assert s.count(inc)==1
    s=s.replace(inc,inc+"#include <functional>\n",1)
    needle = " if(id==519)return {519,1,14,6,0,12,44,42};\n"
    assert s.count(needle) == 1
    addition = "".join(f" if(id=={sid})return {{{sid},{n2},{n3},{r1},{r2},{r3},{S},{r}}};\n" for sid,n2,n3,r1,r2,r3,S,r in EXTRA)
    s=s.replace(needle,needle+addition)
    marker="// Exact minimum of sum q_u p_u under the demand-compatible pointwise caps\n"
    assert s.count(marker)==1
    s=s.replace(marker,HELPER+marker)
    old="    if(gap<=0 && z==0){long long qp=threshold_qp_min(st,q2,q3,a2.q,a3.q,Q);if(qp==INF)continue;gap=sq+qp-base-corr;}\n    best=min(best,gap);"
    new="    if(gap<=0 && z==0){long long qp=threshold_qp_min(st,q2,q3,a2.q,a3.q,Q);if(qp==INF)continue;gap=sq+qp-base-corr;}\n    if(gap<=0){long long po=packed_source_objective(st,q2,q3,a2.q,a3.q,Q);if(po==INF)continue;gap=max(gap,sq+po-base-corr);}\n    best=min(best,gap);"
    assert s.count(old)==1
    s=s.replace(old,new)
    OUT.write_text(s)
    print("BASE_SHA256",hashlib.sha256(raw.encode()).hexdigest())
    print("GENERATED_SHA256",hashlib.sha256(s.encode()).hexdigest())
    print("FALLBACK","exact-p-endpoint-class-packing")

if __name__=="__main__":main()
