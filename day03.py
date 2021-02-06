with open('day03.txt') as f:
    forest = [line.replace('\n', '') for line in f]
f.close()

def checkLane(x: int, y: int, forest: list):
    trees = 0
    pos = 0
    if y == 1:
        for i in forest:
            if str(i[pos % len(i)]) == '#':
                trees += 1
            pos += x
    else:
        for i in range(0, len(forest), 2):
            if str(forest[i][pos % len(forest[i])]) == '#':
                trees += 1
            pos += x
    
    return trees

# part one
print(f'Number of encountered trees: {checkLane(3, 1, forest)}')

# part two
ways = [(1 , 1), (3, 1), (5, 1), (7, 1), (1, 2)]
sum = 1

for r in ways:
    sum *= checkLane(r[0], r[1], forest)

print(f'Sum of encountered trees in all lanes: {sum}')
