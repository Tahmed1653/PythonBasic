"""
Class 
A class is a blueprint for the object 

An object has two characteristics
1. Attributes/Properties 
2. Behaviour/Method

Class syntax:

class classname (object):
    --snip-- 

Creating class object:
objectname= classname(arguments)
"""

class MyClass(object):
    # Document String
    """Ok"""
    a=69

    def MyFunction(self):
        print("Sup")

obj=MyClass()
obj.MyFunction()

print(MyClass.a)
print(MyClass.__doc__)
print(MyClass.__name__)
print(MyClass.__base__)

class GoldenEagle:
    # Class Attribute
    Species="Bird"

    # Instance Attribute
    def __init__(self, n, a):
        print('This is Golden Eagle class')
        self.name=n
        self.age=a 

Hunter=GoldenEagle('Lester', 10)
print(f"{Hunter.name} is a Golden Eagle. He is {Hunter.age} years old")
print(f"Just in case you're retarded, A Golden Eagle is a {Hunter.Species}")
print(Hunter.__class__)
