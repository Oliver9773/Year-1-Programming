#Following instructions on worksheet
print("What is your name?")#Outputs the message "What is your name?"
First_Name = input()#Asighns the user input to the variable First_Name
print("Hello,",First_Name)#Outputs "Hello" as well as the contents of the variable First_Name
Second_Name = str(input("Enter your second name"))#Asighns the user input to the variable Second_Name
print("your second name is, ",Second_Name)#Outputs to the user the contents of the variable Second_Name to the user
print("Hello",First_Name,Second_Name)# Outputs "Hello" followed by the contents of the variables First_Name and, Second_Name
print("Your initials are:",First_Name[0],Second_Name[0]) # Outputs initials of the contents of the variables First_BName and Second_Name
Fullname = First_Name + Second_Name #Applys concatination to the variables First_Name and Second_Name to the variable FirstName
print(Fullname)#Outputs the contents of the variable Full_Name
print(Second_Name.upper(),First_Name.upper()) # Outputs both the contents of the variables Second_Name and First_Name in uppercase
Letter_Number_Second = len(Second_Name)# Asighns the number of characters in Second_Name to the variable Letter_Number_Second
print("They are ",Letter_Number_Second," letters in your second name") #Outputs the contents of the variable Letter_Number_Second