// Adapted for n=28 Delta=15 m=197: t=2, delta(C)>=1, r<=58.
// Separate arithmetic replay. Generates residual multisets by multiplicities,
// refines caps by sorted supplier order statistics, and recomputes every row.
#include <array>
#include <algorithm>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdint>
using namespace std;
using Row=array<int,15>;vector<Row> buckets[64];array<int,12> mult{};
void enumerate_counts(int value,int left,int remaining,int total){
 if(value==12){if(remaining!=12*left)return;mult[11]=left;Row row{};int at=0;for(int j=0;j<12;j++)for(int k=0;k<mult[j];k++)row[at++]=j+1;if(at!=15)throw 1;buckets[total].push_back(row);return;}
 for(int count=0;count<=left;count++){
  int rem=remaining-count*value,nleft=left-count;
  if(rem<(value+1)*nleft||rem>12*nleft)continue;
  mult[value-1]=count;enumerate_counts(value+1,nleft,rem,total);
 }
}
int main(int argc,char**argv){
 // Reviewer-release overlay: validate every input before opening outputs.
 // This is a fixed (a,b,t)=(12,15,2) helper, not a generic enumerator.
 if(argc!=4){cerr<<"usage: check_rows INPUT ROWS BANDS\n";return 2;}
 ifstream f(argv[1]);int N;
 if(!(f>>N)||N<1||N>1229){cerr<<"invalid record count\n";return 2;}
 struct Input { array<int,12> s; int low,high; };
 vector<Input> inputs; inputs.reserve(N);
 for(int id=0;id<N;id++){
  Input item{};
  for(int& v:item.s)if(!(f>>v)||v<0||v>=12){cerr<<"invalid demand\n";return 4;}
  if(!is_sorted(item.s.begin(),item.s.end())){cerr<<"unsorted demand\n";return 4;}
  if(!(f>>item.low>>item.high)||item.low<15||item.low>item.high||item.high>63){cerr<<"unsupported interval\n";return 4;}
  if(id>0 && !(inputs.back().s<item.s)){cerr<<"duplicate or unordered demand\n";return 4;}
  inputs.push_back(item);
 }
 string trailing;if(f>>trailing){cerr<<"trailing input\n";return 4;}
 if(!f.eof()){cerr<<"input read failure\n";return 4;}
 if(string(argv[1])==argv[2] || string(argv[1])==argv[3] || string(argv[2])==argv[3]){cerr<<"distinct paths required\n";return 2;}
 ofstream output(argv[2]),bands(argv[3]);if(!output||!bands){cerr<<"output open failure\n";return 2;}
 long long dp[16][64]{};dp[0][0]=1;
 for(int val=1;val<=12;val++)for(int number=1;number<=15;number++)for(int sum=val;sum<=63;sum++)dp[number][sum]+=dp[number-1][sum-val];
 for(int sum=15;sum<=63;sum++){enumerate_counts(1,15,sum,sum);sort(buckets[sum].begin(),buckets[sum].end());if((long long)buckets[sum].size()!=dp[15][sum])return 3;}
 uint64_t total=0,bound=0,first=0,second=0,kept=0,digest=14695981039346656037ULL;
 auto add=[&](int v){digest^=(uint64_t)v;digest*=1099511628211ULL;};
 for(int id=0;id<N;id++){
  const auto& s=inputs[id].s;int low=inputs[id].low,high=inputs[id].high;
  int lookup[13][13]{},need[13]{};
  for(int k=1;k<=12;k++){need[k]=need[k-1]+s[12-k];for(int r=1;r<=12;r++)for(int j=0;j<k;j++)lookup[k][r]+=(s[11-j]<=r);}
  uint64_t seen=0,saved=0;
  for(int sum=low;sum<=high;sum++)for(const Row&rho:buckets[sum]){
   total++;seen++;add(id);add(sum);for(int r:rho)add(r);
   if(sum>58){bound++;add(100);continue;}
   array<int,15>cap{},next{};for(int u=0;u<15;u++)cap[u]=min({12-rho[u],14,lookup[12][rho[u]]});
   auto failure=[&](){for(int k=1;k<=12;k++){int supplied=0;for(int u=0;u<15;u++)supplied+=min(cap[u],lookup[k][rho[u]]);if(supplied<need[k])return k;}return 0;};
   int bad=failure();if(bad){first++;add(bad);continue;}
   while(true){
    for(int u=0;u<15;u++){
     vector<int>supplier;for(int w=0;w<15;w++)if(u!=w)supplier.push_back(rho[w]+cap[w]);sort(supplier.begin(),supplier.end(),greater<int>());
     int best=0;for(int q=1;q<=cap[u]&&q<=14;q++)if(supplier[q-1]>=q-1)best=q;next[u]=best;
    }
    if(next==cap)break;cap=next;
   }
   bad=failure();if(bad){second++;add(20+bad);}else{kept++;saved++;add(0);output<<id<<' '<<sum;for(int r:rho)output<<' '<<r;output<<'\n';}
  }
  bands<<id<<' '<<seen<<' '<<saved<<'\n';
 }
 output.flush();bands.flush();if(!output||!bands){cerr<<"output write failure\n";return 5;}
 cout<<"{\"states\":"<<total<<",\"low_k_rejections\":"<<bound<<",\"initial_source_rejections\":"<<first<<",\"refined_source_rejections\":"<<second<<",\"survivors\":"<<kept<<",\"fnv64\":\""<<digest<<"\"}\n";
 return 0;
}
