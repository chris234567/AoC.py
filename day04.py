# with open('day04.txt') as f:
#     lines = [line.replace('\n', '') for line in f]
# f.close()

# passports = []
# s = ''
# lines.append('') # for last block to get recognized

# for i in lines:
#     s += ''.join(i)
#     if i == '':
#         passports.append(s)
#         s = ''

# # part one

# # fields required: byr, iyr, eyr, hgt, hcl, ecl, pid optional: cid
# valids = 0

# for i in passports:
#     counter = 0
#     for r in required:
#         if r in i:
#             counter += 1
#     if counter == len(required):
#         valids += 1

# print(valids)

with open('day04.txt') as f:
    lines = [line.replace('\n', ' ') for line in f.read().split('\n\n')]
f.close()

passports = []

for line in lines:
    currPassport = {}
    try: # possibility of index out of range at incorrect values 
        if 'byr' in line:
            currPassport['byr'] = line[line.index('byr') + 4:line.index('byr') + 8]
        if 'iyr' in line:
            currPassport['iyr'] = line[line.index('iyr') + 4:line.index('iyr') + 8]
        if 'eyr' in line:
            currPassport['eyr'] = line[line.index('eyr') + 4:line.index('eyr') + 8]
        if 'hgt' and 'cm' in line:
            currPassport['hgt'] = line[line.index('hgt') + 4:line.index('hgt') + 9]
        elif 'hgt' and 'in' in line:
            currPassport['hgt'] = line[line.index('hgt') + 4:line.index('hgt') + 8]
        if 'hcl' in line:
            currPassport['hcl'] = line[line.index('hcl') + 4:line.index('hcl') + 11]
        if 'ecl' in line:
            currPassport['ecl'] = line[line.index('ecl') + 4:line.index('ecl') + 7]
        if 'pid' in line:
            currPassport['pid'] = line[line.index('pid') + 4:line.index('pid') + 13]
    except:
        pass
    passports.append(currPassport)

# part one
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valids = 0

for line in lines:
    counter = 0
    for req in required:
        if req in line:
            counter += 1
    if counter == len(required):
        valids += 1

print(valids)

# part two
counter = 0

for p in range(len(passports)):
    try:
        val = passports[p].get(req)
        if req == 'byr':
            try:
                counter += 1 if 1920 <= int(val) <= 2002 else 0
            except:
                pass 
        elif req == 'iyr':
            try:
                counter += 1 if 2010 <= int(val) <= 2020 else 0
            except:
                pass
        elif req == 'eyr':
            try:
                counter += 1 if 2020 <= int(val) <= 2030 else 0
            except:
                pass
        elif req == 'hgt':
            try:
                if 'cm' in val:
                    counter += 1 if 150 <= int(val[0:3]) <= 193 else 0
                elif 'in' in val:
                    counter += 1 if 59 <= int(val[0:2]) <= 76 else 0
            except:
                pass
        elif req == 'hcl':
            try:
                ct = 0
                if val.startswith('#'):
                    for c in val[1:7]:
                        if 48 <= ord(c) <= 57:
                            ct += 1
                        elif 97 <= ord(c) <= 122:
                            ct += 1
                counter += 1 if ct == 6 else 0
            except:
                pass
        elif req == 'ecl':
            try:
                for k in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if val == k:
                        counter += 1 # haircolor can only math one at a time
            except:
                pass
        elif req == 'pid':
            try:
                ct = 0
                for c in val:
                    if 48 <= ord(c) <= 57:
                        ct += 1
                if ct == 9:
                    counter += 1
            except:
                pass
    except:
        pass
        
print(counter)
                

        


