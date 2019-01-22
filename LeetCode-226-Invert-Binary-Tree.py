class Solution:
    def invertTree(self, root):
        self.dfsInvert(root)
        return root

    def dfsInvert(self, node):
        """
        dfs swapped left and right
        """
        if node:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            self.dfsInvert(node.left)
            self.dfsInvert(node.right)