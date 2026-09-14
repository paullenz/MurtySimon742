#!/usr/bin/env python3
"""Replay parent proof, shared slack, new seed and failed multiblock experiment.

Run from any working directory in a checkout of paullenz/MurtySimon742. Outputs
are written only to the explicitly supplied directory. Nothing is promoted.
"""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
EXPECTED={
 'SHARED_SLACK_FULL.json':'35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6',
 'FRESH_RECHECK_FULL.json':'754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9',
 'MULTIBLOCK_FULL.json':'d979d53bad1239b65442265b477594cffa05ec67750d8be6b3123add2b2b5127'}
def canonical_hash(path):
 return hashlib.sha256(json.dumps(json.loads(path.read_text()),sort_keys=True,separators=(',',':')).encode()).hexdigest()
def blob(path):
 data=path.read_bytes();return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def main():
 if not __debug__:raise SystemExit('Assertions disabled: do not run with -O')
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4]);ap.add_argument('--outdir',required=True,type=Path);args=ap.parse_args()
 repo=args.repo.resolve();out=args.outdir.resolve();out.mkdir(parents=True,exist_ok=True)
 base=repo/'project/research/general_n';pkg=base/'2026-09-14-joint-blocks-v1';durable=base/'2026-09-14-evidence-preservation-v1/durable'
 prior=base/'2026-09-14-capped-spill-v1/verify_capped_spill.py';block=base/'2026-09-14-block-pressure-v1/verify_block_pressure.py'
 remainder=base/'2026-09-14-block-pressure-v1/REMAINDER_12.json';parent=base/'2026-09-14-conditioned-excess-v1/verify_conditioned_excess.py'
 for path,sha in [(prior,'fa81fa4e9d4bdee6549c70752b835529fe68ea7c'),(block,'31973251dd7e3250f3ded9a3e3af903a35824020'),(parent,'412356d3585e2fda845434868e52653a58852aee'),(pkg/'verify_shared_slack.py','63aacca1d12043db700a9edd5c15667cbd582663'),(pkg/'recheck_fresh.py','6e57b436684957a9f493e3340e82e4d02470b3af'),(pkg/'explore_multiblock.py','11c76894b2f163e12cdb08bd221d3555410561c0'),(pkg/'regenerate_fresh.py','d060de15e38350ffb94320eae55e95824b6f4f61')]:
  if blob(path)!=sha:raise RuntimeError(f'Source changed: {path}; review rather than weakening the hash')
 env=dict(os.environ,PYTHONOPTIMIZE='0',PYTHONHASHSEED='0')
 def run(source,arguments,filename):
  with (out/filename).open('w') as h:subprocess.run([sys.executable,str(source),*map(str,arguments)],stdout=h,env=env,check=True)
 common=['--prior',prior,'--block',block,'--remainder',remainder]
 run(parent,common,'PARENT_REPLAY.json')
 parent_hash='7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e'
 assert canonical_hash(out/'PARENT_REPLAY.json')==parent_hash==canonical_hash(durable/'CONDITIONED_EXCESS_FULL.json')
 run(pkg/'verify_shared_slack.py',common+['--parent-output',out/'PARENT_REPLAY.json'],'SHARED_SLACK_FULL.json')
 assert canonical_hash(out/'SHARED_SLACK_FULL.json')==EXPECTED['SHARED_SLACK_FULL.json']==canonical_hash(pkg/'SHARED_SLACK_FULL.json')
 run(pkg/'regenerate_fresh.py',['--generator',base/'2026-09-14-q-tail-interval-budget-v1/search_synthetic_interval.cpp','--scanner',durable/'inputs/scan_q_crossing_stats.cpp','--outdir',out/'fresh'],'FRESH_GENERATOR_REPLAY.json')
 run(pkg/'recheck_fresh.py',['--prior',prior,'--block',block,'--synthetic',out/'fresh/SYNTHETIC_INTERVAL_PROFILES.tsv'],'FRESH_RECHECK_FULL.json')
 assert canonical_hash(out/'FRESH_RECHECK_FULL.json')==EXPECTED['FRESH_RECHECK_FULL.json']==canonical_hash(pkg/'FRESH_RECHECK_FULL.json')
 run(pkg/'explore_multiblock.py',common+['--shared-result',out/'SHARED_SLACK_FULL.json'],'MULTIBLOCK_FULL.json')
 assert canonical_hash(out/'MULTIBLOCK_FULL.json')==EXPECTED['MULTIBLOCK_FULL.json']
 result=dict(result='PASS',scope='parent/shared-slack/fresh-seed/multiblock internal replay',hashes=EXPECTED,external_review='OPEN',frontier_promoted=False)
 (out/'REPLAY_STATUS.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
