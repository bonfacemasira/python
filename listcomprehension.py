fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# Condition
newlist1 = [x for x in fruits if x != "apple"]

# Iterable
newlist2 = [x for x in range(10)]

# Same example, but with a condition:
newlist3 = [x for x in range(10) if x < 5]

# Expression
newlist4 = ['hello' for x in fruits]

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)