#!/usr/bin/env python3
"""N25 certificate mutations and declared-trust-boundary tests. No original edits."""
import argparse,copy,gzip,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def run(candidate,output):
    if output.exists():raise FileExistsError(output)
    output.mkdir(parents=True)
    audit=load_module('reaudit_terminal',Path(__file__).with_name('terminal_reaudit.py'))
    source=candidate/'d14_156/primary_ledger.jsonl.gz'
    data=json.loads((candidate/'d14_156/hall_certificates.json').read_text())
    certrow=copy.deepcopy(data['certificates'][0]);key=certrow['key'];R=certrow['columns']
    with gzip.open(source,'rt') as f:
        found=next(json.loads(line) for line in f if json.loads(line)['key']==key)
    col=next(copy.deepcopy(c) for c in found['witness']['survivors'] if c['columns']==R)
    ledger={'key':key,'kind':'survives','witness':{'survivors':[col]}}
    certificate={'checked':1,'eliminated':1,'surviving_columns':0,'surviving_outer_states':0,'certificates':[certrow],'survivors':[]}
    records=[]
    def test(name,mutator,old_expected,new_expected,optimized=False):
        a,b=copy.deepcopy(ledger),copy.deepcopy(certificate)
        mutator(a,b)
        folder=output/name;folder.mkdir();src=folder/'ledger.jsonl.gz';dst=folder/'certificate.json'
        src.write_bytes(gzip.compress((json.dumps(a,separators=(',',':'))+'\n').encode(),mtime=0))
        b['input_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
        if name=='wrong_input_hash':b['input_sha256']='0'*64
        dst.write_text(json.dumps(b,indent=2)+'\n')
        command=[sys.executable,'-I','-B']+(['-O'] if optimized else [])+[str(candidate/'check_column_certificates.py'),str(src),str(dst)]
        p=subprocess.run(command,text=True,capture_output=True)
        try:
            out=audit.verify(src,dst);new=True;new_detail=out
        except (ValueError,KeyError,IndexError,TypeError) as e:
            new=False;new_detail=str(e)
        old=p.returncode==0
        if (old,new)!=(old_expected,new_expected):
            raise RuntimeError({'name':name,'old':old,'new':new,'stderr':p.stderr,'new_detail':new_detail})
        records.append({'name':name,'original_exit_code':p.returncode,'original_accepts':old,'new_accepts':new,'new_detail':new_detail,'optimized_original':optimized,'original_stdout':p.stdout,'original_stderr':p.stderr,'ledger_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
    noop=lambda a,b:None
    test('valid_single_column',noop,True,True)
    test('missing_certificate',lambda a,b:b['certificates'].clear(),False,False)
    test('duplicate_certificate',lambda a,b:b['certificates'].append(copy.deepcopy(b['certificates'][0])),False,False)
    test('wrong_demand',lambda a,b:b['certificates'][0]['witness'].__setitem__('required',99),False,False)
    test('wrong_demand_optimized',lambda a,b:b['certificates'][0]['witness'].__setitem__('required',99),False,False,True)
    test('repeated_subset',lambda a,b:b['certificates'][0]['witness']['subset'].append(b['certificates'][0]['witness']['subset'][0]),False,False)
    test('out_of_range_subset',lambda a,b:b['certificates'][0]['witness'].__setitem__('subset',[10]),False,False)
    test('wrong_available_total',lambda a,b:b['certificates'][0]['witness'].__setitem__('available',99),False,False)
    test('wrong_input_hash',noop,False,False)
    def divert(a,b):
        b['survivors']=b['certificates'];b['certificates']=[];b['eliminated']=0;b['surviving_columns']=b['surviving_outer_states']=1
    test('explicit_unresolved_survivor',divert,True,False)
    def forge(a,b):
        d=json.loads(key)[2];demand=sum(max(0,x-y) for x,y in zip(d,R))
        a['witness']['survivors'][0]['caps']=[0]*14
        a['witness']['survivors'][0]['refined_caps']=[0]*14
        b['certificates'][0]['caps']=[0]*14
        b['certificates'][0]['witness']={'subset':list(range(10)),'required':demand,'by_source':[0]*14,'available':0}
    test('coupled_forged_caps',forge,True,False)
    def floatcap(a,b):
        a['witness']['survivors'][0]['refined_caps'][0]=float(a['witness']['survivors'][0]['refined_caps'][0])
        b['certificates'][0]['caps'][0]=float(b['certificates'][0]['caps'][0])
    test('floating_cap_token',floatcap,True,False)
    p=load_module('boundary_primary',candidate/'general_primary.py')
    q=load_module('boundary_secondary',candidate/'general_independent.py')
    p.A=q.A=15;p.B=q.B=9
    first=p.source_caps((0,)*15,(1,)*9);second=q.neighbours_bound((0,)*15,(1,)*9,None)
    audit.need(first==[14]*9 and second==[8]*9,'known helper boundary')
    p.matches=lambda labels,supplies:len(labels)<=len(supplies) and all(d<=c for d,c in zip(reversed(labels),supplies))
    audit.need(p.source_caps((0,)*15,(1,)*9)==second,'proposed helper guard')
    result={'status':'COMPLETED_WITH_DECLARED_TRUST_BOUNDARIES','tests':records,'known_helper':{'status':'REPRODUCED_OUTSIDE_PRODUCTION','primary':first,'secondary':second,'length_guard_agrees':True,'production':{'a9_b15':{'maximum_q':8,'suppliers':14},'a10_b14':{'maximum_q':9,'suppliers':13}}},'original_files_modified':False,'scope':'Standalone modular checker intentionally treats prior ledger caps as premises and can report remaining survivors. Both artificial altered inputs fail the frozen manifest; this is not a bypass of the full frozen replay.'}
    (output/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'tests':len(records),'ordinary_bad_cases_rejected':8,'boundary_cases':3,'valid_case':1},sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('candidate',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.candidate.resolve(),a.output.resolve())
