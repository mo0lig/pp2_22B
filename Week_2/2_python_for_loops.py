#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""Output:
apple
banana
cherry
"""

#Looping Through a String
for x in "banana":
    print(x) 

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
"""Output:
apple
banana"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#OUtput => apple

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


#The range() Function
for x in range(6):
    print(x)

#Using the start parameter:
for x in range(2, 6):
    print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement
for x in [0, 1, 2]:
    pass