import pyaes, pbkdf2, binascii, os, secrets


def byte_to_text(bin_txt):
    (block, step) = len(bin_txt), 8
    byte_list = [bin_txt[i:i+step] for i in range(0, block, step)]
    return ''.join([chr(int(i, 2)) for i in byte_list])


def create_aes_keys():
    password = 's3cr3t*c0d3'
    with open('keysfile.txt', 'wb') as keysfile:
        for i in range(0, 100):
            password_salt = os.urandom(16)
            key = pbkdf2.PBKDF2(password, password_salt).read(32)
            keysfile.write(binascii.hexlify(key))


def read_keys_from_file():
    with open('keysfile.txt', 'rb') as keysfile:
        keys_data = keysfile.read()
    return keys_data


def create_key_format(keys_data):
    keys_list = []
    for i in range(0, 100):
        keys_list.append(keys_data[i*32:(i+1)*32])
    return keys_list


def iterate_all_keys(key_list):
    for i in range(0, len(key_list)):
        plain_text = 'Text From Encryption'
        iv = secrets.randbits(256)
        aes = pyaes.AESModeOfOperationCTR(key_list[i], pyaes.Counter(iv))
        cipher_text = aes.encrypt(plain_text)
        print('Encrypted:', binascii.hexlify(cipher_text))

        aes = pyaes.AESModeOfOperationCTR(key_list[i], pyaes.Counter(iv))
        decrypt_text = aes.decrypt(cipher_text)
        print('Decrypted:', decrypt_text)


if __name__ == '__main__':
    # create_aes_keys()
    keys_data = read_keys_from_file()
    key_list = create_key_format(keys_data)
    iterate_all_keys(key_list)

    d = b'0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
    print(byte_to_text(d))


