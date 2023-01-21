#Example of creating variables
x = 5 #variable x
y = "John" #variable y
print(x)
print(y)


#Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Example
a = 4
A = "Sally"
print(a)
print(A)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Assign values to multiple variables in one line:
#1)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output variables via print()
#1)
x = "Python is awesome"
print(x)
#2)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#3)
x = 5
y = 10
print(x + y)


#Global variable:
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Create a variable inside a function, with the same name as the global variable

#Global variable by keyword global:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Answer => "Python is fantastic"