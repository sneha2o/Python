#Write a program to sort an array elements using bubble sort technique.

def bubblesort(list1):
    for i in range(0, len(list1)-1):
        for j in range(len(list1)-i-1):
            if (list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

    print("Sorted list is: ",list1)

list1 = [88,79,90,2,26,1,5]
print("Original list is: ",list1)
bubblesort(list1)

#Output;-
##Original list is:  [88, 79, 90, 2, 26, 1, 5]
##Sorted list is:  [1, 2, 5, 26, 79, 88, 90]
