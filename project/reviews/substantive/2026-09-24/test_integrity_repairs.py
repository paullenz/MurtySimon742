#!/usr/bin/env python3
"""Positive and hostile transport/solver controls in temporary directories.

Run from the repository with Python, NumPy, SciPy and g++ installed. This
regenerates the published local 11,357-record fixture but performs no new
canonical graph search. No tracked input or historical result is overwritten.
"""
from pathlib import Path
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import types

ROOT = Path(__file__).resolve().parents[4]
CORE = ROOT/'project/research/general_n/2026-09-16-universal-core-defect-v1'
MODEL_DIR = ROOT/'project/research/general_n/2026-09-23-independent-742-r12-count-audit'


def load(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    report={}
    with tempfile.TemporaryDirectory(prefix='substantive-integrity-review-') as tmp:
        tmp=Path(tmp);source=tmp/'fixture';source.mkdir()
        for name in ('universal_core_impl.py','check_universal_core.cpp',
                     'universal_core_integrity.py','check_universal_core.py'):
            shutil.copyfile(CORE/name,source/name)
        generated=subprocess.run([sys.executable,'check_universal_core.py'],cwd=source,
                                 capture_output=True,text=True,timeout=180)
        if generated.returncode:
            raise RuntimeError(generated.stdout+generated.stderr)
        summary=json.loads(generated.stdout)
        if summary.get('records')!=11357 or summary.get('integrity_gate')!='PASS_PINNED_COUNT_HASH_AND_SIDECAR':
            raise RuntimeError('positive generation/replay gate failed')
        report['fresh_generation_records']=summary['records']
        report['input_sha256']=summary['input_sha256']
        report['decision_sha256']=summary['decision_sha256']
        controls=[]
        for case in ('complete','empty','one_record','changed_input',
                     'changed_decisions','changed_summary','changed_sidecar',
                     'gzip_only','optimized','changed_source','locked'):
            dest=tmp/case;shutil.copytree(source,dest)
            if case in ('empty','one_record'):
                for name in ('INPUT.txt','PYTHON_DECISIONS.tsv'):
                    data=(dest/name).read_bytes().splitlines(keepends=True)
                    (dest/name).write_bytes(b''.join(data[:int(case=='one_record')]))
            if case in ('changed_input','changed_decisions'):
                name='INPUT.txt' if case=='changed_input' else 'PYTHON_DECISIONS.tsv'
                data=bytearray((dest/name).read_bytes());data[0]^=1;(dest/name).write_bytes(data)
            if case=='changed_summary':
                p=dest/'CHECK_SUMMARY.json';s=json.loads(p.read_text());s['records']=0;p.write_text(json.dumps(s))
            if case=='changed_sidecar':(dest/'GRAPH_RECORDS.json').write_text('[]\n')
            if case=='changed_source':
                with (dest/'universal_core_impl.py').open('a') as f:f.write('\n# altered source\n')
            if case=='locked':(dest/'.universal-core-integrity.lock').write_text('other writer\n')
            if case=='gzip_only':
                for name in ('INPUT.txt','PYTHON_DECISIONS.tsv','CPP_DECISIONS.tsv','GRAPH_RECORDS.json'):(dest/name).unlink()
            args=[sys.executable]+(['-O'] if case=='optimized' else [])+['check_universal_core.py','--replay-only']
            p=subprocess.run(args,cwd=dest,capture_output=True,text=True,timeout=60)
            expected=0 if case in ('complete','gzip_only') else 2
            if p.returncode!=expected:raise RuntimeError(f'{case}: expected {expected}: {p.stdout}{p.stderr}')
            if expected!=0 and 'PASS_LOCAL_AND_INCIDENCE_CHECKS' in p.stdout:
                raise RuntimeError('failure leaked success output')
            controls.append({'case':case,'exit':p.returncode,'expected':expected})
        report['transport_controls']=controls
    models=[MODEL_DIR/'witness_deficit_exact_star_milp.py',MODEL_DIR/'witness_deficit_milp.py',
            ROOT/'project/research/general_n/2026-09-23-independent-742-r14-near-equality/witness_deficit_milp.py',
            ROOT/'project/research/general_n/2026-09-24-demand15-source-union-v1/witness_deficit_union_milp.py']
    controls=[]
    for number,path in enumerate(models):
        m=load('review_model_'+str(number),path)
        for status,x,fun in ((1,None,17.),(1,None,None),(0,None,17.),(0,[.5],.5),(0,[0],0.),(0,[1],1.),(2,None,None)):
            r=types.SimpleNamespace(status=status,x=x,fun=fun,message='controlled review input')
            try:m.validate_optimal_result(r,[1],[0],[1],[[(0,1)]],[1],[1]);accepted=True
            except RuntimeError:accepted=False
            expected=(status==2 or (status==0 and x==[1]))
            if accepted!=expected:raise RuntimeError(f'bad solver classification: {path}, {status}, {x}')
            controls.append({'model':str(path.relative_to(ROOT)),'status':status,'primal':x,'accepted':accepted})
    report['solver_controls']=controls
    sys.path.insert(0,str(MODEL_DIR))
    screen=load('review_row_screen',MODEL_DIR/'screen_exact_star_row.py')
    original=screen.solve_aggregated
    screen.profiles=lambda n,d:iter([(1,15,(8,7),(8,8))])
    try:
        screen.solve_aggregated=lambda *a,**k:{'status':1,'minimum_deficit':17}
        capture=io.StringIO()
        with contextlib.redirect_stdout(capture):exitcode=screen.main(18,10)
        final=json.loads([s[6:] for s in capture.getvalue().splitlines() if s.startswith('FINAL ')][-1])
        if exitcode!=2 or final['unresolved_count']!=1 or final['range_complete']:
            raise RuntimeError('row driver silently accepted an unresolved result')
        report['unresolved_driver_control']={'exit':exitcode,'unresolved_count':1,'range_complete':False}
    finally:screen.solve_aggregated=original
    report['status']='PASS_POSITIVE_AND_HOSTILE_CONTROLS'
    report['scope']='Stream/process/model-result handling; not external mathematical acceptance'
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
