# Jira

Python cli package to automate some Jira actions for local development

## Actions

### Start a new ticket

```
jira new
```

This does the following:

- Pull the given Jira issue using the Jira API
- Ask for a branch name, giving the title of the issue as a default
- Switch to master branch and pull
- Checkout the new branch
- Add the description of the issue to a notepad for use with [scratch.vim](https://github.com/mtth/scratch.vim)

## Dependencies

- `click` to handle the CLI aspect
- `requests` to handle the HTTP request to the API
- `gitpython` to manage the git actions
