import sys

class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0)

    def helper(self, nums, i):
        if i >= len(nums)-1:
            return 0
        res = []
        for j in range(1, nums[i]+1):
            res.append(self.helper(nums, i+j) + 1)
        if res:
            return min(res)
        else:
            return sys.maxsize

class Solution2:
    def jump(self, nums):
        memo = {}
        return self.helper(nums, 0, memo)

    def helper(self, nums, i, memo):
        if i >= len(nums)-1:
            return 0
        if i in memo:
            return memo[i]
        res = []
        for j in range(1, nums[i]+1):
            res.append(self.helper(nums, i+j, memo) + 1)
        if res:
            memo[i] = min(res)
        else:
            memo[i] = sys.maxsize
        return memo[i]


class Solution3:
    def jump(self, nums):
        dp = [0 for i in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            if j + nums[j] >= len(nums)-1:
                dp[j] = 1
            else:
                res = dp[j+1:j+nums[j]+1]
                dp[j] = min(res) + 1 if res and min(res) < sys.maxsize else sys.maxsize
        return dp[0]

class Solution4:
    def jump(self, nums):
        start = end = step = 0
        n = len(nums)
        maxend = 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for j in range(start, end+1):
                if j + nums[j] >= n-1:
                    return step
                maxend = max(maxend, j+nums[j])
            start = end + 1
            end = maxend
        return step


if __name__ == '__main__':
    nums = [1,2,1,1,1]
    print(Solution4().jump(nums))