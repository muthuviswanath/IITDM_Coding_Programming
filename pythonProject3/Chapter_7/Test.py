maximum = int(input("Enter the number for maximum"))
number = int(input("Enter the number to guess"))
count = 0
low, high = 1, maximum
while low < high:
	mid = (low + high) // 2
	count += 1
	if mid == number:
		print(f"Your number is: {number}")
		break
	elif mid > number:
		high = mid -1
	else:
		low = mid + 1
print(f"Total {count} times searched")