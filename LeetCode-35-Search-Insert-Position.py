class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))