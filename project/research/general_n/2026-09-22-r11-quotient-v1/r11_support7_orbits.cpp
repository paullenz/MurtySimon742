#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
static uint64_t encode(const bool a[7][7],int n,const vector<int>&ord){uint64_t x=0;int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(a[ord[i]][ord[j]])x|=1ULL<<q;return x;}
static void decode(uint64_t g,int n,bool a[7][7]){fill(&a[0][0],&a[0][0]+49,false);int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(g>>q&1)a[i][j]=a[j][i]=true;}
static vector<vector<int>> blocks(const bool a[7][7],int n){vector<pair<int,int>>v;for(int i=0;i<n;i++){int d=0;for(int j=0;j<n;j++)d+=a[i][j];v.push_back({d,i});}sort(v.begin(),v.end());vector<vector<int>>b;for(auto z:v){if(b.empty()||v.empty())b.push_back({z.second});else{int j=b.back()[0],dj=0;for(int x=0;x<n;x++)dj+=a[j][x];if(z.first==dj)b.back().push_back(z.second);else b.push_back({z.second});}}return b;}
static void rec(const vector<vector<int>>&b,int z,vector<int>&cur,const bool a[7][7],int n,uint64_t&best,vector<vector<int>>*auts,uint64_t orig){if(z==(int)b.size()){uint64_t x=encode(a,n,cur);best=min(best,x);if(auts&&x==orig)auts->push_back(cur);return;}auto p=b[z];do{size_t q=cur.size();cur.insert(cur.end(),p.begin(),p.end());rec(b,z+1,cur,a,n,best,auts,orig);cur.resize(q);}while(next_permutation(p.begin(),p.end()));}
static uint64_t canon(const bool a[7][7],int n){auto b=blocks(a,n);vector<int>c;uint64_t best=~0ULL;rec(b,0,c,a,n,best,nullptr,0);return best;}
static vector<vector<int>> auts(uint64_t g,int n){bool a[7][7];decode(g,n,a);auto b=blocks(a,n);vector<int>c;uint64_t best=~0ULL;vector<vector<int>>v;rec(b,0,c,a,n,best,&v,g);return v;}
static int codeR(const array<int,7>&R){int x=0,m=1;for(int i=0;i<7;i++){x+=m*R[i];m*=6;}return x;}
int main(){
 vector<uint64_t>reps={0};for(int n=1;n<7;n++){unordered_set<uint64_t>next;bool a[7][7],old[7][7];for(auto g:reps)for(int s=0;s<(1<<n);s++){decode(g,n,old);fill(&a[0][0],&a[0][0]+49,false);for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=old[i][j];for(int i=0;i<n;i++)if(s>>i&1)a[i][n]=a[n][i]=true;next.insert(canon(a,n+1));}reps.assign(next.begin(),next.end());sort(reps.begin(),reps.end());}
 cerr<<"unlabelled7="<<reps.size()<<"\n";
 const array<array<int,7>,5> parts={{{5,1,1,1,1,1,1},{4,2,1,1,1,1,1},{3,3,1,1,1,1,1},{3,2,2,1,1,1,1},{2,2,2,2,1,1,1}}};
 for(int ci=0;ci<5;ci++){
  long long coloured=0,surv=0;bool a[7][7];
  for(auto g:reps){decode(g,7,a);auto av=auts(g,7);array<int,7>R=parts[ci];sort(R.begin(),R.end());unordered_set<int>seen;
   do{int rc=codeR(R);if(seen.count(rc))continue;coloured++;for(auto&o:av){array<int,7>X;for(int i=0;i<7;i++)X[i]=R[o[i]];seen.insert(codeR(X));}
    int deg[7]={},adjR[7]={};vector<pair<int,int>>edges;int q=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++,q++)if(g>>q&1){edges.push_back({i,j});deg[i]++;deg[j]++;adjR[i]+=R[j];adjR[j]+=R[i];}
    bool P[7];bool ok=true;for(int i=0;i<7;i++){P[i]=deg[i]>R[i];if(P[i]&&(deg[i]-R[i])*(deg[i]-R[i])>adjR[i])ok=false;}if(!ok)continue;
    int eP=0,eN=0;for(auto [i,j]:edges){if(P[i]&&P[j])eP++;if(!P[i]&&!P[j])eN++;}int sumP=0,slack=0;for(int i=0;i<7;i++){if(P[i])sumP+=R[i];else if(R[i]==1&&deg[i]==0)slack++;}
    int t=eP-eN-sumP-slack;if(t<=0)continue;surv++;cout<<ci<<" "<<g<<" "<<t;for(int x:R)cout<<" "<<x;for(int x:deg)cout<<" "<<x;cout<<"\n";
   }while(next_permutation(R.begin(),R.end()));
  }
  cerr<<"case="<<ci<<" coloured="<<coloured<<" strict="<<surv<<"\n";
 }
}
