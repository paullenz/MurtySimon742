// Ordered pool enumeration and dynamic programming, independent of Python's
// sorted-pool expanded-slot method. These are necessary-condition row models.
#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using Key = std::vector<int>;
int main() {
    std::map<Key,std::pair<int,long long>> rows;
    for(int h=0;h<=6;++h) {
        int k=9+h;
        for(int L=0;L<=5*h/4;++L) {
            std::array<int,5> u{};
            std::function<void(int,int)> visit = [&](int at,int left) {
                if(at<4) {
                    for(int x=0;x<=left;++x) {u[at]=x;visit(at+1,left-x);}
                    return;
                }
                u[4]=left;
                const int INF=1000000;
                std::vector<int> dp(k+1,INF);dp[0]=0;
                for(int t=0;t<5;++t) {
                    int capacity=h-L+u[t];
                    if(capacity<0) return;
                    int price=std::max(1,2-u[t]);
                    std::vector<int> next(k+1,INF);
                    for(int used=0;used<=k;++used) if(dp[used]<INF)
                        for(int take=0;take<=capacity && used+take<=k;++take)
                            next[used+take]=std::min(next[used+take],dp[used]+price*take);
                    dp.swap(next);
                }
                auto sorted=u;std::sort(sorted.begin(),sorted.end());
                for(int n0=0;n0<=k;++n0) for(int n1=0;n1<=k-n0;++n1) {
                    int n2=k-n0-n1;
                    if(n1+2*n2>5*h-4*L || dp[n1]>=INF) continue;
                    int cost=5*h+3*L+4*n0+n2+dp[n1];
                    Key key{h,L};key.insert(key.end(),sorted.begin(),sorted.end());
                    key.insert(key.end(),{n0,n1,n2});
                    auto it=rows.find(key);
                    if(it==rows.end()) rows.emplace(key,std::make_pair(cost,1));
                    else {
                        if(it->second.first!=cost) throw std::runtime_error("Symmetry cost mismatch");
                        ++it->second.second;
                    }
                }
            };
            visit(0,L);
        }
    }
    std::cout<<'[';bool comma=false;
    for(const auto &entry:rows) {
        if(comma) std::cout<<',';
        comma=true;std::cout<<'[';
        for(size_t i=0;i<entry.first.size();++i) {
            if(i) std::cout<<',';
            std::cout<<entry.first[i];
        }
        std::cout<<','<<entry.second.first<<','<<entry.second.second<<']';
    }
    std::cout<<"]\n";
}
