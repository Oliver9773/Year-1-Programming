Total_Wage = 0
Villains = ["The Joker","Magneto","Red Mist","Doc Ock"]
Wage = [21,17,3,5]
for counter in range(4):
    print(Villains[counter])
for counter in range(4):
    print(Villains[counter],": £",Wage[counter]," million")
for loop in range(4):
    Total_Wage = Total_Wage + Wage[loop]
print("The total wage for the League is £",Total_Wage)