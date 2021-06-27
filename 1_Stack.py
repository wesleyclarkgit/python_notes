"""Intro:
Intro and challenges to the following data structures:
- Stacks
- Single Linked Lists
- Circular Linked Lists
- Doubly Linked LIsts
- Arrays
- Binary Trees
- Binary Search trees

Problems and solutions concerning a few algos:
- Binary Search
- Recursion
- String Processing
"""


""" Stack:
Just what it sounds like, a stack of objects.  Imaging a stack of bocks, A on the bottom, then B, C, D on the top.  In order to access A, we have to move books D,C,B.  Then only we can access book A.
Stack Operations:
Push - Insert elements in a stack.  We put the element on the previous top element.  The new item becomes the top element.  We insert the book at the top of the stack.
Pop - Take the top item and put it down.  Removing the element from the stack.  
Peek - View what the top element in the stack is.  It does not remove the top element, but it does return it.

Here's the code of the Stack data structure.  

Create a stack class
Constrictor of the class will initialize a Python list
"""

class Stack():
    def __init__(self):
        self.items = []

# here we defined a variable called items and assigned it to an empty list.  
# self.items is created when we create a stack object so now let's create the push method:

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

# push is a member of this class and it's going to take an item as an argument.  In our previous example, the item is the book.  This push would put the book at the top of the stack.
# append is a built-in method ofr a Python list that adds the item to the end of the list, that's what we want for the Stack in the push method.

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
# there's also a built in pop method into Python that returns the last element inserted into the lst.
    def pop(self):
        return self.items.pop()

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print (myStack.get_stack())
myStack.pop()
print(myStack.get_stack())

""" 
Here we made a method called get_stack() that returns the litems list, which forms the core of the stack.  Then I define the object myStack and push A and B onto the stack.  After these operations I can print my stack.  A is at the bootm, because B was added after A.  After we push C, C will be on top.
"""

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# define the is_empty method that will return whether or not the stack is empty
    def is_empty(self):
        return self.items == []
    # at this point it returns True, because we haven't added anything to the Stack

    def get_stack(self):
        return self.items
        
myStack = Stack()
print(myStack.is_empty())


# let's push something and see if it still returns to False

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())


""" The peek operation tells us what the topmost elment of the stack is
If peek is called, it will return D.peek.
This checks to see if the stack is not empty.  If it isn't it returns the last element of the list, which in this case is the top element of the stack.
self.items[-1] is returned.
"""

"""Determine if Brackets are Balanced:

A balanced set of brackets will look like this
{}
{{}}
{}{}
{{()}}

Unbalanced brackets will look like
(()
{{)}}

Steps to solve:
- We iterate through the string and push the bracket onto the stack if it's an opening bracket
- Wf we get an opening bracket we push it onto the stack
- If we encouter a closing bracket, pop off an element from the stack and match it with the closing bracket.  If it's an opening bracket and of the same type as the closing bracket, we conclude it is a successful match and move on.  If not, we conclude that the brackets are not balanced
- The stack will be empty at the end of iteration for a balanced example of brackets while we'll be left with some leemnts in the stack for the unbalanced example.
"""

def is_paren_balanced(paren_string):
    # declare a stack, s
    s = Stack()
    # declare two variables, is_balanced and index
    is_balanced = True
    index = 0

    # the while loop will execute if the index is less than the length of paren-string and is_balanced is equal to True.  If any of the conditions evaluate to false the program will exit the while loop.
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        # check if paren is any type of opening brackets
        if paren in "([{":
            # if it is, push it to the stack
            s.push(paren)
        else:
            # if it isn't, we check if stack s is empty and set is_balanced to False.
            if s.is_empty():
                is_balanced = False
                break
            else:
                # if the stack is not empty, we pop off the top element and check if the current paren matches the type of the top element which is supposed to be an opening bracket.
                top = s.pop()
                if not is_match(top, paren):
                    # if the types dont match, we update is_balanced to False
                    is_balanced = False
                    break
            
            # increment the index for the next iteration.  The while loop keeps executing until the index is equal to or greater than the length of paren_string or is_balanced equals False.
            index += 1

        if s.is_empty() and is_balanced:
            return True
        else:
            return False


# next lets implement the is_match function()

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 =="{" and p2 =="}":
        return True
    elif p1 == "[" and p2 =="]":
        return True
    else:
        return False

"""The is_match function takes in two characters as p1 and p2 and evaluates whether they are a valid pair of brackets.  For p1 and p2 to match, p1 has to be an opening bracket while p2 has to be the corresponding closing bracket.  If p1 and p2 don't fall in any of the valid conditions we return False.
"""
# full implementation:
from stack import Stack

def is_match(p1, p2):
if p1 =="(" and p2 ==")":
    return True
elif p1 =="{" and p2 =="}":
    return True
elif p1 =="[" and p2 =="]":
    return True
else:
    return False

def is_paren_balenced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balance = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String: ((({}))) Balanced or not?")
print(is_paren_balanced("((({})))"))

print ("String: [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]")

print "String : [][] Balanced or not?"
print(is_paren_balanced("[][]"))



from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))


"""Reverse String:  Let's learn how to reverse a string using a stack in Python
"""

# in Python it's easy
input_str = "Wes is learning"
print(input_str[::-1])

# it can also be done using a stack, but is different

"""Steps:
Input a string into a variable
Put the first character of the string onto the stack
Push the next one, and the next until there are no more
Initialize the reverse string.

In short, we push all the characters of the string onto the stack and due to First-In, Last-Out property of a stack, we get all the characters in reverse order when we pop them off the stack

"""

from stack import Stack
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

stack = Stack()
input_str = "gninrael si seW"
print(reverse_string(stack, input_str))

""" The for loop iterates over input_str and pushes each character on to stack.  Then we initialize rev_str as an empty string.  We pop off all the elements from the stack and append them to rev_str one by one until the stack becomes empty and terminates the while loop.  We then return rev_str
"""


"""Exercise, Convert Decimal Integer to Binary:
Use the stack data structure to convert integer values to their binary equivalent.

- Divide the number by two
- Extract the non-fractional part from the answer
- Record the remainder from the division
- Keep dividing the answer from the previous calculation by two until you reach zero and keep recording the remainders

242/2 = 121 --> 0
121/2 = 60 --> 1
60/2 = 30 --> 0
30/2 = 15 --> 0
15/2 = 7 --> 1
7/2 = 3 --> 1
3/2 = 1 --> 1
1/2 = 0 --> 1

The binary equivalent of 232 is 11110010
"""

# build the solution based on division by 2 method

from stack import Stack
def convert_int_to_bin(dec_num):
    
    # cater to the edge case of dec_num equaling 0
    if dec_num == 0:
        return 0

    # declare a stack
    s = Stack()
    
    # create a while loop which executes if dec_num is greater than 0
    while dec_num > 0:
        # create a variable, remainder, and use modulo to calculate it
        remainder = dec_num % 2
        # push the remainder number to a stack
        s.push(remainder)
        # change the dec_num do be whatever it is using floor division divided by 2
        dec_num = dec_num //2

    # declare bin_num as an empty string
    bin_num = ""
    # create a while loop to execute if the stack is not empty
    while not s.is_empty():
        # create the variable bin_num, and pop elements from s until it becomes empty and the while loop is terminated
        bin_num += str(s.pop())

    return bin_num

