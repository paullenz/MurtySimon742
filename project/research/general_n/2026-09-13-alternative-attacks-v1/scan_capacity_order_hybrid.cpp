#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <numeric>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

/*
Capacity-order / joint-endpoint hybrid verifier for the frozen N34 adjacent
family.  This is a necessary-condition relaxation, not a graph search.

The cheap first stage uses CAPACITY_ORDER_ENDPOINT_LEMMA.md: for fixed q,h it
combines the greedy lower bound on sum q*p with the capacity-order lower bound
mu_2 for zero-excess demand-two labels.  Label-correction DPs are memoized by
the score tail they actually see.  Only branches whose cheap gap is <=0 are
sent to the older exact joint source-pair replay.  A branch with cheap gap >0
is already excluded, while a nonpositive branch is replaced by the stronger
joint lower bound.  Thus filtering cannot discard a possible non-strict case.

The four profiles are frozen explicitly so each layer can be replayed as

    scan_capacity_order_hybrid STATE_ID E

for STATE_ID in {230,282,385,519}.
*/

static const long long NEG=-(1LL<<55), INF=(1LL<<55);
struct QT{ vector<int> q; int sq=0; };
struct State{int id,n2,n3,r1,r2,r3,S,r,a=15,b=18;};
static map<tuple<int,int,int>,vector<QT>> pcache;
static void genrec(int pos,int cnt,int last,int mx,int rem,vector<int>&cur,vector<QT>&out){
 if(pos==cnt){if(rem==0){int sq=0;for(int x:cur)sq+=x*x;out.push_back({cur,sq});}return;}
 int slots=cnt-pos-1;
 for(int x=last;x<=mx&&x<=rem;++x){int rr=rem-x;if(rr<x*slots||rr>mx*slots)continue;cur[pos]=x;genrec(pos+1,cnt,x,mx,rr,cur,out);}
}
static const vector<QT>& parts(int cnt,int mx,int sum){
 auto k=make_tuple(cnt,mx,sum);auto it=pcache.find(k);if(it!=pcache.end())return it->second;
 vector<QT> o;if(cnt==0){if(sum==0)o.push_back({{},0});}else if(sum>=0&&sum<=cnt*mx){vector<int> c(cnt);genrec(0,cnt,0,mx,sum,c,o);}return pcache.emplace(k,move(o)).first->second;
}
static State state(int id){
 if(id==230)return {230,4,11,6,3,9,41,39};
 if(id==282)return {282,3,12,6,2,10,42,40};
 if(id==385)return {385,2,13,5,3,10,43,41};
 if(id==519)return {519,1,14,6,0,12,44,42};
 cerr<<"unknown state\n";exit(2);
}
static string sig(const vector<int>&scores){
 string k; k.push_back(char(scores.size()));
 for(size_t i=3;i<scores.size();++i)k.push_back(char(scores[i]));
 return k;
}
struct T2{int E,n2;vector<long long>a; long long& at(int e,int h,int z){return a[(e*(n2+1)+h)*(n2+1)+z];} const long long& at(int e,int h,int z)const{return a[(e*(n2+1)+h)*(n2+1)+z];}};
struct T3{int E,n3;vector<long long>a; long long& at(int e,int h){return a[e*(n3+1)+h];} const long long& at(int e,int h)const{return a[e*(n3+1)+h];}};
struct Corr{int H,n2;vector<long long>a; long long& at(int h,int z){return a[h*(n2+1)+z];} const long long& at(int h,int z)const{return a[h*(n2+1)+z];}};

static unordered_map<string,T2> cache2;
static unordered_map<string,T3> cache3;
static unordered_map<string,Corr> cachec;

