#!/usr/bin/env python3
"""Check every new commit for paired, substantive current-status block edits.

No network, writes or third-party dependencies. This is a documentation guard,
not a proof checker or a test of factual freshness. Revisions are resolved to
commit IDs before use. Historical commits predating AGENTS.md's rule are skipped.
"""
from __future__ import annotations
import argparse
import re
import subprocess
import sys

START = '<!-- CURRENT-STATUS:START -->'
END = '<!-- CURRENT-STATUS:END -->'
PATHS = ('README.md', 'CURRENT_STATE.md')


def git(*args: str, optional: bool = False) -> str:
    p = subprocess.run(['git', *args], text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=False)
    if p.returncode:
        if optional:
            return ''
        raise RuntimeError(p.stderr.strip() or 'git command failed')
    return p.stdout


def resolve(ref: str) -> str:
    if not re.fullmatch(r'[A-Za-z0-9_./~^{}@+-]+', ref) or ref.startswith('-'):
        raise ValueError('invalid revision')
    return git('rev-parse', '--verify', ref + '^{commit}').strip()


def block(text: str) -> str | None:
    if text.count(START) != 1 or text.count(END) != 1:
        return None
    before, after = text.split(START)
    body, _ = after.split(END)
    if END in before or not body.strip():
        return None
    return ' '.join(body.split())


def check_commit(commit: str) -> list[str]:
    parents = git('rev-list', '--parents', '-n', '1', commit).split()[1:]
    parent = parents[0] if parents else None
    rule = 'Every commit must update the CURRENT-STATUS blocks'
    policy = git('show', f'{commit}:AGENTS.md', optional=True)
    prior = git('show', f'{parent}:AGENTS.md', optional=True) if parent else ''
    if rule not in policy and rule not in prior:
        return []
    failures = []
    if rule in prior and rule not in policy:
        failures.append(f'{commit[:12]}: standing status rule removed')
    for path in PATHS:
        new = block(git('show', f'{commit}:{path}', optional=True))
        old = block(git('show', f'{parent}:{path}', optional=True)) if parent else None
        if new is None:
            failures.append(f'{commit[:12]}: {path} lacks one nonempty status block')
        elif new == old:
            failures.append(f'{commit[:12]}: {path} status block unchanged')
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='exclusive prior commit; omit to check only head')
    parser.add_argument('--head', default='HEAD')
    args = parser.parse_args()
    try:
        head = resolve(args.head)
        if args.base and set(args.base) != {'0'}:
            base = resolve(args.base)
            commits = git('rev-list', '--reverse', f'{base}..{head}').split()
        elif args.base:
            commits = git('rev-list', '--reverse', head).split()
        else:
            commits = [head]
        errors = [err for commit in commits for err in check_commit(commit)]
        if errors:
            print('\n'.join(errors), file=sys.stderr)
            return 1
        print(f'Status synchronization PASS: {len(commits)} commit(s) inspected. '
              'Content truth and mathematical scope still require review.')
        return 0
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
