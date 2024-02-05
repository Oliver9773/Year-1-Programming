First_Names = [] # Creates the lists
Second_Names = []
Marks = []
Grades = []
Test_Dates = []
Marker_Names = []
Start = input("Type'Y' to enter students score else type 'N'")
while Start == "Y":#Loops untill all student data entered
    First_Name = input("Enter Student first name")
    Second_Name = input("Enter student second name")
    Mark = input("Enter student mark")
    if Mark < 40:#Calculates the grade from marks
        Grade = "F"
    elif Mark >= 80:
        Grade = "A*"
    elif Mark >= 40 and Mark < 50:
        Grade = "D"
    elif Mark >= 50 and Mark < 60:
        Grade = "C"
    elif Mark >= 60 and Mark < 70:
        Grade = "B"
    elif Mark >= 70  and Mark < 80:
        Grade = "A"
    else:
        Grade = "Disqualified"
        print("The student has cheated")#Outputs that student cheated as condition is not possible
    Test_Date = input("Enter the date of the test")
    Marker_Name = input("Enter the name of the marker")
    First_Names.append(First_Name)#Uploads student data to the list
    Second_Names.append(Second_Name)
    Marks.append(Mark)
    Grades.append(Grade)
    Test_Dates.append(Test_Date)
    Marker_Names.append(Marker_Name)
    Start = input("Type 'Y' to enter another students score else type 'N'")#Allows Loop to continue or not
    

Start_Output = input("Type 'Y' to ouitput student details else type'N'") #Allows list data to output
if Start_Output == "Y":
    Iteration = len(First_Names)
    for Loop in range(Iteration):#Outputs all data in a sutable order
        print(First_Names[Loop])
        print(Second_Names[Loop])
        print(Marks[Loop])
        print(Grades[Loop])
        print(Test_Dates[Loop])
        print(Marker_Names[Loop])