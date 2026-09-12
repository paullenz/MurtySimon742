#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

static constexpr int A = 14;
vector<int> s;
long long total = 0;
map<int,long long> hist;
vector<vector<int>> frontier;

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

void rec(int pos, int lo) {
    if (pos == A) {
        ++total;
        int q = score_Q(s);
        ++hist[q];
        if (q >= 22) {
            vector<int> row;
            row.push_back(q);
            row.insert(row.end(), s.begin(), s.end());
            frontier.push_back(row);
        }
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

int main() {
    rec(0, 0);
    if (total != 20058300LL) return 1;
    if (hist[22] != 18 || hist[23] != 3) return 1;
    if (frontier.size() != 21) return 1;
    for (const auto& row : frontier) {
        for (int i = 1; i <= 14; ++i) {
            if (row[i] <= 0 || row[i] > 5) return 1;
        }
    }
    cout << "OK: 20,058,300 multisets; Q22=18 Q23=3; 21 total; all positive; max demand=5\n";
    return 0;
}
