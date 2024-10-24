#Write a program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.

class student:
    def __init__(self):
        self.name = 'Krishna'

    def get_name(self):
        return self.name

    def set_name(self):
        self.name = 'Ram'

s1 = student() 
n = s1.get_name()

print("Before setter method your name is: ",n)

s1.set_name()
print("After setter mrthod your name is: ",s1.name)

#Output:-
##Before setter method your name is:  Krishna
##After setter mrthod your name is:  Ram


