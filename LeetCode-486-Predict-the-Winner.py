class Solution:
    # O(2^N), O(N)
    # getScore(nums, l, r) the max score that could be obtained by current player given 
    # current numbers
    # at every step, current player can add score nums[l] or nums[r]
    def PredictTheWinner(self, nums: 'List[int]') -> 'bool':
        return self.getScore(nums, 0, len(nums) - 1) >= 0
    
    def getScore(self, nums:'List[int]', l:int, r:int) -> 'int':
        if l == r:
            return nums[l]
        # current score minus maxScore an anti-player can get
        left = nums[l] - self.getScore(nums, l+1, r)
        right = nums[r] - self.getScore(nums, l, r-1)
        return max(left, right)

class Solution2:
    
    def PredictTheWinner(self, nums: 'List[int]') -> 'bool':
        memo = [[0 for i in range(len(nums))] for j in range(len(nums))]
        return self.getScore(nums, 0, len(nums)-1, memo) >= 0

    def getScore(self, nums:'List[int]', l:int, r:int, memo:'List[List[int]]') -> 'int':
        if l == r:
            return nums[l]
        if memo[l][r] > 0:
            return memo[l][r]
        left = nums[l] - self.getScore(nums, l+1, r, memo)
        right = nums[r] - self.getScore(nums, l, r-1, memo)
        memo[l][r] = max(left, right)
        return memo[l][r]