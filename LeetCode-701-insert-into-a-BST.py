# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if val < node.val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val)
        return root
