def character_list_generator():
    character_list = []
    encrypted_character_list = []
    increment_val = 0
    file = open('file.txt', 'r')
 
    end_of_file = False
    while not end_of_file:
     
        # read by character
        character = file.read(1)         
        if not character:
            end_of_file = True
            
        character_list.append(character)
        print(character)
        if character:
            new_char = chr(ord(character)+increment_val)
            encrypted_character_list.append(chr(ord(character)+increment_val))
            increment_val += 1
            
    
    file.close()

    print(character_list)
    print()
    print(encrypted_character_list)
    return encrypted_character_list

def decryption(character_list, key):
    print('nah')


if __name__ == "__main__":
    message = character_list_generator()
    decryption(message, 0)