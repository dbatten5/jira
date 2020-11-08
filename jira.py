"""Module for interacting with the Jira API"""

import requests
from requests.auth import HTTPBasicAuth

from config import BASE_URL, EMAIL, API_TOKEN
from utils import branchify, note_formatted

class Issue():
    """Class for abstracting a Jira issue"""
    def __init__(self, url):
        self.url = url
        self.response = self.__fetch()

    def default_title(self) -> str:
        """Return the title of a issue in branch form"""
        title = self.__fields()['summary']
        return branchify(title)

    def type(self) -> str:
        """Return the type of issue"""
        issue_type = self.__fields()['issuetype']['name'].lower()
        if 'task' in issue_type:
            return 'task'
        return issue_type

    def key(self) -> str:
        """Return the ID of a issue"""
        return self.url.rsplit('/', 1)[-1]

    def description(self) -> str:
        """Return the description of an issue, formatted to be used in a md note"""
        return note_formatted(self.__fields()['description'])

    def __fields(self) -> str:
        return self.response['fields']

    def __fetch(self) -> dict:
        issue_id = self.key()
        return requests.get(
            f"{BASE_URL}/{issue_id}?fields=summary,description,issuetype",
            auth=HTTPBasicAuth(EMAIL, API_TOKEN),
            headers={'Content-Type': 'application/json'}
        ).json()
