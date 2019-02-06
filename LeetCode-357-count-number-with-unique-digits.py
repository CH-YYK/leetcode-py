class Solution:
    def countNumbersWithUniqueDigits(self, n):  # dynamic programming
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        memo = [1] * (n+1)
        memo[1] = 9
        for i in range(2, n+1):
            memo[i] = memo[i-1] * (11-i)
        return sum(memo)

    def countNumbersWithUniqueDigits2(self, n):  # dynamic programming O(1)
        if n == 0:
            return 1
        memo = 9
        count = 10
        for i in range(2, n+1):
            memo *= 11-i
            count += memo
        return count