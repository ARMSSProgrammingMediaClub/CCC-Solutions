inp = list(input())
chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["+","-"]
lastChar = 0
instructions = []

for x in range(len(inp)):
    if inp[x] not in chars and inp[x] not in symbols:
        instructions.append(inp[lastChar:x+1])
        lastChar = x+1

def sort():
    for x in range(len(instructions)):
        if len(instructions[x]) == 1:
            instructions[x-1].append(instructions[x][0])
            instructions[x].pop(0)
            sort()

sort()

instructions = [x for x in instructions if x]
letters = []

for x in range(len(instructions)):
    for y in range(len(instructions[x])):
        if instructions[x][y] in chars:
            letters.append(instructions[x][y])
        if instructions[x][y] == '-':
            direction = "loosen"
            numStart = y
        elif instructions[x][y] == '+':
            direction = "tighten"
            numStart = y
    print(''.join(letters), direction, ''.join(instructions[x][numStart + 1:]))
    letters.clear()
