
def word_count(text):
    return len(text.split())


def longest_first(text):
    return sorted(text.split(), key=len, reverse=True)


def alphabetical(text):
    return sorted(text.split())
