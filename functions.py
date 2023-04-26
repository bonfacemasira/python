def my_function(fname, lname):
    print(f"Hello from a function to {fname} {lname}!")
    print("Hello from a function to " + fname + " " + lname + "!")

# my_function("Bonface", "Masira")

# Arbitrary Arguments, *args
def kids_function(*kids):
  print("The youngest child is " + kids[2])

# kids_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def keyword_function(child3, child2, child1):
   print("The youngest child is " + child3)

# keyword_function(child1="Linus", child2="Emil", child3="Tobias")

# Arbitrary Keyword Arguments, **kwargs
def keyword_arguments_function(**kid):
   print("His last name is " + kid["lname"])

# keyword_arguments_function(fname="Linus", lname = "Masira")

# Default Parameter Value
def default_value_function(country = "Norway"):
  print("I am from " + country)

# default_value_function("Sweden")
# default_value_function("India")
# default_value_function()
# default_value_function("Brazil")

# Passing a List as an Argument
def list_function(food):
   for x in food:
      print(x)

# fruits = ["apple", "banana", "cherry"]
# list_function(fruits)

def return_value_function(x):
   return 5 * x

# print(return_value_function(5))
# print(return_value_function(50))
# print(return_value_function(1))
# print(return_value_function(3))

# The pass Statement
def myfunctions():
   pass


# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)