#Write a program to show variable length argument and its use.

def my_func(*kids):
    print("The yougest child is: ", kids[2])
my_func("sneha", "sonu","shanvi", "neha")
