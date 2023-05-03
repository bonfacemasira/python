# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# print(thislist)

numberlist = [100, 50, 65, 82, 23]
numberlist.sort()
# print(numberlist)

# Sort Descending
thislist.sort(reverse=True)
# print(thislist)

numberlist.sort(reverse=True)
# print(numberlist)

# Customize Sort Function
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

numlist = [100, 50, 65, 82, 23]
numlist.sort(key = myfunc)
# print(numlist)

# Case Insensitive Sort
thislist.sort(key = str.lower)
# print(thislist)

# Reverse Order
reverselist = ["banana", "Orange", "Kiwi", "cherry"]
reverselist.reverse()
print(reverselist)