#Write a program to demonstrate the use of positional argument, keyword argument, and default arguments.

#No args
def my_func():
    print("Hello From a function")
my_func()

#Single args
def my_func(fname):
    print(fname)
my_func("sneha")

#Two args
def my_func(fname, lname):
    print(fname, lname)
my_func("Sneha", "Chaudhary")

#keyword args
def my_func(child3, child2, child1):
    print("The Yougest Child is: " +child3)
my_func(child1 = "Sneha", child2 = "Sonu", child3 = "Shanvi")

#Default args
def my_func(country = "India"):
    print("I am from: "+country)
my_func("Canada")
my_func()
my_func("USA")
my_func("UK")

#Output:-
##Hello From a function
##sneha
##Sneha Chaudhary
##The Yougest Child is: Shanvi
##I am from: Canada
##I am from: India
##I am from: USA
##I am from: UK
