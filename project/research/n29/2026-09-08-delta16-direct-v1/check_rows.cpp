// Independent N=29, Delta=16 residual-row checker: multiplicities/order statistics.
#include <array>
#include <algorithm>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdint>
using namespace std;using Row=array<int,16>;vector<Row>buckets[67];array<int,12>mult{};
void enumerate_counts(int value,int left,int remaining,int total){if(value==12){if(remaining!=12*left)return;mult[11]=left;Row row{};int at=0;for(int j=0;j<12;j++)for(int k=0;k<mult[j];k++)row[at++]=j+1;if(at!=16)throw 1;buckets[total].push_back(row);return;}for(int count=0;count<=left;count++){int rem=remaining-count*value,nleft=left-count;if(rem<(value+1)*nleft||rem>12*nleft)continue;mult[value-1]=count;enumerate_counts(value+1,nleft,rem,total);}}
int main(int argc,char**argv){if(argc!=5)return 2;int t=stoi(argv[4]);if(t!=2&&t!=3)return 2;ifstream f(argv[1]);ofstream output(argv[2]),bands(argv[3]);int N;if(!(f>>N)||!output||!bands)return 2;long long dp[17][67]{};dp[0][0]=1;for(int val=1;val<=12;val++)for(int number=1;number<=16;number++)for(int sum=val;sum<=66;sum++)dp[number][sum]+=dp[number-1][sum-val];for(int sum=16;sum<=66;sum++){enumerate_counts(1,16,sum,sum);sort(buckets[sum].begin(),buckets[sum].end());if((long long)buckets[sum].size()!=dp[16][sum])return 3;}
 uint64_t total=0,bound=0,first=0,second=0,kept=0,digest=14695981039346656037ULL;auto add=[&](int v){digest^=(uint64_t)v;digest*=1099511628211ULL;};
 for(int id=0;id<N;id++){array<int,12>s;int low,high;for(int&v:s)if(!(f>>v))return 4;if(!(f>>low>>high)||low<16||high>66||!is_sorted(s.begin(),s.end()))return 4;int lookup[13][13]{},need[13]{};for(int k=1;k<=12;k++){need[k]=need[k-1]+s[12-k];for(int r=1;r<=12;r++)for(int j=0;j<k;j++)lookup[k][r]+=(s[11-j]<=r);}uint64_t seen=0,saved=0;
  for(int sum=low;sum<=high;sum++)for(const Row&rho:buckets[sum]){total++;seen++;add(id);add(sum);for(int r:rho)add(r);if(sum>60-t){bound++;add(100);continue;}array<int,16>cap{},next{};for(int u=0;u<16;u++)cap[u]=min({12-rho[u],15,lookup[12][rho[u]]});auto failure=[&](){for(int k=1;k<=12;k++){int supplied=0;for(int u=0;u<16;u++)supplied+=min(cap[u],lookup[k][rho[u]]);if(supplied<need[k])return k;}return 0;};int bad=failure();if(bad){first++;add(bad);continue;}while(true){for(int u=0;u<16;u++){vector<int>supplier;for(int w=0;w<16;w++)if(u!=w)supplier.push_back(rho[w]+cap[w]);sort(supplier.begin(),supplier.end(),greater<int>());int best=0;for(int q=1;q<=cap[u]&&q<=15;q++)if(supplier[q-1]>=q-1)best=q;next[u]=best;}if(next==cap)break;cap=next;}bad=failure();if(bad){second++;add(20+bad);}else{kept++;saved++;add(0);output<<id<<' '<<sum;for(int r:rho)output<<' '<<r;output<<'\n';}}
  bands<<id<<' '<<seen<<' '<<saved<<'\n';}
 cout<<"{\"states\":"<<total<<",\"low_k_rejections\":"<<bound<<",\"initial_source_rejections\":"<<first<<",\"refined_source_rejections\":"<<second<<",\"survivors\":"<<kept<<",\"fnv64\":\""<<digest<<"\"}\n";
}
