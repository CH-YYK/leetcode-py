class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashFreq = {}
        hashRequest = {}
        for i in nums:
            hashFreq[i] = hashFreq.get(i, 0) + 1
        for i in nums:
            if hashFreq.get(i, 0) == 0:
                continue
            elif hashRequest.get(i, 0) > 0:
                hashRequest[i] -= 1
                hashRequest[i+1] = hashRequest.get(i+1, 0) + 1
            elif hashFreq.get(i+1, 0) > 0 and hashFreq.get(i+2, 0) > 0:
                hashFreq[i+1] = hashFreq.get(i+1, 0) - 1
                hashFreq[i+2] = hashFreq.get(i+2, 0) - 1
                hashRequest[i+3] = hashRequest.get(i+3, 0) + 1
            else:
                return False
            hashFreq[i] -= 1
        return True

if __name__ == '__main__':
    nums = [1,2,3,3,4,4,5,5]
    print(Solution().isPossible(nums))