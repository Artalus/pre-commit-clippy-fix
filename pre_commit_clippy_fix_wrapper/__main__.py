#!/usr/bin/env python

import subprocess
import sys


def main() -> int:
    _, *script_args = sys.argv

    cmd = ['cargo', 'clippy', '--fix', '--allow-staged', '--allow-dirty', *script_args]
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    rc = process.wait()
    if rc != 0:
        print(f"{' '.join(cmd)} exited with {rc}; STDERR was:\n", file=sys.stderr)
        print(stderr.decode(), file=sys.stderr)
    return rc


if __name__ == '__main__':
    sys.exit(main())
