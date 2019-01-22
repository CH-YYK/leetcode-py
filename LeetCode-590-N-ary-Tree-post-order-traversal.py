"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        traversal = []
        self.dfsPostOrder(root, traversal)
        return traversal

    def dfsPostOrder(self, root, traversal):
        if not root:
            return
        for child in root.children:
            self.dfsPostOrder(child, traversal)
        traversal.append(root.val)

    def postorder2(self, root):
        if not root:
            return
        stack = [root]
        traversal = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            traversal.append(node.val)
            for child in node.children:
                stack.append(child)
        return traversal
