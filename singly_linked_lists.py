"""
Singly Linked Lists:
Structure

Every linked list consists of nodes, which has 2 components.  Data, Next.
- Data allows a node in the linked list to store an element of data that can be of type string, character, number, or any other type of object.
- The next component is a pointer that points from one node to another.

The start of a linked list is the head
The last component of a linked list is null which translates into None in Python.
"""

"""Insertion/Deletion:
The insertion/deletion operation is in O(n) operations for insertion/deletion of value at the beginning of the array.  Imagine we are given a value at the beginning of the arraay.  To insert it we have to shift all the elements in the array to the right to make room for the element to be inserted.  Same goes for deleting an element from the beginning.  Again we have to shift all elements back by one index.  This is what makes it O(n) time complexity.

Inserting a node at the head of a linked list given the head node is a constant-time operation as we need to change the orientation of a few pointers.  If we are given the exact pointer after which we have to insert another node, it will be a constant-time operation.

Accessing any element in an index in arrays is constant time.  If a given array is at an index, it can immediately give you the element at which the entry is stored.  This is because arrays are contiguous.

Accessing an nth element in a linked list is a O(n) operation because you have to access the head node of the linked list.  