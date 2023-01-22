# to work with arrays in Python you will have to import a library, like the NumPy library.

#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)  #['Ford', 'Volvo', 'BMW']

#Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)  #Ford

#Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)  #['Toyota', 'Volvo', 'BMW']

#Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)  #3


#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
"""Output:
Ford
Volvo
BMW"""

#Adding Array Elements
#Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)  #['Ford', 'Volvo', 'BMW', 'Honda']


#Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)  #['Ford', 'BMW']

#Delete the element that has the value "Volvo":
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)  #['Ford', 'BMW']


"""Array Mehtods:
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list"""

