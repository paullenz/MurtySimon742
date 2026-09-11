#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

static constexpr int A = 14;
vector<int> s;
long long count_all = 0, count_q23 = 0;
int best_q = -100;
vector<vector<int>> q23_profiles;

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
        ++count_all;
        int q = score_Q(s);
        if (q > best_q) best_q = q;
        if (q == 23) {
            ++count_q23;
            q23_profiles.push_back(s);
        }
        if (q > 23) {
            cerr << "unexpected score above 23\n";
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
    vector<vector<int>> expected = {
        vector<int>(14, 3),
        [](){ vector<int> v(14, 4); v[0] = 3; return v; }(),
        vector<int>(14, 4)
    };
    if (count_all != 20058300LL || best_q != 23 || count_q23 != 3 ||
        q23_profiles != expected) return 1;
    cout << "OK: " << count_all << " multisets; max Q=" << best_q
         << "; exactly three maximizers: 3^14, 3 4^13, 4^14\n";
    return 0;
}
