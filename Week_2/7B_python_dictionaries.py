#Change Dictionary Items
#Change the "year" to 2018:
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

"""The update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs."""
#Update the "year" of the car by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Adding Items
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Add a color it
# em to the dictionary by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}



#Removing Items
#The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)  #{'brand': 'Ford', 'year': 1964}
 
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem() 
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang'}

#The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)  #{'brand': 'Ford', 'year': 1964}

#The clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)  #{}

#Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)
"""brand
model
year"""

#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
"""Ford
Mustang
1964"""

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)
"""Ford
Mustang
1964"""

#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)
"""brand
model
year"""

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)
"""brand Ford
model Mustang
year 1964"""

#Copy a Dictionary
#Make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Make a copy of a dictionary with the dict() function:
mydict = dict(thisdict)
print(mydict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#Nested Dictionaries
#Create a dictionary that contain three dictionaries:
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
} 
print(myfamily)  #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)  #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

"""DICTIONARY METHODS
Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary"""

