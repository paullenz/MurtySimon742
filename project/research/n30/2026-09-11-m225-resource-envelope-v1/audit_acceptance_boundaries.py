#!/usr/bin/env python3
"""Hostile checks for incomplete covers, negative weights and the p=rho+2 edge."""
from pathlib import Path
import importlib.util,json,subprocess,sys,tempfile

HERE=Path(__file__).resolve().parent

def main():
    data=json.loads((HERE/'JOINT_CERTIFICATES.json').read_text())
    tests=[]
    with tempfile.TemporaryDirectory() as work:
        for name,mutate in [
            ('missing_exception_template',lambda d:d.update(templates=d['templates'][:-1])),
            ('negative_monotone_weight',lambda d:d['templates'][0]['potential'].update(sv=-1)),
        ]:
            d=json.loads(json.dumps(data));mutate(d);p=Path(work)/(name+'.json');p.write_text(json.dumps(d))
            run=subprocess.run([sys.executable,'-I','-B',str(HERE/'verify_joint_certificates.py'),'--certificates',str(p)],capture_output=True,text=True)
            assert run.returncode!=0,name
            tests.append({'mutation':name,'rejected':True,'returncode':run.returncode})
    spec=importlib.util.spec_from_file_location('checker',HERE/'verify_joint_certificates.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    rows=v.reconstruct(v.PROFILE);witness=None
    for T in data['templates']:
        for s,rhos in rows:
            for r in set(rhos):
                Q=min(13-r,sum(si<=r for si in s))
                full=min((v.sval(T,r,q,p),q,p) for q in range(Q+1) for p in range(r+3))
                wrong=min(v.sval(T,r,q,p) for q in range(Q+1) for p in range(r+2))
                if full[0]<wrong:
                    witness={'template':T['name'],'s':s,'rho':r,'qmax':Q,'full_minimum':full[0],'minimizer_q':full[1],'minimizer_p':full[2],'incorrect_rho_plus_one_minimum':wrong};break
            if witness:break
        if witness:break
    assert witness and witness['minimizer_p']==witness['rho']+2
    out={'status':'PASS','negative_acceptance_tests':tests,'correct_supplement_bound_witness':witness,
         'meaning':'The actual acceptance path rejects incomplete/negative-weight inputs. The full source box includes a necessary boundary minimizer that the historical invalid tightening would omit.'}
    (HERE/'ACCEPTANCE_BOUNDARY_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
