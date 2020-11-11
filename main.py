"""Module for defining CLI"""

import click
from git import Repo
from jira import Issue
from manager import Manager

@click.group()
def cli():
    """Jira management"""

@click.option('--url', prompt='Please provide the Jira issue url')
@cli.command()
def new(url):
    """Start a new Jira ticket"""
    repo = Repo('.', search_parent_directories=True)
    manager = Manager(version_control=repo)

    if repo.is_dirty():
        return click.echo('You have unstaged changes. Aborting')

    issue = Issue(url)

    branch_name = manager.move_to_new_branch(issue)
    manager.update_scranch_window(issue, branch_name)

    click.echo("Done")
