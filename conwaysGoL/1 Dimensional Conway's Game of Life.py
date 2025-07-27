import numpy as np

# Parameters
Len = 10    # Size of Board
gen = 100    # Number of Generations

# Creating Game board
board = np.zeros(Len)

# Populating Board; 1 is alive, 0 is dead; if user enters neither 1 nor 0, element is automatically set to 0
for n in range(Len):
    board[n] = int(input(f"Enter the state of cell {n+1}: "))
    if board[n] == 1 or board[n] == 0:
        continue
    else:           # To be improved
        board[n] = 0
        continue
print(board)

# Creating Array to store Memory
mem = np.zeros([Len, 3])

for g in range(gen):
    # Learning states of cell's neighbors
    for n in range(Len):
        if n != Len-1:  # Can be improved
            mem[n, 0] = board[n-1]
            mem[n, 1] = board[n]
            mem[n, 2] = board[n+1]
        else:
            mem[n, 0] = board[n-1]
            mem[n, 1] = board[n]
            mem[n, 2] = board[0]
    # Applying Rules to produce next generation
    for n in range(Len):
        if (mem[n] == [1, 1, 1]).all():
            board[n] = 0
        elif (mem[n] == [1, 0, 1]).all():
            board[n] = 1
        elif (mem[n] == [1, 1, 0]).all():
            board[n] = 1
        elif (mem[n] == [1, 0, 0]).all():
            board[n] = 0
        elif (mem[n] == [0, 1, 0]).all():
            board[n] = 0
        elif (mem[n] == [0, 0, 0]).all():
            board[n] = 1
    print(board)
