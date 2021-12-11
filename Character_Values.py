def get_chars():
    #To be used once at the beginning of every run of the program
    #Simply generates a list of standard characters (numbers, lower and capital case letters)
    #Returns the completed list, doubled
    Character_List1 = [chr(i) for i in range(65,91)]
    Character_List2 = [chr(i) for i in range(97,123)]
    Character_List3 = [chr(i) for i in range(48,58)]
    Full_Character_List = []
    for i in range(len(Character_List3)):
        Full_Character_List.append(Character_List3[i])
    for i in range(len(Character_List2)):
        Full_Character_List.append(Character_List2[i])
    for i in range(len(Character_List1)):
        Full_Character_List.append(Character_List1[i])

    for i in range(len(Full_Character_List)):
        Full_Character_List.append(Full_Character_List[i])


    # for i in range(len(Int_Value_Of_Character)):
    #     print(Full_Character_List[i],end='')
    return Full_Character_List


def char_input_output_encrypting(input_char, encryption_value, Character_List):
    index = 0
    i = 0
    while i != -1:
        if input_char == Character_List[i]:
            index = i
            i = -1
        else:
            i+=1

        if i > 123:
            i = -1
            return input_char

    return Character_List[index+encryption_value]