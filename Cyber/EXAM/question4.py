def middle_square(seed, k, c, a):
    sequence = [seed]
    m = 10 ** (2 * k)

    for _ in range(9):
        x = sequence[-1]
        x = (a * x + c) % m
        sequence.append(x)

    return sequence


if __name__ == "__main__":
    k = 0

    for _ in range(10):
        result = middle_square(1234, k, 10, 7)
        print(k+1, result, end='\n')
        k += 1
