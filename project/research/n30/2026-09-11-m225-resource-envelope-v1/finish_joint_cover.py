#!/usr/bin/env python3
"""Recover the final four certificates from the preserved discovery checkpoints."""
from pathlib import Path
import argparse,json

HERE=Path(__file__).resolve().parent

def compact(name,shapes,weights):
    return {'name':name,'lambda':weights[0],'c':weights[1],'mu':weights[2],
            'tau':{str(j):weights[2+j] for j in range(1,13) if weights[2+j]},
            'potential':{s:v for s,v in zip(shapes,weights[15:]) if v}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--probe-last-row',action='store_true');ap.add_argument('--output',type=Path,default=HERE/'JOINT_CERTIFICATES.json');args=ap.parse_args()
    if args.probe_last_row:
        from mine_joint_potential import search,SHAPES
        from compress_joint_cover import primitive,gap
        from simplify_joint_templates import simplify
        row=json.loads((HERE/'EXACT_AUDIT_SEVEN_INITIAL.json').read_text())['uncovered'][0]
        r=search(row)
        (HERE/'ONE_OLD_SCALAR_ROW_PROBE.json').write_text(json.dumps({'shapes':SHAPES,'row':r},indent=2)+'\n')
        w=primitive(r['weights'])
        rec={'weights':w,'assigned':[row],'minimum_integer_gap':gap(row,tuple(SHAPES),w)}
        out=simplify(SHAPES,rec)
        (HERE/'ONE_OLD_SCALAR_ROW_SIMPLIFIED.json').write_text(json.dumps({'shapes':SHAPES,'template':out},indent=2)+'\n')
    d=json.loads((HERE/'JOINT_RECTANGLES_SIMPLIFIED.json').read_text())
    out=[compact(f'B{i}',d['shapes'],T['weights']) for i,T in enumerate(d['templates'],1)]
    e=json.loads((HERE/'ONE_OLD_SCALAR_ROW_SIMPLIFIED.json').read_text())
    out.append(compact('C1',e['shapes'],e['template']['weights']))
    data={'schema':'n30-four-joint-envelope-certificates-v1','a':13,'b':16,'t':1,'dmax':12,'templates':out}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('Four explicit joint-envelope certificates written')

if __name__=='__main__':main()
