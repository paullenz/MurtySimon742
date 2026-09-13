#!/usr/bin/env python3
"""Generate an exact low-demand extension scanner from the audited adjacent scanner.

The mathematics and search logic are copied byte-for-byte from
scan_incidence_capacity_family.cpp.  This generator only extends the frozen
state-profile table with the seven active records found by
prepare_low_demand_flow_family.py.

Keeping the transformation this small makes the first extension experiment a
regression of the already-audited relaxation rather than a simultaneous code
rewrite.
"""
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_incidence_capacity_family.cpp"
OUT = HERE / "scan_low_demand_extension.generated.cpp"

# state_id: n2,n3,r1,r2,r3,S,r
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
        f" if(id=={sid})return {{{sid},{n2},{n3},{r1},{r2},{r3},{S},{r}}};\\n"
        for sid, n2, n3, r1, r2, r3, S, r in EXTRA
    ).replace("\\n", "\n")
    generated = raw.replace(needle, needle + addition)
    OUT.write_text(generated)
    print("BASE_SHA256", hashlib.sha256(raw.encode()).hexdigest())
    print("GENERATED_SHA256", hashlib.sha256(generated.encode()).hexdigest())
    print("EXTRA_STATES", " ".join(str(x[0]) for x in EXTRA))


if __name__ == "__main__":
    main()
