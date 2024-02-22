
lst = [
			[1,2,6],
			[4,5,6],
			[7,8,9]

		]

def print_diagonal(lst):
    sum = 0
    for i in range (len(lst)):
        sum += lst[i][i]
        print(lst[i][i])
    print(f"Sum of the diagonals: {sum}")
print_diagonal(lst)

def print_diagonal(lst):
    sum = 0
    for i in range (len(lst)):
        for j in range (len(lst)):
            if i+j == len(lst)-1:
                sum += lst[i][j]
                print(lst[i][j])
    print(f"Sum of the secondary diagonals: {sum}")
print_diagonal(lst)