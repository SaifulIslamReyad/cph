class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder(node):
    if node is None: return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def preorder(node):
    if node is None: return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def postorder(node):
    if node is None: return []
    return postorder(node.left) + postorder(node.right) + [node.val]


# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("\nInorder:")
inorder(root)
print("\nPreorder:")
preorder(root)
print("\nPostorder:")
postorder(root)


