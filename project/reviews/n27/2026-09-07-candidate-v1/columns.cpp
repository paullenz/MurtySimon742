// Canonical residual-column scan and certificate replay.
// Build: g++ -O3 -std=c++17 columns.cpp -lz -lcrypto -o columns
// "scan" uses sorted matching and max flow to find cuts.
// "check" rederives caps with threshold cuts and checks recorded inequalities;
// it never invokes max flow. Both enumerate one representative for permutations
// of R within equal d groups, and check orbit counts by independent dynamic programming.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <zlib.h>
#include <openssl/evp.h>
using V=std::vector<int>;using U=uint64_t;
int A,B;bool checking;
void need(bool x,const char*s){if(!x)throw std::runtime_error(s);}
std::string arr(const V&v){std::string s="[";for(size_t i=0;i<v.size();i++){if(i)s+=",";s+=std::to_string(v[i]);}return s+"]";}
V nums(const std::string&s){V a;int value=0;bool active=false;for(char c:s){if(c>='0'&&c<='9'){active=true;value=10*value+c-'0';}else if(active){a.push_back(value);value=0;active=false;}}if(active)a.push_back(value);return a;}
bool line(gzFile f,std::string&s){s.clear();char b[8192];while(gzgets(f,b,sizeof b)){s+=b;if(s.back()=='\n')return true;}return !s.empty();}
void put(gzFile f,const std::string&s){need(gzwrite(f,s.data(),unsigned(s.size()))==int(s.size()),"gzip write failed");}
struct Hash{EVP_MD_CTX*c;Hash(){c=EVP_MD_CTX_new();need(c&&EVP_DigestInit_ex(c,EVP_sha256(),nullptr),"hash init");}~Hash(){EVP_MD_CTX_free(c);}void add(const std::string&s){need(EVP_DigestUpdate(c,s.data(),s.size()),"hash update");}std::string end(){unsigned char b[32];unsigned n;need(EVP_DigestFinal_ex(c,b,&n)&&n==32,"hash end");std::string s;for(int i=0;i<32;i++){s+="0123456789abcdef"[b[i]>>4];s+="0123456789abcdef"[b[i]&15];}return s;}};
struct Flow{
 struct E{int v,rev,cap;};std::vector<std::vector<E>>g;V level,at;
 Flow(int n):g(n),level(n),at(n){}
 void edge(int u,int v,int c){int a=g[u].size(),b=g[v].size();g[u].push_back({v,b,c});g[v].push_back({u,a,0});}
 bool bfs(int s,int t){std::fill(level.begin(),level.end(),-1);std::queue<int>q;q.push(s);level[s]=0;while(!q.empty()){int u=q.front();q.pop();for(auto&e:g[u])if(e.cap&&level[e.v]<0){level[e.v]=level[u]+1;q.push(e.v);}}return level[t]>=0;}
 int dfs(int u,int t,int f){if(u==t)return f;for(int&i=at[u];i<int(g[u].size());i++){auto&e=g[u][i];if(e.cap&&level[e.v]==level[u]+1){int sent=dfs(e.v,t,std::min(f,e.cap));if(sent){e.cap-=sent;g[e.v][e.rev].cap+=sent;return sent;}}}return 0;}
 int run(int s,int t){int ans=0;while(bfs(s,t)){std::fill(at.begin(),at.end(),0);while(int f=dfs(s,t,1000000))ans+=f;}return ans;}
};
struct Caps{
 const V&d;const V&rho;std::vector<V>sup;std::vector<V>cache;
 Caps(const V&dd,const V&rr):d(dd),rho(rr),sup(A+1),cache(A+1){for(int rb:rho)if(cache[rb].empty()){cache[rb].assign(1<<A,-1);bool removed=false;for(int rw:rho){if(!removed&&rw==rb){removed=true;continue;}sup[rb].push_back(rb+rw);}}}
 int get(int rb,int mask){int&cached=cache[rb][mask];if(cached>=0)return cached;
  for(int q=A-rb;q>=1;q--){V labels;for(int i=0;i<A;i++)if((mask&(1<<i))&&d[i]<=rb+q-1)labels.push_back(d[i]);
   if(q>int(labels.size())||q>int(sup[rb].size()))continue;bool ok=true;
   if(!checking){for(int j=0;j<q;j++)if(labels[j]>sup[rb][sup[rb].size()-q+j]){ok=false;break;}}
   else {int m=std::min(labels.size(),sup[rb].size());for(int t=0;t<=2*A+1;t++){int c=0;for(int x:labels)c+=x<t;for(int x:sup[rb])c+=x>=t;m=std::min(m,c);}ok=m>=q;}
   if(ok)return cached=q;
  }return cached=0;
 }
 V operator()(const V&R){V answer;for(int rb:rho){int mask=0;for(int i=0;i<A;i++)if(d[i]<=rb+R[i])mask|=1<<i;answer.push_back(get(rb,mask));}return answer;}
};
U canonical_count(const V&d,const V&lo,int total){
 std::map<std::tuple<int,int,int>,U>memo;
 std::function<U(int,int,int)> f=[&](int i,int left,int prev)->U{
  if(i==A)return left==0;if(left<0)return 0;
  auto key=std::make_tuple(i,left,prev);auto it=memo.find(key);if(it!=memo.end())return it->second;
  int low=std::max(lo[i],i&&d[i]==d[i-1]?prev:0);U ans=0;
  for(int x=low;x<=B&&x<=left;x++)ans+=f(i+1,left-x,x);
  return memo[key]=ans;
 };return f(0,total,0);
}
U labelled_count(const V&lo,int total){std::vector<U>p(total+1),q(total+1);p[0]=1;for(int m:lo){std::fill(q.begin(),q.end(),0);for(int s=0;s<=total;s++)for(int x=m;x<=B&&s+x<=total;x++)q[s+x]+=p[s];p.swap(q);}return p[total];}
U weight(const V&d,const V&R,const std::vector<U>&fact){U ans=1;for(int i=0;i<A;){int j=i;while(j<A&&d[j]==d[i])j++;U w=fact[j-i];for(int p=i;p<j;){int q=p;while(q<j&&R[q]==R[p])q++;w/=fact[q-p];p=q;}ans*=w;i=j;}return ans;}
int main(int argc,char**argv){try{
 need(argc==8,"usage: columns scan|check n delta edges frontier.gz certificate-prefix output-prefix");
 checking=std::string(argv[1])=="check";need(checking||std::string(argv[1])=="scan","bad mode");
 int n=std::stoi(argv[2]),edges=std::stoi(argv[4]);B=std::stoi(argv[3]);A=n-1-B;
 need(A>0&&A<20&&B>0,"unsupported dimensions");
 std::string certprefix=argv[6],outprefix=argv[7];
 gzFile input=gzopen(argv[5],"rb"),certs=gzopen((certprefix+"_cuts.jsonl.gz").c_str(),checking?"rb":"wb6");
 need(input&&certs,"cannot open input/certificates");
 gzFile survivors=checking?nullptr:gzopen((outprefix+"_survivors.jsonl.gz").c_str(),"wb6");
 need(checking||survivors,"cannot open survivors");
 std::ofstream details(outprefix+"_columns.jsonl");
 std::vector<U>fact(A+1,1);for(int i=1;i<=A;i++)fact[i]=fact[i-1]*i;
 U state=0,columns=0,labelled=0,flowchecks=0,surviving=0;std::string s;
 std::map<std::string,std::pair<U,U>>domaincounts;
 Hash whole;
 while(line(input,s)){
  V values=nums(s);need(int(values.size())==2+2*A+B,"malformed frontier");
  int k=values[0],r=values[1];V d(values.begin()+2,values.begin()+2+A),rho(values.begin()+2+A,values.begin()+2+A+B),lo(values.end()-A,values.end());
  Caps cap(d,rho);V R(A),suffix(A+1);for(int i=A-1;i>=0;i--)suffix[i]=suffix[i+1]+lo[i];
  std::string dk=arr(d)+arr(lo)+std::to_string(r);auto dc=domaincounts.find(dk);
  if(dc==domaincounts.end())dc=domaincounts.emplace(dk,std::make_pair(canonical_count(d,lo,r),labelled_count(lo,r))).first;
  U count=0,mass=0,localflow=0,localsurvive=0;std::array<U,3>disposition{};Hash local;
  std::function<void(int,int)> visit=[&](int i,int left){
   if(i<A){int low=std::max(lo[i],i&&d[i]==d[i-1]?R[i-1]:0);int hi=std::min(B,left-suffix[i+1]);
    for(int x=low;x<=hi;x++){R[i]=x;visit(i+1,left-x);}return;}
   if(left)return;
   count++;mass+=weight(d,R,fact);V c=cap(R),dem(A);int required=0,upper=0;
   for(int j=0;j<A;j++){dem[j]=std::max(0,d[j]-R[j]);required+=dem[j];}for(int x:c)upper+=x;
   if(upper>=required){
    while(true){V nc=c;for(int b=0;b<B;b++){int best=0;for(int q=c[b];q>=0;q--){int possible=0;for(int w=0;w<B;w++)possible+=(w!=b&&rho[w]+c[w]>=q-1);if(possible>=q){best=q;break;}}nc[b]=best;}
     if(nc==c)break;c.swap(nc);
    }upper=0;for(int x:c)upper+=x;
   }
   int kind=0,mask=0;
   if(upper>=required){
    localflow++;V eligible(B);for(int b=0;b<B;b++)for(int j=0;j<A;j++)if(d[j]<=rho[b]+c[b]-1&&d[j]<=rho[b]+R[j])eligible[b]|=1<<j;
    if(!checking){
     int src=A+B,sink=src+1;Flow f(sink+1);
     for(int j=0;j<A;j++){f.edge(src,j,dem[j]);for(int b=0;b<B;b++)if(eligible[b]&(1<<j))f.edge(j,A+b,1);}
     for(int b=0;b<B;b++)f.edge(A+b,sink,c[b]);
     int achieved=f.run(src,sink);
     if(achieved<required){for(int j=0;j<A;j++)if(f.level[j]>=0)mask|=1<<j;need(mask>0,"empty failed cut");}
     put(certs,"["+std::to_string(state)+","+arr(R)+","+arr(c)+","+std::to_string(mask)+"]\n");
    }else{
     std::string cs;need(line(certs,cs),"missing certificate row");V cv=nums(cs);
     need(int(cv.size())==A+B+2&&cv[0]==int(state),"certificate state mismatch");
     for(int j=0;j<A;j++)need(cv[j+1]==R[j],"certificate column mismatch");
     for(int b=0;b<B;b++)need(cv[A+1+b]==c[b],"rederived source cap mismatch");
     mask=cv.back();need(mask>=0&&mask<(1<<A),"bad certificate mask");
    }
    if(mask){int demand=0,supply=0;for(int j=0;j<A;j++)if(mask&(1<<j))demand+=dem[j];for(int b=0;b<B;b++)supply+=std::min(c[b],__builtin_popcount(unsigned(mask&eligible[b])));need(demand>supply,"invalid strict subset certificate");kind=1;}
    else{kind=2;localsurvive++;if(!checking)put(survivors,"["+std::to_string(state)+","+std::to_string(k)+","+std::to_string(r)+","+arr(d)+","+arr(rho)+","+arr(R)+","+arr(c)+"]\n");}
   }
   disposition[kind]++;
   local.add(arr(R)+arr(c)+std::to_string(kind)+":"+std::to_string(mask)+"\n");
  };visit(0,r);
  need(count==dc->second.first,"canonical domain count mismatch");need(mass==dc->second.second,"labelled orbit mass mismatch");
  std::string record="{\"state\":"+std::to_string(state)+",\"canonical\":"+std::to_string(count)+",\"labelled\":"+std::to_string(mass)+",\"total_reject\":"+std::to_string(disposition[0])+",\"cut_reject\":"+std::to_string(disposition[1])+",\"survives\":"+std::to_string(disposition[2])+",\"sha256\":\""+local.end()+"\"}\n";
  details<<record;whole.add(record);state++;columns+=count;labelled+=mass;flowchecks+=localflow;surviving+=localsurvive;
  if(state%1000==0){details.flush();std::cout<<"{\"states\":"<<state<<",\"columns\":"<<columns<<",\"flow\":"<<flowchecks<<",\"surviving\":"<<surviving<<"}"<<std::endl;}
 }
 if(checking){std::string extra;need(!line(certs,extra),"unexpected trailing certificate");}
 need(gzclose(input)==Z_OK&&gzclose(certs)==Z_OK,"gzip close failed");if(survivors)need(gzclose(survivors)==Z_OK,"survivors close");
 std::string result="{\"completed\":true,\"n\":"+std::to_string(n)+",\"delta\":"+std::to_string(B)+",\"edges\":"+std::to_string(edges)+",\"checking\":"+(checking?"true":"false")+",\"states\":"+std::to_string(state)+",\"canonical_columns\":"+std::to_string(columns)+",\"labelled_columns\":"+std::to_string(labelled)+",\"flow_columns\":"+std::to_string(flowchecks)+",\"surviving_columns\":"+std::to_string(surviving)+",\"details_sha256\":\""+whole.end()+"\"}";
 std::ofstream(outprefix+"_column_summary.json")<<result<<"\n";std::cout<<result<<std::endl;
 }catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}return 0;}
