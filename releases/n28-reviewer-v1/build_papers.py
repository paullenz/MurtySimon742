#!/usr/bin/env python3
"""Build the two reviewer PDFs; does not execute the mathematical check."""
from pathlib import Path
import hashlib,json,os,re,subprocess,tempfile,shutil
ROOT=Path(__file__).resolve().parent
NAMES=('N28_Reviewer_Manuscript_v1','N28_Verification_Companion_v1')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if not __debug__:raise ValueError('Keep assertions enabled')
    manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())['files']
    for name,item in manifest.items():
        p=ROOT/name
        if p.stat().st_size!=item['bytes'] or h(p)!=item['sha256']:raise ValueError('Source mismatch: '+name)
    report={'schema':'n28-reviewer-paper-build-v1','mathematical_check_performed_by_this_script':False,'source_manifest_sha256':h(ROOT/'SOURCE_MANIFEST.json'),'source_commit':os.environ.get('GITHUB_SHA'),'papers':{}}
    with tempfile.TemporaryDirectory() as td:
        d=Path(td)
        for name in NAMES:
            shutil.copyfile(ROOT/(name+'.tex'),d/(name+'.tex'))
            for _ in range(3):
                p=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=d,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                if p.returncode:raise RuntimeError(p.stdout.decode(errors='replace'))
            log=(d/(name+'.log')).read_text(errors='replace')
            if 'Overfull' in log or 'undefined references' in log or 'undefined citations' in log:raise ValueError('Unresolved typesetting problem: '+name)
            m=re.search(r'Output written on .*?\((\d+) pages?',log,re.S)
            if not m:raise ValueError('Missing build page count')
            shutil.copyfile(d/(name+'.pdf'),ROOT/(name+'.pdf'))
            report['papers'][name]={'source_sha256':h(ROOT/(name+'.tex')),'pdf_sha256':h(ROOT/(name+'.pdf')),'pdf_bytes':(ROOT/(name+'.pdf')).stat().st_size,'pages':int(m.group(1)),'three_pass_build':True,'overfull_or_unresolved_reference_warnings':False}
    report['all_pass']=True
    (ROOT/'PAPER_BUILD_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    files={p.relative_to(ROOT).as_posix():{'bytes':p.stat().st_size,'sha256':h(p)} for p in ROOT.rglob('*') if p.is_file() and p.name not in ('MANIFEST.json','PUBLICATION_RECEIPT.json') and '__pycache__' not in p.parts}
    (ROOT/'MANIFEST.json').write_text(json.dumps({'schema':'n28-reviewer-release-files-v1','files':dict(sorted(files.items()))},indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
