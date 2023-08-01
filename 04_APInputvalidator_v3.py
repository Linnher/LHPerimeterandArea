# Version three of Input validator

# Number input validator - Last version did not accept float input (now it does due to code update)
def check(words):
    try:
        float(input(words))
        print("This value is accepted.")
        return words
    except ValueError:
        print("This value is invalid, please enter a positive integer.")
        return words


# Main Routine
# Input of Shape dimensions
width_one = check("Please enter the width: ")
height_one = check("Please enter the height: ")
