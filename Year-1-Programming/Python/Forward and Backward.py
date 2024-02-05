#Forward and Backward
Input = input("Enter a word")
Input_Reverse = Input[::-1]
if Input == Input_Reverse:
    print(Input, "is a palindrome")
else:
    print("This is not a palindrome")