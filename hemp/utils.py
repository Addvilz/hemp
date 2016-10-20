import sys

from fabric.utils import error, puts
from git import RemoteProgress


def print_err(message, func=None, exception=None, stdout=None, stderr=None):
    error('[Hemp] ' + message, func, exception, stdout, stderr)


def print_info(text, show_prefix=None, end="\n", flush=True):
    puts('[Hemp] ' + text, show_prefix, end, flush)

def _print_git_output(stdout):
    for line in stdout.split('\n'):
        sys.stdout.write('[GIT] ' + line + '\n')
        sys.stdout.flush()

class _SimpleProgressPrinter(RemoteProgress):
    def _parse_progress_line(self, line):
        if '\r' in line:
            line = line.replace('\r', '\r[GIT] ')
        sys.stdout.write('[GIT] ' + line + '\n')
        sys.stdout.flush()