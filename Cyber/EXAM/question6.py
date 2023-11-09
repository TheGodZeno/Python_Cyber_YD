# hex_key = "6c73d5240a948c86981bc294814d"
#
# message1 = "attack at dawn"
# message2 = "attack at dusk"
#
# key_binary = bin(int(hex_key, 16))[2:]
#
# def text_to_binary(text):
#     binary_result = "".join(format(ord(char), '08b') for char in text)
#     return binary_result
#
# message1_binary = text_to_binary(message1)
# message2_binary = text_to_binary(message2)
#
# result_binary = "".join(str(int(a) ^ int(b) ^ int(c)) for a, b, c in zip(key_binary, message1_binary, message2_binary))
#
# result_hex = hex(int(result_binary, 2))[2:]
# print("Hexadecimal Result (XOR of messages with key):", result_hex)
#
# # Print the binary result
# print("Binary Result (XOR of messages with key):", result_binary)

if __name__ == '__main__':
    msg1 = 'attack at dawn'
    msg2 = 'attack at dusk'
    cipher1 = 0x6c73d5240a948c86981bc294814d
    cipher2 = []
    for msg1, msg2, cipher1 in zip(msg1, msg2, cipher1.to_bytes(len(msg1), 'big')):
        cipher2.append(ord(msg1) ^ cipher1 ^ ord(msg2))

    print(cipher2)
    result = 0
    for b in cipher2:
        result = result*256+b
    print(result)

    print(hex(result))

