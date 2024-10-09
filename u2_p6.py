def checkprime():
    num = int(input("Enter a Number: "))
    c = 0
    if num == 1:
        print(num, "is not a prime number: ")
    if num > 1:
        for i in range(2, num + 1):
            if(num % i) == 0:
                c =  c + 1
      if c > 2:
            print("num is not prime")
    else:
                print("num is prime")

checkprime()
