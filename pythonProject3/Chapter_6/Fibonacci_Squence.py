#create the algorithm and the code for generating the fibonacci sequence using recursion and memoization
# create a function called Fibonacci that takes in a number n
# create two variables fnum and snum and set them to 0 and 1 respectively
# print the values of fnum and snum
# create a for loop that iterates through the range of n
# set fnum and snum to snum and fnum + snum respectively
# print the value of snum
# create a function called Fibo_Recur that takes in a number n
# create an if statement that checks if n is equal to 0 or 1
# if true, return n
# else, return Fibo_Recur(n-1) + Fibo_Recur(n-2)
# create a for loop that iterates through the range of 10
# print the value of Fibo_Recur(i)
# create a dictionary called terms with the keys 0 and 1 and the values 0 and 1 respectively
# create a function called fibonacci_memoization that takes in a number n
# create an if statement that checks if n is in terms
# if true, return terms[n]
# else, set terms[n] to fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
# return terms[n]
# create a for loop that iterates through the range of 10

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

# Fibonacci Using Recursion
# 0 1 1 2 3 5 8 13 21
# Fibonacci Using Recursion
# 0 1 1 2 3 5 8 13 21 34
# Fibonacci Using Memoization
# 0 1 1 2 3 5 8 13 21 34