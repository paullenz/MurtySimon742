#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<pair<int,int>> E;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)E.push_back({i,j});
 map<string,int> types; int d11=0; bool allsing=true;
 for(int mask=0;mask<(1<<10);++mask){
  vector<pair<int,int>>Q;int deg[5]={};
  for(int b=0;b<10;b++)if(mask>>b&1){Q.push_back(E[b]);deg[E[b].first]++;deg[E[b].second]++;}
  int m=Q.size(),full=(1<<m)-1; struct F{int bm,c,s;};vector<F>fam;
  for(int S=1;S<32;S++){
   int r=__builtin_popcount((unsigned)S),c=(r==5?0:4-r),sing=(r==1),bm=0;
   for(int qi=0;qi<m;qi++){
    auto [i,j]=Q[qi];bool th=false;
    for(auto pr:{pair<int,int>{i,j},pair<int,int>{j,i}}){
     int t=pr.first,s=pr.second;if((S>>t&1)||!(S>>s&1))continue;
     int cnt=0;
     for(int v=0;v<5;v++)if(S>>v&1){
      int a=min(t,v),b=max(t,v),bi=-1;
      for(int k=0;k<10;k++)if(E[k]==make_pair(a,b)){bi=k;break;}
      if(bi>=0&&(mask>>bi&1))cnt++;
     }
     if(cnt==1){th=true;break;}
    }
    if(th)bm|=1<<qi;
   }
   if(bm)fam.push_back({bm,c,sing});
  }
  pair<int,int> INF={99,99};vector<pair<int,int>>dp(1<<m,INF);dp[0]={0,0};
  for(int st=0;st<(1<<m);st++)if(dp[st]!=INF)for(auto f:fam){
   int ns=st|f.bm;pair<int,int>cand={dp[st].first+f.c,dp[st].second+f.s};
   if(cand<dp[ns])dp[ns]=cand;
  }
  int tau=dp[full].first,mins=dp[full].second,mu=10-m,total=2*mu+tau;
  sort(deg,deg+5);
  if(total==11){d11++;allsing=allsing&&(mins>=1);string k=to_string(mu)+":"+to_string(tau)+":"+to_string(mins)+":";for(int x:deg){k+=to_string(x);}types[k]++;}
  cout<<mask<<' '<<mu<<' '<<tau<<' '<<mins<<' '<<total;for(int x:deg)cout<<' '<<x;cout<<'\n';
 }
 cerr<<"d11="<<d11<<" all_require_singleton="<<allsing<<"\n";for(auto &[k,v]:types)cerr<<k<<" "<<v<<"\n";
}
