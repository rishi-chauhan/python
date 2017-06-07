# for shuffle() and randint()
import random

# getting number of queens
queen_num = int(input("Enter the number of queens: "))

# create board
board = [[0 for i in range(queen_num)] for i in range(queen_num)]

num_of_queens = queen_num

while num_of_queens != 0:
    if num_of_queens >0:
        i = random.randint(0, queen_num-1)
        j = random.randint(0, queen_num-1)
        if board[i][j]==1:
            continue
        else:
            board[i][j] = 1
            num_of_queens -= 1
    else:
        break

print board

def checkRow(row, brd):
    for i in range(queen_num):
        # col is fixed
        if brd[i][piece_col] == 1 and i != piece_row:
            return False

def checkCol(col, brd):
    for i in range(queen_num):
        # row is fixed
        if brd[piece_row][i] == 1 and i != piece_col:
            return False

def checkDiag(row, col, brd):
    row -= 1
    col -= 1
    while row != 0:
        while col != 0:
            brd[row][col]

def dead(piece_row, piece_col, brd):
    for i in range(queen_num):
        # col is fixed
        if brd[i][piece_col] == 1 and i != piece_row:
            return False
        # row is fixed
        if brd[piece_row][i] == 1 and i != piece_col:
            return False

flag = True

while flag:
