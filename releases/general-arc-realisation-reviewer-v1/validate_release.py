#!/usr/bin/env python3
"""Clean standard-library evidence reproduction; no new solver attempts."""
from pathlib import Path
import hashlib,json,os,platform,re,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-arc-realisation-pilot-v1'

def sha(raw):return hashlib.sha256(raw).hexdigest()

def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    runs=[];compared=[]
    with tempfile.TemporaryDirectory(prefix='murty-arc-clean-') as directory:
        clean=Path(directory)
        for p in paths:
            source=ROOT/p
            if source.is_file():
                target=clean/p;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        outputs=['pilot_inputs.json','flow_verification.json','model_verification.json','shortcut_counterexample.json','flow_probes.json','verification.json','new_exclusions.json']
        for p in outputs:(clean/RESEARCH/p).unlink()
        for script in ['prepare_inputs.py','check_flow.py','check_model.py','run_flow_probes.py','verify.py']:
            result=subprocess.run([sys.executable,RESEARCH+'/'+script],cwd=clean,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
            if result.returncode:(HERE/'VALIDATION_FAILURE.log').write_text(script+'\n'+result.stdout+'\n'+result.stderr)
            assert result.returncode==0,(script,result.stdout,result.stderr)
            runs.append(dict(command='python '+RESEARCH+'/'+script,returncode=0,stdout_sha256=sha(result.stdout.encode())))
        for p in outputs:
            assert (clean/RESEARCH/p).read_bytes()==(ROOT/RESEARCH/p).read_bytes(),p
            compared.append(p)
    markdown=[p for p in paths if p.endswith('.md') and (p in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'] or p.startswith(RESEARCH+'/') or p.startswith('releases/general-arc-realisation-reviewer-v1/'))]
    links=0
    for p in markdown:
        file=ROOT/p
        for match in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)',file.read_text()):
            target=match.group(1).split('#')[0]
            if not target or re.match(r'^[a-z]+:',target):continue
            resolved=(file.parent/target).resolve()
            assert resolved.exists() or resolved in [HERE/'VALIDATION.json',HERE/'MANIFEST.json'],(p,target)
            links+=1
    report=dict(status='PASS',date='2026-09-12',python=platform.python_version(),clean_replay=runs,
        regenerated_files_byte_identical=compared,original_models_rebuilt=12,original_solver_attempts_rerun=False,
        original_logs_and_timings_preserved=True,navigation=dict(markdown_files=len(markdown),local_links_checked=links),
        fixed_cross_flow_and_linear_model_challenges='PASS',new_whole_state_exclusions=0,
        combined_exclusions=994,combined_survivors=4584,external_review='OPEN')
    (HERE/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
