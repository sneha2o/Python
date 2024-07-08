# Write a program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.


def search_ele(lst, target):
    for element in lst:
        if element == target:
            print(f"Element {target} found in the list.")
            break
    else:
        print(f"Element {target} not found in the list.")

l1 = ["sneha", "sonu", 10, 20, 30]
target_element = "sneha"

search_ele(l1, target_element)

target_element = 50
search_ele(l1, target_element)

# output:-
# Element sneha found in the list.
# Element 50 not found in the list.


    
        


