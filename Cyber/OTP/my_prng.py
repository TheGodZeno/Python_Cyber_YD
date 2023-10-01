import sys

SEED_SIZE = 16
MODULUS = 36389
GENERATOR = 1500
function_L = lambda x: x**2 - 2*x + 223


def function_H(first_half, second_half):
    mod_exp = bin(pow(GENERATOR, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(min(len(second_half), len(first_half))):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i])))%2

    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed):
    binary_string = initial_seed
    result = ''
    for i in range(function_L(SEED_SIZE)):
        first_half = binary_string[:int(len(binary_string)/2)]
        second_half = binary_string[int(len(binary_string)/2):]
        binary_string = function_H(first_half, second_half)
        result += binary_string[-1]
        binary_string = binary_string[:-1]

    global GENERATOR
    GENERATOR = GENERATOR + 1
    return result

def create_uniqe_pad(seed):
    return function_G(seed)  # sys.argv[1]

def main():
    pad = create_uniqe_pad()
    print('SIZE:', SEED_SIZE, '->', function_L(SEED_SIZE))
    print(pad)
    d = {}


    for i in range(10000):
        pad = create_uniqe_pad()
        if pad not in d.keys():
            d[pad] = 1
        else:
            d[pad] += 1


    if sorted(d.values(), reverse=True)[0]>1:
        print('NOT GOOD!!')
    else:
        print('SABABA :)')


if __name__ == '__main__':
    main()
