# Version one of Shape Type
# Basic version of the Shape Type Component

# Asking user to input the shape type
print("\nShape options: \n"
      "1. Square \n"
      "2. Rectangle \n"
      "3. Parallelogram \n"
      "4. Triangle \n"
      "5. Circle")

# Validating user input
while True:
      shape = input("\nEnter the number corresponding to desired shape: ").lower()

      if shape == "1" or shape == "one":
            print("You have chosen a Square.")

      elif shape == "2" or shape == "two":
            print("You have chosen a Rectangle.")

      elif shape == "3" or shape == "three":
            print("You have chosen a Parallelogram.")

      elif shape == "4" or shape == "four":
            print("You have chosen a Triangle.")

      elif shape == "5" or shape == "five":
            print("You have chosen a Circle.")

      else:
            print("This is an invalid input please try again using a correct number.")
