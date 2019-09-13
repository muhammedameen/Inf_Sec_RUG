import sys
from string import ascii_lowercase as ALPHABET

def shift(message, offset):
    trans = str.maketrans(ALPHABET, ALPHABET[offset:] + ALPHABET[:offset])
    return message.lower().translate(trans)

print(shift(input("Input message you would like encrypted:\n"), 19))