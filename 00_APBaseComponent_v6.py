# Base component for the Area and Perimeter Program
# Version Six - Adding in the New Shape Loop

# Author - Linn Herzig
# LH 2023

# Import libraries below this line **************************
import math

# Initiating lists below this line **************************
area_history = []
perimeter_history = []


# Functions below this line ******************************
# Function to check whether the user input is valid
def yesno(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("This is an invalid value. Please answer yes or no.")


# Function for displaying the instructions
def instructions():
    print(" \n **** How to Use **** \n"
          "- When prompted please enter the number corresponding to the desired shape \n"
          "- Then, when prompted please enter the correct shape dimensions \n"
          "- Once the answers have been shown you will be asked whether you would like to chose another shape or not \n"
          "- If you chose yes, the program will repeat from after viewing the instructions \n"
          "- If you chose no, the program  will display the calculation history of the session before ending \n"
          "- ** Please Note: Answers are rounded to two decimal places **\n")
    return""


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


# Main Routine below this line ******************************
print("Welcome to the Area and Perimeter Homework Calculator")

# Asking user if they would like to view the instructions
show_instructions = yesno("\nWould you like to view the instructions? (yes/no) ")

if show_instructions == "yes":
    instructions()

# Initiating Variables
new_shape = True
invalid = False

# Loop for asking user to enter shape dimensions and if they would like to use a new shape
while new_shape:
    # Printing available shape options
    print("\nShape options: \n"
          "1. Square/Rectangle/Parallelogram \n"
          "2. Triangle \n"
          "3. Circle")

    # Asking user what shape they want to choose:
    shape_type = variety("\nEnter the number corresponding to desired shape: ")

    invalid = False
    while not invalid:
        # Asking the user whether they would like to use another shape
        result = input("\nWould you like to calculate the area and perimeter of another shape? (yes/no) ").lower()

        if result == "yes" or result == "y":
            print("You chose to continue.")
            new_shape = True
            invalid = True

        elif result == "no" or result == "n":
            print("You chose to not use another shape.")
            new_shape = False
            invalid = True

        else:
            new_shape = False
            invalid = False
            print("This is an invalid value. Please answer yes or no.")

# Printing Calculation History
print("\nCalculation History:")
for i in range(len(area_history)):
    print("Calculation", str(i + 1), "-", area_history[i], perimeter_history[i])

# Thank you message
print("\nThank you for using the Area and Perimeter Calculator.")
