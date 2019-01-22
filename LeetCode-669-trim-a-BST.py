# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root

    def trimBST2(self, root, L, R):
        if not root:
            return
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left

        tmp = root
        while tmp:
            while tmp.left and tmp.left.val < L:
                tmp.left = tmp.left.right
            tmp = tmp.left
        tmp = root
        while tmp:
            while tmp.right and tmp.right.val > R:
                tmp.right = tmp.right.left
            tmp = tmp.right
        return root