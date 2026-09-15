#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path

if len(sys.argv)!=4:
    raise SystemExit("usage: aggregate_audit.py RESULTS_DIR CANDIDATE_KEYS.tsv OUT_DIR")
results_dir=Path(sys.argv[1]); key_path=Path(sys.argv[2]); outdir=Path(sys.argv[3]); outdir.mkdir(parents=True,exist_ok=True)

with key_path.open(newline="") as f:
    expected={(int(r["layer"]),int(r["state_id"])) for r in csv.DictReader(f,delimiter="\t")}

rows=[]
for p in sorted(results_dir.rglob("audit-*.json")):
    try:
        x=json.loads(p.read_text())
    except Exception as e:
        rows.append({"path":str(p),"parse_error":str(e)})
        continue
    rows.append(x)

parsed=[r for r in rows if "layer" in r and "state_id" in r]
keys={(int(r["layer"]),int(r["state_id"])) for r in parsed}
missing=sorted(expected-keys)
extra=sorted(keys-expected)
dupes=[]
seen=set()
for r in parsed:
    k=(int(r["layer"]),int(r["state_id"]))
    if k in seen: dupes.append(k)
    seen.add(k)
mismatches=[r for r in parsed if not r.get("match",False)]
parse_errors=[r for r in rows if "parse_error" in r]

summary={
    "schema":"forced-core-canonical-full-independent-audit-v1",
    "expected":len(expected),
    "result_json_files":len(rows),
    "unique_keys":len(keys),
    "matches":len(parsed)-len(mismatches),
    "mismatches":len(mismatches),
    "missing":missing,
    "extra":extra,
    "duplicate_keys":dupes,
    "parse_errors":parse_errors,
}
summary["pass"]=(len(expected)==170 and len(rows)==170 and len(keys)==170 and not mismatches and not missing and not extra and not dupes and not parse_errors)
(outdir/"FULL_AUDIT_SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")

with (outdir/"FULL_AUDIT_MATCHES.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["layer","state_id","match"])
    for r in sorted(parsed,key=lambda z:(int(z["layer"]),int(z["state_id"]))):
        if r.get("match",False): w.writerow([r["layer"],r["state_id"],1])

with (outdir/"FULL_AUDIT_MISMATCHES.json").open("w") as f:
    json.dump(mismatches,f,indent=2,sort_keys=True); f.write("\n")

print(json.dumps(summary,sort_keys=True))
if not summary["pass"]:
    raise SystemExit(1)
