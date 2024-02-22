num = int(input("Enter a number"))

fact = 1

if num < 0:
    print(f"Factorial of {num} doesn't exist")
elif num == 0:
    print(f"Factorial of {num} is: 1")
else:
    for i in range (1,num+1):
        fact = fact * i
    print(f"Factorial of {num} is: {fact}")