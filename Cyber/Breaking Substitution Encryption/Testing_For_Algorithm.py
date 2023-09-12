import pprint, string


# My Method
def createWordPattern(word):
    word = word.upper()  # Convert the word to uppercase for consistency
    pattern = ""
    letter_to_index = {}
    current_index = 0

    for letter in word:
        if letter not in letter_to_index:
            letter_to_index[letter] = current_index
            current_index += 1
        pattern += str(letter_to_index[letter])

    return pattern


# Gal's Method:
def createWordPattern_v2(word):
    word = word.upper()  # Convert the word to uppercase for consistency
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])

    return '.'.join(wordPattern)


# Make word pattern form dictionary
def main():
    all_patterns = {}
    # Change path accordingly
    fo = open('E:\CodingEXS\Python_Stuff\Cyber\Breaking Substitution Encryption\Detecting English\dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        pattern = createWordPattern_v2(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)

    fo = open('allWordPatternDict.py', 'w')
    fo.write('all_patterns= ')
    fo.write(pprint.pformat(all_patterns))
    fo.close()




# Testing:
word1 = "HELLO"
word2 = "ABLE"
word3 = "SUSPECT"

pattern1 = createWordPattern(word1)
pattern2 = createWordPattern(word2)
pattern3 = createWordPattern(word3)

print(f"{word1} -> {pattern1}")
print(f"{word2} -> {pattern2}")
print(f"{word3} -> {pattern3}")


def decryptMessage(cipher, rand_key):
    decryption_table = str.maketrans(rand_key, string.ascii_lowercase)
    plain_text = cipher.translate(decryption_table)
    return plain_text
