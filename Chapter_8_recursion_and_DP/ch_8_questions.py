
######################################################################

# 1. Triple Step
# Top-down thinking: starting with n, we have 3 subproblems:
# n-3, n-2, n-1 -> each of these has 3 subproblems as well
# Base case: if we overshoot the last step, we don't count the path as valid

# Reflect: I think that bottom-up suits this problem better, since we can build a cache of
# <step, paths to step> iterating from the bottom step all the way up to the top step

def triple_step(n):
    cache = [0] * (n + 1)

    # Base cases:
    cache[1] = 1
    cache[2] = 2
    cache[3] = 4

    for i in range(4, n+1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]

    return cache[n]

print("Q1 Triple Step")
print(triple_step(5))


######################################################################

# 2. Robot in a grid
# Bottom-Up thinking: We can build a 2D cache, each entry contains
# the number of paths up to it. If a cell is off-limits, we set the 
# number of paths to 0
# Base case: vertical and horizontal 1's and then 0's
# To build a path, we backtrack from the bottom right:
# - We check cache[i][i-1] (left) and cache[i-1][i] (up) and choose any non-zero value

robot_map = [
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [-1, -1, 0, 0, 0],
    [-1, -1, 0, -1, 0],
    [0, -1, 0, 0, 0]
]

# Let -1 be obstacles that cannot be crossed

def find_robo_path(c):
    x = len(c[-1]) - 1
    y = len(c) - 1

    path = []

    if c[y][x] == 0: return []

    while not (x == 0 and y == 0):
        if y >= 1 and c[y-1][x] > 0:
            y -= 1
            path.append("down")
        elif x >= 1 and c[y][x-1] > 0:
            x -= 1
            path.append("right")
        else:
            return []

    path.reverse()
    return path

def robot_grid(g):
    # Remember this is probably the best way to initialize 2d arrays in python
    # Due to reference property of [] * n
    cache = [[0] * len(g[-1]) for j in range(len(g))]

    # Base case: right and down
    for i in range(0, len(g[-1])):
        if g[0][i] == -1: break
        cache[0][i] = 1

    for i in range(0, len(g)):
        if g[i][0] == -1: break
        cache[i][0] = 1

    
    # Recursive case
    for i in range(1, len(g)):
        for j in range(1, len(g[-1])):
            cache[i][j] = cache[i-1][j] + cache[i][j-1] if g[i][j] != -1 else 0

    #print(cache)
    
    return find_robo_path(cache)

print("Q2 Robot in a Grid")
print(robot_grid(robot_map))


######################################################################

# Q3. Magic Index
