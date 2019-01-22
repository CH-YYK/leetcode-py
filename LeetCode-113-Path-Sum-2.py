# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfsFindSum(root, [], sum, res)
        return res

    def dfsFindSum(self, root, paths, sum, total):
        if not root.left and not root.right:
            if root.val == sum:
                paths += [root.val]
                total.append(paths)
            return
        if not root:
            return
        self.dfsFindSum(root.left, paths + [root.val], sum-root.val, total)
        self.dfsFindSum(root.right, paths + [root.val], sum-root.val, total)