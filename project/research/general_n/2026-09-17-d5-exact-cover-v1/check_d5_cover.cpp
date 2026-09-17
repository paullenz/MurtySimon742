#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<pair<int,int>> E; for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)E.push_back({i,j});
 int best=99; map<pair<int,int>,int> hist; map<string,int> types;
 for(int mask=0;mask<(1<<10);++mask){
  vector<int> qidx(10,-1); vector<pair<int,int>> Q; int deg[5]={};
  for(int b=0;b<10;b++)if(mask>>b&1){qidx[b]=Q.size();Q.push_back(E[b]);deg[E[b].first]++;deg[E[b].second]++;}
  int m=Q.size(), full=(1<<m)-1; vector<pair<int,int>> fam;
  for(int S=1;S<32;S++){
   int r=__builtin_popcount((unsigned)S), cost=(r==5?0:4-r), bm=0;
   for(int qi=0;qi<m;qi++){
    auto [i,j]=Q[qi]; bool threat=false;
    for(auto [t,s]: {pair<int,int>{i,j},pair<int,int>{j,i}}){
      if((S>>t&1)||!(S>>s&1)) continue;
      int cnt=0; for(int v=0;v<5;v++) if((S>>v&1) && v!=t){
        int a=min(t,v),b=max(t,v), bi=-1; for(int k=0;k<10;k++) if(E[k]==make_pair(a,b)){bi=k;break;}
        if(bi>=0 && (mask>>bi&1))cnt++;
      }
      if(cnt==1) threat=true;
    }
    if(threat) bm|=1<<qi;
   }
   if(bm)fam.push_back({bm,cost});
  }
  const int INF=99; vector<int> dp(1<<m,INF); dp[0]=0;
  for(int st=0;st<(1<<m);st++) if(dp[st]<INF) for(auto [bm,c]:fam) dp[st|bm]=min(dp[st|bm],dp[st]+c);
  int c=dp[full], mu=10-m, total=2*mu+c; best=min(best,total); hist[{mu,c}]++;
  sort(deg,deg+5); if(total==11){ string k=to_string(mu)+":"+to_string(c)+":"; for(int x:deg)k+=to_string(x);types[k]++; }
  cout<<mask<<' '<<mu<<' '<<c<<' '<<total; for(int x:deg)cout<<' '<<x; cout<<'\n';
 }
 cerr<<"best="<<best<<"\n"; for(auto &[k,v]:types)cerr<<k<<" "<<v<<"\n";
}
