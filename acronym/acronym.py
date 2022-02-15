import re

def abbreviate(words):
    words = re.sub('[-_]', ' ', words)
    words_split = words.split()
    acronym = ''
    for word in words_split:
        acronym = acronym + word[0].upper()

    return acronym
