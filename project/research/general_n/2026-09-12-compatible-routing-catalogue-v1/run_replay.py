#!/usr/bin/env python3
"""Compile and run the exact engine; keep fresh runtime separate from original."""
from pathlib import Path
import json,platform,subprocess,tempfile,time
HERE=Path(__file__).resolve().parent

def main():
    with tempfile.TemporaryDirectory(prefix='compatible-catalogue-engine-') as directory:
        binary=Path(directory)/'replay'
        command=['g++','-std=c++17','-O2','-Wall','-Wextra','-o',str(binary),str(HERE/'replay.cpp')]
        result=subprocess.run(command,capture_output=True,text=True)
        (HERE/'compile.log').write_text(result.stdout+result.stderr)
        assert result.returncode==0,result.stderr
        start=time.monotonic()
        with (HERE/'engine_input.txt').open() as source,(HERE/'frontier_results.jsonl').open('w') as out,(HERE/'replay.log').open('w') as log:
            result=subprocess.run([str(binary)],stdin=source,stdout=out,stderr=log)
        elapsed=time.monotonic()-start
    report=dict(python=platform.python_version(),compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
        exit_code=result.returncode,reproduction_seconds=elapsed,solver_used=False)
    (HERE/'reproduction_environment.json').write_text(json.dumps(report,indent=2)+'\n')
    assert result.returncode==0
    print((HERE/'replay.log').read_text(),end='')

if __name__=='__main__':main()
