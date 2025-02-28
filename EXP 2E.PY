#Exp 2 E

choice = input("Welcome!! press 1 to continue or 0 to exit")
while choice!= 0:
    # i) accept two strings

    menu = int(input("1) enter strings\n2) common letters(set intersection)\n3) different letters (set difference)\n4) set union 5) symmetric difference"))

    if(menu ==1):
        print("enter two strings")
        string1 = input("string 1: ")
        string2 = input("string 2: ")

    # ii) display common letters in the two strings
    elif(menu == 2):
        print("\nii) common\n")

        common = []
        for i in string1:
            for j in string2:
                if i==j:
                    common.append(i)

        print(set(common))

        #OR

        intersection = set(string1) & set(string2)
        print(intersection)

    # iii) difference

    elif(menu==3):
        print("\niii) difference\n")
        different = []

        for i in string1:
            if i not in string2:
                different.append(i)

        print(set(different))

        difference = set(string1) - set(string2)
        print(difference)

    # iv) union
    elif(menu==4):
        union = []

        print("\niv) this is union\n")

        for i in string1:
            union.append(i)

        for i in string2:
            union.append(i)

        print(set(union))

    #v) symmetric difference
    elif(menu==5):
        print("\nv) symmetric difference\n")

        print(set(union) - intersection)
    
    else:
        print("please enter valid choice")
    
    choice = input("\npress 1 to continue or 0 to exit\n")







    
