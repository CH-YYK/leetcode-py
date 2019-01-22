# Definition for a binary tree node.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfsLCA(root, p, q)

    def dfsLCA(self, root, p, q):
        """
        recursive
        """
        if p.val <= root.val and root.val <= q.val:
            return root
        if p.val >= root.val and root.val >= q.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.dfsLCA(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.dfsLCA(root.right, p, q)

    def lowestCommonAncestor2(self, root, p, q):
        """
        Iterative method:
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

