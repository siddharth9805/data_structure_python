class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(node):
    # Base case: An empty tree has height -1
    if node is None:
        return -1
    # Height of a node is 1 + max of left height and right height
    return 1 + max(height(node.left), height(node.right))


def maxDistance(root):
    """
    Function to find the maximum distance (maximum difference) between any two leaf nodes in an AVL tree.
    """
    # Base case: If the tree is empty, return 0
    if root is None:
        return 0

    # Use the height function to calculate the height of left and right subtrees
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    # The maximum distance between any two leaves in the AVL tree
    # is the sum of the heights of the left and right subtrees plus 2
    return leftHeight + rightHeight + 2


# Example usage:
# Constructing a simple AVL tree for demonstration
#          10
#         /  \
#        5    15
#       / \     \
#      2   7     20
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print("Maximum distance between any two leaf nodes:", maxDistance(root))