#include <array>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

static constexpr int A = 15;
array<int,A> s{};
long long total = 0;
int bestQ = -1000;
long long bestCount = 0;
vector<array<int,A>> bestProfiles;

int cap(int h, int z) {
    return (z * (z - 1) + h * (h + 1)) / 2;
}

int gamma_h(int h, int W) {
    if (W <= 0) return 0;
    int z = h;
    while (W > cap(h, z)) ++z;
    return z;
}

int score_Q() {
    int q = 0;
    for (int x : s) if (x >= 1) ++q;
    for (int h = 2; h < A; ++h) {
        int N = 0, W = 0;
        for (int x : s) if (x >= h) { ++N; W += x; }
        if (N) q += N - gamma_h(h, W);
    }
    return q;
}

void rec(int pos, int lo) {
    if (pos == A) {
        ++total;
        int q = score_Q();
        if (q > bestQ) {
            bestQ = q;
            bestCount = 1;
            bestProfiles.clear();
            bestProfiles.push_back(s);
        } else if (q == bestQ) {
            ++bestCount;
            if (bestProfiles.size() < 10) bestProfiles.push_back(s);
        }
        if (q > 26) {
            cerr << "counterexample Q=" << q << "\n";
            exit(2);
        }
        return;
    }
    for (int x = lo; x < A; ++x) {
        s[pos] = x;
        rec(pos + 1, x);
    }
}

int main() {
    rec(0, 0);
    if (total != 77558760LL) return 1;
    if (bestQ != 26 || bestCount != 2) return 1;

    array<int,A> p1{};
    p1[0]=3; p1[1]=3;
    for (int i=2;i<A;++i) p1[i]=4;
    array<int,A> p2{};
    for (int i=0;i<A;++i) p2[i]=4;

    bool got1=false, got2=false;
    for (const auto& p : bestProfiles) {
        if (p==p1) got1=true;
        if (p==p2) got2=true;
    }
    if (!got1 || !got2) return 1;

    cout << "PASS: 77,558,760 multisets; max Q=26; equality exactly 3^2 4^13 and 4^15\n";
    return 0;
}
