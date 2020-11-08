"""Module for defining CLI"""

from os import getcwd
import click
from git import Repo, RemoteProgress
from jira import Issue
from utils import branchify

@click.group()
def cli():
    """Jira management"""

@click.option('--url', prompt='Please provide the Jira issue url')
@cli.command()
def new(url):
    """Start a new Jira ticket"""
    repo = Repo('/Users/dominic.batten/projects/eigen')
    if repo.is_dirty():
        return click.echo('You have unstaged changes. Aborting')
    issue = Issue(url)
    # branch_input = branchify(
    #     click.prompt(
    #         'Please enter branch name',
    #         default=issue.default_title(),
    #     ),
    # )
    # new_branch = f"{issue.type()}/{branch_input}/{issue.key()}"
    # click.echo(f"Creating new branch {new_branch}")
    # repo.git.checkout('master')
    # click.echo("Pulling latest master")
    # repo.remotes.origin.pull('master')
    # click.echo("Switching to new branch")
    # current = repo.create_head(new_branch)
    # current.checkout()
    # with open('/tmp/scratch.vim' , 'r') as file:
    #     current_notes = file.read(100)
    #     overwrite = click.confirm(
    #         f"Overwrite current scratch window?\n{current_notes}...",
    #         default=True,
    #     )
    # if overwrite:
    with open('/tmp/scratch.md' , 'w') as file:
        file.write(issue.description())
    # else:
    #     with open('/tmp/scratch.vim' , 'a') as file:
    #         file.write(issue.description())
    click.echo("Done")
