class Solution:
    """
    compare: DP [0:N-2] and DP [1:N-1]
    """
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        DP1 = self.helper(nums, 0, len(nums)-2)
        DP2 = self.helper(nums, 1, len(nums)-1)
        return max(DP1, DP2)

    def helper(self, nums, start, end):
        if end < start:
            return 0
        return max(self.helper(nums, start, end-1),
                   self.helper(nums, start, end-2) + nums[end])

    def rob2(self, nums):
        """
        recursive with memory
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [-1] * len(nums)
        memo2 = [-1] * len(nums)
        self.helper2(nums, 0, len(nums)-2, memo)
        self.helper2(nums, 1, len(nums)-1, memo2)
        return max(memo[-2], memo2[-1])

    def helper2(self, nums, start, end, memo):
        if end < start:
            return 0
        if memo[end] >= 0:
            return memo[end]
        memo[end] = max(self.helper2(nums, start, end-1, memo),
                        self.helper2(nums, start, end-2, memo) + nums[end])
        return memo[end]

    def rob3(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 1:
            return max(nums)
        memo1 = [0] * len(nums)
        memo2 = [0] * len(nums)

        nums1 = nums[0:-2]
        nums2 = nums[1:-1]

        memo1[1] = nums1[0]
        memo2[1] = nums2[0]

        for i in range(1, len(nums1)):
            memo1[i+1] = max(memo1[i], memo1[i-1] + nums1[i])

        for i in range(1, len(nums2)):
            memo2[i+1] = max(memo2[i], memo2[i-1] + nums2[i])
        return max(memo1[-1], memo2[-1])