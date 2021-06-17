"""
Array Notes:

Array is a container which can hold a fixed number of items and these should be of the same type.  Most data structures use arrays to implement their algorithms.

Element - each item stored in an array
Index - each location of an element in an array has a numerical index

Basic operations supported by an array:
Traverse - print all the array elements one by one
Insertion - add an element at the given index
Deletion - delete the element at a given index
Search - search an element at the given index or by the value
Update - update an element at the given syntax

from array import *
arrayName = array(typecode,[initializers])

array1 = array('i', [10,20,30,40,50])
for x in array1:
    print(x)
"""

""" Insertion Operation:  Insert operation is to insert one or more data elements into an array.  Based on the requirement, a new element can be added at the beginning, end or any given index of an array.

"""
from array import * 
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
    print(x)


"""Deletion Operation:  Deletion refers to removing an existing element from the array and reorganizing all the elements of an array.  Here we remove a data element using built in remove() method
"""

from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
    print(x)


""" Search operation:
You can perform a search of an array element based on its value or its index.  here we search using built-in index() method
"""

from array import *
array1 = array('i',[10,20,30,40,50])

print(array1.index(40))


"""Update Operation:
Update an existing element from the array at a given index.  Reassign a new value to the desired one
"""

from array import *
array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
    print(x)