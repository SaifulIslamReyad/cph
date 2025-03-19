class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def dfs_recursive(node):
    if not node:
        return
    print(node.val)  # Process the node
    for child in node.children:
        dfs_recursive(child)

def dfs_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)  # Process the node
        stack.extend(reversed(node.children))  # Push children in reverse order


root = TreeNode(1)
root.children.append(TreeNode(2))
root.children.append(TreeNode(3))
root.children[0].children.append(TreeNode(4))
root.children[0].children.append(TreeNode(5))
root.children[1].children.append(TreeNode(6))

print("Recursive DFS:")
dfs_recursive(root)

print("\nIterative DFS:")
dfs_iterative(root)
