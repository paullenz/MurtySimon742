#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main(){
  vector<array<int,7>> perms;
  array<int,7> p={0,1,2,3,4,5,6};
  do { perms.push_back(p); } while(next_permutation(p.begin(),p.end()));
  vector<pair<int,int>> upairs;
  for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)upairs.push_back({i,j});
  int uidx[7][7]; for(int q=0;q<21;q++){auto [i,j]=upairs[q];uidx[i][j]=uidx[j][i]=q;}
  vector<array<int,21>> maps(perms.size());
  for(size_t z=0;z<perms.size();z++)for(int q=0;q<21;q++){
    auto [i,j]=upairs[q];int a=perms[z][i],b=perms[z][j];if(a>b)swap(a,b);
    maps[z][q]=uidx[a][b];
  }
  auto transform=[&](uint32_t m,size_t z){
    uint32_t x=0;while(m){int q=__builtin_ctz(m);m&=m-1;x|=1u<<maps[z][q];}return x;
  };
  vector<unsigned char> seen(1u<<21,0); long long unit_orbits=0,coloured=0,survivors=0;
  for(uint32_t um=0;um<(1u<<21);um++)if(!seen[um]){
    unit_orbits++;
    vector<size_t> aut;
    for(size_t z=0;z<perms.size();z++){
      uint32_t x=transform(um,z);seen[x]=1;if(x==um)aut.push_back(z);
    }
    array<unsigned char,128> hseen{};
    for(int hs=0;hs<128;hs++)if(!hseen[hs]){
      coloured++;
      for(size_t z:aut){
        int x=0;for(int i=0;i<7;i++)if(hs>>i&1)x|=1<<perms[z][i];hseen[x]=1;
      }
      vector<pair<int,int>> edges;
      for(int i=0;i<7;i++)if(hs>>i&1)edges.push_back({0,i+1});
      for(int q=0;q<21;q++)if(um>>q&1)edges.push_back({upairs[q].first+1,upairs[q].second+1});
      int R[8]={2,1,1,1,1,1,1,1},deg[8]={},adjR[8]={};bool adj[8][8]={};
      for(auto [i,j]:edges){deg[i]++;deg[j]++;adj[i][j]=adj[j][i]=1;adjR[i]+=R[j];adjR[j]+=R[i];}
      bool P[8];for(int i=0;i<8;i++)P[i]=deg[i]>R[i];
      bool ok=true;for(int i=0;i<8;i++)if(P[i]&&(deg[i]-R[i])*(deg[i]-R[i])>adjR[i])ok=false;
      if(!ok)continue;
      int eP=0,eN=0;for(auto [i,j]:edges){if(P[i]&&P[j])eP++;if(!P[i]&&!P[j])eN++;}
      int sumP=0,slack=0;for(int i=0;i<8;i++){if(P[i])sumP+=R[i];else if(i>0&&deg[i]==0)slack++;}
      int t=eP-eN-sumP-slack;if(t<=0)continue;
      uint32_t fm=0;int q=0;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++,q++)if(adj[i][j])fm|=1u<<q;
      survivors++;cout<<fm<<" "<<t;for(int i=0;i<8;i++)cout<<" "<<deg[i];cout<<"\n";
    }
  }
  cerr<<"unit_orbits="<<unit_orbits<<" coloured_orbits="<<coloured<<" strict_survivors="<<survivors<<"\n";
}
