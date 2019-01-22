"""
In-order traversal, pre-order traversal, post-order traversal
"""


class BiTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
        self.Traversal = []

    def inOrderTraversal(self, node, traversal):
        """
        In-order: visit left -> right -> current
        """
        if node is not None:
            self.inOrderTraversal(node.left, traversal)
            traversal.append(node.val)
            self.inOrderTraversal(node.right, traversal)

    def preOrderTraversal(self, node, traversal):
        """
        Pre-order: visit current -> left -> right
        """
        if node is not None:
            traversal.append(node.val)
            self.preOrderTraversal(node.left, traversal)
            self.preOrderTraversal(node.right, traversal)

    def postOrderTraversal(self, node, traversal):
        """
        Post-order: visit all children before root.
        """
        if node is not None:
            self.postOrderTraversal(node.left, traversal)
            self.postOrderTraversal(node.right, traversal)
            traversal.append(node.val)


if __name__ == '__main__':
    root = BiTreeNode(1)
    root.left = BiTreeNode(2)
    root.right = BiTreeNode(3)
    root.left.left = BiTreeNode(4)
    root.left.right = BiTreeNode(5)
    root.right.left = BiTreeNode(3)

    Tree = Tree(root)
    # Tree.inOrderTraversal(Tree.root, Tree.Traversal)
    Tree.preOrderTraversal(Tree.root, Tree.Traversal)

    print(Tree.Traversal)
    # Tree.preOrderTraversal(Tree.root)
    # Tree.postOrderTraversal(Tree.root, [])