#!/usr/bin/env python3
"""Generate a strengthened low-demand scanner using endpoint-budget complement.

The only mathematical strengthening is this: if Z is the set of zero-excess
demand-two labels, then

    sum_{i in Z} C_i = (r+Q) - sum_{i notin Z} C_i.

For every complementary label, selected-source forcing gives an upper order-
statistic bound on d_i, hence on C_i=d_i+e_i.  This supplies a second lower
bound on the aggregate endpoint mass of Z.  We take the maximum of that bound
and the existing zero-excess endpoint-order bound.  All other search logic is
copied from the audited incidence-capacity scanner.
"""
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_incidence_capacity_family.cpp"
OUT = HERE / "scan_endpoint_budget.generated.cpp"
EXTRA = [
    (283, 3, 12, 5, 4, 9, 42, 40),
    (153, 5, 10, 7, 2, 9, 40, 38),
    (231, 4, 11, 5, 5, 8, 41, 39),
    (154, 5, 10, 6, 4, 8, 40, 38),
    (122, 6, 9, 7, 3, 8, 39, 37),
    (77, 7, 8, 7, 4, 7, 38, 36),
    (60, 8, 7, 7, 5, 6, 37, 35),
]


def main():
    raw = SRC.read_text()
    s = raw
    needle = " if(id==519)return {519,1,14,6,0,12,44,42};\n"
    assert s.count(needle) == 1
    addition = "".join(
        f" if(id=={sid})return {{{sid},{n2},{n3},{r1},{r2},{r3},{S},{r}}};\n"
        for sid, n2, n3, r1, r2, r3, S, r in EXTRA
    )
    s = s.replace(needle, needle + addition)

    oldsig = "static long long profile_source_objective(const State&st,const vector<int>&q2,const vector<int>&q3,\n                                          const vector<int>&e2,const vector<int>&e3,int z,int Q){"
    newsig = "static long long profile_source_objective(const State&st,const vector<int>&q2,const vector<int>&q3,\n                                          const vector<int>&e2,const vector<int>&e3,int z,int Q,long long zfloor){"
    assert s.count(oldsig) == 1
    s = s.replace(oldsig, newsig)

    oldcost = "best=min(best,cost+1LL*z*lam);"
    newcost = "best=min(best,cost+max(1LL*z*lam,zfloor));"
    assert s.count(oldcost) == 1
    s = s.replace(oldcost, newcost)

    marker = "static long long refine_profile_branch(const State&st,int E,const vector<int>&q2,const vector<int>&q3,\n"
    assert s.count(marker) == 1
    helper = r'''static long long zero2_complement_floor(const State&st,const vector<int>&e2,const vector<int>&e3,
                                              const vector<int>&score2,const vector<int>&score3){
 long long E=0,ub=0;for(int e:e2)E+=e;for(int e:e3)E+=e;
 for(int e:e2){if(e==0)continue;int x=2+e;if(x>(int)score2.size())return INF;ub+=e+score2[x-1];}
 for(int e:e3){int x=3+e;if(x>(int)score3.size())return INF;ub+=e+score3[x-1];}
 long long totalC=st.r+st.S+E;
 return max(0LL,totalC-ub);
}

'''
    s = s.replace(marker, helper + marker)

    oldcall = "    long long so=profile_source_objective(st,q2,q3,a2.q,a3.q,z,Q);if(so==INF)continue;"
    newcall = "    long long zfloor=z?zero2_complement_floor(st,a2.q,a3.q,score2,score3):0;if(zfloor==INF)continue;\n    long long so=profile_source_objective(st,q2,q3,a2.q,a3.q,z,Q,zfloor);if(so==INF)continue;"
    assert s.count(oldcall) == 1
    s = s.replace(oldcall, newcall)

    OUT.write_text(s)
    print("BASE_SHA256", hashlib.sha256(raw.encode()).hexdigest())
    print("GENERATED_SHA256", hashlib.sha256(s.encode()).hexdigest())
    print("STRENGTHENING", "endpoint-budget-complement")


if __name__ == "__main__":
    main()
