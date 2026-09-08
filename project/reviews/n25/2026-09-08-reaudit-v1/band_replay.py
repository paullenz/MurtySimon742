#!/usr/bin/env python3
"""Memory-bounded execution of the frozen n25 classifiers and both generators.
The original classification/matching/domain functions are imported unchanged.
No full-scope pretty JSON is retained; each produced state is checked immediately.
"""
import argparse,hashlib,importlib.util,json,stat,time,zipfile
from collections import Counter
from pathlib import Path
import gzip

BASELINE='af5a05689bee9bdbc50ee5a54974fe5c2a853f8f'
ZIP_SHA='ff5a88f4202fb1e201f52e7e6ec0b50f88248cd43493eee78f120a3c1de15c3d'
GROUPS=['control','equality_k2to5','k1_early','k1_late']+[f'k1_r{r}_s{s}' for r in range(26,30) for s in range(3)]
CONFIGS={'d14_157':(10,157,[5,4,3,2]),'d15_157':(9,157,[3,2]),'d15_156':(9,156,[3,2]),'d14_156':(10,156,[5,4,3,2]),'d14_156_k1':(10,156,[1])}


def need(ok,message):
    if not ok:raise ValueError(message)


def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()


def unpack(p,target):
    with zipfile.ZipFile(p) as z:
        for i in z.infolist():
            q=Path(i.filename)
            need(not q.is_absolute() and '..' not in q.parts and '\\' not in i.filename and not stat.S_ISLNK(i.external_attr>>16),'unsafe ZIP path')
        need(z.testzip() is None,'ZIP CRC');z.extractall(target)


def prepare(repo,work):
    need(not work.exists(),'workspace must be new');work.mkdir(parents=True)
    rel=repo/'releases/n25-reviewer-v1'; receipt=json.loads((rel/'ARCHIVE_RECEIPT.json').read_text())
    archive=work/'original-reviewer.zip'
    with archive.open('xb') as out:
        for part in receipt['parts']:
            p=rel/part['path'];need(p.stat().st_size==part['bytes'] and digest(p)==part['sha256'],'part hash');out.write(p.read_bytes())
    need(archive.stat().st_size==13002402 and digest(archive)==ZIP_SHA,'pinned original ZIP')
    unpack(archive,work)
    reviewer=work/'N25_Reviewer_Package_v1'
    candidatezip=reviewer/'N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip'
    need(digest(candidatezip)=='0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95','candidate ZIP')
    unpack(candidatezip,work)
    candidate=work/'N25_Full_Chain_Candidate_2026-09-06_v1'
    unpack(candidate/'historical/N25_Delta14_Document_Review_Evidence_2026-09-06.zip',work)
    checks=[]
    for root,name in [(reviewer,'MANIFEST.json'),(candidate,'MANIFEST.json'),(work/'N25_Delta14_Document_Review','REVIEW_MANIFEST.json')]:
        m=json.loads((root/name).read_text())
        for item in m['files']:
            q=Path(item['path']);need(not q.is_absolute() and '..' not in q.parts,'manifest path')
            p=root/q;need(p.is_file() and p.stat().st_size==item['bytes'] and digest(p)==item['sha256'],'manifest mismatch '+str(q))
        checks.append({'root':root.name,'files':len(m['files']),'sha256':digest(root/name)})
    (work/'INPUT_INTEGRITY.json').write_text(json.dumps(checks,indent=2)+'\n')
    print('PREPARED',len(checks),'manifests')


def included(group,scope,r,key):
    if group=='control':return scope in ['d14_157','d15_157','d15_156']
    if group=='equality_k2to5':return scope=='d14_156'
    if scope!='d14_156_k1':return False
    if group=='k1_early':return r<=25
    if group=='k1_late':return r>=30
    rr,ss=group.split('_')[1:]
    return r==int(rr[1:]) and int(hashlib.sha256(key.encode()).hexdigest()[:8],16)%3==int(ss[1:])


def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def fingerprint(columns):
    return hashlib.sha256(('\n'.join(sorted(json.dumps(c,separators=(',',':')) for c in columns))+'\n').encode()).hexdigest()


