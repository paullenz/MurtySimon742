#!/usr/bin/env python3
"""Enforce a durable live CURRENT_STATE handoff.

STATUS_SYNC_POLICY_V2 makes CURRENT_STATE.md the per-commit operational source
of truth. RESEARCH_EXECUTION_POLICY_V3 adds explicit work-mode and deferred-admin
fields so research turns cannot silently drift into repository/CI maintenance.
README.md is lower frequency: if README itself is edited, its status block must
also change. Historical pre-v2 commits retain the legacy paired rule.

This is a process guard, not a proof checker or a test of factual freshness.
"""
from __future__ import annotations
import argparse
import re
import subprocess
import sys

START = '<!-- CURRENT-STATUS:START -->'
END = '<!-- CURRENT-STATUS:END -->'
CURRENT = 'CURRENT_STATE.md'
README = 'README.md'
POLICY_V2 = 'STATUS_SYNC_POLICY_V2'
POLICY_V3 = 'RESEARCH_EXECUTION_POLICY_V3'
LEGACY_RULE = 'Every commit must update the CURRENT-STATUS blocks'
REQUIRED_FIELDS = (
    'CHECKPOINT CLASS:',
    'WORK MODE:',
    'INSPECTED PREDECESSOR:',
    'LAST VERIFIED RESULT:',
    'UNPRESERVED WORK:',
    'DEFERRED ADMIN:',
    'NEXT ACTION:',
)
VALID_MODES = ('MATH', 'ADMIN', 'AUDIT', 'STATUS', 'RECOVERY')


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


def changed_paths(commit: str, parent: str | None) -> set[str]:
    if parent:
        out = git('diff-tree', '--no-commit-id', '--name-only', '-r', parent, commit)
    else:
        out = git('ls-tree', '-r', '--name-only', commit)
    return {line.strip() for line in out.splitlines() if line.strip()}


def check_v2(commit: str, parent: str | None, prior_policy: str) -> list[str]:
    failures: list[str] = []
    policy = git('show', f'{commit}:AGENTS.md', optional=True)
    if POLICY_V2 in prior_policy and POLICY_V2 not in policy:
        failures.append(f'{commit[:12]}: STATUS_SYNC_POLICY_V2 removed')
        return failures
    if POLICY_V3 in prior_policy and POLICY_V3 not in policy:
        failures.append(f'{commit[:12]}: RESEARCH_EXECUTION_POLICY_V3 removed')
        return failures

    new_current = block(git('show', f'{commit}:{CURRENT}', optional=True))
    old_current = block(git('show', f'{parent}:{CURRENT}', optional=True)) if parent else None
    if new_current is None:
        failures.append(f'{commit[:12]}: {CURRENT} lacks one nonempty status block')
    elif new_current == old_current:
        failures.append(f'{commit[:12]}: {CURRENT} status block unchanged')
    else:
        for field in REQUIRED_FIELDS:
            if field not in new_current:
                failures.append(f'{commit[:12]}: {CURRENT} status block missing {field}')
        if POLICY_V3 in policy:
            mode_match = re.search(r'WORK MODE:\s*`?([A-Z]+)`?', new_current)
            if not mode_match or mode_match.group(1) not in VALID_MODES:
                failures.append(
                    f'{commit[:12]}: {CURRENT} WORK MODE must be one of '
                    + ', '.join(VALID_MODES)
                )

    paths = changed_paths(commit, parent)
    if README in paths:
        new_readme = block(git('show', f'{commit}:{README}', optional=True))
        old_readme = block(git('show', f'{parent}:{README}', optional=True)) if parent else None
        if new_readme is None:
            failures.append(f'{commit[:12]}: {README} lacks one nonempty status block')
        elif new_readme == old_readme:
            failures.append(f'{commit[:12]}: {README} edited but status block unchanged')
    return failures


def check_legacy(commit: str, parent: str | None, policy: str, prior_policy: str) -> list[str]:
    if LEGACY_RULE not in policy and LEGACY_RULE not in prior_policy:
        return []
    failures: list[str] = []
    for path in (README, CURRENT):
        new = block(git('show', f'{commit}:{path}', optional=True))
        old = block(git('show', f'{parent}:{path}', optional=True)) if parent else None
        if new is None:
            failures.append(f'{commit[:12]}: {path} lacks one nonempty status block')
        elif new == old:
            failures.append(f'{commit[:12]}: {path} status block unchanged')
    return failures


def check_commit(commit: str) -> list[str]:
    parents = git('rev-list', '--parents', '-n', '1', commit).split()[1:]
    parent = parents[0] if parents else None
    policy = git('show', f'{commit}:AGENTS.md', optional=True)
    prior_policy = git('show', f'{parent}:AGENTS.md', optional=True) if parent else ''
    if POLICY_V2 in policy or POLICY_V2 in prior_policy:
        return check_v2(commit, parent, prior_policy)
    return check_legacy(commit, parent, policy, prior_policy)


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
        print(f'Live handoff synchronization PASS: {len(commits)} commit(s) inspected. Content truth and mathematical scope still require review.')
        return 0
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())