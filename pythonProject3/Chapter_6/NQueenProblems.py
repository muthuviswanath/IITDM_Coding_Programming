def possible(row, col):
    for i in range(row):
        if col[row] == col[i] or abs(col[row] - col[i]) == row - i:
            return False
    return True

def queen_position(row, col):
    if possible(row,col):
        if row == len (col) - 1:
            print(col)
        else:
            for i in range(len(col)):
                col[row + 1] = i
                queen_position(row + 1, col)

no_of_queens = int(input("Enter the number of queens: "))
queen_position(-1,[-1]*no_of_queens)