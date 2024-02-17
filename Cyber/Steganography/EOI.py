def hexdump(file, width=16):
    offset = 0
    while True:
        chunk = file.read(width)
        if not chunk:
            break
        hex_line = ' '.join(f'{b:02x}' for b in chunk)
        text_line = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f'{offset:08x}: {hex_line.ljust(width * 3)}  {text_line}')
        offset += len(chunk)


input_file_path = "dogcyber.jpg"
output_file_path = "new_dogcyber.jpg"

message = input("WHAT MESSAGE TO APPEND: ")

with open(input_file_path, "rb") as input_file:
    file = input_file.read()
    message = message + str(len(message)) + "Magic"
    file += message.encode('ascii')

    with open(output_file_path, "wb") as output_file:
        output_file.write(file)

print("File successfully written to:", output_file_path)

with open("new_dogcyber.jpg", "rb") as f:
    hexdump(f)