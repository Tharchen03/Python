# To make sure a string will display as expected, we can format the result with the format() method.
# String format()
# The format() method allows you to format selected parts of a string.
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method

price = 550
txt = "this is the price string format method {}"
#output in terms of decimals
txt1 = "this is the price string format method {:.2f}"
print(txt.format(price))
print(txt1.format(price))
amount = int(input("enter a amount"))
output = "this is string format {}"

print(output.format(amount))

# Syntax
# string.format(value1, value2...)holder

# na named index
namedIndex = 'this is {Name} . and i am {age}'.format(Name ="Tharchen",age = 22)
print(namedIndex)

# indexing 0,1,2,3,4 2 placeholder
indexing = 'this is indexing {0}. this is indexing {1}'.format("therchen","sherpa")
print(indexing)

# empty placeholder
empty = "this is empty placeholder {}, okai {:g}".format("tharchen",2003)
print(empty)

# Multiple Values
# If you want to use more values, just add more values to the format() method:

brand = "mustang GT"
model = 2003
country = "bhttan"

statement = "this is my fravouite brand {0}. modeled {1} by the country {2}"
print(statement.format(brand,model,country))


BrandName = input('name a luxariy brand of your own choice')
modelName = int(input('enter a modelname in terms of yearing'))

inputPrint = 'this is the luxary brand {0} moodeled {1}'
print(inputPrint.format(BrandName,modelName))


brandindexed = "my name is {name} and i am from year {year}".format(name = input("enter ur name: "), year = int(input("enter a year: ")) )
print(brandindexed)













