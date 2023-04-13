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

list = ["apple", "banana", "cherry"]  # Data Types list
print(type(list))
print(list)

frozenset = frozenset({1, 2, 3, 't'})  # Data Types frozenset
print(type(frozenset))
print(frozenset)

bool = True  # Data Types bool || boolean
print(type(bool))
print(bool)

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









