# Write a python program to find the sum of even numbers using command line arguments.

import sys

def sum_Of_EvenNo(args):
    numbers = [int(arg) for arg in args]

    even_sum = sum(num for num in numbers if num % 2==0)
    return even_sum

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print("Please Provide some numbers as command line arguments.")
    else:
        try:
            result = sum_Of_EvenNo(args)
            print(f"Sum of Even Numbers: {result}")
        except ValueError:
            print("Please Ensure all arguments are integers.")



# PS C:\Users\sneha> & C:/Users/sneha/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/sneha/OneDrive/Desktop/python/100 Days/clg python practicles/pro8.py" 1 2 3 4 5 6 
# Sum of Even Numbers: 12

# & C:/Users/sneha/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/sneha/OneDrive/Desktop/python/100 Days/clg python practicles/pro8.py" 10 20 30 40 50 60 
# Sum of Even Numbers: 210



