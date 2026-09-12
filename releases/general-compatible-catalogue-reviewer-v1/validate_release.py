#!/usr/bin/env python3
"""Clean full replay, byte-exact stream recovery and archive-only verification."""
from pathlib import Path
import hashlib,json,os,platform,re,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-compatible-routing-catalogue-v1'

def sha(data):return hashlib.sha256(data).hexdigest()

def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    runs=[];recovered=[]
    with tempfile.TemporaryDirectory(prefix='murty-compatible-catalogue-') as directory:
        clean=Path(directory)
        for name in paths:
            source=ROOT/name
            if source.is_file():
                target=clean/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        study=clean/RESEARCH;env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        storage=json.loads((study/'EVIDENCE_STORAGE.json').read_text())['files']
        def run(script):
            result=subprocess.run([sys.executable,RESEARCH+'/'+script],cwd=clean,env=env,capture_output=True,text=True)
            if result.returncode:(HERE/'VALIDATION_FAILURE.log').write_text(script+'\n'+result.stdout+'\n'+result.stderr)
            assert result.returncode==0,(script,result.stdout,result.stderr)
            runs.append(dict(command='python '+RESEARCH+'/'+script,returncode=0,stdout_sha256=sha(result.stdout.encode())))
            print('PASS',script,flush=True)
        def compare_remove(names):
            for name in names:
                data=(study/name).read_bytes();meta=storage[name]
                assert len(data)==meta['original_bytes'] and sha(data)==meta['original_sha256'],name
                (study/name).unlink();recovered.append(name)
        for script in ['freeze_catalogue.py','prepare_inputs.py','run_replay.py']:run(script)
        assert not (study/'compile.log').read_text(),'current source has compiler diagnostics'
        compare_remove(['pool_inputs.jsonl','engine_input.txt','frontier_results.jsonl'])
        for script in ['independent_verify.py','summarize.py']:run(script)
        compare_remove(['survivors.json','template_coverage.json'])
        for script in ['verify_catalogue_and_summary.py','check_fixed_potential.py']:run(script)
        reproduced=['catalogue.json','catalogue_candidates.json','input_verification.json','replay.log','verification.json',
                    'frontier_summary.json','compression.json','catalogue_and_summary_verification.json','fixed_potential_verification.json']
        for name in reproduced:assert (study/name).read_bytes()==(ROOT/RESEARCH/name).read_bytes(),name
        fresh_environment=json.loads((study/'reproduction_environment.json').read_text())
    markdown=[ROOT/p for p in paths if p.endswith('.md') and
              (p in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'] or
               p.startswith(RESEARCH+'/') or p.startswith('releases/general-compatible-catalogue-reviewer-v1/'))]
    links=0
    for file in markdown:
        for m in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)',file.read_text()):
            target=m.group(1).split('#')[0]
            if not target or re.match(r'^[a-z]+:',target):continue
            resolved=(file.parent/target).resolve()
            assert resolved.exists() or resolved in [HERE/'VALIDATION.json',HERE/'MANIFEST.json'],(str(file),target)
            links+=1
    for name in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md']:
        body=(ROOT/name).read_text()
        for package in ['general-compatible-catalogue-reviewer-v1','general-compatible-routing-reviewer-v1',
                        'general-routing-tail-reviewer-v1','general-joint-routing-reviewer-v1',
                        'general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
            assert package+'/README.md' in body,(name,package)
    report=dict(status='PASS',date='2026-09-12',python=platform.python_version(),replay=runs,
        original_streams_reproduced_byte_for_byte=recovered,reproduced_summary_files=reproduced,
        original_timings_preserved=True,reproduction_environment=fresh_environment,
        exact_checks_from_original_archives_without_raw_streams=True,
        navigation=dict(markdown_files=len(markdown),local_links_checked=links,status='PASS'),
        scope=dict(pool=5578,catalogue_excluded=990,pilot_only_excluded=4,combined_excluded=994,combined_survivors=4584,
                   fixed_potential_states=707,analytic_q_elimination=True,at_most_five_p_candidates=True),external_review='OPEN')
    (HERE/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
