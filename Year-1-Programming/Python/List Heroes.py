Heroes = ["Iron Man","Capitain America","Thor"]
print("Current pilot ",Heroes[0])
print("Current Co-pilot ",Heroes[1])
Heroes[2] = "Hit Girl"
Heroes.append("Hulk")
Heroes.append("Spider Man")
print(Heroes)
Replace_Member = int(input("Enter the hero you want to replace "))
New_Heroes = str(input("Enter the hero you want to replace the hero with "))
Heroes[Replace_Member] = New_Heroes