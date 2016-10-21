from git import Git, Repo
from natsort.natsort import natsorted, ns

from hemp.internal.utils import SimpleProgressPrinter, print_info


def remote_tags(url, alg=ns.VERSION):
    # type: (str, int) -> list
    """
    List all available remote tags naturally sorted as version strings
    :rtype: list
    :param url: Remote URL of the repository
    :param alg: Sorting algorithm
    :return: list of available tags
    """
    tags = []
    remote_git = Git()
    for line in remote_git.ls_remote('--tags', '--quiet', url).split('\n'):
        hash_ref = line.split('\t')
        tags.append(hash_ref[1][10:])
    return natsorted(tags, alg=alg)


def last_remote_tag(url, alg=ns.VERSION):
    # type: (str, int) -> str
    """
    Get last tag from remote repository. This utility retrieves and sorts tags in natural order,
    not by date!
    :rtype: str
    :param url:
    :param alg:
    :return: last available tag, sorted in natural order
    """
    return remote_tags(url, alg)[-1]


def clone(url, directory, single_branch=None):
    print_info('Cloning {0} to {1} {2}'.format(
        url,
        directory,
        '[full clone]' if single_branch is None else '[{0}]'.format(single_branch)
    ))
    # type: (str, str, str) -> Repo
    """
    Clone a repository, optionally using shallow clone
    :rtype: Repo
    :param url: URL of the repository
    :param directory: Directory to clone to
    :param single_branch: branch to clone if shallow clone is preferred
    :return: GitPython repository object of the newly cloned repository
    """
    args = {
        'url': url,
        'to_path': directory,
        'progress': SimpleProgressPrinter(),
        'recursive': True
    }

    if single_branch is not None:
        args['depth'] = 1
        args['branch'] = single_branch
        args['single_branch'] = True

    return Repo.clone_from(**args)
