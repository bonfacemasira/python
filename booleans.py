print(10 > 9)
print((10 == 9))

# Evaluate Values and Variables
print(bool('Hello'))
print(bool(15))
print(bool(0))


#False values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction() :
  return False

print(myFunction())
if myFunction():
  print('YES!')
else:
  print('NO!')

x = 200
print(isinstance(x, int))