import re

f = open("./input.txt")

matches = []
for line in f:
    matches.extend(re.findall(r"mul\(\d+,\d+\)", line))
    # uncomment it for part 2
    #matches.extend(re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line))
print(matches)

# part 2
#total = 0
#enable = True
#for match in matches:
#    if match[2] == "" and enable:
#        total += int(match[0]) * int(match[1])
#    else:
#        if match[2] == 'do()':
#            enable = True 
#        else:
#            enable = False
#
#print(total)

# Part 1
nums = []
for match in matches:
    numlist = re.findall(r'\d+', match)
    nums.append(numlist)

total = 0
for n in nums:
    pro = 1
    for i in range(len(n)):
        pro *= int(n[i])
    total += pro
print(total)




