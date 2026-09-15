#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
// Independently reconstruct the forced-label block and each receiver's missing
// label possibilities, rather than importing Python threshold certificates.
int main(int argc,char**argv){
 if(argc!=2)return 2; ifstream in(argv[1]); int n;in>>n;
 cout<<"layer\tstate_id\trejected\n";
 for(int z=0;z<n;++z){
  string layer;int id,a,b,ns,nr;in>>layer>>id>>a>>b>>ns;
  vector<int>s(ns);for(int&x:s)in>>x;in>>nr;vector<int>r(nr);for(int&x:r)in>>x;
  bool reject=false;set<int>done;
  for(int label=0;label<ns;++label){
   int demand=s[label];if(demand==0||done.count(demand))continue;done.insert(demand);
   vector<int>src,block;
   for(int u=0;u<nr;++u)if(r[u]>=demand)src.push_back(u);
   if((int)src.size()!=demand)continue;
   for(int i=0;i<ns;++i)if(s[i]==demand)block.push_back(i);
   int receivers=0,capacity=0;
   for(int v=0;v<nr;++v){
    if(find(src.begin(),src.end(),v)!=src.end())continue;
    bool possible=false;
    for(int omitted:block){
     int must_be_residual=0;
     for(int i:block)if(i!=omitted&&s[i]>r[v])++must_be_residual;
     if(must_be_residual<=r[v])possible=true;
    }
    if(possible){++receivers;capacity+=min((int)src.size(),max(0,r[v]+b-a-1));}
   }
   if(receivers<(int)block.size()||capacity<(int)(src.size()*block.size()))reject=true;
  }
  cout<<layer<<'\t'<<id<<'\t'<<reject<<'\n';
 }
 return in?0:2;
}
