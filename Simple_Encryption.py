import Main
import Character_Values
from contextlib import redirect_stdout

key = input("Enter encryption key:")

encrypted_char_list = Main.encryption(Main.message_list_generator('file.txt'), int(key), Character_Values.get_chars())

with open ("encrypted.txt", 'w') as f:
    with redirect_stdout(f):
        for i in range(len(encrypted_char_list)):
            print(encrypted_char_list[i], end='')