def is_isogram(string):
    word = string.lower()
    pass_letter = []
    for letter in word:
        if letter.isalpha() and letter in pass_letter:
            return False
        pass_letter.append(letter)
    return True

