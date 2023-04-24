# Python Scope
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


def myfunc():
  x = 300
  print(x)

myfunc()

# The local variable can be accessed from a function within the function:
def myfunc():
  x = "myass its local scope being used in fun insidr=e fun()"
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

x = "global variable"

def myfunc():
  print(x)

myfunc()

print(x)

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.


def myfunc():
  global xx
  xx = "making it global"

myfunc()

print(xx)










































