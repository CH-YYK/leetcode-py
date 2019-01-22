"""
You are given two strings, build a function to find their longest common sub-sequence

O(2^(L1+L2)) --> O(L1*L2)
"""


class Solution:
    def longestCommonSequence(self, string1, string2):
        memo = [[None for i2 in range(len(string2))] for i1 in range(len(string1))]
        return self.solutionMemo(string1, string2, 0, 0, memo)

    def solutionRecur(self, string1, string2, i1, i2):
        if i1 == len(string1) or i2 == len(string2):
            return ""
        if string1[i1] == string2[i2]:

            return string1[i1] + self.solutionRecur(string1, string2, i1+1, i2+1)
        else:
            return max(self.solutionRecur(string1, string2, i1+1, i2),
                       self.solutionRecur(string1, string2, i1, i2+1), key=len)


    def solutionMemo(self, string1, string2, i1, i2, memo):
        if i1 == len(string1) or i2 == len(string2):
            return ""
        if memo[i1][i2]:
            return memo[i1][i2]
        if string1[i1] == string2[i2]:
            memo[i1][i2] = string1[i1] + self.solutionMemo(string1, string2, i1+1, i2+1, memo)
            return memo[i1][i2]
        result1 = self.solutionMemo(string1, string2, i1+1, i2, memo)
        result2 = self.solutionMemo(string1, string2, i1, i2+1, memo)
        if len(result1) > len(result2):
            return result1
        else:
            return result2

if __name__ == '__main__':
    string1 = 'cbcd'
    string2 = 'ccd'
    print(Solution().longestCommonSequence(string1, string2))
