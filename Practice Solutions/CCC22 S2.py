#scores 14/15 for J4 criteria, solution takes >3 sec 

x = int(input()) # num of must
must = [input().split() for _ in range(x)]
y = int(input()) # num of mustnot
mustnot = [input().split() for _ in range(y)]
z = int(input()) # num of groups
groups = [list(input().split()) for _ in range(z)]
violations = 0

for i in range(x): #check violations of must
    for j in range(z):
        if must[i][0] in groups[j]:
            if must[i][1] not in groups[j]:
                violations += 1

for i in range(y):
    for j in range(z):
        if mustnot[i][0] in groups[j] and mustnot[i][1] in groups[j]:
            violations +=1
            
print(violations)
