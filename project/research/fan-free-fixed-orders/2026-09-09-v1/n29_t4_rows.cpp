// Fan-free n29 Delta16 t=4 residual-row scanner.
// Exact copy of the frozen minimal_rows.cpp mathematics with only the historical
// t in {2,3} CLI guard replaced by t==4.  The scanner's formulas do not otherwise
// use t; rmin/rmax are supplied by the audited t4 preparation wrapper.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std; using Row=array<int,16>;
vector<Row> bucket[67]; array<int,12> cnt{};
void gen_counts(int val,int left,int sum,int total){
 if(val==12){
  if(sum!=12*left)return;cnt[11]=left;Row r{};int p=0;
  for(int j=0;j<12;j++)for(int k=0;k<cnt[j];k++)r[p++]=j+1;
  if(p==16)bucket[total].push_back(r);return;
 }
 for(int n=0;n<=left;n++){
  int rem=sum-n*val,L=left-n;
  if(rem<(val+1)*L||rem>12*L)continue;
  cnt[val-1]=n;gen_counts(val+1,L,rem,total);
 }
}
int main(int argc,char**argv){
 if(argc!=5){cerr<<"n29_t4_rows demands.txt survivors.txt bands.txt t\n";return 2;}
 int t=stoi(argv[4]);if(t!=4)return 2;
 ifstream in(argv[1]);ofstream out(argv[2]),bands(argv[3]);int N;
 if(!(in>>N)||N<=0||!out||!bands)return 3;
 for(int r=16;r<=66;r++){gen_counts(1,16,r,r);sort(bucket[r].begin(),bucket[r].end());}
 uint64_t states=0,initial=0,refined=0,surv=0;
 for(int id=0;id<N;id++){
  array<int,12>s;int lo,hi;for(int &x:s)if(!(in>>x))return 4;if(!(in>>lo>>hi))return 4;
  uint64_t seen=0,left=0;
  for(int total=lo;total<=hi;total++)for(const Row&rho:bucket[total]){
   states++;seen++;array<int,16> cap{},next{};
   for(int u=0;u<16;u++){
    int elig=0;for(int x:s)elig+=(x<=rho[u]);
    cap[u]=min(12-rho[u],elig);
   }
   auto violates=[&](){
    for(int k=1;k<=12;k++){
     int need=0;for(int j=12-k;j<12;j++)need+=s[j];
     int supply=0;
     for(int u=0;u<16;u++){
      int e=0;for(int j=12-k;j<12;j++)e+=(s[j]<=rho[u]);
      supply+=min(cap[u],e);
     }
     if(supply<need)return true;
    }
    return false;
   };
   if(violates()){initial++;continue;}
   for(;;){
    for(int u=0;u<16;u++){
     int best=0;
     for(int q=1;q<=cap[u];q++){
      int supporters=0;
      for(int w=0;w<16;w++)if(w!=u&&rho[w]+cap[w]>=q-1)supporters++;
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
