cras = ["BMW", "GTX", "Mustang", "lambgo"]

# indexing
print(cras[0])
x = cras[2]
print(x)

# modifying
cras[0] = "testlea"
print(cras)

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
y = len(cras)
print(y)

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.

for x in cras:
    print(x)


# Adding Array Elements
# You can use the append() method to add an element to an array.

cras.append("new car")
print(cras)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cras.pop()
print(cras)

# with index
cras.pop(1)
print(cras)

# You can also use the remove() method to remove an element from the array.
cras.remove("lambgo")
print(cras)

# Sorts the list
cras.sort()
print(cras)
