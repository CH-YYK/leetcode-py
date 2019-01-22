import sys
class Solution:
    def minDepth(self, root):
        return self.dfsMinDepth(root)

    def dfsMinDepth(self, node):
        if not node:
            return 0
        if not node.left:
            return 1 + self.dfsMinDepth(node.right)
        if not node.right:
            return 1 + self.dfsMinDepth(node.left)
        return min(self.dfsMinDepth(node.left), self.dfsMinDepth(node.right)) + 1

    def dfsMinDepth2(self, node):
        if not node:
            return 0
        leftDepth = self.dfsMinDepth(node.left)
        rightDepth = self.dfsMinDepth(node.right)
        if leftDepth == 0: return rightDepth + 1
        if rightDepth == 0: return leftDepth + 1
        return min(leftDepth, rightDepth) + 1

    def minDepth2(self, root):
        """
        DFS with stack
        """
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0

        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                res = min(res, level) if res > 0 else level
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return res

    def minDepth3(self, root):
        """
        BFS with queue
        """
        if not root:
            return 0
        queue = [(root, 0)]
        res = sys.maxsize
        while queue:
            node, level = queue.pop(0)
            if node and not node.left and not node.right:
                res = min(res, level)
            elif node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res


