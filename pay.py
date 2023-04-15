print('hello bitches')

# variables
x, y, z = 2, 4, 5

print(x + y + z)
print(x, y, z)

# variable types

a = str(34)  # changes variable to type string
b = int(43)  # changes variable to type number
c = float(34)  # changes variable to type float in terms of decimals

print(a, b, c)

# Get the data type of a variable with the type() function.
print(type(x))
print(type(a))

# functions
name = " sheran"  # this is goblal variable


def myfun():  # function decleration
    last = "thasrchrn"  # this is goblal variable
    global name  # this change a global variable inside a function.
    name = 'wang'
    print(name, last)


myfun()  # caalling function

# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# q= range(30) Data Types range
dict = {"name": "tharchen", "age": 21}  # Data Types dict
print(type(dict))
print(dict)

set = {'x', 'y', 'a'}  # Data Types set
print(type(set))
print(set)

list0 = ["apple", "banana", "cherry"]  # Data Types list
print(type(list0))
print(list0)

frozenset = frozenset({1, 2, 3, 't'})  # Data Types frozenset
print(type(frozenset))
print(frozenset)

boole = True  # Data Types bool || boolean
print(type(boole))
print(boole)

bytearray = bytearray(5)  # Data Types bytearray || bytearray
print(type(bytearray))
print(bytearray)

byte = b'hellow'  # Data Types bytes
print(type(byte))
print(byte)

emoryvie1 = memoryview(bytes(5))  # Data Types memoryview
print(type(emoryvie1))
print(emoryvie1)

none = None  # Data Types NoneType
print(type(none))
print(none)

# Setting the Specific Data Type

srinig = str('tharchen sherpa')
age = int(20)
weight = float(70)
com = complex(51j)

hobbies = ["apple", "banana", "cherry"]

memory = memoryview(bytes(100))

print(srinig, age, weight, com, hobbies, memory)

# There are three numeric types in Python:
x1 = 1  # int
y1 = 2.8  # float
z1 = 1j  # complex

print(type(x1))
print(type(y1))
print(type(z1))

# Convert from one type to another:
a = float(x1)

# convert from float to int:
b = int(y1)

# convert from int to complex:
c = complex(y1)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 100))

# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Loop through the letters in the word "banana":

for h in 'banana':
    print(h)

# String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:

exp = 'sherab tharchen'
print(len(exp))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

twt = 'this is tharchen sherpa'
# in
print('tharchen' in twt ) 
# not in
print('sherab' not in twt ) 
# Use it in an if statement:
if 'tharchen' in twt:
    print('yes, "tharchen" is there')

# Check if NOT
if "sherab" not in twt:
    print("not here")


#     Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

slic = 'tharchen sherpa'
print(slic[1:7])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
print(slic[:9])

# Slice To the End
# By leaving out the end index, the range will go to the end:

