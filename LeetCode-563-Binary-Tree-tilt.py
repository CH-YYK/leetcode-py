class Solution:
    def findTilt(self, root):
        self.sum = 0
        self.dfsTilt(root)
        return self.sum

    def dfsTilt(self, root):
        if not root:
            return 0
        left = self.dfsTilt(root.left)
        right = self.dfsTilt(root.right)
        self.sum += abs(left - right)
        return left + right + root.val
