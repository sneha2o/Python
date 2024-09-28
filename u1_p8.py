#Write a python program to sum of even numbers using command line arguments.

import sys
n = int(sys.argv[1])
i = 2
sum = 0
while(i<=n):
    sum += i
    i += 2
print("sum of two even no = ",sum)

#Output:- Run Customized
#10
#sum of even no = 30
