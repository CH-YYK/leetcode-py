class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        nums.sort()
        res1, res2 = 0, nums[0]

        for i in range(0, len(nums), 2):
            res1 += nums[i]

        for i in range(1, len(nums) - 1, 2):
            res2 += nums[i]

        return max(res1, res2)

    def arrayPairSum2(self, nums: 'List[int]') -> 'int':
        nums.sort()
        res = 0
        for i in range(0, len(nums)-1, 2):
            res += nums[i]
        return res