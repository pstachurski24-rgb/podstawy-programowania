plain_text = "The early bird catches the worm"
encrypted_text = ""

for char in plain_text:
    char_code = ord(char)
    new_code = char_code + 1
    encrypted_char = chr(new_code)
    encrypted_text += encrypted_char

print("Original:", plain_text)
print("Encrypted:", encrypted_text)