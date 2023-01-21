#Boolean Values
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#Output => b is not greater than a

#Evaluate Values and Variables
print(bool("Hello")) #True
print(bool(15)) #True

#Evaluate two variables:
x = "Hello"
y = 15
print(bool(x)) #True
print(bool(y)) #True

#True Values
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some false values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Functions can Return a Boolean
def myFunction() :
    return True
print(myFunction()) #True


def myFunction() :
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
    #Output => YES!


x = 200
print(isinstance(x, int)) #True