#!/usr/bin/env python3
"""Verify the lossless audit storage and optionally recover to a new directory."""
from __future__ import annotations
import argparse
import base64
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import sys
import tarfile


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def safe_name(name: str) -> bool:
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and str(p) == name and ".." not in p.parts and "\\" not in name


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New extraction directory; omitted means verify only")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    meta = json.loads((here / "STORAGE_MANIFEST.json").read_text())
    pieces = []
    seen_parts = set()
    for item in meta["parts"]:
        name = item["path"]
        require(safe_name(name) and name not in seen_parts, "Unsafe or duplicate storage path")
        seen_parts.add(name)
        data = (here / name).read_bytes()
        require(len(data) == item["bytes"], f"Storage length mismatch: {name}")
        require(hashlib.sha256(data).hexdigest() == item["sha256"], f"Storage checksum mismatch: {name}")
        pieces.append(data.strip())
    raw = base64.b64decode(b"".join(pieces), validate=True)
    require(len(raw) == meta["archive_bytes"], "Archive length mismatch")
    require(hashlib.sha256(raw).hexdigest() == meta["archive_sha256"], "Archive checksum mismatch")
    root = meta["root"]
    require(safe_name(root) and "/" not in root, "Invalid package root")
    files = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:xz") as archive:
        for member in archive:
            name = member.name
            require(member.isfile() and safe_name(name), f"Unsupported or unsafe member: {name}")
            require(name.startswith(root + "/") and name not in files, f"Wrong root or duplicate: {name}")
            stream = archive.extractfile(member)
            require(stream is not None, f"Missing member content: {name}")
            files[name] = stream.read()
    manifest_name = root + "/MANIFEST.json"
    manifest = json.loads(files[manifest_name])
    expected = manifest["files"]
    require(len(expected) == meta["payload_files"], "Payload count mismatch")
    require(set(files) == {root + "/" + n for n in expected} | {manifest_name}, "Manifest coverage mismatch")
    for name, item in expected.items():
        require(safe_name(name), "Unsafe manifest path")
        data = files[root + "/" + name]
        require(len(data) == item["bytes"], f"Payload length mismatch: {name}")
        require(hashlib.sha256(data).hexdigest() == item["sha256"], f"Payload checksum mismatch: {name}")
    for name in ("REPORT.md", "RESULTS.json"):
        require((here / name).read_bytes() == files[root + "/" + name], f"Readable mirror differs: {name}")
    if args.output is not None:
        require(not args.output.exists() and not args.output.is_symlink(), "Output must be a new directory")
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in files.items():
            target = args.output.joinpath(*PurePosixPath(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as handle:
                handle.write(data)
    print(json.dumps({"storage_parts": len(pieces), "payload_files": len(expected),
                      "all_checks_pass": True, "archive_sha256": meta["archive_sha256"],
                      "output": str(args.output) if args.output is not None else None}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, tarfile.TarError) as exc:
        print(f"Audit recovery FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
