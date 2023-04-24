class classname:
    x = 500 # creating class
objectname = classname() #create object so that class can be read abe
print(objectname.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class person:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    
    def __str__(self,):
        return f'{self.name}({self.age})'


p2 = person("sherabtharchen",19)
p1 = person("tharchen",200)
print(p1.name)
print(p1.age)

print(p2)

# #      The __str__() Function
# # The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:   


#         Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:

class tharchen:
    def __init__(self,num1,stri):
        self.num1 = num1
        self.stri = stri


    def __str__(self):
        return f"{self.num1}({self.stri})"
    


t1 = tharchen(2003,"sheraba")     
t2 =tharchen(2003,"sherpa")

print(t1)
print(t2)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:

class objectfunctions:
    def __init__(self,school,brand):
        self.school = school
        self.brand = brand

    def objfun(self):
        print("school "+self.school)
o1 = objectfunctions("dcs","mustang")
o1.objfun()
        

class suppercar:
    def __init__(self,carname,year):
        self.carname = carname
        self.year = year
    
    def createfunc(self):
        print("car name: " +self.carname + "year: "+ str(self.year) )

sup = suppercar("lambgo",20003)
sup.createfunc()


# Modify Object Properties
# You can modify properties on objects like this:
sup.year = 7000
print(sup.year)

# Delete Objects
# You can delete objects by using the del keyword:

del sup, o1,t1,t2

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

del person,suppercar,objectfunctions,tharchen