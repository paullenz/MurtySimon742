// Integer subset DP, distinct from Python set-partition traversal.
// Necessary receiver-resource model only; no original graphs are enumerated.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <climits>
int main(){
 for(int p=1;p<=4;++p) for(int A=2;A<=6;++A) for(int lambda: {1,A,A+1})
  for(int flags=0;flags<(1<<(2*p));++flags){
   int n=2*p, size=1<<n;
   std::vector<int> cost(size,-1);
   for(int mask=1;mask<size;++mask){
    int seen=0,count=0,selected=0,core=0,reserve=0; bool valid=true;
    for(int i=0;i<n;++i)if(mask>>i&1){
     int group=1<<(i/2),bit=flags>>i&1,other=flags>>(i^1)&1;
     if(seen&group){valid=false;break;}
     seen|=group;++count;selected+=bit;core+=1-bit;
     reserve=std::max(reserve,A+bit-other);
    }
    if(!valid||(selected&&count>1))continue;
    int rho=std::max(core+reserve,selected?lambda:0);
    if(rho<=A+1)cost[mask]=rho-1;
   }
   std::vector<int> best(size,INT_MAX/4);
   std::vector<uint64_t> count(size,0),optimal(size,0);
   best[0]=0;count[0]=optimal[0]=1;
   for(int mask=1;mask<size;++mask){
    int first=mask&-mask;
    for(int block=mask;block;block=(block-1)&mask){
     if(!(block&first)||cost[block]<0)continue;
     int rest=mask^block;
     if(!count[rest])continue;
     count[mask]+=count[rest]; int val=cost[block]+best[rest];
     if(val<best[mask]){best[mask]=val;optimal[mask]=optimal[rest];}
     else if(val==best[mask])optimal[mask]+=optimal[rest];
    }
   }
   std::cout<<p<<' '<<A<<' '<<lambda<<' '<<flags<<' '<<best.back()<<' '
            <<count.back()<<' '<<optimal.back()<<'\n';
  }
}
