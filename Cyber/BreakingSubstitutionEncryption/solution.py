import re, copy, pprint, string, AllPossibleKeys, SubstitutionCipher, WordPattern, allWordPatternDict

KEY = ''
LETTERS = string.ascii_uppercase
cleanPattern = re.compile('[^A-Z\s]')


# key: pgkatwylzovdunirbxhqmesfcj

def main():
    encrypted_message = 'Kiath irtxpqta gc hmghqzqmqzny pkkixazny qi p dpxyt kiatgiiv slzkl dznvta p xpnaiu hqxzny iw klpxpkqtxh ix nmugtxh qi p sixa ix rlxpht. Wix tfpurdt, "MBOLHT" kimda gt qlt kiat wix "Rxiktta qi qlt widdiszny kiixaznpqth." Sltn mhzny p kzrltx qlt ixzyznpd znwixupqzin zh vnisn ph rdpznqtfq, pna qlt tnkxcrqta wixu ph kzrltxqtfq. Qlt kzrltxqtfq uthhpyt kinqpznh pdd qlt znwixupqzin iw qlt rdpznqtfq uthhpyt, gmq zh niq zn p wixupq xtpapgdt gc p lmupn ix kiurmqtx szqlimq qlt rxirtx utklpnzhu qi atkxcrq zq.'
    print('Hacking...')
    letter_map = break_substitution_cipher(encrypted_message)

    print('Final letter map is:')
    pprint.pprint(letter_map)
    print()
    print('Original ciphertext:')
    print(encrypted_message)
    print()
    print(decrypt_cipher_with_final_letter_map(encrypted_message, letter_map))


def create_empty_letter_map():
    return {letter: [] for letter in LETTERS}


def add_candidate_letters_to_map(letter_map, cipher_word, candidate):
    letter_map = copy.deepcopy(letter_map)
    for i in range(len(cipher_word)):
        if candidate[i] not in letter_map[cipher_word[i]]:
            letter_map[cipher_word[i]].append(candidate[i])
    return letter_map


def intersect_between_maps(first_letter_map, second_letter_map):
    intersected_mapping = create_empty_letter_map()
    for letter in LETTERS:
        if not first_letter_map[letter]:
            intersected_mapping[letter] = copy.deepcopy(second_letter_map[letter])
        elif not second_letter_map[letter]:
            intersected_mapping[letter] = copy.deepcopy(first_letter_map[letter])
        else:
            intersected_mapping[letter] = [mappedLetter for mappedLetter in first_letter_map[letter] if mappedLetter in second_letter_map[letter]]

    return intersected_mapping


def delete_letters_from_final_map(letter_map):
    letter_map = copy.deepcopy(letter_map)
    loop_again = True
    while loop_again:
        loop_again = False

        final_letters = [letter_map[cipher_letter][0] for cipher_letter in LETTERS if len(letter_map[cipher_letter]) == 1]

        for cipher_letter in LETTERS:
            for letter in final_letters:
                if len(letter_map[cipher_letter]) != 1 and letter in letter_map[cipher_letter]:
                    letter_map[cipher_letter].remove(letter)
                    if len(letter_map[cipher_letter]) == 1:
                        loop_again = True
    return letter_map


def break_substitution_cipher(message):
    intersected_map = create_empty_letter_map()
    cipher_word_list = cleanPattern.sub('', message.upper()).split()
    for cipher_word in cipher_word_list:
        new_letter_map = create_empty_letter_map()

        word_pattern = WordPattern.createWordPattern(cipher_word)
        if word_pattern not in allWordPatternDict.all_patterns:
            continue

        for candidate in allWordPatternDict.all_patterns[word_pattern]:
            new_letter_map = add_candidate_letters_to_map(new_letter_map, cipher_word, candidate)

        intersected_map = intersect_between_maps(intersected_map, new_letter_map)

    return delete_letters_from_final_map(intersected_map)


def decrypt_cipher_with_final_letter_map(cipher_text, letter_map):
    global KEY
    key = ['?'] * len(LETTERS)
    for cipher_letter in LETTERS:
        if len(letter_map[cipher_letter]) == 1:
            key_index = LETTERS.find(letter_map[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            cipher_text = cipher_text.replace(cipher_letter.lower(), '_')
            cipher_text = cipher_text.replace(cipher_letter.upper(), '_')

    key = ''.join(key)
    KEY = copy.deepcopy(key)

    print("The ABC is:", LETTERS)
    print("The key is:", key)
    print()
    print("Decrypted message is:")
    return SubstitutionCipher.decryptMessage(key, cipher_text)


if __name__ == '__main__':
    main()
    print()
    print('A list with possible keys as a solution:')
    keys = AllPossibleKeys.generate_keys_with_missing_letters(KEY)
    for key in enumerate(keys):
        print(key)
