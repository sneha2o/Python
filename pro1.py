# Write a program to swap two numbers without taking a temporary variable. 

def swap_num(a, b):
    print("Before Swapping: a =",a ,"b =",b)
    a = a + b #a = 10 + 20 = 30
    b = a - b #b = 30 - 20 = 10
    a = a - b #a = 30 - 10 = 20
    print("After Swapping: a=",a, "b=",b)

swap_num(10,20)


a = 10
b = 20

# Output:-

# Before Swapping: a = 10 b = 20
# After Swapping: a= 20 b= 10