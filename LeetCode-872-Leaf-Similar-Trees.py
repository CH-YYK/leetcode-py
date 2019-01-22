class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = []
        leaves2 = []
        self.dfsLeaves(root1, leaves1)
        self.dfsLeaves(root2, leaves2)

        return leaves1 == leaves2

    def dfsLeaves(self, root, leaves):
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        if root.left:
            self.dfsLeaves(root.left, leaves)
        if root.right:
            self.dfsLeaves(root.right, leaves)