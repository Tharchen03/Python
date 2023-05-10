import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
t = camelcase.CamelCase()

anything = 'hello there my name is tharchen .'
print(t.hump(anything))


# What is Matplotlib?
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

import matplotlib
# print(matplotlib._version_)
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
import sys

xaxis = np.array([0,6])
yaxis = np.array([0,250])

plt.plot(xaxis,yaxis)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()












































