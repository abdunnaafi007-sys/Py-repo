import math

print("Area Calculator")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print(f"Area of Rectangle = {area:.2f}")

elif choice == '2':
    side = float(input("Enter the side of the square: "))
    area = side * side
    print(f"Area of Square = {area:.2f}")

elif choice == '3':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print(f"Area of Circle = {area:.2f}")

elif choice == '4':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area:.2f}")

else:
    print("Invalid choice! Please select a number from 1 to 4.")
