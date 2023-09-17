import math


def decrypt_message(key, message):
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


def encrypt_message(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def main():
    # 'Cenoonommstmme oo snnio. s s c'
    message = 'Common sense is not so common.'
    key = 8

    ciphertext = encrypt_message(key, message)
    plaintext = decrypt_message(key, ciphertext)

    print('Cipher Text:\n' + ciphertext + '\n\nDecrypted message:\n' + plaintext)


if __name__ == '__main__':
    main()

