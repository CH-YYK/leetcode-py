class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, len(nums)-1)

    def helper(self, nums, index):
        if index < 0:
            return 0
        return max(self.helper(nums, index-1), self.helper(nums, index-2) + nums[index])