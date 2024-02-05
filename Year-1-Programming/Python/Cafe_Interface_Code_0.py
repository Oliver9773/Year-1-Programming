#Sets the condition for the loop to iterate.
Loop = "Y"

#Initialisation of all necersary variables
Final_Total = 0
Item_1 = 0
Item_2 = 0
Item_3 = 0
Item_4 = 0
Item_5 = 0

#Starts the loop for the menu
while Loop == "Y":
    
    #Outputs all menu options
    print("Press 0 for checkout")
    print("Press 1 to add a Friut Smoothie for £3.00")
    print("Press 2 to add a Muffin for £2.00")
    print("Press 3 to add a French Toast for £5")
    print("Press 4 to add a Coffee for £2.50")
    print("Press 5 to add a Tea for £1.50")
    
    #Allows user to enter the servace they would like
    Item = input("Enter the number for the service you would like: ")
    
    #Checks if Item is equal to 0
    if Item == "0":

        #Outputs amount of each item bought and final total
        print("Fruit Smoothie ordered: ",Item_1)
        print("Muffin ordered: ",Item_2)
        print("French Toast ordered: ",Item_3)
        print("Coffee ordered: ",Item_4)
        print("Tea ordered: ",Item_5)
        print("Total cost: £", Final_Total)

        #Verifys the order is correct
        Final_Order = input("Please enter 'Y' to conferm your order: ")
        if Final_Order == "Y":
            print("Order complete")
            Loop = "N"
        else:
            print("Please continue with your order")
    
    #Checks if Item is equal to 1
    elif Item == "1":
        Final_Total = Final_Total + 3
        Item_1 = Item_1 + 1
        print("One Fruit Smoothie has been added to your order")
    
    #Checks if Item is equal to 2
    elif Item == "2":
        Final_Total = Final_Total + 2
        Item_2 = Item_2 + 1
        print("One Muffin has been added to your order")
    
    #Checks if Item is equal to 3
    elif Item == "3":
        Final_Total = Final_Total + 5
        Item_3 = Item_3 + 1
        print("One French Toast has been added to your order")
    
    #Checks if Item is equal to 4
    elif Item == "4":
        Final_Total = Final_Total + 2.50
        Item_4 = Item_4 + 1
        print("One Coffee has been added to your order")
    
    #Checks if Item is equal to 5
    elif Item == "5":
        Final_Total = Final_Total + 1.50
        Item_5 = Item_5 + 1
        print("One Tea has been added to your order")
    
    else:
        print("The item you have selected has not been found! Please check that you entered the correct number.")