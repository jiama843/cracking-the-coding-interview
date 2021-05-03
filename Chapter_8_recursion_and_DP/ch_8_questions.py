
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

# NOTE: THIS WILL OVERFLOW WHEN THE INTEGER IS LARGE ENOUGH


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

# NOTE: FOR FURTHER QUESTIONS USE r,c (row, column) instead of x, y to avoid confusion

######################################################################

# Q3. Magic Index
# Assume negatives are possible, otherwise the question is trivial (its either 0 or nothing)
# We know the array is sorted, so we can divide and conquer on two cases
# if A[i] > i, we know that the magic index needs to be in A[0:i] since its impossible to maintain 
#   a sorted list by decreasing any A[k] after k > i
# The opposite applies to A[i] < i (it needs to be in A[i+1:end])

test_arr = [-5, -3, -1, 0, 1, 4, 6, 8, 9 , 10, 14]
test_arr2 = [-5, -3, -1, 0, 1, 4, 7, 8, 9 , 10, 14]

def magic_index_help(arr, start, end):
    if end < start: return -1
    mid = int((start + end) /2)

    if arr[mid] > mid:
        return magic_index_help(arr, start, mid - 1)
    elif arr[mid] < mid:
        return magic_index_help(arr, mid + 1, end)
    else:
        return mid

def magic_index(arr):
    return magic_index_help(arr, 0, len(arr) - 1)

print("Q3 Magic Index")
print(magic_index(test_arr)) # Expected 5
print(magic_index(test_arr2)) # Expected -1

# Follow up: Non distinct elements
# Consider the example:
# [-5, -4, -1, 0, 1, 1, 1, 7], if we chose 5, we have A[5] = 1
# This doesn't give us any info on the right side, but on the left,
# we know that we can rule out A[2] to A[5] for being the magic index
# As such, we can recurse on max(A[0:i-A[i]], A[i:end]) if A[i] < i and
# max(A[0:i], A[i+A[i]:end]) if A[i] > i

test_arr3 = [-5, -4, -1, 0, 1, 1, 1, 7]

# def magic_index_followup(arr):


# print(magic_index_followup(test_arr3)) # Expected 7

######################################################################

# Q4. Power Set
# Bottom-up approach: Each element is a subset,
# then each combination of the previous elements, then each combination of those and so on
# this is tougher to imagine in later stages

# Top-down approach: divide and conquer, deal with subproblems on each half of the set
# Base case: we find all combinations of 2 elements (there are 3) e.g
# - [2], [3], [2, 3] are generated from 2 and 3
# Combine step: given two lists of subsets, we weave all the elements together

test_set = [3, 4, 5, 6, 7]

def combine_pset(s1, s2):
    all_subsets = []

    for _s1 in s1:
        for _s2 in s2:
            all_subsets.append(_s1 + _s2)
    
    return all_subsets + s1 + s2

def power_set(s):
    if len(s) == 1: return [s]

    mid = int(len(s)/2)

    l_sets = power_set(s[0:mid])
    r_sets = power_set(s[mid:len(s)])

    return combine_pset(l_sets, r_sets)

print("Q4 Power Set")
print(power_set(test_set))


######################################################################

# Q5. Recursive Multiply