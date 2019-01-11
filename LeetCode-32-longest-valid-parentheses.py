"""
When there a pair is encountered, throw the left side away from the list
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = [-1]
        result = 0
        for i, char in enumerate(s):
            if char == ')' and longest[-1] >= 0 and s[longest[-1]] == '(':
                longest.pop()
                result = max(result, i - longest[-1])
            else:
                longest.append(i)
        return result

    def longestValidParentheses(self, s):
        dp = [0 for i in range(len(s))]
        leftcount = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                leftcount += 1
            elif leftcount > 0:
                dp[i] = dp[i-1] + 2
                dp[i] += dp[i-dp[i]] if i-dp[i] >= 0 else 0
                result = max(result, dp[i])
                leftcount -= 1
        return result
