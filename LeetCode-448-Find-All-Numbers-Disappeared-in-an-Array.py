"""
Literally, the set should be same as index set. I.e each index+1 should have appeared only once
in the set.

Go over the set and set the value whose index corresponding the current value to negative.

Since duplicated values only appeared twice, so only duplicated values will generate positive numbers
at the corresponding indices.
"""


class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for i in range(len(nums)):
            if nums[i] > 0:
                index = nums[i] - 1  # index represented by values
                nums[index] = -nums[index] if nums[index] > 0 else nums[index]

        res = []
        for i in range(len(nums)):
            if nums[i] < 0:
                res.append(i+1)
        return res