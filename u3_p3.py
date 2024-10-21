#Write a program to demonstrate the use of instance and class/static variables.

class student():
    dept = 'BCA'
    def __init__(self, r, n):
        self.roll = r
        self.name = n

s1 = student(10, 'vashu')

print("Roll no is: ",s1.roll)
print("Name is: ",s1.name)
print("Department is: ",s1.dept)
#OR
print(student.dept)

#Output:-
##Roll no is:  10
##Name is:  vashu
##Department is:  BCA
##BCA
