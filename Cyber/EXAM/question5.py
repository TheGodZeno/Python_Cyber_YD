import random


def message_to_binary(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message


def complement_and_balance(binary_message):
    num_ones = binary_message.count('1')
    num_zeros = len(binary_message) - num_ones
    complement = '0' * (num_zeros - num_ones) + '1' * (num_ones - num_zeros)
    print(f'binmsg + c: {binary_message + complement}')
    return binary_message + complement


def pseudo_random_sequence(n):
    return random.sample(range(1, n + 1), n)


def mix_bits(binary_message):
    n = len(binary_message)
    random_indices = pseudo_random_sequence(n)
    mixed_message = ''.join(binary_message[random_indices[i] - 1] for i in range(n))
    return mixed_message


def encrypt_message(message):
    binary_message = message_to_binary(message)
    print(f'bin msg: {binary_message}')
    balanced_binary = complement_and_balance(binary_message)
    mixed_message = mix_bits(balanced_binary)
    return mixed_message


def decrypt_message(encrypted_message, key_seed):
    random.seed(key_seed)

    n = len(encrypted_message)
    random_indices = pseudo_random_sequence(n)

    array_values = list(range(1, n + 1))
    shuffled_array = [array_values[random_indices[i] - 1] for i in range(n)]

    original_message = ''.join(encrypted_message[shuffled_array[i] - 1] for i in range(n))

    return original_message


# Example usage:
message = "hello"
key_seed = 42

encrypted_message = encrypt_message(message)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, key_seed)
print(f"Decrypted Message: {decrypted_message}")
