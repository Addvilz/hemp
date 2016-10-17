from fabric.utils import error, puts


def print_err(message, func=None, exception=None, stdout=None, stderr=None):
    error('[Hemp] ' + message, func, exception, stdout, stderr)


def print_info(text, show_prefix=None, end="\n", flush=True):
    puts('[Hemp] ' + text, show_prefix, end, flush)
