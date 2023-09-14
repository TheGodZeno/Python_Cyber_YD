import itertools
import string


def generate_keys_with_missing_letters(pattern):
    missing_letters = []
    placeholders = []
    for i, c in enumerate(pattern):
        if c not in string.ascii_uppercase:
            placeholders.append(i)

    for c in string.ascii_uppercase:
        if c not in pattern:
            missing_letters.append(c)

    missing_permutations = itertools.permutations(missing_letters)

    keys = []

    for perm in missing_permutations:
        key = list(pattern)
        for i, letter in zip(placeholders, perm):
            key[i] = letter
        keys.append(''.join(key))

    return keys



def main():
  generate_keys_with_missing_letters('PGKATWYLZ?VDUNIR?XHQM?SFC?')


if '__main__' == __name__:
    main()
