Teams = ["Ferrari","Williams","Haas","Racing Point"]
print("Current bonus payment ",Teams[0])
print(Teams[0]," rival is ",Teams[1])
Teams[3] = "Aston Martin"
Teams.append("Team5")
Teams.append("Team6")
print(Teams)
Replace_Member = int(input("Enter the team number you want to replace "))
New_Team = str(input("Enter the team you want to replace the team with "))
Teams[Replace_Member] = New_Team