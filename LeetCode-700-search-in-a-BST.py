# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)

    def searchBST2(self, root, val):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == val:
                return node
            if node.val < val:
                stack.append(node.right)
            if node.val > val:
                stack.append(node.left)
        return