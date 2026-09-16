// Independent distance implementation: explicit length-0/1/2 tests, not Python reach unions.
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using U=std::uint64_t;
bool close(const std::vector<U>& a,int x,int y) {
  if(x==y || ((a[x]>>y)&1)) return true;
  for(int z=0;z<(int)a.size();++z)
    if(((a[x]>>z)&1) && ((a[z]>>y)&1)) return true;
  return false;
}
int main(int argc,char**argv){
  if(argc!=2){std::cerr<<"usage: checker INPUT.tsv\n";return 2;}
  std::ifstream f(argv[1]);if(!f){std::cerr<<"input error\n";return 2;}
  std::string line;
  while(std::getline(f,line)){
    std::istringstream ss(line); std::string id;int d,n;ss>>id>>d>>n;
    if(!ss || n<1 || n>63 || d<2 || d>n){std::cerr<<"bad header\n";return 2;}
    std::vector<U>a(n);for(U&x:a)ss>>x;if(!ss){return 2;}
    std::vector<std::vector<bool>> before(n,std::vector<bool>(n));
    bool diam=true;for(int x=0;x<n;++x)for(int y=x+1;y<n;++y){
      before[x][y]=close(a,x,y);diam=diam&&before[x][y];
    }
    int edges=0,losing_edges=0,after_diam=0;long long lost_pairs=0;
    for(int s=0;s<d;++s)for(int t=s+1;t<d;++t)if((a[s]>>t)&1){
      ++edges; a[s]^=U(1)<<t;a[t]^=U(1)<<s;
      long long lost=0;bool all=true;
      for(int x=0;x<n;++x)for(int y=x+1;y<n;++y){
        bool now=close(a,x,y);all=all&&now;
        if(before[x][y]&&!now)++lost;
      }
      lost_pairs+=lost;losing_edges+=(lost>0);after_diam+=all;
      a[s]^=U(1)<<t;a[t]^=U(1)<<s;
    }
    std::cout<<id<<'\t'<<n<<'\t'<<d<<'\t'<<diam<<'\t'<<edges<<'\t'
       <<losing_edges<<'\t'<<lost_pairs<<'\t'<<after_diam<<'\n';
  }
}
