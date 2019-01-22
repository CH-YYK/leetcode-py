# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.maxAmount, self.pre, self.curFreq, self.res = 1, None, 1, []
        self.cur = None
        self.dfs(root)
        if self.curFreq > self.maxAmount:
            return [self.cur]
        elif self.curFreq == self.maxAmount:
            return self.res + [self.cur]
        else:
            return self.res

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)

        self.cur = root.val
        if not self.pre is None and root.val == self.pre:
            self.curFreq += 1
        elif self.pre is None:
            self.pre = root.val
        else:
            if self.curFreq > self.maxAmount:
                self.maxAmount = self.curFreq
                self.res = [self.pre]
            elif self.curFreq == self.maxAmount:
                self.res.append(self.pre)
            self.curFreq = 1
        self.pre = self.cur

        self.dfs(root.right)

    def findMode2(self, root):
        """
        O(n), O(n)
        :type root: TreeNode
        :rtype: List[int]
        """
        hashmaps = {}
        self.dfs2(root, hashmaps)
        if not hashmaps:
            return []
        freq = max(hashmaps.items(), key=lambda x: x[1])[1]
        return [value for value in hashmaps if hashmaps[value] == freq]

    def dfs2(self, root, hashmaps):
        if not root:
            return
        hashmaps[root.val] = hashmaps.get(root.val, 0) + 1
        self.dfs2(root.left, hashmaps)
        self.dfs2(root.right, hashmaps)
