# 1) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

# 1a) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

def measurements():
    length = float(input("What lenght does your house has? "))
    width = float(input("What is  the width of your house? "))
    if length or width > 0:
        area = length * width
        return area
    else:
        print("Please enter a value greater than 0 ")

area = measurements()
print(f"The square footage of your house is {area} sqft")