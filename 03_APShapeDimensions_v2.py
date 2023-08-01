# Version two of Shape Dimensions
# Combining version two of Shape Type and version one of Shape Dimensions

# Importing Libraries
import math


# Function for asking user to input the shape type:
def variety(answer):
    valid = False
    while not valid:
        shape = input(answer).lower()

        if shape == "1" or shape == "one":
            print("You have chosen a Square.")
            # Input of Shape dimensions for Rectangle, Square, Parallelogram area and perimeter
            width_one = float(input("Please enter the width: "))
            height_one = float(input("Please enter the height: "))
            # Calculating Rectangle, Square, Parallelogram area and perimeter
            area_one = width_one * height_one
            perimeter_one = 2 * (width_one + height_one)
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_one, perimeter_one))
            return shape

        elif shape == "2" or shape == "two":
            print("You have chosen a Rectangle.")
            # Input of Shape dimensions for Rectangle, Square, Parallelogram area and perimeter
            width_one = float(input("Please enter the width: "))
            height_one = float(input("Please enter the height: "))
            # Calculating Rectangle, Square, Parallelogram area and perimeter
            area_one = width_one * height_one
            perimeter_one = 2 * (width_one * height_one)
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_one, perimeter_one))
            return shape

        elif shape == "3" or shape == "three":
            print("You have chosen a Parallelogram.")
            # Input of Shape dimensions for Rectangle, Square, Parallelogram area and perimeter
            width_one = float(input("Please enter the width: "))
            height_one = float(input("Please enter the height: "))
            # Calculating Rectangle, Square, Parallelogram area and perimeter
            area_one = width_one * height_one
            perimeter_one = 2 * (width_one * height_one)
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_one, perimeter_one))
            return shape

        elif shape == "4" or shape == "four":
            print("You have chosen a Triangle.")
            # Input of dimensions for Triangle
            side_b = float(input("Please enter the length of Side B (Base): "))
            side_a = float(input("Please enter the length of Side A: "))
            side_c = float(input("Please enter the length of Side C: "))
            height_two = float(input("Please enter the height: "))
            # Calculating Triangle area and perimeter
            area_two = 0.5 * side_b * height_two
            perimeter_two = side_a + side_b + side_c
            print("\nArea: {:.2f} units^2 \n"
                  "Perimeter: {:.2f} units".format(area_two, perimeter_two))
            return shape

        elif shape == "5" or shape == "five":
            print("You have chosen a Circle.")
            # Input of dimensions for Triangle
            radius = float(input("Please enter the radius: "))
            # Calculating Triangle area and perimeter
            area_three = math.pi * radius ** 2
            circumference = 2 * math.pi * radius
            print("\nArea: {:.2f} units^2 \n"
                  "Circumference: {:.2f} units".format(area_three, circumference))
            return shape

        else:
            print("This is an invalid input please try again using a correct number")


# Main Routine below this line:
# Printing available shape options
print("\nShape options: \n"
      "1. Square \n"
      "2. Rectangle \n"
      "3. Parallelogram \n"
      "4. Triangle \n"
      "5. Circle")

# Asking user what shape they want to choose:
shape_type = variety("\nEnter the number corresponding to desired shape: ")
