#Thief
import random

Digit_1 = input("Enter digit")
Digit_2 = input("Enter digit")
Digit_3 = input("Enter digit")
Digit_4 = input("Enter digit")
List = [Digit_1, Digit_2, Digit_3, Digit_4]
for Loop in range(16):
    random.shuffle(List)
    print(List)