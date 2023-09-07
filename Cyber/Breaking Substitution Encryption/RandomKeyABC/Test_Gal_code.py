import string
import random

LETTERS = string.ascii_uppercase


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

def translate(key, data, letters):
    translation = ''
    charsA = letters
    charsB = key

    for symbol in data:
        if symbol.upper() in charsA:
            index = charsA.find(symbol.upper())
            translation += charsB[index]
        else:
            translation += symbol
    return translation


def encrypt_by_sub(plain_text, key):
    return translate(key, plain_text, LETTERS)


def decrypt_by_sub(cipher_text, key):
    return translate(LETTERS, cipher_text, key)


# Example usage:
plaintext = "HELLO"
key = getRandomKey()
ciphertext = encrypt_by_sub(plaintext, key)
print("Plaintext:", plaintext)
print("Let:", LETTERS)
print("Key:", key)
print("Ciphertext:", ciphertext)

decrypted_message = decrypt_by_sub(ciphertext, key)
print("Decrypted Message:", decrypted_message)


# Version 2.0
def translate_v2(key, data, mode):
    translation = ''
    charsA = LETTERS
    charsB = key

    if mode == 'dec':
        charsA, charsB = charsB, charsA

    for symbol in data:
        if symbol.upper() in charsA:
            index = charsA.find(symbol.upper())
            translation += charsB[index]
        else:
            translation += symbol
    return translation