// Necessary-condition checks only, not original-graph enumeration.
// Different enumeration structures from the Python companion.
#include <algorithm>
#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    const vector<pair<int,int>> edges={{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}};
    vector<vector<int>> records;
    // Choose the six multiplicities inside vertices 0..3. Edges to 4
    // are then uniquely determined by degree six at the first four vertices.
    for(int a=0;a<=6;++a) for(int b=0;b<=6;++b) for(int c=0;c<=6;++c)
    for(int e=0;e<=6;++e) for(int f=0;f<=6;++f) for(int g=0;g<=6;++g){
        int x=6-a-b-c, y=6-a-e-f, z=6-b-e-g, w=6-c-f-g;
        if(min({x,y,z,w})<0 || x+y+z+w!=6) continue;
        vector<int> mult={a,b,c,x,e,f,y,g,z,w}, holes;
        for(int j=0;j<10;++j) for(int n=0;n<mult[j];++n)
            holes.push_back((1<<edges[j].first)|(1<<edges[j].second));
        assert(holes.size()==15);
        int S[5]={0};
        for(int t=0;t<5;++t) for(int j=0;j<15;++j)
            if(holes[j]&(1<<t)) S[t]|=(1<<j);
        vector<int> row=mult; int failed=0;
        for(int t=0;t<5;++t){
            assert(__builtin_popcount((unsigned)S[t])==6);
            for(int j=0;j<15;++j){
                if(!(S[t]&(1<<j))){row.push_back(-1);continue;}
                int mask=0;
                for(int s=0;s<5;++s){
                    // Test destination absence and forward containment
                    // by individual label comparisons, rather than set masks.
                    bool ok=!(holes[j]&(1<<s));
                    for(int k=0;k<15;++k) if(k!=j && (holes[k]&(1<<t)))
                        if(!(holes[k]&(1<<s))) ok=false;
                    if(ok) mask|=(1<<s);
                }
                row.push_back(mask); if(!mask) ++failed;
            }
        }
        assert(failed>=28); records.push_back(row);
    }
    sort(records.begin(),records.end());
    long long feasible=0; vector<int> byh(7,1000000); vector<vector<int>> winners;
    int best=1000000; array<int,5> u{};
    for(int h=0;h<=6;++h) for(int L=0;L<=5*h/4;++L){
        int k=9+h,Q=5*h-4*L;
        function<void(int,int)> pools=[&](int i,int remaining){
            if(i<4){for(int v=0;v<=remaining;++v){u[i]=v;pools(i+1,remaining-v);}return;}
            u[4]=remaining;
            vector<int> dp(k+1,1000000);dp[0]=0;
            for(int t=0;t<5;++t){
                int cap=h-L+u[t],price=max(0,2-u[t]); if(cap<0) return;
                vector<int> ndp(k+1,1000000);
                for(int n=0;n<=k;++n) for(int take=0;take<=min(cap,k-n);++take)
                    ndp[n+take]=min(ndp[n+take],dp[n]+take*price);
                dp=ndp;
            }
            for(int n0=0;n0<=k;++n0) for(int N=0;N<=k-n0;++N){
                int n2=k-n0-N;if(N+2*n2>Q || dp[N]>=1000000) continue;
                ++feasible;int val=5*h+3*L+4*n0+dp[N];
                assert(val>=36-h+(11-h)*L);
                byh[h]=min(byh[h],val);
                vector<int> key={h,L};for(int t=0;t<5;++t)key.push_back(u[t]);
                key.insert(key.end(),{n0,N,n2});
                if(val<best){best=val;winners.clear();} if(val==best)winners.push_back(key);
            }
        };pools(0,L);
    }
    sort(winners.begin(),winners.end());
    auto printvec=[](const vector<int>&v){cout<<'[';for(size_t i=0;i<v.size();++i){if(i)cout<<',';cout<<v[i];}cout<<']';};
    cout<<"{\"interfaces\":[";
    for(size_t i=0;i<records.size();++i){if(i)cout<<',';printvec(records[i]);}
    cout<<"],\"scalar\":{\"feasible_outer_tuples\":"<<feasible<<",\"minimum\":"<<best<<",\"minima_by_h\":";
    printvec(byh);cout<<",\"minimizers\":[";
    for(size_t i=0;i<winners.size();++i){if(i)cout<<',';printvec(winners[i]);}
    cout<<"]}}\n";
}
