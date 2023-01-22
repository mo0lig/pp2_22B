"""Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets."""

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)  #('apple', 'banana', 'cherry')
 
#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  #('apple', 'banana', 'cherry', 'apple', 'cherry')

#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #3

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))  #<class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))  #<class 'str'>

#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)  #('apple', 'banana', 'cherry')
print(tuple2)  #(1, 5, 7, 9, 3)
print(tuple3)  #(True, False, False)

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) #('abc', 34, True, 40, 'male')

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  #<class 'tuple'>

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)  #('apple', 'banana', 'cherry')

"""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
#Access Tuple Items
#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  #banana


#Negative Indexing
#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Range of Indexes
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Range of Negative Indexes
#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if Item Exists
#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


#Change Tuple Values
"""Tuples are unchangeable, or immutable as it also is called."""
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  #("apple", "kiwi", "cherry")

#Add Items
#1)Convert into a list:
#   Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)  #('apple', 'banana', 'cherry', 'orange')
#2)Add tuple to a tuple
#Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  #('apple', 'banana', 'cherry', 'orange')

#Remove Items
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)  #('banana', 'cherry')

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


