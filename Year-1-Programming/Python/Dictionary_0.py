Dictionary = {"Number": 20, "Number": 47, "Number": 7}
Dictionary_Upper = sorted(Dictionary.get("Number"))
Dictionary_Lower = Dictionary_Upper[::-1]
print("Original Dictionary... ", Dictionary)
print("Ascending Dictionary... ", Dictionary_Upper)
print("Decending Dictionary... ", Dictionary_Lower)