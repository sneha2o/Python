#Write a program to access the base class constructor from a sub class by using super() method and also without using super() method.
#Using super method.
class class1():
    def __init__(self):
        print("Hello Sneha.")

class subclass(class1):
    def __init__(self):
        print("Good Morning")

        super().__init__()

s1 = subclass()

#Output:-
##Good Morning
##Hello Sneha.

#without using super method.

class bca():
    def __init__(self):
        print("Hello")

class subclass(bca):
    def __init__(self):
        print("World")

        bca.__init__(self)

s1 = subclass()

#Output:-
##World
##Hello
