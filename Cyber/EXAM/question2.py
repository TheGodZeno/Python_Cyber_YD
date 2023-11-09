def string_to_binary(text):
    return " ".join(format(ord(char), '08b') for char in text)


def main():
    input_string = "I Learn Computer Science"
    binary_result = string_to_binary(input_string)
    print(binary_result)


if __name__ == "__main__":
    main()
