with open('day05.txt') as f:
    lines = [line.replace('\n', '') for line in f]

# binary conversion can be done instead of binary search
# B equals 1 and F equals 0

# part one 

import math

max = 0
boardingPasses = []

for line in lines:
    firstHalf = line[0: 7]
    secondHalf = line[7:]
    num1 = 0
    num2 = 0

    for pos in range(len(firstHalf)):
        if firstHalf[pos] == 'B':
            num1 += math.pow(2, len(firstHalf) - pos - 1)
    for pos in range(len(secondHalf)):
        if secondHalf[pos] == 'R':
            num2 += math.pow(2, len(secondHalf) - pos - 1)

    val = num1 * 8 + num2
    if val > max:
        max = int(val)

    boardingPasses.append(int(val))

print(max)

# part two

boardingPasses.sort()

for i in range(len(boardingPasses)):
    if i != 0: # skip first pass
        # if difference from boardingpass[i - 1] to boardingpass[i] is not 0, there's a seat missing
        if (boardingPasses[i] - boardingPasses[i - 1]) != 1: 
            print(boardingPasses[i] - 1) # index of BP between [i - 1] and [i]
