#!/usr/bin/env python3
"""Recover the byte-exact frozen v4 payload from lossless local repository storage.
Uses the preserved v3 package for four unchanged dependencies. No network,
SciPy, optimisation solver or C++ compiler is needed for recovery.
"""
from pathlib import Path, PurePosixPath
from fractions import Fraction
from collections import Counter
import argparse, base64, gzip, hashlib, importlib.util, io, json, lzma, math
import random, subprocess, sys, tempfile, zipfile

CAPSULE_SHA256 = '21c137f3ff75c6d79eab69925fc09d71c47f4a7940291cf3ba9c0ca724cf71f8'
V3_RESTORER_BLOB = 'f6b82ac8a8977c3a0454dae7365fcd63f2c69023'
DEPENDENCIES = {
    'dependencies/v3_discover.py': 'discover.py',
    'dependencies/v3_check.py': 'check.py',
    'dependencies/v3_n28_demand_frontier.json': 'exploration/extra_n28_b15.json',
    'dependencies/v3_actual_graph_instances.json.gz': 'evidence/actual_graph_instances.json.gz',
}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    need(spec is not None and spec.loader is not None, 'Cannot load '+str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def recover(source, target, v3, zip_output):
    parts = sorted(source.glob('CAPSULE.part*.b64'))
    need(parts, 'Capsule parts missing')
    data = base64.b64decode(''.join(p.read_text().strip() for p in parts), validate=True)
    need(sha(data) == CAPSULE_SHA256, 'Capsule integrity failure')
    capsule = json.loads(lzma.decompress(data))
    need(capsule['format'] == 'label-tail-v4-lossless-1', 'Unknown capsule codec')
    need(not target.exists(), 'Output must be a new directory')
    need(zip_output is None or not zip_output.exists(), 'ZIP output already exists')
    target.mkdir(parents=True)
    for name, text in capsule['raw'].items():
        p = PurePosixPath(name)
        need(not p.is_absolute() and '..' not in p.parts, 'Unsafe path')
        dest = target.joinpath(*p.parts)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(text.encode())
    manifest = json.loads((target/'MANIFEST.json').read_text())
    (target/'dependencies').mkdir(exist_ok=True)
    for destination, original in DEPENDENCIES.items():
        value = (v3/original).read_bytes()
        need(sha(value) == manifest['files'][destination]['sha256'], 'v3 dependency mismatch: '+original)
        (target/destination).write_bytes(value)
    D = load('frozen_v4_dependency', target/'dependencies/v3_discover.py')
    historical = json.loads((target/'dependencies/v3_n28_demand_frontier.json').read_text())
    duals = {tuple(o['profile']['s']):o['cert'] for o in historical['certs']}
    records, demands, counts = [], [], Counter()
    for s in D.demands(12, 15, 1):
        lo, hi = D.bounds(s, 15, 1)
        cert = D.support_certificate(s, 15, hi)
        if cert is None:
            old = duals.get(tuple(s))
            if old is None:
                cert = {'kind':'OPEN'}
            else:
                y = list(map(Fraction, old['y'])); mu = Fraction(old['mu'])
                scale = math.lcm(mu.denominator, *(v.denominator for v in y))
                cert = {'kind':'dual', 'scale':scale,
                        'weights':[int(v*scale) for v in y], 'mu':int(mu*scale)}
        rec = {'s':s, 'rmin':lo, 'rmax':hi}
        if cert['kind'] == 'OPEN':
            demands.append(rec.copy())
        counts[cert['kind']] += 1
        rec['certificate'] = cert
        records.append(rec)
    initial = {'n':28, 'a':12, 'b':15, 'm':196, 't':1, 'counts':dict(counts), 'records':records}
    ev = target/'evidence'
    (ev/'n28_initial_certificates.json.gz').write_bytes(gzip.compress((json.dumps(initial,separators=(',',':'))+'\n').encode(),mtime=0))
    # Formatting is part of the original evidence, and is checked below.
    (ev/'n28_demands.json').write_text(json.dumps(demands,separators=(',',':'))+'\n')
    (ev/'n28_demands.txt').write_text(str(len(demands))+'\n'+'\n'.join(' '.join(map(str,o['s']+[o['rmin'],o['rmax']])) for o in demands)+'\n')
    rows = []
    for demand, indices in capsule['demand_rows'].items():
        for index in indices:
            rho = capsule['rhos'][index]
            rows.append([int(demand),sum(rho)]+rho)
    (ev/'n28_surviving_rows.txt').write_text(''.join(' '.join(map(str,row))+'\n' for row in rows))
    P = load('frozen_v4_projected', target/'check_projected.py')
    codes = capsule['projected_codes']
    need(len(codes)==len(rows), 'Wrong projected-code count')
    certs, survivors = [], []
    for row, code in zip(rows,codes):
        s = demands[row[0]]['s']
        if code == 0:
            survivors.append(row)
            continue
        if code == 1:
            cert = {'kind':'zero_slack', 'slack':sum(s)-row[1]-2}
        else:
            j = code-1
            rejected, pairs, bounds = P.threshold(s,row[2:],row[1],j)
            need(rejected, 'Stored projected disposition does not reject')
            cert = {'kind':'projected_pair', 'threshold':j, 'pairs':pairs, 'bounds':bounds}
        certs.append({'row':row, 'certificate':cert})
    (ev/'n28_projected_pair_certificates.json').write_text(json.dumps(certs,separators=(',',':'))+'\n')
    (ev/'n28_projected_survivors.json').write_text(json.dumps(survivors,separators=(',',':'))+'\n')
    # Recreate original seeded abstract inputs, not a new random sample.
    sys.path.insert(0,str(target))
    M = load('frozen_v4_mathematics', target/'test_mathematics.py')
    M.ROOT = target
    rng = random.Random(2026090704)
    M.knapsack_tests(rng)
    M.abstract_tests(rng)
    actual = {p.relative_to(target).as_posix() for p in target.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.name!='MANIFEST.json'}
    need(actual==set(manifest['files']), 'Missing or extra payload files')
    for name, item in manifest['files'].items():
        value = (target/name).read_bytes()
        need(len(value)==item['bytes'] and sha(value)==item['sha256'], 'Recovery mismatch: '+name)
    report = {'payload_files':len(actual),'all_original_file_hashes_match':True,
              'solver_used':False,'independent_mathematical_review':'OPEN'}
    if zip_output is not None:
        stream = io.BytesIO()
        with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for meta in capsule['zip_infos']:
                zi = zipfile.ZipInfo(meta['filename'],tuple(meta['date_time']))
                for key,value in meta.items():
                    if key not in ('filename','date_time'):
                        setattr(zi,key,value)
                path = PurePosixPath(meta['filename'])
                need(len(path.parts)>1 and '..' not in path.parts,'Unsafe ZIP path')
                z.writestr(zi,target.joinpath(*path.parts[1:]).read_bytes(),compresslevel=9)
        value = stream.getvalue()
        need(sha(value)==capsule['original_zip_sha256'],'Original ZIP mismatch: check Python/zlib versions')
        zip_output.parent.mkdir(parents=True,exist_ok=True)
        zip_output.write_bytes(value)
        report.update(original_zip_bytes=len(value),original_zip_sha256=sha(value))
    return report

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--v3-directory',type=Path,help='Already recovered original demand-support-v3 package')
    ap.add_argument('--zip-output',type=Path)
    args = ap.parse_args()
    source = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix='murty-v3-dependency-') as temp:
        v3 = args.v3_directory
        if v3 is None:
            restorer = source.parent/'2026-09-07-demand-support-v3'/'restore_checkpoint.py'
            value = restorer.read_bytes()
            blob = hashlib.sha1(b'blob '+str(len(value)).encode()+b'\0'+value).hexdigest()
            need(blob==V3_RESTORER_BLOB,'Pinned v3 recovery program mismatch')
            v3 = Path(temp)/'v3'
            subprocess.run([sys.executable,'-I','-B',str(restorer),'--output',str(v3)],check=True)
        report = recover(source,args.output.resolve(),v3.resolve(),args.zip_output)
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
