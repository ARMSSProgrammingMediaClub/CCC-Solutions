#Scores 11/15, test cases 9 and 11 missed
enocdedInstructions = []

while True:
    a = int(input())
    if a != 99999:
        a = [int(x) for x in str(a).zfill(5)]
        enocdedInstructions.append(a)
    else:
        break

for x in range(len(enocdedInstructions)):
    dir = enocdedInstructions[x][0] + enocdedInstructions[x][1]
    if dir % 2 == 0:
        direction = "right"
        previousDir = direction
    elif dir % 2 != 0 and dir > 0:
        direction = "left"
        previousDir = direction
    else:
        direction = previousDir
        
    b = [str(x) for x in enocdedInstructions[x]]
    print(direction, (''.join(b[2:])))
