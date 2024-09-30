#Write a program to search an element in the list using for loop and also demonstrate the use of "else" with for loop.

list1 = [11,22,33,44,55]
n = 0

a = int(input("Enter a Number you want to search: "))

for k in list1:
    if(k==a):
        print("Given number exists.")
    else:
        n = n+1
    if(n == len(list1)):
        print("Given number does not exists.")

