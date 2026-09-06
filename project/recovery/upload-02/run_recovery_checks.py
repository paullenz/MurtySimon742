#!/usr/bin/env python3
"""Recovery checks, not solver replay or new mathematical certification.

Runs archived coverage/arithmetic function bodies unchanged, loading only the
pure graph functions from the encoder. PySAT is unavailable; CNF construction
is explicitly disabled, rather than emulated. Regenerates graph catalogues
with geng rebuilt from the received pinned source tarball.
"""
from __future__ import annotations
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
PAYLOAD = ROOT / 'payload'
CHECKS = ROOT / 'checks'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, data):
    (CHECKS / name).write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')

def no_build(*args, **kwargs):
    raise RuntimeError('CNF construction unavailable; this is a coverage-only check')

def coverage():
    core = PAYLOAD / 'delta14_k5_core_sat.py'
    audit = PAYLOAD / 'audit_delta14_ledgers.py'
    if sha(core) != '7fe0901d0a1c3b9b2e7587100b059bffad56a3896e9ecd6b11bcb709f39928f0':
        raise ValueError('encoder differs from the received pinned source')
    if sha(audit) != '0e268c7dd638e8dfaad106e64f5bb18afb8960075e9563d58fe5692f94a7bd80':
        raise ValueError('coverage auditor differs from the received pinned source')
    core_ast = ast.parse(core.read_text())
    selected = []
    for node in core_ast.body:
        if isinstance(node, ast.ImportFrom) and node.module == '__future__':
            selected.append(node)
        elif isinstance(node, ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('N_A','N_B') for t in node.targets):
            selected.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in ('decode_graph6','graph_data'):
            selected.append(node)
    scope = {'__name__':'archived_coverage_dependency_adapter', 'build':no_build}
    exec(compile(ast.Module(body=selected,type_ignores=[]), str(core), 'exec'),scope)
    tree = ast.parse(audit.read_text())
    tree.body = [node for node in tree.body
                 if not (isinstance(node,ast.ImportFrom) and node.module=='delta14_k5_core_sat')
                 and not isinstance(node,ast.If)]
    exec(compile(tree,str(audit),'exec'),scope)
    bands=[]
    old=os.getcwd()
    try:
        os.chdir(PAYLOAD)
        for k, ranges in ((5,range(12,18)),(6,range(3,13))):
            for r in ranges:
                bands.append(scope['audit_band'](k,r,False))
    finally:
        os.chdir(old)
    report={'status':'ALL-COVERAGE-AND-ARITHMETIC-CHECKS-PASSED','bands':bands,
            'execution':'Archived function bodies, pure-function AST loader; no PySAT import or CNF build',
            'source_sha256':{p.name:sha(p) for p in (core,audit)},
            'cnf_hashes_rebuilt':False,'sat_proof_replay':False,
            'mathematical_lemmas_independently_audited':False}
    write('coverage_arithmetic_fresh.json',report)
    print('Coverage:',len(bands),'bands,',sum(b['catalogue_records'] for b in bands),'records,',
          sum(b['arithmetic_rejections'] for b in bands),'arithmetic rejections,',
          sum(b['screening_sat_calls'] for b in bands),'screening calls',flush=True)

def catalogues():
    dest=ROOT/'regenerated_catalogues'
    dest.mkdir(exist_ok=True)
    rows=[]
    for k, ranges in ((5,range(12,18)),(6,range(3,13))):
        for r in ranges:
            name=f'delta14_k{k}_r{r}_all.g6'
            out=dest/name
            cmd=[str(ROOT/'bin/geng'),'-q',f'-D{9-k}','10',f'{r+3}:{r+3}',str(out)]
            result=subprocess.run(cmd,capture_output=True,text=True,timeout=60,check=True)
            expected=sha(PAYLOAD/'catalogues'/name)
            actual=sha(out)
            if actual!=expected:
                raise ValueError(f'geng bytes mismatch: {name}')
            rows.append({'k':k,'r':r,'path':name,'command':cmd,'expected_sha256':expected,
                         'actual_sha256':actual,'records':len(out.read_bytes().splitlines()),
                         'status':'BYTE-IDENTICAL'})
    write('catalogue_regeneration_fresh.json',{'status':'ALL-16-CATALOGUES-BYTE-IDENTICAL','rows':rows,
        'vendor_sha256':sha(PAYLOAD/'recovered/vendor/pynauty-2.8.8.1.tar.gz'),
        'independent_generation_algorithm':False,
        'note':'Fresh executable and run, same pinned nauty source, not independent generator verification.'})
    print('Fresh geng:',sum(r['records'] for r in rows),'records in',len(rows),'byte-identical catalogues',flush=True)

def manifest_links():
    def jsonl(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
    def key(x): return x['r'],x['core_index'],tuple(x['rho'])
    rows=[]
    for k in (5,6):
        certroot=PAYLOAD/f'certificates/delta14_k{k}_rup'
        manifest=jsonl(certroot/'manifest.jsonl')
        bykey={key(x):x for x in manifest}
        assert len(bykey)==len(manifest)
        expected={}
        for p in (PAYLOAD/'results').glob(f'delta14_k{k}_r*_full.jsonl'):
            for core in jsonl(p):
                assert core['status']=='ALL-FULL-UNSAT'
                for pattern in core['patterns']:
                    assert pattern['status']=='UNSAT-FULL'
                    ky=(core['r'],core['core_index'],tuple(pattern['rho']))
                    assert ky not in expected
                    expected[ky]=core['graph6']
        assert set(expected)==set(bykey)
        assert all(bykey[ky]['graph6']==g for ky,g in expected.items())
        historical=json.loads((PAYLOAD/f'results/delta14_k{k}_rup_replay.json').read_text())
        replay={key(x):x for x in historical['results']}
        assert len(replay)==len(historical['results'])==historical['records']==len(bykey)
        assert set(replay)==set(bykey)
        assert historical['status']=='ALL-RUP-VERIFIED'
        for ky,entry in bykey.items():
            assert replay[ky]['status']=='RUP-VERIFIED'
            assert replay[ky]['proof_sha256']==entry['proof_sha256']
            assert replay[ky]['formula_sha256']==entry['formula_sha256']
            assert entry.get('max_degree_f',4)==9-k
        rows.append({'k':k,'expected_full_patterns':len(expected),'proof_manifest_records':len(bykey),
            'historical_replay_records':len(replay),'all_identity_and_hash_links_match':True,
            'fresh_mathematical_proof_replays':0})
    write('full_stage_manifest_links.json',{'status':'MATCH','branches':rows,
       'note':'Fresh reconciliation of metadata and case coverage, not fresh proof-clause replay.'})
    print('Full-stage manifest links:',rows,flush=True)

if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Do not disable assertion checks with python -O')
    CHECKS.mkdir(exist_ok=True)
    coverage()
    catalogues()
    manifest_links()
