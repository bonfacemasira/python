mylist = ["apple", "banana", "cherry"]
# print(mylist[0])
# print(len(mylist))

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)
thislist.insert(2, "watermelon")
# print(thislist)
thislist.append("orange")
# print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# print(list1)
# print(list2)
# print(list4)
# print(type(list4))

thatlist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thatlist[-1])

fruitlist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruitlist.extend(tropical)
# print(fruitlist)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print(thislist)

removelist = ["apple", "banana", "cherry"]
print(removelist)
# removelist.remove('banana')
# removelist.pop(1)
# removelist.pop()
# del removelist[0]
# del removelist
removelist.clear()
print(removelist)