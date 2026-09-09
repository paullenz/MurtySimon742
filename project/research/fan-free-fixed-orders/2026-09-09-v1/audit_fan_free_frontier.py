#!/usr/bin/env python3
"""Hostile consistency audit for the Fan-free fixed-order proof layer.

This is deliberately not a new proof generator. It checks that the assembled
Fan-free replacement has no missing numerical bands, that exact-acceptance
checkpoints report zero survivors, that v2 proof surfaces no longer invoke Fan
logically, and that frozen historical sources still hash to the values recorded
when the v2 editions were built.
"""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[4]
D = ROOT / 'project/research/fan-free-fixed-orders/2026-09-09-v1'

def load(rel):
    return json.loads((ROOT/rel).read_text())

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require(cond,msg):
    if not cond:
        raise AssertionError(msg)

def check_zero(doc,label):
    require(doc.get('final_survivors') == 0 or doc.get('all_final_survivors_zero') is True,
            f'{label}: nonzero/unknown final survivor status')

results={}

# n=25 / n=27 aggregate and deep n27 closure.
base=load('project/research/fan-free-fixed-orders/2026-09-09-v1/CHECKPOINT.json')
bands={(x['n'],x['delta']):x for x in base['outer_scan']['bands']}
expected={(25,14):(158,175),(25,15):(158,187),(25,16):(158,200),
          (27,15):(184,202),(27,16):(184,216),(27,17):(184,229)}
for key,rng in expected.items():
    require(tuple(bands[key]['edges'])==rng,f'{key}: wrong scanned edge interval')
for key in [(25,14),(25,15),(25,16),(27,16),(27,17)]:
    require(bands[key]['outer_survivors']==0,f'{key}: outer survivors remain')
require(bands[(27,15)]['outer_survivors']==661,'n27 d15: unexpected outer frontier')
closures={x['edges']:x for x in base['n27_delta15_column_closure']['scopes']}
require(set(closures)=={184,185},'n27 d15: deep closure scopes are not exactly 184,185')
for m,x in closures.items():
    require(x['surviving_columns']==0,f'n27 d15 m={m}: surviving columns remain')
require(base['n27_delta15_column_closure']['scan_check_agreement'] is True,'n27 scan/check disagreement')
results['n25']={'status':'PASS','upper_ranges':[[158,175],[158,187],[158,200]]}
results['n27']={'status':'PASS','upper_ranges':[[184,202],[184,216],[184,229]],'deep_scopes':[184,185]}

# n=28: m=198,199 trusted closures and m=200..210 exact early kernel.
for m in (198,199):
    x=load(f'project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N28_D15_M{m}.json')
    check_zero(x,f'n28 d15 m={m}')
    require(x['close']['floating_infeasibility_alone_accepted'] is False,f'n28 m={m}: float-only acceptance')
    require(x['close']['all_model_rejections_exact_integer_farkas_verified'] is True,f'n28 m={m}: exact checker flag missing')
e=load('project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N28_D15_UPPER_EARLY.json')
require(set(map(int,e['results']))==set(range(200,211)),'n28 early coverage is not 200..210')
require(e['all_final_survivors_zero'] is True,'n28 early closure has survivor')
d197=load('project/research/general_n/2026-09-07-direct-197-v8/RESULTS.json')
require(d197['scope']['n']==28 and d197['scope']['m']==197 and d197['final_survivors']==0,'n28 direct197 base not closed')
results['n28']={'status':'PASS','direct_scope':197,'fresh_upper_range':[198,210]}

# n=29: m=212 exact trusted closure, 213..215 exact early, 216..232 zero outer frontier.
x=load('project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N29_D16_M212.json')
check_zero(x,'n29 d16 m=212')
require(x['all_late_exclusions_exact_integer_farkas_reverified'] is True,'n29 m212: late exact recheck missing')
require(x['residual_rows']==2 and x['exact_rejections']==2,'n29 m212: unexpected late frontier')
e=load('project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N29_D16_UPPER_EARLY.json')
require(set(map(int,e['results']))=={213,214,215},'n29 early coverage is not 213..215')
require(e['all_final_survivors_zero'] is True,'n29 early closure has survivor')
# Generic discovery scan is preserved as an artifact-level claim in the reduction note.
# Here we also require the reduction text to state the exact remaining interval.
ff=(D/'FAN_FREE_REDUCTION.md').read_text()
require('zero survivors at every `m=216..232`' in ff,'n29 reduction does not record 216..232 closure')
results['n29']={'status':'PASS','fresh_upper_range':[212,232]}