static const T2& getT2(const State&st,int E,const vector<int>&scores){
 string k=sig(scores); auto it=cache2.find(k); if(it!=cache2.end())return it->second;
 T2 t{E,st.n2,vector<long long>((E+1)*(st.n2+1)*(st.n2+1),NEG)};t.at(0,0,0)=0;
 int maxe=(int)scores.size()-2;
 if(maxe<0){auto [jt,_]=cache2.emplace(k,move(t));return jt->second;}
 for(int lab=0;lab<st.n2;++lab){
  vector<long long> nd(t.a.size(),NEG);
  auto idx=[&](int e,int h,int z){return (e*(st.n2+1)+h)*(st.n2+1)+z;};
  for(int se=0;se<=E;++se)for(int h=0;h<=st.n2;++h)for(int z=0;z<=st.n2;++z){
   long long cur=t.at(se,h,z);if(cur==NEG)continue;
   for(int e=0;e<=maxe&&se+e<=E;++e){int nh=h+(e>=2),nz=z+(e==0);if(nh>st.n2||nz>st.n2)continue;long long w=0;if(e>=2)w=1LL*(e-1)*(e+scores[e+1]);auto &v=nd[idx(se+e,nh,nz)];v=max(v,cur+w);}
  }
  t.a.swap(nd);
 }
 auto [jt,_]=cache2.emplace(k,move(t));return jt->second;
}
static const T3& getT3(const State&st,int E,const vector<int>&scores){
 string k=sig(scores); auto it=cache3.find(k); if(it!=cache3.end())return it->second;
 T3 t{E,st.n3,vector<long long>((E+1)*(st.n3+1),NEG)};t.at(0,0)=0;
 int maxe=(int)scores.size()-3;
 if(maxe<0){auto [jt,_]=cache3.emplace(k,move(t));return jt->second;}
 for(int lab=0;lab<st.n3;++lab){
  vector<long long> nd(t.a.size(),NEG);
  for(int se=0;se<=E;++se)for(int h=0;h<=st.n3;++h){long long cur=t.at(se,h);if(cur==NEG)continue;
   for(int e=0;e<=maxe&&se+e<=E;++e){int nh=h+(e>=2);if(nh>st.n3)continue;long long w=0;if(e>=1)w=1LL*e*(e+scores[e+2]);auto &v=nd[(se+e)*(st.n3+1)+nh];v=max(v,cur+w);}
  }
  t.a.swap(nd);
 }
 auto [jt,_]=cache3.emplace(k,move(t));return jt->second;
}
static const Corr& getCorr(const State&st,int E,const vector<int>&s2,const vector<int>&s3){
 string k=sig(s2);k.push_back(char(255));k+=sig(s3);auto it=cachec.find(k);if(it!=cachec.end())return it->second;
 const auto&t2=getT2(st,E,s2);const auto&t3=getT3(st,E,s3);int H=min(15,E/2);Corr c{H,st.n2,vector<long long>((H+1)*(st.n2+1),NEG)};
 for(int e2=0;e2<=E;++e2){int e3=E-e2;
  for(int h2=0;h2<=st.n2;++h2)for(int z=0;z<=st.n2;++z){long long v2=t2.at(e2,h2,z);if(v2==NEG)continue;
   for(int h3=0;h3<=st.n3;++h3){long long v3=t3.at(e3,h3);if(v3==NEG)continue;int h=h2+h3;if(h>H)continue;c.at(h,z)=max(c.at(h,z),v2+v3);}
  }
 }
 auto [jt,_]=cachec.emplace(k,move(c));return jt->second;
}
struct Src{int q,rho;};
struct SB{long long pmin;int mu;};
static vector<SB> source_bounds(const State&st,int E,const vector<int>&q2,const vector<int>&q3,int H){
 int Q=st.S+E;vector<Src>src;for(int i=0;i<st.r1;++i)src.push_back({0,1});for(int q:q2)src.push_back({q,2});for(int q:q3)src.push_back({q,3});assert((int)src.size()==18);
 sort(src.begin(),src.end(),[](auto&a,auto&b){return tie(a.q,a.rho)<tie(b.q,b.rho);});
 vector<SB> out(H+1,{INF,INT_MAX});
 for(int h=0;h<=H;++h){
  array<int,18> cap{};int U=0;for(int i=0;i<18;++i){int c=(src[i].q>h)?src[i].rho:(src[i].rho+2);c=min(c,17-src[i].q);c=max(c,0);cap[i]=c;U+=c;}
  if(Q>U)continue;
  int left=Q;long long pc=0;for(int i=0;i<18&&left;++i){int take=min(left,cap[i]);pc+=1LL*src[i].q*take;left-=take;}if(left)continue;
  int mu=INT_MAX;
  for(int lam=0;lam<=17;++lam){int d1=INT_MAX,d2=INT_MAX,cnt=0;for(int i=0;i<18;++i){if(src[i].rho<2||src[i].q<=0||src[i].q>lam)continue;++cnt;int m=min({cap[i],src[i].rho-1,lam-src[i].q});int loss=cap[i]-m;if(loss<d1){d2=d1;d1=loss;}else if(loss<d2)d2=loss;}
   if(cnt>=2&&d2<INT_MAX&&Q<=U-d1-d2){mu=max(2,lam);break;}
  }
  out[h]={pc,mu};
 }
 return out;
}

