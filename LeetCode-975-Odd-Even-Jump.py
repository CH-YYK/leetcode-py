class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        dp = [[0] * n for i in range(2)]
        dp[0][-1] = 1
        dp[1][-1] = 1
        res = 0
        for j in range(len(A) - 1, -1, -1):
            if next_higher[j] > 0:
                dp[0][j] = dp[1][next_higher[j]]
            res += dp[0][j]
            if next_lower[j] > 0:
                dp[1][j] = dp[0][next_lower[j]]
        return res