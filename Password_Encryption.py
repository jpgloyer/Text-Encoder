import Character_Values
from Main import message_list_generator


def get_vals_from_password(Password, max_key):
    password_vals = []
    Letter_Nums = ''
    key = 0
    for i in range(len(Password)):   
        Letter_Nums = str(ord(Password[i]))
        for j in Letter_Nums:  
            password_vals.append(int(j))

    #Key creation
    #Code here doesn't really matter as long as the key is never allowed to be greater than the max_key. Everything else will produce the 
    #same result when used for encryption and decryption
    for i in password_vals:
        #print(password_vals[-1])
        if password_vals[0] != 0 and password_vals[-1] != 0:
            if i % password_vals[0] < 2 and i % password_vals[-1] < 2:
                key += i
        #key += i
        if key > max_key:
            key = 0
    #print(key)

    return password_vals, key

def encrypt(message, password_values, key, Character_Reference_List):
    encrypted_message = []
    
    
    #Converts message string to encrypted_message list of characters
    for i in message:
        encrypted_message.append(i)
    #print(password_values)
    for k in range(1000+key):
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
                        #print(key)
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

    for k in range(1000+key):
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

    operation_choice = ''
    while operation_choice != 'encryption' and operation_choice != 'decryption' and operation_choice != 'Encryption' and operation_choice != 'Decryption' and operation_choice != 'E' and operation_choice != 'D' and operation_choice != 'e' and operation_choice != 'd':
        operation_choice = input("Encryption or decryption:")

    print()

    if operation_choice == 'Encryption' or operation_choice == 'encryption' or operation_choice == 'E' or operation_choice == 'e':
        Password_Vals, key = get_vals_from_password(input("Password(Used as encryption key, remember for decryption):"), int(len(Character_Reference_List)/2-1))
        encrypted_message = encrypt(message_list_generator("input.txt"), Password_Vals, key, Character_Reference_List)
        with open((input("Enter output file name(no file extension):")+'.txt'), 'w') as f:
            for i in encrypted_message:
                f.write(i)

    elif operation_choice == 'Decryption' or operation_choice == 'decryption' or operation_choice =='D' or operation_choice == 'd':
        Input_Password_Vals, input_key = get_vals_from_password(input("Password:"), int(len(Character_Reference_List)/2-1))
        decrypted_message = decrypt(message_list_generator(input("Encrypted file name/path:")), Input_Password_Vals, input_key, Character_Reference_List)
        with open('Password_Encryption_Output.txt', 'w') as f:
            for i in decrypted_message:
                f.write(i)

    print()
    # for i in decrypted_message:
    #     print(i, end='')
    print()
    print()

if __name__ == "__main__":
    main()