static long long joint_source_objective(const State&st,int E,const vector<int>&q2,const vector<int>&q3,int h,int z,int Q){
 vector<Src> src;for(int i=0;i<st.r1;++i)src.push_back({0,1});for(int q:q2)src.push_back({q,2});for(int q:q3)src.push_back({q,3});
 struct SC{int q,rho,cap;};vector<SC>a;for(auto x:src){int c=(x.q>h)?x.rho:(x.rho+2);c=min(c,17-x.q);c=max(c,0);a.push_back({x.q,x.rho,c});}
 vector<int>ord(a.size());iota(ord.begin(),ord.end(),0);sort(ord.begin(),ord.end(),[&](int i,int j){return tie(a[i].q,a[i].rho)<tie(a[j].q,a[j].rho);});
 auto rest=[&](int skip1,int skip2,int need){long long cost=0;if(need<0)return INF;for(int k:ord){if(k==skip1||k==skip2)continue;int take=min(need,a[k].cap);cost+=1LL*a[k].q*take;need-=take;if(!need)return cost;}return INF;};
 if(z==0)return rest(-1,-1,Q);
 long long best=INF;
 for(int i=0;i<(int)a.size();++i){if(a[i].rho<2||a[i].q<=0)continue;int mi=min(a[i].cap,a[i].rho-1);
  for(int j=i+1;j<(int)a.size();++j){if(a[j].rho<2||a[j].q<=0)continue;int mj=min(a[j].cap,a[j].rho-1);
   for(int pi=0;pi<=mi;++pi)for(int pj=0;pj<=mj;++pj){long long rc=rest(i,j,Q-pi-pj);if(rc==INF)continue;long long cost=1LL*a[i].q*pi+1LL*a[j].q*pj+rc;int lam=max({2,a[i].q+pi,a[j].q+pj});best=min(best,cost+1LL*z*lam);}
  }
 }
 return best;
}

int main(int argc,char**argv){if(argc!=3){cerr<<"usage STATE E\n";return 2;}int id=stoi(argv[1]),E=stoi(argv[2]);State st=state(id);int Q=st.S+E;int qmax2=min(13,st.n2),qmax3=12;long long best=INF;long long combos=0,filtered=0;vector<int>bestq2,bestq3;int besth=-1,bestz=-1;long long bestcorr=0,bestsrc=0;
 for(int sum2=0;sum2<=st.r2*qmax2&&sum2<=Q;++sum2){int sum3=Q-sum2;if(sum3<0||sum3>st.r3*qmax3)continue;const auto&p2=parts(st.r2,qmax2,sum2);const auto&p3=parts(st.r3,qmax3,sum3);
  for(const auto&a2:p2)for(const auto&a3:p3){++combos;vector<int>s2,s3;for(int q:a2.q)if(q>0)s2.push_back(q+1);for(int q:a3.q)if(q>0){s2.push_back(q+2);s3.push_back(q+2);}sort(s2.begin(),s2.end(),greater<int>());sort(s3.begin(),s3.end(),greater<int>());
   if((st.n2&&s2.size()<2)||(st.n3&&s3.size()<3))continue;const Corr&c=getCorr(st,E,s2,s3);auto sb=source_bounds(st,E,a2.q,a3.q,c.H);long long sq=1LL*a2.sq+a3.sq,base=3LL*(st.r+Q);
   for(int h=0;h<=c.H;++h){if(sb[h].pmin==INF)continue;for(int z=0;z<=st.n2;++z){long long cv=c.at(h,z);if(cv==NEG)continue;if(z>0&&sb[h].mu==INT_MAX)continue;long long so=sb[h].pmin+(z?1LL*z*sb[h].mu:0);long long gap=sq+so-base-cv;if(gap<=0&&z>0){++filtered;long long jo=joint_source_objective(st,E,a2.q,a3.q,h,z,Q);if(jo==INF)continue;so=jo;gap=sq+so-base-cv;}if(gap<best){best=gap;bestq2=a2.q;bestq3=a3.q;besth=h;bestz=z;bestcorr=cv;bestsrc=so;}}}
  }
 }
 cout<<"state="<<id<<" E="<<E<<" combos="<<combos<<" gap="<<best<<" h="<<besth<<" z="<<bestz<<" corr="<<bestcorr<<" source="<<bestsrc<<" filtered="<<filtered<<" cache2="<<cache2.size()<<" cache3="<<cache3.size()<<" cachec="<<cachec.size()<<"\nq2=";for(int x:bestq2)cout<<x<<',';cout<<" q3=";for(int x:bestq3)cout<<x<<',';cout<<"\n";
}
