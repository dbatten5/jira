from jira import Issue
import requests_mock

@requests_mock.Mocker()
class TestIssue():
    base_url = 'https://acme.atlassian.net/rest/api/2/issue'

    def __init__(self, m):
        self.issue_url = 'https://acme.atlassian.net/browse/ID-123'
        m.register_uri(
            'GET',
            f"{self.base_url}/ID-123",
            json={
                'fields': {
                    'summary': 'The summary',
                    'description': 'The description',
                    'issuetype': {
                        'name': 'Task'
                    }
                }
            },
        )
        self.issue = Issue()

