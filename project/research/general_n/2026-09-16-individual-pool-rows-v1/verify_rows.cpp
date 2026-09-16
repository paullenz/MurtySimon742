// Ordered full pool compositions plus bounded-allocation DP.
// Checks an integer relaxation, not original diameter-two critical graphs.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
int main(){
  bool first=true;cout<<'[';
  for(int d=3;d<=10;++d)for(int z: {1,2}){
    int k0=1+z*(d-1),h0=(2*k0+d-3)/(d-2),best=d*h0;
    uint64_t feasible=0;set<vector<int>> winners;vector<int> by_h(h0+1,1000000000);
    for(int h=0;h<=h0;++h){int k=k0+h;
      for(int L=0;(d-1)*L<=d*h;++L){
        vector<int> u(d,0);
        function<void(int,int)> visit=[&](int t,int remaining){
          if(t<d-1){for(int x=0;x<=remaining;++x){u[t]=x;visit(t+1,remaining-x);}return;}
          u[t]=remaining;
          vector<int> dp(k+1,1000000000);dp[0]=0;
          for(int j=0;j<d;++j){
            int cap=h-L+u[j],price=max(0,d-1-z-u[j]);
            if(cap<0)return;
            vector<int> next(k+1,1000000000);
            for(int s=0;s<=k;++s)if(dp[s]<1000000000)
              for(int n=0;n<=cap && n+s<=k;++n)
                next[s+n]=min(next[s+n],dp[s]+n*price);
            dp.swap(next);
          }
          for(int n0=0;n0<=k;++n0)for(int N=0;N<=k-n0;++N){
            int n2=k-n0-N;
            if(N+2*n2>d*h-(d-1)*L || dp[N]==1000000000)continue;
            ++feasible;
            int val=d*h+(d-2)*L+(d-1)*n0+dp[N];
            by_h[h]=min(by_h[h],val);
            if(val<best){best=val;winners.clear();}
            if(val==best){
              auto sorted=u;sort(sorted.begin(),sorted.end());
              vector<int> key{h,L};key.insert(key.end(),sorted.begin(),sorted.end());
              key.insert(key.end(),{n0,N,n2});winners.insert(key);
            }
          }
        };
        visit(0,L);
      }
    }
    if(!first) { cout<<','; }
    first=false;
    cout<<"{\"d\":"<<d<<",\"z\":"<<z<<",\"h_cutoff\":"<<h0<<",\"minimum\":"<<best
        <<",\"ordered_pool_and_type_tuples\":"<<feasible<<",\"minima_by_h\":[";
    for(size_t i=0;i<by_h.size();++i){if(i)cout<<',';cout<<by_h[i];}
    cout<<"],\"minimizers\":[";bool firstkey=true;
    for(auto &key:winners){if(!firstkey)cout<<',';firstkey=false;cout<<'[';
      for(size_t i=0;i<key.size();++i){if(i)cout<<',';cout<<key[i];}cout<<']';}
    cout<<"]}";
  }
  cout<<"]\n";
}
