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

    def canPartition4(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        memo = {}
        return self.recurSubset4(0, nums, subsetSum, memo)

    def recurSubset4(self, index, nums, subsetSum, memo):
        if index <= len(nums) and subsetSum == 0:
            return True
        elif index == len(nums):
            return False
        elif subsetSum < 0:
            return False
        tmp = (index, subsetSum)
        if tmp in memo:
            return memo[tmp]
        if subsetSum >= nums[index]:
            res = self.recurSubset4(index + 1, nums, subsetSum - nums[index], memo)
            if res:
                memo[tmp] = True
        else:
            res = self.recurSubset4(index + 1, nums, subsetSum, memo)
            memo[tmp] = res
        return memo[tmp]

    def canPartition3(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        memo = [[False for i in range(subsetSum + 1)] for _ in range(len(nums))]
        memo[0][0] = True
        return self.recurSubset3(0, nums, 0, subsetSum, memo)

    def recurSubset3(self, index, nums, subsetSum, sums, memo):
        if index <= len(nums) and subsetSum == sums:
            return True
        elif index == len(nums):
            return False
        elif subsetSum > sums:
            return False
        if memo[index][subsetSum]:
            return memo[index][subsetSum]
        res1 = self.recurSubset3(index + 1, nums, subsetSum, sums, memo)
        res2 = self.recurSubset3(index + 1, nums, subsetSum + nums[index], sums, memo)
        memo[index][subsetSum] = res1 or res2
        return memo[index][subsetSum]

    def canPartition5(self, nums: 'List[int]') -> 'bool':
        """
        find subsets, find out whether the sum of the subset is half to total sum
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        subsetSum = sums // 2
        memo = [[False for i in range(subsetSum + 1)] for _ in range(len(nums) + 1)]
        memo[0][0] = True

        for i in range(1, len(nums) + 1):
            memo[i][0] = True

        for j in range(1, subsetSum + 1):
            memo[0][j] = False

        for i in range(1, len(nums) + 1):
            for j in range(1, subsetSum + 1):
                memo[i][j] = memo[i-1][j]
                if j >= nums[i-1]:
                    memo[i][j] = memo[i][j] or memo[i-1][j-nums[i-1]]
        return memo[len(nums)][subsetSum]






