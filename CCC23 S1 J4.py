C = int(input())

row1 = input().split(" ")
row2 = input().split(" ")

for i in range(len(row1)):
    row1[i] = int(row1[i])
    row2[i] = int(row2[i])


wet = row1.count(1) + row2.count(1) #count total wet squares (1)
adj = 0
for i in range(C):
    if i != C-1 and row1[i] == 1 and row1[i+1] == 1: #if i not last index and next is
        adj += 1
    if i != C-1 and row2[i] == 1 and row2[i+1] == 1: #row2: if i not last index and next is wet
        adj += 1 
    if row1[i] == 1 and row2[i] == 1 and i%2==0: #vert: if even and up down = 1
        adj += 1
print(wet*3-adj*2)