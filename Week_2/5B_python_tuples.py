#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#Packing a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)  #('apple', 'banana', 'cherry')

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)  #apple
print(yellow) #banana
print(red)    #cherry

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)    #apple
print(yellow)   #banana
print(red)      #['cherry', 'strawberry', 'raspberry']

#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)    #apple
print(tropic)   #['mango', 'papaya', 'pineapple']
print(red)      #cherry


#Python - Loop Tuples

#Loop Through a Tuple
#Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
"""Output:
apple
banana
cherry"""

#Loop Through the Index Numbers
#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#Using a While Loop
#Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


#Join Two Tuples
#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  #('a', 'b', 'c', 1, 2, 3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


"""Tuple Methods:
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found"""








