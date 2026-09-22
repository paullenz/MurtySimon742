#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
static uint64_t enc(const bool a[9][9],int n,const vector<int>&o){uint64_t x=0;int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(a[o[i]][o[j]])x|=1ULL<<q;return x;}
static void dec(uint64_t g,int n,bool a[9][9]){fill(&a[0][0],&a[0][0]+81,false);int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(g>>q&1)a[i][j]=a[j][i]=true;}
static vector<vector<int>> bl(const bool a[9][9],int n){vector<pair<int,int>>v;for(int i=0;i<n;i++){int d=0;for(int j=0;j<n;j++)d+=a[i][j];v.push_back({d,i});}sort(v.begin(),v.end());vector<vector<int>>b;int last=-1;for(auto [d,i]:v){if(b.empty()||d!=last)b.push_back({i});else b.back().push_back(i);last=d;}return b;}
static void rr(const vector<vector<int>>&b,int z,vector<int>&c,const bool a[9][9],int n,uint64_t&best,vector<vector<int>>*av,uint64_t orig){if(z==(int)b.size()){uint64_t x=enc(a,n,c);best=min(best,x);if(av&&x==orig)av->push_back(c);return;}auto p=b[z];do{auto s=c.size();c.insert(c.end(),p.begin(),p.end());rr(b,z+1,c,a,n,best,av,orig);c.resize(s);}while(next_permutation(p.begin(),p.end()));}
static uint64_t canon(const bool a[9][9],int n){auto b=bl(a,n);vector<int>c;uint64_t best=~0ULL;rr(b,0,c,a,n,best,nullptr,0);return best;}
static vector<vector<int>> aut(uint64_t g,int n){bool a[9][9];dec(g,n,a);auto b=bl(a,n);vector<int>c;uint64_t best=~0ULL;vector<vector<int>>v;rr(b,0,c,a,n,best,&v,g);return v;}
static int rcode(const array<int,9>&R){int x=0,m=1;for(int r:R){x+=m*r;m*=6;}return x;}
int main(){
 vector<uint64_t>reps={0};for(int n=1;n<9;n++){unordered_set<uint64_t>nx;bool a[9][9],old[9][9];for(auto g:reps)for(int s=0;s<(1<<n);s++){dec(g,n,old);fill(&a[0][0],&a[0][0]+81,false);for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=old[i][j];for(int i=0;i<n;i++)if(s>>i&1)a[i][n]=a[n][i]=true;nx.insert(canon(a,n+1));}reps.assign(nx.begin(),nx.end());sort(reps.begin(),reps.end());cerr<<"unlabelled"<<n+1<<"="<<reps.size()<<"\n";}
 const array<array<int,9>,3>parts={{{4,1,1,1,1,1,1,1,1},{3,2,1,1,1,1,1,1,1},{2,2,2,1,1,1,1,1,1}}};
 for(int ci=0;ci<3;ci++){long long coloured=0,surv=0;bool a[9][9];
  for(auto g:reps){dec(g,9,a);auto av=aut(g,9);array<int,9>R=parts[ci];sort(R.begin(),R.end());unordered_set<int>seen;
   do{int rc=rcode(R);if(seen.count(rc))continue;coloured++;for(auto&o:av){array<int,9>X;for(int i=0;i<9;i++)X[i]=R[o[i]];seen.insert(rcode(X));}
    int deg[9]={},adjR[9]={};vector<pair<int,int>>edges;int q=0;for(int i=0;i<9;i++)for(int j=i+1;j<9;j++,q++)if(g>>q&1){edges.push_back({i,j});deg[i]++;deg[j]++;adjR[i]+=R[j];adjR[j]+=R[i];}
    bool P[9],ok=true;for(int i=0;i<9;i++){P[i]=deg[i]>R[i];if(P[i]&&(deg[i]-R[i])*(deg[i]-R[i])>adjR[i])ok=false;}if(!ok)continue;
    int eP=0,eN=0;for(auto [i,j]:edges){if(P[i]&&P[j])eP++;if(!P[i]&&!P[j])eN++;}int sumP=0,slack=0;for(int i=0;i<9;i++){if(P[i])sumP+=R[i];else if(R[i]==1&&deg[i]==0)slack++;}int t=eP-eN-sumP-slack;if(t<=0)continue;
    surv++;cout<<ci<<" "<<g<<" "<<t;for(int x:R)cout<<" "<<x;for(int x:deg)cout<<" "<<x;cout<<"\n";
   }while(next_permutation(R.begin(),R.end()));
  }cerr<<"case="<<ci<<" coloured="<<coloured<<" strict="<<surv<<"\n";
 }
}

