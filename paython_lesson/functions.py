# Creating a Function
# In Python a function is defined using the def keyword:

def myfun():
    print("hello BItches")
myfun() # calling a function


# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def witharguments(firstname):
    print(firstname + "tharchen")

witharguments("tharchen")
witharguments("1000")
witharguments("sherab")

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def twoargu(fname,lname):
    print(fname+ "fullname: " +lname )

twoargu("dhrtab","tharchen")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

def fuct(*kids):
    print("this are my kids)" + kids[0])

fuct("tharchen","wangmo","tandin")


# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

def keyarg(key1,key2,key3,key4):
    print("the youngest chile is " + key1)
    print("the youngest chile is " + key2)
    print("the youngest chile is " + key3)
    print("the youngest chile is " + key4)

keyarg(key1 = "tharchen", key2 = "sherpa", key3 = "sherab" ,key4 = "bitches")


# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def defaultpara(country ="bhutan"):
    print("i am from: " + country)

defaultpara()
defaultpara("India and this is default parama=eters")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
food = ["apple","mango","gwva"]

def listarg(food):
    for x in food:
        print(x)

listarg(food)


done = [1,2,3,4,5,6,7,8]
def num(done):
    for x in done:
        print(x)
num(done)
# Return Values
# To let a function return a value, use the return statement:

def cal(x):
    return x + x
print(cal(20))
print(cal(200))
print(cal(2000))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a+10
print(x(10))

y = lambda q,e,r : q+e+r
print(y(10,20,30))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def mylambda(n):
   return lambda a : a * n

double = mylambda(2)
print(double(20))

triple = mylambda(20)
print(triple(20))
