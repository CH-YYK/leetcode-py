class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for start in range(len(nums)):
            Sum = 0
            for end in range(start, len(nums)):
                Sum += nums[end]
                if Sum == k:
                    count += 1
        return count

    def subarraySum_hash(self, nums, k):
        cumulativeSum = {}
        Sum = 0
        count = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum == k:
                count += 1
            if Sum - k in cumulativeSum:
                count += cumulativeSum[Sum-k]

            if Sum in cumulativeSum:
                cumulativeSum[Sum] += 1
            else:
                cumulativeSum[Sum] = 1
        return count

if __name__ == '__main__':
    nums = [1, 1, 1]
    print(Solution().subarraySum_hash(nums, 2))