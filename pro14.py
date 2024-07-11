# Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays.


import array as arr

a = arr.array('i', [1,2,3,4,5])
print(a) #Display array

a[0] = 7 #Update array using indexing
print(a) 

a [0:2] = arr.array('i', [8,9]) #update array using slicing
print(a)

# output:-
# array('i', [1, 2, 3, 4, 5])
# array('i', [7, 2, 3, 4, 5])
# array('i', [8, 9, 3, 4, 5])