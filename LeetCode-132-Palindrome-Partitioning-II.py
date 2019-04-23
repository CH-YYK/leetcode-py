import sys

class Solution:
    def minCut(self, s: str) -> 'List[List[str]]':
        self.memo = {}
        return self.dfs(s, len(s) - 1) - 1

    def dfs(self, s, i):
        if i < 0:
            return 0
        if i == 0:
            return 1
        if i in self.memo:
            return self.memo[i]
        res = sys.maxsize
        for l in range(i + 1, 0, -1):
            if self.is_palindrom(s[i-l+1: i+1]):
                res = min(res, self.dfs(s, i-l))
        if res == sys.maxsize:
            self.memo[i] = res
        else:
            self.memo[i] = res + 1
        return self.memo[i]

    def is_palindrom(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution2:
    def minCut(self, s: str) -> 'List[List[str]]':
        dp = [i - 1 for i in range(n+1)]
        for i in range(n+1):
            j = 0
            while i - j >= 0 and i + j < n and s[i + j] == s[i-j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j + 1] + 1)
                j += 1
        return dp[n]

    

if __name__ == "__main__":
    ans = Solution().minCut('aab')
    print(ans)