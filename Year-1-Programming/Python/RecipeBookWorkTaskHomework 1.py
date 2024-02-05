Recipe_Name = input("Enter the name of recipe ") #Sets up storage locations and initialises variables
Number_People_Recipe_Serves = int(input("Enter the number of people the recipe serves "))
Ingredient_Names = []
Ingredient_Quantitys = []
Ingredient_Units = []
Ingredient_Add = input("Type 'Y' if entering a new ingredient else type 'N' ")
Loop_User_Interface = "Y"

while Ingredient_Add == "Y":#Stores the spesification of each ingredient in the correct list
    Ingredient_Name = input("Enter the ingredient name ")
    Ingredient_Quantity = float("Enter the quantity of ingredients (DO NOT INCLUED UNITS)")
    Ingredient_Unit = input("Enter the unit used ")
    Ingredient_Names.append(Ingredient_Name)
    Ingredient_Quantitys.append(Ingredient_Quantity)
    Ingredient_Units.append(Ingredient_Unit)
    Ingrediant_Add = input("Type 'Y' if you need to add anougher ingredient else type 'N' ")

while Loop_User_Interface == "Y":#Supplys user with correct measurments of ingredients (asks for the number of people being served)
    Number_People_Recipe_Must_Serve = int(input("Enter the number of people the recipe must serve "))
    Ingredient_Number = len(Ingredient_Quantitys)
    print(Recipe_Name)
    for Ingredient_Counter in range (Ingredient_Number):#Calculates and outputs the correct measurment of each ingredient
        One_Serving = Ingredient_Quantitys[Ingredient_Counter] / Number_People_Recipe_Serves
        Total = One_Serving * Number_People_Recipe_Must_Serve
        print(Ingredient_Names[Ingredient_Counter]," ",Total,Ingredient_Units[Ingredient_Counter])