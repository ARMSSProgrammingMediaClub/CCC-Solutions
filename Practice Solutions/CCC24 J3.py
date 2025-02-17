#updated solution 2025
n = int(input())
scores = []

for i in range(n):
    x = int(input())
    scores.append(x)

unique = list(set(scores))
bronze = unique.sort(reverse=True)

print(unique[2], scores.count(unique[2]))
