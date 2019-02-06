import sys
class Solution:
    def numSquares(self, n):  ## recursive solution
        """
        :type n: int
        :rtype: int
        """
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1
        return self.helper(n, nums)

    def helper(self, n, nums):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return min([self.helper(n-num, nums) for num in nums if num <= n]) + 1

    def numSquares2(self, n):  ## recursive solution with memo
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1
        memo = [-1] * (n+1)
        memo[0] = 0
        return self.helper_memo(n, nums, memo)

    def helper_memo(self, n, nums, memo):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if memo[n] >= 0:
            return memo[n]
        memo[n] = min([self.helper_memo(n-num, nums, memo) for num in nums if num <= n]) + 1
        return memo[n]

    def numSquares3(self, n):  ## recursive solution
        res = []
        while len(res) < n:
            m = len(res)
            i = 1
            currMin = sys.maxsize
            while i**2 < m:
                currMin = min(currMin, res[m-i**2]+1)
                i += 1
            res.append(currMin)
        return res[-1]
