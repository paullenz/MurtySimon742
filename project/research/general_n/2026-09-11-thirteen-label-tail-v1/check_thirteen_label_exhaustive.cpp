#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static constexpr int A = 13;
vector<int> s;
long long count_all = 0, count_q21 = 0;
int best_q = -1;
vector<int> best_profile;

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
    int Q = 0;
    for (int x : v) if (x >= 1) ++Q;
    for (int h = 2; h < A; ++h) {
        int N = 0, W = 0;
        for (int x : v) if (x >= h) { ++N; W += x; }
        if (N) Q += N - gamma_h(h, W);
    }
    return Q;
}

void rec(int pos, int lo) {
    if (pos == A) {
        ++count_all;
        int q = score_Q(s);
        if (q > best_q) { best_q = q; best_profile = s; }
        if (q == 21) {
            ++count_q21;
            if (!all_of(s.begin(), s.end(), [](int x){ return x == 3; })) {
                cerr << "unexpected Q=21 profile\n";
                exit(2);
            }
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
    if (count_all != 5200300LL || best_q != 21 || count_q21 != 1) return 1;
    cout << "OK: " << count_all << " multisets; max Q=" << best_q
         << "; unique maximizer=";
    for (int x : best_profile) cout << x;
    cout << "\n";
    return 0;
}
