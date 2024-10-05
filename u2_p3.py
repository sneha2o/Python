#Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.

from array import *

a = array('i', [1,2,3,4,5,6,7,8])

print("Full array: ")
for i in range(5):
    print(a[i])

a.append(9)
print(a)

a.insert(2,22)
print(a)

a.pop(2)
print(a)

a.remove(5)
print(a)

x = a.index(6)
print(x)

x = a.count(1)
print(x)

x = a.tolist()
print(x)

#Output:-
##Full array: 
##1
##2
##3
##4
##5
##array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
##array('i', [1, 2, 22, 3, 4, 5, 6, 7, 8, 9])
##array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
##array('i', [1, 2, 3, 4, 6, 7, 8, 9])
##4
##1
##[1, 2, 3, 4, 6, 7, 8, 9]
