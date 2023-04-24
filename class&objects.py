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


# parent  child class
class sherab:
    def __init__(self,name,age): # parent
        self.name = name
        self.age =age

    def parent_child(self): # child
        print(self.name, self.age)
        


x = sherab("tharchen",50)
print(x.name)
print(x.age)

x.parent_child()

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x1 = Student("Mike", "Olsen")
x1.printname()

        
# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class superclass:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
    
    def output(self):
        print(self.brand, self.model)

class names(superclass):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        # self.properyyes = 20003

x2 = names("Mustang","100 cc")
x2.output()
# print(x.properyyes)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
# Add Properties
del superclass,x,names



# In the given code, an instance x of the superclass is created with the arguments "Mustang" and "100 cc". However, the superclass does not have a property named properyyes. This property is only defined in the subclass names. Therefore, the code will raise an attribute error when we try to access the properyyes property on the x object of superclass.
# To fix this, we need to create an instance of the names subclass instead of superclass if we want to access the properyyes property.
# Here's an updated code that should work as intended:

class superclass:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def output(self):
        print(self.brand, self.model)

class names(superclass):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.properyyes = 20003

x1 = names("Mustang", "100 cc")
x1.output()
print(x1.properyyes)

# Add Methods
# Add a method called welcome to the Student class:

class athang:
    def __init__(self,date,pie):
        self.date = date
        self.pie = pie
    
    def printu(self):
        print(self.date ,self.pie)

class tharchen(athang):
    def __init__(self, date, pie):
        super().__init__(date, pie)
        self.addnew = 2000000
    
    def welcome(self):
        print("hi: ",self.date, "class of :    ",self.pie, "count",self.addnew)

ad = tharchen("1/1/1 ", "tharchen")
ad.welcome()
    
    
