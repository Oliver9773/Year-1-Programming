Password_True = 0 # Variable inisilisation
Password_Strength = 0
Upper = 0
Lower = 0
Number = 0

while Password_True == 0:#While loop to make sure the password is at corect length
    Password = str(input("Enter the password"))
    Password_Length = len(Password)
    if Password_Length <= 12:
        if Password_Length >= 6:
            print("Password is accepted")
            Password_True = 1#stops the condition of the while loop as length of password is correct

            for Password_Capital in range (0,Password_Length,1):#    Password capital letter check
                Character_Check = Password[Password_Capital]
                if is(Character_Check).upper == True:
                    Upper = Upper + 1
                if Upper > 0:
                    Password_Strength = Password_Strength + 1
            
            for Password_Capital in range (0,Password_Length,1):#    Password lower letter check
                Character_Check = Password[Password_Capital]
                if is(Character_Check).upper == True:
                    Upper = Upper + 1
                if Upper > 0:
                    Password_Strength = Password_Strength + 1
            
            for Password_Number in range (0,Password_Length,1):#    Password number check
                Character_Check = Password[Password_Number]
                if is(Character_Check).integer == True:
                    Number = Number + 1
                if Upper > 0:
                    Password_Strength = Password_Strength + 1
        else:
            print("Password must contain at least 6 characters")#Output source of password error
    else:
        print("Password must contain 12 or less characters")#Outputs source of password error