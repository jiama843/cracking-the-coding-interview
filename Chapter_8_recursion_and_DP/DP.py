# DP and Memoization
# - take recursive algorithm, find overlapping subproblems and cache results

# Fibonacci number 
def fib(i):
    if i == 0:  return 0
    if i == 1:  return 1
    return fib(i-1) + fib(i-2)

print(fib(6))

# Analyzing efficiency:

# Each recursive call splits into 2 recursive calls, subtracting by a factor of 1 or 2
# We will reach a base case 2^n times, the next level up there will be 2^n-1 and so on.

# Overall, this algorithm is about O(2^n) time 
# (if we want to be more specific its closer to 1.6^n since one side decrements by 2)



# Top-Down Dynamic programming (Memoization)
# By studying the recursion tree for identical nodes, we see that a node like fib(3) is called
# multiple times. Why not just store the result in a map (cache) so no excessive recursive calls are
# required?

cache = {}

def fib_mem(i):
    if i == 0 or i == 1:
        cache[i] = i
        return i

    if i not in cache:
        cache[i] = fib_mem(i-1) + fib_mem(i-2)

    return cache[i]

print(fib_mem(500))

# This has runtime O(n), the reason for this is because we always cache the first time we
# compute a result, so we really only "compute each node in the recursion tree once"

# Bottom up approach, the traditional way to think about DP
# Start with the base case and determine how the "next elements build off of the previous"

def fib_bu(n):
    cache = [0] * (n + 1)
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]

print(fib_bu(8))

