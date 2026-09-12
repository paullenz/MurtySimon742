#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,tempfile,time
HERE=Path(__file__).resolve().parent

def main():
    with tempfile.TemporaryDirectory(prefix='closed-potential-reference-') as directory:
        binary=Path(directory)/'reference'
        run=subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra','-o',str(binary),str(HERE/'reference.cpp')],capture_output=True,text=True)
        (HERE/'reference_compile.log').write_text(run.stdout+run.stderr);assert run.returncode==0,run.stderr
        start=time.monotonic()
        with (HERE/'engine_input.txt').open() as src,(HERE/'reference_results.jsonl').open('w') as out,(HERE/'reference.log').open('w') as log:
            run=subprocess.run([str(binary)],stdin=src,stdout=out,stderr=log)
        elapsed=time.monotonic()-start;assert run.returncode==0
    raw=(HERE/'reference_results.jsonl').read_bytes()
    report=dict(status='PASS',reference_bytes=len(raw),reference_sha256=hashlib.sha256(raw).hexdigest(),
        original_reference_seconds=elapsed,compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
        exact_full_enumeration=True,cardinality_dynamic_programming=True,external_review='OPEN')
    (HERE/'reference_environment.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
