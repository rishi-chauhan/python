######################################################################################################
#### Name: Rishi Raj Singh Chauhan                                                                ####
#### The following code on genetic algorithm tries to minimise the function given in "func"       ####
#### function and display the result.                                                             ####
######################################################################################################

# import something
import random
import copy

# define population
population = [p for p in xrange(10)]

# function to minimise 2x+3
def func(var):
    return (2*var) + 3

# making chromo
def makeChromo(ch):
    # return "{0:b}".format(ch)
    return bin(ch)

# generating random population
def genPop(pop):
    l = []
    # making population of 4
    for i in range(10):
        l.append(random.choice(pop))
    return l

# calculating probabilities
def calcProb(lst):
    total = 0.0
    for i in lst:
        total += float(func(i))

    # probability dictionary to store probabilities
    prob = {}

    # calculating probabilities
    for i in lst:
        prob[i] = float(func(i)/total)
    return prob

# finding winnner according to tournament method
def findWinner(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        # stores winners of each round
        winners = copy.deepcopy(lst)
        for i,j in zip(range(0,len(lst),2), range(1,len(lst),2)):
            if func(lst[i]) >= func(lst[j]):
                winners.remove(lst[i])
            else:
                winners.remove(lst[j])
        return findWinner(winners)

# selecting parents
def selectParent(pop):
    p1 = findWinner(pop)
    pop.remove(p1)
    p2 = findWinner(pop)

    return p1, p2

# cross-over function
def crossOver(chromo1, chromo2):
    # length of chromosomes will be equal to lenght of largest chromosome
    if chromo1 > chromo2:
        length = len(chromo1)
    else:
        length = len(chromo2)
    # making length even so that cross-over is easy
    if length % 2 != 0:
        length += 1
    # string to enter into the format function
    s = "#0"+str(length)+"b"
    # formating chromosomes of equal lenghts
    chromo1 = format(int(chromo1, 2), s)
    chromo2 = format(int(chromo2, 2), s)
    temp1 = ""
    temp2 = ""
    # interchanging alternate digits
    for i in range(2, length-1, 2):
        temp1 += chromo1[i] + chromo2[i+1]
        temp2 += chromo1[i+1] + chromo2[i]
    return temp1, temp2

result_mila = False
old_result = 0
new_result = 0
flag = 0

while not result_mila:
    # generating random population
    random_selection = genPop(population)
    # print "Randomly selected population = ", random_selection

    # selecting parents
    p1, p2 = selectParent(random_selection)

    # print("random_selection = ", random_selection)

    # displaying parents
    # print "\nParent 1 (p1) = ", p1
    # print "Parent 2 (p2) = ", p2

    # converting to binary to get chromosomes
    p1 = makeChromo(p1)
    p2 = makeChromo(p2)

    # printing chromosomes
    # print "\nBinary of p1 = ", p1
    # print "Binary of p2 = ", p2

    new_p1, new_p2 = crossOver(p1, p2)

    # print "\np1 after cross-over: ", new_p1, "\np2 after cross-over: ", new_p2
    # print "\nInteger value of p1: ", int(new_p1,2), "\nInteger value of p2: ", int(new_p2,2)

    # passing the cross-over into function
    if func(int(new_p1, 2)) < func(int(new_p2, 2)):
        new_result = func(int(new_p1, 2))
    else:
        new_result = func(int(new_p1, 2))

    if old_result <= new_result:
        flag += 1
    else:
        old_result = new_result

    if flag == 1000:
        result_mila = True

print "Minimum of the function is: ", new_result
