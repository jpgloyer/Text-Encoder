import Character_Values


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
    #Converts message string to encrypted_message list of characters
    for i in message:
        encrypted_message.append(i)
    print(password_values)
    for i in password_values:
        if i == 0:
            #alter every character in message
            for j in range(len(message)):
                encrypted_message[j] = Character_Values.char_input_output(encrypted_message[j], key, Character_Reference_List)
        else:
            for j in range(len(message)):
                print(i)
                if j % i == 0:
                    encrypted_message[j] = Character_Values.char_input_output(encrypted_message[j], key, Character_Reference_List)
    return encrypted_message
                    
                    
def decrypt(encrypted_message, password_values, key, Character_Reference_List):
    decrypted_message = []
    password_values.reverse()
    for i in encrypted_message:
        decrypted_message.append(i)

    for i in password_values:
        if i == 0:
            for j in range(len(encrypted_message)):
                decrypted_message[j] = Character_Values.char_input_output(decrypted_message[j], -key, Character_Reference_List)
        else:
            for j in range(len(encrypted_message)):
                if j % i == 0:
                    decrypted_message[j] = Character_Values.char_input_output(decrypted_message[j], -key, Character_Reference_List)
    return decrypted_message

    
    

def main():
    Character_Reference_List = Character_Values.get_chars()
    print(encrypt("Pierce is cool", get_vals_from_password("Pierce"), 1, Character_Reference_List))
    #print(get_vals_from_password("Pierce"))
    print(decrypt('5tpCoq tF ozAw', get_vals_from_password("Pierce"), 1, Character_Reference_List))

if __name__ == "__main__":
    main()