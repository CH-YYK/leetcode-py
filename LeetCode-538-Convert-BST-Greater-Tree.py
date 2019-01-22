# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.Sum = 0
        self.reverseInorder(root)
        return root

    def reverseInorder(self, root):
        if not root:
            return
        self.reverseInorder(root.right)
        root.val += self.Sum
        self.Sum = root.val
        self.reverseInorder(root.left)