print(slic[9:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print(slic[-5:-2])


# Upper Case
# The upper() method returns the string in upper case:

cas =' sherab , tharchen '
bas = "sherpa"
print(cas.upper())

# The lower() method returns the string in lower case:
print(cas.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end:

print(cas.strip())

# Replace String
# The replace() method replaces a string with another string:
print(cas.replace('s', 't'))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:
print(cas.split('b'))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
jd = cas + bas
space = cas + '          ' + bas 
print(jd)
print(space)

# String Format()
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age = 36
ft = cas + '          ' + bas + 'i am {}'
print(ft.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity, itemno, price))


# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

esacp = "this is bash \'Escape Character\' ean la"
print(esacp)

# Single Quote
txt1 = 'It\'s alright.'
print(txt1) 

# Backslash
txt2 = "This will insert one \\ (backslash)."
print(txt2) 

# New Line
txt3 = "Hello\nWorld!"
print(txt3)

# Carriage Return
txt4 = "Hello\rWorld!"
print(txt4) 

# Tab
txt5 = "Hello\tWorld!"
print(txt5) 

# Backspace
#This example erases one character (backspace):
txt6 = "Hello \bWorld!"
print(txt6)   

# Form Feed
txt7 = "Hello \fWorld!"
print(txt7)   

# Octal value
#A backslash followed by three integers will result in a octal value:
txt8 = "\110\14\154\154\157"
print(txt8) 

# Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt0 = "\x48\x65\x6c\x6c\x6f"
print(txt0) 


# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.

t =300
f= 900

if t==f:
    print('right backback')
else:
    print('wrong backback')

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool(t))
print(bool(f))

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(bool(False))

# Python Assignment Operators
# Assignment operators are used to assign values to variables:


num1=20
num2=10

num1 += 5 # x = x + 3

print(num1)

# Comparison Operators
print(num1 != num2)
print(num1 == num2)

# Python Logical Operators
# Logical operators are used to combine conditional statements:

print(num1<10 and num2>3) # Returns True if both statements are true

print(num1 == 0 or num2== 1)  # Returns True if one of the statements is true

print(not( num1 == 0 and num2== 1)) # 	Reverse the result, returns False if the result is true

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

print(num1 is num2)
# print(num1 not in num2)

# Python Bitwise Operators
print(num1&num2) # AND
print(num1&num2) # OR
print(num1^num2) # XOR
print(~num2) # NOT
print(num2 << 2) # 	Zero fill left shift
print(num2 >> 2) # Signed right shift	

# List

mylist = ['wang','toll', 'thars,',4]
print(mylist)
print(mylist[0])
print(len(mylist)) #length

list1 = ["abc", 34, True, 40, "male"] #mixed

print(list1)

print(type(list1)) # data types

# Range of Indexes
print(list1[1:4])
print(list1[:3])
print(list1[3:])

if 'abc' in list1:
    print('true mf')

# Change Item Value
# To change the value of a specific item, refer to the index number:
list1[0]= 'sherpas'
print(list1)

# Change a Range of Item Values
mylist[1:2] = ['abbs' ,'abbs2']
print(mylist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

mylist.insert(0, 'tharchens')
list1.insert(1, 2000)
print(mylist)
print(list1)


# Append Items
# To add an item to the end of the list, use the append() method:

list1.append(10000)
mylist.insert(50,600090)
print(mylist)
print(list1)

# Extend List
# To append elements from another list to the current list, use the extend() method.

mylist.extend(list1)
print(mylist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.
mylist.remove("tharchens")
print(mylist)

# Remove Specified Index
# The pop() method removes the specified index.

mylist.pop(3)
thislist.pop(3)
print(mylist)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
mylist.pop()
print(mylist)

# The del keyword also removes the specified index:
del mylist[0]
print(mylist)

# The del keyword can also delete the list completely.
# del mylist
# print(mylist)

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

thislist.clear()
print(thislist)

# Loop Through a List

newlist =['sherab','tharchen','bhai']

for x in newlist:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

for i in range(len(newlist)):
    print(newlist[i])

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.


k = 0
while k < len(newlist):
    print(newlist[k])
    k = k + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:

[print(n) for n in newlist]


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitlist =[]
for x in fruits:
    if "a" in x:
        fruitlist.append(x)
print(fruitlist) # prints sting with a in it


# With list comprehension you can do all that with only one line of code:
listing = [x for x in fruits if "i" in x]
print(listing)

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# Condition
# The condition is like a filter that only accepts the items that valuate to True.

newlisting = [x for x in fruits if x != 'apple']
print(newlisting)

noif = [x for x in fruits]
print(noif)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc
# You can use the range() function to create an iterable:
iteri = [x for x in range(10)]
print(iteri)


# Accept only numbers up on given condition :
only = [x for x in range(15) if x >7 ]
print(only)

# Set the values in the new list to upper case:
capt = [x.upper() for x in fruits]
print(capt)

# Set all values in the new list to 'hello':
change = ['hello' for x in fruits]
print(change)


# Return "orange" instead of "banana":
ret = [x if x != 'banana' else 'orange' for x in fruits]
print(ret)

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
shortlist = ['sherab','vikra','tharchen','dherpa','okai']
# all ascending
shortlist.sort() # arranges the string
print(shortlist)

num = [20,0,2,23,4,5,56,5,4,9]
num.sort()
print(num)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

shortlist.sort(reverse= True)
print(shortlist)

num.sort(reverse= True)
print(num)


# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key= str.lower)
print(thislist)

# The reverse() method reverses the current sorting order of the elements.

thislist.reverse()
print(thislist)

# Copy a List
# There are ways to make a copy, one way is to use the built-in List method copy().
listcopy = thislist.copy()
print(listcopy)

# Join Two Lists
joinlist = listcopy + num
print(joinlist  )

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = [1,2,3,4,5]
list2= [2,4,6,7,89,9]

for x in list2:
    list1.append(x)
print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1.extend(list2)
print(list1)

# ct = fruitlist.count()
# print(ct)

# Python Tuples
mytuple = ('sherab','tharchen', 'sherpa', 'bhai')
# A tuple is a collection which is ordered and unchangeable.
print(mytuple)
print(type(mytuple))
print(len(mytuple))

mytuple1 = ('only one')
print(type(mytuple1))

# Using the tuple() method to make a tuple:
tup = tuple((1,2,3,True,False))
print(tup)
print(tup[3])

# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

print(tup[-1])
print(tup[-2])
print(tup[:3]) # range of indexing
print(tup[-2:-4]) # range of indexing

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

if 1 in tup:
    print('hell ya bitch')
else:
    print('no bitches')

# Change Tuple Values
app = list(tup)
app.append('orabge') # append() method
tup = tuple(app)

print(tup)

# app1 = list(tup)
# app1[0] = 000
# tup = tuple(tup)

# print(tup)


# Remove Items
remo = list(tup)
remo.remove(2) # remove methoid
tup = tuple(remo)

print(tup)

# The del keyword can delete the tuple completely:

del tup
# print(tup) # cause an error cause tup is lready deleated

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
unpack = (1,2,3,4)
(a,b,c,d) = unpack

print(a)
print(b)
print(c)
print(d)

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Asterisk = [1,2,3,4]
(a,*red) = Asterisk

print(a)
print(red)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

for x in Asterisk:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

for i in range(len(Asterisk)):
    print(Asterisk[i])

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#   Using a While Loop
# You can loop through the tuple items by using a while loop.

# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tub1 = (1,2,3,4,5)
tub2 = (3,0,4,5,6,7)

tub3 = tub1 + tub2 #addation
print(tub3)

tub4 = tub2 *2 #multiply
print(tub4)

# Python Sets
# Unchangeable Unordered
myset = {"apple", "banana", "cherry",1 }

print(myset)
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data,

# Duplicates Not Allowed
dipcl = {'sherab','sherab','sherab','tharchen'}
print(dipcl)

sets = {1,True,3,4,5,6,7} # The values True and 1 are considered the same value in sets, and are treated as duplicates:
print(sets)

print(len(sets))
print(type(sets))

# looping
for x in sets:
    print(x)

# Check if "   " is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# To add one item to a set use the add() method.
thisset.add('tharchen')
print(thisset)

# To add items from another set into the current set, use the update() method.
updateset = {"apple", "banana", "cherry","tharchen", "wangmo"}
thisset.update(updateset)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
irrset = [1,20]
thisset.update(irrset)
print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove('apple')
print(thisset)

#  using the discard() method:
thisset.discard('tharchen')
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

# pop() method
# thisset.pop()
# print(thisset) doing direct

p = thisset.pop() # shows the pop item
print(p)
print(thisset)

# clear ()
thisset.clear()
print(thisset)

#del 
del sets
# print(sets) gives err as sets is already deleted

thisset = {"apple", "banana", "cherry"}

# looping
for x in thisset:
    print(x)

# Join Two Sets
# The union() method returns a new set with all items from both sets:
thisset1 ={1,2,3,4,5}
thisset2 = thisset.union(thisset1)
print(thisset2)

# The update() method inserts the items in set2 into set1:
thisset3 ={1,2,3,4,5,6}
thisset.update(thisset3)
print(thisset)

# Note: Both union() and update() will exclude any duplicate items.

del x
del y

# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
del z
z =x.intersection(y)
print(z)

del x
del y


# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)


# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
zd = x.symmetric_difference(y)
print(zd)

# True and 1 is considered the same value: