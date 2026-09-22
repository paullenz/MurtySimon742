#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 vector<array<int,6>> perms;array<int,6> p={0,1,2,3,4,5};
 do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 vector<pair<int,int>> up;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)up.push_back({i,j});
 int idx[6][6];for(int q=0;q<15;q++){auto [i,j]=up[q];idx[i][j]=idx[j][i]=q;}
 vector<array<int,15>> maps(perms.size());
 for(size_t z=0;z<perms.size();z++)for(int q=0;q<15;q++){auto [i,j]=up[q];int a=perms[z][i],b=perms[z][j];if(a>b)swap(a,b);maps[z][q]=idx[a][b];}
 auto utrans=[&](uint32_t m,size_t z){uint32_t x=0;while(m){int q=__builtin_ctz(m);m&=m-1;x|=1u<<maps[z][q];}return x;};
 vector<unsigned char> useen(1u<<15);long long uorbits=0,coloured=0,survivors=0;
 for(uint32_t um=0;um<(1u<<15);um++)if(!useen[um]){
  uorbits++;vector<size_t> aut;for(size_t z=0;z<perms.size();z++){auto x=utrans(um,z);useen[x]=1;if(x==um)aut.push_back(z);}
  array<unsigned char,8192> seen{};
  for(int cfg=0;cfg<8192;cfg++)if(!seen[cfg]){
   coloured++;
   for(size_t z:aut)for(int sw=0;sw<2;sw++){
    int x=cfg&1;
    for(int h=0;h<2;h++)for(int i=0;i<6;i++)if(cfg>>(1+6*h+i)&1){
      int hh=sw?1-h:h;x|=1<<(1+6*hh+perms[z][i]);
    }seen[x]=1;
   }
   bool adj[8][8]={};vector<pair<int,int>> edges;
   if(cfg&1)edges.push_back({0,1});
   for(int h=0;h<2;h++)for(int i=0;i<6;i++)if(cfg>>(1+6*h+i)&1)edges.push_back({h,i+2});
   for(int q=0;q<15;q++)if(um>>q&1)edges.push_back({up[q].first+2,up[q].second+2});
   int R[8]={2,2,1,1,1,1,1,1},deg[8]={},adjR[8]={};
   for(auto [i,j]:edges){adj[i][j]=adj[j][i]=1;deg[i]++;deg[j]++;adjR[i]+=R[j];adjR[j]+=R[i];}
   bool P[8];for(int i=0;i<8;i++)P[i]=deg[i]>R[i];
   bool ok=true;for(int i=0;i<8;i++)if(P[i]&&(deg[i]-R[i])*(deg[i]-R[i])>adjR[i])ok=false;if(!ok)continue;
   int eP=0,eN=0;for(auto [i,j]:edges){if(P[i]&&P[j])eP++;if(!P[i]&&!P[j])eN++;}
   int sumP=0,slack=0;for(int i=0;i<8;i++){if(P[i])sumP+=R[i];else if(i>=2&&deg[i]==0)slack++;}
   int t=eP-eN-sumP-slack;if(t<=0)continue;
   uint32_t fm=0;int q=0;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++,q++)if(adj[i][j])fm|=1u<<q;
   survivors++;cout<<fm<<" "<<t;for(int i=0;i<8;i++)cout<<" "<<deg[i];cout<<"\n";
  }
 }
 cerr<<"unit_orbits="<<uorbits<<" coloured_orbits="<<coloured<<" strict_survivors="<<survivors<<"\n";
}
