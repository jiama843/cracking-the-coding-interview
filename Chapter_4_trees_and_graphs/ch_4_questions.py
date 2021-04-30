import copy

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
        self.parent = None

    def insert(self, n):
        if(self.val < n.val):
            if self.right == None:
                self.right = n
                n.parent = self
            else:
                self.right.insert(n)
        elif(self.val > n.val):
            if self.left == None:
                self.left = n
                n.parent = self
            else:
                self.left.insert(n)

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

def create_p_tree():
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

######################################################################

# 1. Route between nodes
# dijkstra's algo + find smallest path in dist
# Modify BFS to return if dest in visited set

def route_btw_nodes(g, n, dest):
    visited = set()

    queue = []
    queue.append(n)
    visited.add(n)
    
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

######################################################################

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

######################################################################

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

l_depth = list_of_depths(create_tree())
for k, v in l_depth.items():
    v = list(map(lambda n: n.val, v))
    print(v)

######################################################################

# 4. Check Balanced
# Best way is to store height in BST as part of structure
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
print(check_balanced(create_tree())) # Expected False
print(check_balanced(min_tree(test_arr))) # Expected True

######################################################################

# 5. Validate BST
# Can mod BST to keep track of parent nodes
# Good way is to use inorder traversal and see if its sorted

reg_bin_tree = min_tree([1,4,2,5,0,6])
def valid_bst(n):
    if n == None: return True

    l_check = n.left == None or n.left.val < n.val
    r_check = n.right == None or n.right.val > n.val

    valid_node = l_check and r_check
    valid_left = valid_bst(n.left)
    valid_right = valid_bst(n.right)

    return valid_node and valid_left and valid_right

print("Q5 Valid BST")
print(valid_bst(reg_bin_tree)) # Expected False
print(valid_bst(create_tree())) # Expected True

######################################################################

# 6. Successor
# Tricker than it leads on to be
# If there is a right node, go right once and find leftmost node
# Otherwise find the first ancestor that is larger than it

# Could use while loops for all of these and save stack space
# but recursion is easier
def find_next_ancestor(n):
    curr = n
    while curr != None and curr.val <= n.val:
        curr = curr.parent
    
    return curr

def find_leftmost(n):
    if n.left == None:
        return n
    else:
        return find_leftmost(n.left)

def successor(n):
    if n.right != None:
        return find_leftmost(n.right)
    else:
        return find_next_ancestor(n)

test_node_left = create_p_tree().left.left.right
test_node_anc = create_p_tree().left.left.right.right

print("Q6 Successor")
print(successor(test_node_left).val) # Expected 3
print(successor(test_node_anc).val) # Expected 5

######################################################################

# 7. Build order
# Two adjacency lists (forward dependency and backward dependency)
# Modify BFS so that if there are still deps for a node, place it in the back of queue
# Generate list of dep_order alongside visited list

# class Node:
#     self.val: int
#     self.neighbors: []
#     self.visited: bool

test_proj = ["a", "b", "c", "d", "e", "f"]
test_deps = [
    ("a", "d"),
    ("f", "b"),
    ("b", "d"),
    ("f", "a"),
    ("d", "c"),
    ("f", "c")
]

def pop_deps(proj, deps):
    dep_for, dep_bac = {}, {}

    for p in proj:
        dep_for[p], dep_bac[p] = set(), set()

    # Populate dependency maps
    for dep in deps:
        d, p = dep

        dep_for[p].add(d)
        dep_bac[d].add(p)

    return dep_for, dep_bac

def build_order(proj, deps):
    dep_for, dep_bac = pop_deps(proj, deps)
    print(dep_for)
    print(dep_bac)

    visited = set()
    queue = []
    dep_order = []

    for p in proj:
        if len(dep_for[p]) == 0:
            queue.append(p)
            visited.add(p)

    while len(queue) > 0:
        v = queue.pop(0)
        dep_order.append(v)

        for neighbor in dep_bac[v]:
            # Don't append if there are still dependencies to be resolved
            if not dep_for[neighbor].issubset(visited): continue

            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    # Check for invalid dep
    if len(proj) != len(dep_order): return "ERROR"

    return dep_order

print("Q7 Build Order")
print(build_order(test_proj, test_deps))
print(build_order(test_proj, test_deps + [("c", "a")]))

######################################################################

# 8. First Common Ancestor
# Integrate parent/visited into the TreeNode
# Trace the first node upward and set all nodes to visted along the way
# Trace the second node upward and stop

def fca(n1, n2):
    # Trace n1
    while n1 != None:
        n1.visited = True
        n1 = n1.parent

    # Trace n2 and print common ancestor
    while n2 != None:
        if n2.visited: return n2
        n2 = n2.parent

    return None

print("Q8 First common ancestor -> Skipped since it seems simple enough")


######################################################################

# Q9. BST Sequences
# Divide and conquer
# Base case: return value
# Combine: merge all combinations of lists

# All combinations of the right subtree can occur between 
# all combs of the left subtree and vice-versa
def bst_seq_combine(curr_val, lscomb, rscomb):
    comb_list = []
    for l in lscomb:
        for i in range(0, len(l)):
            for r in rscomb:
                comb = [curr_val] + l[0:i] + r + l[i:len(l)]
                comb_list.append(comb)

    for r in rscomb:
        for i in range(0, len(r)):
            for l in lscomb:
                comb = [curr_val] + r[0:i] + l + r[i:len(r)]
                comb_list.append(comb)

    return comb_list

def bst_sequences(node):
    if node == None: return [[]]
    if node.left == None and node.right == None: return [[node.val]]

    lscomb = bst_sequences(node.left)
    rscomb = bst_sequences(node.right)

    curr_combs = bst_seq_combine(node.val, lscomb, rscomb)

    # remove duplicates (there is a problem with returning [[]], 
    # but would need to dig deeper to find a soln)
    curr_combs = [tuple(v) for v in curr_combs]
    curr_combs = list(dict.fromkeys(curr_combs))
    curr_combs = [list(v) for v in curr_combs]

    return curr_combs

print("Q9 BST sequences")
print(bst_sequences(create_tree()))


######################################################################

# Q10. Check Subtree
# BFS for potential root nodes, generate list and compare all of them
# Keep track of height + size in tree node and can use those to figure it out

print("Q10 Check Subtree -> Skipped due to time")

######################################################################

# Q11. Random Node
# 