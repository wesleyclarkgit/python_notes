"""Procedural Programming:

A programming paradigmn in which a program is divided into smaller parts called methods.  These methods are the basic entities used to construct a program.  One of the main advantages of procedural programming is code reusability, however implementation in complex problems becomes difficult and unnecessarily complex.

This is what gave rise to Object-Oriented Programming
OOP: a programming paradigm that includes or relies on the concept of classes and objects.  The basic idea of OOP is to divide sophisticated programs into a bunch of objects that talk to each other.

Anatomy of Objects and Classes:
Objects may contain data in the form of fields(variables) and methods to operate on that data.  For example, a light bult could be an object.  It has a state(on/off), beahavior(when you turn it on, it lights up).  Basically objects are a collection of data and their beahviors.

Objects come from a Class.  A class can be thought of as a blueprint for creating objects.
Going back to the bulb example

Class Bulb
    - State Bulb
        - onOff
    - Behavior of Bulb
        turnOn()
        turnOff()
Objects are generally modeled using variables in a class, and the behavior is modeled using methods.
There can be many objects of the same class.  Each can be in an independent state, but they all share the same behavior and characteristics


User-Defined Data Types:  We can infer from above that classes are user-defined data types implemented using primitive data types(boolean, int, char).  User-defined data types

can encapsulate state and its behaviors into a unit.
"""

"""Indtroduction: Objects and Classes
We can see objects everywhere in our surroundings.  In the example of a company employee, an employee has the following attributes
- ID
- Salary
- Department
The following actions or beahaviors can be performed on an employee
- Calculation of tax on salary
- Calculation of saray per day

In a company each worker has a different name, salary and department but the type of each worker is employee.  SO there is a generic blueprint for each worker in the company, but each of them has different attributes associated with them.
Having the same blueprint but different properties is the basis for classes and objects!

Suppose in a company there are two employees, Mark and Chris.  

Mark 
- ID: 72655
- Salary: 3000
- Department: Software
Chris
- ID: 72644
- Salary: 4000
- Department: Marketing

Properties(aka attributes) in this example are ID, Salary, Department.
Methods are tax(), salaryPerDay()

Properties are variables that contain information regarding the object of a class.  New properties could be added to be a part of an object of the employee class.  Behaviors are sometimes referred to as member functions, or methods.  Let's call them methods for now.

Methods are like functions that have access to properties of a class.  Methods can accept parameters and return values.  They are used to perform an action on an object of a class.  

Benefits of Objects and Classes:
- Instrumental in compartmentalizing code.  Different components can become separate classes which would interact through interfaces.  These ready-made components will also be available for use in future applications
- The use of classes makes it easier to maintain different parts of an application since it is easier to make changes in classes.
"""

"""Declaring a class: 
class keyword tells the compiler that wer are creating a custom class followed by :
Naming rules: 
- Must start with a letter or underscore
- Should only be comprised of numbers, letters or underscores
"""
class ClassName:
    pass

# The name of the class, MyClass will be used to instantiate an object of the class in our main program.  We can create an object of a class by simply using the name of the class followed by a pair of parenthesis.  

class MyClass:
    pass

obj = MyClass() # creating a MyClass object
print(obj)

# Output
# 0.93s
# <__main__.MyClass object at 0x7f073731e940>

# printing this object showed us the memory address at which the object is stored.


"""Implementing Properties in a Class:
Let's implement the Employee class illustrated below:
Start by adding the properties of the class and extend it by adding methods to it
Properties: ID, salar, department
Method: 
"""

class Employee:
    # define the properties and assign them to None for now
    ID = None
    salar = None
    department = None

# We defined three properties as class variables; ID, salary and department for the class employee.
# Note that if you do not initialize the values of properties the Python code will not compile.  Initializing the values of properties inside the class is necessary  

# This code won't work, because we haven't initialized the values of properties.  
class Employee:
    ID
    salary
    department
    # errrorrrrr hellpppp me compile by initializing these properties with valuessssszzzz

"""Accessing Properties and Assigning Values
To access properties of an object dot notation is used

object.property

Two ways to assign values to properties of a class
- Assign values when defining the class
- Assign values in the main code
"""

# initializing

class Employee:
    # define the properties and assign values to them
    ID = 3789
    salary = 2500
    department = "Human Resources"

# creating an object of the Employee class
Steve = Employee()

# printing the properties of Steve - an object of the Employee class
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)



# assigning
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None

