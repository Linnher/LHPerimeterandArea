# Version One of Calculation History
# Basic function of Calculation History - Test Version

# Calculation History Lists
area_history = []
perimeter_history = []

# Test Data
shape_1 = "Rectangle"
shape_2 = "Square"
test_1 = 1
test_2 = 2
test_3 = 3

# Adding to List
area_history.append("{}: Area = {} units^2".format(shape_1, test_1,))
perimeter_history.append("{}: Perimeter = {} units".format(shape_2, test_3,))
total_history = area_history + perimeter_history

# Printing Area History
for i in range(len(total_history)):
    print(total_history[i])
