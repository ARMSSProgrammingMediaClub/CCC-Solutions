#easiest J4/S1 question
n = input()
grid = [1,2,3,4]
H = n.count('H')
V = n.count('V')
if H % 2 == 1: #if 1 H flip horizontal
    grid[0], grid[2] = grid[2], grid[0]
    grid[1], grid[3] = grid[3], grid[1]
if V % 2 == 1: #if 1 H flip vertical
    grid[0], grid[1] = grid[1], grid[0]
    grid[2], grid[3] = grid[3], grid[2]
print(grid[0], grid[1])
print(grid[2], grid[3])
