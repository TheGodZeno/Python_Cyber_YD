import random
import string


def getRandKey():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    rand_key = ''.join(alphabet)
    return rand_key


def encryptMessage(message, rand_key):
    translation_table = str.maketrans(string.ascii_lowercase, rand_key)
    encrypted_message = message.lower().translate(translation_table)
    return encrypted_message


def decryptMessage(cipher, rand_key):
    decryption_table = str.maketrans(rand_key, string.ascii_lowercase)
    plain_text = cipher.translate(decryption_table)
    return plaintext


plaintext = "This is a secret message."
key = getRandKey()

# Encrypt the message
encrypted_message = encryptMessage(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decryptMessage(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
print("Key:", key)