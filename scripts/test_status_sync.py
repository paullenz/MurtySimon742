#!/usr/bin/env python3
"""Regression tests for the prospective paired-status guard; isolated temp Git repo."""
from pathlib import Path
import subprocess
import sys
import tempfile

SCRIPT = Path(__file__).with_name('check_status_sync.py').resolve()
START, END = '<!-- CURRENT-STATUS:START -->', '<!-- CURRENT-STATUS:END -->'


def run(*args, cwd):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def main():
    checks = 0
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for args in [('init', '-q'), ('config', 'user.name', 'Status guard test'),
                     ('config', 'user.email', 'status-guard@example.invalid')]:
            assert run('git', *args, cwd=root).returncode == 0

        def write_status(name, text):
            (root / name).write_text(f'{START}\n{text}\n{END}\n')

        def commit(message):
            assert run('git', 'add', '.', cwd=root).returncode == 0
            assert run('git', 'commit', '-qm', message, cwd=root).returncode == 0
            return run('git', 'rev-parse', 'HEAD', cwd=root).stdout.strip()

        def expect(code, *args):
            nonlocal checks
            result = run(sys.executable, str(SCRIPT), *args, cwd=root)
            assert result.returncode == code, result.stdout + result.stderr
            checks += 1

        (root / 'old.txt').write_text('Historical commit before rule.\n')
        historical = commit('historic')
        expect(0)
        (root / 'AGENTS.md').write_text('Every commit must update the CURRENT-STATUS blocks\n')
        for name in ('README.md', 'CURRENT_STATE.md'):
            write_status(name, 'Policy installed; mathematical status unchanged.')
        installed = commit('install')
        expect(0, '--base', historical)
        (root / 'code.py').write_text('print(1)\n')
        commit('missing both updates')
        expect(1)
        write_status('README.md', 'README-only update.')
        commit('missing handoff update')
        expect(1)
        for name in ('README.md', 'CURRENT_STATE.md'):
            write_status(name, 'Paired update; mathematical status unchanged.')
        good = commit('paired')
        expect(0)
        for name in ('README.md', 'CURRENT_STATE.md'):
            with (root / name).open('a') as f:
                f.write('Outside-block change.\n')
        commit('outside only')
        expect(1)
        for name in ('README.md', 'CURRENT_STATE.md'):
            write_status(name, '  Paired   update; mathematical status unchanged.  ')
        commit('whitespace only')
        expect(1)
        expect(1, '--base', installed)
        expect(1, '--base', '0' * 40)
        (root / 'AGENTS.md').write_text('Rule removed.\n')
        for name in ('README.md', 'CURRENT_STATE.md'):
            write_status(name, 'Changed while policy removed.')
        commit('removed rule')
        expect(1)
        expect(2, '--head', '--not-a-ref')
    print(f'Status guard regression PASS: {checks} checks.')


if __name__ == '__main__':
    main()
