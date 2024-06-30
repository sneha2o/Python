# Create a program to display memory locations of two variables using id() function, and then use identity operators two compare whether two objects are same or not.
# The 'id()' function in Python is used to obtain the unique identifier (memory address) of an object. This unique identifier is guaranteed to be constant and unique for the object during its lifetime. 


def main(v1, v2):
    print(f"Memory location of v1 ({v1}): {id(v1)}")
    print(f"Memory location of v1 ({v2}): {id(v2)}")

    if v1 is v2:
        print("v1 & v2 are same object.")
    else:
        print("v1 & v2 are not same object.")

    if v1 is not v2:
        print("v1 & v2 are not same object.")
    else:
        print("v1 & v2 are same object.")

a = 10
b = 10
c = 20

main(a, b)
print()
main(a, c)

# # output:
# Memory location of v1 (10): 140703583255256
# Memory location of v1 (10): 140703583255256
# v1 & v2 are same object.
# v1 & v2 are same object.

# Memory location of v1 (10): 140703583255256
# Memory location of v1 (20): 140703583255576
# v1 & v2 are not same object.
# v1 & v2 are not same object.
