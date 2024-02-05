Username_Correct = "Mr Leeman" #Sets up Correct user login data
Password_Correct = "Password1."

ID_Number = [0,] # the lists of all the data needed by Mr Leeman
Surname = ["Bobby"]
Forname = ["Bob"]
Date_Of_Birth = ["01/01/1001"]
Home_Adress = ["NA"]
Home_Phone_Number = ["+876477897675"]
Gender = ["Male"]
Tutor_Group = ["Mr Leeman"]
Grade = ["A*"]
Behavior = ["NA"]

Loop_Password = "Y" # Sets the condition for log in screen to loop

while Loop_Password == "Y": # Starts login screen loop
    Username_Entered = input("Enter your username: ")
    Password_Entered = input("Enter your password: ")

    if Username_Entered == Username_Correct and Password_Entered == Password_Correct:
        Login = "Y"#Loads up menu
        while Login == "Y":
            
            New_Student = input("Enter 'Y' to add a new student")
            if New_Student == "Y":
                Add_New_Student = "Y"
                while Add_New_Student == "Y":#Adds new students
                    New_Student_ID_Number = int(input("Enter the ID number of the new student: "))
                    New_Student_Forename = input("Enter the forename of the new student: ")
                    New_Student_Surname = input("Enter the surname of the new student: ")
                    New_Student_Date_Of_Birth = input("Enter the date of birth of the new student: ")
                    New_Student_Home_Adress = input("Enter the home adress of the new student: ")
                    New_Student_Home_Phone_Number = input("Enter the home phone number of the new student: ")
                    New_Student_Gender = input("Enter the gender of the new student: ")
                    New_student_Tutor_Group = input("Enter the tutor group of the new student: ")
                    New_Student_Grade = input("Enter the new student grade: ")
                    New_Student_Behavior = input("Enter the new student behavior comments: ")
                    New_Student_Add_Verify = input("Type 'Y' to conferm the adition to the database: ")
                    if New_Student_Add_Verify == 'Y':
                        ID_Number.append(New_Student_ID_Number)
                        Forname.append(New_Student_Forename)
                        Surname.append(New_Student_Surname)
                        Date_Of_Birth.append(New_Student_Date_Of_Birth)
                        Home_Adress.append(New_Student_Home_Adress)
                        Home_Phone_Number.append(New_Student_Home_Phone_Number)
                        Gender.append(New_Student_Gender)
                        Tutor_Group.append(New_student_Tutor_Group)
                        Grade.append(New_Student_Grade)
                        Behavior.append(New_Student_Behavior)
                        Add_New_Student = input("Enter 'Y' to add a new student")
                    else:
                        Add_New_Student = input("Enter 'Y' to add a new student")


            Search_For_Student = input("Type 'Y' to search for a student by ID number: ")#Searches for student
            if Search_For_Student == "Y":
                Search_Student = "Y"
                while Search_Student == "Y":
                    Search_Student_ID_Number = int(input("Enter the student ID number: "))
                    Student_Place_Value = len(ID_Number)
                    for Loop in range(Student_Place_Value):
                        if ID_Number[Loop] == Search_Student_ID_Number:
                            print("Forname: ", Forname[Loop])
                            print("Surname: ", Surname[Loop])
                            print("Date of birth: ", Date_Of_Birth[Loop])
                            print("Home adress: ", Home_Adress[Loop])
                            print("Home phone number: ", Home_Phone_Number[Loop])
                            print("Gender: ", Gender[Loop])
                            print("Tutor group: ", Tutor_Group[Loop])
                            print("Grade: ", Grade[Loop])
                            print("Behavior: ", Behavior[Loop])
                            Search_Student = ("Enter 'Y' to search another student: ")
                        else:
                            print("Student not found")
                            Search_Student = ("Enter 'Y' to search another student: ")

            Make_Report = input("Enter 'Y' to make a report on a student: ")#Makes report
            if Make_Report == "Y":
                Report = "Y"
                while Report == "Y":
                    Report_Student_ID_Number = int(input("Enter the student ID number: "))
                    Report_Student_Place_Value = len(ID_Number)
                    for Loop_1 in range(Report_Student_Place_Value):
                        if ID_Number[Loop_1] == Report_Student_ID_Number:
                            print("Student Report")
                            print("Student Forname: ", Forname[Loop_1])
                            print("Student Surname: ", Surname[Loop_1])
                            print("Student Tutor: ", Tutor_Group[Loop_1])
                            print("Student Grade: ", Grade[Loop_1])
                            print("Student Behavior comments: ", Behavior[Loop_1])
                            Report = ("Enter 'Y' to search another student: ")
                        else:
                            print("Student not found")
                            Report = ("Enter 'Y' to search another student: ")

            Login = input("If you would like to remain logged in type 'Y'")#Asks if you want to remain logged in
        print(Username_Entered, " You have sucessfully logged out")#Log out message
    else:
        print("Your Username or password is not correct, please try again")#Says if username and password is wrong