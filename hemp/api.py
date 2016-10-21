"""
Quick and dirty import of Hemp api's
"""
from hemp.tasks.stage import on, development, production, staging
from gitutils import remote_tags, last_remote_tag, clone, repo_url_to_project_name
from release import release_local
from workspace import create_temporary_workspace