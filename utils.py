"""Module for providing various string formatting utils"""

import textwrap

def branchify(name: str) -> str:
    """Return a lowercase, kebab-case string"""
    return name.strip().replace(' ', '-').lower()

def note_formatted(text: str) -> str:
    """Format to look nice in a markdown note"""
    text = text.replace('{{', '`').replace('}}', '`')

    return wrap_text(text)

def wrap_text(text: str, width=80) -> str:
    """Wrap text at a given width, preserving new lines"""
    if '\n' not in text:
        return textwrap.fill(text, width=width)

    new_text = ""

    lines = text.split("\n")

    for line in lines:
        if len(line) > width:
            wrapper = textwrap.TextWrapper(width=width, break_long_words=False)
            line = '\n'.join(wrapper.wrap(line))
        new_text += line + "\n"

    return new_text
