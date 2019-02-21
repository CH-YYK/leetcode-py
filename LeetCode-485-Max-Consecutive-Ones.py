class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        maxSum = 0
        Sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxSum = max(maxSum, Sum)
                Sum = 0
            else:
                Sum += 1
        return max(maxSum, Sum)

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))