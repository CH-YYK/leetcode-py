import sys

class Solution:
    # brute force solution O(n^2)
    # divide the string into two parts. Count and store the number of ways
    # needed to flip all left parts to zeros plus those needed to flip all 
    # right parts to ones
    def minFlipsMonoIncr(self, S: str) -> int:
        ans = sys.maxsize
        for k in range(len(S)+1):
            ans1 = 0
            for i in range(0, k):
                if S[i] != '0':
                    ans1 += 1
            
            ans2 = 0
            for j in range(k, len(S)):
                if S[j] != '1':
                    ans2 += 1 
            ans = min(ans1 + ans2, ans)
        return ans

class Solution2:
    # DP version O(n) in time O(n) in space
    # create two arrays to cache
    # e.g l1[i] stored the number of flips needed to flip all zeros on the left
    #     l2[j] stored the number of flips needed to flip all ones on the right
    def minFlipsMonoIncr(self, S:str) -> int:
        l1 = [0] * (len(S) + 1)
        l2 = [0] * (len(S) + 1)
        
        for i in range(len(S)):
            l1[i+1] += l1[i]
            if S[i] != '0':
                l1[i+1] += 1
        
        for j in range(len(S) - 1, -1, -1):
            l2[j] += l2[j+1]
            if S[j] != '1':
                l2[j] += 1 
                
        ans = l1[0] + l2[0]
        for i in range(1, len(S) + 1):
            ans = min(ans, l1[i]+l2[i])
        return ans

class Solution3:
    def minFlipsMonoIncr(self, S):
        dp = [[0 for i in range(len(S))] for j in range(2)]
        if S[0] == '0':
            dp[0][0] = 0
            dp[1][0] = 1
        else:
            dp[0][0] = 1
            dp[1][0] = 0
        for k in range(1, len(S)):
            if S[k] == '0':
                dp[0][k] = dp[0][k-1]
                dp[1][k] = min(dp[1][k-1], dp[0][k-1]) + 1
            else:
                dp[1][k] = min(dp[0][k-1], dp[1][k-1])
                dp[0][k] = dp[0][k-1] + 1
        return min(dp[1][-1], dp[0][-1])

class Solution4:
    def minFlipsMonoIncr(self, S):
        val0 = 0
        val1 = 1
        for i in range(1, len(S) + 1):
            val0 = val0 + (S[i-1] == '1')
            val1 = min(val1, val0) + (S[i-1] == '0')
        return min(val0, val1)

if __name__ == "__main__":
    S = '11011'
    ans = Solution3().minFlipsMonoIncr(S)
    print(ans)
