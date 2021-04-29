# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")


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
    
    return root
    
def inorder_traversal(root):
    ret = []

    if root == None: return ret

    ret = ret + inorder_traversal(root.left)
    ret.append(root.val)
    ret = ret + inorder_traversal(root.right)
    
    return ret
    
def preorder_traversal(root):
    ret = []

    if root == None: return ret

    ret.append(root.val)
    ret = ret + preorder_traversal(root.left)
    ret = ret + preorder_traversal(root.right)
    
    return ret
    
def postorder_traversal(root):
    ret = []

    if root == None: return ret

    ret = ret + preorder_traversal(root.left)
    ret = ret + preorder_traversal(root.right)
    ret.append(root.val)
    
    return ret


root = create_tree()
root.print_tree()
print(inorder_traversal(root))
print(preorder_traversal(root))
print(postorder_traversal(root))