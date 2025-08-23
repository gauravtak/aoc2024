f = open('./input.txt')

list1 = []
list2 = []

for line in f:
    x,y = map(int, line.split())
    list1.append(x)
    list2.append(y)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

diff = 0
count = 0
total = 0
for i in range(len(list1)):
    diff += abs(sorted_list1[i] - sorted_list2[i])
    for j in range(len(list2)):
        if sorted_list1[i] == sorted_list2[j]:
            count = count + 1
    total += sorted_list1[i] * count
    count = 0

print(f"part 1: {diff}")
print(f"part 2: {total}")
