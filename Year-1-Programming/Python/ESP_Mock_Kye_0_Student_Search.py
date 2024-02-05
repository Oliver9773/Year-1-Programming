Username_Correct = "Mr Leeman" #Sets up Correct user login data
Password_Correct = "Password1."

ID_Number = [] # the lists of all the data needed by Mr Leeman
Surname = []
Forname = []
Date_Of_Birth = []
Home_Adress = []
Home_Phone_Number = []
Gender = []
Tutor_Group = []

Loop_Password = "Y" # Sets the condition for log in screen to loop

def Student_Search(): # Searches for student data in the database.
    Search_Student = "Y":
    while Search_Student == "Y":
        Search_Student_ID_Number = int(input("Enter the student ID number: "))
        Student_Place_Value = len(ID_Number)
        for Loop in range(Student_Place_Value):
            if ID_Number(Loop) == Search_Student_ID_Number:
                print("Forname: ", Forname(Loop))
                print("Surname: ", Surname(Loop))
                print("Date of birth: ", Date_Of_Birth(Loop))
                print("Home adress: ", Home_Adress(Loop))
                print("Home phone number: ", Home_Phone_Number(Loop))
                print("Gender: ", Gender(Loop))
                print("Tutor group", Tutor_Group(Loop))
                Search_Student = ("Enter 'Y' to search another student: ")

def Add_Student():#Adds new students
    Add_New_Student = "Y"
    while Add_New_Student == "Y":
        New_Student_ID_Number = int(input("Enter the ID number of the new student: "))
        New_Student_Forename = input("Enter the forename of the new student: ")
        New_Student_Surname = input("Enter the surname of the new student: ")
        New_Student_Date_Of_Birth = input("Enter the date of birth of the new student: ")
        New_Student_Home_Adress = input("Enter the home adress of the new student: ")
        New_Student_Home_Phone_Number = int(input("Enter the home phone number of the new student: "))
        New_Student_Gender = input("Enter the gender of the new student: ")
        New_student_Tutor_Group = input("Enter the tutor group of the new student: ")
        New_Student_Add_Verify = input("Type 'Y' to conferm the adition of ", New_Student_Forename, " ", New_Student_Surname, " to the database: ")
        if New_Student_Add_Verify == 'Y':
            ID_Number.append(New_Student_ID_Number)
            Forname.append(New_Student_Forename)
            Surname.append(New_Student_Surname)
            Date_Of_Birth.append(New_Student_Date_Of_Birth)
            Home_Adress.append(New_Student_Home_Adress)
            Home_Phone_Number.append(New_Student_Home_Phone_Number)
            Gender.append(New_Student_Gender)
            Tutor_Group.append(New_student_Tutor_Group)
            Add_New_Student = input("Enter 'Y' to add a new student")
        else:
            Add_New_Student = input("Enter 'Y' to add a new student")

def Menu(): # Loads up the menu screen
    Login = "Y"
    while Login == "Y":
        New_Student = input("Enter 'Y' to add a new student")
        if New_Student == "Y":
            Add_Student()
        Search_For_Student = input("Type 'Y' to search for a student by ID number: ")
        if Search_For_Student == "Y":
            Student_Search()

while Loop_Password == "Y": # Starts login screen loop
    Username_Entered = input("Enter your username: ")
    Password_Entered = input("Enter your password: ")
    if Username_Entered == Username_Correct and Password_Entered == Password_Correct:
        Menu()
        print(Username_Entered, " You have sucessfully logged out")
    else:
        print("Your Username or password is not correct, please try again")