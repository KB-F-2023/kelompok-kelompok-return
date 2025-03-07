import random

SIZE = 8

def cost(board):
    attacks = 0
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if board[i] == board[j]:
                # Check row attacks
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                # Check diagonal attacks
                attacks += 1
    return attacks

def print_board(board):
    for row in board:
        for col in row:
            if col == 1:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()

def hill_climbing(board):
    current_cost = cost(board)
    while current_cost > 0:
        new_board = board.copy()
        new_cost = current_cost
        for i in range(SIZE):
            for j in range(SIZE):
                if new_board[i][j] == 1:
                    continue
                new_board[i][j] = 1
                new_board[i][j] = 0
                c = cost(new_board)
                if c < new_cost:
                    new_cost = c
                    row = i
                    col = j
                new_board[i][j] = 0
        if new_cost >= current_cost:
            # Stuck at local optimum
            break
        board[row][col] = 1
        current_cost = new_cost

def generate_board():
    board = [[0 for j in range(SIZE)] for i in range(SIZE)]
    for i in range(SIZE):
        j = random.randint(0, SIZE-1)
        board[i][j] = 1
    return board

board = generate_board()
print("Initial Board:")
print_board(board)
hill_climbing(board)
print("\nFinal Board:")
print_board(board)
