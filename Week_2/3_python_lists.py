#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist) #Output => ['apple', 'banana', 'cherry']

#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1) #["apple", "banana", "cherry"]
print(list2) #[1, 5, 7, 9, 3]
print(list3) #[True, False, False]

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1) #['abc', 34, True, 40, 'male']

#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #Output => <class 'list'>

#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

#Negative Indexing
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry

#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword also removes the specified index

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)