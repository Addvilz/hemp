import yaml
from os.path import expanduser, join, isfile
from os import getcwd
from fabric.api import env

_default_locations = [
    expanduser('~'),
    getcwd()
]


def discover_hempfiles(extra_locations=None):
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
    if file_paths is None:
        file_paths = discover_hempfiles()
    config = {}
    for file_path in file_paths:
        stream = open(file_path, 'r')
        entries = yaml.load_all(stream)
        config = _deep_merge(config, entries)
    return config


def load_hempfiles(file_paths=None):
    config = parse_hempfiles(file_paths)
    for option, value in config.items():
        if option is not 'hemp':
            setattr(env, option, value)
        else:
            _load_hemp_configs(value)


def _load_hemp_configs(value):
    pass


def _deep_merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            _deep_merge(value, node)
        else:
            destination[key] = value
    return destination
