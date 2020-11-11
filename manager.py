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
        return new_branch

    def update_scranch_window(self, issue, branch_name):
        """Add the description to a new scranch note"""
        project_name = os.path.basename(os.getcwd())
        scranch_project_path = f"/tmp/scranch/{project_name}"
        if not os.path.exists(scranch_project_path):
            os.makedirs(scranch_project_path)
        sanitized_branch_name = branch_name.replace('/', '_')
        scratch_path = f"{scranch_project_path}/{sanitized_branch_name}.md"
        with open(scratch_path , 'w+') as file:
            file.write(issue.description())
