# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        inOrder = []
        self.dfsInOrder(root, inOrder)
        ans = node = TreeNode(None)
        for value in inOrder:
            node.right = TreeNode(value)
            node = node.right
        return ans.right


    def dfsInOrder(self, root, traversal):
        if not root:
            return
        self.dfsInOrder(root.left, traversal)
        traversal.append(root.val)
        self.dfsInOrder(root.right, traversal)

    def increasingBST2(self, root):
        if not root:
            return
        ans = node = TreeNode(None)
        for v in self.dfsInOrder_yield(root):
            node.right = TreeNode(v)
            node = node.right
        return ans.right

    def dfsInOrder_yield(self, root):
        if root:
            yield from self.dfsInOrder_yield(root.left)
            yield root.val
            yield from self.dfsInOrder_yield(root.right)