
static vector<Type> make_types(const vector<int>&q,const vector<int>&rho){
 map<pair<int,int>,int> ct; for(size_t i=0;i<q.size();++i) ++ct[{rho[i],q[i]}];
 vector<Type> t; for(auto const&kv:ct)t.push_back({kv.first.first,kv.first.second,kv.second,kv.first.first+kv.first.second,0}); return t;
}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: replay_forced_core_witnesses INPUT OUTPUT.tsv\n";return 2;}
 ifstream in(argv[1]); ofstream out(argv[2]); if(!in||!out)return 2; int N; in>>N;
 out<<"layer\tstate_id\tpass\treason\tE\tEmax\tcost\tenvelope\tcore_reason\n";
 int passn=0;
 for(int z=0;z<N;++z){
  State st; int ns,nr,nq,nwr; in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns; st.s.resize(ns); for(int&x:st.s)in>>x; in>>nr; st.rho.resize(nr); for(int&x:st.rho)in>>x;
  vector<int>q,wrho; in>>nq; q.resize(nq); for(int&x:q)in>>x; in>>nwr; wrho.resize(nwr); for(int&x:wrho)in>>x;
  bool ok=true; string why="PASS"; long long cost=-1,env=-1; int E=-1,Emax=-1; CoreCert cc;
  if((int)q.size()!=st.b || wrho.size()!=q.size()){ok=false;why="SIZE";}
  if(ok && wrho!=st.rho){ok=false;why="RHO_MISMATCH";}
  int S=accumulate(st.s.begin(),st.s.end(),0), Q=accumulate(q.begin(),q.end(),0); E=Q-S;
  int U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*(st.b-st.a-1); int Qmax=min(U,st.b*(st.b-1)/2); long long sumqmax=0;
  if(ok){
   for(size_t u=0;u<q.size();++u){int r=wrho[u];int labels=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=r;});int qm=max(0,min(st.a-r,labels));sumqmax+=qm;if(q[u]<0||q[u]>qm){ok=false;why="Q_RANGE";break;}}
  }
  Qmax=min<long long>(Qmax,sumqmax); Emax=Qmax-S;
  if(ok && (E<0||E>Emax)){ok=false;why="E_RANGE";}
  if(ok){env=excess_envelope(st,E);if(env==-(1LL<<50)){ok=false;why="ENVELOPE_UNDEFINED";}}
  vector<Type>types; if(ok){types=make_types(q,wrho);cc=forced_core_types(st,types);if(cc.reject){ok=false;why="FORCED_CORE";}}
  vector<int>P; if(ok){auto pe=pair_capacity_types(st,types,E,q,wrho);P=pe.P;if(!pe.pass){ok=false;why="PAIRCAP";}}
  if(ok && !variable_incidence(st,q,wrho)){ok=false;why="INCIDENCE";}
  if(ok && pair_flow(q,wrho)<Q){ok=false;why="PAIRHALL";}
  if(ok){auto fc=target_cost_flow(q,wrho,P,Q);if(fc.first<Q){ok=false;why="TARGETHALL";}else cost=fc.second;}
  if(ok && env>=0 && cost>env){ok=false;why="COST";}
  if(ok)++passn;
  out<<st.layer<<'\t'<<st.id<<'\t'<<(ok?1:0)<<'\t'<<why<<'\t'<<E<<'\t'<<Emax<<'\t'<<cost<<'\t'<<env<<'\t'<<cc.why<<'\n';
 }
 cerr<<"replayed "<<N<<" witnesses; pass="<<passn<<" fail="<<(N-passn)<<"\n"; return passn==N?0:1;
}
