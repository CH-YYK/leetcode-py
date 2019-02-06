class Solution:
    def longestPalindromeSubsequence(self, s):  ## recursive solution
        return self.recur(s, 0, len(s)-1)

    def recur(self, s, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + self.recur(s, i+1, j-1)
        else:
            return max(self.recur(s, i+1, j), self.recur(s, i, j-1))

    def longestPalindromeSubsequence2(self, s):  ## recursive solution with memo
        memo = [[0 for i in range(len(s))] for j in range(len(s))]
        return self.recur_memo(s, 0, len(s)-1, memo)

    def recur_memo(self, s, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return 1
        if memo[i][j] > 0:
            return memo[i][j]
        if s[i] == s[j]:
            memo[i][j] = 2 + self.recur_memo(s, i+1, j-1, memo)
        else:
            memo[i][j] = max(self.recur_memo(s, i+1, j, memo),
                             self.recur_memo(s, i, j-1, memo))
        return memo[i][j]

    def longestPalindromeSubsequence3(self, s):
        memo = [[0 for i in range(len(s))] for j in range(len(s))]
        for l in range(1, len(s)+1):
            for i in range(0, len(s)-l+1):
                j = i + l -1
                if i == j:
                    memo[i][j] = 1
                elif s[i] == s[j]:
                    memo[i][j] = 2 + memo[i+1][j-1]
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j-1])
        return memo[0][len(s)-1]


if __name__ == '__main__':
    s = "bbbab"
    print(Solution().longestPalindromeSubsequence3(s))