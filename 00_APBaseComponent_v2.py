# Base component for the Area and Perimeter Program
# Version Two - Adding in the Shape Type

# Author - Linn Herzig
# LH 2023

# Import libraries below this line **************************

# Initiating lists below this line **************************

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


# Function for displaying the instructions
def instructions():
    print(" \n **** How to Use **** \n"
          "- When prompted please enter the number corresponding to the desired shape \n"
          "- Then, when prompted please enter the correct shape dimensions \n"
          "- Once the answers have been shown you will be asked whether you would like to chose another shape or not \n"
          "- If you chose yes, the program will repeat from after viewing the instructions \n"
          "- If you chose no, the program  will display the calculation history of the session before ending "
          "- ** Please Note: Answers are rounded to two decimal places **\n")
    return""


# Main Routine below this line ******************************
print("Welcome to the Area and Perimeter Homework Calculator")

# Asking user if they would like to view the instructions
show_instructions = yesno("\nWould you like to view the instructions? (yes/no) ")

if show_instructions == "yes":
    instructions()

# Printing available shape options
print("\nShape options: \n"
      "1. Square \n"
      "2. Rectangle \n"
      "3. Parallelogram \n"
      "4. Triangle \n"
      "5. Circle")

# Asking user what shape they want to choose:
shape_type = variety("\nEnter the number corresponding to desired shape: ")
