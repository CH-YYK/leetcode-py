"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        Depth = []
        for child in root.children:
            if child:
                Depth.append(self.maxDepth(child))
            else:
                Depth.append(0)
        return max(Depth) + 1

    def maxDepth(self, root):
        if not root:
            return
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            maxDepth = max(maxDepth, depth)
            for child in node.children:
                stack.append((child, depth + 1))
        return maxDepth