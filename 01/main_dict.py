# this problem has two parts
f = open('./input.txt')

list1 = []
list2 = []

for line in f:
    x,y = map(int, line.split())
    list1.append(x)
    list2.append(y)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# part 1
diff = 0
for i in range(len(list1)):
    diff += abs(sorted_list1[i] - sorted_list2[i])
print(f"answer for part 1: {diff}")

# part 2
d = {}
for k in range(len(sorted_list1)):
    if sorted_list1[k] in d:
        d[sorted_list1[k]] += 1
    else:
        d[sorted_list1[k]] = 1
ss = 0
for num in sorted_list2:
    if num in sorted_list1:
        ss += num * d[num]

print(f"answer for part 2: {ss}")

