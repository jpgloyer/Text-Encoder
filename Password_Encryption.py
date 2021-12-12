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
    #Character_Reference_List_Length = len(Character_Reference_List)/2
    #print(Character_Reference_List_Length)
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
    stop = False
    while stop == False:
        file_choice = input("Which file would you like to encrypt?")
        if file_choice == '1' or file_choice == 'test_information1' or file_choice == 'test_information1.txt':
            file_choice = 'test_information1.txt'
            stop = True
        elif file_choice == '2' or file_choice == 'test_information2' or file_choice == 'test_information2.txt':
            file_choice = 'test_information2.txt'
            stop = True
        elif file_choice == '3' or file_choice == 'test_information3' or file_choice == 'test_information3.txt':
            file_choice = 'test_information3.txt'
            stop = True

    print()
    Password_Vals, key = get_vals_from_password("Guardian927", int(len(Character_Reference_List)/2-1))
    encrypted_message = encrypt(message_list_generator(file_choice), Password_Vals, key, Character_Reference_List)

    
    Input_Password_Vals, input_key = get_vals_from_password(input("Password:"), int(len(Character_Reference_List)/2-1))
    decrypted_message = decrypt(encrypted_message, Input_Password_Vals, input_key, Character_Reference_List)


    print()
    for i in decrypted_message:
        print(i, end='')
    print()
    print()

if __name__ == "__main__":
    main()
    #make key to be variation of sum of ascii values of chars in password