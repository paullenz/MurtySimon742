#!/usr/bin/env python3
"""Verify and materialize sealed research evidence; no ledger promotion.

All writes stay inside this package's durable/ directory. Network downloads and
Git publication are separate workflow steps. Missing files or hash differences
are blockers, never reasons to change frozen expectations.
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.util, json, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GENERAL = ROOT.parent
SOURCE_BLOBS = {
 'block_pressure/exploration/block_trial.py':'f8bda91d748a9eaab97e58898f0388b3aea6f5b5',
 'block_pressure/exploration/dual_explore.py':'e590a591d239c3771d6aafedb43371f353fa214f',
 'block_pressure/exploration/explore.py':'d867b23e57925e0f349c6e0198770baeed8424db',
 'block_pressure/exploration/multi_block.py':'a7bd9b21541133b1fbb1f2205a128f34f3df0f70',
 'block_pressure/exploration/weighted_trial.py':'d0341f8a978c40f421c515714a44dce5b1e818ae',
 'block_pressure/exploration/prior.py':'fa81fa4e9d4bdee6549c70752b835529fe68ea7c',
 'capped_spill/exploration/baseline.py':'9aab15ff0cd88d68fa60fef1fb37ad2dd99e714e',
 'capped_spill/exploration/explore.py':'5b0a4c094098243df6bdee2a98a018dcf1b9536c',
 'capped_spill/exploration/spill_math.py':'286d83c6454b05e947a19a709161c6f02c3c5395',
 'capped_spill/exploration/stages.py':'eacd735023e54d8d293e82c4ee3d33c6883523b6',
 'capped_spill/exploration/test_capped.py':'673e01d9ad96a1457fa74c7fc1072516e0f9d901',
 'capped_spill/exploration/test_synthetic.py':'ace671e7bd9e2d0a8e6abda81abb1145c8dfb76b',
 'block_pressure/exploration/block_trials.json':'8783cec55ebabd95422b1321fd89c6d814be6fc1',
 'block_pressure/exploration/dual_trials.json':'9befe3411b6de15263d25393daaf182267088541',
 'block_pressure/exploration/multiblock_trials.json':'e0057eab53606c876d8dc7b12ad83c79e4cb2e9e',
 'block_pressure/exploration/source_specific_trial.json':'93b2be8e502ee1c6bb555779b49a18467b79693b',
 'block_pressure/exploration/weighted_trials.json':'d83eb6230c84697d2383358ddada3e830a108f83',
}
ARTIFACT_FILES = {
 'BLOCK_ACTUAL.json':'64bab1d0302b0545f3fae030b5767eaa79a3e635de7d6c18a23abf58f7343180',
 'BLOCK_EXPECTED.json':'64bab1d0302b0545f3fae030b5767eaa79a3e635de7d6c18a23abf58f7343180',
 'CAPPED_ACTUAL.json':'1d744c2da2e3570c82960c7adf091b68eaeb610764b000d716212ef57999d4d1',
 'CAPPED_EXPECTED.json':'1d744c2da2e3570c82960c7adf091b68eaeb610764b000d716212ef57999d4d1',
 'GENERATOR_ACTUAL.json':'8ae1a96fa3f749fd57884430e0d0619abd79ee6f776e9b76e0ddd6c65f14622c',
 'QUEUE_AFTER.json':'f1e40669e9fb8ab0b7ff480bf431c8afd03301099ad368d1a76e2c4dfe724e7b',
 'QUEUE_BEFORE.json':'c342b8099600f44adbf3c92640ecf335d6e89f6890bd439a2e2c86fb7ef463ab',
 'SYNTHETIC_INTERVAL_PROFILES.tsv':'157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572',
 'scan_q_crossing_stats.cpp':'7b07649c355028818ba2153dedf461eb001b92541a5d994a83967cf366757906',
 'Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt':'6a2391d22d5a04734f340461545feecdcec78cf9d498af5091583bb2f3f20240',
 'LAYER_EXCEPTION_DIAGNOSTIC.tsv':'c4f859f97bed726f6e4799473906bd1673520aa2501d755fc5136a1c3cb46885',
}
HISTORICAL_HASHES = {
 'synthetic':'74ff677ed15b66eb57b8c20392de134bb8cb63307d37284115f45f2a967ee3bd',
 'capped':'a2335c1292fe69e659e100626a2c9d35fbda1f6cfae523d7934e4edd456e3cc6',
}
FULL_HASH = '7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e'


def sha(data): return hashlib.sha256(data).hexdigest()
def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def canonical(value): return json.dumps(value,sort_keys=True,separators=(',',':')).encode()

def check_sources():
 for name,expected in SOURCE_BLOBS.items():
  if blob((ROOT/name).read_bytes())!=expected: raise ValueError('Source transfer mismatch: '+name)


def historical(corpus,mode):
 # The two original numerical experiments are regenerated with identical integer
 # formulae and insertion order. Original scripts remain byte-for-byte intact.
 sys.path.insert(0,str(ROOT/'capped_spill/exploration'))
 import spill_math as m
 counts=Counter();survivors=[];new=[]
 for j,raw in enumerate(csv.DictReader(corpus.decode().splitlines(),delimiter='\t')):
  p={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()}
  q,rho,s=[p[k] for k in ('q','rho','s')]
  local=m.old.localized(s,q,rho,p['P']);caps,trace=m.spill(s,q,rho,local)
  E=p['Esel'];env=m.envelope(s,q,rho,p['b']-p['a']) if mode=='capped' else m.envelope(s,q,rho)
  oldscore=m.priced(q,rho,s,local)[0];midscore=m.priced(q,rho,s,caps)[0];score=m.priced(q,rho,s,caps,env)
  counts['profiles']+=1;counts['old_rejected']+=oldscore>0;counts['spill_rejected']+=midscore>0
  counts['new_rejected']+=score[0]>0;counts['unrejected']+=score[0]<=0;counts['cap_stricter']+=caps!=local
  counts['envelope_stricter']+=env<E*(E+max(s))
  if oldscore<=0 and score[0]>0:
   p.update(row=j,oldcap=local,newcap=caps,new_envelope=env,old_envelope=E*(E+max(s)),score=score,trace=trace);new.append(p)
  if score[0]<=0:survivors.append(dict(p,row=j,newcap=caps,new_envelope=env,score=score))
 out=json.dumps(dict(counts=dict(counts),newly_rejected=new,survivors=survivors),indent=2).encode()
 if sha(out)!=HISTORICAL_HASHES[mode]:raise ValueError('Historical replay mismatch: '+mode)
 return out


def main():
 if sys.flags.optimize:raise RuntimeError('Run without -O; assertions are verification checks')
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--inputs',type=Path,required=True);args=ap.parse_args()
 check_sources();payload={}
 for name,expected in ARTIFACT_FILES.items():
  found=list(args.inputs.rglob(name))
  if len(found)!=1:raise ValueError(f'Expected exactly one {name}: {found}')
  raw=found[0].read_bytes()
  if sha(raw)!=expected:raise ValueError('Artifact hash mismatch: '+name)
  payload['inputs/'+name]=raw
 for scope in ('BLOCK','CAPPED'):
  assert json.loads(payload['inputs/'+scope+'_ACTUAL.json'])==json.loads(payload['inputs/'+scope+'_EXPECTED.json'])
 snapshot=json.loads(payload['inputs/QUEUE_AFTER.json']);jobs=snapshot['runs']['34854911792']['jobs']
 assert len(jobs)==257 and len({x['id'] for x in jobs})==257
 assert {x['name'] for x in jobs}=={'plan',*(f'audit ({i})' for i in range(256))}
 corpus=payload['inputs/SYNTHETIC_INTERVAL_PROFILES.tsv']
 for mode in HISTORICAL_HASHES:payload['historical/'+mode+'_results.json']=historical(corpus,mode)
 package=GENERAL/'2026-09-14-conditioned-excess-v1'
 frozen=json.loads((package/'FROZEN_RESULT.json').read_text())
 assert frozen['full_output_canonical_sha256']==FULL_HASH
 with tempfile.TemporaryDirectory() as tmp:
  output=Path(tmp)/'full.json'
  with output.open('w') as handle:
   subprocess.run([sys.executable,str(package/'verify_conditioned_excess.py'),
    '--prior',str(GENERAL/'2026-09-14-capped-spill-v1/verify_capped_spill.py'),
    '--block',str(GENERAL/'2026-09-14-block-pressure-v1/verify_block_pressure.py'),
    '--remainder',str(GENERAL/'2026-09-14-block-pressure-v1/REMAINDER_12.json')],stdout=handle,check=True)
  raw=output.read_bytes();actual=json.loads(raw)
  if sha(canonical(actual))!=FULL_HASH:raise ValueError('Complete conditioned replay differs from frozen hash')
  payload['CONDITIONED_EXCESS_FULL.json']=raw
 original=json.loads((GENERAL/'2026-09-14-block-pressure-v1/REMAINDER_12.json').read_text())
 kept=set(actual['replay']['not_excluded'])
 payload['REMAINDER_9.json']=json.dumps(dict(source_corpus_sha256=original['source_sha256'],
  scope='Nine not-excluded sampled relaxations; not realized graphs or canonical whole states',
  rows=[p for p in original['rows'] if p['row'] in kept]),indent=2,sort_keys=True).encode()+b'\n'
 record=dict(schema='research-evidence-materialization-v1',result='PASS',external_review='OPEN',promotion='NONE',
  checked_source_files=len(SOURCE_BLOBS),combined_ci_run=34887492789,combined_artifact=10364839603,
  combined_archive_sha256='08b3df5892c99c5fb8acc728052e1355ffe51a3af2d6d965c248d2003fe0e5a1',
  conditioned_full_canonical_sha256=FULL_HASH,original_713_corpus_sha256=sha(corpus),
  historical_output_sha256=HISTORICAL_HASHES,audit_snapshot_observed=snapshot['observed_utc'],
  audit_snapshot_counts=snapshot['runs']['34854911792']['counts'],
  audit_snapshot_warning='Historical full-page snapshot, NOT a current aggregate or promotion',
  files={n:dict(bytes=len(data),sha256=sha(data)) for n,data in sorted(payload.items())})
 payload['MATERIALIZATION_STATUS.json']=json.dumps(record,indent=2,sort_keys=True).encode()+b'\n'
 # Nothing is published until every check above passed. Refuse different existing
 # bytes rather than silently replacing a previously frozen artifact.
 out=ROOT/'durable'
 for name,raw in payload.items():
  dest=out/name
  if dest.exists() and dest.read_bytes()!=raw:raise ValueError('Different existing durable file: '+name)
 for name,raw in payload.items():
  dest=out/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 print(json.dumps(record,indent=2,sort_keys=True))
if __name__=='__main__':main()
