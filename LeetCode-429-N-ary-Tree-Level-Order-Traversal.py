"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        self.dfsLevelOrder(root, 0, res)
        return res

    def dfsLevelOrder(self, root, level, total):
        if not root:
            return
        if len(total) < level + 1:
            total.insert(level, [])
        total[level].append(root.val)
        for child in root.children:
            self.dfsLevelOrder(child, level + 1, total)

    def levelOrder2(self, root):
        if not root:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if len(res) < level + 1:
                res.insert(level, [])
            res[level].append(node.val)
            for child in range(len(node.children)-1, -1, -1):
                stack.append((node.children[child], level + 1))
        return res