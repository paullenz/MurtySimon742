// Independent-structure capacity enumeration: choose actual incoming counts
// rather than subsets. This is an auxiliary resource model, not graph search.
#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <vector>

using Group = std::array<int,3>; // g, m, theta
std::vector<Group> options;
std::vector<unsigned char> costs;

int allocation(const std::vector<Group>& groups, int r, int gap, int pos,
               int mates, int ext, int incoming) {
    if (mates+ext>r || incoming>std::max(0,r+gap)) return -1;
    if (pos==static_cast<int>(groups.size())) return incoming;
    auto [g,m,theta]=groups[pos];
    int best=-1;
    for (int y=0;y<=m;++y) {
        best=std::max(best,allocation(groups,r,gap,pos+1,
                    mates+(y ? g-1 : 0), y ? std::max(ext,theta) : ext,
                    incoming+y));
    }
    return best;
}

void build(std::vector<Group>& groups, int n) {
    if (static_cast<int>(groups.size())==n) {
        for (int gap : {-1,0,2}) for(int r=1;r<=6;++r) {
            int value=allocation(groups,r,gap,0,0,0,0);
            if(value<0 || value>255) std::abort();
            costs.push_back(static_cast<unsigned char>(value));
        }
        return;
    }
    for (auto option : options) {
        groups.push_back(option); build(groups,n); groups.pop_back();
    }
}

int main() {
    for(int g : {2,3}) for(int m : {1,2}) for(int theta=0;theta<=3;++theta)
        options.push_back({g,m,theta});
    std::vector<Group> groups;
    for(int n=1;n<=3;++n) build(groups,n);
    if(costs.size()!=78624) return 2;
    std::cout.write(reinterpret_cast<const char*>(costs.data()), costs.size());
}
