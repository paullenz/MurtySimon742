#!/usr/bin/env python3
"""Focused floating test: does the complete D=2 rectangle layer alone support all 902 n=29,t=2 profiles?"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=902:raise SystemExit(f'expected902 got {len(P)}')
 M,rect,diag=rd.build(P,12,16,10,(2,),());st=time.time();res=M.solve()
 out={'schema':'n29-t2-D2-all-scan-v1','profiles':902,'support':'all B(2,V), V=0..16','success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
 if res.success:
  act=[{'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8];out['active_rectangles']=act;out['active_count']=len(act);out['objective']=float(res.fun)
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
