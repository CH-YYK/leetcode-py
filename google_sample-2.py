"""
This problem has been posted on Leetcode: Patching numbers
"""


class Solution:
    def minPatches(self, nums, n):
        miss = 1
        initial = len(nums)
        i = 0
        while miss <= n:
            if i > len(nums)-1:
                nums.insert(i, miss)
                miss += miss
            elif nums[i] > miss:
                nums.insert(i, miss)
                miss += miss
            else:
                miss += nums[i]
            i += 1
        return len(nums) - initial

class Solution:
    def minPatches(self, nums, n):
        miss = 1
        i = 0
        res = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                res += 1
                miss += miss
        return res

if __name__ == '__main__':
    nums = [1, 2, 4, 13, 43]
    n = 100
    print(Solution().pathingNumbers(nums, n))
