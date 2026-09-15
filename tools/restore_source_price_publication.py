#!/usr/bin/env python3
"""Repair one diagnosed publication error; preserve the original expected hash.

Run only in the dedicated main-branch workflow. The successful one-off restoration
is now retained for manual replay only. No theorem, generator, expected hash or
validator is changed. Publication, when needed, is atomic and non-forced.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

PACKAGE = Path('project/research/general_n/2026-09-14-source-sharing-v1')
RESULT = PACKAGE / 'ORIGINAL_SIX_RESULTS.json'
AUDIT = PACKAGE / 'CI_AUDIT.md'
BAD = '0705a7da14d49e81bd02f5442464b81b5796791454d5a3de8cace333bc74596c'
GOOD = '1953c61d26c68dc2bcbb9aeddbe0d18336e05b118541f4d9ca3f9528c808caae'
START = '<!-- SOURCE-PRICE-PUBLICATION:START -->'
END = '<!-- SOURCE-PRICE-PUBLICATION:END -->'


def restore(path: Path) -> bool:
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest == GOOD:
        return False
    if digest != BAD:
        raise ValueError('Refusing an unrecognized result-file version')
    data = json.loads(raw)
    row = next(r for r in data['profiles'] if r['row'] == 338)
    entry = next(r for r in row['results'] if r['coefficients'] == 'low-q-weight')
    if len(entry['best']['prices']) != 29 or entry['best']['prices'] != [0] * 29:
        raise ValueError('The diagnosed extra-zero location no longer matches')
    entry['best']['prices'].pop()
    fixed = (json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if hashlib.sha256(fixed).hexdigest() != GOOD:
        raise ValueError('Repair does not restore the ORIGINAL expected byte hash')
    path.write_bytes(fixed)
    return True


def command(*args: str) -> str:
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=True)
    print(result.stdout, end='', flush=True)
    return result.stdout


def update_status(path: Path, receipt: str) -> None:
    text = path.read_text()
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError(f'{path}: expected one pending publication-status marker')
    left, rest = text.split(START)
    _, right = rest.split(END)
    if '<!-- CURRENT-STATUS:START -->' not in left or '<!-- CURRENT-STATUS:END -->' not in right:
        raise ValueError(f'{path}: publication receipt must remain inside current status')
    path.write_text(left + START + '\n' + receipt + '\n' + END + right)


def main() -> None:
    if os.environ.get('GITHUB_REPOSITORY') != 'paullenz/MurtySimon742':
        raise RuntimeError('Dedicated canonical-repository workflow required')
    if os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise RuntimeError('Publication is restricted to main')
    run = os.environ['GITHUB_RUN_ID']
    if not run.isdigit():
        raise ValueError('Invalid workflow run ID')
    parent = command('git', 'rev-parse', 'HEAD').strip()
    changed = restore(RESULT)
    command(sys.executable, str(PACKAGE / 'run_replay.py'))

    # The one-off publication completed on 2026-09-14 and later status rewrites
    # intentionally removed its temporary publication markers. A manual replay of
    # an already-correct checkout must therefore be read-only, not a fresh commit.
    status_texts = [Path(name).read_text() for name in ['README.md', 'CURRENT_STATE.md']]
    markers_present = all(
        text.count(START) == 1 and text.count(END) == 1 for text in status_texts
    )
    if not markers_present:
        if changed:
            raise RuntimeError(
                'Repair was required but publication markers are no longer present; '
                'refusing to create a new historical publication commit'
            )
        print('Restoration already published; unchanged replay passed. No repository mutation required.',
              flush=True)
        return

    # Source, copied-input, canonical-input and ORIGINAL result-byte hashes plus
    # both COMPLETE parsed replay outputs have now passed the unchanged harness.
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    receipt = (
        f'**Publication verification — {stamp}; run {run}.** '
        f'The original source-price result file is restored to its pre-existing SHA256 `{GOOD}`. '
        'The UNCHANGED offline harness passed all source/input hashes, the canonical twelve-row input, '
        'the six-row transcription, 9,043 incidence/demand checks, 371 brute-force comparisons, '
        'three hostile/boundary fixtures and complete output equality for all 576 price evaluations. '
        'The failed run 34904353492 remains recorded. '
        '**Mathematical status unchanged: zero new profile exclusions.** '
        'This receipt covers the original source-sharing package, NOT the separate stronger price/witness package. '
        'The current label/destination/common-residual-neighbourhood research target below remains unchanged. '
        f'Validated checkout: `{parent}`; this atomic commit publishes the repaired data and paired status receipt. '
        f'See [repair audit]({AUDIT.as_posix()}).')
    for name in ['README.md', 'CURRENT_STATE.md']:
        update_status(Path(name), receipt)
    with AUDIT.open('a') as output:
        output.write(f'\n## Completed exact replay, {stamp}\n\n')
        output.write(f'Run {run}; checked-out predecessor `{parent}`. ')
        output.write('The known extra-zero repair restored the original byte hash. ' if changed
                     else 'The correct original byte hash was already present. ')
        output.write('The unchanged full harness passed before this publication attempt. '
                     'No expected hash, source, numerical result or validator was weakened. '
                     'Only the original source-sharing package was replayed. '
                     'The whole workflow also requires non-forced publication and a final remote-ref check; '
                     'its final conclusion must be inspected separately.\n')
    command(sys.executable, 'tools/check_readme_review_materials.py')
    files = ['README.md', 'CURRENT_STATE.md', str(RESULT), str(AUDIT)]
    command('git', 'add', '--', *files)
    staged = set(command('git', 'diff', '--cached', '--name-only').splitlines())
    if not staged.issubset(set(files)) or not {'README.md', 'CURRENT_STATE.md'} <= staged:
        raise RuntimeError('Unexpected staged files or missing paired status')
    # Use GitHub's canonical Actions identity. Do not invent a generic
    # users.noreply.github.com address: GitHub may map it to another GitHub account.
    command('git', '-c', 'user.name=github-actions[bot]',
            '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
            'commit', '-m', f'Restore original source-price data; record exact replay {run} in both statuses')
    command(sys.executable, 'scripts/check_status_sync.py', '--base', parent, '--head', 'HEAD')
    command('git', 'push', 'origin', 'HEAD:main')
    published = command('git', 'rev-parse', 'HEAD').strip()
    remote = command('git', 'ls-remote', 'origin', 'refs/heads/main').split()[0]
    if remote != published:
        # Do not overwrite another writer. A later descendant may have appeared;
        # retain this diagnostic for a human/agent to reconcile explicitly.
        raise RuntimeError(f'Remote changed during receipt verification: {remote}; published {published}')
    print(f'Publication verified: {published}', flush=True)


if __name__ == '__main__':
    main()
