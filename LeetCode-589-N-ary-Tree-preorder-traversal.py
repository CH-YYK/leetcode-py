"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        traversal = []
        self.dfsPreOrder(root, traversal)
        return traversal

    def dfsPreOrder(self, root, traversal):
        if not root:
            return
        traversal.append(root.val)
        for child in root.children:
            self.dfsPreOrder(child, traversal)

    def preorder2(self, root):
        if not root:
            return []
        stack = [root]
        traversal = []
        while stack:
            node = stack.pop(0)
            if not node:
                continue
            traversal.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return traversal