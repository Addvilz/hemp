from os import chmod
from os import mkdir
from os.path import join
from tempfile import mkdtemp


def create_temporary_workspace(version=None, mode=0700):
    # type: (str, int) -> str
    """
    Create a temporary directory, optionally by placing a subdirectory: version
    :rtype: str
    :return: Directory path
    """
    workspace = mkdtemp('hemp_')
    if version is not None:
        workspace = join(workspace, version)
        mkdir(workspace, mode)
    chmod(workspace, mode)
    return workspace
