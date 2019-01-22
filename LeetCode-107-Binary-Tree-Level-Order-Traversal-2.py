# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        dfs recursive
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-level-1].append(node.val)
            self.dfs(node.left, level + 1, res)
            self.dfs(node.right, level + 1, res)

    def levelOrderBottom2(self, root):
        """
        dfs stack
        """
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    def levelOrderBottom3(self, root):
        """
        bfs queue
        """
        queue = [(root, 0)]
        res = []
        while queue:
            node, level = queue.pop(0)
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res

