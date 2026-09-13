#include <algorithm>
#include <cassert>
#include <chrono>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Strengthened all-excess orientation / selected-incidence relaxation.

For each scalar state and every source selected-degree profile q (up to
permutation inside equal-rho classes), this scanner asks whether some selected
label degrees x>=s can exist.  It uses:

  * exact lower-bound source-label incidence circulation;
  * canonical orientation compatibility D(u,w);
  * unordered-pair uniqueness and potential-pair degree caps;
  * the old one-dimensional orientation prefix cuts;
  * unordered-pair Hall flow;
  * target-capacity Hall flow; and
  * TOTAL_EXCESS_SOURCE_CAP.md, which keeps the selected-excess coupling while
    quantifying only total E=sum(x-s), rather than a fixed excess profile.

ALL_EXCESS_EXCLUDED is therefore a whole-scalar-state exclusion under the
stated canonical bridge assumptions. SURVIVES_RELAXATION is only survival of
these necessary conditions, not graph feasibility.
*/

struct Edge { int to, rev, cap; };
struct Dinic {
    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;
    Dinic(int n): n(n), g(n), level(n), it(n) {}
    void add(int u, int v, int cap) {
        Edge a{v, (int)g[v].size(), cap};
        Edge b{u, (int)g[u].size(), 0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q; level[s] = 0; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto const& e : g[u]) if (e.cap && level[e.to] < 0) {
                level[e.to] = level[u] + 1; q.push(e.to);
            }
        }
        return level[t] >= 0;
    }
    int dfs(int u, int t, int f) {
        if (u == t) return f;
        for (int& k = it[u]; k < (int)g[u].size(); ++k) {
            Edge& e = g[u][k];
            if (!e.cap || level[e.to] != level[u] + 1) continue;
            int z = dfs(e.to, t, min(f, e.cap));
            if (z) { e.cap -= z; g[e.to][e.rev].cap += z; return z; }
        }
        return 0;
    }
    int flow(int s, int t) {
        int ans = 0;
        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (int z = dfs(s, t, INT_MAX / 4)) ans += z;
        }
        return ans;
    }
};

struct State { int layer, id, a, b, t; vector<int> s, rho; };
struct Cls { int rho, cnt, qmax; };

