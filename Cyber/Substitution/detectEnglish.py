import string
UPPERLETTER = string.ascii_uppercase
LETTER_AND_SPACE = string.ascii_uppercase + string.ascii_lowercase + ' \t\n'


def loadDictionary():
    dictFile = open('DetectingEnglish/dictionary.txt')
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

def isEnglish(msg, wordPercentage=20, letterPercentage=80):
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