def run(work,group,out):
    need(not out.exists(),'output exists');start=time.monotonic();scopes=[]
    for scope,(a,edges,ks) in CONFIGS.items():
        if group=='control' and scope not in ['d14_157','d15_157','d15_156']:continue
        if group=='equality_k2to5' and scope!='d14_156':continue
        if group.startswith('k1_') and scope!='d14_156_k1':continue
        root=work/('N25_Delta14_Document_Review' if scope=='d14_157' else 'N25_Full_Chain_Candidate_2026-09-06_v1')
        folder=root/('results' if scope=='d14_157' else scope)
        primary_path=root/('verify_primary.py' if scope=='d14_157' else 'general_primary.py')
        second_path=root/('verify_independent.py' if scope=='d14_157' else 'general_independent.py')
        p=load('frozen_primary_'+scope,primary_path);s=load('frozen_secondary_'+scope,second_path)
        b=24-a;L=300-edges-a-b*(b-1)//2;t=a*(a-1)//2-L
        for m in [p,s]:m.A=a;m.B=b;m.LEDGER=L;m.GAP=t
        expected={};expected_columns=0
        with gzip.open(folder/'primary_ledger.jsonl.gz','rt') as f:
            for line in f:
                row=json.loads(line);key=row['key'];r=json.loads(key)[1]
                if not included(group,scope,r,key):continue
                need(key not in expected,'duplicate archived state')
                cols=[[c['columns'],c['required'],c['caps'],c['refined_caps']] for c in row['witness'].get('columns',[])]
                expected[key]=(row['kind'],hashlib.sha256(p.stable_bytes(row)).hexdigest(),fingerprint(cols),len(cols));expected_columns+=len(cols)
        observed=set();counts=Counter();pc=0
        for k in ks:
            D=a-1-k
            for r in range(b,L-(a*k+1)//2+1):
                for ds in p.multisets(a,2*(r+t),0,D):
                    if ds[-1]!=D:continue
                    for rs in p.multisets(b,r,1,a):
                        key=p.state_key(k,r,ds,rs)
                        if not included(group,scope,r,key):continue
                        need(key not in observed and key in expected,'primary domain');observed.add(key)
                        kind,w=p.classify(ds,rs,r)
                        need(hashlib.sha256(p.stable_bytes({'key':key,'kind':kind,'witness':w})).hexdigest()==expected[key][1],'primary full-state mismatch')
                        counts[kind]+=1;pc+=len(w.get('columns',[]))
        need(observed==set(expected) and pc==expected_columns,'primary exact coverage')
        second_seen=set();sc=0;second_counts=Counter()
        for k in ks:
            D=a-1-k
            for r in range(b,L-(a*k+1)//2+1):
                for hd in s.histograms(D,a,2*r+2*t):
                    if hd[-1]==0:continue
                    ds=s.expand(hd)
                    for hr in s.histograms(a-1,b,r-b):
                        rs=s.expand(hr,1);key=json.dumps([k,r,ds,rs],separators=(',',':'))
                        if not included(group,scope,r,key):continue
                        need(key not in second_seen and key in expected,'secondary domain');second_seen.add(key)
                        kind,cols=s.analyse(ds,rs,r)
                        need(kind==expected[key][0] and fingerprint(cols)==expected[key][2] and len(cols)==expected[key][3],'secondary classification/columns mismatch')
                        sc+=len(cols);second_counts[kind]+=1
        need(second_seen==observed and sc==pc and second_counts==counts,'secondary complete coverage')
        record={'scope':scope,'states':len(observed),'columns':pc,'dispositions':dict(sorted(counts.items())),'state_key_sha256':hashlib.sha256(('\n'.join(sorted(observed))+'\n').encode()).hexdigest(),'primary_source_sha256':digest(primary_path),'secondary_source_sha256':digest(second_path),'all_full_primary_rows_equal':True,'all_secondary_columns_equal':True}
        scopes.append(record);print(json.dumps(record),flush=True)
    result={'status':'PASS','group':group,'archive_sha256':ZIP_SHA,'scopes':scopes,'elapsed_seconds':time.monotonic()-start,'classifiers_and_generators_unchanged':True,'driver':'per-band immediate comparison; avoids whole-scope pretty JSON','unpartitioned_original_wrapper_completed':False,'external_review':False}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')


def aggregate(directory,output):
    need(not output.exists(),'output exists');records={}
    for p in directory.rglob('band-*.json'):
        r=json.loads(p.read_text());need(r['status']=='PASS' and r['group'] not in records and r['group'] in GROUPS,'invalid/duplicate shard');records[r['group']]=r
    need(set(records)==set(GROUPS),'missing shards')
    totals={k:Counter() for k in CONFIGS}
    for record in records.values():
        for r in record['scopes']:
            totals[r['scope']]['states']+=r['states'];totals[r['scope']]['columns']+=r['columns']
    expected={'d14_157':(59264,1480),'d15_157':(108,0),'d15_156':(211,0),'d14_156':(82452,188520),'d14_156_k1':(401543,3252212)}
    need(all((v['states'],v['columns'])==expected[k] for k,v in totals.items()),'aggregate coverage totals')
    result={'status':'PASS','groups':GROUPS,'scopes':totals,'outer_states':sum(x['states'] for x in totals.values()),'labelled_columns':sum(x['columns'] for x in totals.values()),'every_shard_matched_both_generators_and_classifiers':True,'partition':'disjoint scope/r bands, or exhaustive SHA256(key) modulo 3','unpartitioned_original_wrapper_completed':False,'external_review':False}
    output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);sp=p.add_subparsers(dest='mode',required=True)
    q=sp.add_parser('prepare');q.add_argument('repo',type=Path);q.add_argument('work',type=Path)
    q=sp.add_parser('run');q.add_argument('work',type=Path);q.add_argument('group',choices=GROUPS);q.add_argument('--output',type=Path,required=True)
    q=sp.add_parser('aggregate');q.add_argument('directory',type=Path);q.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.mode=='prepare':prepare(a.repo,a.work)
    elif a.mode=='run':run(a.work,a.group,a.output)
    else:aggregate(a.directory,a.output)
