#!/usr/bin/env python3
"""One bounded solver process. It makes no mathematical infeasibility claim."""
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix
from storage import read_model

def main():
    model_path,result_path,input_path=map(Path,sys.argv[1:])
    model=read_model(model_path);inputs=json.loads(input_path.read_text())
    rr=[];cc=[];vv=[];lo=[];hi=[]
    for k,row in enumerate(model['rows']):
        for j,c in row['terms']:rr.append(k);cc.append(j);vv.append(c)
        lo.append(-np.inf if row['lower'] is None else row['lower'])
        hi.append(np.inf if row['upper'] is None else row['upper'])
    matrix=csc_matrix((np.array(vv,dtype=float),(np.array(rr,dtype=np.int32),np.array(cc,dtype=np.int32))),shape=(len(lo),len(model['variables'])))
    matrix.indices=matrix.indices.astype(np.int32);matrix.indptr=matrix.indptr.astype(np.int32)
    started=time.perf_counter()
    result=milp(np.zeros(len(model['variables'])),integrality=np.ones(len(model['variables']),dtype=np.int32),
        bounds=Bounds(model['lower_bounds'],model['upper_bounds']),constraints=LinearConstraint(matrix,lo,hi),
        options={**inputs['solver_options'],'disp':True})
    report=dict(status=int(result.status),message=str(result.message),original_solver_seconds=time.perf_counter()-started,
                variables=len(model['variables']),rows=len(lo),nonzero_coefficients=len(vv),
                raw_x=None if result.x is None else result.x.tolist())
    for name in ['fun','mip_node_count','mip_dual_bound','mip_gap']:
        value=getattr(result,name,None);report[name]=None if value is None else float(value)
    result_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('SAVED_RESULT',result_path.name,report['status'],flush=True)

if __name__=='__main__':main()
