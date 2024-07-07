# Write a program to assert the user enters a number greater than zero.


def get_positive_numbers():
    try:
        numbers = float(input("Enter a number greater than zero: "))
        assert numbers > 0, "The number must be greater than 0."
        print("You Entered: ", numbers)
    except ValueError:
        print("Invalid input. please enter valid numbers.")
    except AssertionError as e:
        print(e)

get_positive_numbers()

# output:-
# Enter a number greater than zero: 10
# You Entered:  10.0

# Enter a number greater than zero: -1
# The number must be greater than 0.

# Enter a number greater than zero: sneha
# Invalid input. please enter valid numbers.