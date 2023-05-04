# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

otherfruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = otherfruits

# print(green)
# print(yellow)
# print(red)

(green, *tropic, red) = otherfruits

print(green)
print(yellow)
print(red)
