// Independent local checker: adjacency matrix and explicit paths of length <=2.
// Input: record d tight_mask common_support probe_support common_probe_edge.
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using Matrix = std::vector<std::vector<bool>>;
bool short_path(const Matrix& a,int i,int j) {
    if(i==j || a[i][j]) return true;
    for(int v=0;v<(int)a.size();++v) if(a[i][v] && a[v][j]) return true;
    return false;
}
int main() {
    std::uint64_t id,q,cm,xm; int d,cx;
    while(std::cin >> id >> d >> q >> cm >> xm >> cx) {
        if(d<3 || d>9 || cx<0 || cx>1) throw std::runtime_error("invalid record");
        const int n=d+2; Matrix a(n,std::vector<bool>(n,false));
        unsigned b=0; int deg0=0,deg1=0;
        for(int i=0;i<d;++i) for(int j=i+1;j<d;++j,++b) {
            a[i][j]=a[j][i]=((q>>b)&1);
            if(a[i][j]) { if(i==0) ++deg0; if(i==1 || j==1) ++deg1; }
        }
        std::uint64_t full=(std::uint64_t(1)<<d)-1;
        int xs=__builtin_popcountll(xm);
        bool support=(xm==0 || xm==full || xs==d-1 || (xs==1 && cx==1));
        bool eligible=a[0][1] && deg0>=2 && deg1>=2 && cm==full && support;
        for(int i=0;i<d;++i) {
            a[i][d]=a[d][i]=(cm>>i)&1;
            a[i][d+1]=a[d+1][i]=(xm>>i)&1;
        }
        a[d][d+1]=a[d+1][d]=cx;
        Matrix before(n,std::vector<bool>(n,false)); bool diameter2=true;
        for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) {
            before[i][j]=short_path(a,i,j); diameter2=diameter2 && before[i][j];
        }
        a[0][1]=a[1][0]=false; std::uint64_t lost=0; b=0;
        for(int i=0;i<n;++i) for(int j=i+1;j<n;++j,++b)
            if(before[i][j] && !short_path(a,i,j)) lost |= std::uint64_t(1)<<b;
        std::cout << id << ' ' << eligible << ' ' << diameter2 << ' '
                  << __builtin_popcountll(lost) << ' ' << lost << '\n';
    }
    if(!std::cin.eof()) throw std::runtime_error("malformed input");
}
