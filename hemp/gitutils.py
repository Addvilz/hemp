
from natsort.natsort import natsorted, ns
from git import Git, Repo

from hemp.utils import _SimpleProgressPrinter


def remote_tags(url, alg=ns.VERSION):
    tags = []
    remote_git = Git()
    for line in remote_git.ls_remote('--tags', '--quiet', url).split('\n'):
        hash_ref = line.split('\t')
        tags.append(hash_ref[1][10:])
    return natsorted(tags, alg=alg)


def last_remote_tag(url, alg=ns.VERSION):
    return remote_tags(url, alg)[-1]


def clone(url, directory, single_branch=None):
    args = {
        'url': url,
        'to_path': directory,
        'progress': _SimpleProgressPrinter(),
        'recursive': True
    }

    if single_branch is not None:
        args['depth'] = 1
        args['branch'] = single_branch
        args['single_branch'] = True

    return Repo.clone_from(**args)
