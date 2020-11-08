"""Module for managing Jira actions"""
import os
import click

from utils import branchify

class Manager:
    def __init__(self, version_control):
        self.vcs = version_control

    def move_to_new_branch(self, issue):
        """Create new branch off master and move to it"""
        branch_input = branchify(
            click.prompt(
                'Please enter branch name',
                default=issue.default_title(),
            ),
        )
        new_branch = f"{issue.type()}/{branch_input}/{issue.key()}"
        click.echo(f"Creating new branch {new_branch}")
        self.vcs.git.checkout('master')
        click.echo("Pulling latest master")
        self.vcs.remotes.origin.pull('master')
        click.echo("Switching to new branch")
        current = self.vcs.create_head(new_branch)
        current.checkout()

    def update_scratch_window(self, issue):
        """Either overwrite or append the current scratch window"""
        project_name = os.path.basename(os.getcwd())
        scratch_path = f"/tmp/scratch/{project_name}.md"
        with open(scratch_path , 'r') as file:
            current_notes = file.read(100)
            overwrite = click.confirm(
                f"Overwrite current scratch window?\n{current_notes}...",
                default=True,
            )
        if overwrite:
            with open(scratch_path, 'w') as file:
                file.write(issue.description())
        else:
            with open(scratch_path, 'a') as file:
                file.write(issue.description())
