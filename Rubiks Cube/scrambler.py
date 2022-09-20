import random

faces = ["U", "D", "L", "R", "F", "B"]
variations = ["", "'", "2"]


def create_scramble():
    lst = [[random.choice(faces), random.choice(variations)] for i in range(25)]

    while lst[0][0] == lst[1][0]: # do this because the other checker 3 lines down doesn't check if index 1 and index 0 are equal
        lst[0][0] = random.choice(faces)

    for i in range(2, 25): 
        while lst[i][0] == lst[i-1][0] or lst[i][0] == lst[i-2][0]: 
            lst[i][0] = random.choice(faces)

    return lst


def print_scramble(lst):
    for item in lst:
        print(item[0]+item[1]+" ", end="")



scramble = create_scramble()

print_scramble(scramble)