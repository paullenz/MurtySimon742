#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

static constexpr int A = 14;
vector<int> s;
long long total = 0;
map<int,long long> hist;
long long frontier_count = 0;
long long zero_count = 0;
ofstream csvout;

int cap(int h, int z) {
    return (z * (z - 1) + h * (h + 1)) / 2;
}

int gamma_h(int h, int W) {
    if (W <= 0) return 0;
    int z = h;
    while (W > cap(h, z)) ++z;
    return z;
}

int score_Q(const vector<int>& v) {
    int q = 0;
    for (int x : v) if (x >= 1) ++q;
    for (int h = 2; h < A; ++h) {
        int N = 0, W = 0;
        for (int x : v) if (x >= h) { ++N; W += x; }
        if (N) q += N - gamma_h(h, W);
    }
    return q;
}

void emit(int q) {
    ++frontier_count;
    if (s.front() == 0) ++zero_count;
    if (csvout.is_open()) {
        csvout << q;
        for (int x : s) csvout << ',' << x;
        csvout << '\n';
    }
}

void rec(int pos, int lo) {
    if (pos == A) {
        ++total;
        int q = score_Q(s);
        ++hist[q];
        if (q >= 19) emit(q);
        if (q > 23) {
            cerr << "unexpected Q>23\n";
            exit(2);
        }
        return;
    }
    for (int x = lo; x < A; ++x) {
        s.push_back(x);
        rec(pos + 1, x);
        s.pop_back();
    }
}

int main(int argc, char** argv) {
    if (argc == 3 && string(argv[1]) == "--csv") {
        csvout.open(argv[2]);
        if (!csvout) return 3;
    } else if (argc != 1) {
        cerr << "usage: check_n32_t1_frontier [--csv OUTPUT.csv]\n";
        return 3;
    }

    rec(0, 0);

    if (total != 20058300LL) return 1;
    if (hist[19] != 206 || hist[20] != 104 || hist[21] != 50 ||
        hist[22] != 18 || hist[23] != 3) return 1;
    if (frontier_count != 381) return 1;
    if (zero_count != 36) return 1;

    cout << "PASS: 20,058,300 multisets; "
         << "Q19=206 Q20=104 Q21=50 Q22=18 Q23=3; "
         << "381 frontier profiles; 36 zero-demand profiles\n";
    return 0;
}
