import pprint


def createWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])

    return '.'.join(wordPattern)


def main():
    all_patterns = {}
    # לשנות אם צריך
    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        pattern = createWordPattern(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)

    fo = open('allWordPatternDict.py', 'w')
    fo.write('all_patterns= ')
    fo.write(pprint.pformat(all_patterns))
    fo.close()

