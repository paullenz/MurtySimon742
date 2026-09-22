#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
static uint32_t enc(const bool a[8][8],int n,const vector<int>&o){uint32_t x=0;int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(a[o[i]][o[j]])x|=1U<<q;return x;}
static void dec(uint32_t g,int n,bool a[8][8]){fill(&a[0][0],&a[0][0]+64,false);int q=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(g>>q&1)a[i][j]=a[j][i]=true;}
static vector<vector<int>> blocks(const bool a[8][8],int n){vector<pair<int,int>>v;for(int i=0;i<n;i++){int d=0;for(int j=0;j<n;j++)d+=a[i][j];v.push_back({d,i});}sort(v.begin(),v.end());vector<vector<int>>b;int last=-1;for(auto [d,i]:v){if(b.empty()||d!=last)b.push_back({i});else b.back().push_back(i);last=d;}return b;}
static void relabels(const vector<vector<int>>&b,int z,vector<int>&c,const bool a[8][8],int n,uint32_t&best,vector<vector<int>>*av,uint32_t orig){if(z==(int)b.size()){uint32_t x=enc(a,n,c);best=min(best,x);if(av&&x==orig)av->push_back(c);return;}auto p=b[z];do{auto s=c.size();c.insert(c.end(),p.begin(),p.end());relabels(b,z+1,c,a,n,best,av,orig);c.resize(s);}while(next_permutation(p.begin(),p.end()));}
static uint32_t canon(const bool a[8][8],int n){auto b=blocks(a,n);vector<int>c;uint32_t best=~0U;relabels(b,0,c,a,n,best,nullptr,0);return best;}
static vector<vector<int>> aut(uint32_t g,int n){bool a[8][8];dec(g,n,a);auto b=blocks(a,n);vector<int>c;uint32_t best=~0U;vector<vector<int>>v;relabels(b,0,c,a,n,best,&v,g);return v;}
static int perm_mask(int s,const vector<int>&o){int x=0;for(int i=0;i<8;i++)if(s>>o[i]&1)x|=1<<i;return x;}
int main(){
 vector<uint32_t>reps={0};for(int n=1;n<8;n++){unordered_set<uint32_t>nx;bool a[8][8],old[8][8];for(auto g:reps)for(int s=0;s<(1<<n);s++){dec(g,n,old);fill(&a[0][0],&a[0][0]+64,false);for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=old[i][j];for(int i=0;i<n;i++)if(s>>i&1)a[i][n]=a[n][i]=true;nx.insert(canon(a,n+1));}reps.assign(nx.begin(),nx.end());sort(reps.begin(),reps.end());}
 long long maxdeg2=0,coloured=0,strict=0;bool u[8][8];
 for(auto g:reps){dec(g,8,u);int in[8]={};bool ok=true;for(int i=0;i<8;i++){for(int j=0;j<8;j++)in[i]+=u[i][j];if(in[i]>2)ok=false;}if(!ok)continue;maxdeg2++;auto av=aut(g,8);
  unordered_set<uint32_t>seen;
  for(int e=0;e<=1;e++)for(int a=0;a<256;a++)for(int b=0;b<256;b++){
   if(popcount((unsigned)a)+e>4||popcount((unsigned)b)+e>4)continue;
   uint32_t key=(e<<16)|(a<<8)|b;if(seen.count(key))continue;uint32_t best=key;
   for(auto&o:av){int x=perm_mask(a,o),y=perm_mask(b,o);best=min(best,(uint32_t)((e<<16)|(x<<8)|y));best=min(best,(uint32_t)((e<<16)|(y<<8)|x));}
   seen.insert(best);if(key!=best)continue;coloured++;
   int d[10]={};d[0]=popcount((unsigned)a)+e;d[1]=popcount((unsigned)b)+e;for(int i=0;i<8;i++)d[i+2]=in[i]+((a>>i)&1)+((b>>i)&1);
   bool P[10],valid=true;for(int h=0;h<2;h++){P[h]=d[h]>2;int adj=popcount((unsigned)(h?a:b))+2*e;if(P[h]&&(d[h]-2)*(d[h]-2)>adj)valid=false;}
   for(int i=0;i<8;i++){P[i+2]=d[i+2]>1;int adj=in[i]+2*((a>>i)&1)+2*((b>>i)&1);if(P[i+2]&&(d[i+2]-1)*(d[i+2]-1)>adj)valid=false;}if(!valid)continue;
   int eP=0,eN=0;if(e){if(P[0]&&P[1])eP++;if(!P[0]&&!P[1])eN++;}
   for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)if(u[i][j]){if(P[i+2]&&P[j+2])eP++;if(!P[i+2]&&!P[j+2])eN++;}
   for(int i=0;i<8;i++){if(a>>i&1){if(P[0]&&P[i+2])eP++;if(!P[0]&&!P[i+2])eN++;}if(b>>i&1){if(P[1]&&P[i+2])eP++;if(!P[1]&&!P[i+2])eN++;}}
   int sumP=(P[0]?2:0)+(P[1]?2:0),slack=0;for(int i=0;i<8;i++){if(P[i+2])sumP++;else if(d[i+2]==0)slack++;}
   int t=eP-eN-sumP-slack;if(t<=0)continue;strict++;cout<<g<<" "<<e<<" "<<a<<" "<<b<<" "<<t<<" 2 2";for(int i=0;i<8;i++)cout<<" 1";for(int i=0;i<10;i++)cout<<" "<<d[i];cout<<"\n";
  }
 }
 cerr<<"unlabelled8="<<reps.size()<<" maxdeg2_unit_cores="<<maxdeg2<<" coloured="<<coloured<<" strict="<<strict<<"\n";
}

