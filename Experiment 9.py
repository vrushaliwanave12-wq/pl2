#Shapes.py
import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

#Main.py
import Shapes

def main():
    print("Choose a shape to calculate the area:")
    print("1.Circle")
    print("2.Rectangle")
    print("3.Triangle")

    choice = input("Enter the number of your choice:")

    if choice == "1":
        radius = float(input("Enter the radius of the circle:"))
        area = shapes.circle_area(radius)
        print("The area of the circle is: {area:.2f}")

    elif choice == "2":
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        area = shapes.rectangle_area(length, width)
        print("The area of the rectangle is: {area:.2f}")

    elif choice == "3":
        base = float(input("Enter the base of the triangle:"))
        height = float(input("Enter the height of the triangle:"))
        area = shapes.triangle_area(base, height)
        print("The area of the triangle is: {area:.2f}")

    else:
       print("Invalid choice. Please select a valid option.")

if _name_=="_main_":
    main()