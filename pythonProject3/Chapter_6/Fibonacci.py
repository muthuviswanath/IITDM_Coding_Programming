def Fibonacci(n):
    fnum,snum = 0, 1
    print(fnum,snum, end =" ")
    for i in range(n):
        fnum,snum= snum,fnum+snum
        print(snum, end=" ")

Fibonacci(8)
print()
print("Fibonacci Using Recursion")
def Fibo_Recur(n):
    if n ==0 or n== 1:
        return n
    else:
        return Fibo_Recur(n-1) + Fibo_Recur(n-2)
for i in range (10):
    print(Fibo_Recur(i), end=" ")

# Using memoization

terms = {0:0, 1:1}
def fibonacci_memoization(n):
    if n in terms:
        return terms[n]
    else:
        terms[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
        return terms[n]

print()
print("Fibonacci Using Memoization")
for i in range (10):
    print (fibonacci_memoization(i), end =" ")