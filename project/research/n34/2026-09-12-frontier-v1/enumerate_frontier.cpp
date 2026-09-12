// Complete nondecreasing 15-demand domain via descending multiplicities.
// Q is accumulated one tail at a time; no floating point or solver is used.
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int A=15, B=18;
array<int,A> counts{}, tails{};
long long total=0, output_rows=0;
map<int,long long> hist;
array<long long,5> raw{}, closed{}, dcap{};
ofstream out;
int inverse_cap(int h,int w) {
    if (!w) return 0;
    int z=h;
    while (z*(z-1)+h*(h+1)<2*w) ++z;
    return z;
}
void rec(int h,int slots,int mass,int score) {
    if (h==0) {
        ++total;
        counts[0]=slots;
        ++hist[score];
        if (score<20) return;
        int z=0, extra=0;
        for(int j=A-1;j>=2;--j) {
            z=max(z,tails[j]);
            extra+=z-tails[j];
        }
        int cq=score-extra;
        for(int t=1;t<=4;++t) {
            if(score>=B+2*t) ++raw[t];
            if(cq>=B+2*t) ++closed[t];
            if(cq>=B+2*t && counts[14]==0) ++dcap[t];
        }
        if(cq<20 || counts[14]) return;
        ++output_rows;
        out<<score<<','<<cq;
        for(int j=0;j<A;++j) for(int c=0;c<counts[j];++c) out<<','<<j;
        out<<'\n';
        return;
    }
    for(int c=0;c<=slots;++c) {
        counts[h]=c;
        int w=mass+h*c, n=A-slots+c;
        tails[h]=h>=2 ? inverse_cap(h,w) : 0;
        rec(h-1,slots-c,w,score+n-tails[h]);
    }
}
int main(int argc,char**argv) {
    if(argc!=2) {cerr<<"usage: enumerate_frontier output.csv\n";return 2;}
    out.open(argv[1]);
    if(!out) return 2;
    out<<"Q,Q_monotone";
    for(int i=0;i<A;++i) out<<",s"<<i;
    out<<'\n';
    rec(A-1,A,0,0);
    if(total!=77558760 || hist.rbegin()->first!=26 || hist[26]!=2) return 1;
    cout<<"total="<<total<<" maxQ="<<hist.rbegin()->first<<" maxQ_count="<<hist[26]<<'\n';
    for(auto [q,c]:hist) if(q>=20) cout<<"Q="<<q<<" profiles="<<c<<'\n';
    for(int t=1;t<=4;++t) cout<<"t="<<t<<" m="<<288+t<<" raw="<<raw[t]<<" monotone="<<closed[t]<<" dcap="<<dcap[t]<<'\n';
    cout<<"saved_union_profiles="<<output_rows<<'\n';
}
