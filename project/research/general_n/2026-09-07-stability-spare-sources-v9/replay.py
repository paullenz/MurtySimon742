#!/usr/bin/env python3
"""Replay v9 supporting checks. No universal or full Lean theorem is certified."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,time,shutil
ROOT=Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(root):
    m=json.loads((root/'MANIFEST.json').read_text())
    for name,e in m['files'].items():
        p=root/name
        if not p.is_file() or p.is_symlink() or p.stat().st_size!=e['bytes'] or digest(p)!=e['sha256']:
            raise ValueError('Integrity failure: '+name)
    formal=(root/'evidence/checked-source-sha256.txt').read_text().split()[0]
    if digest(root/'formal/QuasiCore.lean')!=formal:raise ValueError('Lean source mismatch')
    return {'payload_files':len(m['files']),'all_sha256_match':True,'formal_record_matches_source':True}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--verify-only',action='store_true');a=ap.parse_args()
    before=verify(ROOT)
    if a.verify_only:
        print(json.dumps({'integrity':before,'arithmetic_replayed':False,'lean_replayed':False},indent=2));return
    if a.output is None:ap.error('--output is required for the default full check')
    out=a.output.resolve()
    if out==ROOT or ROOT in out.parents or out.exists():raise ValueError('Output must be new and outside checkpoint')
    out.mkdir(parents=True);reports={};jobs=[];start=time.monotonic()
    for stem,expected in [('exact_checks','EXACT_ALGEBRA_REPORT.json'),('interval_check','INTERVAL_CHECK_REPORT.json'),('graph_checks','GRAPH_CHECK_REPORT.json'),('abstract_checks','ABSTRACT_CHECK_REPORT.json')]:
        log=out/(stem+'.log');target=out/expected;cmd=[sys.executable,'-I','-B',str(ROOT/'src'/f'{stem}.py'),'--output',str(target)]
        t=time.monotonic()
        with log.open('w') as f:proc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,check=False)
        if proc.returncode:raise RuntimeError(f'{stem} failed; see {log}')
        data=json.loads(target.read_text());prior=json.loads((ROOT/'evidence'/expected).read_text())
        if data!=prior:raise ValueError('Historical report mismatch: '+expected)
        jobs.append({'script':stem,'exit_code':0,'matches_recorded_report':True,'seconds':time.monotonic()-t});reports[stem]=data
    after=verify(ROOT)
    report={'all_checks_pass':True,'jobs':jobs,'seconds':time.monotonic()-start,'integrity':before,'original_payloads_unchanged':before==after,
      'actual_graph_systems':reports['graph_checks']['counts']['systems'],'actual_distinct_labelled_graphs':reports['graph_checks']['distinct_labelled_graphs'],
      'actual_positive_surplus_graphs':reports['graph_checks']['counts']['positive_surplus'],
      'actual_nonempty_spare_classes':reports['graph_checks']['counts']['nonempty_spare_classes'],
      'reduced_systems_with_exceptional_arcs':reports['abstract_checks']['valid_systems_with_exceptional_arcs'],
      'independent_specialist_review':'OPEN','universal_mathematical_proof_formally_verified':False,
      'lean_replayed':False,'recorded_lean_local_theorems':5,
      'scope':'Supporting finite algebra and regression checks only; not universal proof by enumeration; no n28 replay performed'}
    (out/'FULL_REPLAY_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
