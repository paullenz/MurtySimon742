// Fan-free fixed-order upper-range verifier for Murty-Simon n=25 and n=27.
// Exact integer necessary-condition enumeration; no use of Fan's bound.
// Reuses only graph lemmas already stated in the fixed-order manuscripts:
// residual activity, selected-pair threshold bound, source caps/thresholds,
// and residual-column h-index lower bound.
//
// Build: g++ -O3 -std=c++17 fan_free_outer.cpp -o fan_free_outer
// Run:   ./fan_free_outer n delta edges
#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using V=std::vector<int>;
int A,B,GAP,L;

std::vector<V> parts(int n,int total,int low,int high){
  std::vector<V> out; V cur;
  std::function<void(int,int,int)> f=[&](int left,int sum,int lo){
    if(!left){if(!sum)out.push_back(cur);return;}
    for(int x=lo;x<=high && x*left<=sum;x++){
      if(x+high*(left-1)<sum)continue;
      cur.push_back(x); f(left-1,sum-x,x); cur.pop_back();
    }
  }; f(n,total,low); return out;
}

int matched(const V&labels,const V&supplies){
  size_t i=0; for(int s:supplies) if(i<labels.size() && labels[i]<=s) i++; return int(i);
}
bool match_q(const V&labels,const V&supplies,int q){
  if(q>int(labels.size())||q>int(supplies.size()))return false;
  for(int i=0;i<q;i++) if(labels[i]>supplies[supplies.size()-q+i]) return false;
  return true;
}
V caps(const V&d,const V&rho){
  V c(B); std::array<int,64> cache; cache.fill(-1);
  for(int b=0;b<B;b++){
    int rb=rho[b]; if(cache[rb]>=0){c[b]=cache[rb];continue;}
    V supplies; for(int w=0;w<B;w++) if(w!=b) supplies.push_back(rb+rho[w]);
    std::sort(supplies.begin(),supplies.end());
    int best=0;
    for(int q=A-rb;q>=1;q--){
      V labels; for(int x:d) if(x<=rb+q-1) labels.push_back(x);
      if(match_q(labels,supplies,q)){best=q;break;}
    }
    cache[rb]=best; c[b]=best;
  }
  return c;
}

int main(int argc,char**argv){
 try{
  if(argc!=4) throw std::runtime_error("usage: fan_free_outer n delta edges");
  int n=std::stoi(argv[1]),delta=std::stoi(argv[2]),edges=std::stoi(argv[3]);
  B=delta; A=n-1-B;
  L=n*(n-1)/2-edges-A-B*(B-1)/2;
  GAP=A*(A-1)/2-L;
  if(A<2||A>=63||B>=63||GAP<=0) throw std::runtime_error("unsupported domain or nonpositive surplus");
  uint64_t total=0,frontier=0;
  std::array<uint64_t,5> dispositions{};
  for(int k=0;k<A;k++){
    // Small-k necessary inequalities from the residual-active proof.
    if(k==0 && B>L-(A-1)*(A-2)/2) continue;
    if(k==1 && B>L-1-(A-2)*(A-3)/2) continue;
    int D=A-1-k;
    for(int r=B;r<=L-(A*k+1)/2;r++){
      auto rhos=parts(B,r,1,A);
      auto degrees=parts(A,2*(r+GAP),0,D);
      for(const V&d:degrees){
        if(d.empty()||d.back()!=D) continue;
        std::array<int,64> num{},sum{};
        for(int j=1;j<=D;j++) for(int x:d) if(x>=j){num[j]++;sum[j]+=x;}
        for(const V&rho:rhos){
          int kind=4;
          // Selected incidences at high-degree labels inject into distinct
          // unordered missing B-pair slots satisfying rho_b+rho_w>=j.
          for(int j=1;j<=D;j++){
            int lower=sum[j],upper=0;
            for(int x:rho) lower-=std::min(x,num[j]);
            for(int b=0;b<B;b++) for(int w=0;w<b;w++) upper+=rho[b]+rho[w]>=j;
            if(lower>upper){kind=0;break;}
          }
          V c;
          if(kind==4){
            c=caps(d,rho); int upper=0; for(int x:c) upper+=x;
            if(upper<r+2*GAP) kind=1;
          }
          if(kind==4){
            for(int j=1;j<=D;j++){
              int lower=sum[j],upper=0; for(int x:rho) lower-=std::min(x,num[j]);
              std::array<int,64> cache; cache.fill(-1);
              for(int b=0;b<B;b++){
                int rb=rho[b]; if(cache[rb]>=0){upper+=cache[rb];continue;}
                V labels,supplies;
                for(int x:d) if(x>=j&&x<=rb+c[b]-1) labels.push_back(x);
                for(int w=0;w<B;w++) if(w!=b) supplies.push_back(rb+rho[w]);
                std::sort(supplies.begin(),supplies.end());
                cache[rb]=std::min(c[b],matched(labels,supplies)); upper+=cache[rb];
              }
              if(lower>upper){kind=2;break;}
            }
          }
          if(kind==4){
            int h=0; for(int j=1;j<=A;j++){int ct=0;for(int x:rho)ct+=x>=j;if(ct>=j)h=j;}
            int lower=0; for(int x:d) lower+=std::max(0,x-h);
            if(lower>r) kind=3;
          }
          dispositions[kind]++; total++; if(kind==4) frontier++;
        }
      }
    }
  }
  std::cout << "{\"n\":"<<n<<",\"delta\":"<<delta<<",\"edges\":"<<edges
            <<",\"a\":"<<A<<",\"b\":"<<B<<",\"L\":"<<L<<",\"t\":"<<GAP
            <<",\"states\":"<<total<<",\"dispositions\":["
            <<dispositions[0]<<","<<dispositions[1]<<","<<dispositions[2]<<","<<dispositions[3]<<","<<dispositions[4]
            <<"],\"frontier\":"<<frontier<<"}"<<std::endl;
  return frontier==0?0:2;
 }catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}
}
