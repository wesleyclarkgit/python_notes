"""2: Merge two sorted lists
Given two sorted lists, merge them into one list whic should also be sorted.

Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.  Name it merge_lists(1st1, 1st2)
"""
"""Need to know more about linked lists before solving this one!"""


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

def new_sorted_list(list1, list2):
    for item in list1, list2:
        if item < 