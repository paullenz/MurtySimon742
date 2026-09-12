#!/usr/bin/env python3
"""Verify the translated certificate without importing the original model."""
import json
from pathlib import Path
from count_model import build,verify

HERE=Path(__file__).resolve().parent
print(json.dumps(verify(build(),json.loads((HERE/'count_certificate.json').read_text())),indent=2))
