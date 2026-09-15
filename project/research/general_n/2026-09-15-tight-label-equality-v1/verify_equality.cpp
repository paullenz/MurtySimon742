#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
// Direct forced union reconstruction, not imported Python certificates.
int main(int argc,char**argv){
 if(argc!=2)return 2;ifstream in(argv[1]);int n;in>>n;
 cout<<"layer\tstate_id\tapplicable\trejected\n";
 for(int z=0;z<n;++z){
  string layer;int id,a,b,ns,nr;in>>layer>>id>>a>>b>>ns;
  vector<int>s(ns);for(int&x:s)in>>x;in>>nr;vector<int>r(nr);for(int&x:r)in>>x;
  bool applicable=false,reject=false;set<int>done;
  for(int seed=0;seed<ns;++seed){
   int d=s[seed];if(d<=0||done.count(d))continue;done.insert(d);
   vector<int>block,H,M,L;
   for(int i=0;i<ns;++i)if(s[i]==d)block.push_back(i);
   if((int)block.size()!=d)continue;
   for(int u=0;u<nr;++u){if(r[u]>=d)H.push_back(u);else if(r[u]+1==d)M.push_back(u);else L.push_back(u);}
   if((int)H.size()!=d||(int)M.size()!=d)continue;applicable=true;
   set<int>forced_union;
   for(int i=0;i<ns;++i){
    if(find(block.begin(),block.end(),i)!=block.end())continue;
    int remaining=s[i];for(int u:L)if(s[i]<=r[u])--remaining;
    if(remaining>0)forced_union.insert(i);
   }
   for(int u:H)if(forced_union.size()>(size_t)r[u])reject=true;
  }
  cout<<layer<<'\t'<<id<<'\t'<<applicable<<'\t'<<reject<<'\n';
 }
 return in?0:2;
}
