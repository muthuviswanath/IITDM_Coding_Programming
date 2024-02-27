import Powers
def CheckAmstrong(num):
    # logic to find the total number of digits
    temp_a = num
    digits,sum = 0,0
    while temp_a >0:
        temp_a //= 10
        digits += 1
    print (digits)

    while num > 0:
        digit = num % 10
        sum = sum + Powers.power(digit,digits)
        num //= 10
    print(sum)

n = int(input("Enter any number"))
result = CheckAmstrong(n)
if n == result:
    print(f"Given number {n} is an amstrong number")
else:
    print(f"Given number {n} is not an amstrong number")