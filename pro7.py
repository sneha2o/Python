# Write a program that evaluates an expression given by the user at run time using eval() function. Example:
# Enter and expression: 10+8-9*2-(10*2)
# Result: -20

def eva_ex():
    try:
        ex = input("Enter an expression: ")
        result = eval(ex)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    eva_ex()

# output:
# Enter an expression: (2+4)/10
# Result: 0.6