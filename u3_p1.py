#Write a program to create a Student class with name, age and marks as data members.
#Also create a method named display() to view the student details.
#Create an object to Student class and call the method using the object.

class student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)

s1 = student('sneha', 20, 79)
s1.display()

#Output:-
#sneha 20 79

    
