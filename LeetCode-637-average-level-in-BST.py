# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        total = []
        self.dfsAddValue(root, 0, total)
        return [sum(var)/len(var) for var in total]

    def dfsAddValue(self, root, level, total):
        if not root:
            return
        if len(total) < level+1:
            total.insert(level, [])
        total[level].append(root.val)
        self.dfsAddValue(root.left, level + 1, total)
        self.dfsAddValue(root.right, level + 1, total)

    def averageOfLevels2(self, root):
        if not root:
            return []
        total = [[root.val]]
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if len(total) < level + 1:
                total.insert(level, [])
            total[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return [sum(var)/len(var) for var in total]

    def averageOfLevels3(self, root):
        if not root:
            return []
        total = [[root.val]]
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if len(total) < level + 1:
                total.insert(level, [])
            total[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return [sum(var)/len(var) for var in total]
