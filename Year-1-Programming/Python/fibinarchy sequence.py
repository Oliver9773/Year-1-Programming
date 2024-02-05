Number1 = 0
Number2 = 1
Places = int(input("Enter the number of places: "))
Reverse_Places = []
for Loop in range(Places):
   print(Number1)
   Reverse_Places.append(Number1)
   Number1, Number2 = Number2, Number1 + Number2
Reverse_Places.reverse()
print("Reverced order: ", Reverse_Places)
Total = sum(Reverse_Places)
print("Total: ", Total)