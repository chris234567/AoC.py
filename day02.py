with open('day02.txt') as f:
    lines = f.readlines()
f.close()

# part one

valids = 0
valids2 = 0

def cutString(line: list):
    return line.replace('-', ' ').replace(':', ' ').split()

for i in lines:
    currLine = cutString(i)

     # part one 

    counter = 0
    for pos in currLine[3]:
        counter += 1 if pos == currLine[2] else 0
    valids += 1 if counter >= int(currLine[0]) and counter <= int(currLine[1]) else 0

    # part two

    a = currLine[3][int(currLine[0]) - 1] == currLine[2] 
    b = currLine[3][int(currLine[1]) - 1] == currLine[2]
    valids2 += 1 if a != b else 0 # XOR

print('According to corporate policy ' + str(valids) + ' passwords are valid')
print('According to the official toboggan corporate Authentification policy ' 
    + str(valids2) + ' passwords are valid')
    