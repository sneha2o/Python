# Write a program to display sum of two complex numbers.

def comp_numbers(c1, c2):
    return c1 + c2

comp1 = complex(2,4)
comp2 = complex(3,6)

result = comp_numbers(comp1, comp2)
print("The sum of", comp1, "and", comp2, "is: ",result)

# output:
# The sum of (2+4j) and (3+6j) is:  (5+10j) ------>(2+3 = 5) (4+6 = 10)

