# Version Two of Calculation History
# Adding the Calculation History Component to Area and Perimeter Calculator

# Importing Libraries
import math

# Lists
area_history = []
perimeter_history = []


# Number input validator
def check(words):
    valid = False
    while not valid:
        answer = input(words)
        test_answer = answer

        if test_answer.replace(".", "").isnumeric():
            real_answer = float(answer)
            print("This value is accepted.")
            return real_answer

        else:
            print("This value is invalid, please enter a positive number.")


# Function for asking user to input the shape type:
def variety(answer):
    valid = False
    while not valid:
        shape = input(answer).lower()

        if shape == "1" or shape == "one":
            print("You have chosen a Square/Rectangle/Parallelogram \n")
            # Input of Shape dimensions for Rectangle, Square, Parallelogram area and perimeter
            width_one = check("Please enter the width: ")
            height_one = check("Please enter the height: ")
            # Calculating Rectangle, Square, Parallelogram area and perimeter
            area_one = width_one * height_one
            perimeter_one = 2 * (width_one + height_one)
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_one, perimeter_one))
            # Adding to Calculation History List
            area_history.append("Square/Rectangle/Parallelogram: \nArea = {:.2f} units^2".format(area_one))
            perimeter_history.append("Perimeter = {:.2f} units".format(perimeter_one))
            return shape

        elif shape == "2" or shape == "two":
            print("You have chosen a Triangle. \n")
            # Input of dimensions for Triangle
            side_b = check("Please enter the length of Side B (Base): ")
            side_a = check("Please enter the length of Side A: ")
            side_c = check("Please enter the length of Side C: ")
            height_two = check("Please enter the height: ")
            # Calculating Triangle area and perimeter
            area_two = 0.5 * side_b * height_two
            perimeter_two = side_a + side_b + side_c
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_two, perimeter_two))
            # Adding to Calculation History List
            area_history.append("Triangle: \nArea = {:.2f} units^2".format(area_two))
            perimeter_history.append("Perimeter = {:.2f} units".format(perimeter_two))
            return shape

        elif shape == "3" or shape == "three":
            print("You have chosen a Circle. \n")
            # Input of dimensions for Circle
            radius = check("Please enter the radius: ")
            # Calculating Circle area and perimeter
            area_three = math.pi * radius ** 2
            circumference = 2 * math.pi * radius
            print("\nArea: {:.2f} units^2 \n"
                  "Circumference: {:.2f} units".format(area_three, circumference))
            # Adding to Calculation History List
            area_history.append("Circle: \nArea = {:.2f} units^2".format(area_three))
            perimeter_history.append("Circumference = {:.2f} units".format(circumference))
            return shape

        else:
            print("This is an invalid input please try again using a number ranging from 1 - 3.")


# Main Routine below this line:
# Printing available shape options
print("\nShape options: \n"
      "1. Square/Rectangle/Parallelogram \n"
      "2. Triangle \n"
      "3. Circle")

# Asking user what shape they want to choose:
shape_type = variety("\nEnter the number corresponding to desired shape: ")

# Concatenating Lists
total_history = area_history + perimeter_history

# Printing Calculation History
print("\nCalculation History:")
for i in range(len(total_history)):
    print(total_history[i])
