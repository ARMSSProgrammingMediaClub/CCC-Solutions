# another horrible solution lol

x = input().split()
n = list(map(int, x))

bruh1 = n[0]
bruh2 = n[1]
bruh3 = n[2]
bruh4 = n[3]

print(0, bruh1, bruh1+bruh2, bruh1+bruh2+bruh3, bruh1+bruh2+bruh3+bruh4)
print(bruh1, 0, bruh2, bruh2+bruh3, bruh2+bruh3+bruh4)
print(bruh1+bruh2, bruh2, 0, bruh3, bruh3+bruh4)
print(bruh1+bruh2+bruh3, bruh2+bruh3, bruh3, 0, bruh4)
print(bruh1+bruh2+bruh3+bruh4, bruh2+bruh3+bruh4, bruh3+bruh4, bruh4, 0)
