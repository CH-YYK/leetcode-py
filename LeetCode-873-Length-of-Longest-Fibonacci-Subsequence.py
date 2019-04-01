class Solution:
    def lenLongestFibSubseq(self, A: 'List[int]') -> int:
        n = len(A)
        hashmap = {}
        for i in range(0, n):
            hashmap[A[i]] = i 
        dp = [[2 for i in range(n)] for j in range(n)]
        ans = 0
        for j in range(n):
            for k in range(j+1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                if a_i not in hashmap:
                    continue
                i = hashmap[a_i]
                dp[j][k] = dp[i][j] + 1
                ans = max(ans, dp[j][k])
        return ans

if __name__ == "__main__":
    A = [1,3,7,11,12,14,18]
    print(Solution().lenLongestFibSubseq(A))