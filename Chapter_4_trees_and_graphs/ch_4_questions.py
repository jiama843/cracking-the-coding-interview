graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2],
    4: [6],
    5: [4],
    6: [5]
}

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        # n is Treenode

    def insert(self, n):
        if(self.val < n.val):
            self.right = n if self.right == None else self.right.insert(n)
        elif(self.val > n.val):
            self.left = n if self.left == None else self.left.insert(n)

        return self

    def print_tree(self):
        print(self.val, end = " ")
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

def create_tree():
    root = TreeNode(7, None, None)
    root.insert(TreeNode(5, None, None))
    root.insert(TreeNode(8, None, None))
    root.insert(TreeNode(20, None, None))
    root.insert(TreeNode(1, None, None))
    root.insert(TreeNode(2, None, None))
    root.insert(TreeNode(6, None, None))
    root.insert(TreeNode(3, None, None))
    
    return root

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
# Create node from middle element, recurse on left and right side of array
# 

test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def min_tree(s_arr):
    mid = int(len(s_arr)/2)

    if len(s_arr) == 0: return None
    
    node = TreeNode(s_arr[mid], None, None)
    if len(s_arr) == 1: return node

    node.left = min_tree(s_arr[0: mid])
    node.right = min_tree(s_arr[mid + 1: len(s_arr)])

    return node

print("Q2 minimal tree")
print(min_tree(test_arr).print_tree())


# 3. List of depths
# Modify BFS to keep track of depth and return map (easy to transform into linked list)

def list_of_depths(node):
    # depth map
    d_map = {}
    
    # queue entries this time should be a tuple (node, depth)
    queue = []
    queue.append((node, 0))

    while len(queue) > 0:
        n, depth = queue.pop(0)

        d_map[depth] = d_map.get(depth, [])
        d_map[depth].append(n)

        if n.left: queue.append((n.left, depth + 1))
        if n.right: queue.append((n.right, depth + 1))

    return d_map

print("Q3 list of depths")
print(list_of_depths(create_tree()))

# 4. Check Balanced
# post order traversal, check at middle 
# (pass depth down in recursive case and return depth in base case)

def mod_post_trav(node, depth):
    if node == None: return (True, depth)

    l_balanced, l_depth = mod_post_trav(node.left, depth + 1)
    r_balanced, r_depth = mod_post_trav(node.right, depth + 1)

    balanced = l_balanced and r_balanced and abs(r_depth - l_depth) <= 1
    max_depth = max(l_depth, r_depth)
    return (balanced, max_depth)

def check_balanced(root):
    balanced, _depth = mod_post_trav(root, 0)
    return balanced

print("Q4 Check BST balance")
print(check_balanced(create_tree()))
print(check_balanced(min_tree(test_arr)))

# 5. Validate BST

def valid_bst(n):
    pass