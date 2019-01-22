class Solution:
    def climbStairs(self, n):   ## recursive solution
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):   ## recursive with memo
        if n<2:
            return 1
        memo = [-1] * (n+1)
        self.recurMemo(n, memo)
        return memo[n]

    def recurMemo(self, n, memo):
        if n < 2:
            return 1
        if memo[n] >= 0:
            return memo[n]
        memo[n] = self.recurMemo(n-1, memo) + self.recurMemo(n-2, memo)
        return memo[n]

    def climbStairs3(self, n):
        if n < 2:
            return 1
        memo = [0] * (len(n) + 1)
        for i in range(2, len(memo)):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
