from os import getcwd
from os.path import expanduser, join, isfile

import yaml
from fabric.state import env
from hemp.internal.utils import print_info

_default_locations = [
    expanduser('~'),
    getcwd()
]


def discover_hempfiles(extra_locations=None):
    # type: (list) -> list
    locations = _default_locations
    if extra_locations is not None:
        locations = extra_locations + _default_locations
    files = []
    for directory in locations:
        hemp_file = join(directory, 'hemp.yml')
        if isfile(hemp_file):
            files.append(hemp_file)
    return files


def parse_hempfiles(file_paths=None):
    # type: (list) -> dict
    if file_paths is None:
        file_paths = discover_hempfiles()
    config = {}
    for file_path in file_paths:
        stream = open(file_path, 'r')
        entries = yaml.load(stream)
        config = _deep_merge(config, entries)
    return config


def load_hempfiles(file_paths=None):
    # type: (list) -> None
    if 'hemp' in env:
        return
    config = parse_hempfiles(file_paths)
    for option, value in config.items():
        if 'hemp' != option:
            print_info('[ENV] {0}: {1}'.format(option, value))
        setattr(env, option, value)


def _deep_merge(source, destination):
    # type: (dict, dict) -> dict
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            _deep_merge(value, node)
        else:
            destination[key] = value
    return destination
