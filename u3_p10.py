#Write a program to create a static method that counts the number of instances created for a class.

class student:
    counter = 0

    def __init__(self):
        student.counter += 1

    @staticmethod

    def dis():
        print("Total object created: ", student.counter)

s1 = student()
s2 = student()
s3 = student()
student.dis()
