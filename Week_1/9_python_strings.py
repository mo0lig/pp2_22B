print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1]) #Answer=> e

#Looping Through a String
for x in "banana":
    print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String 1
txt = "The best things in life are free!"
print("free" in txt)

#Check String 2 by if
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT 1
txt = "The best things in life are free!"
print("expensive" not in txt)

#Check if NOT 2 by if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


#Slicing Strings 
b = "Hello, World!"
print(b[2:5]) # Output => llo

#Slice From the Start
b = "Hello, World!"
print(b[:5]) #Output => Hello

#Slice To the End
b = "Hello, World!"
print(b[2:]) #Output => llo, World!

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#String upper case
a = "Hello, World!"
print(a.upper()) #Output => HELLO, WORLD!

#Lower Case
a = "Hello, World!"
print(a.lower()) #OUtput =>hello, world!

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c) #Output => HelloWorld

#String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Escape Character, Error:
txt = "We are the so-called "Vikings" from the north."

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."

#Single Quote
txt = 'It\'s alright.'
print(txt)  # Output => It's alright.

#Backslash
txt = "This will insert one \\ (backslash)."
print(txt) #Output => This will insert one \ (backslash).

#New Line
txt = "Hello\nWorld!"
print(txt) 
"""Ouput => 
Hello
World!"""

#Carriage Return
txt = "Hello\rWorld!"
print(txt) 
"""Ouput => 
Hello
World!"""

#Tab
txt = "Hello\tWorld!"
print(txt)  #Output => Hello   World!

#Backspace
txt = "Hello \bWorld!"
print(txt)  #Output => HelloWorld!
