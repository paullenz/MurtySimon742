#!/usr/bin/env python3
"""Recover the exact frozen v3 payload and original ZIP from its lossless capsule.

No SciPy, solver, network access, or prior checkout is required. The capsule stores
all non-derived values; redundant row tables and seeded test data use deterministic
recipes. Every recovered file and the ZIP must match the original SHA-256.
Byte-level recovery was tested with CPython 3.13.5 and zlib 1.3.1; an incompatible
serializer/PRNG/compressor must fail the hashes, never silently alter evidence.
Run only trusted project code, as for the original replay scripts.
"""
from __future__ import annotations
import argparse, base64, contextlib, gzip, hashlib, importlib.util, io, json, lzma
from fractions import Fraction
from pathlib import Path, PurePosixPath
import zipfile


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, 'Cannot load '+str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def recover(source: Path, target: Path, zip_path: Path | None) -> dict:
    manifest = json.loads((source/'CAPSULE_MANIFEST.json').read_text())
    encoded = []
    for part in manifest['parts']:
        data = (source/part['name']).read_bytes()
        require(len(data) == part['bytes'] and digest(data) == part['sha256'],
                'Capsule part integrity failure: '+part['name'])
        encoded.append(data.strip())
    packed = base64.b64decode(b''.join(encoded), validate=True)
    require(digest(packed) == manifest['decoded_xz_sha256'], 'XZ integrity failure')
    raw = lzma.decompress(packed)
    require(digest(raw) == manifest['json_sha256'], 'Capsule JSON integrity failure')
    capsule = json.loads(raw)
    require(capsule['format'] == 'murty-demand-support-lossless-capsule-v1', 'Unknown format')
    require(not target.exists(), 'Output directory already exists; use a new path')
    if zip_path is not None:
        require(not zip_path.exists(), 'ZIP output already exists')
    for entry in capsule['files']:
        name = PurePosixPath(entry['name'])
        require(not name.is_absolute() and '..' not in name.parts, 'Unsafe payload path')
    target.mkdir(parents=True)

    def save(entry: dict, data: bytes) -> None:
        require(len(data) == entry['bytes'] and digest(data) == entry['sha256'],
                'Recovered bytes differ from the original: '+entry['name'])
        path = target/entry['name']
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    # Literal source, reports, manifests, and nonredundant graph-test data first.
    for entry in capsule['files']:
        if entry['kind'] == 'text':
            save(entry, entry['data'].encode())
        elif entry['kind'] == 'gzip-text-v1':
            save(entry, gzip.compress(entry['data'].encode(), mtime=0))
    discover = load_module('frozen_v3_discovery', target/'discover.py')
    rows = load_module('frozen_v3_rows', target/'exploration/refine_rows.py')
    for entry in capsule['files']:
        kind = entry['kind']
        if kind == 'final-evidence-v1':
            data = entry['data']
            for rec in data['records']:
                if rec['certificate']['kind'] == 'residual_rows':
                    recovered = []
                    for total in range(rec['rmin'], rec['rmax']+1):
                        for rho in discover.residual_profiles(data['a'], data['b'], total):
                            recovered.append({'rho':list(rho),
                                              'certificate':discover.row_certificate(rec['s'],rho)})
                    rec['certificate']['rows'] = recovered
            raw = (json.dumps(data, sort_keys=True, separators=(',',':'))+'\n').encode()
            save(entry, gzip.compress(raw, mtime=0))
        elif kind == 'exploration-rows-v1':
            data = entry['data']; a = data['n']-1-data['b']
            for rec in data['profiles']:
                profile = rec['profile']; recovered = []
                for total in range(profile['rmin'], profile['rmax']+1):
                    for rho in rows.residuals(a, data['b'], total):
                        recovered.append({'r':total, 'rho':rho,
                                          'cert':rows.cut(profile['s'],rho)})
                rec['rows'] = recovered
            save(entry, (json.dumps(data, indent=2)+'\n').encode())
        elif kind == 'exploration-duals-v1':
            data = entry['data']; b = data['b']; n = data['n']
            t = n*n//4-b*(n-b)
            for key in ['survivors','certs']:
                recovered = []
                for s, sparse_y, mu in data[key]:
                    lo, hi = discover.bounds(s,b,t)
                    y = ['0']*len(s)
                    for index,value in sparse_y:
                        y[index] = value
                    descending = sorted(s,reverse=True)
                    value = sum(Fraction(y[k])*sum(descending[:k+1]) for k in range(len(s)))+b*Fraction(mu)
                    cert = {'lower_excess':str(value), 'upper_excess':hi-b,
                            'reject':value>hi-b, 'y':y, 'mu':mu, 'status':entry['status']}
                    recovered.append({'profile':{'s':s,'rmin':lo,'rmax':hi},'cert':cert})
                data[key] = recovered
            save(entry, (json.dumps(data,indent=2)+'\n').encode())
        elif kind == 'seeded-abstract-v1':
            abstract = load_module('frozen_v3_abstract',target/'test_abstract_support.py')
            with contextlib.redirect_stdout(io.StringIO()):
                abstract.main()
            # The original seeded recipe writes its evidence and report. Check
            # both against the frozen manifest below; no new run is called old.
            save(entry,(target/entry['name']).read_bytes())
        else:
            require(kind in ('text','gzip-text-v1'), 'Unknown file codec: '+kind)
    for entry in capsule['files']:
        data = (target/entry['name']).read_bytes()
        require(len(data)==entry['bytes'] and digest(data)==entry['sha256'],
                'Post-recovery integrity failure: '+entry['name'])
    original = json.loads((target/'MANIFEST.json').read_text())
    require(len(original['files'])==41, 'Unexpected original manifest size')
    result = {'files_restored':len(capsule['files']), 'manifested_payload_files':41,
              'every_original_file_sha256_matches':True,
              'mathematical_status':'candidate; independent review OPEN'}
    if zip_path is not None:
        stream = io.BytesIO()
        with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_DEFLATED,
                             compresslevel=capsule['zip_level']) as archive:
            for meta in capsule['zip']:
                zi = zipfile.ZipInfo(meta['filename'],tuple(meta['date_time']))
                for key,value in meta.items():
                    if key not in ('filename','date_time'):
                        setattr(zi,key,value)
                name = PurePosixPath(meta['filename'])
                require(len(name.parts)>1 and '..' not in name.parts,'Unsafe ZIP path')
                data = (target/Path(*name.parts[1:])).read_bytes()
                archive.writestr(zi,data,compresslevel=capsule['zip_level'])
        data = stream.getvalue()
        require(len(data)==capsule['zip_bytes'] and digest(data)==capsule['zip_sha256'],
                'ZIP bytes do not match the original; check Python/zlib version')
        zip_path.parent.mkdir(parents=True,exist_ok=True)
        zip_path.write_bytes(data)
        result['original_zip_sha256'] = digest(data)
        result['original_zip_bytes'] = len(data)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='New output directory')
    parser.add_argument('--zip-output',type=Path,help='Optional new path for exact original ZIP')
    args = parser.parse_args()
    print(json.dumps(recover(Path(__file__).resolve().parent,args.output,args.zip_output),
                     indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
