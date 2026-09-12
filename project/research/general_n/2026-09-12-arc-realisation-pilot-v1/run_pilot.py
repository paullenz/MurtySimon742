#!/usr/bin/env python3
"""Run the frozen pilot sequentially, preserving every bounded attempt."""
from pathlib import Path
import hashlib,json,os,platform,subprocess,sys,time
import scipy,numpy
from model import build
from storage import write_model,sha
from check_witness import extract
HERE=Path(__file__).resolve().parent

def main():
    out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else HERE/'runs'
    out.mkdir(parents=True,exist_ok=False)
    raw=(HERE/'pilot_inputs.json').read_bytes();inputs=json.loads(raw)
    assert inputs['plan_sha256']==sha((HERE/'PLAN.md').read_bytes())
    environment=dict(python=platform.python_version(),platform=platform.platform(),scipy=scipy.__version__,numpy=numpy.__version__,
        input_sha256=sha(raw),plan_sha256=inputs['plan_sha256'],solver='SciPy milp / bundled HiGHS; full version in each solver log',
        options=inputs['solver_options'],wall_guard_seconds=inputs['wall_guard_seconds'],
        source_hashes={p.name:sha(p.read_bytes()) for p in HERE.glob('*.py')})
    (out/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
    results=[];catalogue={}
    for rec in inputs['sample']:
        for mode in inputs['modes']:
            stem=rec['layer']+'-'+str(rec['state_id'])+'-'+mode
            model=build(rec,mode);model_path=out/(stem+'.model.json.gz.b64')
            meta=write_model(model_path,model);catalogue[stem+'.model.json']=meta
            (out/'EVIDENCE_STORAGE.json').write_text(json.dumps(dict(schema='arc-model-storage-v1',encoding='base64(gzip), mtime=0',files=catalogue),indent=2)+'\n')
            solver_path=out/(stem+'.solver.json');log_path=out/(stem+'.solver.log')
            command=[sys.executable,str(HERE/'solve_one.py'),str(model_path),str(solver_path),str(HERE/'pilot_inputs.json')]
            started=time.perf_counter();timed_out=False
            with log_path.open('wb') as log:
                try:
                    run=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,timeout=inputs['wall_guard_seconds'],env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
                    returncode=run.returncode
                except subprocess.TimeoutExpired:timed_out=True;returncode=None
            result=dict(layer=rec['layer'],state_id=rec['state_id'],mode=mode,model=meta,
                command=['python','solve_one.py',model_path.name,solver_path.name,'../pilot_inputs.json'],
                original_wall_seconds=time.perf_counter()-started,process_returncode=returncode,wall_guard_fired=timed_out,
                log=log_path.name,log_sha256=sha(log_path.read_bytes()),solver_file=None,classification='OPEN_PROCESS_LIMIT' if timed_out else 'OPEN_PROCESS_ERROR')
            if solver_path.exists():
                result['solver_file']=solver_path.name;result['solver_sha256']=sha(solver_path.read_bytes())
                solved=json.loads(solver_path.read_text());result['solver_status']=solved['status']
                witness=extract(model,solved['raw_x']);result['witness']=witness
                if witness and witness['status']=='VERIFIED_RELAXATION_WITNESS':result['classification']=witness['status']
                elif witness:result['classification']=witness['status']
                elif solved['status']==2:result['classification']='UNCERTIFIED_INFEASIBILITY_REPORT'
                else:result['classification']='OPEN_NO_VERIFIED_INCUMBENT'
            results.append(result)
            (out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
            print(stem,result['classification'],'wall_seconds',round(result['original_wall_seconds'],3),flush=True)
    print('DONE',len(results),'attempts; no solver status is an exclusion',flush=True)

if __name__=='__main__':main()
