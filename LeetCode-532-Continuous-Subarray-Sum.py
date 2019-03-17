class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        if len(nums) < 2:
            return False
        if k == 0:
            return True if sum(nums) == 0 else False
        hashmap = {}
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if i > 0 and Sum % k == 0:
                return True
            if Sum % k in hashmap:
                return True if i - hashmap[Sum % k] > 1 else
            else:
                hashmap[Sum % k] = i
        return False