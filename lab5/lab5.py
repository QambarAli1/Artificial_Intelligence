# Maze , Cannibal, and N Queen Wala krna hai + Dry Run ..!!


def solveNQueens(N):
    def initializeEmptyBoard(N):
        return [['.' for _ in range(N)] for _ in range(N)]

    def isSafe(board, row, col, N):
        # Check if there is any queen in the current column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def placeQueens(board, row, N):
        if row >= N:
            return True
        for col in range(N):
            if isSafe(board, row, col, N):
                board[row][col] = 'Q'
                if placeQueens(board, row + 1, N):
                    return True
                board[row][col] = '.'
        return False

    board = initializeEmptyBoard(N)
    if placeQueens(board, 0, N):
        return board
    else:
        return "No solution exists"

# Test the function
N = 8  # Change N to the desired board size
solution = solveNQueens(N)
if solution != "No solution exists":
    for row in solution:
        print(' '.join(row))
else:
    print(solution)
