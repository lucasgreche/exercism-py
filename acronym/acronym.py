import re

def abbreviate(words):
    return ''.join(i[0] for i in re.findall(r'[A-Z0-9]+\'[A-Z0-9]|[A-Z0-9]+', words.upper()))