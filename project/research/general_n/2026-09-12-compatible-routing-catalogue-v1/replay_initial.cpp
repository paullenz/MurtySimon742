// Exact frozen-catalogue replay. No floating arithmetic or solver.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using I=int64_t;
constexpr I NEG=-(I(1)<<50);
struct Weight { I eta,w,mu,lambda,nu; vector<pair<int,I>> ordinary,forced; };
vector<Weight> weights;
array<vector<int>,3> modes;
using Maxima=vector<array<I,2>>;
unordered_map<uint64_t,Maxima> cache;
const array<string,3> layer_names={"n34-m289","n35-m306","n35-m307"};
const array<string,3> mode_names={"heavy_only","selected_degree","eligible"};

const Maxima& local(int domain,int a,int b,int h,int j,int rho,int hi,int lo) {
    if(!domain)lo=0;
    uint64_t key=0;
    for(int x:{domain,a,b,h,j,rho,hi,lo}) {assert(0<=x && x<32);key=key*32+x;}
    auto found=cache.find(key);if(found!=cache.end())return found->second;
    Maxima best(weights.size(),{NEG,NEG});
    if(!domain && rho<h) {
        for(auto& v:best)v[0]=0;
    } else {
        int qcap=min(a-rho,hi+lo);
        for(int q=0;q<=qcap;++q) {
            int first=domain?max(0,q-lo):q,last=min(q,hi);
            for(int H=first;H<=last;++H) {
                int e=H>h;if(e && !j)continue;
                int pcap=min(rho+b-a-1,b-1-q);
                for(int p=0;p<=pcap;++p) {
                    I F=e*H,m=rho>=h?min(p,j-e):0;
                    I L=I(H)*(h+max(0,4*h-max(h,q+p)));
                    for(size_t ti=0;ti<weights.size();++ti) {
                        const auto& t=weights[ti];
                        I v=t.w*L+t.eta*H-t.mu*F-t.lambda*(F-m)-t.nu*(q-p);
                        for(auto [k,c]:t.ordinary)v-=c*((q>k?q:0)-(rho+q>=k?p:0));
                        for(auto [k,c]:t.forced)v-=c*((q>k?F:0)-(rho+q>=k?m:0));
                        best[ti][e]=max(best[ti][e],v);
                    }
                }
            }
        }
    }
    return cache.emplace(key,move(best)).first->second;
}

vector<I> gaps(int domain,int a,int b,int h,int j,const vector<int>& s,const vector<int>& rho,const vector<int>& ids) {
    int z=count_if(rho.begin(),rho.end(),[&](int v){return v>=h;});
    I W=0,G=0,r=0;for(int v:s)if(v>=h){W+=v;G+=max(4*h,v);}for(int v:rho)r+=v;
    I K=I(j)*(z-j)+I(j)*(j-1)/2;
    map<int,int> sizes;for(int v:rho)++sizes[v];
    vector<pair<int,const Maxima*>> locals;
    for(auto [rv,n]:sizes) {
        int hi=0,lo=0;for(int v:s)if(v<=rv){if(v>=h)++hi;else ++lo;}
        locals.push_back({n,&local(domain,a,b,h,j,rv,hi,lo)});
    }
    vector<I> out;
    for(int id:ids) {
        I total=0;vector<I> diff;
        for(auto [n,ptr]:locals) {
            auto v=(*ptr)[id];assert(v[0]!=NEG);total+=n*v[0];
            if(v[1]!=NEG)for(int i=0;i<n;++i)diff.push_back(v[1]-v[0]);
        }
        assert(int(diff.size())>=j);sort(diff.rbegin(),diff.rend());
        for(int i=0;i<j;++i)total+=diff[i];
        const auto& t=weights[id];out.push_back(t.eta*W+t.w*h*(G-r)-t.mu*K-total);
    }
    return out;
}

