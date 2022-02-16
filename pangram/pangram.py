alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
    if sentence == '':
        return False
        
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True
