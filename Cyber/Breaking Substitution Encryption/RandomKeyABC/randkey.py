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


plaintext = "Codes operated by substituting according to a large codebook which linked a random string of characters or numbers to a word or phrase. For example, UQJHSE could be the code for Proceed to the following coordinates. When using a cipher the original information is known as plaintext, and the encrypted form as ciphertext. The ciphertext message contains all the information of the plaintext message, but is not in a format readable by a human or computer without the proper mechanism to decrypt it."
key = getRandKey()

# Encrypt the message
encrypted_message = encryptMessage(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decryptMessage(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
print("Key:", key)

