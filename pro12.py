# Write a python program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. (2.54 = 1 inch).


def cm_to_inches(cm):
    return cm / 2.54

def main():
    try:
        length_cm =float(input("Enter a length in centimeters: "))
        if length_cm < 0:
            print("Invalid Entry, length cannot be negative.")
        else:
            length_in = cm_to_inches(length_cm)
            print(f"{length_cm} cm is equal to {length_in: .2f} inches.")
    except ValueError:
        print("Invalid Input. Please enter a numeris value.")

if __name__ == "__main__":
    main()


# output:-
# Enter a length in centimeters: 5
# 5.0 cm is equal to  1.97 inches.

# Enter a length in centimeters: 20
# 20.0 cm is equal to  7.87 inches.