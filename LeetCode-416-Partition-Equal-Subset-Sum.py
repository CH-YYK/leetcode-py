class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        return self.recurSubset(0, nums, subsetSum, sums)

    def recurSubset(self, index, nums, subsetSum, sums):
        if index <= len(nums) and subsetSum == 0:
            return True
        elif index == len(nums):
            return False
        elif subsetSum < 0:
            return False

        res1 = self.recurSubset(index + 1, nums, subsetSum, sums)
        res2 = self.recurSubset(index + 1, nums, subsetSum - nums[index], sums)
        return res1 or res2

    def canPartition2(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        memo = {}
        return self.recurSubset2(0, nums, subsetSum, sums, memo)

    def recurSubset2(self, index, nums, subsetSum, sums, memo):
        if index <= len(nums) and subsetSum == 0:
            return True
        elif index == len(nums):
            return False
        elif subsetSum < 0:
            return False
        tmp = str(index) + "|" + str(subsetSum)
        if tmp in memo:
            return memo[tmp]
        res1 = self.recurSubset2(index + 1, nums, subsetSum, sums, memo)
        res2 = self.recurSubset2(index + 1, nums, subsetSum - nums[index], sums, memo)
        memo[tmp] = res1 or res2
        return memo[tmp]

    def canPartition3(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        memo = [[False for i in range(subsetSum)] for _ in range(len(nums))]
        return self.recurSubset3(0, nums, subsetSum, subsetSum, memo)

    def recurSubset3(self, index, nums, subsetSum, sums, memo):
        if index <= len(nums) and subsetSum == 0:
            return True
        elif index == len(nums):
            return False
        elif subsetSum < 0:
            return False
        if memo[index][sums - subsetSum - 1]:
            return memo[index][sums-subsetSum-1]
        res1 = self.recurSubset3(index + 1, nums, subsetSum, sums, memo)
        res2 = self.recurSubset3(index + 1, nums, subsetSum - nums[index], sums, memo)
        memo[index][sums - subsetSum - 1] = res1 or res2
        return memo[index][sums - subsetSum - 1]



