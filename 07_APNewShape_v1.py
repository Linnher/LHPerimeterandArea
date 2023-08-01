# Version One of New Shape
# Looping the Program and asking user if they want to use another shape

# Importing Libraries
import math


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
            return shape

        else:
            print("This is an invalid input please try again using a number ranging from 1 - 3.")


# Main Routine below this line:
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
            print("You chose to not continue.")
            new_shape = False
            invalid = True

        else:
            new_shape = False
            invalid = False
            print("This is an invalid value. Please answer yes or no.")

# Thank you message
print("\nThank you for using the Area and Perimeter Calculator!")
