# Starting Parameters
boardDim = 10
numGen = 10

# Creating Board
board = [[0 for i in range(boardDim)] for i in range(boardDim)]

# Setting up initial board conditions - 0 = Dead, 1 = Alive
# User can choose to generate random board or create their own custom one
choice = int(input("Type 1 for a Randomly Generated Board \n"
                   "Type 2 to create a Custom Board \n"))
if choice == 1:
    import random
    for i in range(boardDim):
        for j in range(boardDim):
            board[i][j] = random.randint(0,1)
elif choice == 2:
    for i in range(boardDim):
        for j in range(boardDim):
            board[i][j] = int(input(f"Enter the state of cell ({i + 1},{j + 1}): "))
            if board[i][j] != 1 and board[i][j] != 0:
                board[i][j] = 0  # If user inputs neither 1 nor 0, cell automatically set to 0
else:
    print("Please only enter a 1 or 2...")
    exit()

# Defining Functions
def nbr(i, j):      # Count number of alive Neighbors
    global board
    alive = 0
    alive += board[i-1][j-1]
    alive += board[i-1][j]
    alive += board[i-1][(j+1)%boardDim]
    alive += board[i][j-1]
    alive += board[i][(j+1)%boardDim]
    alive += board[(i+1)%boardDim][j-1]
    alive += board[(i+1)%boardDim][j]
    alive += board[(i+1)%boardDim][(j+1)%boardDim]
    return alive

# Rules
    # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

# Running Programme
print("Gen0")
for i in range(boardDim): print(board[i])
for t in range(numGen):
    print(f"Gen{t+1}")
    tempBoard = [[0 for i in range(boardDim)] for i in range(boardDim)]     # Creating tempBoard
    for i in range(boardDim):       # Applying aforementioned rules to each cell to determine next generation
        for j in range(boardDim):
            x = board[i][j]
            y = nbr(i, j)
            if x == 1:
                if y < 2:
                    tempBoard[i][j] = 0
                elif y > 3:
                    tempBoard[i][j] = 0
                else:
                    tempBoard[i][j] = 1
            if x == 0:
                if y < 3:
                    tempBoard[i][j] = 0
                elif y > 3:
                    tempBoard[i][j] = 0
                else:
                    tempBoard[i][j] = 1
    board = tempBoard
    for i in range(boardDim): print(board[i])

# Haven't ensured that it follows the rules correctly but in theory it should!