vector<I> capacities(int a,int h,const vector<int>& s,const vector<int>& rho) {
    int z=0;I low=0;vector<int> high;
    for(int rv:rho)if(rv>=h) {
        ++z;int eligible=0;for(int sv:s)eligible+=h<=sv && sv<=rv;
        int cap=min(a-rv,eligible);low+=min(h,cap);if(cap>h)high.push_back(cap);
    }
    sort(high.rbegin(),high.rend());vector<I> out;I sum=0;
    for(int j=0;j<=int(high.size());++j) {
        if(j)sum+=high[j-1];I pair=I(j)*z-I(j)*(j+1)/2;
        out.push_back(low-I(j)*h+min(sum,pair));
    }
    return out;
}

template<class T> void array_json(const vector<T>& v) {
    cout<<'[';for(size_t i=0;i<v.size();++i){if(i)cout<<',';cout<<v[i];}cout<<']';
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int nt;cin>>nt;assert(0<nt && nt<=64);weights.resize(nt);
    for(auto& t:weights) {
        cin>>t.eta>>t.w>>t.mu>>t.lambda>>t.nu;
        assert(0<=t.eta && t.eta<=1000 && 0<=t.w && t.w<=1000 && 0<=t.mu && t.mu<=1000 && 0<=t.lambda && t.lambda<=1000 && abs(t.nu)<=1000);
        for(auto ptr:{&t.ordinary,&t.forced}) {
            int n;cin>>n;assert(0<=n && n<=32);
            for(int i=0;i<n;++i){int k;I c;cin>>k>>c;assert(0<=k && k<=32 && 0<=c && c<=1000);ptr->push_back({k,c});}
        }
    }
    for(auto& ids:modes){int n;cin>>n;for(int i=0;i<n;++i){int id;cin>>id;assert(0<=id && id<nt);ids.push_back(id);}}
    int count;cin>>count;assert(count==5578);
    array<int,3> excluded={0,0,0};
    for(int index=0;index<count;++index) {
        int layer,id,a,b,t,ns,nr;cin>>layer>>id>>a>>b>>t>>ns;
        assert(0<=layer && layer<3 && a==15 && (b==18||b==19) && t>0 && ns==a);
        vector<int> s(ns);for(int& v:s){cin>>v;assert(0<=v && v<=a);}
        cin>>nr;assert(nr==b);vector<int> rho(nr);for(int& v:rho){cin>>v;assert(1<=v && v<=a);}
        cout<<"{\"layer\":\""<<layer_names[layer]<<"\",\"state_id\":"<<id<<",\"modes\":{";
        int maxs=*max_element(s.begin(),s.end());
        for(int mode=0;mode<3;++mode) {
            if(mode)cout<<',';cout<<'"'<<mode_names[mode]<<"\":{\"thresholds\":[";
            bool firsth=true;int witness=0;
            for(int h=2;h<=maxs;++h) {
                if(!firsth)cout<<',';firsth=false;
                auto caps=capacities(a,h,s,rho);I W=0;for(int sv:s)if(sv>=h)W+=sv;
                cout<<"{\"h\":"<<h<<",\"capacities\":";array_json(caps);cout<<",\"attempts\":[";
                bool firstj=true,blocked=false;
                for(int j=0;j<int(caps.size());++j) {
                    if(caps[j]<W)continue;
                    auto values=gaps(mode!=0,a,b,h,j,s,rho,modes[mode]);
                    if(!firstj)cout<<',';firstj=false;
                    cout<<"{\"j\":"<<j<<",\"gaps\":";array_json(values);cout<<'}';
                    if(*max_element(values.begin(),values.end())<=0){blocked=true;break;}
                }
                cout<<"]}";
                if(!blocked){witness=h;break;}
            }
            cout<<"],\"witness_h\":";if(witness)cout<<witness;else cout<<"null";cout<<'}';
            excluded[mode]+=witness!=0;
        }
        cout<<"}}\n";
        if((index+1)%500==0 || index+1==count) {
            cerr<<"PROGRESS "<<index+1<<"/"<<count<<" excluded "<<excluded[0]<<' '<<excluded[1]<<' '<<excluded[2]<<" cached "<<cache.size()<<'\n';
            cout.flush();
        }
    }
    assert(cin);string extra;assert(!(cin>>extra));
}
