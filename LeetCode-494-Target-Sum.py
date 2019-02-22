class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        return self.helper(nums, S, 0, 0)
    
    def helper(self, nums, S, i, curr):
        if i == len(nums) and curr == S:
            return 1
        elif i == len(nums):
            return 0
        return self.helper(nums, S, i+1, curr+nums[i]) + self.helper(nums, S, i+1, curr-nums[i])

class Solution2:
    def findTargetSumWays(self, nums, S):
        memo = [[-1 for j in range(2*sum(nums)+1)] for i in range(len(nums)+1)]
        self.helper(nums, S, 0, memo, sum(nums))
        return memo[0][S+sum(nums)]
    
    def helper(self, nums, S, i, memo, shift):
        if i == len(nums) and S == 0:
            return 1
        elif i == len(nums) or S > sum(nums):
            return 0
        if memo[i][S + shift] >= 0:
            return memo[i][S + shift]
        else:
            memo[i][S + shift] = self.helper(nums, S-nums[i], i+1, memo, shift)+\
                self.helper(nums, S+nums[i], i+1, memo, shift)
            return memo[i][S+shift]

class Solution3:
    def findTargetSumWays(self, nums, S):
        if S > sum(nums) or S < -sum(nums): return 0
        Sum = (S + sum(nums)) // 2
        # find out how many ways to subset nums so that the subset add up to Sum
        
        dp = [[0 for i in range(Sum+1)] for j in range(len(nums))]
        dp[0][0] = 1
        if nums[0] <= Sum:
            dp[0][nums[0]] = 1

        for i in range(1, len(nums)):
            for j in range(0, Sum+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)-1][Sum]

if __name__ == "__main__":
    nums = [1,1,1,1,1]
    S = 3
    print(Solution3().findTargetSumWays(nums, S))