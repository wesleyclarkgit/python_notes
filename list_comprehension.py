# notes from a list comprehension video from Socratica:  https://www.youtube.com/watch?v=AhSvKGTh28Q


list = [1, 2, 'a', 3.14]

# List comprehensions are a more succing way of iterating over lists, as opposed to creating for loops

# here's the old way

# create an empty list
list2 = []

# set up a for loop
for i in range(5):
    # add items to the list one by one
    list2.append(i)

print(list2)


# list comprehensions allow this to be done in a single line
# [expression for value in collection]
# [ expression for value in collection if <test>]
# [ expression for value in collection if clause1 and if clause 2]
# [ expression for value1 in collection 1 and value2 in collection2]

squares = []
for i in range(1, 101):
    squares.append(i**2)

# same thing using list comprehension
squares2 = [i**2 for i in range(1,101)]
print(squares2)

# another example
remainders5 = [x**2 % 5 for x in range(1, 101)]

names = ['gary', 'wes', 'patricia', 'jessica', 'spark']
g_names = []
for name in names:
    if name.startswith("g"):
        g_names.append(name)

print(g_names)

list_comp_g_names = [name for name in g_names if name.startswith("g")]
print(list_comp_g_names)