// Independent decision implementation: explicit adjacency matrices and paths.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using U=std::uint64_t; using Mat=std::vector<std::vector<bool>>;
bool path(const Mat&a,int u,int v){if(u==v||a[u][v])return true;for(int r=0;r<(int)a.size();++r)if(a[u][r]&&a[r][v])return true;return false;}
int main(){char type;U id;
 while(std::cin>>type>>id){
  if(type=='G'){
   int n,d,t,s;U km,vm;std::cin>>n>>d>>km>>vm>>t>>s;
   if(n<3||n>16||d>n||t>=d||s>=d)throw std::runtime_error("bad graph dimensions");
   Mat a(n,std::vector<bool>(n));for(int i=0;i<n;++i){U ns;std::cin>>ns;for(int j=0;j<n;++j)a[i][j]=(ns>>j)&1;}
   for(int i=0;i<n;++i){if(a[i][i])throw std::runtime_error("loop");for(int j=0;j<n;++j)if(a[i][j]!=a[j][i])throw std::runtime_error("asymmetry");}
   if(!a[t][s])throw std::runtime_error("deleted edge absent");
   bool pc=true,pp=true,threat=false;
   for(int i=0;i<d;++i)for(int j=i+1;j<d;++j){bool common=false;for(int k=d;k<n;++k)if((km>>k&1)&&a[i][k]&&a[j][k])common=true;pc=pc&&common;}
   for(int v=d;v<n;++v)if(vm>>v&1){int count=0,label=-1;for(int i=0;i<d;++i)if(a[v][i]){++count;label=i;}if(count!=1){pp=false;continue;}for(int k=d;k<n;++k)if((km>>k&1)&&a[label][k]&&!a[v][k])pp=false;}
   for(int x=d;x<n;++x)if(!(vm>>x&1))for(int side=0;side<2;++side){int u=side?s:t,v=side?t:s;if(!a[x][u]&&a[x][v]){int common=0;for(int r=0;r<d;++r)if(a[u][r]&&a[x][r])++common;if(common==1)threat=true;}}
   Mat before(n,std::vector<bool>(n));bool dia=true;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){before[i][j]=path(a,i,j);dia=dia&&before[i][j];}
   a[t][s]=a[s][t]=false;int count=0;std::string bits;
   for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){bool lost=before[i][j]&&!path(a,i,j);bits+=lost?'1':'0';count+=lost;}
   if(pc&&pp&&!threat&&count)throw std::runtime_error("local lemma counterexample");
   std::cout<<"G "<<id<<' '<<pc<<' '<<pp<<' '<<threat<<' '<<dia<<' '<<count<<' '<<bits<<'\n';
  }else if(type=='Q'){
   int d,charge;U q;std::cin>>d>>q>>charge;if(d<3||d>6)throw std::runtime_error("bad Q dimension");
   Mat a(d,std::vector<bool>(d));std::vector<std::pair<int,int>> edges;std::vector<int>degree(d);
   unsigned b=0;int ne=0;for(int i=0;i<d;++i)for(int j=i+1;j<d;++j,++b){edges.push_back({i,j});if(q>>b&1){a[i][j]=a[j][i]=true;++degree[i];++degree[j];++ne;}}
   int mu=(int)edges.size()-ne,g=0;for(int x:degree)g+=(x==d-1);
   std::vector<int>eh;int demand=(d-2)*std::max(0,g-1);
   for(int h=1;h<d;++h){int e=0;for(auto ij:edges)if(a[ij.first][ij.second]&&degree[ij.first]>=h+1&&degree[ij.second]>=h+1)++e;eh.push_back(e);demand=std::max(demand,(h*e+h)/(h+1));}
   if(eh[0]<(int)edges.size()-mu-(2*mu)/(d-2) || 2*mu+(eh[0]+1)/2<(d*(d-1)+3)/4)throw std::runtime_error("quadratic corollary failed");
   std::cout<<"Q "<<id<<' '<<mu<<' '<<g<<' '<<2*mu+demand;for(int e:eh)std::cout<<' '<<e;
   if(charge)for(U sup=1;sup<(U(1)<<d);++sup){int ell=0;for(int i=0;i<d;++i)ell+=(sup>>i&1);
    for(int h=1;h<d;++h){U mask=0;int count=0;
     for(unsigned z=0;z<edges.size();++z){int i=edges[z].first,j=edges[z].second;if(!a[i][j]||degree[i]<h+1||degree[j]<h+1)continue;
      for(int side=0;side<2;++side){int t=side?j:i,s=side?i:j;if(!(sup>>t&1)&&(sup>>s&1)){int hit=0;for(int r=0;r<d;++r)if((sup>>r&1)&&a[t][r])++hit;if(hit==1){mask|=U(1)<<z;++count;}}}}
     if(count>d-ell)throw std::runtime_error("outside-support charge failed");
     for(int w=d-1;w<=d;++w)if(w>=ell){int loss=w-ell;if((count&&loss<h)||count>loss+1)throw std::runtime_error("loss charge failed");}
     std::cout<<' '<<mask;
    }}
   std::cout<<'\n';
  }else throw std::runtime_error("bad record type");
  if(!std::cin)throw std::runtime_error("truncated input");
 }
 if(!std::cin.eof())throw std::runtime_error("input failure");
}
