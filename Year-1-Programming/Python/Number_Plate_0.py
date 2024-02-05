Criminal_Vehicals = []#Sets up a wanted list
Iteration_Loop = str(input("Enter a capital 'Y' to add another vehical else enter capital 'N': "))#Asks if user wants to enter a vehical

while Iteration_Loop == "Y":#Loops vehical entery details
    Number_Plate = str(input("Enter the numberplate recorded: "))
    Distance = float(input("Enter the distance between the two sensors in miles: "))
    Time_Entered = float(input("Enter the time entered the monitored zone in hours: "))
    Time_Exit = float(input("Enter the time left the monitored zone in hours: "))
    Speed_Limit = float(input("Enter the speed limit for the road in miles per hour: "))

    Time = Time_Exit - Time_Entered#Calculates the time taken to travel from sensor 1 to sensor 2
    
    Speed = Distance / Time#Calculates Vehical speed
    
    if Speed > Speed_Limit:#Checks if speeding
        print("Wanted!")
        Criminal_Vehicals.append(Number_Plate)#Stores wanted vehical to criminal vehical list
    
   
    elif (Number_Plate[0:1]).isalpha == False:#Checks if registration is correct
        print("Wanted!")
        Criminal_Vehicals.append(Number_Plate)#Stores wanted vehical to criminal vehical list
    elif (Number_Plate[2:3]).isdigit == False:
        print("Wanted!")
        Criminal_Vehicals.append(Number_Plate)#Stores wanted vehical to criminal vehical list

    elif (Number_Plate[4:6]).isalpha == False:
        print("Wanted!")
        Criminal_Vehicals.append(Number_Plate)#Stores wanted vehical to criminal vehical list

   
    else:
        print("Not Wanted!")
    
    Iteration_Loop = str(input("Enter a capital 'Y' to add another vehical else enter capital 'N': "))#Asks if user wants to enter another vehical

print("All speeding vehicals: ", Criminal_Vehicals)#Outputs all criminal vehicals