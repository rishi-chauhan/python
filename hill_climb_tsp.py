"""
College assignment for using hill climb for a travelling salesman problem
"""
# for shuffle()
from random import shuffle

# vertices of the graph
VERTICES = [0, 1, 2, 3]

# matrix is the graph matrix
MATRIX = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

# total sum of the path travelled
PATH_SUM = 0
MIN_PATH_SUM = 1000000

# flag to check whether we've reached a plateau
FLAG = 0

# randomising sequence of vertices
shuffle(VERTICES)

def rd(l):
    """to randomise the list except 1st element"""
    s = [l[0]]
    l1 = l[1:]
    shuffle(l1)
    for i in l1:
        s.append(i)

# hill climb begins
while 1:
    PATH_SUM = 0
    for i in range(len(VERTICES)):
        if i < len(VERTICES)-1:
            PATH_SUM += MATRIX[VERTICES[i]][i+1]
        else:
            PATH_SUM += MATRIX[VERTICES[i]][0]

    if PATH_SUM < MIN_PATH_SUM:
        MIN_PATH_SUM = PATH_SUM
    else:
        FLAG += 1

    if FLAG == 10000:
        break
    rd(VERTICES)

print(PATH_SUM)
