from fabric import main as fabric_main
from fabric import state
from fabric.main import load_tasks_from_module

from hemp import api
from hemp.hempfile import load_hempfiles
from hemp.utils import print_info


def main(fabfile_locations=None, file_paths=None):
    if fabfile_locations is None:
        fabfile_locations = ['~/fabfile.py']
        print_info('Added $HOME to fabfile locations')

    docstring, new_style, classic, default = load_tasks_from_module(api)
    tasks = new_style if state.env.new_style_tasks else classic
    state.commands.update(tasks)

    print_info('Forwarding execution to Fabric')

    _load_settings_original = fabric_main.load_settings

    def hemp_load_settings(path):
        print_info('Loading hempfiles')
        load_hempfiles(file_paths)
        return _load_settings_original(path)

    fabric_main.load_settings = hemp_load_settings
    fabric_main.main(fabfile_locations)
