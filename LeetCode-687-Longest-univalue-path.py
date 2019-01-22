# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.integer = 0
        self.dfs(root)
        return self.integer

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        leftl = left + 1 if root.left and root.left.val == root.val else 0
        rightl = right + 1 if root.right and root.right.val == root.val else 0
        self.integer = max(self.integer, leftl + rightl)
        return max(leftl, rightl)
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        leftL = left + 1 if root.left and root.left.val == root.val else 0
        rightL = right + 1 if root.right and root.right.val == root.val else 0
        self.integer = max(self.integer, leftL + rightL)
        return max(leftL, rightL)