f = open("./input.txt")

diff = []
count1 = 0
count2 = 0

def check_safe(list_l):
    if list_l == sorted(list_l) or list_l == sorted(list_l, reverse=True):
        for i in range(len(list_l)-1):
            diff = abs(list_l[i+1] - list_l[i]) 
            if diff<1 or diff>3:
                break
        else:
            return True

for line in f:
    list_l = list(map(int,line.split()))
    if check_safe(list_l):
        count1 += 1
    
    check = False
    for j in range(len(list_l)):
        l = list_l[:j] + list_l[j+1:]
        if check_safe(l):
            check = True
    if check: 
        count2 += 1

print(count1)
print(count2)
