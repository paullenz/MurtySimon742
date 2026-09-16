// Exhaust every n0,n1,n2 composition; unlike Python's n1 elimination.
// This verifies finite scalar relaxations, NOT original graphs.
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <cstdint>
int main(){
  std::vector<std::array<int,2>> domain;
  for(int d=3;d<=20;++d) for(int z=1;z<=std::min(d,4);++z) domain.push_back({d,z});
  for(int d=21;d<=50;++d) for(int z=1;z<=2;++z) domain.push_back({d,z});
  std::cout<<'['; bool first=true;
  for(auto [d,z]:domain){
    int k0=1+z*(d-1),h0=(2*k0+d-3)/(d-2),best=d*h0;
    std::uint64_t count=0; std::vector<std::array<int,5>> win;
    for(int h=0;h<=h0;++h) for(int L=0;(d-1)*L<=d*h;++L){
      int k=k0+h,q=d*h-(d-1)*L,price=std::max(0,d-1-z-L);
      for(int n0=0;n0<=k;++n0) for(int n1=0;n1<=k-n0;++n1){
        int n2=k-n0-n1;
        if(n1+2*n2>q) continue;
        ++count;
        int cost=d*h+(d-2)*L+(d-1)*n0+price*n1;
        if(cost<best){best=cost;win.clear();}
        if(cost==best) win.push_back({h,L,n0,n1,n2});
      }
    }
    if(!first) { std::cout<<','; }
    first=false;
    std::cout<<"{\"d\":"<<d<<",\"z\":"<<z<<",\"h_cutoff\":"<<h0<<",\"minimum\":"<<best
             <<",\"feasible_tuples\":"<<count<<",\"minimizers\":[";
    for(std::size_t i=0;i<win.size();++i){ if(i)std::cout<<','; std::cout<<'[';
      for(int j=0;j<5;++j){if(j)std::cout<<',';std::cout<<win[i][j];} std::cout<<']';}
    std::cout<<"]}";
  }
  std::cout<<"]\n";
}
