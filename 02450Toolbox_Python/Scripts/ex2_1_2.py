# exercise 2.1.2

from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show

# Imports the numpy and xlrd package, then runs the ex2_1_1 code
from ex2_1_1 import *

# (requires data structures from ex. 2.1.1)

# Data attributes to be plotted
i = 2
j = 1

# Make a simple plot of the ith attribute against the jth attribute
# Notice that X is of matrix type (but it will also work with a numpy array)
# X = np.array(X) #Try to uncomment this line
plot(X[:, i], X[:, j], 'o')

# %%
# Make another more fancy plot that includes legend, class labels, 
# attribute names, and a title.
f = figure()
title('NanoNose data')

for c in range(C):
    # select indices belonging to class c:
    class_mask = y == c
    plot(X[class_mask, i], X[class_mask, j], 'o', alpha=.3)

legend(classNames)
xlabel(attributeNames[i])
ylabel(attributeNames[j])

# Output result to screen
show()
print('Ran Exercise 2.1.2')
