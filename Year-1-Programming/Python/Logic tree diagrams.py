Character_Male = input("If the character is male type'Y' else type 'N")
if Character_Male == "Y":
    Character_Jedi = input("If the character is a Jedi type 'Y' else type 'N'")
    if Character_Jedi == "Y":
        Character_Green_Lightsabre = input("If the character is known to have a green lightsabre type'Y' else type 'N'")
        if Character_Green_Lightsabre == "Y":
            print("Your Character is 'Luke Skywalker'")
        else:
            print("Your character is 'Obi-Wan Kenobi'")
    else:
        Character_Sith_Lord = input("If character is a sith lord type 'Y' else type 'N'")
        if Character_Sith_Lord == "Y":
            print("Your Character is 'Darth Vader'")
        else:
            print("Your character is 'Grand Admiral Thrawn'")
else:
    Character_Droid = input("If character is a droid type 'Y' else type 'N'")
    if Character_Droid == "Y":
        print("Your Character is 'R2D2'")
    else:
        print("Your Character is 'Princess Leia'")