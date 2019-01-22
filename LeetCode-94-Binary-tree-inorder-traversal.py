# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfsInorder(root, res)
        return res

    def dfsInorder(self, root, traversal):
        if root:
            self.dfsInorder(root.left, traversal)
            traversal.append(root.val)
            self.dfsInorder(root.right, traversal)

    def inorderTraversal(self, root):
        if not root:
            return
        stack = [root]
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

