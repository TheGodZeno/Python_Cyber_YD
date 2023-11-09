import sys

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256 # one byte give 256 different values

def main():
    filename = 'encrypted_file.txt'
    mode = 'encrypt'

    if mode == 'encrypt':
        message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        publicKeyFilename = 'al_sweigart_pubkey.txt'
        print('this is the encryption:')
        encryptText = encryptAndWriteToFile(filename, publicKeyFilename, message)
    elif mode == 'decrypt':
        #TODO - H.W
        #palintext = cipher^d mod N
        pass


def encryptAndWriteToFile(messageFilename, publicKeyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    keySize, n, e = readKeyFile(publicKeyFilename)
    if keySize < blockSize * 8:
        sys.exit('ERROR: block size is %s bits and key size is %s. in RSA the block size must be smaller than the key size')

    encryptBlocks = encryptMsg(message, (n,e), blockSize)
    for i in range(len(encryptBlocks)):
        encryptBlocks[i] = str(encryptBlocks[i])
    encryptContent = ''.join(encryptBlocks)

    encryptContent = '%s_%s_%s' % (len(message), blockSize, encryptContent)
    fo  = open(messageFilename, 'w')
    fo.write(encryptContent)
    fo.close()
    return encryptContent


def readKeyFile(publicKeyFilename):
    fo = open(publicKeyFilename)
    content = fo.read()
    fo.close()
    keySize, n, e = content.split(',')
    return (int(keySize), int(n), int(e))


def encryptMsg(message, key , blockSize=DEFAULT_BLOCK_SIZE):
    encryptBlocks = []
    n, e = key
    for block in getBlockSizeFromText(message, blockSize):
        # cipher RSA = plain_txt_block^e mod N
        encryptBlocks.append(pow(block, e, n))
    return encryptBlocks


def getBlockSizeFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    messageBytes = message.encode('ascii')
    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        # for i in range(min(blockSize, len(messageBytes) - blockStart)):
        #     blockInt += messageBytes[blockStart + i] * (BYTE_SIZE ** i)
        for i in range(blockStart, min(blockStart+blockSize), len(messageBytes)):
            blockInt += messageBytes[i]*(BYTE_SIZE**(i%blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlock(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    pass