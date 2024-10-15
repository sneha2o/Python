#Write a program to create Student class with a constructor having more than one parameter.

class student():
    def __init__(self, nm = '.', ag = 20, m = 0):
        self.name = nm
        self.age = ag
        self.marks = m

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

s1 = student('sneha', 21, 80)
s1.display()

s1 = student('kishu')
s1.display()

#Output:-
##Name:  sneha
##Age:  21
##Marks:  80
##Name:  kishu
##Age:  20
##Marks:  0
