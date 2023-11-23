import string
# from secret import MSG


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)


def decryption(cipher):
    pt = []
    for char in cipher:
        pt.append(((char - 18) * 179) % 256)
    return bytes(pt)

# ct = encryption(MSG)
# f = open('./msg.enc','w')
# f.write(ct.hex())
# f.close()
#
# with open('msg.enc') as f:
#     ct = bytes.fromhex(f.read())
#
# pt = decryption(ct)
# print(pt)


def findX(y, k):
    x = y + 256*k -18
    if x % 123 == 0:
        return x
    elif k == 0:
        return -1
    else:
        return findX(y, k-1)

def decryptChar(hex_value):
    num = int(hex_value, 16)
    x = findX(num, 100)
    if x == -1:
        print('ERROR!!')
        return -1
    else:
        return x/123


def decryptAll():
    dec_res = ''
    with open('msg.enc') as f:
        encData = f.read()
        for i in range(0, len(encData),2):
            hex_val = encData[i] + encData[i+1]
            dec_res += chr(int(decryptChar(hex_val)))

    print(dec_res)

decryptAll()

