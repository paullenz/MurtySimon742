// Independent complete integer source enumeration; no closed-form code.
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
using Maxima=vector<array<I,2>>;
unordered_map<uint64_t,Maxima> cache;
I option_checks=0;
const array<string,3> layers={"n34-m289","n35-m306","n35-m307"};

const Maxima& local(int a,int b,int h,int j,int rho,int hi,int lo) {
    uint64_t key=0;
    for(int x:{a,b,h,j,rho,hi,lo}){assert(0<=x && x<32);key=key*32+x;}
    auto found=cache.find(key);if(found!=cache.end())return found->second;
    Maxima best(a+2,{NEG,NEG});
    for(int H=0;H<=a;++H)for(int q=0;q<=a;++q)for(int p=0;p<b;++p) {
        if(H>hi || H>q || q-H>lo || q+rho>a || q+p>=b || p>rho+b-a-1)continue;
        int e=H>h;if(e>j)continue;
        I ramp=0;for(int cut=h;cut<4*h;++cut)ramp+=q+p<=cut;
        I receiving=rho>=h?min(p,j-e):0;
        I base=H*(h+ramp)+H-2*(e*H-receiving);
        ++option_checks;
        for(int k=0;k<a+2;++k) {
            I cost=base-4*((q>=k+1?q:0)-(rho+q>=k?p:0));
            best[k][e]=max(best[k][e],cost);
        }
    }
    return cache.emplace(key,move(best)).first->second;
}

vector<I> capacity(int a,int h,const vector<int>& s,const vector<int>& rho) {
    vector<int> caps;
    for(int rv:rho)if(rv>=h) {
        int labels=0;for(int sv:s)labels+=sv>=h && sv<=rv;
        caps.push_back(min(a-rv,labels));
    }
    sort(caps.rbegin(),caps.rend());I low=0;int large=0;
    for(int c:caps){low+=min(c,h);large+=c>h;}
    vector<I> answer;I prefix=0;int z=caps.size();
    for(int j=0;j<=large;++j) {
        if(j)prefix+=caps[j-1];
        I bound=low-I(j)*h+min(prefix,I(j)*(z-j)+I(j)*(j-1)/2);
        answer.push_back(bound);
    }
    return answer;
}

I gap(int a,int b,int h,int k,int j,const vector<int>& s,const vector<int>& rho) {
    // Different aggregation from discovery: dynamic programming over sources.
    map<int,const Maxima*> sources;
    for(int rv:rho)if(!sources.count(rv)) {
        int hi=0,lo=0;for(int sv:s)if(sv<=rv){if(sv>=h)++hi;else ++lo;}
        sources[rv]=&local(a,b,h,j,rv,hi,lo);
    }
    vector<I> dp(j+1,NEG);dp[0]=0;
    for(int rv:rho) {
        vector<I> next(j+1,NEG);auto value=(*sources[rv])[k];
        for(int used=0;used<=j;++used)if(dp[used]!=NEG)for(int e=0;e<=1;++e) {
            if(used+e<=j && value[e]!=NEG)next[used+e]=max(next[used+e],dp[used]+value[e]);
        }
        dp=move(next);
    }
    assert(dp[j]!=NEG);
    I W=0,G=0,r=0;for(int sv:s)if(sv>=h){W+=sv;G+=max(4*h,sv);}for(int rv:rho)r+=rv;
    return h*(G-r)+W-dp[j];
}

template<class T>void print_array(const vector<T>& values) {
    cout<<'[';for(size_t i=0;i<values.size();++i){if(i)cout<<',';cout<<values[i];}cout<<']';
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int n;cin>>n;assert(n==5578);array<int,2> counts={0,0};
    for(int index=0;index<n;++index) {
        int layer,id,a,b,t,ns,nr;cin>>layer>>id>>a>>b>>t>>ns;
        assert(0<=layer && layer<3 && a==15 && (b==18 || b==19) && t>0 && ns==a);
        vector<int> s(ns);for(int& x:s){cin>>x;assert(0<=x && x<=a);}
        cin>>nr;assert(nr==b);vector<int> rho(nr);for(int& x:rho){cin>>x;assert(1<=x && x<=a);}
        cout<<"{\"layer\":\""<<layers[layer]<<"\",\"state_id\":"<<id<<",\"modes\":{";
        for(int mode=0;mode<2;++mode) {
            if(mode)cout<<',';
            cout<<'"'<<(mode?"all_k":"fixed_k2")<<"\":{\"thresholds\":[";
            int witness=0;bool firsth=true;
            for(int h=2;h<=*max_element(s.begin(),s.end());++h) {
                if(!firsth)cout<<',';
                firsth=false;auto caps=capacity(a,h,s,rho);I W=0;for(int sv:s)if(sv>=h)W+=sv;
                cout<<"{\"h\":"<<h<<",\"capacities\":";print_array(caps);cout<<",\"attempts\":[";
                bool blocked=false,firstj=true;
                for(int j=0;j<int(caps.size());++j) {
                    if(caps[j]<W)continue;
                    vector<I> values;
                    if(mode)for(int k=0;k<a+2;++k)values.push_back(gap(a,b,h,k,j,s,rho));
                    else values.push_back(gap(a,b,h,2,j,s,rho));
                    if(!firstj)cout<<',';
                    firstj=false;cout<<"{\"j\":"<<j<<",\"gaps\":";print_array(values);cout<<'}';
                    if(*max_element(values.begin(),values.end())<=0){blocked=true;break;}
                }
                cout<<"]}";
                if(!blocked){witness=h;break;}
            }
            cout<<"],\"witness_h\":";
            if(witness)cout<<witness;else cout<<"null";
            cout<<'}';counts[mode]+=witness!=0;
        }
        cout<<"}}\n";
        if((index+1)%500==0 || index+1==n){cerr<<"VERIFIED "<<index+1<<" excluded "<<counts[0]<<' '<<counts[1]<<'\n';cout.flush();}
    }
    assert(cin);string extra;assert(!(cin>>extra));
    cerr<<"SOURCE_CONTEXTS "<<cache.size()<<" SOURCE_OPTIONS "<<option_checks<<'\n';
}
