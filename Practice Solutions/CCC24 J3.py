#updated solution 2025
n = int(input())
scores = [int(input()) for _ in range(n)]
unique = list(set(scores))
unique.sort(reverse=True)
print(unique[2], scores.count(unique[2]))
