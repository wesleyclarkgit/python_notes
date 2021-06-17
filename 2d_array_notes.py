"""
Two dimensional arrays are an array within an array.  It's an array of arrays.  In this type of array the position of a data element is referred to two brackets instead of one.  It represents a table with rows of columns of data.

Imagine recording the temperature 4 times a day

Day 1 - 11, 12, 5, 2
Day 2 - 15, 6, 10
Day 3 - 10, 8, 12, 5
Day 4 - 12, 15, 8, 6
"""

T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]


"""Accessing elements in a 2d array:  """

from array import *

T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(T[0])

print(T[1][2])

# to print the entire array use a loop

from array import *
T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

for r in T:
    for c in r:
        print(c, end = " ")
    print()


"""Inserting values in a 2d array:  use the insert() method and specify the index"""

from array import *

T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
T.insert(2, [0,5,11,13,6])

for r in T:
    for c in r:
        print(c, end = " ")
    print()


""" You can also update specific elements in an array instead of the entire one"""

from array import *

T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c, end = " ")
    print()


"""Deleting values in a 2d array:
"""

T = [[11,12,5,2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

del T[3]

for r in T:
    for c in r:
        print(c, end = " ")
    print()
