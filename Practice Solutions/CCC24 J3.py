#updated solution 2025
import sys
input = sys.stdin.buffer.readline #fast read input
n = int(input())
scores = [int(input()) for _ in range(n)] #add scores to liist
unique = sorted(list(set(scores)), reverse=True)
print(unique[2], scores.count(unique[2]))
