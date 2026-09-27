"""Offline acceptance tests: fake Codex, local Git fixtures, real process/crash tests.
These never sign in, invoke a model, or make a paid/network request.
"""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import worker as w

FAKE = r'''#!/usr/bin/env python3
import json, os, sys, time
from pathlib import Path
base=Path(__file__)
mode=base.with_suffix('.mode').read_text().strip()
if 'app-server' in sys.argv:
    for line in sys.stdin:
        req=json.loads(line)
        if 'id' not in req: continue
        if req['method']=='initialize': ans={}
        elif req['method']=='account/read':
            ans={'account':{'type':'chatgpt','planType':'pro'},'requiresOpenaiAuth':True}
        elif req['method']=='account/rateLimits/read':
            credits={'hasCredits':mode=='paid','unlimited':False}
            bucket={'primary':{'usedPercent':99 if mode=='quota' else 10},'credits':credits}
            if mode=='unknown_credit': bucket.pop('credits')
            ans={'rateLimits':bucket}
        else: sys.exit(5)
        print(json.dumps({'id':req['id'],'result':ans}),flush=True)
    sys.exit(0)
if 'exec' not in sys.argv: sys.exit(8)
prompt=sys.stdin.read()
data=json.loads(prompt.split('\n\n',1)[1])
jid=data['task']['id']
with open(base.with_suffix('.calls'),'a') as f: f.write(jid+'\n'); f.flush(); os.fsync(f.fileno())
result={'job_id':jid,'scope':'hall-mincut-pilot','outcome':'review',
        'report_markdown':'OFFLINE FAKE RESULT. No mathematics performed. '+('fixture text; '*15),
        'unresolved':['This is a fake backend, not mathematical evidence.']}
def emit(e): print(json.dumps(e),flush=True)
if mode!='empty':
    emit({'type':'thread.started','thread_id':'fixture-'+jid})
    emit({'type':'turn.started'})
if mode=='slow': time.sleep(3)
if mode=='long': time.sleep(30)
if mode=='failure': sys.exit(7)
if mode=='wrong_id': result['job_id']='not-the-job'
Path(sys.argv[sys.argv.index('--output-last-message')+1]).write_text(json.dumps(result))
if mode not in ('empty','truncated'):
    emit({'type':'item.completed','item':{'type':'agent_message','text':json.dumps(result)}})
    emit({'type':'turn.completed','usage':{'input_tokens':0,'output_tokens':0}})
'''


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.repo=self.root/'repo'; self.repo.mkdir()
        def git(*args):
            return subprocess.check_output(['git','-C',str(self.repo),*args],stderr=subprocess.DEVNULL)
        git('init'); git('config','user.name','Offline test'); git('config','user.email','test@example.invalid')
        (self.repo/'CURRENT_STATE.md').write_text('Historical scheduled research is paused.\n')
        p=self.repo/w.PACKAGE; p.mkdir(parents=True)
        (p/'ABSTRACT_CROSSING_DOMINANCE.md').write_text('OFFLINE definition fixture only.\n')
        (p/'MANUSCRIPT.md').write_text('OFFLINE manuscript fixture only.\n')
        git('add','.'); git('commit','-m','fixture')
        self.fake=self.root/'fake-codex.py'; self.fake.write_text(FAKE); self.fake.chmod(0o700)
        self.mode('ok')
        self.state=self.root/'state'
        with contextlib.redirect_stdout(io.StringIO()): w.init(self.state,self.repo,str(self.fake))
        self.envpatch=patch.dict(os.environ,{k:os.environ[k] for k in ('PATH','HOME','LANG') if k in os.environ},clear=True)
        self.envpatch.start()
        self.enable()

    def tearDown(self):
        self.envpatch.stop(); self.temp.cleanup()

    def mode(self,mode): self.fake.with_suffix('.mode').write_text(mode)
    def enable(self):
        s=w.readj(self.state/'settings.json'); s['enabled']=True
        s['billing_confirmation']={'auto_reload_disabled':True,'no_purchased_credits':True,
            'personal_included_plan':True,'confirmed_at_unix':time.time()}
        w.atomic(self.state/'settings.json',w.blob(s))
    def settings(self,**kwargs):
        s=w.readj(self.state/'settings.json'); s.update(kwargs)
        w.atomic(self.state/'settings.json',w.blob(s))
    def calls(self):
        p=self.fake.with_suffix('.calls'); return p.read_text().splitlines() if p.exists() else []
    def records(self):
        c=w.db(self.state)
        try:return [dict(x) for x in c.execute('SELECT * FROM jobs ORDER BY id')]
        finally:c.close()
    def command(self,*args):
        return [sys.executable,str(Path(w.__file__).resolve()),'--state',str(self.state),*args]
    def runcli(self,*args):
        return subprocess.run(self.command(*args),capture_output=True,text=True,timeout=20)
    def waitfor(self,predicate,timeout=8):
        end=time.monotonic()+timeout
        while time.monotonic()<end:
            if predicate(): return
            time.sleep(.04)
        self.fail('Timed out waiting for test event')
    def firstfolder(self):
        return next((self.state/'attempts').glob('*'))
    def account(self):return {'account':{'type':'chatgpt','planType':'pro'}}
    def limits(self):return {'rateLimits':{'primary':{'usedPercent':20},'credits':{'hasCredits':False,'unlimited':False}}}

    def test_disabled_is_default(self):
        other=self.root/'other'
        with contextlib.redirect_stdout(io.StringIO()):w.init(other,self.repo,str(self.fake))
        with self.assertRaises(w.Blocked):w.policy(other)
        self.assertEqual(self.calls(),[])

    def test_full_pilot_and_idempotent_restart(self):
        p=self.runcli('run'); self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual([j['status'] for j in self.records()],['saved_unreviewed']*3)
        self.assertEqual(len(self.calls()),3)
        self.assertEqual(self.runcli('run').returncode,0)
        self.assertEqual(len(self.calls()),3)

    def test_reject_paid_credits_before_model_launch(self):
        self.mode('paid'); p=self.runcli('run')
        self.assertEqual(p.returncode,2); self.assertEqual(self.calls(),[])

    def test_missing_credit_data_is_unknown_not_zero(self):
        self.mode('unknown_credit'); self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.calls(),[])

    def test_usage_limit_pauses_without_retries(self):
        self.mode('quota'); self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.calls(),[])

    def test_api_auth_rejected(self):
        a=self.account(); a['account']['type']='apiKey'
        with self.assertRaises(w.Blocked):w.validate_account(a,self.limits(),80)

    def test_paid_workspace_or_unknown_plan_rejected(self):
        for plan in ('business','enterprise','unknown'):
            a=self.account(); a['account']['planType']=plan
            with self.assertRaises(w.Blocked):w.validate_account(a,self.limits(),80)

    def test_no_api_environment_fallback(self):
        with patch.dict(os.environ,{'OPENAI_API_KEY':'test-not-a-real-key'}):
            with self.assertRaises(w.Blocked):w.policy(self.state)
        self.assertEqual(self.calls(),[])

    def test_completed_queue_is_revalidated_on_restart(self):
        self.assertEqual(self.runcli('run').returncode,0)
        folder=self.state/'attempts'/self.records()[0]['attempt']
        (folder/'result.json').write_text('{}')
        self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.records()[0]['status'],'needs_attention')
        self.assertEqual(len(self.calls()),3)

    def test_custom_endpoint_rejected(self):
        with patch.dict(os.environ,{'OPENAI_BASE_URL':'https://example.invalid'}):
            with self.assertRaises(w.Blocked):w.policy(self.state)

    def test_stale_billing_confirmation_blocks(self):
        s=w.readj(self.state/'settings.json'); s['billing_confirmation']['confirmed_at_unix']=0
        w.atomic(self.state/'settings.json',w.blob(s))
        self.assertEqual(self.runcli('run').returncode,2);self.assertEqual(self.calls(),[])

    def test_config_drift_rejected(self):
        (self.state/'codex-home/config.toml').write_text(w.CONFIG+'\n# altered\n')
        with self.assertRaises(w.Blocked):w.policy(self.state)

    def test_source_corruption_rejected(self):
        (self.state/'sources.json').write_text('{}')
        with self.assertRaises(w.Blocked):w.policy(self.state)

    def test_schema_drift_rejected(self):
        w.atomic(self.state/'output.schema.json',b'{}')
        with self.assertRaises(w.Blocked):w.policy(self.state)

    def test_empty_stream_rejected_even_with_zero_exit(self):
        self.mode('empty');self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.records()[0]['status'],'needs_attention')
        self.assertEqual(len(self.calls()),1)

    def test_matching_truncated_stream_rejected(self):
        self.mode('truncated');self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.records()[0]['status'],'needs_attention')

    def test_wrong_job_output_rejected(self):
        self.mode('wrong_id');self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.records()[0]['status'],'needs_attention')

    def test_nonzero_exit_preserved_not_retried(self):
        self.mode('failure');self.assertEqual(self.runcli('run').returncode,2)
        self.assertTrue((self.firstfolder()/'receipt.json').exists())
        self.assertEqual(self.runcli('run').returncode,2);self.assertEqual(len(self.calls()),1)

    def test_tampering_after_receipt_rejected(self):
        self.assertEqual(self.runcli('run').returncode,0)
        folder=self.state/'attempts'/self.records()[0]['attempt']
        (folder/'result.json').write_text('{}')
        with self.assertRaises(w.Blocked):w.validate_attempt(folder,'01-proof-audit')

    def test_duplicate_launch_is_rejected(self):
        self.mode('slow')
        p=subprocess.Popen(self.command('run'),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            self.waitfor(lambda:len(self.calls())==1)
            other=self.runcli('run');self.assertEqual(other.returncode,2)
            self.assertIn('lock',other.stderr)
            self.assertEqual(len(self.calls()),1)
            self.runcli('stop');p.wait(timeout=10)
        finally:
            if p.poll() is None:p.kill();p.wait()

    def test_supervisor_kill_completed_child_is_recovered_without_duplicate(self):
        self.mode('slow')
        p=subprocess.Popen(self.command('run'),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            self.waitfor(lambda:len(self.calls())==1)
            p.kill();p.wait(timeout=5)
            # Child still working holds inherited OS lock.
            self.assertEqual(self.runcli('run').returncode,2)
            self.waitfor(lambda:(self.firstfolder()/'receipt.json').exists())
            self.mode('ok')
            result=self.runcli('run');self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(self.calls().count('01-proof-audit'),1)
            self.assertEqual([j['status'] for j in self.records()],['saved_unreviewed']*3)
        finally:
            if p.poll() is None:p.kill();p.wait()

    def test_ambiguous_crash_never_silently_relaunches(self):
        c=w.db(self.state)
        try:w.setjob(c,'01-proof-audit','running','01-proof-audit-missing')
        finally:c.close()
        self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(self.records()[0]['status'],'needs_attention');self.assertEqual(self.calls(),[])

    def test_timeout_terminates_and_preserves_partial_attempt(self):
        self.mode('long');self.settings(max_job_seconds=1)
        self.assertEqual(self.runcli('run').returncode,2)
        r=w.readj(self.firstfolder()/'receipt.json')
        self.assertTrue(r['interrupted']);self.assertEqual(len(self.calls()),1)

    def test_stop_terminates_current_job_and_leaves_queue(self):
        self.mode('long')
        p=subprocess.Popen(self.command('run'),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            self.waitfor(lambda:len(self.calls())==1)
            self.assertEqual(self.runcli('stop').returncode,0)
            p.wait(timeout=10)
            self.assertTrue(w.readj(self.firstfolder()/'receipt.json')['interrupted'])
            self.assertEqual(len(self.calls()),1)
        finally:
            if p.poll() is None:p.kill();p.wait()

    def test_explicit_retry_preserves_failed_attempt(self):
        self.mode('failure');self.runcli('run');folder=self.firstfolder()
        self.mode('ok')
        self.assertEqual(self.runcli('retry','01-proof-audit','--previous-turn-ended').returncode,0)
        self.assertEqual(self.runcli('run').returncode,0)
        self.assertTrue((folder/'receipt.json').exists());self.assertEqual(len(self.calls()),4)

    def test_attempt_ceiling_stops_next_job(self):
        self.settings(max_total_attempts=1)
        self.assertEqual(self.runcli('run').returncode,2)
        self.assertEqual(len(self.calls()),1)
        self.assertEqual(self.records()[1]['status'],'queued')

    def test_status_and_preflight_do_not_launch_models(self):
        self.assertEqual(self.runcli('preflight').returncode,0)
        self.assertEqual(self.runcli('status').returncode,0);self.assertEqual(self.calls(),[])

    def test_missing_or_bad_usage_window_rejected(self):
        for val in (None,True,float('nan'),-1,100):
            r=self.limits();r['rateLimits']['primary']['usedPercent']=val
            with self.assertRaises(w.Blocked):w.validate_account(self.account(),r,80)

    def test_result_structure_is_not_theorem_validation(self):
        r={'job_id':'x','scope':w.SCOPE,'outcome':'review',
           'report_markdown':'A formally valid container can contain a mathematically wrong argument. '*3,
           'unresolved':[]}
        w.validate_result(r,'x') # Intentional: no claim of semantic proof certification.

    def test_state_cannot_live_inside_repository(self):
        with self.assertRaises(w.Blocked):w.init(self.repo/'private-state',self.repo,str(self.fake))


if __name__=='__main__':
    unittest.main(verbosity=2)