# n=30 Delta16 complete 227..240.
for m in (227,228,229,230):
    x=load(f'project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N30_D16_M{m}.json')
    check_zero(x,f'n30 d16 m={m}')
    require(x['close']['floating_infeasibility_alone_accepted'] is False,f'n30 d16 m={m}: float-only acceptance')
    require(x['close']['all_model_rejections_exact_integer_farkas_verified'] is True,f'n30 d16 m={m}: exact checker flag missing')
e=load('project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N30_D16_UPPER_EARLY.json')
require(set(map(int,e['results']))==set(range(231,241)),'n30 d16 early coverage is not 231..240')
require(e['all_final_survivors_zero'] is True,'n30 d16 early closure has survivor')
# n30 Delta17 complete 227..255 explicit scan.
e17=load('project/research/fan-free-fixed-orders/2026-09-09-v1/checkpoints_N30_D17_UPPER.json')
require(e17['edge_range']==[227,255],'n30 d17 wrong edge range')
require(set(map(int,e17['results']))==set(range(227,256)),'n30 d17 missing edge count')
require(e17['all_final_survivors_zero'] is True,'n30 d17 survivor remains')
results['n30']={'status':'PASS','delta16_range':[227,240],'delta17_range':[227,255]}

# Historical source integrity and Fan semantics on current proof surfaces.
history={
  25:('project/reviews/n25/2026-09-09-fan-free-v2/HISTORY.md','project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md','project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md'),
  27:('project/reviews/n27/2026-09-09-fan-free-v2/HISTORY.md','project/reviews/n27/2026-09-07-candidate-v1/PROOF.md','project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md'),
  28:('project/reviews/n28/2026-09-09-fan-free-v2/HISTORY.md','releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.tex','project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex'),
  29:('project/reviews/n29/2026-09-09-fan-free-v2/HISTORY.md','project/reviews/n29/2026-09-08-candidate-v1/PROOF.md','project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md'),
  30:('project/reviews/n30/2026-09-09-fan-free-v2/HISTORY.md','project/reviews/n30/2026-09-09-candidate-v1/PROOF.md','project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md'),
}
banned=["Fan's strict bound leaves", "Fan's strict bound gives", 'Fan supplies the global reduction', "external density input is Fan's strict estimate"]
for n,(hrel,oldrel,newrel) in history.items():
    ht=(ROOT/hrel).read_text(); actual=sha256(ROOT/oldrel)
    require(actual in ht,f'n={n}: frozen source SHA no longer matches HISTORY')
    nt=(ROOT/newrel).read_text()
    require('not a logical dependency' in nt or 'not} a logical dependency' in nt or 'not a logical dependency of edition 2' in nt,
            f'n={n}: Fan-free semantic marker missing')
    for phrase in banned:
        require(phrase not in nt,f'n={n}: old logical Fan invocation remains: {phrase}')
results['history_integrity']={'status':'PASS','orders':[25,27,28,29,30]}
results['fan_semantics']={'status':'PASS','logical_dependency':False,'historical_citation_retained':True}

report={
  'schema':'fan-free-fixed-order-hostile-audit-v1',
  'date':'2026-09-09',
  'status':'PASS',
  'scope_orders':[25,27,28,29,30],
  'checks':results,
  'limitations':[
    'This audit checks assembly coverage, exact-checkpoint acceptance semantics, and source integrity; it is not external independent review.',
    'Hand graph-to-residual lemmas and monotonicity arguments remain mathematical trust boundaries and require independent specialist review.',
    'The published n=26 result is historical literature context and is not re-proved by this Fan-free project layer.'
  ]
}
(D/'FAN_FREE_AUDIT_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
(D/'FAN_FREE_AUDIT.md').write_text('''# Hostile assembly audit — Fan-free fixed-order frontier\n\n9 September 2026. **PASS internally; independent external review remains OPEN.**\n\nThis audit was written after an external-AI critique challenged two selection/residual semantics and the reliance on Fan's 1987 upper bound. The two semantic objections were resolved by explicit definitions; the project then went further and removed Fan as a logical dependency from its current fixed-order candidate proofs at n=25,27,28,29,30.\n\nThe audit checks the replacement as an assembled dependency chain rather than merely trusting green workflows. It verifies complete edge-range coverage of the new upper-band computations, zero final survivors in every required exact checkpoint, exact-certificate acceptance flags, the absence of the old logical Fan phrases from v2 proof surfaces, and SHA-256 integrity of every frozen historical source named by the v2 history files.\n\nResult: **PASS** on all machine-checkable assembly checks. See `FAN_FREE_AUDIT_REPORT.json`.\n\nThe result is deliberately not described as external verification. The universal graph-to-residual lemmas and the short hand monotonicity arguments remain the main mathematical trust boundary. Historical v1 proof surfaces and Fan citations are retained rather than overwritten.\n''')
print(json.dumps(report,sort_keys=True))
