# Initialize counters
even_count = 0
odd_count = 0

# Input the size of the array
n = int(input("Enter the number of elements: "))

# Input the array elements
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the result
print("\n----- Result -----")
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
