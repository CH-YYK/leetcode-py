class Solution(object):
    def numDecodings(self, s):  # recursive solution
        """
        :type s: str
        :rtype: int
        """
        return self.helper_recur(s, 0, len(s))

    def helper_recur(self, s, start, end):
        if start > end:     # no character left in string
            return 0
        if end == start:    # the past case passed
            return 1
        ways = 0
        if int(s[start]) > 0:
            ways += self.helper_recur(s, start + 1, end)
            tmp = int(s[start:start+2])
            if 10 <= tmp <= 26:
                ways += self.helper_recur(s, start + 2, end)
        return ways

    def numDecodings2(self, s):  #recursive solution with memo
        memo = [-1] * len(s)
        self.helper_memo(s, 0, len(s), memo)
        return memo[0]

    def helper_memo(self, s, start, end, memo):
        if start > end:
            return 0
        if end == start:
            return 1
        if memo[start] >= 0:
            return memo[start]
        ways = 0
        if int(s[start]) > 0:
            ways += self.helper_memo(s, start+1, end, memo)
            if 10 <= int(s[start:start+2]) <= 26:
                ways += self.helper_memo(s, start+2, end, memo)
        memo[start] = ways
        return memo[start]

    def numDecodings3(self, s):   # dynamic programming
        memo = [0] * (len(s)+1)
        memo[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            memo[i] += memo[i+1] if int(s[i]) > 0 else 0
            if 10 <= int(s[i:i+2]) <= 26:
                memo[i] += memo[i+2]
        return memo[0]

