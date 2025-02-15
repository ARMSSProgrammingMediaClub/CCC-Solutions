n = str(input())
numbers = '0123456789'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '-+'

result = ""
x = []
for i in range(len(n)):
    if n[i] in alphabet or n[i] in symbols:
        result += n[i]
    if n[i] in numbers:
        if i+1 < len(n) and n[i+1] in alphabet: #if the next character after a number is in alphabet, add the current index and a space
            result += n[i]
            result += " "
        else:
            result += n[i]

x = result.split() #split the string into a list at every space


for y in range(len(x)):
    answer = ""
    for j in range(len(x[y])):
        if x[y][j] in alphabet:
            answer += x[y][j]
        if x[y][j] == '+':
            answer += ' tighten '
        if x[y][j] == '-':
            answer += ' loosen '
        if x[y][j] in numbers:
            answer += x[y][j]
    print(answer)
