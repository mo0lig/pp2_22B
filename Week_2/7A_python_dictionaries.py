"""Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""
#Create and print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

"""Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name."""
#Print the "brand" value of the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"]) #Ford

"""When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index."""
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Print the number of items in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(len(thisdict))  #3

#String, int, boolean, and list data types:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
} 
print(thisdict)  #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#Print the data type of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))  #<class 'dict'>

#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)  #{'name': 'John', 'age': 36, 'country': 'Norway'}


#Accessing Items
#Get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]  #Mustang

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)  #Mustang

#The keys() method will return a list of all the keys in the dictionary.
#Get a list of the keys:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.keys()
print(x)  #dict_keys(['brand', 'model', 'year'])

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change -> dict_keys(['brand', 'model', 'year'])

car["color"] = "white"
print(x) #after the change  -> dict_keys(['brand', 'model', 'year', 'color'])


#Get Values
#The values() method will return a list of all the values in the dictionary.
#Get a list of the values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)  #dict_values(['Ford', 'Mustang', 1964])

#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change  ->  dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x) #after the change   ->  dict_values(['Ford', 'Mustang', 2020])

#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change  ->  dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
print(x) #after the change   ->  dict_values(['Ford', 'Mustang', 1964, 'red'])

#The items() method will return each item in a dictionary, as tuples in a list.
#Get a list of the key:value pairs
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)  #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change  ->  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
print(x) #after the change   ->  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

#Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change  ->  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["color"] = "red"
print(x) #after the change   ->  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

#Check if "model" is present in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary