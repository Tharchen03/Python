import mymodule

mymodule.greatting("tharchen")
mymodule.greatting("kmc")

x  = mymodule.person1["name"]
print(x)

ab1 = dir(mymodule)
print(ab1)
# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
import mymodule as rename

z = rename.person1["age"]
print(z)

ab = dir(rename)
print(ab)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

import platform
# prints operating system
deft =  platform.system()
print(deft)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
funt = dir(platform)
# print(funt)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from mymodule import person1
print(person1['name'])


# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)


import datetime

d2 = datetime.datetime.now()

print(d2)


# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter:

print(d2.year)

print(x.strftime('%A'))


# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

import datetime

dateobject = datetime.datetime(2023,5,30)

print(dateobject)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:



print(dateobject.strftime('%B'))



































