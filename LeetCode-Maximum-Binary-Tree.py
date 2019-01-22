class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.dfsBuildTree(nums, 0, len(nums) - 1)

    def dfsBuildTree(self, nums, start, end):
        if start > end:
            return
        maxNum = max(nums[start:end+1])
        maxId = nums[start:end+1].index(maxNum) + start
        root = TreeNode(nums[maxId])
        root.left = self.dfsBuildTree(nums, start, maxId-1)
        root.right = self.dfsBuildTree(nums, maxId+1, end)
        return root

    def constructMaximumBinaryTree2(self, nums):
        if not nums:
            return
        return self.dfsTree(nums)

    def dfsTree(self, nums):
        if not nums:
            return
        else:
            maxNum = max(nums)
            maxId = nums.index(maxNum)
            root = TreeNode(maxNum)
            root.left = self.dfsTree(nums[:maxId])
            root.right = self.dfsTree(nums[maxId+1:])
            return root


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.helper(nums)
        return root

    def helper(self, nums):
        if nums:
            currMax = max(nums)
            currI = nums.index(currMax)

            nNode = TreeNode(currMax)
            nNode.left = self.helper(nums[0:currI])
            nNode.right = self.helper(nums[currI + 1:])
            return nNode
        return None