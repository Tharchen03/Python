# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
    print(x)
except:
    print("undefined")
# The try block will generate an exception, because x is not defined:

try:
    print(tharchen)
except NameError:
    print("NameError")
except:
    print("error")
# Print one message if the try block raises a NameError and another for other errors:

# else
try:
    print("hellow bitches")
except:
    print("anything else")
else:
    print("You can use the else keyword to define a block of code to be executed if no errors were raised:")
# You can use the else keyword to define a block of code to be executed if no errors were raised:


# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print("finally")
except:
    print("on going argument which goes to end only using finally")
finally:
    print("The 'try except' is finished")

# This can be useful to close objects and clean up resources:
try: 
    x = open('txt.txt')
    try:
        x.write('tharchen sherpa')
    except:
        print("smth went wrong")
    finally:
        print("this is finally man")
except:
    print("this is try except method gi bay")
# Try to open and write to a file that is not writable:

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

# y = 9
# if y != 10:
#     raise Exception("this is exception method")

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# Raise a TypeError if  is not a variablean integer:
num = "string"
if not type(num) is int:
    raise TypeError("this is typeerror")



























