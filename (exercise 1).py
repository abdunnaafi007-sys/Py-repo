print("temperature converter")
print("1.fahrenheit to celsius")
print("2.celsius to fahrenheit") 
choice = input("Enter your choice (1 or 2):")
if choice == '1':
    f = float(input("Enter temperature in fahrenheit:"))
    c = (f-32)*5/9
    print(f"temperature in celsius:{c:.2f}c")
elif choice == '2':
    c = float(input("Enter temperature in celsius:"))
    f = (c*9/5)+32
    print(f"temperature is fahrenheit:{f:.2f}f")
else:
    print("invalid choice !please enter 1 or 2")
