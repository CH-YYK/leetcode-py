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

    def inordertraversal_nonrecur(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(BiTreeNode(node.val))
                if node.left:
                    stack.append(node.left)
        return res

    def postordertraversal_nonrecur(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            else:
                stack.append(BiTreeNode(node.val))
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res

    def preordertraversal_nonrecur(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(BiTreeNode(node.val))
        return res





if __name__ == '__main__':
    root = BiTreeNode(1)
    root.left = BiTreeNode(2)
    root.right = BiTreeNode(3)
    root.left.left = BiTreeNode(4)
    root.left.right = BiTreeNode(5)
    root.right.left = BiTreeNode(3)

    Tree = Tree(root)
    # Tree.inOrderTraversal(Tree.root, Tree.Traversal)
    # Tree.inOrderTraversal(Tree.root, Tree.Traversal)
    Tree.preOrderTraversal(Tree.root, Tree.Traversal)
    print(Tree.Traversal)
    #print(Tree.inordertraversal_nonrecur(Tree.root))
    #print(Tree.postordertraversal_nonrecur(Tree.root))
    print(Tree.preordertraversal_nonrecur(Tree.root))
    # Tree.preOrderTraversal(Tree.root)
    # Tree.postOrderTraversal(Tree.root, [])