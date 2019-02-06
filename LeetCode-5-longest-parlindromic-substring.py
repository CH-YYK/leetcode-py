class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = [[0 for i in range(len(s))] for j in range(len(s))]
        for l in range(1, len(s)+1):
            for i in range(0, len(s) - l + 1):
                j = i+l-1
                if i == j:
                    memo[i][j] = 1
                elif j - i == 1:
                    if s[j] == s[i]:
                        memo[i][j] = j-i+1
                    else:
                        memo[i][j] = 0
                else:
                    if memo[i+1][j-1] > 0 and s[i] == s[j]:
                        memo[i][j] = j-i+1
                    else:
                        memo[i][j] = 0

        res = (0, 0)
        maxLength = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if memo[i][j] >= maxLength:
                    maxLength = memo[i][j]
                    res = i, j
        return s[res[0]:res[1]+1]



if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
