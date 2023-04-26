# Python For Loops

fruits = ["apple", "orange", "banana"]
for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break Statement
for x in fruits:
    print(x)
    if x == "orange":
        break

for x in fruits:
    if x == "orange":
        break
    print(x)


# The continue Statement
for x in fruits:
    if x == "orange":
        continue
    print(x)

# The range() Function
for x in range(6):
    print(x)

# Define start point in range() function
for x in range(2,8):
    print(x)

# Define the increment value in range() function
for x in range(10, 30, 2):
    print(x)

# Else in For Loop
for x in range(100):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in  fruits:
        print(x, y)

# The pass Statement
for x in [0, 1, 2]:
    pass