import heapq
import sys
class Solution(object):
    def findMax(self, nums):
        heapq.heapify(nums)
        res = [nums[0]]
        while nums:
            curr = heapq.heappop(nums)
            while res and curr[1] > res[-1][1]:
                res.pop()
            res.append(curr)
        return res

if __name__ == "__main__":
    num = int(input())
    nums = []
    for i in range(num):
        nums.append([int(i) for i in sys.stdin.readline().split()])
    ans = Solution().findMax(nums)

    for i in ans:
        print("{} {}".format(i[0], i[1]))
