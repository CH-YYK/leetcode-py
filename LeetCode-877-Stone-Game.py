class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.getStone(piles, 0, len(piles)-1) >= 0

    def getStone(self, piles:List[int], l:int, r:int):
        if l == r:
            return piles[l]
        left = piles[l] - self.getStone(piles, l+1, r)
        right = piles[r] - self.getStone(piles, l, r-1)
        return max(left, right)
    
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = [[0 for i in range(len(piles))] for j in range(len(piles))]
        return self.getStone(piles, 0, len(piles)-1, memo) >= 0

    def getStone(self, piles:List[int], l:int, r:int, memo:List[List[int]]):
        if l == r:
            return piles[l]
        if memo[l][r] > 0: return memo[l][r]
        left = piles[l] - self.getStone(piles, l+1, r)
        right = piles[r] - self.getStone(piles, l, r-1)
        memo[l][r] = max(left, right)
        return memo[l][r]

class Solution3:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0 for i in range(len(piles))] for j in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for l in range(2, len(piles)+1):
            for i in range(0, len(piles)-l+1):
                j = i + l-1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][len(piles) - 1] > 0

class Solution4:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [0 for i in range(len(piles))]
        for l in range(2, len(piles)+1):
            for i in range(0, len(piles)- l + 1):
                dp[i] = max(piles[i] - dp[i+1], piles[i+l-1]-dp[i])
        return dp[0] > 0
