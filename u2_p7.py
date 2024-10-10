#Write a python program that removes any repeated items from a list so that each item appears at most once.
#For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

def remove(duplicate):
    final_list = []

    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

duplicate = [1,1,2,3,4,5,5,6]
print(remove(duplicate))
