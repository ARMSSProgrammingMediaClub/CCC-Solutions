# alternate solution using 2D array and reverse index splice
n = input()
grid = [[1,2],[3,4]]
H = n.count('H')
V = n.count('V')
if H % 2 == 1: #if 1 H flip horizontal
    grid = grid[::-1]
if V % 2 == 1: #if 1 H flip vertical
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

print(*grid[0])
print(*grid[1])
