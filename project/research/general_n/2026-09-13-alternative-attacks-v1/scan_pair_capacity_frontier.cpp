#include <algorithm>
#include <cassert>
#include <chrono>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Canonical pair-capacity frontier scanner.

This is intentionally a simpler and *larger-universe* scan than the exact
selected-incidence / Hall machinery.  For each scalar state it enumerates every
source selected-degree multiset q, up to permutation inside equal-rho classes,
subject only to

    0 <= q_u <= min(a-rho_u, #{i:s_i<=rho_u}),
    sum q_u = S+E.

No selected-incidence flow, base-demand prefix inequality, orientation Hall
flow, pair Hall flow, or weighted excess-budget flow is used.

For each q it applies only:

  p_u <= rho_u+b-a-1,
  p_u <= b-1-q_u,
  TOTAL_EXCESS_SOURCE_CAP.md (with its zero-demand correction),
  p_u <= d_KD(u)-q_u,

where K_D is the orientation-independent potential-pair graph induced by the
necessary directed compatibility

  D(u,w) iff u!=w, q_u<=q_w+rho_w+1, q_w<=q_u+rho_u.

If every q profile at every admissible E has total possible incoming capacity
strictly below Q=sum q=sum p (or a negative pointwise capacity), the whole
scalar state is excluded under these canonical bridge lemmas.  A passing q is
only survival of this relaxation, not graph feasibility.
*/

struct State {
    int layer, id, a, b, t;
    vector<int> s, rho;
};
struct Cls { int rho, cnt, qmax; };

static map<tuple<int,int,int>, vector<vector<int>>> part_cache;

static void gen_parts_rec(int pos, int cnt, int last, int mx, int rem,
                          vector<int>& cur, vector<vector<int>>& out) {
    if (pos == cnt) {
        if (rem == 0) out.push_back(cur);
        return;
    }
    int left = cnt - pos - 1;
    for (int x = last; x <= mx && x <= rem; ++x) {
        int rr = rem - x;
        if (rr < x * left || rr > mx * left) continue;
        cur[pos] = x;
        gen_parts_rec(pos + 1, cnt, x, mx, rr, cur, out);
    }
}

static const vector<vector<int>>& parts(int cnt, int mx, int sum) {
    auto key = make_tuple(cnt, mx, sum);
    auto it = part_cache.find(key);
    if (it != part_cache.end()) return it->second;
    vector<vector<int>> out;
    if (cnt == 0) {
        if (sum == 0) out.push_back({});
    } else if (sum >= 0 && sum <= cnt * mx) {
        vector<int> cur(cnt);
        gen_parts_rec(0, cnt, 0, mx, sum, cur, out);
    }
    return part_cache.emplace(key, move(out)).first->second;
}

struct ProfileResult {
    bool passes = false;
    int pre_margin = INT_MIN;
    int pair_margin = INT_MIN;
    vector<int> caps;
    vector<int> pairdeg;
};

static ProfileResult check_profile(const State& st, int E,
                                   const vector<int>& q,
                                   const vector<int>& rho) {
    const int n = (int)q.size();
    const int Q = accumulate(q.begin(), q.end(), 0);
    const int z = count(st.s.begin(), st.s.end(), 0);

    vector<int> c(n);
    for (int u = 0; u < n; ++u) c[u] = q[u] + rho[u];

    vector<int> basecap(n);
    long long base_sum = 0;
    bool base_nonnegative = true;
    for (int u = 0; u < n; ++u) {
        int p = min(rho[u] + st.b - st.a - 1, st.b - 1 - q[u]);
        if (q[u] > 0) {
            int kstar = min(z, min(q[u], E));
            if (q[u] > kstar) {
                int extra = (E - kstar) / (q[u] - kstar);
                p = min(p, rho[u] + extra - 1);
            }
        }
        basecap[u] = p;
        if (p < 0) base_nonnegative = false;
        else base_sum += p;
    }

    ProfileResult ans;
    ans.pre_margin = base_nonnegative ? (int)(base_sum - Q) : INT_MIN / 2;
    if (!base_nonnegative || base_sum < Q) return ans;

    vector<int> pairdeg(n, 0);
    auto D = [&](int u, int w) {
        return u != w && q[u] <= c[w] + 1 && q[w] <= c[u];
    };
    for (int u = 0; u < n; ++u) {
        for (int w = u + 1; w < n; ++w) {
            if (D(u,w) || D(w,u)) {
                ++pairdeg[u];
                ++pairdeg[w];
            }
        }
    }

    long long pair_sum = 0;
    bool pair_nonnegative = true;
    vector<int> caps(n);
    for (int u = 0; u < n; ++u) {
        int p = min(basecap[u], pairdeg[u] - q[u]);
        caps[u] = p;
        if (p < 0) pair_nonnegative = false;
        else pair_sum += p;
    }
    ans.pairdeg = move(pairdeg);
    ans.caps = move(caps);
    ans.pair_margin = pair_nonnegative ? (int)(pair_sum - Q) : INT_MIN / 2;
    ans.passes = pair_nonnegative && pair_sum >= Q;
    return ans;
}

struct StateResult {
    long long profiles = 0;
    long long pre_pair_passes = 0;
    long long pair_passes = 0;
    int best_pre_margin = INT_MIN;
    int best_pair_margin = INT_MIN;
    int witness_E = -1;
    vector<int> witness_q, witness_rho;
    bool survives = false;
    int Emax = -1;
    double seconds = 0.0;
};

struct Scanner {
    const State& st;
    int S, qmax_total, Emax;
    vector<Cls> cls;
    vector<int> suffix_qmax;
    StateResult res;
    bool stop = false;

    explicit Scanner(const State& s): st(s) {
        S = accumulate(st.s.begin(), st.s.end(), 0);
        map<int,int> counts;
        for (int r : st.rho) ++counts[r];
        for (auto [rho,cnt] : counts) {
            int label_count = count_if(st.s.begin(), st.s.end(),
                                       [&](int d){ return d <= rho; });
            int qmax = min(st.a - rho, label_count);
            cls.push_back({rho, cnt, max(0, qmax)});
        }
        suffix_qmax.assign(cls.size() + 1, 0);
        for (int i = (int)cls.size() - 1; i >= 0; --i)
            suffix_qmax[i] = suffix_qmax[i + 1] + cls[i].cnt * cls[i].qmax;
        qmax_total = suffix_qmax[0];

        int U = accumulate(st.rho.begin(), st.rho.end(), 0)
              + st.b * (st.b - st.a - 1);
        int Qmax = min({qmax_total, U, st.b * (st.b - 1) / 2});
        Emax = Qmax - S;
        res.Emax = Emax;
    }

    void evaluate(int E, const vector<int>& q, const vector<int>& rho) {
        ++res.profiles;
        ProfileResult pr = check_profile(st, E, q, rho);
        res.best_pre_margin = max(res.best_pre_margin, pr.pre_margin);
        if (pr.pre_margin >= 0) ++res.pre_pair_passes;
        res.best_pair_margin = max(res.best_pair_margin, pr.pair_margin);
        if (pr.passes) {
            ++res.pair_passes;
            res.survives = true;
            res.witness_E = E;
            res.witness_q = q;
            res.witness_rho = rho;
            stop = true;
        }
    }

    void rec(int ci, int used, int Q, int E,
             vector<int>& q, vector<int>& rho) {
        if (stop) return;
        if (ci == (int)cls.size()) {
            if (used == Q) evaluate(E, q, rho);
            return;
        }

        const Cls C = cls[ci];
        int lo = max(0, Q - used - suffix_qmax[ci + 1]);
        int hi = min(C.cnt * C.qmax, Q - used);
        if (lo > hi) return;

        vector<int> sums;
        for (int sm = lo; sm <= hi; ++sm)
            if (!parts(C.cnt, C.qmax, sm).empty()) sums.push_back(sm);

        // Central class sums tend to find a relaxation witness early. This is
        // only search ordering; excluded states still enumerate everything.
        int remaining_sources = 0;
        for (int j = ci; j < (int)cls.size(); ++j) remaining_sources += cls[j].cnt;
        double target = remaining_sources
            ? (double)(Q - used) * C.cnt / remaining_sources : 0.0;
        stable_sort(sums.begin(), sums.end(), [&](int x, int y) {
            return abs(x - target) < abs(y - target);
        });

        for (int sm : sums) {
            for (auto const& pv : parts(C.cnt, C.qmax, sm)) {
                size_t old = q.size();
                q.insert(q.end(), pv.begin(), pv.end());
                rho.insert(rho.end(), C.cnt, C.rho);
                rec(ci + 1, used + sm, Q, E, q, rho);
                q.resize(old); rho.resize(old);
                if (stop) return;
            }
        }
    }

    StateResult run() {
        auto t0 = chrono::steady_clock::now();
        vector<int> q, rho;
        if (Emax >= 0) {
            // Small E first; this is usually the tightest layer and often finds
            // a surviving relaxation witness quickly. Excluded states scan all.
            for (int E = 0; E <= Emax && !stop; ++E) {
                int Q = S + E;
                rec(0, 0, Q, E, q, rho);
            }
        }
        res.seconds = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        return res;
    }
};

static string vecstr(const vector<int>& v) {
    ostringstream out;
    for (size_t i = 0; i < v.size(); ++i) {
        if (i) out << ',';
        out << v[i];
    }
    return out.str();
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: scan_pair_capacity_frontier INPUT OUTPUT.tsv\n";
        return 2;
    }
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    if (!in || !out) return 2;

    int N; in >> N;
    out << "layer\tstate_id\tS\tEmax\tprofiles_tested\tpre_pair_passes\t"
           "pair_passes\tbest_pre_margin\tbest_pair_margin\tstatus\t"
           "witness_E\tseconds\twitness_rho\twitness_q\n";

    int excluded = 0, survived = 0;
    long long total_profiles = 0;
    for (int z = 0; z < N; ++z) {
        State st; int ns, nr;
        in >> st.layer >> st.id >> st.a >> st.b >> st.t >> ns;
        st.s.resize(ns); for (int& x : st.s) in >> x;
        in >> nr; st.rho.resize(nr); for (int& x : st.rho) in >> x;

        Scanner scan(st);
        StateResult r = scan.run();
        string status = r.survives ? "SURVIVES_PAIR_CAPACITY" : "PAIR_CAPACITY_EXCLUDED";
        if (r.survives) ++survived; else ++excluded;
        total_profiles += r.profiles;

        auto shown = [](int x){ return x <= INT_MIN/4 ? -999999999 : x; };
        out << st.layer << '\t' << st.id << '\t'
            << accumulate(st.s.begin(), st.s.end(), 0) << '\t' << r.Emax << '\t'
            << r.profiles << '\t' << r.pre_pair_passes << '\t' << r.pair_passes << '\t'
            << shown(r.best_pre_margin) << '\t' << shown(r.best_pair_margin) << '\t'
            << status << '\t' << r.witness_E << '\t' << r.seconds << '\t'
            << vecstr(r.witness_rho) << '\t' << vecstr(r.witness_q) << '\n';

        cerr << "state " << st.id << ' ' << status
             << " Emax=" << r.Emax << " profiles=" << r.profiles
             << " best_pair_margin=" << shown(r.best_pair_margin)
             << " sec=" << r.seconds << '\n';
    }
    cerr << "SUMMARY states=" << N
         << " pair_capacity_excluded=" << excluded
         << " survives=" << survived
         << " profiles=" << total_profiles << '\n';
    return 0;
}
