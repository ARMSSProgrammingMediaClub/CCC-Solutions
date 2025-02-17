#updated solution 2025
import sys
input = sys.stdin.buffer.readline
n = int(input())
scores = [int(input()) for _ in range(n)]
unique = list(set(scores))
unique.sort(reverse=True)
print(unique[2], scores.count(unique[2]))
