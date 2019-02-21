class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        # deleting values from nums
        if len(nums) < 2:
            return len(nums)
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                del nums[j]
            i += 1
        return len(nums)

    def removeDuplicates2(self, nums: 'List[int]') -> 'int':
        # modifying values in the nums
        if len(nums) < 2:
            return len(nums)
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1




if __name__ == '__main__':
    print(Solution().removeDuplicates([1,2,2,3]))