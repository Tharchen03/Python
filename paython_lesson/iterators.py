# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# for sets of datas
mylist = ("apps","tong","long",5000)
myIterators = iter(mylist)

# next is for the next values

print(next(myIterators))
print(next(myIterators))
print(next(myIterators))
print(next(myIterators))

# for a string
mystring ="tharchen"
stlet = iter(mystring)

print(next(stlet))
print(next(stlet))
print(next(stlet))
print(next(stlet))
print(next(stlet))
print(next(stlet))
print(next(stlet))
print(next(stlet))



# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:

loopsvalue = (1,2,3,4,5,6,7,8)

for x in loopsvalue:
    print(x)

# Iterate the characters of a string: through loop;
stringloop ="sherpa"
for x in stringloop:
    print(x)


# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class num:
    def __iter__(self):
        self.add = 1
        return self
    
    def __next__(self):
        x = self.add
        self.add += 1
        return x
    
num1 = num()
myiter = iter(num1)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


# Stop after 20 iterations:
class x:
    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        if self.a <= 20:
            x =self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
y = x()
itler =iter(y)

for z in itler:
    print(z)



        
        






































