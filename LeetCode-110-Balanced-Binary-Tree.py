class Solution:
    def isBalanced(self, root):
        return not (self.dfs(root) == -1)

    def dfs(self, node):
        if not node:
            return 0
        leftheight = self.dfs(node.left)
        rightheight = self.dfs(node.right)
        if leftheight == -1 or rightheight == -1:
            return -1
        if abs(leftheight-rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    def isBalanced2(self, root):
        return self.dfs2(root)[1]

    def dfs2(self, node):
        if not node:
            return 0, True
        leftH, leftB = self.dfs2(node.left)
        rightH, rightB = self.dfs2(node.right)
        height = max(leftH, rightH) + 1  # current
        balance = leftB and rightB and abs(leftH-rightH) <= 1
        return height, balance

