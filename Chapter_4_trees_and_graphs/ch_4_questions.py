graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2],
    4: [6],
    5: [4],
    6: [5]
}

# g = graph, s = source
# def dijkstra(g, s):
#     dist = {}
#     prev = {}

#     # Set path and dist maps
#     for v in p1:
#         dist[v] = 
    
#     return (dist, prev)


# 1. Route between nodes
# dijkstra's algo + find smallest path in dist
# Modify BFS to return if dest in visited set

def route_btw_nodes(g, n, dest):
    visited = set()

    queue = []
    queue.append(n)
    
    while len(queue) > 0:
        v = queue.pop(0)

        if v == dest: return True

        if v not in visited:        
            visited.add(v)
            for neighbor in g[v]:
                queue.append(neighbor)

    return dest in visited

print("Q1 route between nodes")
print(route_btw_nodes(graph, 2, 1))


# 2. Minimal tree
# 