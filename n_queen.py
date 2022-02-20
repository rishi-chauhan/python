"""Code to solve n-queen problem"""
from random import randint
from sys import argv

# num_of_queens = int(input("Enter number of queens: "))
num_of_queens = int(argv[1])
board=[[0]*num_of_queens for i in range(num_of_queens)]

def check_row(row_ind):
    """checks if row is safe"""
    if 1 in board[row_ind]:
        return False
    return True

def check_col(col_ind):
    """checks if col is safe"""
    for row in board:
        if row[col_ind]==1:
            return False
    return True

def check_diag(row_ind, col_ind):
    """checks if all diagonals are safe"""
    return check_diag_up_left(row_ind, col_ind) and \
        check_diag_up_right(row_ind, col_ind) and \
        check_diag_bot_left(row_ind, col_ind) and \
        check_diag_bot_right(row_ind, col_ind)

def check_diag_up_left(row_ind, col_ind):
    """Checks if there is another queen placed on the top-left diagonal of the
    cell mentioned"""
    while row_ind>=0 and col_ind>=0:
        if board[row_ind][col_ind]==1:
            return False
        row_ind-=1
        col_ind-=1
    return True

def check_diag_up_right(row_ind, col_ind):
    """Checks if there is another queen placed on the top-right diagonal of the
    cell mentioned"""
    while row_ind>=0 and col_ind<num_of_queens:
        if board[row_ind][col_ind]==1:
            return False
        row_ind-=1
        col_ind+=1
    return True

def check_diag_bot_left(row_ind, col_ind):
    """Checks if there is another queen placed on the bottom-left diagonal of the
    cell mentioned"""
    while 0<=row_ind<num_of_queens and col_ind>=0:
        if board[row_ind][col_ind]==1:
            return False
        row_ind+=1
        col_ind-=1
    return True

def check_diag_bot_right(row_ind, col_ind):
    """Checks if there is another queen placed on the bottom-right diagonal of the
    cell mentioned"""
    while row_ind<num_of_queens and col_ind<num_of_queens:
        if board[row_ind][col_ind]==1:
            return False
        row_ind+=1
        col_ind+=1
    return True

def solution(row, col, queens_left, visited):
    """solve and return the solution board"""
    if queens_left==0:
        return board
    if check_row(row) and check_col(col) and check_diag(row, col):
        board[row][col]=1
        return solution(randint(0,num_of_queens-1), \
            randint(0, num_of_queens-1), queens_left-1, [])
    return solution(randint(0,num_of_queens-1), randint(0, num_of_queens-1), \
        queens_left, visited)

print(solution(randint(0,num_of_queens-1), randint(0, num_of_queens-1), num_of_queens, []))
