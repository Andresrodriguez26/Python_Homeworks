# 1b) Has a function to calculate the circumference of a circle 2 Pi r


    
import math

def circle():
    radius = float(input("What is the radius of your circle? "))
    circumference = 2 * math.pi * radius
    return circumference

circumference = circle()
print(f"The circumference of your circle is {circumference} cm")
