#Write a program to implement single inheritance in which two sub classes are derived from a single base class.

class A:
    p1 = "Hello class A"

class B(A):
    p2 = "Hello class B"

class C(A):
    p3 = "Hello class C"

b1 = B()
print(b1.p1)

c1 = C()
print(c1.p1)

#Output:-
##Hello class A
##Hello class A


class A:
    def display1(self):
        print("Hello")
class B(A):
    def display2(self):
        print("World")
class C(A):
    def display3(self):
        print("Have a nice day...!")

b1 = B()
b1.display1()
b1.display2()

c1 = C()
c1.display1()
c1.display3()

#Output:-
##Hello class A
##Hello class A
##Hello
##World
##Hello
##Have a nice day...!
