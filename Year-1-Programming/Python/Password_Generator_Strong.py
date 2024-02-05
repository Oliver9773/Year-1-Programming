#Password generator
import random
import string
Letter_Upper = string.ascii_uppercase
Letter_Lower = string.ascii_lowercase
Number = random.randint(100000,999999)
Number = str(Number)
Punctuation = string.punctuation
Password = [Letter_Lower, Letter_Upper, Number, Punctuation]
Password_list = set(Password)
Password_Answer = str(Password_list)
print(Password_list)