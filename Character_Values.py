Character_List1 = [chr(i) for i in range(65,91)]
Character_List2 = [chr(i) for i in range(97,123)]
Character_List3 = [chr(i) for i in range(48,58)]
Int_Value_Of_Character = [i for i in range(62)]
Full_Character_List = []
for i in range(len(Character_List3)):
    Full_Character_List.append(Character_List3[i])
for i in range(len(Character_List2)):
    Full_Character_List.append(Character_List2[i])
for i in range(len(Character_List1)):
    Full_Character_List.append(Character_List1[i])


for i in range(len(Int_Value_Of_Character)):
    print(Full_Character_List[i],end='')
