#Create a program to display memory locations of two variables using id() function, and than use identity operators compare where two objects are same or not.

a = 10
b = 20
print("Memory location of a: ", id(a))
print("Momory location of b: ", id(b))

if(a is b):
    print("a & b have same identity.")
else:
    print("a & b do not have same identity.")

#output: -
##Memory location of a:  140712335391448
##Momory location of b:  140712335391768
##a & b do not have same identity.
