// N=29, Delta=16 residual-row scan; adaptation of direct197 v8.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std; using Row=array<int,16>;
vector<Row> rows[67]; Row cur;
void gen(int pos,int low,int rem,int total){if(pos==16){if(rem==0)rows[total].push_back(cur);return;}for(int v=low;v<=12&&v*(16-pos)<=rem;v++){if(rem-v>12*(15-pos))continue;cur[pos]=v;gen(pos+1,v,rem-v,total);}}
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage: scan_rows input survivors bands t\n";return 2;}int t=stoi(argv[4]);if(t!=2&&t!=3)return 2;
 ifstream in(argv[1]);ofstream out(argv[2]),summary(argv[3]);int nd;if(!(in>>nd)||nd<=0||!out||!summary)return 2;
 for(int r=16;r<=66;r++)gen(0,1,r,r);uint64_t all=0,initialrej=0,refinedrej=0,boundrej=0,surv=0,fnv=14695981039346656037ULL;auto hash=[&](int z){fnv^=(uint64_t)z;fnv*=1099511628211ULL;};
 for(int id=0;id<nd;id++){array<int,12>s;int lo,hi;for(int&v:s)if(!(in>>v))return 3;if(!(in>>lo>>hi)||lo<16||hi>66||!is_sorted(s.begin(),s.end()))return 3;int elig[13][13]{},dem[13]{};for(int k=1;k<=12;k++){dem[k]=dem[k-1]+s[12-k];for(int j=1;j<=12;j++)elig[k][j]=elig[k-1][j]+(s[12-k]<=j);}uint64_t seen=0,left=0;
  for(int r=lo;r<=hi;r++)for(const auto&rho:rows[r]){all++;seen++;hash(id);hash(r);for(int z:rho)hash(z);if(r>60-t){boundrej++;hash(100);continue;}int c[16],nc[16];for(int u=0;u<16;u++)c[u]=min(12-rho[u],elig[12][rho[u]]);auto violation=[&](){for(int k=1;k<=12;k++){int cap=0;for(int u=0;u<16;u++)cap+=min(c[u],elig[k][rho[u]]);if(dem[k]>cap)return k;}return 0;};int reject=violation();if(reject){initialrej++;hash(reject);continue;}bool change=true;while(change){change=false;for(int u=0;u<16;u++){int q=c[u];while(q){int cnt=0;for(int w=0;w<16;w++)if(u!=w&&rho[w]+c[w]>=q-1)cnt++;if(cnt>=q)break;q--;}nc[u]=q;if(nc[u]!=c[u])change=true;}copy(nc,nc+16,c);}reject=violation();if(reject){refinedrej++;hash(20+reject);}else{surv++;left++;hash(0);out<<id<<' '<<r;for(int z:rho)out<<' '<<z;out<<'\n';}}
  summary<<id<<' '<<seen<<' '<<left<<'\n';}
 cout<<"{\"states\":"<<all<<",\"low_k_rejections\":"<<boundrej<<",\"initial_source_rejections\":"<<initialrej<<",\"refined_source_rejections\":"<<refinedrej<<",\"survivors\":"<<surv<<",\"fnv64\":\""<<fnv<<"\"}\n";
}
