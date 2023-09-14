import random
import string

LETTERS = string.ascii_uppercase

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            index = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[index].upper()
            else:
                translated += charsB[index].lower()
        else:
            translated += symbol
    return translated


def main():
    message = 'Codes operated by substituting according to a large codebook which linked a random string of characters or numbers to a word or phrase. For example, "UQJHSE" could be the code for "Proceed to the following coordinates." When using a cipher the original information is known as plaintext, and the encrypted form as ciphertext. The ciphertext message contains all the information of the plaintext message, but is not in a format readable by a human or computer without the proper mechanism to decrypt it.'
    key = getRandomKey()  # 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    mode = 'encrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)

    print('Using key %s' % key)
    print('The %sed message is:' % mode)
    print(translated)

    print(message)
    print(encryptMessage('pgkatwylzovdunirbxhqmesfcj', message))


if __name__ == '__main__':
    main()


# My Method of encrypting and decrypting the message (Optional)

def encryptMessage_v2(message, rand_key):
    translation_table = str.maketrans(string.ascii_lowercase, rand_key)
    encrypted_message = message.lower().translate(translation_table)
    return encrypted_message


def decryptMessage_v2(cipher, rand_key):
    decryption_table = str.maketrans(rand_key, string.ascii_lowercase)
    plain_text = cipher.translate(decryption_table)
    return plain_text
