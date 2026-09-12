#!/usr/bin/env python3
"""Clean rediscovery comparison, original-archive checks and navigation."""
from pathlib import Path
import base64,gzip,hashlib,json,os,platform,re,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-compatible-routing-pilot-v1'

def sha(data):return hashlib.sha256(data).hexdigest()

def without_attempt_times(records):
    copy=json.loads(json.dumps(records))
    for record in copy:
        for attempt in record['attempts']:del attempt['seconds']
    return copy

def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    runs=[]
    with tempfile.TemporaryDirectory(prefix='murty-compatible-routing-') as directory:
        clean=Path(directory)
        for name in paths:
            source=ROOT/name
            if source.is_file():
                target=clean/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        study=clean/RESEARCH
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        meta=json.loads((study/'EVIDENCE_STORAGE.json').read_text())['files']['pilot_results.jsonl']
        stored=(study/meta['stored_file']).read_bytes()
        assert len(stored)==meta['stored_bytes'] and sha(stored)==meta['stored_sha256']
        original=gzip.decompress(base64.b64decode(stored))
        assert len(original)==meta['original_bytes'] and sha(original)==meta['original_sha256']
        expected=[json.loads(line) for line in original.splitlines()]
        assert len(expected)==meta['records']
        def run(script):
            result=subprocess.run([sys.executable,RESEARCH+'/'+script],cwd=clean,env=env,capture_output=True,text=True)
            if result.returncode:
                (HERE/'VALIDATION_FAILURE.log').write_text(script+'\n'+result.stdout+'\n'+result.stderr)
            assert result.returncode==0,(script,result.stdout,result.stderr)
            runs.append(dict(command='python '+RESEARCH+'/'+script,returncode=0,stdout_sha256=sha(result.stdout.encode())))
            print('PASS',script,flush=True)
        run('select_pilot.py')
        assert (study/'pilot_inputs.json').read_bytes()==(ROOT/RESEARCH/'pilot_inputs.json').read_bytes()
        run('probe.py')
        fresh=[json.loads(line) for line in (study/'pilot_results.jsonl').read_bytes().splitlines()]
        assert without_attempt_times(fresh)==without_attempt_times(expected),'rediscovery result fields differ'
        fresh_summary=json.loads((study/'summary.json').read_text());original_summary=json.loads((ROOT/RESEARCH/'summary.json').read_text())
        del fresh_summary['seconds'];del original_summary['seconds']
        assert fresh_summary==original_summary
        # Raw discovery is removed: all subsequent evidence reads must use the
        # original archive, whose exact recovery was checked above.
        (study/'pilot_results.jsonl').unlink()
        for script in ['verify_selection.py','independent_verify.py','extract_envelopes.py','verify_envelopes.py','check_routing.py','check_compact.py']:
            run(script)
        reproduced=['pilot_inputs.json','selection_verification.json','verification.json','envelopes.json',
                    'envelope_verification.json','routing_verification.json','compact_verification.json']
        for name in reproduced:
            assert (study/name).read_bytes()==(ROOT/RESEARCH/name).read_bytes(),name
    markdown=[ROOT/p for p in paths if p.endswith('.md') and
              (p in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'] or
               p.startswith(RESEARCH+'/') or p.startswith('releases/general-compatible-routing-reviewer-v1/'))]
    links=0
    for file in markdown:
        for m in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)',file.read_text()):
            target=m.group(1).split('#')[0]
            if not target or re.match(r'^[a-z]+:',target):continue
            # The report and manifest are generated at the end of packaging.
            resolved=(file.parent/target).resolve()
            assert resolved.exists() or resolved in [HERE/'VALIDATION.json',HERE/'MANIFEST.json'],(str(file),target)
            links+=1
    for name in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md']:
        body=(ROOT/name).read_text()
        for package in ['general-compatible-routing-reviewer-v1','general-routing-tail-reviewer-v1',
                        'general-joint-routing-reviewer-v1','general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
            assert package+'/README.md' in body,(name,package)
    report=dict(status='PASS',date='2026-09-12',python=platform.python_version(),replay=runs,
        original_archive_recovered=dict(bytes=len(original),sha256=sha(original),records=len(expected)),
        rediscovery_all_result_fields_except_attempt_seconds_identical=True,
        rediscovery_all_summary_fields_except_total_seconds_identical=True,
        original_timing_evidence_preserved=True,reproduced_byte_identical_files=reproduced,
        exact_checks_from_original_archive_without_raw_stream=True,
        navigation=dict(markdown_files=len(markdown),local_links_checked=links,status='PASS'),
        scope=dict(sample=29,excluded=19,survivors=10,additional_from_eligibility=16,
                   additional_whole_states_from_mixed_cuts=0,full_pool_replay=False),external_review='OPEN')
    (HERE/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