static map<tuple<int,int,int>, vector<vector<int>>> part_cache;
static void gen_parts_rec(int pos, int cnt, int last, int mx, int rem,
                          vector<int>& cur, vector<vector<int>>& out) {
    if (pos == cnt) { if (rem == 0) out.push_back(cur); return; }
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

static void lower_edge(Dinic& F, vector<int>& bal,
                       int u, int v, int lo, int hi) {
    assert(0 <= lo && lo <= hi);
    F.add(u, v, hi - lo);
    bal[u] -= lo;
    bal[v] += lo;
}

static bool variable_incidence(const State& st,
                               const vector<int>& q,
                               const vector<int>& rho) {
    int n = q.size(), m = st.s.size();
    int S0 = n + m, T0 = S0 + 1, SS = T0 + 1, TT = SS + 1, N = TT + 1;
    Dinic F(N);
    vector<int> bal(N, 0);
    int Q = accumulate(q.begin(), q.end(), 0);

    for (int u = 0; u < n; ++u)
        lower_edge(F, bal, S0, u, q[u], q[u]);

    for (int u = 0; u < n; ++u)
        for (int i = 0; i < m; ++i)
            if (st.s[i] <= rho[u])
                lower_edge(F, bal, u, n + i, 0, 1);

    for (int i = 0; i < m; ++i) {
        int up = 0;
        for (int u = 0; u < n; ++u) if (st.s[i] <= rho[u]) ++up;
        if (st.s[i] > up) return false;
        lower_edge(F, bal, n + i, T0, st.s[i], up);
    }

    lower_edge(F, bal, T0, S0, 0, Q);

    int need = 0;
    for (int v = 0; v <= T0; ++v) {
        if (bal[v] > 0) { F.add(SS, v, bal[v]); need += bal[v]; }
        else if (bal[v] < 0) F.add(v, TT, -bal[v]);
    }
    return F.flow(SS, TT) == need;
}

struct OrientData {
    vector<vector<unsigned char>> D;
    vector<int> pairdeg, P, c;
    bool caps_ok = true, prefix_ok = true;
};

static OrientData orient_data(const State& st,
                              const vector<int>& q,
                              const vector<int>& rho,
                              int baseS,
                              int zero_labels) {
    int n = q.size();
    int Q = accumulate(q.begin(), q.end(), 0);
    int E = Q - baseS;
    assert(E >= 0);

    OrientData z;
    z.c.resize(n);
    for (int i = 0; i < n; ++i) z.c[i] = q[i] + rho[i];

    z.D.assign(n, vector<unsigned char>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (i != j && q[i] <= z.c[j] + 1 && q[j] <= z.c[i])
                z.D[i][j] = 1;

    z.pairdeg.assign(n, 0);
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if (z.D[i][j] || z.D[j][i]) {
                ++z.pairdeg[i]; ++z.pairdeg[j];
            }

    z.P.resize(n);
    long long sumP = 0;
    for (int i = 0; i < n; ++i) {
        int pcap = rho[i] + st.b - st.a - 1;
        pcap = min(pcap, st.b - 1 - q[i]);
        pcap = min(pcap, z.pairdeg[i] - q[i]);

        // TOTAL_EXCESS_SOURCE_CAP.md.  If q_i>k*, at least q_i-k*
        // selected incidences must use positive-demand labels, while k* zero-
        // demand incidences consume at least k* units of E.
        if (q[i] > 0) {
            int kstar = min(zero_labels, min(q[i], E));
            if (q[i] > kstar) {
                int extra = (E - kstar) / (q[i] - kstar);
                pcap = min(pcap, rho[i] + extra - 1);
            }
        }

        z.P[i] = pcap;
        if (pcap < 0) z.caps_ok = false;
        else sumP += pcap;
    }

    if (sumP < Q) z.caps_ok = false;

    if (z.caps_ok) {
        int maxc = *max_element(z.c.begin(), z.c.end());
        for (int k = 0; k <= maxc; ++k) {
            long long cap = 0;
            for (int i = 0; i < n; ++i) if (q[i] <= k + 1) cap += q[i];
            for (int j = 0; j < n; ++j) if (z.c[j] > k) cap += z.P[j];
            if (cap < Q) { z.prefix_ok = false; break; }
        }
    } else {
        z.prefix_ok = false;
    }
    return z;
}

static int pair_flow(const vector<int>& q, const OrientData& z) {
    int n = q.size();
    vector<pair<int,int>> pairs;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if (z.D[i][j] || z.D[j][i]) pairs.push_back({i,j});

    int SRC = n + pairs.size(), SNK = SRC + 1;
    Dinic F(SNK + 1);
    for (int i = 0; i < n; ++i) F.add(SRC, i, q[i]);
    for (int k = 0; k < (int)pairs.size(); ++k) {
        auto [i,j] = pairs[k];
        int node = n + k;
        if (z.D[i][j]) F.add(i, node, 1);
        if (z.D[j][i]) F.add(j, node, 1);
        F.add(node, SNK, 1);
    }
    return F.flow(SRC, SNK);
}

static int target_flow(const vector<int>& q, const OrientData& z) {
    int n = q.size(), SRC = 2 * n, SNK = SRC + 1;
    Dinic F(SNK + 1);
    for (int i = 0; i < n; ++i) F.add(SRC, i, q[i]);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (z.D[i][j]) F.add(i, n + j, 1);
    for (int j = 0; j < n; ++j) F.add(n + j, SNK, max(0, z.P[j]));
    return F.flow(SRC, SNK);
}

struct Result {
    long long profiles = 0, incidence_fail = 0, cap_fail = 0,
              prefix_fail = 0, pair_fail = 0, target_fail = 0;
    bool pass = false;
    int witnessQ = -1;
    vector<int> witness_q, witness_rho;
    double seconds = 0;
};

struct Scanner {
    const State& st;
    int baseS, zero_labels, Qmax;
    vector<Cls> cls;
    vector<int> tailmax, highbase;
    Result res;
    bool stop = false;

    Scanner(const State& s): st(s) {
        baseS = accumulate(st.s.begin(), st.s.end(), 0);
        zero_labels = count(st.s.begin(), st.s.end(), 0);

        map<int,int> cnt;
        for (int r : st.rho) ++cnt[r];
        for (auto [rho,c] : cnt) {
            int compatible_labels = 0;
            for (int demand : st.s) if (demand <= rho) ++compatible_labels;
            cls.push_back({rho, c, min(st.a - rho, compatible_labels)});
        }

        tailmax.assign(cls.size() + 1, 0);
        for (int i = (int)cls.size() - 1; i >= 0; --i)
            tailmax[i] = tailmax[i + 1] + cls[i].cnt * cls[i].qmax;

        int rsum = accumulate(st.rho.begin(), st.rho.end(), 0);
        long long incoming_global = rsum + 1LL * st.b * (st.b - st.a - 1);
        Qmax = min<long long>(tailmax[0], incoming_global);
        Qmax = min<long long>(Qmax, 1LL * st.b * (st.b - 1) / 2);

        highbase.resize(cls.size());
        for (int i = 0; i < (int)cls.size(); ++i) {
            int R = cls[i].rho, forced_later = 0;
            for (int demand : st.s) if (demand > R) forced_later += demand;
            highbase[i] = forced_later;
        }
    }

    void evaluate(const vector<int>& q, const vector<int>& rho, int Q) {
        ++res.profiles;
        if (!variable_incidence(st, q, rho)) {
            ++res.incidence_fail; return;
        }
        OrientData z = orient_data(st, q, rho, baseS, zero_labels);
        if (!z.caps_ok) { ++res.cap_fail; return; }
        if (!z.prefix_ok) { ++res.prefix_fail; return; }
        if (pair_flow(q, z) < Q) { ++res.pair_fail; return; }
        if (target_flow(q, z) < Q) { ++res.target_fail; return; }

        res.pass = true;
        res.witnessQ = Q;
        res.witness_q = q;
        res.witness_rho = rho;
        stop = true;
    }

    void rec(int ci, int used, int Q, vector<int>& q, vector<int>& rho) {
        if (stop) return;
        if (ci == (int)cls.size()) {
            if (used == Q) evaluate(q, rho, Q);
            return;
        }

        auto C = cls[ci];
        int lo = max(0, Q - used - tailmax[ci + 1]);
        int hi = min(C.cnt * C.qmax, Q - used);

        // Labels with base demand > current rho cannot be carried by any source
        // in the classes processed through this one.
        hi = min(hi, Q - highbase[ci] - used);
        if (lo > hi) return;

        vector<int> sums;
        for (int sm = lo; sm <= hi; ++sm)
            if (!parts(C.cnt, C.qmax, sm).empty()) sums.push_back(sm);

        double target = (double)(Q - used) * C.cnt /
            max(1, accumulate(cls.begin() + ci, cls.end(), 0,
                              [](int z, const Cls& x){ return z + x.cnt; }));
        stable_sort(sums.begin(), sums.end(), [&](int x, int y) {
            return abs(x - target) < abs(y - target);
        });

        for (int sm : sums) {
            for (auto const& pv : parts(C.cnt, C.qmax, sm)) {
                size_t old = q.size();
                q.insert(q.end(), pv.begin(), pv.end());
                rho.insert(rho.end(), C.cnt, C.rho);
                rec(ci + 1, used + sm, Q, q, rho);
                q.resize(old); rho.resize(old);
                if (stop) return;
            }
        }
    }

    Result run() {
        auto t0 = chrono::steady_clock::now();
        vector<int> q, rho;
        for (int Q = baseS; Q <= Qmax && !stop; ++Q)
            rec(0, 0, Q, q, rho);
        res.seconds = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        return res;
    }
};

static string vecstr(const vector<int>& v) {
    ostringstream o;
    for (size_t i = 0; i < v.size(); ++i) { if (i) o << ','; o << v[i]; }
    return o.str();
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: scan_orientation_total_excess_frontier INPUT OUTPUT.tsv\n";
        return 2;
    }
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    if (!in || !out) return 2;

    int N; in >> N;
    out << "layer\tstate_id\tmax_s\tS\tprofiles_tested\tincidence_fail\tcap_fail\t"
           "prefix_fail\tpair_fail\ttarget_fail\tstatus\twitness_Q\tseconds\t"
           "witness_rho\twitness_q\n";

    int excluded = 0, survived = 0;
    for (int z = 0; z < N; ++z) {
        State st; int ns, nr;
        in >> st.layer >> st.id >> st.a >> st.b >> st.t >> ns;
        st.s.resize(ns); for (int& x : st.s) in >> x;
        in >> nr; st.rho.resize(nr); for (int& x : st.rho) in >> x;

        Scanner sc(st);
        Result r = sc.run();
        string status = r.pass ? "SURVIVES_RELAXATION" : "ALL_EXCESS_EXCLUDED";
        if (r.pass) ++survived; else ++excluded;

        out << st.layer << '\t' << st.id << '\t'
            << *max_element(st.s.begin(), st.s.end()) << '\t'
            << accumulate(st.s.begin(), st.s.end(), 0) << '\t'
            << r.profiles << '\t' << r.incidence_fail << '\t' << r.cap_fail << '\t'
            << r.prefix_fail << '\t' << r.pair_fail << '\t' << r.target_fail << '\t'
            << status << '\t' << r.witnessQ << '\t' << r.seconds << '\t'
            << vecstr(r.witness_rho) << '\t' << vecstr(r.witness_q) << '\n';

        cerr << "state " << st.id << ' ' << status
             << " profiles=" << r.profiles << " Q=" << r.witnessQ
             << " sec=" << r.seconds << '\n';
    }
    cerr << "SUMMARY states=" << N << " all_excess_excluded=" << excluded
         << " survives=" << survived << '\n';
    return 0;
}
