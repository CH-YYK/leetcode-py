class Solution:
    def canIWin(self, M: int, T: int) -> bool:
        Sum = M * (M+1) // 2
        if(Sum < T):
            return False
        if(T <= 0):
            return True
    
    def recurCanIWin(self, M:int, T:int) -> bool:
        if T <= 0:
            return False
        for i in range(0, M):
            if !self.recurCanIWin(M, )



class Solution2:
    def canIWin(self, maxChoosableInteger: 'int', desiredTotal: 'int') -> 'bool':
        sums = sum(range(maxChoosableInteger+1))
        if sums < desiredTotal:
            return False
        nums = list(range(1, maxChoosableInteger+1))
        memo = {}
        return self.recurHelper(nums, desiredTotal, memo)

    def recurHelper(self, nums, desiredTotal, memo):
        hash = str(nums)
        if hash in memo:
            return memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.recurHelper(nums[:i] + nums[i+1:], desiredTotal-nums[i], memo):
                memo[hash] = True
                return True
        return False

