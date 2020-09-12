"""
The following code on genetic algorithm tries to minimise the function given in "func"
function and display the result
"""

import random
import copy

# define population
POPULATION = [p for p in range(10)]
RESULT_MILA = False
OLD_RESULT = 0
NEW_RESULT = 0
FLAG = 0

def func(var):
    """function to minimise 2x+3"""
    return (2*var) + 3

def make_chromo(ch):
    """making chromo"""
    return bin(ch)

def gen_pop(pop):
    """generating random population of 4"""
    l = []
    for i in range(10):
        l.append(random.choice(pop))
    return l

def calc_prob(lst):
    """calculating probabilities"""
    total = 0.0
    for i in lst:
        total += float(func(i))

    # probability dictionary to store probabilities
    prob = {}

    # calculating probabilities
    for i in lst:
        prob[i] = float(func(i)/total)
    return prob

def find_winner(lst):
    """finding winnner according to tournament method"""
    if len(lst) == 1:
        return lst[0]
    # stores winners of each round
    winners = copy.deepcopy(lst)
    for i, j in zip(range(0, len(lst), 2), range(1, len(lst), 2)):
        if func(lst[i]) >= func(lst[j]):
            winners.remove(lst[i])
        else:
            winners.remove(lst[j])
    return find_winner(winners)

def select_parent(pop):
    """selecting parents"""
    p_1 = find_winner(pop)
    pop.remove(p_1)
    p_2 = find_winner(pop)

    return p_1, p_2

def cross_over(chromo1, chromo2):
    """cross-over function
    length of chromosomes will be equal to lenght of largest chromosome"""
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

while not RESULT_MILA:
    # generating random population
    RANDOM_SELECTION = gen_pop(POPULATION)

    # selecting parents
    P1, P2 = select_parent(RANDOM_SELECTION)

    # converting to binary to get chromosomes
    P1 = make_chromo(P1)
    P2 = make_chromo(P2)

    NEW_P1, NEW_P2 = cross_over(P1, P2)

    # passing the cross-over into function
    if func(int(NEW_P1, 2)) < func(int(NEW_P2, 2)):
        NEW_RESULT = func(int(NEW_P1, 2))
    else:
        NEW_RESULT = func(int(NEW_P2, 2))

    if OLD_RESULT <= NEW_RESULT:
        FLAG += 1
    else:
        OLD_RESULT = NEW_RESULT

    if FLAG == 1000:
        RESULT_MILA = True

print("Minimum of the function is: ", NEW_RESULT)
