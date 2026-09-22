#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;

static uint64_t encode(const bool a[8][8], int n, const vector<int>& ord){
  uint64_t x=0; int q=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)
    if(a[ord[i]][ord[j]]) x|=1ULL<<q;
  return x;
}
static void decode(uint64_t g,int n,bool a[8][8]){
  fill(&a[0][0],&a[0][0]+64,false); int q=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,q++)if(g>>q&1)a[i][j]=a[j][i]=true;
}
static void orders_rec(const vector<vector<int>>& blocks,int b,vector<int>& cur,
                       const bool a[8][8],int n,uint64_t& best,vector<vector<int>>* autos,uint64_t original){
  if(b==(int)blocks.size()){
    uint64_t x=encode(a,n,cur); if(x<best)best=x;
    if(autos && x==original)autos->push_back(cur);
    return;
  }
  vector<int> p=blocks[b];
  do{
    size_t z=cur.size();cur.insert(cur.end(),p.begin(),p.end());
    orders_rec(blocks,b+1,cur,a,n,best,autos,original);cur.resize(z);
  }while(next_permutation(p.begin(),p.end()));
}
static vector<vector<int>> degree_blocks(const bool a[8][8],int n){
  vector<pair<int,int>> v;
  for(int i=0;i<n;i++){int d=0;for(int j=0;j<n;j++)d+=a[i][j];v.push_back({d,i});}
  sort(v.begin(),v.end());vector<vector<int>> blocks;
  for(auto [d,i]:v){if(blocks.empty()){blocks.push_back({i});continue;}
    int j=blocks.back()[0],dj=0;for(int z=0;z<n;z++)dj+=a[j][z];
    if(d==dj)blocks.back().push_back(i);else blocks.push_back({i});
  }
  return blocks;
}
static uint64_t canon(const bool a[8][8],int n){
  auto blocks=degree_blocks(a,n);vector<int> cur;uint64_t best=~0ULL;
  orders_rec(blocks,0,cur,a,n,best,nullptr,0);return best;
}
static vector<vector<int>> automorphisms(uint64_t g,int n){
  bool a[8][8];decode(g,n,a);auto blocks=degree_blocks(a,n);vector<int> cur,autos_dummy;
  vector<vector<int>> autos;uint64_t best=~0ULL;
  orders_rec(blocks,0,cur,a,n,best,&autos,g);return autos;
}
int main(){
  vector<uint64_t> reps={0};
  for(int n=1;n<8;n++){
    unordered_set<uint64_t> next; bool a[8][8];
    for(uint64_t g:reps)for(int s=0;s<(1<<n);s++){
      decode(g,n+1,a);
      // decode above leaves vertex n isolated while preserving old edge bit positions
      // only because old pairs occupy the same prefix in lexicographic pair order is false;
      // rebuild old adjacency explicitly before adding the new vertex.
      bool old[8][8];decode(g,n,old);fill(&a[0][0],&a[0][0]+64,false);
      for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=old[i][j];
      for(int i=0;i<n;i++)if(s>>i&1)a[i][n]=a[n][i]=true;
      next.insert(canon(a,n+1));
    }
    reps.assign(next.begin(),next.end());sort(reps.begin(),reps.end());
    cerr<<"n="<<n+1<<" unlabeled="<<reps.size()<<"\n";
  }
  long long coloured=0,survivors=0; bool uadj[8][8];
  for(uint64_t ug:reps){
    decode(ug,8,uadj);auto aut=automorphisms(ug,8);array<unsigned char,256> seen{};
    for(int hs=0;hs<256;hs++)if(!seen[hs]){
      coloured++;
      for(auto &ord:aut){int x=0;for(int i=0;i<8;i++)if(hs>>ord[i]&1)x|=1<<i;seen[x]=1;}
      bool adj[9][9]={};vector<pair<int,int>> edges;
      for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)if(uadj[i][j])edges.push_back({i+1,j+1});
      for(int i=0;i<8;i++)if(hs>>i&1)edges.push_back({0,i+1});
      int R[9]={2,1,1,1,1,1,1,1,1},deg[9]={},adjR[9]={};
      for(auto [i,j]:edges){adj[i][j]=adj[j][i]=true;deg[i]++;deg[j]++;adjR[i]+=R[j];adjR[j]+=R[i];}
      bool P[9];for(int i=0;i<9;i++)P[i]=deg[i]>R[i];
      bool ok=true;for(int i=0;i<9;i++)if(P[i]&&(deg[i]-R[i])*(deg[i]-R[i])>adjR[i])ok=false;
      if(!ok)continue;
      int eP=0,eN=0;for(auto [i,j]:edges){if(P[i]&&P[j])eP++;if(!P[i]&&!P[j])eN++;}
      int sumP=0,slack=0;for(int i=0;i<9;i++){if(P[i])sumP+=R[i];else if(i>0&&deg[i]==0)slack++;}
      int t=eP-eN-sumP-slack;if(t<=0)continue;
      survivors++;cout<<ug<<" "<<hs<<" "<<t;for(int i=0;i<9;i++)cout<<" "<<deg[i];cout<<"\n";
    }
  }
  cerr<<"unit_graphs="<<reps.size()<<" rooted_orbits="<<coloured<<" strict_survivors="<<survivors<<"\n";
}
