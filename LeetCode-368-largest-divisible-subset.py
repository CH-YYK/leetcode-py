class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        hashset = {}
        hashset[0] = [nums[0]]
        sizeSubset = [0] * len(nums)
        sizeSubset[0] = 1
        for i in range(1, len(nums)):
            maxIndex = i
            maxLength = 1
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0:
                    tmpLength = 1 + sizeSubset[j]
                    if tmpLength > maxLength:
                        maxIndex = j
                        maxLength = tmpLength
            sizeSubset[i] = maxLength
            if maxIndex < i:
                hashset[i] = hashset[maxIndex] + hashset.get(i, [nums[i]])
            else:
                hashset[i] = [nums[i]]
        maxIndex = 0
        maxLength = 0
        for i in range(len(sizeSubset)):
            if sizeSubset[i] > maxLength:
                maxLength = sizeSubset[i]
                maxIndex = i
        return hashset[maxIndex]


if __name__ == '__main__':
    nums = [3,4,8,16]
    print(Solution().largestDivisibleSubset(nums))
