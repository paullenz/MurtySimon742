#!/usr/bin/env python3
"""Reproduce the direct order-28 candidate using a mandatory hardened v8 helper.

Default: complete checking, not integrity only. Six original archives are
required (see ARCHIVES.json). --verify-only explicitly skips arithmetic.
Never changes an original archive, original extracted source or old report.
No optimisation solver or network is used. Python 3.10+, g++/C++17, Boost.
"""
from __future__ import annotations
import argparse, concurrent.futures, gzip, hashlib, json, os, shutil
import stat, subprocess, sys, time, zipfile
from pathlib import Path, PurePosixPath
ROOT=Path(__file__).resolve().parent

def need(ok:bool,msg:str)->None:
    if not ok: raise ValueError(msg)
def sha(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def stable(x):
    if isinstance(x,dict):return {k:stable(v) for k,v in x.items() if k not in ('seconds','stage_seconds')}
    if isinstance(x,list):return [stable(v) for v in x]
    return x

def verify_directory(root:Path)->dict:
    raw=json.loads((root/'MANIFEST.json').read_text())['files']
    entries=raw if isinstance(raw,dict) else {x['path']:x for x in raw}
    need(len(entries)==len(raw),'Duplicate manifest paths')
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    need(actual==set(entries)|{'MANIFEST.json'},'Unexpected or missing payload')
    for name,item in entries.items():
        rel=PurePosixPath(name);p=root/name
        need(not rel.is_absolute() and '..' not in rel.parts and not p.is_symlink(),'Unsafe manifest path')
        need(p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],'Payload mismatch: '+name)
    return {'files':len(entries),'manifest_sha256':sha(root/'MANIFEST.json'),'all_pass':True}

def extract(a:Path,entry:dict,dest:Path)->Path:
    need(a.stat().st_size==entry['bytes'] and sha(a)==entry['sha256'],'Wrong original archive: '+a.name)
    with zipfile.ZipFile(a) as z:
        names=z.namelist();need(len(names)==len(set(names)),'Duplicate ZIP paths')
        need(z.testzip() is None,'ZIP CRC failure')
        for item in z.infolist():
            r=PurePosixPath(item.filename)
            need(not r.is_absolute() and '..' not in r.parts and r.parts[0]==entry['root'],'Unsafe ZIP path')
            need(not stat.S_ISLNK(item.external_attr>>16),'ZIP symlink prohibited')
        z.extractall(dest)
    root=dest/entry['root'];need(sha(root/'MANIFEST.json')==entry['manifest_sha256'],'Wrong manifest')
    verify_directory(root);return root

def decoded(p:Path)->bytes:
    raw=p.read_bytes();return gzip.decompress(raw) if p.suffix=='.gz' else raw

