def encrypt(message, key):
    binary_list = []
    for i in message:
        for j in range(0,7):
            binary_list.append(format(ord(i), '08b')[j])
    print(binary_list)
    for i in range(len(binary_list)):
        if i % 2 == 0:
            if binary_list[i] == '0':
                binary_list[i] = '1'
            elif binary_list[i] == '1':
                binary_list[i] = '0'
    
    print(binary_list)
    return binary_list

def decrypt(message, key):
    decrypted_message = ''
    for i in range(len(message)):
        if i % 2 == 0:
            if message[i] == '0':
                message[i] = '1'
            elif message[i] == '1':
                message[i] = '0'
    print(message)

    decrypted_message = binary_to_string(message)
    return decrypted_message


    # for i in range(0,len(message),7):
    #     for j in range(0,7):
    #         character = character + message[i+j]
    #     decrypted_message = decrypted_message + chr(binary_to_decimal(character))
    # print(message)
    # print(decrypted_message)
    # return decrypted_message

def binary_to_decimal(binary):
    string = int(binary,2)
    print("binary to string")
    print(string)
    return string

def binary_to_string(binary):
    bin_data = ''
    for i in range(len(binary)):
        bin_data = bin_data + binary[i]
    
    str_data =' '
    
    for i in range(0, len(bin_data), 7):
        
        temp_data = bin_data[i:i + 7]
        
        decimal_data = binary_to_decimal(temp_data)
        
        str_data = str_data + chr(decimal_data)
    return str_data



    # return_string = ''
    # temp_character = ''
    # for i in range(0,len(binary),7):
    #     temp_character = ''
    #     for j in range(0,7):
    #         temp_character = str(temp_character) + str(binary[i+j])
    #     temp_character = binary_to_decimal(temp_character)
    #     return_string = return_string + chr(temp_character)
    # return return_string

#print(
#encrypt('Pierce', 0)
#print(
print(decrypt(encrypt('Pierce', 0),0))