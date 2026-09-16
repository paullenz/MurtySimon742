// Independent-structure exhaustive binary-interface checker.
// Not an enumeration of original diameter-two critical graphs.
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
#include <utility>
#include <cassert>
#include <algorithm>

int main() {
    std::vector<std::array<int,3>> sc;
    for (int k=3;k<=6;++k) sc.push_back({3,1,k});
    for (int k=5;k<=7;++k) sc.push_back({3,2,k});
    sc.push_back({4,1,4});
    struct Row {int d,z,k; uint64_t n=0,s=0,ss=0,x=0;};
    std::vector<Row> rows;
    uint64_t overall=0;
    for (size_t sid=0;sid<sc.size();++sid) {
        const auto [d,z,k]=sc[sid];
        Row row{d,z,k};
        std::vector<std::pair<int,int>> pairs;
        for (int i=0;i<d;++i) for (int j=i+1;j<d;++j) pairs.push_back({i,j});
        const int te=static_cast<int>(pairs.size());
        const uint64_t rowmask=(uint64_t(1)<<k)-1;
        for (int cc=0;cc<(1<<d);++cc) {
            int c[4]={0},ell=0;
            for (int t=0;t<d;++t) { c[t]=z+((cc>>t)&1); ell+=c[t]; }
            for (int tm=0;tm<(1<<te);++tm) {
                int itdeg[4]={0};
                for (int q=0;q<te;++q) if (!((tm>>q)&1)) {
                    ++itdeg[pairs[q].first]; ++itdeg[pairs[q].second];
                }
                bool possible=true;
                for (int t=0;t<d;++t) if (itdeg[t]+k-d<ell-c[t]) possible=false;
                if (!possible) continue;
                for (uint64_t cm=0;cm<(uint64_t(1)<<(d*k));++cm) {
                    uint64_t all=rowmask, any=0;
                    bool valid=true;
                    int cross_missing=0;
                    for (int t=0;t<d;++t) {
                        uint64_t missing=(cm>>(t*k))&rowmask;
                        int present=k-__builtin_popcountll(missing);
                        int delta=itdeg[t]+present;
                        if (delta-d<ell-c[t]) { valid=false; break; }
                        all &= missing; any |= missing;
                        cross_missing+=k-present;
                    }
                    if (!valid || all) continue;
                    int common=k-__builtin_popcountll(any);
                    int h=k-1-z*(d-1), L=ell-z*d;
                    int mu=__builtin_popcount(static_cast<unsigned>(tm));
                    assert(2*mu+cross_missing<=d*h-(d-1)*L);
                    assert(common>=std::max(0,k-d*h+(d-1)*L+2*mu));
                    assert(d*h+(d-1)*common>=d*(z+1)-1);
                    uint64_t id=cm | (uint64_t(tm)<<(d*k))
                        | (uint64_t(cc)<<(d*k+te)) | (uint64_t(sid)<<(d*k+te+d));
                    ++row.n; row.s+=id; row.ss+=id*id; row.x^=id;
                }
            }
        }
        rows.push_back(row); overall+=row.n;
    }
    std::cout << "{\"cases\":" << overall << ",\"rows\":[";
    for (size_t j=0;j<rows.size();++j) {
        const auto &r=rows[j]; if(j) std::cout << ',';
        std::cout << "{\"d\":" << r.d << ",\"z\":" << r.z
            << ",\"kappa\":" << r.k << ",\"cases\":" << r.n
            << ",\"sum\":" << r.s << ",\"sum_squares\":" << r.ss
            << ",\"xor\":" << r.x << '}';
    }
    std::cout << "]}\n";
}
