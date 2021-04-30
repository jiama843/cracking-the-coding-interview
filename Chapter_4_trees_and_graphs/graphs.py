graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2],
    4: [6],
    5: [4],
    6: [5]
}


visited = set()

def DFS(n):
    if not n in graph: return

    visited.add(n)
    for neighbor in graph[n]:
        if not neighbor in visited:
            visited.add(neighbor)
            DFS(neighbor)

DFS(2)
print(visited)

# Basically visited set
colored = set()
def BFS(n):
    queue = []
    queue.append(n)
    colored.add(n)

    while len(queue) > 0:
        v = queue.pop(0)
        for neighbor in graph[v]:
            if not neighbor in colored:
                queue.append(neighbor)
                colored.add(neighbor)

BFS(2)
print(colored)
