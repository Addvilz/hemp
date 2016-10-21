"""
Quick and dirty import of Hemp api's
"""
from hemp.tasks.stage import on, development, production, staging
from gitutils import remote_tags, last_remote_tag, clone
from release import release_local
from workspace import create_temporary_workspace