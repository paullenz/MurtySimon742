// Exact integer outer-domain survey. No graph catalogue or theorem-status inference.
// Build: g++ -O3 -std=c++17 survey.cpp -lz -o survey
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <zlib.h>
using V=std::vector<int>;
int A,B,GAP,L;
std::vector<V> parts(int n,int total,int low,int high){
  std::vector<V> out;V cur;
  std::function<void(int,int,int)> f=[&](int left,int sum,int lo){
    if(!left){if(!sum)out.push_back(cur);return;}
    for(int x=lo;x<=high && x*left<=sum;x++){
      if(x+high*(left-1)<sum)continue;
      cur.push_back(x);f(left-1,sum-x,x);cur.pop_back();
    }
  };f(n,total,low);return out;
}
std::string arr(const V&v){std::string s="[";for(size_t i=0;i<v.size();i++){if(i)s+=",";s+=std::to_string(v[i]);}return s+"]";}
int matched(const V&labels,const V&supplies){
  size_t i=0;for(int s:supplies)if(i<labels.size() && labels[i]<=s)i++;return int(i);
}
bool match_q(const V&labels,const V&supplies,int q){
  if(q>int(labels.size())||q>int(supplies.size()))return false;
  for(int i=0;i<q;i++)if(labels[i]>supplies[supplies.size()-q+i])return false;
  return true;
}
V caps(const V&d,const V&rho){
  V c(B);std::array<int,64> cache;cache.fill(-1);
  for(int b=0;b<B;b++){
    int rb=rho[b];if(cache[rb]>=0){c[b]=cache[rb];continue;}
    V supplies;for(int w=0;w<B;w++)if(w!=b)supplies.push_back(rb+rho[w]);
    int best=0;
    for(int q=A-rb;q>=1;q--){V labels;for(int x:d)if(x<=rb+q-1)labels.push_back(x);
      if(match_q(labels,supplies,q)){best=q;break;}}
    cache[rb]=best;c[b]=best;
  }return c;
}
void put(gzFile f,const std::string&s){if(gzwrite(f,s.data(),unsigned(s.size()))!=int(s.size()))throw std::runtime_error("gzip write failed");}
int main(int argc,char**argv){
 try{
  if(argc!=5)throw std::runtime_error("usage: survey n delta edges output-prefix");
  int n=std::stoi(argv[1]),delta=std::stoi(argv[2]),edges=std::stoi(argv[3]);
  B=delta;A=n-1-B;L=n*(n-1)/2-edges-A-B*(B-1)/2;GAP=A*(A-1)/2-L;
  if(A<2||A>=63||B>=63||GAP<=0)throw std::runtime_error("unsupported domain or nonpositive surplus");
  std::string prefix=argv[4];gzFile ledger=gzopen((prefix+"_ledger.jsonl.gz").c_str(),"wb6");
  gzFile frontier=gzopen((prefix+"_frontier.jsonl.gz").c_str(),"wb6");
  if(!ledger||!frontier)throw std::runtime_error("cannot open output");
  std::ofstream summary(prefix+"_summary.jsonl");
  uint64_t total=0,leftover=0;
  for(int k=0;k<A;k++){
    if(k==0 && B>L-(A-1)*(A-2)/2)continue;
    if(k==1 && B>L-1-(A-2)*(A-3)/2)continue;
    int D=A-1-k;
    for(int r=B;r<=L-(A*k+1)/2;r++){
      std::array<uint64_t,5> count{};
      auto rhos=parts(B,r,1,A);auto degrees=parts(A,2*(r+GAP),0,D);
      for(const V&d:degrees){
        if(d.back()!=D)continue;
        std::array<int,64> num{},sum{};
        for(int j=1;j<=D;j++)for(int x:d)if(x>=j){num[j]++;sum[j]+=x;}
        std::string dtext=arr(d);
        for(const V&rho:rhos){
          int kind=4;V witness,c,minimum;
          for(int j=1;j<=D;j++){
            int lower=sum[j],upper=0;
            for(int x:rho)lower-=std::min(x,num[j]);
            for(int b=0;b<B;b++)for(int w=0;w<b;w++)upper+=rho[b]+rho[w]>=j;
            if(lower>upper){kind=0;witness={j,lower,upper};break;}
          }
          if(kind==4){
            c=caps(d,rho);int upper=0;for(int x:c)upper+=x;
            if(upper<r+2*GAP){kind=1;witness=c;}
          }
          if(kind==4){
            for(int j=1;j<=D;j++){
              int lower=sum[j],upper=0;for(int x:rho)lower-=std::min(x,num[j]);
              std::array<int,64> cache;cache.fill(-1);
              for(int b=0;b<B;b++){
                int rb=rho[b];if(cache[rb]>=0){upper+=cache[rb];continue;}
                V labels,supplies;for(int x:d)if(x>=j&&x<=rb+c[b]-1)labels.push_back(x);
                for(int w=0;w<B;w++)if(w!=b)supplies.push_back(rb+rho[w]);
                cache[rb]=std::min(c[b],matched(labels,supplies));upper+=cache[rb];
              }
              if(lower>upper){kind=2;witness={j,lower,upper};break;}
            }
          }
          if(kind==4){
            int h=0;for(int j=1;j<=A;j++){int num=0;for(int x:rho)num+=x>=j;if(num>=j)h=j;}
            int lower=0;for(int x:d){minimum.push_back(std::max(0,x-h));lower+=minimum.back();}
            if(lower>r){kind=3;witness={h,lower,r};}else witness=minimum;
          }
          count[kind]++;total++;
          std::string key="["+std::to_string(k)+","+std::to_string(r)+","+dtext+","+arr(rho);
          put(ledger,key+","+std::to_string(kind)+","+arr(witness)+"]\n");
          if(kind==4){leftover++;put(frontier,key+","+arr(minimum)+"]\n");}
        }
      }
      std::string row="{\"n\":"+std::to_string(n)+",\"delta\":"+std::to_string(delta)+",\"edges\":"+std::to_string(edges)+",\"k\":"+std::to_string(k)+",\"r\":"+std::to_string(r)+",\"counts\":[";
      for(int i=0;i<5;i++){if(i)row+=",";row+=std::to_string(count[i]);}row+="]}";
      summary<<row<<"\n";summary.flush();std::cout<<row<<std::endl;
    }
  }
  if(gzclose(ledger)!=Z_OK||gzclose(frontier)!=Z_OK)throw std::runtime_error("gzip close failed");
  std::cout<<"{\"completed\":true,\"states\":"<<total<<",\"frontier\":"<<leftover<<"}"<<std::endl;
 }catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}
}
