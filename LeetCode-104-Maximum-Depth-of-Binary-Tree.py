# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfsHeight(root, 0)

    def dfsHeight(self, root, depth):
        """
        recursively
        """
        if not root:
            return depth
        leftHeight = self.dfsHeight(root.left, depth+1) if root.left else 0
        rightHeight = self.dfsHeight(root.right, depth+1) if root.right else 0
        return max(leftHeight, rightHeight) + 1

    def maxDepth2(self, root):
        if not root:
            return 0
        stack = [(root, 0)]
        depth = -1
        while stack:
            node, currDepth = stack.pop()
            if not node.left and not node.right:
                depth = max(depth, currDepth) if depth >= 0 else currDepth
            else:
                if node.right:
                    stack.append((node.right, currDepth+1))
                if node.left:
                    stack.append((node.left, currDepth + 1))
        return depth

    