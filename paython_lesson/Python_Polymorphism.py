# Python Polymorphism

# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.
# String
# For strings len() returns the number of characters:
x = "hit tharchen"
print(len(x))

xx =(1,2,3,4,5,6,7)
print(len(xx))
print(type(xx))



# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():


class car:
    def __init__(self,brand,name):
        self.brand =brand
        self.name =name

    def move(self):
        print("drive")
    
class boat:
    def __init__(self,brand,name):
        self.brand =brand
        self.name = name

    def move(self):
        print("boat")

class plane:
    def __init__(self,brand,name):
        self.brand =brand
        self.name = name

    def move(self):
        print("plane")


car1 = car("mustang","tharchen")
boat1 = boat("mustang","tharchen")
plane1 = plane("mustang","tharchen")

for x in (car1,boat1,plane1):
    x.move()

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.name)
    x.move()

        
# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class vechile:
    def __init__(self,brand,name):
        self.brand =brand
        self.name =name

    def move(self):
        print("drive")

class cars(vechile):
    pass

class boatt(vechile):
    def move(self):
        print("water")

class plannes(vechile):
     def move(self):
        print("sky")

cars1 = cars("mustang",9000)
boatt1 = boatt("badang",9000)
plannes1 = plannes("plannes",9000)

for x in (cars1,boatt1,plannes1):
    print(x.brand)
    print(x.name)
    x.move()















