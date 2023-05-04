# Change Tuple Values
x = ("apple", "orange", "cherry", )
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)

# Add Items - Convert into a list:
thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(z)

# print(thistuple)

# Add Items - Add tuple to tuple:
c = ("tomoko",)
thistuple += c
# print(thistuple)

# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
m = list(thistuple)
m.remove("apple")
thistuple = tuple(m)

# print(m)

# Or you can delete the tuple completely:
# del thistuple
print(thistuple)