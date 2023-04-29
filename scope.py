# Local Scope
def myfunc():
    x = 300
    print(x)

# myfunc()

# Function Inside Function
def myfunc1():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

# myfunc1()

# Global Scope
y = 200

def myfunc2():
    print(y)
    
# myfunc2()

# print(y)

# Naming Variables
def myfunc3():
    y = 100
    print(y)

# myfunc3()

# print(y)

# Global Keyword
def myfunc4():
  global z
  z = 300

# myfunc4()

# print(z)

c = 300

def myfunc():
  global c
  c = 200

myfunc()

print(c)