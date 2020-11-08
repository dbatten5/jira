"""Tests for the Jira module"""

import pytest

import jira
from jira import Issue

class TestIssue():
    """Tests for the jira Issue class"""
    issue = None

    @pytest.fixture(autouse=True)
    def set_up(self, mocker, requests_mock):
        """Set up the class, including mocked API call"""
        base_url = 'https://acme.atlassian.net/rest/api/2/issue'
        mocker.patch.object(
            jira,
            'BASE_URL',
            base_url,
        )
        requests_mock.register_uri(
            'GET',
            f"{base_url}/ID-123",
            json={
                'fields': {
                    'summary': 'The summary',
                    'description': 'The description',
                    'issuetype': {
                        'name': 'Subtask'
                    }
                }
            },
        )
        self.issue = Issue('https://acme.atlassian.net/browse/ID-123')

    def test_default_title(self):
        """
        Given a Jira issue,
        When I retreve the title,
        Then I expect to receive the title of the issue in branch form
        """
        assert self.issue.default_title() == 'the-summary'

    def test_type(self):
        """
        Given a Jira issue,
        When I retrieve the type,
        Then I expect to receive the type of ticket in lowercase
        """
        assert self.issue.type() == 'task'

    def test_key(self):
        """
        Given a Jira issue,
        When I retrieve the key,
        Then I expect to receive the key / id of the ticket
        """
        assert self.issue.key() == 'ID-123'

    def test_description(self):
        """
        Given a Jira issue,
        When I retrieve the description,
        Then I expect to receive the description in markdown note format
        """
        assert self.issue.description() == 'The description'
