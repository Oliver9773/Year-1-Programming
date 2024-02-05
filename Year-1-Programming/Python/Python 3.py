#User Name Creator
Second_Name = str(input("Enter your second name ")) # Asighns the user input to the variable Second_Name
Second_Name_3 = Second_Name[0]+Second_Name[1]+Second_Name[2] # Asighns the first 3 characters of the contents of the variable Second_Name to Second_Name_3
First_Name = str(input("Enter your first name ")) #Asighns the user input to the contents of the variable Second_Name
First_Name_Initial = First_Name[0] # Asighns the first character of the variable First_Name to the variable First_Name_Initial
Second_Name_Length = len(Second_Name)#Asighns the number of characters stored within the variable Second_Name to the variable Second_Name_Length
Second_Name_Length = str(Second_Name_Length)#Asighns the contents of the variable Second_Name_Length to the string data type from the integer data type
User_Name = Second_Name_3+First_Name_Initial+Second_Name_Length # Asighns the contents of the variables Second_Name_3 First_Name_Initial Second_Name_Length combined to the variable User_Name
print("Your user name is ",User_Name)#Outputs the contents of the variable User_Name