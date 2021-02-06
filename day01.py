with open('day01.txt') as f:
    nums = list(map(int, f.readlines()))

f.close()

# part one short

for i in nums:
    for r in nums[nums.index(i):]:
        if i + r == 2020:
            print(i * r)

# part two short
            
for i in nums:
    for r in nums[nums.index(i):]:
        for k in nums[nums.index(r):]:
            if i + r + k == 2020:
                print(i * r * k)

# part one extended

pair = []

for i in nums:
    for r in nums[nums.index(i):]: # musn't check whole list to avoid duplicate pairs
        if i + r == 2020:
            pair.append(i)
            pair.append(r)

print('The correct pair is: ' + str(pair))

sum = 1
for k in pair:
    sum *= k

print('Its sum equals: ' + str(sum))

# part two extended

values = []

for i in nums:
    for r in nums[nums.index(i):]: # musn't check whole list to avoid duplicate pairs
        for k in nums[nums.index(r):]:
            if i + r + k == 2020:
                values.append(i)
                values.append(r)
                values.append(k)

print('The correct values are: ' + str(values))

sum2 = 1
for k in values:
    sum2 *= k

print('Their sum equals: ' + str(sum2))
