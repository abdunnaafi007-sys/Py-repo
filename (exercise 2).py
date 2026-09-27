# Number of rows in the increasing part
n = 5

# Upper triangle (including middle row)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Lower triangle
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
