#########################################################################
## Name: Rishi Raj Singh Chauhan                                       ##
## ID: 14B00025                                                        ##
#########################################################################

# for shuffle()
from random import shuffle

# vertices of the graph
vertices = [0,1,2,3]

# matrix is the graph matrix
matrix = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]

# total sum of the path travelled
pathSum = 0
min_pathSum = 1000000

# flag to check whether we've reached a plateau
flag = 0

# randomising sequence of vertices
shuffle(vertices)

# to randomise the list except 1st element
def rd(l):
    s = [l[0]]
    l1 = l[1:]
    shuffle(l1)
    for i in l1:
        s.append(i)

# hill climb begins
while 1:
    pathSum = 0
    for i in range(len(vertices)):
        if i <len(vertices)-1:
            pathSum += matrix[vertices[i]][i+1]
        else:
            pathSum += matrix[vertices[i]][0]

    if pathSum<min_pathSum:
        min_pathSum = pathSum
    else:
        flag += 1

    if flag == 10000:
        break
    rd(vertices)

print pathSum
