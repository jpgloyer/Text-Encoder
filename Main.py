import Character_Values

def message_list_generator():
    character_list = []
    file = open('file.txt', 'r')
    end_of_file = False

    while not end_of_file: 
        # read by character
        character = file.read(1)         
        if not character:
            end_of_file = True
            

        #print(character)
        if character:
            character_list.append(chr(ord(character)))

    file.close()

    #print(character_list)
    #print()
    #print(encrypted_character_list)
    return character_list

def encryption(Message_Character_List, key, Character_List):
    if key < 0:
        key = -key
    if key > 61:
        key = key % 61
    Encrypted_Character_List = []
    for i in range(len(Message_Character_List)):
        if Message_Character_List[i]:
            print(Character_Values.char_input_output_encrypting(Message_Character_List[i], key, Character_List), i, Message_Character_List[i])
            Encrypted_Character_List.append(Character_Values.char_input_output_encrypting(Message_Character_List[i], key, Character_List))
            key += 1
        if key == 62:
            key = 0
    return Encrypted_Character_List


def decryption(Encrypted_Character_List, key, Character_List):
    if key > 0:
        key = -key
    if key < -61:
        key = key % 61
    Decrypted_Character_List = []
    for i in range(len(Encrypted_Character_List)):
        if Encrypted_Character_List[i]:
            Decrypted_Character_List.append(Character_Values.char_input_output_encrypting(Encrypted_Character_List[i], key, Character_List))
            key -= 1
        if key == -62:
            key = 0
    return Decrypted_Character_List
        


if __name__ == "__main__":
    message = message_list_generator()
    Character_List = Character_Values.get_chars()
    print(message)
    Encrypted_Character_List = encryption(message, 3, Character_List)
    #for i in range(len(Encrypted_Character_List)):
    print(Encrypted_Character_List)
    Decrypted_Character_List = decryption(Encrypted_Character_List, 3, Character_List)
    print(Decrypted_Character_List)
