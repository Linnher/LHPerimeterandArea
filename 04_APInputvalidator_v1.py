# Version one of Input validator

# Number input validator - Checks if input is negative or positive
def check(num):
    valid = False
    while not valid:
        answer = float(input(num))

        if answer < 0:
            print("This value is negative. Please enter a positive integer.")

        elif answer >= 0:
            print("This value is accepted.")
            return answer
        else:
            print("This value is invalid, please enter a positive integer.")


# Main Routine
# Input of Shape dimensions
width_one = check("Please enter the width: ")
height_one = check("Please enter the height: ")







