// Standalone outer-ledger checker: threshold-cut matching, generating-function
// domain counts, strict ordered-key uniqueness, and direct witness arithmetic.
// Imports no survey/column search source. Build with g++ -O3 -std=c++17 -lz.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
#include <zlib.h>
using V=std::vector<int>;using U=uint64_t;
int A,B,GAP,L;
void need(bool x,const char*s){if(!x)throw std::runtime_error(s);}
bool line(gzFile f,std::string&s){s.clear();char b[8192];while(gzgets(f,b,sizeof b)){s+=b;if(s.back()=='\n')return true;}return !s.empty();}
V nums(const std::string&s){V out;int value=0;bool active=false;for(char c:s){if(c>='0'&&c<='9'){value=10*value+c-'0';active=true;}else if(active){out.push_back(value);value=0;active=false;}}if(active)out.push_back(value);return out;}
U multiset_count(int slots,int total,int low,int high){
 if(total<0||high<low)return 0;
 std::vector<std::vector<U>>dp(slots+1,std::vector<U>(total+1));dp[0][0]=1;
 for(int v=low;v<=high;v++)for(int l=1;l<=slots;l++)for(int s=v;s<=total;s++)dp[l][s]+=dp[l-1][s-v];
 return dp[slots][total];
}
int match_bound(const V&labels,const V&supplies){
 int upper=std::min(labels.size(),supplies.size());
 for(int t=0;t<=2*A+1;t++){int cap=0;for(int x:labels)cap+=x<t;for(int x:supplies)cap+=x>=t;upper=std::min(upper,cap);}
 return upper;
}
V source_caps(const V&ds,const V&rs){
 std::map<int,int>types;
 for(int rb:rs)if(!types.count(rb)){
  V supply;bool used=false;for(int rw:rs){if(rw==rb&&!used){used=true;continue;}supply.push_back(rb+rw);}
  int best=0;for(int q=1;q<=A-rb;q++){V labels;for(int d:ds)if(d<rb+q)labels.push_back(d);if(match_bound(labels,supply)>=q)best=q;}
  types[rb]=best;
 }V c;for(int rb:rs)c.push_back(types[rb]);return c;
}
int main(int argc,char**argv){try{
 need(argc==5,"usage: check_survey n delta edges prefix");int n=std::stoi(argv[1]),edges=std::stoi(argv[3]);B=std::stoi(argv[2]);A=n-1-B;
 L=n*(n-1)/2-edges-A-B*(B-1)/2;GAP=A*(A-1)/2-L;need(GAP>0,"positive surplus required");
 std::map<std::pair<int,int>,U>expected,seen;
 for(int k=0;k<A;k++){
  if(k==0&&B>L-(A-1)*(A-2)/2)continue;
  if(k==1&&B>L-1-(A-2)*(A-3)/2)continue;
  int D=A-1-k;for(int r=B;r<=L-(A*k+1)/2;r++){
   U degree=multiset_count(A,2*(r+GAP),0,D)-multiset_count(A,2*(r+GAP),0,D-1);
   expected[{k,r}]=degree*multiset_count(B,r,1,A);seen[{k,r}]=0;
  }
 }
 std::string prefix=argv[4];gzFile input=gzopen((prefix+"_ledger.jsonl.gz").c_str(),"rb"),frontier=gzopen((prefix+"_frontier.jsonl.gz").c_str(),"rb");need(input&&frontier,"cannot open input");
 U total=0;std::array<U,5>counts{};V previous;std::string s;
 while(line(input,s)){
  V all=nums(s);need(int(all.size())>=A+B+4,"malformed record");
  int k=all[0],r=all[1],kind=all[2+A+B],D=A-1-k;
  V ds(all.begin()+2,all.begin()+2+A),rs(all.begin()+2+A,all.begin()+2+A+B),w(all.begin()+3+A+B,all.end());
  V key(all.begin(),all.begin()+2+A+B);need(previous.empty()||key>previous,"duplicate or unsorted key");previous=key;
  need(expected.count({k,r}),"out-of-domain band");
  need(std::is_sorted(ds.begin(),ds.end())&&ds.front()>=0&&ds.back()==D,"degree domain");
  need(std::accumulate(ds.begin(),ds.end(),0)==2*(r+GAP),"degree sum");
  need(std::is_sorted(rs.begin(),rs.end())&&rs.front()>=1&&rs.back()<=A,"residual domain");
  need(std::accumulate(rs.begin(),rs.end(),0)==r,"residual sum");
  need(kind>=0&&kind<=4,"bad kind");
  if(kind==0||kind==2){
   need(w.size()==3&&w[0]>=1&&w[0]<=D,"bad threshold witness");int j=w[0],high=0,lower=0,upper=0;
   for(int d:ds)if(d>=j){high++;lower+=d;}for(int rb:rs)lower-=std::min(high,rb);
   if(kind==0){for(int b=0;b<B;b++)for(int v=0;v<b;v++)upper+=rs[b]+rs[v]>=j;}
   else{V c=source_caps(ds,rs);std::map<int,int>cache;
    for(int b=0;b<B;b++){
     int rb=rs[b];if(cache.count(rb)){upper+=cache[rb];continue;}
     V labels,sup;for(int d:ds)if(d>=j&&d<rb+c[b])labels.push_back(d);
     for(int v=0;v<B;v++)if(v!=b)sup.push_back(rb+rs[v]);
     cache[rb]=std::min(c[b],match_bound(labels,sup));upper+=cache[rb];
    }
   }need(lower==w[1]&&upper==w[2]&&lower>upper,"invalid threshold rejection");
  }else if(kind==1){V c=source_caps(ds,rs);need(c==w,"recorded source caps mismatch");need(std::accumulate(c.begin(),c.end(),0)<r+2*GAP,"invalid source-total rejection");}
  else{
   int h=0;for(int j=1;j<=B;j++)if(rs[B-j]>=j)h=j;
   V lo;for(int d:ds)lo.push_back(std::max(0,d-h));int lower=std::accumulate(lo.begin(),lo.end(),0);
   if(kind==3)need(w==V({h,lower,r})&&lower>r,"invalid column lower bound");
   else{
    need(w==lo&&lower<=r,"invalid frontier lower bounds");std::string f;need(line(frontier,f),"missing frontier state");V fk=key;fk.insert(fk.end(),lo.begin(),lo.end());need(nums(f)==fk,"frontier coverage mismatch");
   }
  }
  seen[{k,r}]++;counts[kind]++;total++;
  if(total%1000000==0)std::cout<<"{\"verified_states\":"<<total<<"}"<<std::endl;
 }
 need(seen==expected,"finite-domain cardinality mismatch");need(!line(frontier,s),"extra frontier row");
 need(gzclose(input)==Z_OK&&gzclose(frontier)==Z_OK,"gzip integrity failure");
 std::string result="{\"status\":\"PASS\",\"n\":"+std::to_string(n)+",\"delta\":"+std::to_string(B)+",\"edges\":"+std::to_string(edges)+",\"states\":"+std::to_string(total)+",\"bands\":"+std::to_string(expected.size())+",\"counts\":[";
 for(int i=0;i<5;i++){if(i)result+=",";result+=std::to_string(counts[i]);}result+="],\"external_review\":false}";
 std::ofstream(prefix+"_outer_check.json")<<result<<"\n";std::cout<<result<<std::endl;
 }catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}return 0;}
