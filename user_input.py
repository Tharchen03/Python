# User Input
# Python allows for user input.
# That means we are able to ask the user for input.
# The method is a bit different in Python 3.6 than Python 2.7.


#The following example asks for the username, and when you entered the username, it gets printed on the screen:

# Python 2.7 uses the raw_input() method.
# variable = raw_input()
# but this is not working
# Python 3.6 uses the input() method.

username = input("UR username ")
print("username  " +username)


print("   my form   ")
# age = input("ur age: ")
age = int(input("ur age: "))
adress = input("ur adress: ")

if type(age) is int:
    print("Username: " + username)
    print("age is int")
    print("Age: " +str(age))
    print("adress: " +adress)
    
else:
    print("not int")


num = input("what operation u want to do: ")



a = int(input("1st num: "))
b = int(input("2nd num: "))

if num == "add":
    sum1 = a+b
    print("sum: " +str(sum1))
elif num == "sub":
    sub = a-b
    print("sub: " +str(sub))
elif num == "div":
    div = a/b
    print("div: " +str(div))
elif num == "mul":
    mul = a*b
    print("mul: "+str(mul))
else:
    print("invalid")



