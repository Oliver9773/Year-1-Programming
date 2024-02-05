file = open("gamerscore.csv", "r")
line = file.readline()

while(line):
    data = line.split(",")
    
    if data[1] == "7963":
        print("Handel: ",data[0])

    if int(data[1]) < 6000:
        print("Handel: ",data[0])
        print("Gamerscore: ",data[1])
    line=file.readline()

file.close()