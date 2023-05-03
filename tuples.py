thistuple = ("apple", "orange", "cherry", "banana")
# print(thistuple)

# Tuple Length
# print(len(thistuple))

# Create Tuple With One Item
oneitemtuple = ("apple",)
# print(type(oneitemtuple))

createdtuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(createdtuple)

# Python - Access Tuple Items
print(thistuple[1])

# Negative Indexing
print(thistuple[-1])

# Range of Indexes
print(thistuple[2:5])

print(thistuple[:4])

print(thistuple[2:])

# Range of Negative Indexes
print(thistuple[-4:-1])

# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")