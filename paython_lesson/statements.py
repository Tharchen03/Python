# if statement
a = 10
b = 103

if a == b:
    print("a==b")
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
elif a != b:
    print("a != b:") # using Elif
# The else keyword catches anything which isn't caught by the preceding conditions.
else:
    print('this is else')

del a,b 

x = 100
y = 200

# Short Hand If ... Else
print("x == y") if x == y else print('Short Hand If ... Else')

# This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:

print("x == y") if x == y else print('Short Hand If ... Else')if x > y else print('a > y ')

del x,y
# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("The and keyword is a logical operator, and is used to combine conditional statements:")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
if a == b or c > a:
    print("At least one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

if not a == b:
    print('The not keyword is a logical operator, and is used to reverse the result of the conditional statement:')

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x= 100

if x != 50:
    print('x != 50')
    if x > 200:
        print(" x < 200")
    else:
        print("x= 100")

if x == 300:
    pass
del x
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

while i < 7:
    print(i)
    if i == 5:
        break
    i += 1

del i
x = 10

while x < 30:
    print(x)
    if x == 25:
        break
    x += 1
del x

x=0
# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
while x < 6:
  x += 1
  if x == 3 :
      continue
  print(x)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i =1 
while i == 1:
    print(i)
    i +=1
else:
    print("i is no longer less than 6")

del x,i

# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
for x in 'banana':
    print(x)

for x in fruits:
    print(x)
    if x == "banana":
        break
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits1 = ["apple", "cherry1","banana", "cherry"]

for y in fruits1:
    print(y)
    if y == "banana":
        break
    print(y)

del x, y

num = [1,2,3,4,5,6]

for x in num:
    print(x)
    if x == 3:
        continue
    print(x)

for x in fruits:
    print(x)
    if x == "banana":
        continue
    print(x)

del fruits,fruits1,x,

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2,6): # starting fro, 2 to 6
    print(x)
print(" ########")
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("done printing")

print(" ########")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print(x) #If the loop breaks, the else block is not executed.

print(" ########")
# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

lop1 =[1,2,3,4]
lop2 = [5,6,7,8]

for x in lop1:
    for y in lop2:
        print(x,y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

