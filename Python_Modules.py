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







































