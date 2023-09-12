import string
UPPERLETTER = string.ascii_uppercase
LETTER_AND_SPACE = string.ascii_uppercase + string.ascii_lowercase + ' \t\n'


def loadDictionary():
    dictFile = open('dictionary.txt')
    englishWords = {}
    for word in dictFile.read().split('\n'):
        englishWords[word] = None
    dictFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def removeNonLetter(msg):
    lettersOnly = []
    for symbol in msg:
        if symbol in LETTER_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def getEnglishCount(msg):
    msg = msg.upper()
    msg = removeNonLetter(msg)
    possible_words = msg.split()

    matches = 0
    if not possible_words:
        return 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches +=1

    return matches/len(possible_words)

# My Method
def isEnglish(msg, wordPercentage=80, letterPercentage=80):
    words = msg.upper().split()
    english_word_count = sum(1 for word in words if word.upper() in ENGLISH_WORDS)
    non_english_word_count = len(words) - english_word_count
    english_word_percentage = (english_word_count / len(words)) * 100
    non_english_word_percentage = (non_english_word_count / len(words)) * 100

    if english_word_percentage >= wordPercentage and non_english_word_percentage <= (100 - wordPercentage):
        english_letters_percentage = (sum(1 for char in msg if char in LETTER_AND_SPACE) / len(msg)) * 100
        if english_letters_percentage >= letterPercentage:
            return True

    return False


# Gal's Method
def isEnglish_v2(msg, wordPercentage=20, letterPercentage=80):
    wordsMatch = getEnglishCount(msg) * 100 >= wordPercentage
    numLetters = len(removeNonLetter(msg))
    messageLettersPercentage = float(numLetters) / len(msg) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch


# Example usage:
message = "This isis very nice367376373763673733495*$*#$&*$%(^(##%&(^"
if isEnglish(message):
    print("The message is likely in English.")
else:
    print("The message is not in English.")




