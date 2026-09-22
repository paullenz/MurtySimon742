#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
static uint64_t enc(const bool a[9][9],int n,const vector<int>&o){uint64_t x=0;int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(a[o[i]][o[j]])x|=1ULL<<q;return x;}
static void dec(uint64_t g,int n,bool a[9][9]){fill(&a[0][0],&a[0][0]+81,false);int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(g>>q&1)a[i][j]=a[j][i]=true;}
static vector<vector<int>> blocks(const bool a[9][9],int n){vector<pair<int,int>>v;for(int i=0;i<n;i++){int d=0;for(int j=0;j<n;j++)d+=a[i][j];v.push_back({d,i});}sort(v.begin(),v.end());vector<vector<int>>b;int last=-1;for(auto [d,i]:v){if(b.empty()||d!=last)b.push_back({i});else b.back().push_back(i);last=d;}return b;}
static void relabels(const vector<vector<int>>&b,int z,vector<int>&c,const bool a[9][9],int n,uint64_t&best,vector<vector<int>>*av,uint64_t orig){if(z==(int)b.size()){uint64_t x=enc(a,n,c);best=min(best,x);if(av&&x==orig)av->push_back(c);return;}auto p=b[z];do{auto s=c.size();c.insert(c.end(),p.begin(),p.end());relabels(b,z+1,c,a,n,best,av,orig);c.resize(s);}while(next_permutation(p.begin(),p.end()));}
static uint64_t canon(const bool a[9][9],int n){auto b=blocks(a,n);vector<int>c;uint64_t best=~0ULL;relabels(b,0,c,a,n,best,nullptr,0);return best;}
static vector<vector<int>> aut(uint64_t g,int n){bool a[9][9];dec(g,n,a);auto b=blocks(a,n);vector<int>c;uint64_t best=~0ULL;vector<vector<int>>v;relabels(b,0,c,a,n,best,&v,g);return v;}
int main(){
 vector<uint64_t>reps={0};
 for(int n=1;n<9;n++){unordered_set<uint64_t>nx;bool a[9][9],old[9][9];for(auto g:reps)for(int s=0;s<(1<<n);s++){dec(g,n,old);fill(&a[0][0],&a[0][0]+81,false);for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=old[i][j];for(int i=0;i<n;i++)if(s>>i&1)a[i][n]=a[n][i]=true;nx.insert(canon(a,n+1));}reps.assign(nx.begin(),nx.end());sort(reps.begin(),reps.end());}
 long long maxdeg2=0,coloured=0,strict=0;bool a[9][9];
 for(auto g:reps){
  dec(g,9,a);int internal[9]={};bool ok=true;for(int i=0;i<9;i++){for(int j=0;j<9;j++)internal[i]+=a[i][j];if(internal[i]>2)ok=false;}if(!ok)continue;maxdeg2++;
  auto av=aut(g,9);unordered_set<int>seen;
  for(int s=0;s<512;s++){
   if(popcount((unsigned)s)>4||seen.count(s))continue;
   coloured++;for(auto&o:av){int x=0;for(int i=0;i<9;i++)if(s>>o[i]&1)x|=1<<i;seen.insert(x);}
   int degree[10]={};degree[0]=popcount((unsigned)s);for(int i=0;i<9;i++)degree[i+1]=internal[i]+((s>>i)&1);
   bool P[10],valid=true;P[0]=degree[0]>2;if(P[0]&&(degree[0]-2)*(degree[0]-2)>degree[0])valid=false;
   for(int i=0;i<9;i++){P[i+1]=degree[i+1]>1;int adjR=internal[i]+(((s>>i)&1)?2:0);if(P[i+1]&&(degree[i+1]-1)*(degree[i+1]-1)>adjR)valid=false;}
   if(!valid)continue;
   int eP=0,eN=0,eUnit=0;for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)if(a[i][j]){eUnit++;if(P[i+1]&&P[j+1])eP++;if(!P[i+1]&&!P[j+1])eN++;}
   for(int i=0;i<9;i++)if(s>>i&1){if(P[0]&&P[i+1])eP++;if(!P[0]&&!P[i+1])eN++;}
   int sumP=P[0]?2:0,slack=0;for(int i=0;i<9;i++){if(P[i+1])sumP++;else if(degree[i+1]==0)slack++;}
   int t=eP-eN-sumP-slack;if(t<=0)continue;
   strict++;cout<<g<<" "<<s<<" "<<t;cout<<" 2";for(int i=0;i<9;i++)cout<<" 1";for(int i=0;i<10;i++)cout<<" "<<degree[i];cout<<"\n";
  }
 }
 cerr<<"unlabelled9="<<reps.size()<<" maxdeg2_unit_cores="<<maxdeg2<<" coloured="<<coloured<<" strict="<<strict<<"\n";
}
