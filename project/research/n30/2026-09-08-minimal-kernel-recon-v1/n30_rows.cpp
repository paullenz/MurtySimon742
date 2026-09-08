// n=30, Delta=16 residual-row scanner derived from the audited n=29 minimal scanner.
// Uses only necessary source-capacity Hall cuts and monotone supplement-cap refinement.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
static constexpr int A=13,B=16,MAXR=78;
using Row=array<int,B>;
vector<Row> bucket[MAXR+1]; array<int,A> cnt{};

void gen_counts(int val,int left,int sum,int total){
 if(val==A){
  if(sum!=A*left)return;cnt[A-1]=left;Row r{};int p=0;
  for(int j=0;j<A;j++)for(int k=0;k<cnt[j];k++)r[p++]=j+1;
  if(p==B)bucket[total].push_back(r);return;
 }
 for(int n=0;n<=left;n++){
  int rem=sum-n*val,L=left-n;
  if(rem<(val+1)*L||rem>A*L)continue;
  cnt[val-1]=n;gen_counts(val+1,L,rem,total);
 }
}

int main(int argc,char**argv){
 if(argc!=4){cerr<<"n30_rows demands.txt survivors.txt bands.txt\n";return 2;}
 ifstream in(argv[1]);ofstream out(argv[2]),bands(argv[3]);int N;
 if(!(in>>N)||N<=0||!out||!bands)return 3;
 for(int r=B;r<=MAXR;r++){gen_counts(1,B,r,r);sort(bucket[r].begin(),bucket[r].end());}
 uint64_t states=0,initial=0,refined=0,surv=0;
 for(int id=0;id<N;id++){
  array<int,A>s;int lo,hi;for(int &x:s)if(!(in>>x))return 4;if(!(in>>lo>>hi))return 4;
  uint64_t seen=0,left=0;
  for(int total=lo;total<=hi;total++)for(const Row&rho:bucket[total]){
   states++;seen++;array<int,B> cap{},next{};
   for(int u=0;u<B;u++){
    int elig=0;for(int x:s)elig+=(x<=rho[u]);
    cap[u]=min(A-rho[u],elig);
   }
   auto violates=[&](){
    for(int k=1;k<=A;k++){
     int need=0;for(int j=A-k;j<A;j++)need+=s[j];
     int supply=0;
     for(int u=0;u<B;u++){
      int e=0;for(int j=A-k;j<A;j++)e+=(s[j]<=rho[u]);
      supply+=min(cap[u],e);
     }
     if(supply<need)return true;
    }
    return false;
   };
   if(violates()){initial++;continue;}
   for(;;){
    for(int u=0;u<B;u++){
     int best=0;
     for(int q=1;q<=cap[u];q++){
      int supporters=0;
      for(int w=0;w<B;w++)if(w!=u&&rho[w]+cap[w]>=q-1)supporters++;
      if(supporters>=q)best=q;
     }
     next[u]=best;
    }
    if(next==cap)break;cap=next;
   }
   if(violates()){refined++;continue;}
   surv++;left++;out<<id<<' '<<total;for(int x:rho)out<<' '<<x;out<<'\n';
  }
  bands<<id<<' '<<seen<<' '<<left<<'\n';
 }
 cout<<"{\"states\":"<<states<<",\"initial_source_rejections\":"<<initial<<",\"refined_source_rejections\":"<<refined<<",\"survivors\":"<<surv<<"}\n";
}
