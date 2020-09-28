def abbreviate(text):
    titles_only = (c for c in text.title() if c.isupper())
    return ''.join(titles_only)

print(abbreviate("Halley's Comet"))