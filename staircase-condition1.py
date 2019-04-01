class Solution:
    def numWays(self, n, canstand):
        self.memo = {}
        return self.helper(n, canstand)

    def helper(self, n, canstand):
        if n == 0:
            return 1
        if not canstand[n-1]:
            return 0
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = 0
        for i in [3, 2, 1]:
            if n >= i:
                self.memo[n] += self.helper(n-i)
        return self.memo[n]

class Solution2:
    def numWays(self, n):
        """
        even: 2, 4
        odd: 1, 3

        0: odd
        1: even

        odd follows even
        even follows odd
        """
        dp = [[0] * (n+1) for i in range(2)]
        dp[1][0] = 1

        for i in range(1, n+1):
            if i >= 1:
                dp[0][i] += dp[1][i-1]
            if i >= 2:
                dp[1][i] += dp[0][i-2]
            if i >= 3:
                dp[0][i] += dp[1][i-3]
            if i >= 4:
                dp[1][i] += dp[0][i-4]
        return dp[0][n] + dp[1][n]
