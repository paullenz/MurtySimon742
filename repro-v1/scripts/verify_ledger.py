#!/usr/bin/env python3
import json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
L=json.load(open(root/'ledger/theorem_ledger.json'))
I=json.load(open(root/'ledger/paper_import_manifest.json'))
by={b['id']:b for b in L['branches']}
allowed=set(I['allowed_statuses']); fail=[]
for bid in I['branch_ids']:
 b=by.get(bid)
 if not b: fail.append(f'unknown import branch {bid}'); continue
 if b['status'] not in allowed or not b.get('theorem_dependency_allowed'):
  fail.append(f'UNCERTIFIED IMPORT {bid}: {b["status"]}')
for b in L['branches']:
 if b.get('theorem_dependency_allowed') and b['status'] not in allowed:
  fail.append(f'ledger allows dependency on disallowed status {b["id"]}: {b["status"]}')
for b in L['branches']:
 for e in b.get('evidence',[]):
  if not (root/e).exists() and not e.startswith('external/'):
   fail.append(f'missing evidence link {b["id"]}: {e}')
print(f"theorem ledger: {len(L['branches'])} branches; {len(I['branch_ids'])} allowed imports; {len(fail)} failures")
for x in fail: print(x,file=sys.stderr)
sys.exit(bool(fail))
