import git.cmd as git_cmd
from natsort.natsort import natsorted, ns


def remote_tags(url, alg=ns.VERSION):
    tags = []
    remote_git = git_cmd.Git()
    for line in remote_git.ls_remote('--tags', '--quiet', url).split('\n'):
        hash_ref = line.split('\t')
        tags.append(hash_ref[1][10:])
    return natsorted(tags, alg=alg)


def last_remote_tag(url, alg=ns.VERSION):
    return remote_tags(url, alg)[-1]
