from turtle import *#imports the turtle

Iterate = "Y"#Forces interface to always be active
while Iterate == "Y":
    color ('blue', 'red')#Sets the turtle color (Border, Interior)
    begin_fill()#Tells turtle to draw / get ready to draw

    Shape_Type = input("Enter the shape you would like to draw in capital letters")#Allows user to select their choice
    Shape_Size = int(input("Enter the size of the shape"))
    
    if Shape_Type == "SQUARE":#Square
        for Loop in range(4):
            forward(Shape_Size)
            right(90)

    elif Shape_Type == "TRYANGLE":
        for Loop in range(2):
            forward(Shape_Size)
            right(60)
        right(90)
        Shape_Size = Shape_Size * 2
        forward(Shape_Size)

    elif Shape_Type == "PENTAGON":
        for Loop in range(5):
            forward(Shape_Size)
            left(72)
    
    else:
        print("Shape not found")
    
    end_fill()#Resets the turtle
    done()