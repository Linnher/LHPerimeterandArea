# Version one of Shape Dimensions
# Basic version of what component is supposed to achieve

# Importing Libraries
import math

# Input of Shape dimensions for Rectangle, Square, Parallelogram area and perimeter
width_one = float(input("Please enter the width: "))
height_one = float(input("Please enter the height: "))

# Calculating Rectangle, Square, Parallelogram area and perimeter
area_one = width_one * height_one
perimeter_one = 2 * (width_one * height_one)

print("\nArea: {:.2f} units^2 \n"
      "Perimeter: {:.2f} units".format(area_one, perimeter_one))

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

# Input of dimensions for Circle
radius = float(input("Please enter the radius: "))

# Calculating Circle area and perimeter
area_three = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("\nArea: {:.2f} units^2 \n"
      "Circumference: {:.2f} units".format(area_three, circumference))

