def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

terms = int (input("Enter the number of terms"))

print(f"Fibonacci Sum: {fibonacci(terms)}")

if terms <= 0:
    print("Not possible to generate")
else:
    print("Fibo Sequence")
    for i in range (terms):
        print(fibonacci(i),end=" ")