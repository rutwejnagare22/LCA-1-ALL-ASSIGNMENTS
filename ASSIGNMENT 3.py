Write a Python program that accepts the length of three sides of a triangle as inputs. The program should indicate whether or not the triangle is a right-angled triangle using function.

# Assignment 3: Check whether a triangle is right-angled or not using function

def is_right_angled(a, b, c):
    sides = sorted([a, b, c])  # Arrange sides in ascending order

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Input three sides
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# Check and display result
if is_right_angled(side1, side2, side3):
    print("The triangle is a Right-Angled Triangle.")
else:
    print("The triangle is NOT a Right-Angled Triangle.") 