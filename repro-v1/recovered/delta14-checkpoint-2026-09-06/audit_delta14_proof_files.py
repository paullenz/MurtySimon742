#!/usr/bin/env python3
"""Check every proof file's two hashes and gzip integrity without trusting logs."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("proof_root")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.proof_root)
    rows = [json.loads(line) for line in (root/"manifest.jsonl").read_text().splitlines()]
    results = []
    for row in rows:
        entry = {k:row[k] for k in ("r", "core_index", "rho", "proof_path")}
        try:
            compressed = (root/row["proof_path"]).read_bytes()
            entry["compressed_hash_matches"] = hashlib.sha256(compressed).hexdigest() == row["proof_gzip_sha256"]
            raw = gzip.decompress(compressed)
            entry["payload_hash_matches"] = hashlib.sha256(raw).hexdigest() == row["proof_sha256"]
            entry["passed"] = entry["compressed_hash_matches"] and entry["payload_hash_matches"]
        except Exception as error:
            entry["passed"] = False
            entry["error"] = str(error)
        results.append(entry)
    report = {"root":str(root), "records":len(rows),
              "passed":sum(x["passed"] for x in results),
              "failed":sum(not x["passed"] for x in results), "results":results}
    Path(args.output).write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k != "results"}))
    print(json.dumps([x for x in results if not x["passed"]][:5], indent=2))


if __name__ == "__main__":
    main()
