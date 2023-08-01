# Version two of Shape Type
# Turning the previous version into a function

# Function for asking user to input the shape type
def variety(answer):
    valid = False
    while not valid:
        shape = input(answer).lower()

        if shape == "1" or shape == "one":
            print("You have chosen a Square.")
            return shape

        elif shape == "2" or shape == "two":
            print("You have chosen a Rectangle.")
            return shape

        elif shape == "3" or shape == "three":
            print("You have chosen a Parallelogram.")
            return shape

        elif shape == "4" or shape == "four":
            print("You have chosen a Triangle.")
            return shape

        elif shape == "5" or shape == "five":
            print("You have chosen a Circle.")
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
