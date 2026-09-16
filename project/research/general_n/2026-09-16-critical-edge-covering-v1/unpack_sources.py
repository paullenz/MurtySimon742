#!/usr/bin/env python3
"""Restore the three byte-preserved verification sources beside this file."""
import base64, hashlib, io, zipfile
from pathlib import Path
p=Path(__file__).resolve().parent
raw=base64.b64decode((p/'SOURCE_BUNDLE.zip.b64').read_text(),validate=False)
assert hashlib.sha256(raw).hexdigest()=='a858d93ca2c1c3ed73d14f37c2d01a9d76207d74e95f575abcdf9c8110cea00c'
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    names=set(z.namelist())
    assert names=={'check_covering.py','verify_covering.cpp','summarize_checks.py'}
    for name in sorted(names):
        content=z.read(name);target=p/name
        if target.exists() and target.read_bytes()!=content:
            raise RuntimeError('Refusing to overwrite a different existing source: '+name)
        target.write_bytes(content)
print('Restored three exact sources. To regenerate and check: python3 check_covering.py')
