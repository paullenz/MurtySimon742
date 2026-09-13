#!/usr/bin/env python3
"""Generate a diagnostic variant of the audited low-demand extension scanner.

This script makes only reporting changes to the existing scanner: it adds the
seven extension states and records the exact excess profile attaining the
reported minimum.  It does not change any feasibility test or objective.
"""
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_incidence_capacity_family.cpp"
OUT = HERE / "scan_low_demand_witness.generated.cpp"

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
    needle = " if(id==519)return {519,1,14,6,0,12,44,42};\n"
    assert raw.count(needle) == 1
    addition = "".join(
        f" if(id=={sid})return {{{sid},{n2},{n3},{r1},{r2},{r3},{S},{r}}};\n"
        for sid, n2, n3, r1, r2, r3, S, r in EXTRA
    )
    s = raw.replace(needle, needle + addition)

    glob = "static unordered_map<string,Corr> cachec;\n"
    assert s.count(glob) == 1
    s = s.replace(glob, glob + "static vector<int> DBG_E2,DBG_E3,CUR_E2,CUR_E3;\n")

    old = "    best=min(best,gap);\n"
    new = "    if(gap<best){best=gap;CUR_E2=a2.q;CUR_E3=a3.q;}\n"
    assert s.count(old) == 1
    s = s.replace(old, new)

    old = "if(gap<best){best=gap;bestq2=a2.q;bestq3=a3.q;besth=h;bestz=z;}"
    new = "if(gap<best){best=gap;bestq2=a2.q;bestq3=a3.q;besth=h;bestz=z;DBG_E2=CUR_E2;DBG_E3=CUR_E3;}"
    assert s.count(old) == 1
    s = s.replace(old, new)

    old = 'cout<<" q3=";for(int x:bestq3)cout<<x<<\',\';cout<<"\\n";\n}'
    new = 'cout<<" q3=";for(int x:bestq3)cout<<x<<\',\';cout<<"\\ne2=";for(int x:DBG_E2)cout<<x<<\',\';cout<<" e3=";for(int x:DBG_E3)cout<<x<<\',\';cout<<"\\n";\n}'
    assert s.count(old) == 1
    s = s.replace(old, new)

    OUT.write_text(s)
    print("BASE_SHA256", hashlib.sha256(raw.encode()).hexdigest())
    print("WITNESS_SHA256", hashlib.sha256(s.encode()).hexdigest())
    print("REPORTING_ONLY_PATCH", 1)


if __name__ == "__main__":
    main()
