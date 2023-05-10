import re

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# RegEx Modul
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:

txt = "my name is tharchen"
# Search the string to see if it starts with "The" and ends with "Spain":

x = re.search("^my.*tharchen$", txt)

if x:
    print("yes")
else:
    print('no')

# The findall() Function
# The findall() function returns a list containing all matches.

y = re.findall("a" ,txt)
print(y)

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

txt1 = 'a quisck brown fox jump over the lazy dog'

s1 = re.search('\s', txt1)

print("The first white-space character is located in position:", s1.start())

# Make a search that returns no match:

nomat = re.search("tharchen",txt1)
print(nomat)
# or using statements using my own logic
if nomat:
    print("matches")
else:
    print("no matches")


# The split() Function
# The split() function returns a list where the string has been split at each match:

#Split the string at every white-space character:
splitexp = re.split("\s",txt1)
print(splitexp)

# Split the string only at the first occurrence:
splitexp1 = re.split("\s", txt1, 1)
print(splitexp1)


# The sub() Function
# The sub() function replaces the matches with the text of your choice:

subfnc = re.sub("a", "fk",txt1)
print(subfnc)

# Replace every white-space character with the number 9:
subfnc1 = re.sub("\s","9",txt1)
print(subfnc1)

# Replace the first 2 occurrences:
subfnc2 = re.sub("\s","9",txt1,2)
print(subfnc2)

# Match Object
# A Match Object is an object containing information about the search and the result.


txt2 = "the rain in spain"
math = re.search("ai",txt2)
print(math)


# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

#Search for an upper case "S" character in the beginning of a word, and print its position:
spanx = re.search(r'\bs\w+',txt2)
print(spanx.span())


#The string property returns the search string:
stringx = re.search(r'\bs\w+',txt2)
print(stringx.string)


#Search for an upper case "S" character in the beginning of a word, and print the word:
groupx = re.search(r'\bs\w+',txt2)
print(groupx.group())


































