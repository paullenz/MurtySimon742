#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit("usage: compare_one.py INDEPENDENT.tsv PRIMARY.tsv OUT.json")

ind_path, primary_path, out_path = map(Path, sys.argv[1:])
with ind_path.open(newline="") as f:
    ind_rows = list(csv.DictReader(f, delimiter="\t"))
if len(ind_rows) != 1:
    raise SystemExit(f"expected one independent row, got {len(ind_rows)}")
ind = ind_rows[0]
key=(int(ind["layer"]), int(ind["state_id"]))

with primary_path.open(newline="") as f:
    prims={(int(r["layer"]),int(r["state_id"])):r for r in csv.DictReader(f,delimiter="\t")}
if key not in prims:
    raise SystemExit(f"missing primary key {key}")
prim=prims[key]
fields=[
    "S","Emax","profiles_tested","paircap_fail","paircap_pass",
    "incidence_fail","incidence_pass","pairhall_fail","pairhall_pass",
    "targethall_fail","targethall_pass","cost_fail","cost_pass",
    "core_fail","core_capacity_fail","core_high_fail","status"
]
diffs={f:{"primary":prim[f],"independent":ind[f]} for f in fields if prim[f] != ind[f]}
out={
    "schema":"forced-core-canonical-independent-audit-row-v1",
    "layer":key[0],
    "state_id":key[1],
    "fields_compared":fields,
    "match":not diffs,
    "differences":diffs,
}
out_path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,sort_keys=True))
