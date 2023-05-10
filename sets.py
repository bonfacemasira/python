myset = {"apple", "banana", "cherry"}
# print(myset)

# Add Items
myset.add("orange")
# print(myset)

# Add sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
# print(thisset)

mylist = ["kiwi", "orange"]
myset.update(mylist)
# print(myset)

# Remove Item
removeset = {"apple", "banana", "cherry"}
print(removeset)

# removeset.remove("banana")
x = removeset.pop()
print(x)

print(removeset)

# The del keyword will delete the set completely:
# del removeset
print(removeset)

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)


print(s)

print(f'The set s has {len(s)} items.')