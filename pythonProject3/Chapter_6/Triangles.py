triangle = [
    [7],
    [2, 1],
    [7, 2, 1],
    [8, 1, 7,0]
]

def find_min_cost(row, col, triangle): # row = 0,col = 0
    if row == len(triangle):
        return 0
    else:
        cost =  min (find_min_cost(row+1, col,triangle) ,
                    find_min_cost(row+1, col+1,triangle))
        return cost + triangle[row][col]

min_cost = find_min_cost(0,0,triangle)
print(min_cost)
