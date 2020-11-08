"""Tests for the utils module"""

from utils import branchify, note_formatted
import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Branch One", 'branch-one'),
        ("branch one", 'branch-one'),
        ("branch_one", 'branch_one'),
        ("", ""),
        (" ", ""),
    ],
)
def test_branchify(test_input, expected):
    """
    Given an input string,
    When I run it through the branchify method,
    Then I expect to receive a lowercased string in kebab case
    """
    assert branchify(test_input) == expected


class TestNoteFormatted:
    def test_long_strings(self):
        """
        Given an input text of more than 80 characters,
        When I format the text,
        Then I expect the text to be wrapped at 80 characters
        """
        long_text = 'a ' * 50
        formatted = note_formatted(long_text)
        assert len(formatted.partition('\n')[0]) == 79

    def test_code_snippets(self):
        """
        Given an input text with jira code snippets {{  }},
        When I format the text,
        Then I expect the text to contain markdown code snippets ` `
        """
        text = 'code sample {{code_here}}'
        assert note_formatted(text) == 'code sample `code_here`'
