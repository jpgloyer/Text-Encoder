import Main
import Character_Values
from contextlib import redirect_stdout


decrypted_char_list = Main.decryption(Main.message_list_generator('encrypted.txt'), 3, Character_Values.get_chars())

with open ("output.txt", 'w') as f:
    with redirect_stdout(f):
        for i in range(len(decrypted_char_list)):
            print(decrypted_char_list[i], end='')