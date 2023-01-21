# Numbers
x = 1
y = 2.8
z = 1j
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Numbers type INT
x = 1
y = 35656222554887711
z = -3255522
print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>

# Numbers type float
x = 1.10
y = 1.0
z = -35.59
print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>

#Numbers type complex
x = 3+5j
y = 5j
z = -5j
print(type(x)) # <class 'complex'>
print(type(y)) # <class 'complex'>
print(type(z)) # <class 'complex'>

#Type Conversion
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x)) # <class 'float'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'complex'>

#Random Number
import random
print(random.randrange(1, 10))

