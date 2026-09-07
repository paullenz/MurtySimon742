#!/usr/bin/env python3
"""Verify the frozen archive or reproduce its complete n=27 arithmetic in a new directory."""
import argparse,hashlib,importlib.util,json,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def verify():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for item in manifest['files']:
        path=ROOT/item['path'];assert path.is_file() and path.stat().st_size==item['bytes'] and digest(path)==item['sha256'],item['path']
    for name in ('preflight','check_final'):
        spec=importlib.util.spec_from_file_location(name,ROOT/(name+'.py'));module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if name=='preflight':assert module.main()['status']=='PASS'
        else:
            for e in (183,182):assert module.run(e)['unresolved']==0
    print(json.dumps({'status':'FROZEN_FILES_AND_FINAL_CERTIFICATES_VERIFIED','files':len(manifest['files']),
                      'full_arithmetic_replayed_in_this_call':False,'external_review':False}),flush=True)

def replay(out,prepare_only=False):
    if out.exists():raise ValueError('Output must be a new directory.')
    out.mkdir(parents=True)
    for p in ROOT.iterdir():
        if p.suffix in ('.py','.cpp') or p.name=='validation_frontier.jsonl.gz':shutil.copyfile(p,out/p.name)
    if prepare_only:
        print(json.dumps({'status':'REPLAY_DIRECTORY_PREPARED_ONLY','output':str(out),'arithmetic_run':False}));return
    def command(args,log):
        print(json.dumps({'running':args,'log':log}),flush=True)
        with (out/log).open('w') as stream:subprocess.run(args,cwd=out,stdout=stream,stderr=subprocess.STDOUT,check=True)
    py=[sys.executable,'-I','-B']
    for program,libs in [('survey',['-lz']),('check_survey',['-lz']),('columns',['-lz','-lcrypto'])]:
        command(['g++','-O3','-std=c++17',program+'.cpp',*libs,'-o',program],program+'_build.log')
    for e in (183,182):
        small=f'd16_{e}';prefix=f'd15_{e}'
        command(py+['general_primary.py','--n','27','--a','10','--edges',str(e),'--ks','2','3','4','--output',small],small+'_primary.log')
        command(py+['general_independent.py','--n','27','--a','10','--edges',str(e),'--ks','2','3','4','--reference',small,'--output',small],small+'_independent.log')
        command(['./survey','27','15',str(e),prefix],prefix+'_survey.log')
        command(['./check_survey','27','15',str(e),prefix],prefix+'_outer_check.log')
        command(['./columns','scan','27','15',str(e),prefix+'_frontier.jsonl.gz',prefix,prefix],prefix+'_columns.log')
        command(['./columns','check','27','15',str(e),prefix+'_frontier.jsonl.gz',prefix,prefix+'_check'],prefix+'_check.log')
        command(py+['pair_column.py',prefix+'_survivors.jsonl.gz',prefix],prefix+'_pair.log')
    command(py+['supplement_pair.py','d15_182_pair_survivors.jsonl.gz','d15_182'],'d15_182_supplement.log')
    command(py+['check_final.py'],'final_check.log');command(py+['preflight.py'],'preflight.log')
    command(['./columns','scan','27','15','0','validation_frontier.jsonl.gz','validation','validation'],'validation_scan.log')
    command(['./columns','check','27','15','0','validation_frontier.jsonl.gz','validation','validation_check'],'validation_check.log')
    command(py+['check_column_sample.py'],'column_sample_check.log')
    command(py+['structural_validation.py'],'structural_validation.log')
    for name in ('FINAL_CHECK.json','COLUMN_SAMPLE_CHECK.json','structural_results.json'):
        assert json.loads((out/name).read_text())['status']=='PASS',name
    print(json.dumps({'status':'COMPLETE_INTERNAL_REPLAY_PASS','output':str(out),'external_review':False}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--verify-only',action='store_true');p.add_argument('--replay',action='store_true');p.add_argument('--prepare-only',action='store_true');p.add_argument('--output',type=Path)
    a=p.parse_args()
    if not a.replay and not a.prepare_only:verify()
    else:
        if a.output is None:p.error('--output is required')
        verify();replay(a.output.resolve(),a.prepare_only)
