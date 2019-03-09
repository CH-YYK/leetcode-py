# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.memo = {}
        return self.recur(root)
    def recur(self, root):
        if not root:
            return 0
        if root in self.memo: 
            return self.memo[root]
        max1 = root.val
        max2 = self.recur(root.left) + self.recur(root.right)
        if root.left and root.left.left:
            max1 += self.recur(root.left.left)
        if root.left and root.left.right:
            max1 += self.recur(root.left.right)
        if root.right and root.right.left:
            max1 += self.recur(root.right.left)
        if root.right and root.right.right:
            max1 += self.recur(root.right.right)
        self.memo[root] = max(max1, max2)
        return self.memo[root]

