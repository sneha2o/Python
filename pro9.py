# Write a menu driven python program which perform the following:
# Find area of circle
# Find area of triangle
# Find area of square and rectangle
# Find Simple Interest
# Exit.( Hint: Use infinite while loop for Menu)


import math

def area_of_circle(radius):
    return math.pi *(radius ** 2)

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_square(side):
    return side ** 2

def area_of_rectangle(length, breadth):
    return length * breadth

def simple_interest(principle, rate, time):
    return (principle * rate * time)/100

def menu():
    print("\n Menu: ")
    print("1. Find area of circle")
    print("2. Find area of tringle")
    print("3. Find area of sqaure")
    print("4. Find area of rectangle")
    print("5. Find Simple Interest")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            print(f"Area of circle: {area_of_circle(radius)}")

        elif choice == "2":
            base = float(input("Enter the base of the tringle: "))
            height = float(input("Enter the height of the tringle: "))
            print(f"Area of tringle: {area_of_triangle(base, height)}")

        elif choice == "3":
            side = float(input("Enter side of square: "))
            print(f"Area of square: {area_of_square(side)}")

        elif choice == "4":
            length = float(input("Enter the length of ractangle: "))
            breadth = float(input("Enter the breadth of ractangle: "))
            print(f"Area of Ractangle: {area_of_triangle(length, breadth)}")

        elif choice == "5":
            principle = int(input("Enter the principle: "))
            rate = int(input("Enter the rate of interest: "))
            time = int(input("Enter the period of time: "))
            print(f"Simple Interest : {simple_interest(principle, rate, time)}")

        elif choice == "6":
            
            print("Exiting the program, GoodBye!!")
            break
        else:
            print("Please enter the numbers between 1 to 6")


# output:-
#  Menu: 
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 1
# Enter the radius of the circle: 5
# Area of circle: 78.53981633974483

#  Menu: 
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 2
# Enter the base of the tringle: 2
# Enter the height of the tringle: 10
# Area of tringle: 10.0

#  Menu:
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 3
# Enter side of square: 10
# Area of square: 100.0

#  Menu:
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 4
# Enter the length of ractangle: 10
# Enter the breadth of ractangle: 8
# Area of Ractangle: 40.0

#  Menu:
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 5
# Enter the principle: 10000
# Enter the rate of interest: 10
# Enter the period of time: 5
# Simple Interest : 5000.0

#  Menu:
# 1. Find area of circle
# 2. Find area of tringle
# 3. Find area of sqaure
# 4. Find area of rectangle
# 5. Find Simple Interest
# 6. Exit
# Enter your choice (1-6): 6
# Exiting the program, GoodBye!!