def run(name:str,command:list[str],cwd:Path,logs:Path)->dict:
    t=time.monotonic(); log=logs/(name+'.log')
    env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONHASHSEED='0')
    with log.open('wb') as f:
        q=subprocess.run(command,cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT)
    result={'name':name,'command':command,'exit_code':q.returncode,'seconds':time.monotonic()-t,'log':str(log)}
    (logs/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    need(q.returncode==0,'FAILED '+name+'; inspect '+str(log));return result

def main()->None:
    need(__debug__,'Do not use Python -O')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archives-dir',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--verify-only',action='store_true')
    p.add_argument('--jobs',type=int,default=3)
    args=p.parse_args();need(1<=args.jobs<=6,'--jobs must be 1..6')
    out=args.output.resolve();ar=args.archives_dir.resolve()
    need(ar.is_dir(),'Archives directory does not exist')
    need(not out.exists() and out!=ROOT and ROOT not in out.parents,'Use a NEW output directory outside the release')
    out.mkdir(parents=True); (out/'logs').mkdir(); start=time.monotonic()
    entries=json.loads((ROOT/'ARCHIVES.json').read_text())['archives'];roots={};pinned={}
    for entry in entries:
        a=ar/entry['filename'];need(a.is_file(),'Missing archive '+str(a))
        roots[entry['version']]=extract(a,entry,out/'originals');pinned[str(a)]=sha(a)
    initial={v:verify_directory(r) for v,r in roots.items()}
    report={'schema':'n28-reviewer-check-v1','mode':'integrity_only' if args.verify_only else 'full_hardened_check','original_integrity':initial,'mathematical_status':'candidate; independent mathematical review OPEN','independent_external_review':False}
    if args.verify_only:
        report.update(all_pass=True,arithmetic_replayed=False)
        (out/'REVIEW_CHECK_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));return
    overlay=json.loads((ROOT/'OVERLAY.json').read_text());v8=roots['v8']
    need(sha(v8/overlay['original_path'])==overlay['original_sha256'],'Unexpected original helper')
    need(sha(ROOT/overlay['hardened_file'])==overlay['hardened_sha256'],'Unexpected hardened helper')
    work=out/'hardened_v8';shutil.copytree(v8,work)
    shutil.copyfile(ROOT/overlay['hardened_file'],work/overlay['original_path'])
    differences=[p.relative_to(v8).as_posix() for p in v8.rglob('*') if p.is_file() and p.read_bytes()!=(work/p.relative_to(v8)).read_bytes()]
    need(differences==[overlay['original_path']],'Unexpected overlay changes')
    # The original manifest is intentionally retained. The derivative is checked
    # here, not misrepresented as an unchanged original package.
    (out/'APPLIED_OVERLAY.json').write_text(json.dumps(overlay,indent=2)+'\n')
    py=[sys.executable,'-I','-B'];logs=out/'logs'
    jobs=[('v3',py+[str(roots['v3']/'check.py')],roots['v3']),
          ('v4',py+[str(roots['v4']/'replay.py'),'--replay','--output',str(out/'v4_check')],roots['v4'])]
    for v in ('v5','v6','v7'):
        jobs.append((v,py+[str(roots[v]/'replay.py'),'--check','--output',str(out/(v+'_check'))],roots[v]))
    jobs.append(('v8_hardened',py+[str(work/'src/check197.py'),'--output',str(out/'v8_check')],work))
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures={pool.submit(run,name,cmd,cwd,logs):name for name,cmd,cwd in jobs}
        for f in concurrent.futures.as_completed(futures):
            results.append(f.result());print('PASS',futures[f],flush=True)
    results.append(run('degree_scope',py+[str(work/'src/check_scope197.py'),'--output',str(out/'ALL_DEGREES_AND_FAN.json')],work,logs))
    results.append(run('helper_regressions',py+[str(ROOT/'test_helper.py'),'--original-v8',str(v8),'--output',str(out/'helper_regressions')],ROOT,logs))
    new=json.loads((out/'v8_check/EXACT_CHECK_REPORT.json').read_text())
    need(stable(new)==stable(json.loads((v8/'evidence/EXACT_CHECK_REPORT.json').read_text())),'Hardened v8 report differs')
    need(json.loads((out/'ALL_DEGREES_AND_FAN.json').read_text())==json.loads((v8/'evidence/ALL_DEGREES_AND_FAN.json').read_text()),'Degree-scope mismatch')
    # The individual wrappers check exhaustive domains; compare exact shared
    # evidence at stage boundaries instead of only comparing aggregate counts.
    pairs=[('v3','exploration/extra_n28_b15.json','v4','dependencies/v3_n28_demand_frontier.json'),
           ('v4','evidence/n28_demands.json','v5','dependencies/n28_demands.json'),
           ('v4','evidence/n28_projected_survivors.json','v5','dependencies/n28_projected_survivors.json'),
           ('v5','evidence/FINAL_SURVIVORS.json','v6','dependencies/v5_FINAL_SURVIVORS.json.gz'),
           ('v6','evidence/FINAL_SURVIVORS.json.gz','v7','dependencies/v6_FINAL_SURVIVORS.json.gz')]
    handoffs=[]
    for va,pa,vb,pb in pairs:
        left,right=roots[va]/pa,roots[vb]/pb
        need(left.is_file() and right.is_file(),'Missing handoff '+str((va,pa,vb,pb)))
        a,b=decoded(left),decoded(right);need(a==b,'Handoff mismatch')
        handoffs.append({'from':va+'/'+pa,'to':vb+'/'+pb,'decoded_sha256':hashlib.sha256(a).hexdigest(),'byte_identical':True})
    need(all(sha(Path(p))==s for p,s in pinned.items()),'Original ZIP changed')
    for v,r in roots.items():need(verify_directory(r)==initial[v],'Original extracted package changed: '+v)
    need(sha(work/overlay['original_path'])==overlay['hardened_sha256'],'Overlay changed during check')
    report.update(all_pass=True,arithmetic_replayed=True,hardened_helper_default=True,scope={'n':28,'equality_edges':196,'counterexample_edges':197},jobs=sorted(results,key=lambda x:x['name']),handoffs=handoffs,original_archives_unchanged=True,original_extracted_packages_unchanged=True,final_197_survivors=new['final_survivors'],new_196_survivors=json.loads((out/'v7_check/FULL_REPLAY_REPORT.json').read_text())['final_survivors'],seconds=time.monotonic()-start)
    (out/'REVIEW_CHECK_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,subprocess.SubprocessError) as e:
        print('FAILED: '+str(e),file=sys.stderr);sys.exit(1)
