with open('day06.txt') as f:
    input = [line.replace('\n', '') for line in f]

input.append('') # needed for last block to be recognized as such

def find(input: list, b: bool):
    if b:
        answered = [] # part one
    else:
        answered = {} # part two
        lines = 0
    sum = 0
    lines = 0

    for line in input:
        if line == '':
            temp = 0

            if not b:
                for key in answered: # for part two
                    if answered.get(key) == lines:
                        temp += 1

            if b:
                sum += len(answered)
                answered = []  # reset
            else:
                sum += temp
                lines = 0      # reset
                answered = {}  # reset
        else:
            lines += 1
        for char in line:
            if char not in answered:
                if b:
                    answered.append(char)
                else:
                    answered[char] = 1
            elif not b:
                answered[char] += 1

    return sum

print(find(input, True))
print(find(input, False))
