class Solution:
    def rob(self, nums):  ## recursive solution
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.recurRob(nums, len(nums)-1)

    def recurRob(self, nums, index):
        if index < 0:
            return 0
        return max(self.recurRob(nums, index-1), self.recurRob(nums, index-2) + nums[index])

    def rob2(self, nums):  ## recursive solution with memory
        memo = [-1] * len(nums)
        return self.recurRob_memo(nums, len(nums)-1, memo)

    def recurRob_memo(self, nums, index, memo):
        if index < 0:
            return 0
        if memo[index] >= 0:
            return memo[index]
        memo[index] = max(self.recurRob_memo(nums, index-1, memo),
                          self.recurRob_memo(nums, index-2, memo)+nums[index])
        return memo[index]

    def rob3(self, nums):  ## iterative solution with memo
        """
        memo[i] = max(memo[i-1], memo[i-2]+nums[i])
        """
        if len(nums) == 0:
            return []
        memo = [0] * (len(nums)+1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + val)
        return memo[-1]

    def rob4(self, nums):  ## two variable method
        prev1 = 0
        prev2 = 0
        for num in nums:
            tmp = prev2
            prev2 = max(prev2, prev1 + num)
            prev1 = tmp
        return prev2