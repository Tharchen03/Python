# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
f1 = open("demofile.txt" , 'r')

f = open('demofile.txt','rt')
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:

print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

print(f1.read(8))
f.close()
# Read Lines
# You can return one line by using the readline() method:
line = open('demofile.txt','r')
print(line.readline())

# By calling readline() two times, you can read the two first lines:
print(line.readline())
line.close()

# By looping through the lines of the file, you can read the whole file, line by line:
gt = open('file.txt','r')
for x in gt:
    print(x)

# Close Files
# It is a good practice to always close the file when you are done with it.
gt.close()

# Python File Write
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
wt = open('file.txt','a')
wt.write("adding the content through write function")
wt.close()

#open and read the file after the appending:
wt = open('file.txt','r')
print(wt.read())

# Note: the "w" method will overwrite the entire file.
overwrite = open('demofile.txt','w')
overwrite.write('entire file gets overwrite')
overwrite.close()

overwrite = open('demofile.txt','r')
print(overwrite.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt":
# new = open('myfile.txt','x')


# Create a new file if it does not exist:
ct = open("myfile1.txt",'w')
ct.close()

# # Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove('myfile1.txt')

dt = open('tharchen.txt','w')
dt.close()

os.remove('tharchen.txt')

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists('tharchen.txt'):
    os.remove('tharchen.txt')
else:
    print('Invalid')
    
# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# os.rmdir('tharchen')

if os.path.exists('tharchen'):
    os.rmdir('tharchen')
else:
    print('invalid, folder already deleted')























