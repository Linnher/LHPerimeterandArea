# Base component for the Area and Perimeter Program
# Version Seven - Implementing the User Feedback Suggestions
# Final Version of the Area and Perimeter Program

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
            print("Sorry, this is an invalid value. Please answer yes or no.")


# Function for displaying the instructions
def instructions():
    print(" \n**** Instructions for Use **** \n"
          "- When asked please enter the number matching the shape you want to calculate\n"
          "- Then enter the correct shape dimensions\n"
          "- You are given the option to use the calculator again\n"
          "- Your Calculation History will be shown at the end of the session\n"
          "Please Note: The calculator assumes numbers of same units are entered for each individual calculation\n"
          "Please Note: Answers are rounded to two decimal places\n")
    return""


# Number input validator
def check(words):
    valid = False
    while not valid:
        answer = input(words)
        test_answer = answer

        if test_answer.replace(".", "").isnumeric():
            real_answer = float(answer)
            return real_answer

        else:
            print("Sorry, this is an invalid value. Please enter a positive number.")


# Function for asking user to input the shape type:
def variety(answer):
    valid = False
    while not valid:
        shape = input(answer).lower()

        if shape == "1" or shape == "one":
            print("You chose a Square/Rectangle/Parallelogram \n")
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
            print("You chose an Isosceles Triangle. \n")
            # Input of dimensions for Triangle
            base = check("Please enter the length of the base: ")
            height_two = check("Please enter the height: ")
            # Calculating Triangle area and perimeter
            area_two = 0.5 * base * height_two
            side_c = math.sqrt(((base / 2) ** 2) + (height_two ** 2))
            perimeter_two = base + (side_c * 2)
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_two, perimeter_two))
            # Adding to Calculation History List
            area_history.append("Triangle: \nArea = {:.2f} units^2".format(area_two))
            perimeter_history.append("Perimeter = {:.2f} units".format(perimeter_two))
            return shape

        elif shape == "3" or shape == "three":
            print("You chose a Circle. \n")
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
            print("Sorry, this is an invalid input. Please try again using a number ranging from 1 - 3.")


# Main Routine below this line ******************************
print("Welcome to the Area and Perimeter Homework Calculator \n"
      "This is a tool which allows you to check and calculate the area and perimeter of different shapes.")

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
          "2. Isosceles Triangle \n"
          "3. Circle")

    # Asking user what shape they want to choose:
    shape_type = variety("\nPlease enter the shape number: ")

    invalid = False
    while not invalid:
        # Asking the user whether they would like to use another shape
        result = input("\nWould you like to calculate the area and perimeter of another shape? (yes/no) ").lower()

        if result == "yes" or result == "y":
            new_shape = True
            invalid = True

        elif result == "no" or result == "n":
            new_shape = False
            invalid = True

        else:
            new_shape = False
            invalid = False
            print("Sorry, this is an invalid value. Please answer yes or no.")

# Printing Calculation History
print("\nCalculation History:")
for i in range(len(area_history)):
    print("Calculation", str(i + 1), "-", area_history[i], perimeter_history[i])

# Thank you message
print("\nThank you for using the Area and Perimeter Calculator.")
