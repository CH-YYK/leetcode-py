class Solution(object):
    def numTrees(self, n):  # recursive solution
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        count = 0
        for i in range(n):
            leftnodes = self.numTrees(i)
            rightnodes = self.numTrees(n-i-1)
            count += leftnodes * rightnodes
        return count

    def numTrees2(self, n):  # recursive solution with memo
        memo = [0] * n
        self.helper_memo(n, memo)
        return memo[n-1]

    def helper_memo(self, n, memo):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if memo[n-1] > 0:
            return memo[n-1]
        count = 0
        for i in range(n):
            count += self.helper_memo(i, memo) * self.helper_memo(n-i-1, memo)
        memo[n-1] = count
        return memo[n-1]

    def numTrees3(self, n):  # dynamic programming
        if n == 0:
            return 1
        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1
        for num in range(1, n+1):
            for i in range(num+1):
                memo[num] += memo[i] * memo[num-i-1]
        return memo[n]



