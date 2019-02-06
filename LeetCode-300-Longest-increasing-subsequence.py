import sys
class Solution:
    def lengthOfLIS(self, nums):
        return self.lengthoflIS(nums, -sys.maxsize, 0)

    def lengthoflIS(self, nums, prev, index):
        if index == len(nums):
            return 0
        taken = 0
        if nums[index] > prev:
            taken = 1 + self.lengthoflIS(nums, nums[index], index+1)
        untaken = self.lengthoflIS(nums, prev, index+1)
        return max(taken, untaken)

    def lengthOfLIS2(self, nums):  ## recursive with memory
        memo = [[-1 for i in nums] for j in range(len(nums) + 1)]
        return self.lengthofLIS_memo(nums, -1, 0, memo)

    def lengthofLIS_memo(self, nums, prevIndex, index, memo):
        if index == len(nums):
            return 0
        taken = 0
        if memo[prevIndex+1][index] >= 0:
            return memo[prevIndex+1][index]
        if prevIndex < 0 or nums[index] > nums[prevIndex]:
            taken = 1 + self.lengthofLIS_memo(nums, index, index+1, memo)
        untaken = self.lengthofLIS_memo(nums, prevIndex, index + 1, memo)
        memo[prevIndex+1][index] = max(taken, untaken)
        return memo[prevIndex+1][index]

    def lengthOfLIS3(self, nums):  ## dynamic programming
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(dp[j], maxval)
            dp[i] = maxval + 1
        return dp[-1]

if __name__ == '__main__':
    array = [10,9,2,5,3,7,101,18]
    solution = Solution()
    print(solution.lengthOfLIS3(array))
