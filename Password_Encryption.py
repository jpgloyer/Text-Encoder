import Character_Values
from Main import message_list_generator


def get_vals_from_password(Password):
    password_vals = []
    Letter_Nums = ''
    for i in range(len(Password)):   
        Letter_Nums = str(ord(Password[i]))
        for i in Letter_Nums:  
            password_vals.append(int(i))

    return password_vals

def encrypt(message, password_values, key, Character_Reference_List):
    encrypted_message = []
    #Character_Reference_List_Length = len(Character_Reference_List)/2
    #print(Character_Reference_List_Length)
    #Converts message string to encrypted_message list of characters
    for i in message:
        encrypted_message.append(i)
    #print(password_values)
    for k in range(100*key):
        for i in password_values:
            if i == 0:
                #alter every character in message
                for j in range(len(message)):
                    encrypted_message[j] = Character_Values.char_input_output(encrypted_message[j], key, Character_Reference_List)
                    # key += 1
                    # #print(key)
                    # if key == Character_Reference_List_Length:
                    #     key = 0

            else:
                for j in range(len(message)):
                    #print(i)
                    if j % i == 0:
                        encrypted_message[j] = Character_Values.char_input_output(encrypted_message[j], key, Character_Reference_List)
                        # key += 1
                        # #print(key)
                        # if key == Character_Reference_List_Length:
                        #     key = 0
    return encrypted_message
                    
                    
def decrypt(encrypted_message, password_values, key, Character_Reference_List):
    #Character_Reference_List_Length = len(Character_Reference_List)/2
    decrypted_message = []
    password_values.reverse()
    for i in encrypted_message:
        decrypted_message.append(i)

    for k in range(100*key):
        for i in password_values:
            if i == 0:
                for j in range(len(encrypted_message)):
                    decrypted_message[j] = Character_Values.char_input_output(decrypted_message[j], -key, Character_Reference_List)
                    # key += 1
                    # if key == Character_Reference_List_Length:
                    #     key = 0
            else:
                for j in range(len(encrypted_message)):
                    if j % i == 0:
                        decrypted_message[j] = Character_Values.char_input_output(decrypted_message[j], -key, Character_Reference_List)
                        # key += 1
                        # if key == Character_Reference_List_Length:
                        #     key = 0
    return decrypted_message

    
    

def main():
    Character_Reference_List = Character_Values.get_chars()
    #print(encrypt("Pierce is cool", get_vals_from_password("Pierce"), 2, Character_Reference_List))
    #print(get_vals_from_password("Pierce"))
    #print(decrypt('5tpCoq tF ozAw', get_vals_from_password("Pierce"), 1, Character_Reference_List))
    print()
    encrypted_message = encrypt(message_list_generator("input.txt"), get_vals_from_password("Pierce"), 2, Character_Reference_List)
    decrypted_message = decrypt(encrypted_message, get_vals_from_password(input("Password:")), int(input("Key(integer):")), Character_Reference_List)
    print()
    for i in decrypted_message:
        print(i, end='')
    print()
    print()
    #print(decrypt(encrypt(message_list_generator("input.txt"), get_vals_from_password("Pierce"), 2, Character_Reference_List), get_vals_from_password("Pierce"), 2, Character_Reference_List))

if __name__ == "__main__":
    main()