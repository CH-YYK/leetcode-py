class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        if len(nums) < 2:
            return False
        hashmap = {0:-1}
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if k != 0:
                Sum %= k
            prev = hashmap.get(Sum, None)
            if prev is not None:
                if i -  prev > 1:
                    return True
            else:
                hashmap[Sum] = i
        return False