from shutil import rmtree
from tempfile import mkdtemp

from git import Repo
from semver import bump_build, bump_prerelease, bump_patch, bump_major, bump_minor

from hemp.utils import _SimpleProgressPrinter, print_err, print_info, _print_git_output


def release_local(url, version='patch', base='master', integration=None, default_version='0.0.1', use_prefix=None):
    workspace = mkdtemp()
    repo = Repo.clone_from(url, workspace, progress=_SimpleProgressPrinter())

    if repo.bare:
        print_err('Cloned a bare repository, can not release [???]')

    origin = repo.remote('origin')

    if repo.active_branch.name != base:
        origin.fetch('refs/heads/{0}:refs/heads/{0}'.format(base), progress=_SimpleProgressPrinter())
        repo.heads[base].checkout()

    last_tag = None

    if repo.tags:
        sorted_tags = sorted(repo.tags, key=lambda t: t.commit.committed_date)
        current_tag = sorted_tags[-1].path[10:]
        print_info('Current tag is {0}'.format(current_tag))
        if use_prefix is not None and current_tag.startswith(use_prefix):
            last_tag = current_tag[len(use_prefix):]
        else:
            last_tag = current_tag

    print_info('Last known version: {0}'.format(last_tag))

    if 'build' == version:
        next_version = bump_build(last_tag)

    elif 'prerelease' == version:
        next_version = bump_prerelease(last_tag)

    elif 'patch' == version:
        next_version = bump_patch(last_tag)

    elif 'minor' == version:
        next_version = bump_minor(last_tag)

    elif 'major' == version:
        next_version = bump_major(last_tag)

    else:
        if version in ['build', 'prerelease', 'patch', 'minor', 'major']:
            next_version = default_version
        else:
            next_version = version

    print_info('Next version: {0}'.format(next_version))

    next_tag = next_version

    if use_prefix is not None:
        next_tag = use_prefix + next_version

    print_info('Next tag: {0}'.format(next_tag))

    if integration is not None and integration in repo.heads:
        print_info('Found integration branch "{0}", fetching'.format(integration))
        origin.fetch('refs/heads/{0}:refs/heads/{0}'.format(integration), progress=_SimpleProgressPrinter())
        print_info('Will now attempt fast-forward {0} to include {1}'.format(base, integration))
        _print_git_output(repo.git.merge('--commit', '--no-edit', '--stat', '--ff-only', '-v', integration))

    print_info('Tagging and pushing version')

    release_tag = repo.create_tag(next_tag, message='Release tag of {0}'.format(next_version))
    origin.push([release_tag, repo.heads[base]], progress=_SimpleProgressPrinter())

    print_info('Done, clearing workspace')
    rmtree(workspace)