# creating an object of the Employee class
Steve = Employee()

# assigning values to the properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department", Steve.department)


"""PPython provides the user with a feature that most languages do not, creating properties of an object outside the class.  Let's see an example of this by extending the example of the Employee class we discussed above:
"""

# add the title: Manager to Steve

class Employee:
    ID = None
    salary = None
    department = None

# creating an object of the employee class
Steve = Employee()

# assign values to properties of Steve
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# look how easy it is to add a new property and assign it!!  Awwww yeah.
Steve.title = "Manager"


"""Initializers: Initializer is used to initialize an object of a class.  It's a special method that outlines the steps that are performed when an object of a class is created in the program.  It's used to define and assign values to instance variables.

The initialization method has a predefined name, __init__
The double underscores mean that this is a special method that Python interpreter will treat as a special case
The initializer is a special method because it does not have a return type.  The first parameter of __init__ is self, which is a way to refer to the object being initialized.
"""

# Defining Initializers:
class Employee:
    # defining the properties and assigning them to None
    def __init__(self, ID, Salary, department):
        self.ID = ID
        self.salary = salary
        self.department = deaprtment

# create an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)

"""The initializer is automatically called when an object of the class is created.  Now that we will be using initializers to make objects, its a good practice to initialize all of the object properties when defining the intializer.

It is important to define the initializer with complete parameters to avoid any errors.  Similar to methods, initializers also have the provision for optional parameters.
When defining an initializer with optional parameters, it's essentiaal to assign default values to the properties.  You can also have a default intializer that has all properties as optional.  In this case, all the new objects will be created using the properties intialized in the initializer definition.
"""

# example of one Employee class object created without parameters and one with parameters

class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

# create an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")


"""Class and Instance Variables:  Let's learn about instance and class variables!

In Python properties can be defined into two parts
- class variables
    - The class variables are shared by all instances or objects of the classes.  A change in the class variable will change the value of that property in all the objects of the class
- instance variables
    - Instance variables are unique to each instance or object of the class.  A change in the instance variable will change the value of the property in that specific object only.
"""

class Player:
    teamName = 'Liverpool' # class variable
    
    def __init__(self, name):
        self.name = name # creating instance variable

p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)

# careful when using class variables!!  They must be assigned properly since they are shared by all the class objects and can be modified using any one of them.

# if we use class variables well they can be quite useful:

class Player:
    teamName = 'Liverpool' # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name # instance variable
        self.formerTeams = []
        self.teamMembers.append(self.name)

p1 = Player('Mark')
p2 = Player('Steve')
print("Name:", p1.name)
print("Team Members:")
print("p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)

"""Here's what we did up there ^^
- Defined a class variable teamMembers, which is a list that will be shared by all the objects of the class Player
- This list, teamMembers, will contain names of all the instances created of the Player class
- Whenever a new object is created its name is appended in teamMembers
teamMembers is accessed by p1 and p2 respectively and both produce the same output
"""


"""Implementing Methods in a Class: Get to know more about the role of methods in classes and what method overloading is
Three types of methods in Python
- instance methods
- class methods
- static methods

We'll be discussing instance methods since they are the most used in Python.  Instance are often just referred to as methods since they are so much more common than class/static

Methods act as an interface between a program and the properties of a class in the program.  These methods can either alter the contents of the properties or use their values to perform a particular computation

 Definition and Declaration: A method is a group of statements that performs some operations and may or may not return a result.
 Method parameters make it possible to pass values to the method.  In Python, the first parameter of the method should ALWAYS be self, and is followed by the remaining parameters
 Return Statement: makes it possible to get the value from the method
 The return statement must be immediately followed by the return value

 The self Argument: One of the major differences between functions and methods in Python is the first argument in the method definition.  Conventionally, this is named self.  The user can use different names as well, but self is used by almost all devs working in Python.  We will be using this convention for ease of understanding.

 This pseudo-variable provides a reference to the calling object that is the object to which the method or property belongs to.  If the user does not mention the self as the first argument, the parameter will be treated for reference to the other object.

 """

 # Here's an example of implementing methods in a class:

 class Employee:
     # define the initializer
     def __init__(self, ID=None, salary=None, department=None):
         self.ID = ID
         self.salary = salary
         self.department = department

        def tax(self):
            return(self.salary * .2)

        def salaryPerDay(self):
            return(self.salary/30)

# initialize an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# print properties of Steve
print("ID = ", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())