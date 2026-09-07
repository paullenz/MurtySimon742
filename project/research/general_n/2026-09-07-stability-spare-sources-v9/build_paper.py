#!/usr/bin/env python3
"""Build the authored TeX and inventory the release; this is not a proof replay."""
from pathlib import Path
import hashlib,json,subprocess,tempfile,re,shutil
ROOT=Path(__file__).resolve().parent
NAME='General_Structural_Theorems_v9'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    m=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
    for name,e in m['files'].items():
        p=ROOT/name
        if p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:raise ValueError('Source hash mismatch: '+name)
    with tempfile.TemporaryDirectory(prefix='v9-paper-') as td:
        td=Path(td)
        for i in range(3):
            proc=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(td),str(ROOT/(NAME+'.tex'))],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=False)
            if proc.returncode:raise RuntimeError(proc.stdout.decode(errors='replace'))
        log=(td/(NAME+'.log')).read_text(errors='replace')
        if re.search(r'Overfull|undefined references|LaTeX Warning: Label',log):raise ValueError('Unresolved paper layout/reference warning')
        pages=int(re.search(r'Output written on .+?\((\d+)\s+pages?',log,re.S).group(1))
        shutil.copyfile(td/(NAME+'.pdf'),ROOT/(NAME+'.pdf'))
        version=subprocess.run(['pdflatex','--version'],stdout=subprocess.PIPE,text=True,check=True).stdout.splitlines()[0]
    report={'paper':NAME+'.pdf','pages':pages,'bytes':(ROOT/(NAME+'.pdf')).stat().st_size,'sha256':sha(ROOT/(NAME+'.pdf')),
      'tex_sha256':sha(ROOT/(NAME+'.tex')),'readable_proof_sha256':sha(ROOT/'PROOF.md'),'three_pass_build':True,
      'overfull_or_unresolved_reference_warnings':False,'tex_version':version,'mathematical_replay_performed_by_build':False}
    (ROOT/'PAPER_BUILD_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    files={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name not in ('MANIFEST.json','PUBLICATION_RECEIPT.json')}
    (ROOT/'MANIFEST.json').write_text(json.dumps({'schema':'v9-checkpoint-manifest-v1','files':files},indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
