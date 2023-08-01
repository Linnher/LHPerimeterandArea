# Version two of Input validator
# This is the Input Validator version used in the next components - only fully functioning version

# Number input validator - Now additionally checks if the input is a string
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


# Main Routine
# Input of Shape dimensions
width_one = check("Please enter the width: ")
height_one = check("Please enter the height: ")




