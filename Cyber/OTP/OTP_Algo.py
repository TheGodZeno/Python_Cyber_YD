import my_prng
import onetimepad

def text_to_byte(text):
    return ''.join([format(ord(c), 'b').zfill(8) for c in text])


def byte_to_text(bin_txt):
    (block, step) = len(bin_txt), 8
    byte_list = [bin_txt[i:i+step] for i in range(0, block, step)]
    return ''.join([chr(int(i, 2)) for i in byte_list])


def otp_enc_dec(bin_txt, bin_pad):
    return bytes([a ^ b for a, b in zip(bin_txt, bin_pad)])


def main():
    text = input('enter your plaintext:')
    bin_text = text_to_byte(text)
    seed = '1010101010'  # get it from sys.argv
    bin_pad = my_prng.create_uniqe_pad(seed)
    print('Current pad:\n', bin_pad)
    enc = otp_enc_dec(bytes(bin_text, 'ascii'), bytes(bin_pad[0:len(bin_text)], 'ascii'))
    print('Encrypted text (binary): ', enc.hex())
    dec = otp_enc_dec(enc, bytes(bin_pad[0:len(bin_text)], 'ascii'))
    print('Decrypted text (binary): ', dec)
    print(byte_to_text(dec))


if __name__ == '__main__':
    main()
