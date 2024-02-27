# Write the code for Nqueen Problem using Backtracking
#
# # create a function called isSafe that takes in a 2D list called board, an integer called row and an integer called col
# # create a for loop that iterates through the range of col
# # create an if statement that checks if board[row][i] is equal to 1
# # if true, return False
# # create a for loop that iterates through the range of row and col
# # create an if statement that checks if board[i][col] is equal to 1
# # if true, return False
# # create a variable called i and set it to row
# # create a variable called j and set it to col
# # create a while loop that iterates while i is greater than or equal to 0 and j is greater than or equal to 0

# # create an if statement that checks if board[i][j] is equal to 1
# # if true, return False
# # decrement i and j by 1
# # create a variable called i and set it to row
# # create a variable called j and set it to col
# # create a while loop that iterates while i is less than the length of board and j is greater than or equal to 0
# # create an if statement that checks if board[i][j] is equal to 1
# # if true, return False
# # decrement i by 1 and increment j by 1
# # return True
# # create a function called solveNQ that takes in a 2D list called board and an integer called col
# # create a base case that checks if col is equal to the length of board
# # if true, return True
# # create a for loop that iterates through the range of the length of board
# # create an if statement that checks if isSafe(board, i, col) is equal to True
# # if true, set board[i][col] to 1
# # create an if statement that checks if solveNQ(board, col + 1) is equal to True
# # if true, return True
# # set board[i][col] to 0
# # return False
# # create a function called printSolution that takes in a 2D list called board
# # create a for loop that iterates through the range of the length of board
# # create a for loop that iterates through the range of the length of board
# # create an if statement that checks if board[i][j] is equal to 1
# # if true, print "Q" end = " "
# # else, print "0" end = " "
# # print()

# # create a function called solveNQ that takes in an integer called N
# # create a 2D list called board and set it to a list comprehension that creates a list of N lists with N elements each
# # create a for loop that iterates through the range of N
# # create a for loop that iterates through the range of N
# # set board[i][j] to 0
# # create an if statement that checks if solveNQ(board, 0) is equal to False
# # if true, print("Solution does not exist")
# # return False
# # printSolution(board)
# # return True
# # create a function called isSafe that takes in a 2D list called board, an integer called row and an integer called col
# # create a for loop that iterates through the range of col
# # create an if statement that checks if board[row][i] is equal to 1
# # if true, return False
# # create a for loop that iterates through the range of row and col
# # create an if statement that checks if board[i][col] is equal to 1
# # if true, return False
# # create a variable called i and set it to row
# # create a variable called j and set it to col
# # create a while loop that iterates while i is greater than or equal to 0 and j is greater than or equal to 0
# # create an if statement that checks if board[i][j] is equal to 1
# # if true, return False
# # decrement i and j by 1
# # create a variable called i and set it to row
# # create a variable called j and set it to col
# # create a while loop that iterates while i is less than the length of board and j is greater than or equal to 0
# # create an if statement that checks if board[i][j] is equal to 1
# # if true, return False
