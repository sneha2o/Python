#Write a program to implement multiple inheritance using two base classes.

class A:
    demo1 = 10
    def fun1(self):
        print(self.demo1)

class B:
    demo2 = 20
    def fun2(self):
        print(self.demo2)

class C(A,B):
    def fun3(self):
        print("Hey there, You are in child class.")

c1 = C()
c1.fun3()

print("First Number is: ", c1.demo1)
print("Second Number is: ", c1.demo2)

#Output:-
##Hey there, You are in child class.
##First Number is:  10
##Second Number is:  20
