#Write a program to search the position of an element in an array using index() method of array class.

from array import *

a = array('i', [1,2,3,4,5,6,7,8])

print("Full Array: ")
for i in range(5):
    print(a[i])

b = a.index(7)
print("Position of an element: ",b)

#Output:-
##Full Array: 
##1
##2
##3
##4
##5
##Position of an element:  6
