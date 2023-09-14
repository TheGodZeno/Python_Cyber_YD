import string

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = string.ascii_uppercase


def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                   'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                   'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def getItemAtIndexZero(item):
    return item[0]


def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letter_to_frequency = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    frequency_to_letter = {}
    for letter in LETTERS:
        if letter_to_frequency[letter] not in frequency_to_letter:
            frequency_to_letter[letter_to_frequency[letter]] = [letter]
        else:
            frequency_to_letter[letter_to_frequency[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in frequency_to_letter:
        frequency_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        frequency_to_letter[freq] = ''.join(frequency_to_letter[freq])

    # fourth, convert the frequency_to_letter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(frequency_to_letter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def englishFreqMatchScore(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    frequency_order = getFrequencyOrder(message)

    match_score = 0

    for common_letter in ETAOIN[:6]:
        if common_letter in frequency_order[:6]:
            match_score += 1

    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in frequency_order[-6:]:
            match_score += 1

    return match_score


print(englishFreqMatchScore('This is a secret message'))
