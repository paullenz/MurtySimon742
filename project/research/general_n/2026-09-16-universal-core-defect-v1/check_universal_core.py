#!/usr/bin/env python3
"""Entry point for the preserved universal-core verification implementation.

Expand the graph sidecar before replay so
its final deterministic recompression also works in a freshly unpacked package.
"""
from pathlib import Path
import gzip
import runpy
import shutil
import sys


def main() -> None:
    root = Path(__file__).resolve().parent
    if "--replay-only" in sys.argv[1:]:
        graph = root / "GRAPH_RECORDS.json"
        if not graph.exists():
            with gzip.open(root / "GRAPH_RECORDS.json.gz", "rb") as source:
                with graph.open("wb") as destination:
                    shutil.copyfileobj(source, destination)
    runpy.run_path(str(root / "universal_core_checked.py"), run_name="__main__")


if __name__ == "__main__":
    main()
