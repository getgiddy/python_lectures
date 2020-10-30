'''
Object-oriented programming (OOP) is a programming paradigm that provides
a means of structuring a program so that related properties and 
behaviors are bundled into individual objects.

~ Goals:
    - Create a class, which is like a blueprint for creating an object
    - Use classes to create new objects
    - Model systems with class inheritance

~ Classes VS Instances/Objects:

Classes are used to create user-defined data structures. Classes define
functions called methods, which identify the behaviors and actions that
an object created from the class can perform with its data.

While the class is the blueprint, an instance is an object that is built
from a class and contains real data.

Put another way, a class is like a form or questionnaire. An instance is
like a form that has been filled out with information. Just like many
people can fill out the same form with their own unique information, 
many instances can be created from a single class.

~ An object has two characteristics:
    - attributes
    - behavior

~ Define a class:
>>> class Dog:
...    pass

The properties that all Dog objects must have are defined in a method 
called .__init__(). Every time a new Dog object is created, .__init__()
sets the initial state of the object by assigning the values of the 
object’s properties. That is, .__init__() initializes each new instance
of the class.

You can give .__init__() any number of parameters, but the first parameter
will always be a variable called self. When a new class instance is created,
the instance is automatically passed to the self parameter in .__init__() 
so that new attributes can be defined on the object.

>>> class Dog:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age

Attributes created in .__init__() are called instance attributes. An instance
attribute’s value is specific to a particular instance of the class. 
All Dog objects have a name and an age, but the values for the name and age 
attributes will vary depending on the Dog instance.

On the other hand, class attributes are attributes that have the same value 
for all class instances. You can define a class attribute by assigning a 
value to a variable name outside of .__init__().

>>> class Dog:
...     # Class attribute
...     species = "Canis familiaris"

...     def __init__(self, name, age):
...         self.name = name
...         self.age = age

Use class attributes to define properties that should have the same value
for every class instance. Use instance attributes for properties that vary
from one instance to another.

~ Instantiating classes ( creating objects )
~ Instance methods
~ __str__() method

############################################################################

~ Exercise
Create a Car class with two instance attributes:

    - .color, which stores the name of the car’s color as a string
    - .mileage, which stores the number of miles on the car as an integer

Then instantiate two Car objects—a blue car with 20,000 miles and a red car
with 30,000 miles—and print out their colors and mileage. Your output should
look like this:

    The blue car has 20,000 miles.
    The red car has 30,000 miles.

############################################################################

~ Inheritance
Inheritance is the process by which one class takes on the attributes and
methods of another. Newly formed classes are called child classes, and the
classes that child classes are derived from are called parent classes.

Child classes can override or extend the attributes and methods of parent
classes. In other words, child classes inherit all of the parent’s attributes
and methods but can also specify attributes and methods that are unique to
themselves.

~ Parent Classes vs Child Classes
~ isinstance()
~ Extending the functionality of a parent class:
To override a method defined on the parent class, you define a method with
the same name on the child class. 

One thing to keep in mind about class inheritance is that changes to the 
parent class automatically propagate to child classes. This occurs as long
as the attribute or method being changed isn’t overridden in the child class.

~ super()



'''