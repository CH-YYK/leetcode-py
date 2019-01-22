# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfsLeftSum(root, 0, False)

    def dfsLeftSum(self, node, Sum, left):
        if not node.left and not node.right and left:
            return Sum + node.val
        leftSum = self.dfsLeftSum(node.left, Sum, True) if node.left else 0
        rightSum = self.dfsLeftSum(node.right, Sum, False) if node.right else 0
        return leftSum + rightSum

    def sumOfLeftLeaves2(self, root):
        if not root:
            return 0
        stack = [(root, False)]
        Sum = 0
        while stack:
            node, Left = stack.pop()
            if not node.left and not node.right and Left:
                Sum += node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, True))
        return Sum
