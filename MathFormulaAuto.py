## Program to automate various mathematical calculations
# Import Modules before anything else
import math

# Setting Variable libraries to create the branching program
shapes = ['triangle', 'rectangle', 'circle']
equation =['hypotenuse', 'area', 'perimeter', 'radius', 'circumference']

# Asking for unser input to decide what if statements to follow
shape = input("Are you working with a triangle, rectangle or circle?\n")

# If Triangle:
if shape == shapes[0]:
    user_selection_input = str(input("Would you like to find the hypotenuse, perimeter or the area of the triangle?\n"))
    short = float(input("what is the length of the short side?\n"))
    long = float(input("what is the length of the long side that is not the hypotenuse?\n"))

    # compute hypotenuse
    if user_selection_input == equation [0]:
        sides = (short**2 + long**2)
        hypotenuse = math.sqrt(sides)
        print("The hypotenuse is " + str(hypotenuse))
        print("Isn't it fun finding the hypotenuse that easily?")

    # compute area
    if user_selection_input == str(equation [1]):
        area = (short * long)/2
        print ("The area of your triangle is " + str(area))
        print ("Isn't it fun finding the area so easily?")


    # compute perimeter
    if user_selection_input == equation[2]:
        sides = (short**2 + long**2)
        hypotenuse = math.sqrt(sides)
        perimeter = short + long + hypotenuse
        print("The perimeter of your triangle is " + str(perimeter))
        print("Isn't it delightful to automate the perimeter like this?")

# If Rectangle:
if shape == shapes[1]:
    user_selection_input = str(input("Would you like to find the perimeter or the area of the rectangle?\n"))
    side1 = float(input("what is the length of the the first side?\n"))
    side2 = float(input("what is the length of the the second side?\n"))

    if user_selection_input == equation [1]:
        area = side1 * side2
        print("The Area of your Rectangle is " + str(area) + ".\nIsn't it fun how easy this is?")
        
    if user_selection_input == equation [4]:
        perimeter = side1 *2 + side2 * 2
        print("The Perimeter of your Rectangle is " + str(perimeter) + ".\nIsn't it fun how easy this is?")
        


# If Circle
if shape == shapes[2]:
    user_selection_input = str(input("Would you like to find the circumference or the area of the circle?\n"))
    radius = float(input("what is the radius of your circle?\n"))

    if user_selection_input == equation [1]:
        area = math.pi*radius**2
        print("The Area of your Circle is " + str(area) + ".\nHow sweet is that?")

    if user_selection_input == equation [4]:
        circumference = (2*math.pi)*radius
        print("The Circumference of your Circle is " + str(circumference) + ".\nNow, wasn't that easy?")
