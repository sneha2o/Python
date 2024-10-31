#Write a program to use class method to handle the common features of all the instance of student class.

class student:
    dept = 'bca'

    @classmethod

    def display(cls, r, n):
        cls.roll = r
        cls.name = n

        print(cls.roll) 
        print(cls.name)
        print(cls.dept)

s1 = student()
s1.display(10, 'Shiva')
#OR
student.display(20, 'Parvati')

#Output:-
##10
##Shiva
##bca
##20
##Parvati
##bca

        


        
