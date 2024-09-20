#Write a program to find out and display the common and Non common elements in the list using membership operators.

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,33,4,88,99,7]

c = []
nc = []
for a in l1:
    if(a in l2):
        c.append(a)
    else:
        nc.append(a)
print("Common elements are: ", c)
print("Non Common elements are: ", nc)

#output:-
##Common elements are:  [1, 2, 4, 7]
##Non Common elements are:  [3, 5, 6]




















