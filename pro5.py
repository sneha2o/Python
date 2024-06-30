# Write a program to find out and display the common and the non common elements in the list using membership operators

def com_and_noncom_ele(l1, l2):
    com_ele = []
    noncom_ele = []

    for element in l1:
        if element in l2 and element not in com_ele:
            com_ele.append(element)

    for element in l2:
        if element in l1 and element not in com_ele:
            com_ele.append(element)

    for element in l1:
        if element not in l2:
            noncom_ele.append(element)

    for element in l2:
        if element not in l1 :
            noncom_ele.append(element)

    print("The Common Elements: ", com_ele)
    print("The Non Common Elements: ", noncom_ele)

l1 = [1,2,3,4,5,6]
l2 = [4,5,6,7,8,9,10]

com_and_noncom_ele(l1, l2)



# output:
# The Common Elements:  [4, 5, 6]
# The Non Common Elements:  [1, 2, 3, 7, 8, 9, 10]