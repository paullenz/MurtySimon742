// Separately written histogram diagnostic. No original-graph enumeration.
#include <iostream>
#include <vector>
#include <map>
#include <stdexcept>
int main() {
    int n;
    if (!(std::cin>>n) || n<0) return 2;
    for(int it=0;it<n;++it) {
        int sid,a,b;
        if(!(std::cin>>sid>>a>>b) || a<0 || b<0) return 2;
        std::vector<int> r(b);
        std::map<int,int> counts;
        for(int j=0,x;j<a;++j){if(!(std::cin>>x)||x<0)return 2; ++counts[x];}
        for(int &x:r) if(!(std::cin>>x)||x<0)return 2;
        for(const auto &[d,nt]:counts){
            if(d<2)continue;
            int nh=0,nlow=0;
            for(int x:r) nh+=(x>=d);
            for(const auto &[s,c]:counts) if(s<d-1)nlow+=c;
            bool match=nt==d && nh==d;
            // Degree lower bound at a tight label versus all possible
            // neighbours left after the endpoint-cap classification.
            bool reject=match && (2*d-1 > (d-1)+nlow);
            std::cout<<sid<<' '<<d<<' '<<nt<<' '<<nh<<' '<<nlow<<' '<<match<<' '<<reject<<'\n';
        }
    }
}
