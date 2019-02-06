class Solution:
    def findOddFreqNumber(self, nums):
        """
        O(N) in time, O(N) in space
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        return [(i, j) for i, j in hashmap.items() if j % 2 != 0][0][1]

    def findOddFreqNumber2(self, nums):
        """
        O(N) in time, O(1) in space
        """
        hashmap = {}
        for num in nums:
            if num in hashmap:
                del hashmap[num]
            else:
                hashmap[num] = True
        return hashmap.popitem()[1]

if __name__ == '__main__':
    nums = [1,1, 2,2, 3,3,3]
    print(Solution().findOddFreqNumber2(nums))