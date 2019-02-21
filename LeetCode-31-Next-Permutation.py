class Solution:
    def nextPermutation(self, nums):

        k = 0
        while k < len(nums) - 1:
            if nums[k] < nums[k+1]:
                break
            else:
                k += 1

        l = len(nums) - 1
        while nums[l] < nums[k]:
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]

        nums[k+1:] = nums[k+1:][::-1]
        return nums